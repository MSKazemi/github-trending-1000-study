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
        self.assertEqual(x["net_gco2e_reuse_minus_build"], -700)
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


    def test_malformed_evidence_type_is_rejected(self):
        p = example()
        p["arms"]["reuse"]["ci"]["evidence"] = []
        with self.assertRaises(EnergyError):
            compare(p)


if __name__ == "__main__":
    unittest.main()
