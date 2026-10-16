import copy
from contextlib import redirect_stderr
import io
import json
from pathlib import Path
import tempfile
import unittest
from trending_study.goldset import GoldsetError, evaluate, main


DATA = {
    "schema_version": "1.0", "dataset_kind": "synthetic", "tasks": [{
        "task_id": "T1",
        "baseline_utc": "2026-10-11T12:00:00Z",
        "spec_sha256": "a" * 64,
        "acceptance_sha256": "b" * 64,
        "candidates": [
            {"id": "x", "final_label": "viable", "reviewer_labels": ["viable", "viable"],
             "available_since_utc": "2026-09-01T12:00:00Z",
             "gates": {"functional": "pass", "license": "pass", "security": "pass", "maintenance": "pass"},
             "evidence_ref": "SYNTHETIC ONLY"},
            {"id": "y", "final_label": "unknown", "reviewer_labels": ["unknown", "unknown"],
             "available_since_utc": None,
             "gates": {"functional": "unknown", "license": "unknown", "security": "unknown", "maintenance": "unknown"},
             "evidence_ref": None},
            {"id": "z", "final_label": "not_viable", "reviewer_labels": ["not_viable", "not_viable"],
             "available_since_utc": "2026-09-01T12:00:00Z",
             "gates": {"functional": "fail", "license": "pass", "security": "unknown", "maintenance": "unknown"},
             "evidence_ref": "SYNTHETIC FAIL"},
        ],
        "systems": [
            {"name": "lex", "ranked_candidate_ids": ["x", "z"]},
            {"name": "semantic", "ranked_candidate_ids": ["y", "x"]},
        ],
    }],
}


