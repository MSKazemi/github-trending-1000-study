"""Synthetic-only agreement calculations; not a human-rating audit."""
import unittest
from trending_study.rubric_agreement import RubricError, evaluate


def sample(*pairs):
    return {"rater_a": "blindA", "rater_b": "blindB",
            "records": [{"item_id": str(i), "project_type": "cli",
                         "criterion": "documented_first_run",
                         "rating_a": x, "rating_b": y}
                        for i, (x, y) in enumerate(pairs)]}


class RubricAgreementTests(unittest.TestCase):
    def test_perfect_balanced_is_one(self):
        r = evaluate(sample(("pass", "pass"), ("fail", "fail")))
        self.assertEqual(r["cohens_kappa"], 1)
        self.assertEqual(r["rated_pairs"], 2)

    def test_observed_half_chance_half_zero_kappa(self):
        r = evaluate(sample(("pass", "pass"), ("pass", "fail"),
                            ("fail", "pass"), ("fail", "fail")))
        self.assertEqual(r["cohens_kappa"], 0)
        self.assertEqual(len(r["disagreement_ids"]), 2)

    def test_single_category_is_undefined_not_perfect_kappa(self):
        self.assertIsNone(evaluate(sample(("pass", "pass")))["cohens_kappa"])

    def test_unknown_excluded_and_counted(self):
        r = evaluate(sample(("pass", "pass"), ("unknown", "pass")))
        self.assertEqual((r["total"], r["rated_pairs"], r["excluded_unknown"]),
                         (2, 1, 1))

    def test_distinguishes_na_disagreement(self):
        r = evaluate(sample(("not_applicable", "fail"), ("pass", "pass")))
        self.assertIn("0", r["disagreement_ids"])

    def test_duplicate_ids_rejected(self):
        p = sample(("pass", "pass"), ("fail", "fail"))
        p["records"][1]["item_id"] = "0"
        with self.assertRaises(RubricError):
            evaluate(p)

    def test_no_rated_pairs_is_missing(self):
        self.assertIsNone(evaluate(sample(("unknown", "pass")))["cohens_kappa"])

    def test_same_rater_rejected(self):
        p = sample(("pass", "pass"))
        p["rater_b"] = "blindA"
        with self.assertRaises(RubricError):
            evaluate(p)


if __name__ == "__main__":
    unittest.main()
