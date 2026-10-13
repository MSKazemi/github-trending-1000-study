"""Synthetic maintainer-burden accounting, never private participant data."""
import copy
import json
from pathlib import Path
import unittest
from trending_study.maintainer_burden import BurdenError, summarize, FIELDS

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "maintainer_externality.synthetic.json"

def card():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))

class BurdenTests(unittest.TestCase):
    def test_absent_logs_cannot_be_zero_cost(self):
        r = summarize([card()])
        self.assertEqual(r["case_count"], 1)
        self.assertEqual(r["missing_component_entries"], 6)
        self.assertIsNone(r["overall_human_minutes"])
        self.assertIsNone(r["per_accepted_task_minutes"])
        self.assertFalse(r["independent_review_authenticated"])

    def test_unconsented_work_may_not_be_recorded(self):
        c = card()
        c["human_time_minutes"]["upstream_review"] = 0
        with self.assertRaisesRegex(BurdenError, "unconsented"):
            summarize([c])

    def test_consent_declared_partial_is_not_complete_total(self):
        c = card()
        c["consent_state"] = "consented"
        c["human_time_minutes"]["upstream_review"] = 11.5
        r = summarize([c])
        self.assertEqual(r["known_partial_minutes_not_a_total"], 11.5)
        self.assertIsNone(r["overall_human_minutes"])
        self.assertEqual(r["missing_component_entries"], 5)

    def test_duplicate_case_does_not_inflate_independent_count(self):
        with self.assertRaisesRegex(BurdenError, "unique"):
            summarize([card(), copy.deepcopy(card())])

    def test_complete_synthetic_stays_unauthenticated(self):
        c = card()
        c["consent_state"] = "consented"
        c["task_accepted_by_independent_reviewer"] = "pass"
        c["human_time_minutes"] = {k: 1 for k in FIELDS}
        r = summarize([c])
        self.assertEqual(r["overall_human_minutes"], 6)
        self.assertEqual(r["cases_with_complete_time_boundary"], 1)
        self.assertIsNone(r["per_accepted_task_minutes"])
        self.assertEqual(r["synthetic_case_count"], 1)

    def test_negative_nan_or_future_time_fail(self):
        for value in (-1, float("nan"), float("inf")):
            c = card()
            c["consent_state"] = "consented"
            c["human_time_minutes"]["upstream_review"] = value
            with self.subTest(value=str(value)), self.assertRaises(BurdenError):
                summarize([c])
        c = card()
        c["observed_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(BurdenError, "future"):
            summarize([c])

if __name__ == "__main__":
    unittest.main()
