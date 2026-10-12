"""Synthetic guard tests; not a verification of live Trending pages."""
import copy
import unittest

from trending_study.trending_overlap import OverlapError, evaluate


def fixture():
    return {
        "schema_version": "1.0",
        "dataset_kind": "synthetic",
        "captures": [
            {"capture_id": "a", "captured_at_utc": "2026-10-10T12:00:00Z",
             "page_url": "https://github.com/trending?since=daily", "window": "daily",
             "language_filter": None, "source_sha256": "a" * 64,
             "repository_ids": [10, 20, 30]},
            {"capture_id": "b", "captured_at_utc": "2026-10-11T12:00:00Z",
             "page_url": "https://github.com/trending?since=daily", "window": "daily",
             "language_filter": None, "source_sha256": "b" * 64,
             "repository_ids": [20, 10, 40]},
        ],
    }


class TrendingOverlapTests(unittest.TestCase):
    def test_set_overlap_and_common_rank_reversal(self):
        result = evaluate(fixture())
        self.assertAlmostEqual(result["jaccard"], 0.5)
        self.assertEqual(result["common_unique_ids"], 2)
        self.assertEqual(result["kendall_comparable_pairs"], 1)
        self.assertEqual(result["kendall_tau_on_common"], -1.0)
        self.assertFalse(result["eligible_for_confirmatory_cohort"])
        self.assertGreater(result["discounted_prefix_overlap_lower_bound"], 0)
        self.assertLess(result["discounted_prefix_overlap_lower_bound"], 1)

    def test_equal_lists(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [10, 20, 30]
        out = evaluate(data)
        self.assertEqual(out["jaccard"], 1)
        self.assertEqual(out["kendall_tau_on_common"], 1)

    def test_disjoint_rank_tau_not_zero(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [50, 60]
        out = evaluate(data)
        self.assertEqual(out["jaccard"], 0)
        self.assertIsNone(out["kendall_tau_on_common"])

    def test_one_common_rank_tau_unknown(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [10, 40]
        self.assertIsNone(evaluate(data)["kendall_tau_on_common"])

    def test_duplicate_ids_fail(self):
        data = fixture()
        data["captures"][0]["repository_ids"] = [10, 10]
        with self.assertRaises(OverlapError):
            evaluate(data)

    def test_wrong_surface_fails(self):
        for key, value in (("window", "weekly"),
                           ("language_filter", "Python"),
                           ("page_url", "https://github.com/trending/python?since=daily")):
            with self.subTest(key=key):
                data = fixture()
                data["captures"][1][key] = value
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_unverified_or_incomplete_input_fails(self):
        for key, value in (("source_sha256", None), ("repository_ids", []),
                           ("captured_at_utc", "2026-10-11T13:00:00+02:00")):
            with self.subTest(key=key):
                data = fixture()
                data["captures"][1][key] = value
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_not_positive_stable_ids(self):
        for value in (True, 0, -1, "10"):
            data = fixture()
            data["captures"][0]["repository_ids"] = [value]
            with self.assertRaises(OverlapError):
                evaluate(data)

    def test_no_forward_time_travel(self):
        data = fixture()
        data["captures"].reverse()
        with self.assertRaises(OverlapError):
            evaluate(data)

    def test_schema_and_persistence(self):
        data = fixture()
        data["dataset_kind"] = "observed_verified"
        with self.assertRaises(OverlapError):
            evaluate(data)
        for bad in (0, 1, True, -0.5):
            with self.assertRaises(OverlapError):
                evaluate(fixture(), bad)


if __name__ == "__main__":
    unittest.main()
