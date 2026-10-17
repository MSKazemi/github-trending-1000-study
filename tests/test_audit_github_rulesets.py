"""Synthetic, offline negative verification of GitHub ruleset readback."""
import copy
import io
import json
from pathlib import Path
import tempfile
import traceback
import unittest
from unittest.mock import patch

from scripts import audit_github_rulesets as verifier

ROOT = Path(__file__).resolve().parents[1]
OPS = ROOT / "ops" / "rulesets"
REPO = "MSKazemi/github-trending-1000-study"
BASE = "1e656cfcbceb4995467280b796e77e870c6c5f39"


def payloads():
    return (json.loads((OPS / "main.json").read_text(encoding="utf-8")),
            json.loads((OPS / "branch-archive-tags.json").read_text(encoding="utf-8")))


def fake_get(main, archive, *, protected=True, head=BASE, rows=None):
    details = {
        23: dict(copy.deepcopy(main), id=23, source=REPO),
        17: dict(copy.deepcopy(archive), id=17, source=REPO),
    }
    if rows is None:
        rows = [
            {"id": 23, "name": main["name"], "target": "branch", "source": REPO},
            {"id": 17, "name": archive["name"], "target": "tag", "source": REPO},
        ]
    calls = []
    def get(path):
        calls.append(path)
        if path == f"/repos/{REPO}/branches/main":
            return {"commit": {"sha": head}, "protected": protected}
        if path.startswith(f"/repos/{REPO}/rulesets?"):
            page = int(path.rsplit("page=", 1)[-1])
            return copy.deepcopy(rows) if page == 1 else []
        if path.startswith(f"/repos/{REPO}/rulesets/"):
            rid = int(path.rsplit("/", 1)[-1])
            return copy.deepcopy(details[rid])
        raise AssertionError("unexpected/non-GET route")
    return get, details, calls


