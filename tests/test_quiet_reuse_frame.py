"""Synthetic frame selection checks; no actual cohort has been drawn."""
import copy
import unittest
from trending_study.quiet_reuse_frame import FrameError, select


def fake():
    return {"frozen_at_utc": "2026-10-12T00:00:00Z",
            "seed": "synthetic-fixed-seed", "quotas": {"old_low": 1, "young": 1},
            "repositories": [{"repository_id": i, "stratum": "old_low" if i <= 3 else "young",
                              "package_id": "fictional-" + str(i),
                              "source_url": "https://example.org/not-a-real-registry",
                              "snapshot_at_utc": "2026-10-01T00:00:00Z"}
                             for i in range(1, 6)]}


class FrameSelectionTests(unittest.TestCase):
    def test_input_order_independent(self):
        p = fake()
        a = select(p)
        p["repositories"].reverse()
        self.assertEqual(a["selected"], select(p)["selected"])
        self.assertEqual(a["frame_content_sha256"], select(p)["frame_content_sha256"])

    def test_stratified_nontrivial_sample(self):
        r = select(fake())
        self.assertEqual(len(r["selected"]), 2)
        self.assertEqual({x["stratum"] for x in r["selected"]}, {"old_low", "young"})

    def test_duplicate_repository_id(self):
        p = fake()
        p["repositories"].append(copy.deepcopy(p["repositories"][0]))
        with self.assertRaises(FrameError):
            select(p)

    def test_rejects_future_only_information(self):
        p = fake()
        p["repositories"][0]["future_reuse"] = 99
        with self.assertRaises(FrameError):
            select(p)

    def test_future_snapshot_rejected(self):
        p = fake()
        p["repositories"][0]["snapshot_at_utc"] = "2026-11-01T00:00:00Z"
        with self.assertRaises(FrameError):
            select(p)

    def test_missing_predeclared_stratum_rejected(self):
        p = fake()
        p["quotas"]["nonexistent"] = 2
        with self.assertRaises(FrameError):
            select(p)

    def test_insufficient_quota_disclosed(self):
        p = fake()
        p["quotas"]["young"] = 3
        self.assertEqual(select(p)["strata_with_insufficient_members"], ["young"])


    def test_unknown_columns_cannot_smuggle_future_outcome_proxies(self):
        for field in ("downstream_2027_uses", "stars_next_year", "favorite_candidate"):
            p = fake()
            p["repositories"][0][field] = 1
            with self.subTest(field=field), self.assertRaisesRegex(FrameError, "prespecified"):
                select(p)

    def test_future_frozen_frame_or_spoofed_source_rejected(self):
        p = fake()
        p["frozen_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(FrameError, "future"):
            select(p)
        p = fake()
        p["repositories"][0]["source_url"] = "https://registry.example@evil.example/pkg"
        with self.assertRaisesRegex(FrameError, "credentials"):
            select(p)

    def test_nominal_fraction_is_not_population_probability(self):
        report = select(fake())
        self.assertTrue(report["random_seed_independence_unverified"])
        self.assertFalse(report["eligible_for_population_prevalence_claim"])

    def test_malformed_stratum_type_is_rejected(self):
        p = fake()
        p["repositories"][0]["stratum"] = []
        with self.assertRaises(FrameError):
            select(p)


if __name__ == "__main__":
    unittest.main()
