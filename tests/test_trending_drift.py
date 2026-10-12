"""Synthetic ranking tests, not empirical Trending ranking comparisons."""
import unittest
from trending_study.trending_drift import DriftError, compare


def dataset(a, b, left_date="2026-10-01T00:00:00Z", right_date="2026-10-02T00:00:00Z"):
    return {"before": {"repository_ids": a, "observed_at_utc": left_date, "window": "daily",
                       "source_sha256": "a"*64, "language": None},
            "after": {"repository_ids": b, "observed_at_utc": right_date, "window": "daily",
                      "source_sha256": "b"*64, "language": None}}


class DriftTests(unittest.TestCase):
    def test_identical(self):
        r = compare(dataset([1, 2, 3], [1, 2, 3]))
        self.assertEqual(r["jaccard"], 1)
        self.assertEqual(r["kendall_tau_shared_only"], 1)
        self.assertAlmostEqual(r["rbo_extrapolated_equal_depth"], 1)

    def test_reversed(self):
        r = compare(dataset([1, 2, 3], [3, 2, 1]))
        self.assertEqual(r["kendall_tau_shared_only"], -1)
        self.assertLess(r["rbo_extrapolated_equal_depth"], 1)

    def test_disjoint(self):
        r = compare(dataset([1, 2], [3, 4]))
        self.assertEqual(r["jaccard"], 0)
        self.assertIsNone(r["kendall_tau_shared_only"])
        self.assertEqual(r["rbo_extrapolated_equal_depth"], 0)

    def test_unequal_depth(self):
        r = compare(dataset([1, 2], [1, 3, 2]))
        self.assertIsNone(r["rbo_extrapolated_equal_depth"])
        self.assertAlmostEqual(r["jaccard"], 2/3)

    def test_rejects_backdated(self):
        with self.assertRaises(DriftError):
            compare(dataset([1], [2], "2026-10-02T00:00:00Z", "2026-10-01T00:00:00Z"))

    def test_rejects_duplicate_ids(self):
        with self.assertRaises(DriftError):
            compare(dataset([1, 1], [1]))

    def test_rejects_surface_mismatch(self):
        x = dataset([1], [1])
        x["after"]["window"] = "weekly"
        with self.assertRaises(DriftError):
            compare(x)

    def test_rejects_missing_source(self):
        x = dataset([1], [1])
        del x["after"]["source_sha256"]
        with self.assertRaises(DriftError):
            compare(x)

    def test_rejects_utc_naive(self):
        with self.assertRaises(DriftError):
            compare(dataset([1], [1], "2026-10-01T00:00:00", "2026-10-02T00:00:00Z"))


if __name__ == "__main__":
    unittest.main()
