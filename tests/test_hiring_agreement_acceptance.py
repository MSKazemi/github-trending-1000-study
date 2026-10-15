"""Independent fictional CLI acceptance for ISSUE-223-HIRING-AGREEMENT-OFFLINE-V1.

Requirements frozen before candidate implementation inspection. These tests neither
authenticate reviewers nor supply real research observations or source permission.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
THEMES = (
    "agent_runtime", "context_memory", "evaluation_quality", "rl_training",
    "sandbox_security", "enterprise_integrations", "inference_efficiency",
    "developer_reuse", "platform_infrastructure", "agent_operations", "other",
)
SELECTED = ("S01", "S02", "S03", "S04", "S05", "S06", "S09", "S10", "S12")


class HiringAgreementIndependentAcceptance(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="independent-fictional-hiring-")
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        self.frame_path = ROOT / "references/hiring_agreement/pilot_frame_v1.json"
        self.frame = json.loads(self.frame_path.read_text())
        self.a = self.review("fictional_A")
        self.b = self.review("fictional_B")

    def cli(self, *args, success=True):
        result = subprocess.run(
            [sys.executable, "-m", "trending_study.hiring_agreement", *map(str, args)],
            cwd=ROOT, text=True, capture_output=True, timeout=8,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def write(self, name, obj):
        path = self.dir / name
        path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
        return path

    def sha(self, path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def fingerprint(self, value):
        return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=True, allow_nan=False).encode()).hexdigest()

    def review(self, reviewer):
        return {
            "schema_version": "hiring-223-v1",
            "sample_id": "hiring-223-direct-read-candidates-2026-10-14",
            "frame_sha256": self.fingerprint(self.frame), "dataset_kind": "synthetic",
            "reviewer_id": reviewer, "reviewed_at_utc": "2026-10-13T12:00:00Z",
            "human_attested": False,
            "ratings": [{"item_id": item, "source_access": "read",
                         "source_checked_at_utc": "2026-10-13T11:00:00Z",
                         "themes": dict.fromkeys(THEMES, "absent"),
                         "primary_task": "uncertain", "evidence_ref": "fictional_note",
                         "counterinterpretation": "ambiguous_text"} for item in SELECTED],
        }

    def analyze(self, a=None, b=None, adjudication=None, success=True, output=None):
        a_path = self.write("a.json", self.a if a is None else a)
        b_path = self.write("b.json", self.b if b is None else b)
        output = output or self.dir / "result.json"
        args = ["analyze", "--frame", self.frame_path, "--coder-a", a_path,
                "--coder-b", b_path, "--output", output]
        if adjudication is not None:
            args += ["--adjudication", self.write("c.json", adjudication)]
        self.cli(*args, success=success)
        if success:
            return json.loads(output.read_text())
        self.assertFalse(output.exists())

    def adjudication(self, decisions):
        return {"schema_version": "hiring-223-v1", "sample_id": self.a["sample_id"],
                "frame_sha256": self.fingerprint(self.frame),
                "review_a_sha256": self.fingerprint(self.a),
                "review_b_sha256": self.fingerprint(self.b), "dataset_kind": "synthetic",
                "adjudicator_id": "fictional_C", "adjudicated_at_utc": "2026-10-13T13:00:00Z",
                "predictions_unseen_attested": True, "decisions": decisions}

    def inaccessible(self, row):
        row.update(source_access="unavailable", primary_task="not_reviewable",
                   themes=dict.fromkeys(THEMES, "not_reviewable"),
                   counterinterpretation="access_failure")

    def test_frame_denominator_source_status_and_selected_identity(self):
        result = json.loads(self.cli("verify-frame", "--frame", self.frame_path).stdout)
        self.assertEqual(result["source_frame_n"], 24)
        self.assertEqual(result["selected_n"], 9)
        self.assertEqual(result["raw_frame_sha256"], self.sha(self.frame_path))
        self.assertEqual(result["status_counts"], {"selected_pending_recheck": 9,
                         "index_text_only": 13, "identity_hold": 1, "direct_access_unconfirmed": 1})
        self.assertEqual(tuple(x["item_id"] for x in self.frame["items"] if x["selected"]), SELECTED)
        for source in self.frame["sources"]:
            self.assertEqual(source["sha256"], self.sha(ROOT / source["path"]))

    def test_blind_packets_omit_analyst_hypotheses_and_remain_unrated(self):
        out = self.dir / "packet.json"
        self.cli("pack", "--frame", self.frame_path, "--reviewer-id", "fictional_A", "--output", out)
        packet = json.loads(out.read_text())
        self.assertEqual([x["item_id"] for x in packet["ratings"]], list(SELECTED))
        self.assertEqual(packet["frame_sha256"], self.fingerprint(self.frame))
        self.assertFalse(packet["human_attested"])
        self.assertIsNone(packet["reviewed_at_utc"])
        for row in packet["ratings"]:
            self.assertEqual(row["themes"], dict.fromkeys(THEMES, "not_reviewable"))
        for forbidden in ("theme_hypotheses", "theme_codes", "source_url", "employer", "roadmap"):
            self.assertNotIn(forbidden, out.read_text())

    def test_known_per_theme_math_preserves_abstention_disagreement(self):
        left = ["present", "present", "present", "absent", "absent", "absent",
                "uncertain", "not_reviewable", "absent"]
        right = ["present", "present", "absent", "present", "present", "absent",
                 "absent", "not_reviewable", "uncertain"]
        for i, (a, b) in enumerate(zip(left, right)):
            if a == "not_reviewable":
                self.inaccessible(self.a["ratings"][i])
                self.inaccessible(self.b["ratings"][i])
            self.a["ratings"][i]["themes"]["agent_runtime"] = a
            self.b["ratings"][i]["themes"]["agent_runtime"] = b
        result = self.analyze()
        stats = result["per_theme"]["agent_runtime"]
        self.assertEqual(stats["n"], 6)
        self.assertEqual(stats["selected_n"], 9)
        self.assertEqual(stats["excluded_n"], 3)
        self.assertEqual(stats["confusion"], {"PP": 2, "PA": 1, "AP": 2, "AA": 1})
        self.assertAlmostEqual(stats["observed_agreement"], .5)
        self.assertAlmostEqual(stats["chance_agreement"], .5)
        self.assertAlmostEqual(stats["cohens_kappa"], 0)
        self.assertAlmostEqual(stats["positive_agreement"], 4 / 7)
        self.assertAlmostEqual(stats["negative_agreement"], 2 / 5)
        self.assertEqual(stats["rater_a_exclusions"], {"missing": 0, "uncertain": 1, "not_reviewable": 1})
        self.assertEqual(stats["rater_b_exclusions"], {"missing": 0, "uncertain": 1, "not_reviewable": 1})
        disputed = {x["item_id"] for x in result["disagreements"] if x["code"] == "agent_runtime"}
        self.assertEqual(disputed, {"S03", "S04", "S05", "S09", "S12"})
        self.assertEqual(len(result["records"]), 24)
        self.assertEqual(set(result["per_theme"]), set(THEMES))
        self.assertNotIn("cohens_kappa", result)

    def test_primary_nominal_math_is_separate_from_multilabel(self):
        left = ["agent_harness", "agent_harness", "evaluations", "evaluations", "evaluations", "agent_harness"]
        right = ["agent_harness", "evaluations", "evaluations", "agent_harness", "evaluations", "evaluations"]
        for i, (a, b) in enumerate(zip(left, right)):
            self.a["ratings"][i]["primary_task"] = a
            self.b["ratings"][i]["primary_task"] = b
            for form in (self.a, self.b):
                form["ratings"][i]["themes"].update(agent_runtime="present", evaluation_quality="present")
        result = self.analyze()
        stats = result["primary_task"]
        self.assertEqual(stats["n"], 6)
        self.assertAlmostEqual(stats["observed_agreement"], .5)
        self.assertAlmostEqual(stats["chance_agreement"], .5)
        self.assertAlmostEqual(stats["cohens_kappa"], 0)
        self.assertNotIn("positive_agreement", stats)
        self.assertEqual(result["per_theme"]["agent_runtime"]["n"], 9)
        self.assertAlmostEqual(result["per_theme"]["agent_runtime"]["cohens_kappa"], 1)

    def test_undefined_binary_and_primary_degenerate_cases(self):
        report = self.analyze()
        binary = report["per_theme"]["agent_runtime"]
        self.assertIsNone(binary["cohens_kappa"])
        self.assertIn("chance", binary["reason"])
        self.assertIsNone(binary["positive_agreement"])
        self.assertEqual(binary["negative_agreement"], 1)
        self.assertIsNone(report["primary_task"]["cohens_kappa"])
        for form in (self.a, self.b):
            for row in form["ratings"]:
                row["themes"]["agent_runtime"] = "uncertain"
            form["ratings"][0]["themes"]["agent_runtime"] = "present"
            form["ratings"][0]["primary_task"] = "agent_harness"
        one = self.analyze(output=self.dir / "one.json")
        for stats in (one["per_theme"]["agent_runtime"], one["primary_task"]):
            self.assertEqual(stats["n"], 1)
            self.assertIsNone(stats["cohens_kappa"])
            self.assertIn("two", stats["reason"])

    def test_missing_review_rows_do_not_shrink_selected_denominator(self):
        self.b["ratings"].pop()
        result = self.analyze()
        self.assertEqual(result["selected_n"], 9)
        self.assertEqual(len(result["records"]), 24)
        stats = result["per_theme"]["agent_runtime"]
        self.assertEqual(stats["n"], 8)
        self.assertEqual(stats["selected_n"], 9)
        self.assertEqual(stats["rater_b_exclusions"]["missing"], 1)

    def test_missing_rater_rows_do_not_masquerade_as_completed_adjudication(self):
        # All submitted votes agree, so there are *zero disputes*. Yet the
        # selected denominator remains nine and the review is not complete.
        self.b["ratings"].pop()
        report = self.analyze(output=self.dir / "one-unpaired.json")
        self.assertEqual(report["disagreements"], [])
        self.assertEqual(report["selected_n"], 9)
        self.assertEqual(report["review_submission"]["paired_selected_n"], 8)
        self.assertEqual(report["review_submission"]["missing_a_item_ids"], [])
        self.assertEqual(report["review_submission"]["missing_b_item_ids"], ["S12"])
        self.assertEqual(report["adjudication"]["status"], "incomplete_reviews")
        self.assertEqual(report["adjudication"]["missing_rating_item_ids"], ["S12"])
        self.assertEqual(report["adjudication"]["pending"], [])
        # Both coders can omit an item; that is still missing, not agreement.
        self.a["ratings"].pop()
        both = self.analyze(output=self.dir / "both-unpaired.json")
        self.assertEqual(both["review_submission"]["paired_selected_n"], 8)
        self.assertEqual(both["review_submission"]["missing_a_item_ids"], ["S12"])
        self.assertEqual(both["review_submission"]["missing_b_item_ids"], ["S12"])
        self.assertEqual(both["adjudication"]["status"], "incomplete_reviews")
        self.assertFalse(both["human_independence_verified"])

    def test_complete_submission_without_disputes_does_not_certify_humans(self):
        report = self.analyze(output=self.dir / "full-submissions.json")
        self.assertEqual(report["review_submission"]["paired_selected_n"], 9)
        self.assertEqual(report["adjudication"]["status"], "complete")
        self.assertEqual(report["adjudication"]["missing_rating_item_ids"], [])
        self.assertFalse(report["human_independence_verified"])
        self.assertEqual(report["research_enrollment"], "blocked")

    def test_pseudonyms_do_not_authenticate_humans_or_source_rights(self):
        report = self.analyze()
        self.assertFalse(report["human_independence_verified"])
        self.assertFalse(report["source_rights_verified"])
        self.assertEqual(report["research_enrollment"], "blocked")
        self.assertEqual(report["dataset_kind"], "synthetic")

    def test_reject_invalid_review_identity_binding_and_schema(self):
        mutations = [lambda x: x.update(reviewer_id="FICTIONAL_a"),
                     lambda x: x.update(reviewer_id="email@example.com"),
                     lambda x: x.update(reviewer_id="unknown"),
                     lambda x: x.update(frame_sha256="0" * 64),
                     lambda x: x.update(sample_id="wrong"),
                     lambda x: x.update(human_attested=True),
                     lambda x: x.update(dataset_kind="self_reported"),
                     lambda x: x.update(reviewed_at_utc="2026-10-13T12:00:00"),
                     lambda x: x.update(reviewed_at_utc="2026-10-12T12:00:00Z"),
                     lambda x: x["ratings"][0].update(item_id="E01"),
                     lambda x: x["ratings"].append(copy.deepcopy(x["ratings"][0])),
                     lambda x: x["ratings"][0]["themes"].pop("other"),
                     lambda x: x["ratings"][0]["themes"].update(other="guessed"),
                     lambda x: x["ratings"][0].update(source_checked_at_utc="2026-10-13T13:00:00Z")]
        for i, mutate in enumerate(mutations):
            with self.subTest(mutation=i):
                bad = copy.deepcopy(self.b)
                mutate(bad)
                self.analyze(b=bad, success=False)

    def test_inaccessible_never_negative_and_primary_requires_present_theme(self):
        for label in ("absent", "present", "uncertain"):
            bad = copy.deepcopy(self.b)
            self.inaccessible(bad["ratings"][0])
            bad["ratings"][0]["themes"]["agent_runtime"] = label
            self.analyze(b=bad, success=False)
        bad = copy.deepcopy(self.b)
        bad["ratings"][0]["primary_task"] = "agent_harness"
        self.analyze(b=bad, success=False)

    def test_adjudication_preserves_pre_adjudication_math_and_original_labels(self):
        self.a["ratings"][0]["themes"]["agent_runtime"] = "present"
        self.a["ratings"][1]["themes"]["agent_runtime"] = "uncertain"
        original = self.analyze(output=self.dir / "original.json")
        c = self.adjudication([{"item_id": "S01", "code": "agent_runtime",
                               "decision": "present", "evidence_ref": "fictional_resolve"}])
        resolved = self.analyze(adjudication=c, output=self.dir / "resolved.json")
        for key in ("per_theme", "primary_task", "disagreements", "records"):
            self.assertEqual(original[key], resolved[key])
        self.assertEqual(resolved["adjudication"]["status"], "partial")
        self.assertEqual(len(resolved["adjudication"]["pending"]), 1)

    def test_reject_extra_duplicate_undisputed_or_stale_adjudication(self):
        self.a["ratings"][0]["themes"]["agent_runtime"] = "present"
        decision = {"item_id": "S01", "code": "agent_runtime", "decision": "absent", "evidence_ref": "fictional_resolution"}
        candidates = [self.adjudication([dict(decision, item_id="S02")]),
                      self.adjudication([decision, decision]),
                      self.adjudication([dict(decision, item_id="E01")]),
                      self.adjudication([dict(decision, code="unlisted")]),
                      dict(self.adjudication([decision]), adjudicator_id="FICTIONAL_A"),
                      dict(self.adjudication([decision]), review_b_sha256="0" * 64),
                      dict(self.adjudication([decision]), predictions_unseen_attested=False),
                      dict(self.adjudication([decision]), adjudicated_at_utc="2026-10-13T12:00:00Z")]
        for candidate in candidates:
            with self.subTest(candidate=candidate):
                self.analyze(adjudication=candidate, success=False)

    def test_frame_tampering_rejected_even_with_recomputed_review_hash(self):
        original = self.frame_path
        for change in (lambda x: x["items"].pop(),
                       lambda x: x["items"][0].update(selected=False),
                       lambda x: x["sources"][0].update(sha256="0" * 64),
                       lambda x: x["items"][0].update(source_url="https://example.invalid/fictional")):
            mutated = copy.deepcopy(self.frame)
            change(mutated)
            self.frame_path = self.write("bad-frame.json", mutated)
            self.cli("verify-frame", "--frame", self.frame_path, success=False)
        self.frame_path = original

    def test_adjudicated_primary_requires_consistent_theme_resolution(self):
        self.a["ratings"][0]["primary_task"] = "agent_harness"
        self.a["ratings"][0]["themes"]["agent_runtime"] = "present"
        bad = self.adjudication([
            {"item_id": "S01", "code": "primary_task", "decision": "agent_harness", "evidence_ref": "fictional_primary"},
            {"item_id": "S01", "code": "agent_runtime", "decision": "absent", "evidence_ref": "fictional_theme"},
        ])
        self.analyze(adjudication=bad, success=False)
        valid = copy.deepcopy(bad)
        valid["decisions"][1]["decision"] = "present"
        report = self.analyze(adjudication=valid)
        self.assertEqual(report["adjudication"]["status"], "complete")
        self.assertEqual(report["primary_task"]["n"], 0)
        self.assertEqual(len(report["disagreements"]), 2)

    def test_unfilled_packets_cannot_be_analyzed_as_completed_review(self):
        out = self.dir / "blank.json"
        self.cli("pack", "--frame", self.frame_path, "--output", out)
        self.analyze(a=json.loads(out.read_text()), success=False)

    def test_all_present_null_negative_agreement_and_nominal_chance_one(self):
        for form in (self.a, self.b):
            for row in form["ratings"]:
                row["primary_task"] = "agent_harness"
                row["themes"]["agent_runtime"] = "present"
        result = self.analyze()
        self.assertIsNone(result["per_theme"]["agent_runtime"]["negative_agreement"])
        self.assertEqual(result["per_theme"]["agent_runtime"]["positive_agreement"], 1)
        self.assertIsNone(result["primary_task"]["cohens_kappa"])
        self.assertIn("chance", result["primary_task"]["reason"])

    def test_raw_submitted_file_hashes_separate_from_canonical_binding(self):
        a_path = self.write("a.json", self.a)
        b_path = self.dir / "b.json"
        b_path.write_text(json.dumps(self.b, sort_keys=False, indent=4) + "\n\n", encoding="utf-8")
        out = self.dir / "raw.json"
        self.cli("analyze", "--frame", self.frame_path, "--coder-a", a_path,
                 "--coder-b", b_path, "--output", out)
        report = json.loads(out.read_text())
        self.assertEqual(report["raw_input_sha256"], {"frame": self.sha(self.frame_path),
                        "coder_a": self.sha(a_path), "coder_b": self.sha(b_path), "adjudication": None})
        self.assertEqual(report["review_b_sha256"], self.fingerprint(self.b))
        self.assertNotEqual(report["review_b_sha256"], report["raw_input_sha256"]["coder_b"])
        canonical_b = self.dir / "canonical-b.json"
        canonical_b.write_text(json.dumps(self.b, sort_keys=True, separators=(",", ":")))
        second = self.dir / "second-raw.json"
        self.cli("analyze", "--frame", self.frame_path, "--coder-a", a_path,
                 "--coder-b", canonical_b, "--output", second)
        other = json.loads(second.read_text())
        self.assertEqual(other["review_b_sha256"], report["review_b_sha256"])
        self.assertNotEqual(other["raw_input_sha256"]["coder_b"], report["raw_input_sha256"]["coder_b"])
        self.assertEqual(other["per_theme"], report["per_theme"])

    def test_raw_adjudication_hash_preserved(self):
        self.a["ratings"][0]["themes"]["agent_runtime"] = "present"
        c = self.adjudication([{"item_id": "S01", "code": "agent_runtime",
                              "decision": "absent", "evidence_ref": "fictional_resolve"}])
        report = self.analyze(adjudication=c)
        self.assertEqual(report["raw_input_sha256"]["adjudication"], self.sha(self.dir / "c.json"))
        self.assertEqual(report["adjudication_sha256"], self.fingerprint(c))

    def test_negative_kappa_is_preserved_instead_of_truncated_to_zero(self):
        for i in range(9):
            for form in (self.a, self.b):
                form["ratings"][i]["themes"]["developer_reuse"] = "uncertain"
        for i in range(6):
            self.a["ratings"][i]["themes"]["developer_reuse"] = "present" if i < 3 else "absent"
            self.b["ratings"][i]["themes"]["developer_reuse"] = "absent" if i < 3 else "present"
            self.a["ratings"][i]["primary_task"] = "evaluations" if i < 3 else "context_memory"
            self.b["ratings"][i]["primary_task"] = "context_memory" if i < 3 else "evaluations"
            for form in (self.a, self.b):
                form["ratings"][i]["themes"].update(evaluation_quality="present", context_memory="present")
        report = self.analyze()
        binary = report["per_theme"]["developer_reuse"]
        self.assertEqual(binary["confusion"], {"PP": 0, "PA": 3, "AP": 3, "AA": 0})
        self.assertEqual(binary["cohens_kappa"], -1)
        self.assertEqual(binary["positive_agreement"], 0)
        self.assertEqual(binary["negative_agreement"], 0)
        self.assertEqual(report["primary_task"]["cohens_kappa"], -1)

    def test_strict_bounded_json_and_nonregular_inputs_fail_without_output(self):
        for raw in (b'{"schema_version":"wrong","schema_version":"hiring-223-v1"}',
                    b'{"n":NaN}', b'{"n":Infinity}', b'{"n":1e9999}',
                    b'{"n":1e-9999}', b'\xff', b'[' * 100 + b'0' + b']' * 100,
                    b' ' * (1024 * 1024 + 1)):
            bad = self.dir / "bad.json"
            bad.write_bytes(raw)
            result = self.cli("verify-frame", "--frame", bad, success=False)
            self.assertNotIn("Traceback", result.stderr)
        link = self.dir / "link.json"
        link.symlink_to(self.frame_path)
        self.cli("verify-frame", "--frame", link, success=False)
        fifo = self.dir / "pipe.json"
        os.mkfifo(fifo)
        self.cli("verify-frame", "--frame", fifo, success=False)
        self.cli("verify-frame", "--frame", self.dir, success=False)

    def test_cli_json_and_missing_path_errors_never_echo_private_input_details(self):
        private_name = "PRIVATE-fictional-rater-identity"
        path = self.dir / (private_name + ".json")
        path.write_text('{"' + private_name + '":1,"' + private_name + '":2}', encoding="utf-8")
        bad = self.cli("verify-frame", "--frame", path, success=False)
        self.assertIn("strict UTF-8 JSON", bad.stderr)
        self.assertNotIn(private_name, bad.stderr)
        self.assertNotIn(str(path), bad.stderr)
        self.assertNotIn("Traceback", bad.stderr)
        path.unlink()
        absent = self.cli("verify-frame", "--frame", path, success=False)
        self.assertNotIn(private_name, absent.stderr)
        self.assertNotIn(str(path), absent.stderr)
        self.assertNotIn("Traceback", absent.stderr)

    def test_pack_and_analyze_outputs_are_write_once_even_for_aliases(self):
        output = self.dir / "existing.json"
        output.write_bytes(b"original fictional evidence")
        original = output.read_bytes()
        self.cli("pack", "--frame", self.frame_path, "--output", output, success=False)
        self.assertEqual(output.read_bytes(), original)
        a_path = self.write("a.json", self.a)
        b_path = self.write("b.json", self.b)
        snapshot = a_path.read_bytes()
        for path in (output, a_path):
            self.cli("analyze", "--frame", self.frame_path, "--coder-a", a_path,
                     "--coder-b", b_path, "--output", path, success=False)
        self.assertEqual(a_path.read_bytes(), snapshot)
        link = self.dir / "alias.json"
        link.symlink_to(a_path)
        self.cli("pack", "--frame", self.frame_path, "--output", link, success=False)
        hardlink = self.dir / "hardlink.json"
        os.link(a_path, hardlink)
        self.cli("pack", "--frame", self.frame_path, "--output", hardlink, success=False)
        self.assertEqual(a_path.read_bytes(), snapshot)


if __name__ == "__main__":
    unittest.main()
