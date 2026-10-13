"""Synthetic test only; no real participant, consent or task outcome."""
import copy
import json
from pathlib import Path
import unittest
from trending_study.usefulness_task import UsefulnessError, summarize

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "usefulness_task.synthetic.json"

def card():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))

class UsefulnessTaskTests(unittest.TestCase):
    def test_fictional_unknown_is_not_zero_or_empirical(self):
        r = summarize(card())
        self.assertEqual(r["attempts"], 1)
        self.assertEqual(r["applicable_assigned_denominator"], 1)
        self.assertEqual(r["pass_fraction_logical_lower"], 0.0)
        self.assertEqual(r["pass_fraction_logical_upper"], 1.0)
        self.assertFalse(r["empirical_study_accepted"])

    def test_missing_outcomes_expand_bounds_not_denominator(self):
        p = card()
        p["attempts"].append(dict(p["attempts"][0], attempt_id="FICTIONAL-A2",
                                  participant_id="synthetic-second",
                                  accepted="fail"))
        p["attempts"][0]["accepted"] = "pass"
        p["attempts"][0]["time_to_first_success_minutes"] = 3
        r = summarize(p)
        self.assertEqual(r["applicable_assigned_denominator"], 2)
        self.assertEqual(r["pass_fraction_logical_lower"], 0.5)
        self.assertEqual(r["pass_fraction_logical_upper"], 0.5)

    def test_unattempted_pass_and_missing_time_fail(self):
        p = card()
        a = p["attempts"][0]
        a.update(accepted="pass", task_attempted=False, time_to_first_success_minutes=1)
        with self.assertRaisesRegex(UsefulnessError, "unattempted"):
            summarize(p)
        a["task_attempted"] = True
        a["time_to_first_success_minutes"] = None
        with self.assertRaisesRegex(UsefulnessError, "success time"):
            summarize(p)

    def test_duplicate_attempt_and_bogus_consent_fail(self):
        p = card()
        p["attempts"].append(copy.deepcopy(p["attempts"][0]))
        with self.assertRaises(UsefulnessError):
            summarize(p)
        p["attempts"].pop()
        p["attempts"][0]["consent_state"] = "consented"
        with self.assertRaisesRegex(UsefulnessError, "fictional"):
            summarize(p)

    def test_cannot_call_fictional_card_real(self):
        p = card()
        p["synthetic"] = False
        with self.assertRaisesRegex(UsefulnessError, "conflated"):
            summarize(p)

    def test_future_source_timestamp_rejected(self):
        p = card()
        p["attempts"][0]["observed_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(UsefulnessError, "future"):
            summarize(p)

if __name__ == "__main__":
    unittest.main()
