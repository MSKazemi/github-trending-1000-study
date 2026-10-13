"""Synthetic kWh examples only, never actual energy measurements."""
import unittest
from trending_study.energy_boundary import COMPONENTS, EnergyError, compare


def example():
    def arm(value):
        return {x: {"evidence": "modeled", "source_ref": "synthetic model only",
                    "kwh": value} for x in COMPONENTS}
    return {"functional_unit": {"task_id": "fake-1", "horizon_days": 90,
                                "boundary_description": "fictional accepted task",
                                "reuse_task_accepted": True, "build_task_accepted": True},
            "arms": {"reuse": arm(1), "build": arm(2)},
            "grid_intensity_gco2e_per_kwh": 100}


class EnergyBoundaryTests(unittest.TestCase):
    def test_synthetic_net_is_signed(self):
        x = compare(example())
        self.assertTrue(x["comparable"])
        self.assertEqual(x["net_kwh_reuse_minus_build"], -7)
        self.assertIsNone(x["net_gco2e_reuse_minus_build"])
        self.assertEqual(x["grid_only_scenario_gco2e_delta"], -400)
        self.assertIn("model_inference", x["modeled_reuse"])

    def test_missing_inference_yields_unknown_net(self):
        p = example()
        p["arms"]["reuse"]["model_inference"] = {"evidence": "unavailable", "kwh": None}
        x = compare(p)
        self.assertFalse(x["comparable"])
        self.assertIsNone(x["net_kwh_reuse_minus_build"])

    def test_rejects_tokens_as_kwh(self):
        p = example()
        p["arms"]["build"]["ci"]["kwh"] = "200 tokens"
        with self.assertRaises(EnergyError):
            compare(p)

    def test_large_finite_inputs_cannot_overflow_totals(self):
        p = example()
        for part in COMPONENTS:
            p["arms"]["reuse"][part]["kwh"] = 1e308
        with self.assertRaisesRegex(EnergyError, "summed energy"):
            compare(p)

    def test_huge_integer_is_controlled_validation_failure(self):
        p = example()
        p["arms"]["build"]["ci"]["kwh"] = 10 ** 1000
        with self.assertRaisesRegex(EnergyError, "nonnegative finite"):
            compare(p)

    def test_grid_scenario_overflow_is_rejected_not_infinity_json(self):
        p = example()
        p["grid_intensity_gco2e_per_kwh"] = 1e308
        with self.assertRaisesRegex(EnergyError, "grid scenario carbon"):
            compare(p)

    def test_rejects_negative_or_nan(self):
        p = example()
        p["arms"]["build"]["ci"]["kwh"] = float("nan")
        with self.assertRaises(EnergyError):
            compare(p)

    def test_mismatched_accepted_task(self):
        p = example()
        p["functional_unit"]["build_task_accepted"] = False
        self.assertFalse(compare(p)["comparable"])

    def test_rejects_undeclared_upstream_boundary(self):
        p = example()
        del p["arms"]["reuse"]["upstream_support"]
        with self.assertRaises(EnergyError):
            compare(p)

    def test_no_carbon_without_grid_intensity(self):
        p = example()
        p["grid_intensity_gco2e_per_kwh"] = None
        self.assertIsNone(compare(p)["net_gco2e_reuse_minus_build"])
        self.assertIsNone(compare(p)["grid_only_scenario_gco2e_delta"])


    def test_unaccepted_task_still_requires_valid_energy_ledger(self):
        p = example()
        p["functional_unit"]["build_task_accepted"] = False
        del p["arms"]["build"]["upstream_support"]
        with self.assertRaisesRegex(EnergyError, "all seven"):
            compare(p)

    def test_unaccepted_task_cannot_hide_invalid_grid_intensity(self):
        p = example()
        p["functional_unit"]["build_task_accepted"] = False
        for invalid in ("garbage", -1, float("nan"), True):
            with self.subTest(invalid=invalid):
                p["grid_intensity_gco2e_per_kwh"] = invalid
                with self.assertRaisesRegex(EnergyError, "grid_intensity"):
                    compare(p)


    def test_modeled_components_never_masquerade_as_measured(self):
        r = compare(example())
        self.assertEqual(r["modeling_or_measurement_status"], "mixed_modeled_scenario_only")
        self.assertIsNone(r["net_gco2e_reuse_minus_build"])
        p = example()
        p["arms"]["reuse"]["model_inference"] = {"evidence":"unavailable", "kwh":None}
        self.assertEqual(compare(p)["modeling_or_measurement_status"], "incomplete_boundary")

    def test_malformed_evidence_type_is_rejected(self):
        p = example()
        p["arms"]["reuse"]["ci"]["evidence"] = []
        with self.assertRaises(EnergyError):
            compare(p)


if __name__ == "__main__":
    unittest.main()
