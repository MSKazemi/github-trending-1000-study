import copy
import unittest

from trending_study.lifecycle_break_even import BoundaryError, evaluate


def energy(kwh):
    return {"kwh": kwh, "basis": "synthetic", "evidence_ref": "SYNTHETIC SCENARIO"}


def scenario():
    def arm(pre, runtime):
        return {"pre_run": {
            "discovery": energy("0"),
            "development": energy(pre),
            "verification": energy("0"),
            "maintenance": energy("0"),
            "other": energy("0"),
        }, "runtime_per_use": energy(runtime)}
    return {
        "schema_version": "1.0", "dataset_kind": "synthetic",
        "functional_unit_id": "same_accepted_task", "task_spec_sha256": "a" * 64,
        "acceptance_sha256": "b" * 64, "horizon_days": 90,
        "boundary_id": "hypothetical_local_and_runtime",
        "excluded_terms": ["cloud_inference", "embodied_hardware", "water", "upstream_burden"],
        "n_uses": [0, 100, 267, 300],
        "strategies": {"build": arm("12", "0.01"), "reuse": arm("4", "0.04")},
    }


class LifecycleBreakEvenTests(unittest.TestCase):
    def test_synthetic_crossing_and_sign(self):
        a = evaluate(scenario())
        self.assertEqual(a["calculation_status"], "scenario_only_no_uncertainty_interval")
        self.assertEqual(a["crossing"]["kind"], "reuse_lower_below_threshold")
        self.assertEqual(a["crossing"]["n_uses_equal_approx"], "266.666667")
        self.assertEqual(a["crossing"]["last_integer_n_reuse_lower"], 266)
        self.assertEqual(a["crossing"]["first_integer_n_build_lower"], 267)
        self.assertIsNone(a["crossing"]["integer_n_equal"])
        self.assertEqual(a["points"][0]["delta_build_minus_reuse_kwh"], "8.000000")
        self.assertEqual(a["points"][-1]["delta_build_minus_reuse_kwh"], "-1.000000")
        self.assertEqual(a["scope"], "partial_declared_boundary")

    def test_unknown_propagates_without_zero_imputation(self):
        d = scenario()
        d["strategies"]["reuse"]["pre_run"]["maintenance"] = {
            "kwh": None, "basis": "unknown", "evidence_ref": None}
        a = evaluate(d)
        self.assertEqual(a["calculation_status"], "incomplete_no_point_estimate")
        self.assertEqual(a["missing_included_terms"], ["reuse.maintenance"])
        self.assertIsNone(a["points"][0]["delta_build_minus_reuse_kwh"])
        self.assertIsNone(a["crossing"])

    def test_unknown_cannot_claim_zero(self):
        d = scenario()
        d["strategies"]["reuse"]["pre_run"]["maintenance"] = {
            "kwh": "0", "basis": "unknown", "evidence_ref": None}
        with self.assertRaises(BoundaryError):
            evaluate(d)

    def test_negative_and_bool_workloads_rejected(self):
        for value in (-1, True, 0.5):
            d = scenario()
            d["n_uses"] = [value]
            with self.assertRaises(BoundaryError):
                evaluate(d)

    def test_unbounded_workload_or_horizon_is_rejected(self):
        for count in (1_000_000_001, 10**90):
            d = scenario()
            d["n_uses"] = [count]
            with self.assertRaises(BoundaryError):
                evaluate(d)
        d = scenario()
        d["horizon_days"] = 3651
        with self.assertRaises(BoundaryError):
            evaluate(d)

    def test_exact_integer_equality_not_called_savings(self):
        d = scenario()
        d["strategies"]["reuse"]["runtime_per_use"]["kwh"] = "4.01"
        d["n_uses"] = [1, 2, 3]
        a = evaluate(d)
        self.assertEqual(a["crossing"]["integer_n_equal"], 2)
        self.assertEqual(a["crossing"]["last_integer_n_reuse_lower"], 1)
        self.assertEqual(a["crossing"]["first_integer_n_build_lower"], 3)
        self.assertEqual(a["points"][1]["delta_build_minus_reuse_kwh"], "0.000000")

    def test_rounding_near_zero_cannot_hide_integer_crossover(self):
        d = scenario()
        d["strategies"]["build"]["pre_run"]["development"]["kwh"] = "0.000001"
        d["strategies"]["reuse"]["pre_run"]["development"]["kwh"] = "0"
        d["strategies"]["build"]["runtime_per_use"]["kwh"] = "0"
        d["strategies"]["reuse"]["runtime_per_use"]["kwh"] = "999999999.999999"
        d["n_uses"] = [0, 1]
        a = evaluate(d)
        self.assertEqual(a["crossing"]["last_integer_n_reuse_lower"], 0)
        self.assertEqual(a["crossing"]["first_integer_n_build_lower"], 1)
        self.assertEqual(a["points"][1]["delta_build_minus_reuse_kwh"], "-999999999.999998")

    def test_zero_horizon_cannot_claim_lifecycle_comparison(self):
        d = scenario()
        d["horizon_days"] = 0
        with self.assertRaisesRegex(BoundaryError, "strictly positive"):
            evaluate(d)

    def test_unhashable_evidence_basis_fails_closed(self):
        d = scenario()
        d["strategies"]["build"]["pre_run"]["discovery"]["basis"] = []
        with self.assertRaisesRegex(BoundaryError, "invalid evidence"):
            evaluate(d)

    def test_invalid_nonfinite_decimal_rejected(self):
        for val in ("NaN", "Infinity", "-1", "1e99", 3.2, None):
            d = scenario()
            d["strategies"]["build"]["runtime_per_use"]["kwh"] = val
            with self.assertRaises(BoundaryError):
                evaluate(d)

    def test_synthetic_cannot_claim_metered(self):
        d = scenario()
        d["strategies"]["reuse"]["runtime_per_use"]["basis"] = "metered"
        with self.assertRaises(BoundaryError):
            evaluate(d)

    def test_reuse_lower_at_all_counts(self):
        d = scenario()
        d["strategies"]["reuse"]["runtime_per_use"]["kwh"] = "0.005"
        self.assertEqual(evaluate(d)["crossing"]["kind"], "reuse_never_higher_for_nonnegative_n")

    def test_reuse_lower_only_after_threshold(self):
        d = scenario()
        d["strategies"]["reuse"]["pre_run"]["development"]["kwh"] = "14"
        d["strategies"]["reuse"]["runtime_per_use"]["kwh"] = "0.005"
        a = evaluate(d)
        self.assertEqual(a["crossing"]["kind"], "reuse_lower_above_threshold")
        self.assertEqual(a["crossing"]["n_uses_equal_approx"], "400.000000")
        self.assertEqual(a["crossing"]["last_integer_n_build_lower"], 399)
        self.assertEqual(a["crossing"]["first_integer_n_reuse_lower"], 401)
        self.assertEqual(a["crossing"]["integer_n_equal"], 400)

    def test_reuse_never_lower(self):
        d = scenario()
        d["strategies"]["reuse"]["pre_run"]["development"]["kwh"] = "14"
        self.assertEqual(evaluate(d)["crossing"]["kind"], "reuse_never_lower_for_nonnegative_n")

    def test_nonzero_unknown_included_term_must_not_be_excluded(self):
        d = scenario()
        d["excluded_terms"].append("maintenance")
        with self.assertRaises(BoundaryError):
            evaluate(d)


if __name__ == "__main__":
    unittest.main()