class ReadonlyRulesetReadbackTests(unittest.TestCase):
    def setUp(self):
        self.expected_main, self.expected_archive = payloads()

    def audit(self, getter, main=None, archive=None, *, sha=BASE):
        return verifier.audit(REPO, sha,
                              main if main is not None else self.expected_main,
                              archive if archive is not None else self.expected_archive,
                              getter)

    def test_current_unprotected_empty_rulesets_fails_closed_not_approved(self):
        get, _, calls = fake_get(self.expected_main, self.expected_archive,
                                 protected=False, rows=[])
        report = self.audit(get)
        self.assertEqual(report["configuration_status"], "absent_or_partial")
        self.assertFalse(report["main_protected"])
        self.assertFalse(report["negative_enforcement_tests_verified"])
        self.assertFalse(report["independent_review_verified"])
        self.assertTrue(report["read_only"])
        self.assertEqual(len(calls), 4)

    def test_active_exact_readback_is_only_configuration_not_actual_enforcement(self):
        get, _, calls = fake_get(self.expected_main, self.expected_archive)
        report = self.audit(get)
        self.assertEqual(report["configuration_status"],
                         "matching_rulesets_observed_not_enforcement_proof")
        self.assertEqual((report["main_ruleset_id"], report["archive_ruleset_id"]), (23, 17))
        self.assertFalse(report["negative_enforcement_tests_verified"])
        self.assertFalse(report["independent_review_verified"])
        self.assertEqual(set(report["required_checks"]), verifier.EXPECTED_CHECKS)
        self.assertEqual(len(calls), 6)

    def test_main_moving_during_ruleset_detail_readback_is_detected(self):
        getter, _, calls = fake_get(self.expected_main, self.expected_archive)
        state = {"main_reads": 0}
        def changing(path):
            if path == f"/repos/{REPO}/branches/main":
                state["main_reads"] += 1
                if state["main_reads"] == 2:
                    return {"commit": {"sha": "a" * 40}, "protected": True}
            return getter(path)
        with self.assertRaisesRegex(verifier.RulesetAuditError, "main or protection changed"):
            self.audit(changing)
        self.assertEqual(state["main_reads"], 2)
        # The wrapped second main GET is intercepted; the initial main, list,
        # and two detail reads are still recorded by the mock provider.
        self.assertEqual(len(calls), 4)

    def test_ruleset_list_movement_during_readback_is_detected(self):
        getter, _, calls = fake_get(self.expected_main, self.expected_archive)
        state = {"lists": 0}
        def changing(path):
            if "/rulesets?" in path:
                state["lists"] += 1
                if state["lists"] == 2:
                    return []
            return getter(path)
        with self.assertRaisesRegex(verifier.RulesetAuditError, "inventory changed"):
            self.audit(changing)
        self.assertEqual(state["lists"], 2)

    def test_authenticated_readback_rejects_redirect_and_does_not_forward_token(self):
        from unittest.mock import MagicMock
        opened = MagicMock()
        opened.__enter__.return_value.read.return_value = b'[]'
        gateway = MagicMock()
        gateway.open.return_value = opened
        with patch.dict("os.environ", {"GH_TOKEN": "PRIVATE_NO_NETWORK_TOKEN"},
                        clear=True), patch.object(verifier, "build_opener",
                                                  return_value=gateway) as opener:
            self.assertEqual(verifier._get(f"/repos/{REPO}/rulesets"), [])
        request = gateway.open.call_args.args[0]
        self.assertNotIn("Authorization", request.headers)
        self.assertEqual(request.unredirected_hdrs["Authorization"],
                         "Bearer PRIVATE_NO_NETWORK_TOKEN")
        redirect_guard = opener.call_args.args[0]
        self.assertIsNone(redirect_guard.redirect_request(request, None, 302,
                          "redirect", {}, "https://malicious.example/steal"))

    def test_server_can_return_rules_and_checks_in_a_different_order(self):
        get, details, _ = fake_get(self.expected_main, self.expected_archive)
        details[23]["rules"].reverse()
        details[23]["rules"][0]["parameters"]["required_status_checks"].reverse()
        details[17]["rules"].reverse()
        self.assertIn("matching_rulesets", self.audit(get)["configuration_status"])

    def test_detects_every_critical_server_side_weakened_rule(self):
        changes = (
            (23, lambda x: x.update(enforcement="evaluate")),
            (23, lambda x: x["bypass_actors"].append({"actor_id": 7})),
            (23, lambda x: x["rules"].pop()),
            (23, lambda x: x["rules"][2]["parameters"].update(required_approving_review_count=0)),
            (23, lambda x: x["rules"][2]["parameters"].update(dismiss_stale_reviews_on_push=False)),
            (23, lambda x: x["rules"][3]["parameters"].update(strict_required_status_checks_policy=False)),
            (23, lambda x: x["rules"][3]["parameters"]["required_status_checks"].pop()),
            (23, lambda x: x["rules"][3]["parameters"]["required_status_checks"][0].update(integration_id=6)),
            (17, lambda x: x["rules"].pop()),
            (17, lambda x: x["conditions"]["ref_name"].update(include=["refs/tags/branch-archive/*"])),
            (17, lambda x: x["bypass_actors"].append({"actor_id": 7})),
        )
        for index, (rid, mutate) in enumerate(changes):
            with self.subTest(case=index):
                get, details, _ = fake_get(self.expected_main, self.expected_archive)
                mutate(details[rid])
                with self.assertRaises(verifier.RulesetAuditError):
                    self.audit(get)

    def test_weakened_checked_in_intent_cannot_make_weakened_live_pass(self):
        main = copy.deepcopy(self.expected_main)
        main["rules"][2]["parameters"]["required_approving_review_count"] = 0
        get, _, calls = fake_get(main, self.expected_archive)
        with self.assertRaisesRegex(verifier.RulesetAuditError, "weakened"):
            self.audit(get, main=main)
        self.assertEqual(calls, [])

    def test_base_sha_movement_fails_before_trusting_live_readback(self):
        get, _, calls = fake_get(self.expected_main, self.expected_archive, head="a" * 40)
        with self.assertRaisesRegex(verifier.RulesetAuditError, "main moved"):
            self.audit(get)
        self.assertEqual(len(calls), 1)

    def test_partial_only_one_ruleset_cannot_report_installed(self):
        row = {"id": 23, "name": self.expected_main["name"], "target": "branch"}
        get, _, _ = fake_get(self.expected_main, self.expected_archive, rows=[row])
        report = self.audit(get)
        self.assertEqual(report["configuration_status"], "absent_or_partial")
        self.assertEqual(report["matched_ruleset_names"], ["main"])

    def test_duplicate_ids_names_and_inherited_rulesets_rejected(self):
        base_rows = [
            {"id": 23, "name": self.expected_main["name"], "target": "branch", "source": REPO},
            {"id": 17, "name": self.expected_archive["name"], "target": "tag", "source": REPO},
        ]
        for alteration in (
            base_rows + [dict(base_rows[0])],
            base_rows + [dict(base_rows[0], id=42)],
            [dict(base_rows[0], source="another/owner"), base_rows[1]],
            [dict(base_rows[0], target="tag"), base_rows[1]],
        ):
            with self.subTest(rows=alteration):
                get, _, _ = fake_get(self.expected_main, self.expected_archive, rows=alteration)
                with self.assertRaises(verifier.RulesetAuditError):
                    self.audit(get)

    def test_invalid_repo_or_unreviewed_sha_never_calls_network(self):
        def never_get(path):
            self.fail("untrusted route reached network")
        for repo in ("../fake", "owner/..", "foo/bar/extra", None):
            with self.subTest(repo=repo), self.assertRaises(verifier.RulesetAuditError):
                verifier.audit(repo, BASE, self.expected_main, self.expected_archive, never_get)
        for sha in ("main", "deadbeef", "a" * 39, None):
            with self.subTest(sha=sha), self.assertRaises(verifier.RulesetAuditError):
                verifier.audit(REPO, sha, self.expected_main, self.expected_archive, never_get)

    def test_negative_untrusted_duplicate_rule_type_not_accepted(self):
        get, details, _ = fake_get(self.expected_main, self.expected_archive)
        details[23]["rules"].append(copy.deepcopy(details[23]["rules"][0]))
        with self.assertRaisesRegex(verifier.RulesetAuditError, "duplicate rule"):
            self.audit(get)

    def test_private_invalid_payload_or_live_error_does_not_chain_system_exit(self):
        # This audit can be run in a privileged admin session. Diagnostics
        # must not leak local payload paths or raw remote response text even
        # through in-process SystemExit.__context__.
        marker = "PRIVATE_RULESET_PAYLOAD_OR_TOKEN_20261017"
        for failing_input in ("payload", "live"):
            with self.subTest(failing_input=failing_input):
                main_payload, archive_payload = payloads()
                with patch.object(verifier, "load_research_json_file") as load, \
                     patch.object(verifier, "_get") as remote, \
                     patch("sys.stderr", new_callable=io.StringIO) as errors:
                    if failing_input == "payload":
                        load.side_effect = ValueError(marker)
                    else:
                        load.side_effect = [main_payload, archive_payload]
                        remote.side_effect = ValueError(marker)
                    try:
                        verifier.main([
                            "--repo", REPO, "--expected-main-sha", BASE,
                            "--payload-dir", str(OPS)])
                    except SystemExit as exc:
                        self.assertEqual(exc.code, 2)
                        self.assertIsNone(exc.__cause__)
                        self.assertIsNone(exc.__context__)
                        self.assertNotIn(marker, errors.getvalue())
                        self.assertNotIn(marker, "".join(traceback.format_exception(exc)))
                    else:
                        self.fail("unsafe audit input must fail closed")

    def test_cli_returns_nonzero_for_missing_protection_without_claiming_approval(self):
        get, _, _ = fake_get(self.expected_main, self.expected_archive,
                              protected=False, rows=[])
        with patch.object(verifier, "_get", side_effect=get), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            result = verifier.main(["--repo", REPO, "--expected-main-sha", BASE,
                                    "--payload-dir", str(OPS)])
        self.assertEqual(result, 2)
        report = json.loads(output.getvalue())
        self.assertEqual(report["configuration_status"], "absent_or_partial")
        self.assertFalse(report["negative_enforcement_tests_verified"])


if __name__ == "__main__":
    unittest.main()
