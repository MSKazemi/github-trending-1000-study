"""Synthetic arithmetic crosswalk for the repository's two energy instruments.

Never authenticates kWh, task equivalence or environmental impact. Compares
exactly one accepted use under a fully declared, matched synthetic boundary.
"""
from decimal import Decimal
import unittest

from trending_study.energy_boundary import COMPONENTS, compare as compare_boundary
from trending_study.lifecycle_break_even import evaluate as evaluate_lifecycle


def _boundary_card(build, reuse):
    def arm(components):
        assert set(components) == set(COMPONENTS)
        return {key: {"evidence": "modeled", "source_ref": "synthetic-parameter",
                      "kwh": float(value)}
                for key, value in components.items()}
    return {"functional_unit": {"task_id": "synthetic-accepted-one-use",
                                "horizon_days": 90,
                                "boundary_description": "fictional identical accepted task, one use",
                                "reuse_task_accepted": True,
                                "build_task_accepted": True},
            "arms": {"build": arm(build), "reuse": arm(reuse)}}


def _lifecycle_card(build, reuse):
    def value(kwh):
        return {"kwh": format(Decimal(str(kwh)), "f"),
                "basis": "synthetic", "evidence_ref": "synthetic-parameter"}

    def arm(c):
        return {"pre_run": {
            "discovery": value(0),
            "development": value(Decimal(str(c["local_development"])) +
                                 Decimal(str(c["model_inference"]))),
            "verification": value(c["ci"]),
            "maintenance": value(c["maintenance"]),
            "other": value(Decimal(str(c["embodied"])) +
                           Decimal(str(c["upstream_support"])))},
            "runtime_per_use": value(c["runtime"])}
    return {"schema_version": "1.0", "dataset_kind": "synthetic",
            "functional_unit_id": "synthetic-accepted-one-use",
            "task_spec_sha256": "a" * 64, "acceptance_sha256": "b" * 64,
            "horizon_days": 90, "boundary_id": "synthetic-exact-crosswalk",
            "excluded_terms": [], "n_uses": [1],
            "strategies": {"build": arm(build), "reuse": arm(reuse)}}


def _components(development, ci, inference, runtime, maintenance, embodied, upstream):
    return dict(local_development=development, ci=ci, model_inference=inference,
                runtime=runtime, maintenance=maintenance, embodied=embodied,
                upstream_support=upstream)


class EnergyModelCrosswalkTests(unittest.TestCase):
    def test_signed_energy_agrees_on_matched_one_use(self):
        build = _components(3, 2, 2, 1, 1, 1, 1)
        reuse = _components(2, 1, 1, 1, 1, 1, 1)
        boundary = compare_boundary(_boundary_card(build, reuse))
        lifecycle = evaluate_lifecycle(_lifecycle_card(build, reuse))
        self.assertTrue(boundary["comparable"])
        self.assertEqual(boundary["net_kwh_reuse_minus_build"], -3)
        self.assertEqual(lifecycle["calculation_status"],
                         "scenario_only_no_uncertainty_interval")
        delta = Decimal(lifecycle["points"][0]["delta_build_minus_reuse_kwh"])
        self.assertEqual(delta, -Decimal(str(boundary["net_kwh_reuse_minus_build"])))
        self.assertIsNone(boundary["net_gco2e_reuse_minus_build"])

    def test_missing_included_component_blocks_both_models(self):
        build = _components(3, 2, 2, 1, 1, 1, 1)
        reuse = _components(2, 1, 1, 1, 1, 1, 1)
        boundary = _boundary_card(build, reuse)
        boundary["arms"]["reuse"]["model_inference"] = {
            "evidence": "unavailable", "kwh": None}
        a = compare_boundary(boundary)
        self.assertFalse(a["comparable"])
        self.assertIsNone(a["net_kwh_reuse_minus_build"])
        lifecycle = _lifecycle_card(build, reuse)
        lifecycle["strategies"]["reuse"]["pre_run"]["development"] = {
            "basis": "unknown", "kwh": None, "evidence_ref": None}
        b = evaluate_lifecycle(lifecycle)
        self.assertEqual(b["calculation_status"], "incomplete_no_point_estimate")
        self.assertIsNone(b["points"][0]["delta_build_minus_reuse_kwh"])

    def test_unaccepted_functional_task_never_gives_net_energy(self):
        build = _components(3, 2, 2, 1, 1, 1, 1)
        reuse = _components(2, 1, 1, 1, 1, 1, 1)
        boundary = _boundary_card(build, reuse)
        boundary["functional_unit"]["reuse_task_accepted"] = False
        result = compare_boundary(boundary)
        self.assertFalse(result["comparable"])
        self.assertIsNone(result["net_kwh_reuse_minus_build"])


if __name__ == "__main__":
    unittest.main()
