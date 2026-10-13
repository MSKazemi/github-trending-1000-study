"""Issue #19: synthetic controls for reuse-first search validation.

No search engine has been run, no reviewer identity authenticated and no
retrieved candidate is installed by these tests.
"""
import copy
import unittest

from trending_study.goldset import GoldsetError, evaluate
from tests.test_goldset import DATA


class TaskFirstGoldsetTests(unittest.TestCase):
    def test_missing_review_cannot_be_promoted_to_viable(self):
        data = copy.deepcopy(DATA)
        data["tasks"][0]["candidates"][0]["reviewer_labels"] = ["unknown", "viable"]
        data["tasks"][0]["candidates"][0]["adjudicator_ref"] = "synthetic-third"
        with self.assertRaisesRegex(GoldsetError, "missing independent reviewer"):
            evaluate(data)

    def test_search_rank_shortfall_is_explicit_and_penalized(self):
        data = copy.deepcopy(DATA)
        data["tasks"][0]["systems"][0]["ranked_candidate_ids"] = ["x"]
        row = evaluate(data, k=5)["results"][0]["systems"][0]
        self.assertEqual(row["returned_at_k"], 1)
        self.assertEqual(row["unfilled_rank_slots_at_k"], 4)
        self.assertAlmostEqual(row["precision_at_k"], 0.2)

    def test_unjudged_rank_is_not_treated_as_negative(self):
        data = copy.deepcopy(DATA)
        item = evaluate(data, k=2)["results"][0]["systems"][1]
        self.assertIsNone(item["precision_at_k"])
        self.assertEqual(item["unjudged_at_k"], 1)
        self.assertEqual((item["precision_at_k_lower_bound"],
                          item["precision_at_k_upper_bound"]), (0.5, 1.0))

    def test_pilot_task_baseline_cannot_be_in_future(self):
        data = copy.deepcopy(DATA)
        data["dataset_kind"] = "pilot"
        data["tasks"][0]["baseline_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(GoldsetError, "future"):
            evaluate(data)


if __name__ == "__main__":
    unittest.main()
