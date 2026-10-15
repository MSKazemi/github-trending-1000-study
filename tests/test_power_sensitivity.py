"""Synthetic-only checks for methodological power sensitivity; not a real pilot."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.power_sensitivity import PowerPlanError, evaluate


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "power_sensitivity.synthetic.json"


def source():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class PowerSensitivityTests(unittest.TestCase):
    def test_expected_main_effect_and_group_sizes(self):
        result = evaluate(source())
        rows = result["results"]
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["total_assigned_tasks_assumed"], 480)
        self.assertEqual(rows[0]["assumed_marginal_effect_reuse_minus_usual"], 0.10)
        self.assertEqual(rows[0]["design_effect"], 1.0)
        self.assertEqual(rows[0]["effective_tasks_per_arm_approx"], 120.0)
        self.assertFalse(result["covered_primary_throughput_endpoint"])

    def test_higher_icc_reduces_approx_power(self):
        a = evaluate(source())["results"]
        self.assertGreater(a[0]["normal_approx_rejection_probability"],
                           a[1]["normal_approx_rejection_probability"])
        self.assertGreater(a[1]["design_effect"], a[0]["design_effect"])

    def test_more_independent_clusters_increases_power(self):
        a = evaluate(source())["results"]
        self.assertGreater(a[2]["normal_approx_rejection_probability"],
                           a[1]["normal_approx_rejection_probability"])

    def test_null_effect_has_nominal_rejection_probability(self):
        d = source()
        for scenario in d["scenarios"]:
            for arm in scenario["arm_acceptance_probabilities"]:
                scenario["arm_acceptance_probabilities"][arm] = "0.50"
        for r in evaluate(d)["results"]:
            self.assertAlmostEqual(r["normal_approx_rejection_probability"], 0.05, places=6)
            self.assertEqual(r["estimand_sign"], "equal_assumed_rates")

    def test_one_task_per_cluster_is_independent_of_icc(self):
        d = source()
        d["scenarios"][0]["tasks_per_cluster"] = 1
        d["scenarios"][1]["tasks_per_cluster"] = 1
        a = evaluate(d)["results"]
        self.assertEqual(a[0]["design_effect"], 1.0)
        self.assertEqual(a[1]["design_effect"], 1.0)
        self.assertEqual(a[0]["normal_approx_rejection_probability"],
                         a[1]["normal_approx_rejection_probability"])

    def test_negative_effect_is_not_reported_as_positive_benefit(self):
        d = source()
        scenario = d["scenarios"][0]
        p = scenario["arm_acceptance_probabilities"]
        p["human_reuse_first"], p["human_usual"] = p["human_usual"], p["human_reuse_first"]
        p["agent_reuse_first"], p["agent_usual"] = p["agent_usual"], p["agent_reuse_first"]
        a = evaluate(d)["results"][0]
        self.assertEqual(a["estimand_sign"], "reuse_lower")
        self.assertEqual(a["assumed_marginal_effect_reuse_minus_usual"], -0.10)

    def test_reject_unfrozen_real_study_and_unsupported_endpoints(self):
        for key, value in (("dataset_kind", "pilot"), ("outcome", "throughput_human_hour"),
                           ("estimand", "agent_effect"), ("schema_version", "2.0")):
            d = source()
            d[key] = value
            with self.subTest(key=key), self.assertRaises(PowerPlanError):
                evaluate(d)

    def test_reject_invalid_probabilities_and_alpha(self):
        for bad in (0.05, "NaN", "1", "0", "0.000000", "-0.1", None, "0.1234567"):
            d = source()
            d["two_sided_alpha"] = bad
            with self.subTest(alpha=bad), self.assertRaises(PowerPlanError):
                evaluate(d)
        for bad in (True, 0, 1, "1", "0", "1.000000", "-0.01", "NaN"):
            d = source()
            d["scenarios"][0]["arm_acceptance_probabilities"]["agent_usual"] = bad
            with self.subTest(probability=bad), self.assertRaises(PowerPlanError):
                evaluate(d)

    def test_reject_invalid_icc_and_cluster_counts(self):
        for bad in ("1", "-0.01", "NaN", 0.2):
            d = source()
            d["scenarios"][0]["intracluster_correlation"] = bad
            with self.subTest(icc=bad), self.assertRaises(PowerPlanError):
                evaluate(d)
        for key, bad in (("clusters_per_arm", 29), ("clusters_per_arm", True),
                         ("clusters_per_arm", 10001), ("tasks_per_cluster", 0),
                         ("tasks_per_cluster", 1001)):
            d = source()
            d["scenarios"][0][key] = bad
            with self.subTest(key=key, value=bad), self.assertRaises(PowerPlanError):
                evaluate(d)

    def test_reject_missing_arm_and_duplicate_scenarios(self):
        d = source()
        del d["scenarios"][0]["arm_acceptance_probabilities"]["agent_reuse_first"]
        with self.assertRaises(PowerPlanError):
            evaluate(d)
        d = source()
        d["scenarios"][1]["scenario_id"] = d["scenarios"][0]["scenario_id"]
        with self.assertRaises(PowerPlanError):
            evaluate(d)

    def test_cli_sample_and_duplicate_json_keys_fail_closed(self):
        cmd = [sys.executable, "-m", "trending_study.power_sensitivity", "--input", str(FIXTURE)]
        ok = subprocess.run(cmd, text=True, capture_output=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(len(json.loads(ok.stdout)["results"]), 3)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"a":1,"a":2}', encoding="utf-8")
            bad = subprocess.run([*cmd[:-1], str(path)], text=True, capture_output=True)
            self.assertEqual(bad.returncode, 2)
            self.assertIn("duplicate JSON key", bad.stderr)


if __name__ == "__main__":
    unittest.main()
