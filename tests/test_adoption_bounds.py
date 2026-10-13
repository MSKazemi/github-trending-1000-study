"""Synthetic, finite-panel bounds only; no inferred real users."""
import copy
import json
from pathlib import Path
import unittest
from trending_study.adoption_bounds import AdoptionError, summarize

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "adoption_signals.synthetic.json"

def fake():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))

class AdoptionBoundsTests(unittest.TestCase):
    def test_unknown_and_not_applicable_denominators(self):
        result = summarize([fake()])
        a = result["signals"]["independently_verified_downstream_integration"]
        b = result["signals"]["desktop_gui_completion"]
        self.assertEqual((a["eligible"], a["unknown"]), (1, 1))
        self.assertEqual((a["logical_lower"], a["logical_upper"]), (0.0, 1.0))
        self.assertEqual((b["eligible"], b["na"]), (0, 1))
        self.assertIsNone(b["logical_lower"])
        self.assertFalse(result["independent_review_authenticated"])

    def test_verified_and_missing_span_are_not_confidence_intervals(self):
        a = fake()
        b = copy.deepcopy(a)
        b["repository_id"] = 100000000
        b["signals"][0].update(status="observed_verified",
                               evidence_source_url="https://example.org/fixture",
                               observed_at_utc="2026-10-12T12:00:00Z",
                               independent_reviewer="synthetic-observer")
        result = summarize([a, b])
        x = result["signals"]["independently_verified_downstream_integration"]
        self.assertEqual((x["eligible"], x["verified"], x["unknown"]), (2, 1, 1))
        self.assertEqual((x["logical_lower"], x["logical_upper"]), (0.5, 1.0))
        self.assertTrue(result["bounds_are_not_population_estimates_or_confidence_intervals"])

    def test_ineligible_is_not_negative(self):
        c = fake()
        c["signals"][1]["status"] = "observed_negative"
        with self.assertRaisesRegex(AdoptionError, "not_applicable"):
            summarize([c])

    def test_duplicate_repo_is_not_two_independent_users(self):
        with self.assertRaisesRegex(AdoptionError, "double-count"):
            summarize([fake(), fake()])

    def test_future_attestation_does_not_qualify(self):
        c = fake()
        c["signals"][0].update(status="observed_verified",
                               evidence_source_url="https://example.org/data",
                               observed_at_utc="2099-01-01T00:00:00Z",
                               independent_reviewer="synthetic-observer")
        with self.assertRaisesRegex(AdoptionError, "future"):
            summarize([c])

    def test_unknown_cannot_keep_fake_observation(self):
        c = fake()
        c["signals"][0]["evidence_source_url"] = "https://example.org/data"
        with self.assertRaisesRegex(AdoptionError, "false verified"):
            summarize([c])

if __name__ == "__main__":
    unittest.main()