class GoldSetTests(unittest.TestCase):
    def test_complete_judgment_and_relative_recall(self):
        a = evaluate(DATA, k=2)["results"][0]
        self.assertEqual(a["observed_opportunity"], "viable_found_in_audited_pool")
        self.assertEqual(a["raw_agreement"], 1.0)
        lex = a["systems"][0]
        self.assertEqual(lex["precision_at_k"], 0.5)
        self.assertEqual(lex["pooled_relative_recall_at_k"], 1.0)

    def test_unjudged_is_not_a_negative(self):
        a = evaluate(DATA, k=2)["results"][0]["systems"][1]
        self.assertIsNone(a["precision_at_k"])
        self.assertIsNone(a["pooled_relative_recall_at_k"])
        self.assertEqual(a["precision_at_k_lower_bound"], 0.5)
        self.assertEqual(a["precision_at_k_upper_bound"], 1.0)
        self.assertEqual(a["unjudged_at_k"], 1)

    def test_release_after_task_cannot_be_viable(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["available_since_utc"] = "2026-12-01T00:00:00Z"
        with self.assertRaises(GoldsetError):
            evaluate(d)

    def test_unknown_with_positive_label_rejected(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["gates"]["security"] = "unknown"
        with self.assertRaises(GoldsetError):
            evaluate(d)

    def test_reviewer_disagreement_requires_adjudicator(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["reviewer_labels"] = ["viable", "not_viable"]
        with self.assertRaises(GoldsetError):
            evaluate(d)
        d["tasks"][0]["candidates"][0]["adjudicator_ref"] = "SYNTHETIC THIRD REVIEWER"
        self.assertEqual(evaluate(d)["task_count"], 1)

    def test_unknown_candidates_cannot_appear_as_negative(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["systems"][0]["ranked_candidate_ids"] = ["not-in-pool"]
        with self.assertRaises(GoldsetError):
            evaluate(d)

    def test_no_known_viable_is_not_no_global_solution(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"] = [d["tasks"][0]["candidates"][2]]
        d["tasks"][0]["systems"] = []
        a = evaluate(d)["results"][0]
        self.assertEqual(a["observed_opportunity"], "none_found_in_audited_pool_not_global_absence")

    def test_duplicate_task_ids_rejected(self):
        d = copy.deepcopy(DATA)
        d["tasks"].append(copy.deepcopy(d["tasks"][0]))
        with self.assertRaises(GoldsetError):
            evaluate(d)

    def test_invalid_k_rejected(self):
        with self.assertRaises(GoldsetError):
            evaluate(DATA, k=0)

    def test_temporal_availability_alone_can_make_candidate_not_viable(self):
        # Synthetic historical task: code shipped later, other gates pass.
        d = copy.deepcopy(DATA)
        candidate = d["tasks"][0]["candidates"][2]
        candidate["available_since_utc"] = "2026-10-12T01:00:00Z"
        candidate["gates"] = {
            "functional": "pass", "license": "pass",
            "security": "pass", "maintenance": "pass",
            "availability": "fail",
        }
        self.assertEqual(evaluate(d)["results"][0]["pool_verified_not_viable"], 1)

    def test_future_release_cannot_claim_available_even_when_label_negative(self):
        d = copy.deepcopy(DATA)
        candidate = d["tasks"][0]["candidates"][2]
        candidate["available_since_utc"] = "2026-10-12T01:00:00Z"
        candidate["gates"]["availability"] = "pass"
        with self.assertRaisesRegex(GoldsetError, "released after task baseline"):
            evaluate(d)

    def test_unknown_availability_must_not_pass_positive_label(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["gates"]["availability"] = "unknown"
        with self.assertRaisesRegex(GoldsetError, "viable without full passing gates"):
            evaluate(d)

    def test_two_abstaining_reviewers_cannot_establish_viability(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["reviewer_labels"] = ["unknown", "unknown"]
        with self.assertRaisesRegex(GoldsetError, "two unknown reviewer labels"):
            evaluate(d)

    def test_two_abstaining_reviewers_cannot_establish_nonviability(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][2]["reviewer_labels"] = ["unknown", "unknown"]
        with self.assertRaisesRegex(GoldsetError, "two unknown reviewer labels"):
            evaluate(d)

    def test_unresolved_reviewers_remain_unknown(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][1]["reviewer_labels"] = ["unknown", "unknown"]
        d["tasks"][0]["candidates"][1]["final_label"] = "unknown"
        self.assertEqual(evaluate(d)["results"][0]["pool_unknown"], 1)

    def test_partial_review_needs_adjudicator_for_definitive_label(self):
        d = copy.deepcopy(DATA)
        c = d["tasks"][0]["candidates"][0]
        c["reviewer_labels"] = ["viable", "unknown"]
        with self.assertRaisesRegex(GoldsetError, "disagreement needs adjudicator_ref"):
            evaluate(d)
        c["adjudicator_ref"] = "SYNTHETIC ADJUDICATION ONLY"
        self.assertEqual(evaluate(d)["results"][0]["pool_verified_viable"], 1)

    def test_invalid_availability_gate_rejected(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["gates"]["availability"] = "guessed"
        with self.assertRaisesRegex(GoldsetError, "availability must be"):
            evaluate(d)



    def test_private_task_candidate_and_system_ids_not_in_error(self):
        d = copy.deepcopy(DATA)
        task = d["tasks"][0]
        task["task_id"] = "PRIVATE_TASK_6346"
        task["candidates"][0]["id"] = "PRIVATE_CANDIDATE_6350"
        task["systems"][0]["name"] = "PRIVATE_SYSTEM_6351"
        task["systems"][0]["ranked_candidate_ids"] = [
            "PRIVATE_CANDIDATE_6350", "z",
        ]
        markers = ("PRIVATE_TASK_6346", "PRIVATE_CANDIDATE_6350",
                   "PRIVATE_SYSTEM_6351")
        def check(candidate):
            with self.assertRaises(GoldsetError) as captured:
                evaluate(candidate)
            self.assertTrue(str(captured.exception))
            for marker in markers:
                self.assertNotIn(marker, str(captured.exception))
        bad = copy.deepcopy(d)
        bad["tasks"][0]["candidates"][0]["gates"]["security"] = "PRIVATE_BAD_GATE"
        check(bad)
        bad = copy.deepcopy(d)
        bad["tasks"].append(copy.deepcopy(bad["tasks"][0]))
        check(bad)
        bad = copy.deepcopy(d)
        bad["tasks"][0]["candidates"].append(copy.deepcopy(bad["tasks"][0]["candidates"][0]))
        check(bad)
        bad = copy.deepcopy(d)
        bad["tasks"][0]["systems"].append(copy.deepcopy(bad["tasks"][0]["systems"][0]))
        check(bad)
        bad = copy.deepcopy(d)
        bad["tasks"][0]["systems"][0]["ranked_candidate_ids"][0] = "UNPOOLED_PRIVATE_ID"
        check(bad)

    def test_cli_redacts_private_ids_even_on_invalid_gate(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["task_id"] = "PRIVATE_TASK_ID_MARKER"
        d["tasks"][0]["candidates"][0]["id"] = "PRIVATE_CANDIDATE_ID_MARKER"
        d["tasks"][0]["candidates"][0]["gates"]["license"] = "bad"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "PRIVATE_FILENAME_MARKER.json"
            path.write_text(json.dumps(d), encoding="utf-8")
            stderr = io.StringIO()
            with redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
                main(["--input", str(path), "--k", "3"])
            self.assertEqual(caught.exception.code, 2)
            for private in ("PRIVATE_TASK_ID_MARKER", "PRIVATE_CANDIDATE_ID_MARKER",
                            "PRIVATE_FILENAME_MARKER"):
                self.assertNotIn(private, stderr.getvalue())
            self.assertIn("candidate: gate license", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
