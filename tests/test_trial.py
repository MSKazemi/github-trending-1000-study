"""Synthetic-only trial instrument checks; no real developer or task outcomes."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.trial import ARMS, TrialError, assign, audit


FIXTURES = Path(__file__).resolve().parents[1] / "examples"


def source():
    return json.loads((FIXTURES / "trial_frame.synthetic.json").read_text(encoding="utf-8"))


def results():
    return json.loads((FIXTURES / "trial_outcomes.synthetic.json").read_text(encoding="utf-8"))


class TrialTests(unittest.TestCase):
    def test_assignment_repeats_and_counts_all_tasks(self):
        frame = source()
        first = assign(frame)
        self.assertEqual(first, assign(frame))
        self.assertEqual(len(first["assigned"]), 8)
        self.assertEqual(len(first["excluded_before_assignment"]), 1)
        self.assertEqual(set(first["allocation_counts"]), set(ARMS))
        self.assertEqual(sorted(first["allocation_counts"].values()), [2, 2, 2, 2])
        reversed_frame = copy.deepcopy(frame)
        reversed_frame["tasks"].reverse()
        a = assign(reversed_frame)
        self.assertEqual(first["assigned"], a["assigned"])
        self.assertEqual(first["allocation_counts"], a["allocation_counts"])

    def test_all_task_itt_includes_refused_failed_pending(self):
        a = audit(source(), assign(source()), results())
        self.assertEqual(a["sampled_tasks"], 9)
        self.assertEqual(a["all_assigned_tasks"], 8)
        self.assertEqual(a["outcome_records"], 8)
        self.assertEqual(a["preassignment_exclusions"], 1)
        self.assertEqual(a["pending_count"], 1)
        self.assertEqual(a["missing_human_minutes"], 1)
        self.assertEqual(sum(item["accepted"] for item in a["by_arm"].values()), 4)
        self.assertTrue(any(v["accepted_per_human_hour"] is None for v in a["by_arm"].values()))

    def test_missing_or_extra_outcomes_rejected(self):
        data = results()
        data["outcomes"].pop()
        with self.assertRaisesRegex(TrialError, "every assigned task"):
            audit(source(), assign(source()), data)
        data = results()
        data["outcomes"].append(dict(data["outcomes"][0]))
        with self.assertRaisesRegex(TrialError, "duplicate outcome"):
            audit(source(), assign(source()), data)

    def test_unknown_opportunity_or_leakage_field_rejected(self):
        data = source()
        data["tasks"][0]["reuse_opportunity"] = "viable"
        with self.assertRaisesRegex(TrialError, "unexpected"):
            assign(data)
        data = source()
        data["tasks"][0]["accepted"] = True
        with self.assertRaises(TrialError):
            assign(data)

    def test_assignment_tampering_rejected(self):
        frame = source()
        allocation = assign(frame)
        allocation["assigned"][0]["arm"] = "agent_reuse_first"
        with self.assertRaisesRegex(TrialError, "disagree"):
            audit(frame, allocation, results())

    def test_invalid_seed_and_changed_frame_fail(self):
        data = source()
        data["randomization_seed"] = True
        with self.assertRaises(TrialError):
            assign(data)
        data = source()
        original = assign(data)
        data["frame_locked_at_utc"] = "2026-10-11T14:00:00Z"
        with self.assertRaises(TrialError):
            audit(data, original, results())

    def test_task_dates_and_digests(self):
        data = source()
        data["tasks"][0]["baseline_utc"] = "2026-10-13T00:00:00Z"
        with self.assertRaises(TrialError):
            assign(data)
        data = source()
        data["tasks"][0]["acceptance_sha256"] = "bad-sha"
        with self.assertRaises(TrialError):
            assign(data)
        data = source()
        data["frame_locked_at_utc"] = "2026-10-11T13:00:00+01:00"
        with self.assertRaises(TrialError):
            assign(data)

    def test_duplicate_task_and_cross_cluster_family(self):
        data = source()
        data["tasks"][1]["task_id"] = data["tasks"][0]["task_id"]
        with self.assertRaises(TrialError):
            assign(data)
        data = source()
        data["tasks"][1]["family_id"] = data["tasks"][0]["family_id"]
        with self.assertRaisesRegex(TrialError, "multiple clusters"):
            assign(data)

    def test_cluster_stratum_consistency_and_valid_preexclude(self):
        data = source()
        data["tasks"][1]["cluster_id"] = data["tasks"][0]["cluster_id"]
        data["tasks"][1]["language"] = "go"
        with self.assertRaisesRegex(TrialError, "blocking strata"):
            assign(data)
        data = source()
        data["tasks"][-1]["exclusion_reason"] = "no_reusable_library"
        with self.assertRaisesRegex(TrialError, "prespecified"):
            assign(data)

    def test_pilot_requires_consent_and_ethics(self):
        data = source()
        data["dataset_kind"] = "pilot"
        with self.assertRaises(TrialError):
            assign(data)
        data["ethics_review_ref"] = "research-team-approval-ref"
        for task in data["tasks"]:
            task["source_kind"] = "opt_in"
            task["consent_ref"] = "opt-in-consent-ref"
        self.assertEqual(len(assign(data)["assigned"]), 8)
        data["tasks"][0]["consent_ref"] = None
        with self.assertRaises(TrialError):
            assign(data)

    def test_accepted_requires_independent_review_and_security_rights(self):
        frame = source()
        data = results()
        data["outcomes"][0]["independent_review_ref"] = None
        with self.assertRaises(TrialError):
            audit(frame, assign(frame), data)
        data = results()
        data["outcomes"][0]["security_gate"] = "unknown"
        with self.assertRaises(TrialError):
            audit(frame, assign(frame), data)

    def test_missing_time_remains_null_not_zero(self):
        frame = source()
        summary = audit(frame, assign(frame), results())
        failed_arm = next(x["arm"] for x in assign(frame)["assigned"] if x["task_id"] == "synthetic-T03")
        self.assertIsNone(summary["by_arm"][failed_arm]["human_active_minutes_total"])
        self.assertIsNone(summary["by_arm"][failed_arm]["accepted_per_human_hour"])

    def test_cli_round_trip_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "alloc.json"
            cmd = [sys.executable, "-m", "trending_study.trial", "assign", "--frame", str(FIXTURES / "trial_frame.synthetic.json"), "--output", str(path)]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(json.loads(path.read_text())["assigned"], assign(source())["assigned"])
            double = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(double.returncode, 0)
            audit_cmd = [sys.executable, "-m", "trending_study.trial", "audit", "--frame", str(FIXTURES / "trial_frame.synthetic.json"), "--assignments", str(path), "--outcomes", str(FIXTURES / "trial_outcomes.synthetic.json")]
            report = subprocess.run(audit_cmd, capture_output=True, text=True)
            self.assertEqual(report.returncode, 0, report.stderr)
            self.assertEqual(json.loads(report.stdout)["dataset_kind"], "synthetic")


if __name__ == "__main__":
    unittest.main()
