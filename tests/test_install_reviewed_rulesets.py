"""No-network, adversarial ruleset installation tests; NEVER create live rules."""
import copy
import io
import json
from pathlib import Path
from unittest.mock import MagicMock, patch
import unittest

from scripts import install_reviewed_rulesets as installer


ROOT = Path(__file__).resolve().parents[1]
POLICIES = installer.load_policies(ROOT / "ops" / "rulesets")
MAIN = "61e60134a17d903e81a9350413924261340578b3"
REPO = installer.REPOSITORY


class Fake:
    def __init__(self, installed=()):
        self.installed = set(installed)
        self.calls = []
        self.posts = []
        self.admin = True
        self.main_sha = MAIN
        self.main_protected_override = None
        self.moves_on_second_main_get = False
        self.branch_reads = 0
        self.bad_check = None
        self.bad_source = False
        self.extra_ruleset = False
        self.fail_on_main_post = False

    def _detail(self, name):
        d = copy.deepcopy(POLICIES["main.json" if name == "main" else "branch-archive-tags.json"])
        d["id"] = 21 if name == "main" else 11
        d["source"] = "different/owner" if self.bad_source else REPO
        return d

    def get(self, path):
        self.calls.append(("GET", path))
        if path == f"/repos/{REPO}":
            return {"default_branch": "main", "permissions": {"admin": self.admin}}
        if path == f"/repos/{REPO}/branches/main":
            self.branch_reads += 1
            sha = ("f" * 40 if self.moves_on_second_main_get
                   and self.branch_reads >= 2 else self.main_sha)
            protected = "main" in self.installed
            if self.main_protected_override is not None:
                protected = self.main_protected_override
            return {"commit": {"sha": sha}, "protected": protected}
        if path == f"/repos/{REPO}/commits/{MAIN}/check-runs?per_page=100":
            checks = [
                {"name": name, "head_sha": MAIN, "status": "completed",
                 "conclusion": "success", "app": {"id": 15368, "slug": "github-actions"}}
                for name in sorted(installer.policy.EXPECTED_CHECKS)
            ]
            if self.bad_check == "missing":
                checks.pop()
            if self.bad_check == "failed":
                checks[0]["conclusion"] = "failure"
            if self.bad_check == "wrong_app":
                checks[0]["app"]["id"] = 42
            if self.bad_check == "duplicate":
                checks.append(copy.deepcopy(checks[0]))
            return {"total_count": len(checks), "check_runs": checks}
        if path.startswith(f"/repos/{REPO}/rulesets?"):
            rows = [
                {"id": self._detail(k)["id"], "name": self._detail(k)["name"],
                 "target": self._detail(k)["target"], "source": self._detail(k)["source"]}
                for k in sorted(self.installed)
            ]
            if self.extra_ruleset:
                rows.append({"id": 55, "name": "surprise", "target": "branch",
                             "source": REPO})
            page = int(path.rsplit("page=", 1)[-1])
            return rows if page == 1 else []
        if path == f"/repos/{REPO}/rulesets/11":
            return self._detail("archive")
        if path == f"/repos/{REPO}/rulesets/21":
            return self._detail("main")
        raise AssertionError("unexpected GET API route " + path)

    def post(self, path, payload):
        self.calls.append(("POST", path))
        if path != f"/repos/{REPO}/rulesets":
            raise AssertionError("unexpected ruleset destination")
        if payload.get("name") == POLICIES["branch-archive-tags.json"]["name"]:
            name, ident = "archive", 11
        elif payload.get("name") == POLICIES["main.json"]["name"]:
            name, ident = "main", 21
        else:
            raise AssertionError("unreviewed POST payload")
        self.posts.append(name)
        if name == "main" and self.fail_on_main_post:
            raise installer.InstallationError("ambiguous simulated network failure")
        if name in self.installed:
            raise AssertionError("duplicate POST to installed policy")
        self.installed.add(name)
        return {"id": ident}


