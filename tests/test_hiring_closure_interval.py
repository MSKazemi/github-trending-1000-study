"""Prospective issue #222: synthetic, explicit-only closure intervals.

These are source-asserted records, not actual vacancy outcomes; no pages were
fetched, no employers or people identified and no jobs inferred as filled.
"""
import copy
import unittest

from tests.test_hiring_observations import fixture
from trending_study.hiring_observations import HiringObservationError, audit


class RequisitionClosureIntervalTests(unittest.TestCase):
    def test_explicit_close_is_observation_interval_not_actual_time(self):
        d = fixture()
        d["observations"] = d["observations"][:5]  # includes 2 listed variants, explicit close and later access failure
        result = audit(d)
        a = result["requisitions"][0]
        self.assertFalse(a["right_censored"])
        self.assertEqual(a["closure_interval_last_listed_at_utc"],
                         "2026-01-02T12:00:00Z")
        self.assertEqual(a["closure_interval_first_explicitly_closed_at_utc"],
                         "2026-01-04T12:00:00Z")
        self.assertIsNone(a["actual_closure_at_utc"])
        self.assertIsNone(a["filled_positions"])
        self.assertFalse(result["independent_verification"])
        self.assertFalse(result["eligible_for_confirmatory_cohort"])

    def test_inaccessible_later_does_not_prove_close(self):
        d = fixture()
        d["observations"] = d["observations"][:3]
        a = audit(d)["requisitions"][0]
        self.assertTrue(a["right_censored"])
        self.assertIsNone(a["closure_interval_last_listed_at_utc"])
        self.assertIsNone(a["closure_interval_first_explicitly_closed_at_utc"])
        self.assertIsNone(a["actual_closure_at_utc"])

    def test_existing_reopened_req_has_no_current_close(self):
        result = audit(fixture())
        a, b, c = result["requisitions"]
        for row in (a, b, c):
            self.assertIsNone(row["closure_interval_last_listed_at_utc"])
            self.assertIsNone(row["closure_interval_first_explicitly_closed_at_utc"])
            self.assertIsNone(row["actual_closure_at_utc"])
            self.assertIsNone(row["filled_positions"])

    def test_second_explicit_close_bounds_only_latest_open_interval(self):
        d = fixture()
        close = copy.deepcopy(d["observations"][3])
        close["observation_id"] = "SYN_REPEAT_CLOSE"
        close["observed_at_utc"] = "2026-01-06T13:00:00Z"
        close["accessed_at_utc"] = close["observed_at_utc"]
        close["recorded_at_utc"] = close["observed_at_utc"]
        d["observations"].insert(6, close)
        a = audit(d)["requisitions"][0]
        self.assertFalse(a["right_censored"])
        self.assertEqual(a["closure_interval_last_listed_at_utc"],
                         "2026-01-06T12:00:00Z")
        self.assertEqual(a["closure_interval_first_explicitly_closed_at_utc"],
                         "2026-01-06T13:00:00Z")
        self.assertIsNone(a["actual_closure_at_utc"])

    def test_first_seen_closed_has_no_artificial_lower_bound(self):
        d = fixture()
        d["observations"] = [copy.deepcopy(d["observations"][3])]
        a = audit(d)["requisitions"][0]
        self.assertIsNone(a["first_listed_observation_at_utc"])
        self.assertIsNone(a["closure_interval_last_listed_at_utc"])
        self.assertEqual(a["closure_interval_first_explicitly_closed_at_utc"],
                         "2026-01-04T12:00:00Z")
        self.assertIsNone(a["actual_closure_at_utc"])

    def test_private_metadata_hosts_rejected_without_network(self):
        for host in ("localhost", "corp.internal", "jobs.local",
                     "127.0.0.1", "169.254.169.254", "192.168.1.4",
                     "10.10.10.10"):
            d = fixture()
            d["sources"][0]["index_url"] = f"https://{host}/jobs"
            d["sources"][0]["listing_host"] = host
            with self.subTest(host=host):
                with self.assertRaisesRegex(HiringObservationError, "source URL"):
                    audit(d)

    def test_observation_source_does_not_establish_review_or_consent(self):
        report = audit(fixture())
        self.assertFalse(report["source_access_approved"])
        self.assertFalse(report["human_methods_approved"])
        self.assertFalse(report["independent_verification"])
        self.assertFalse(report["eligible_for_confirmatory_cohort"])


if __name__ == "__main__":
    unittest.main()
