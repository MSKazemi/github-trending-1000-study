"""Issue #23 synthetic scenario-envelope tests: no real energy measured."""
import copy
import json
from pathlib import Path
import unittest

from trending_study.lifecycle_break_even import BoundaryError
from trending_study.lifecycle_sensitivity import evaluate

SOURCE = Path(__file__).resolve().parents[1] / "examples/lifecycle_sensitivity.synthetic.json"


def fixture():
    return json.loads(SOURCE.read_text(encoding="utf-8"))


class LifecycleSensitivityTests(unittest.TestCase):
    def test_same_task_synthetic_range_and_signed_direction(self):
        report = evaluate(fixture())
        self.assertEqual(report["scenario_count"], 3)
        self.assertEqual(report["dataset_kind"], "synthetic")
        self.assertEqual(report["calculation_status"],
                         "deterministic_sensitivity_envelope_not_confidence_interval")
        self.assertIn("NOT a statistical confidence interval", report["warning"])
        points = {row["n_uses"]: row for row in report["points"]}
        self.assertEqual((points[100]["delta_min_kwh"],
                          points[100]["delta_max_kwh"]), ("3.000000", "10.000000"))
        self.assertEqual(points[100]["direction_across_scenarios"],
                         "reuse_lower_in_every_supplied_scenario")
        self.assertEqual((points[266]["delta_min_kwh"],
                          points[266]["delta_max_kwh"]), ("-3.640000", "8.340000"))
        self.assertEqual(points[266]["direction_across_scenarios"],
                         "mixed_or_zero_across_supplied_scenarios")
        self.assertEqual((points[300]["delta_min_kwh"],
                          points[300]["delta_max_kwh"]), ("-5.000000", "8.000000"))
        self.assertEqual(report["excluded_terms"], [
            "cloud_inference", "embodied_hardware", "water", "upstream_burden"
        ])

    def test_missing_one_included_term_blocks_every_range(self):
        data = fixture()
        data["scenarios"][1]["input"]["strategies"]["reuse"]["pre_run"]["maintenance"] = {
            "kwh": None, "basis": "unknown", "evidence_ref": None,
        }
        result = evaluate(data)
        self.assertEqual(result["calculation_status"], "incomplete_no_envelope")
        self.assertEqual(result["missing_scenarios"], [{
            "scenario_id": "higher_reuse_cost",
            "missing_included_terms": ["reuse.maintenance"],
        }])
        self.assertTrue(all(row["delta_min_kwh"] is None and
                            row["delta_max_kwh"] is None and
                            row["direction_across_scenarios"] == "unknown"
                            for row in result["points"]))

    def test_cross_task_or_boundary_mismatch_fails_closed(self):
        mutations = [
            ("task_spec_sha256", "c" * 64),
            ("acceptance_sha256", "d" * 64),
            ("functional_unit_id", "different_task"),
            ("boundary_id", "different_boundary"),
            ("horizon_days", 120),
            ("excluded_terms", ["other_omission"]),
            ("n_uses", [0, 10]),
            ("dataset_kind", "pilot"),
        ]
        for field, value in mutations:
            d = fixture()
            d["scenarios"][1]["input"][field] = value
            with self.subTest(field=field):
                with self.assertRaisesRegex(BoundaryError, "same task|share task"):
                    evaluate(d)

    def test_duplicate_scenario_and_too_many_cases_refused(self):
        d = fixture()
        d["scenarios"][1]["scenario_id"] = "base"
        with self.assertRaisesRegex(BoundaryError, "unique"):
            evaluate(d)
        d = fixture()
        d["scenarios"] = d["scenarios"][:1]
        with self.assertRaisesRegex(BoundaryError, "2 to 16"):
            evaluate(d)
        d = fixture()
        d["scenarios"] = d["scenarios"] * 6
        with self.assertRaisesRegex(BoundaryError, "2 to 16"):
            evaluate(d)

    def test_invalid_embedded_energy_and_fake_metering_refused(self):
        d = fixture()
        d["scenarios"][0]["input"]["strategies"]["build"]["runtime_per_use"]["kwh"] = "NaN"
        with self.assertRaisesRegex(BoundaryError, "nonnegative decimal"):
            evaluate(d)
        d = fixture()
        d["scenarios"][0]["input"]["strategies"]["reuse"]["runtime_per_use"]["basis"] = "metered"
        with self.assertRaisesRegex(BoundaryError, "synthetic dataset"):
            evaluate(d)

    def test_input_remains_unchanged(self):
        d = fixture()
        original = copy.deepcopy(d)
        evaluate(d)
        self.assertEqual(d, original)


if __name__ == "__main__":
    unittest.main()