class ReviewedRulesetInstallerTests(unittest.TestCase):
    def test_policy_git_blobs_and_minimum_safeguards_are_pinned(self):
        self.assertEqual(set(POLICIES), set(installer.PINNED_POLICY_BLOBS))
        self.assertEqual(POLICIES["main.json"]["bypass_actors"], [])
        self.assertEqual(POLICIES["branch-archive-tags.json"]["bypass_actors"], [])
        with patch.object(installer, "load_research_json_file",
                          side_effect=AssertionError("unchanged payload still needs parsing")):
            with self.assertRaises(AssertionError):
                installer.load_policies(ROOT / "ops" / "rulesets")

    def test_default_preflight_performs_no_mutation(self):
        fake = Fake()
        result = installer.install(fake, MAIN, POLICIES)
        self.assertEqual(result["mode"], "preflight_only")
        self.assertEqual(result["rulesets"], {})
        self.assertEqual(fake.posts, [])
        self.assertTrue(all(kind == "GET" for kind, _ in fake.calls))
        self.assertFalse(result["negative_enforcement_tests_verified"])
        self.assertFalse(result["independent_review_verified"])

    def test_complete_two_stage_install_and_safe_repeat(self):
        fake = Fake()
        answer = installer.install(fake, MAIN, POLICIES, apply=True,
                                   review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(fake.posts, ["archive", "main"])
        self.assertEqual(answer["mode"], "installed_configuration_only")
        self.assertTrue(answer["main_protected"])
        self.assertEqual(answer["rulesets"], {"archive": 11, "main": 21})
        self.assertFalse(answer["negative_enforcement_tests_verified"])
        self.assertFalse(answer["independent_review_verified"])
        second = installer.install(fake, MAIN, POLICIES, apply=True,
                                   review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(second["mode"], "already_installed")
        self.assertFalse(second["write_attempted"])
        self.assertEqual(fake.posts, ["archive", "main"])

    def test_existing_complete_configuration_is_read_only_even_with_apply(self):
        fake = Fake(("archive", "main"))
        result = installer.install(fake, MAIN, POLICIES, apply=True,
                                   review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(result["mode"], "already_installed")
        self.assertEqual(fake.posts, [])

    def test_resume_partial_requires_separate_explicit_flag(self):
        fake = Fake(("archive",))
        self.assertEqual(installer.install(fake, MAIN, POLICIES)["mode"], "preflight_only")
        with self.assertRaisesRegex(installer.InstallationError, "resume"):
            installer.install(fake, MAIN, POLICIES, apply=True,
                              review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(fake.posts, [])
        result = installer.install(fake, MAIN, POLICIES, apply=True,
                                   resume=True, review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(result["rulesets"], {"archive": 11, "main": 21})
        self.assertEqual(fake.posts, ["main"])

    def test_ambiguous_main_post_preserves_archive_and_never_auto_retries(self):
        fake = Fake()
        fake.fail_on_main_post = True
        with self.assertRaisesRegex(installer.InstallationError, "ambiguous"):
            installer.install(fake, MAIN, POLICIES, apply=True,
                              review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(fake.posts, ["archive", "main"])
        self.assertEqual(fake.installed, {"archive"})
        with self.assertRaisesRegex(installer.InstallationError, "resume"):
            installer.install(fake, MAIN, POLICIES, apply=True,
                              review_ref="SECURITY-APPROVAL-123")
        self.assertEqual(fake.posts, ["archive", "main"])

    def test_unreviewed_ref_or_invalid_sha_never_writes(self):
        for ref in (None, "", "a" * 201, "has spaces", "\nPRIVATE"):
            fake = Fake()
            with self.subTest(ref=ref), self.assertRaises(installer.InstallationError):
                installer.install(fake, MAIN, POLICIES, apply=True, review_ref=ref)
            self.assertEqual(fake.calls, [])
        fake = Fake()
        with self.assertRaises(installer.InstallationError):
            installer.install(fake, "main", POLICIES)
        self.assertFalse(fake.posts)

    def test_preflight_rejects_missing_bad_or_duplicated_ci(self):
        for kind in ("missing", "failed", "wrong_app", "duplicate"):
            fake = Fake()
            fake.bad_check = kind
            with self.subTest(kind=kind), self.assertRaises(installer.InstallationError):
                installer.install(fake, MAIN, POLICIES, apply=True,
                                  review_ref="SECURITY-APPROVAL-123")
            self.assertFalse(fake.posts)

    def test_admin_and_original_main_are_mandatory(self):
        for variant in ("not_admin", "moved_sha", "moved_after_preflight"):
            fake = Fake()
            if variant == "not_admin":
                fake.admin = False
            elif variant == "moved_sha":
                fake.main_sha = "a" * 40
            else:
                fake.moves_on_second_main_get = True
            with self.subTest(variant=variant), self.assertRaises(installer.InstallationError):
                installer.install(fake, MAIN, POLICIES, apply=True,
                                  review_ref="SECURITY-APPROVAL-123")
            self.assertEqual(fake.posts, [])

    def test_unexpected_inherited_or_main_only_ruleset_block_all_posts(self):
        for variant in ("inherited", "unrelated", "main_only", "unexplained_protection"):
            fake = Fake()
            if variant == "inherited":
                fake.installed.add("archive")
                fake.bad_source = True
            elif variant == "unrelated":
                fake.extra_ruleset = True
            elif variant == "main_only":
                fake.installed.add("main")
            else:
                fake.main_protected_override = True
            with self.subTest(variant=variant):
                if variant == "unexplained_protection":
                    # A protected main with no identified rules is a legacy
                    # protection state requiring human reconciliation.
                    with self.assertRaises(installer.InstallationError):
                        installer.install(fake, MAIN, POLICIES, apply=True,
                                          review_ref="SECURITY-APPROVAL-123")
                else:
                    with self.assertRaises(installer.InstallationError):
                        installer.install(fake, MAIN, POLICIES, apply=True,
                                          review_ref="SECURITY-APPROVAL-123")
            self.assertFalse(fake.posts)

    def test_http_client_fixed_route_non_forwarded_token_and_no_redirect(self):
        fake_response = MagicMock()
        fake_response.status = 201
        fake_response.read.return_value = b'{"id":17}'
        transport = MagicMock()
        transport.open.return_value.__enter__.return_value = fake_response
        with patch.object(installer, "build_opener", return_value=transport) as created:
            client = installer.GitHub(token="PRIVATE_ADMIN_TOKEN")
            self.assertEqual(
                client.post(f"/repos/{REPO}/rulesets", POLICIES["main.json"]), {"id": 17})
        req = transport.open.call_args.args[0]
        self.assertNotIn("Authorization", req.headers)
        self.assertEqual(req.unredirected_hdrs["Authorization"], "Bearer PRIVATE_ADMIN_TOKEN")
        self.assertEqual(req.get_method(), "POST")
        guard = created.call_args.args[0]
        self.assertIsNone(guard.redirect_request(
            req, None, 307, "redirect", {}, "https://malicious.example/upload"))
        with self.assertRaises(installer.InstallationError):
            client.post(f"/repos/{REPO}/branches/main", {})
        with self.assertRaises(installer.InstallationError):
            installer.GitHub().post(f"/repos/{REPO}/rulesets", {})


if __name__ == "__main__":
    unittest.main()
