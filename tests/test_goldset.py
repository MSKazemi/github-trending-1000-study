import copy
import unittest
from trending_study.goldset import GoldsetError, evaluate


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

    def test_invalid_availability_gate_rejected(self):
        d = copy.deepcopy(DATA)
        d["tasks"][0]["candidates"][0]["gates"]["availability"] = "guessed"
        with self.assertRaisesRegex(GoldsetError, "availability must be"):
            evaluate(d)



if __name__ == "__main__":
    unittest.main()
