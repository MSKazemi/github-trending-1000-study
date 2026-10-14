"""Offline task-cost audit regression tests: all values are synthetic."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.task_costs import CostAuditError, audit_costs
from trending_study.trial import TrialError, assign


FIXTURES = Path(__file__).resolve().parents[1] / "examples"


def read(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def inputs():
    frame = read("trial_frame.synthetic.json")
    return (frame, assign(frame), read("trial_outcomes.synthetic.json"),
            read("task_costs.synthetic.json"))


class TaskCostTests(unittest.TestCase):
    def test_full_trial_denominator_and_no_fabricated_efficiency(self):
        report = audit_costs(*inputs())
        self.assertEqual(report["dataset_kind"], "synthetic")
        self.assertEqual(report["trial_status"], "synthetic_demonstration")
        self.assertEqual(report["overall"]["assigned"], 8)
        self.assertEqual(report["overall"]["accepted"], 4)
        self.assertEqual(report["overall"]["status_counts"]["refused"], 1)
        self.assertEqual(report["overall"]["status_counts"]["failed"], 1)
        self.assertEqual(report["overall"]["status_counts"]["abandoned"], 1)
        self.assertEqual(report["overall"]["status_counts"]["pending"], 1)
        self.assertEqual(report["overall"]["missing_human_tasks"], 2)
        self.assertEqual(report["overall"]["missing_event_tasks"], 3)
        self.assertEqual(report["overall"]["missing_monetary_tasks"], 3)
        self.assertIsNone(report["overall"]["accepted_per_human_hour"])
        self.assertIsNone(report["overall"]["cost_per_accepted_task_usd"])
        self.assertIsNone(report["overall"]["token_totals"]["input_tokens"])
        self.assertEqual(len(report["tasks"]), 8)
        self.assertFalse(any("co2" in key or "kwh" in key for key in report["overall"]))

    def test_empty_randomized_arms_remain_explicitly_unmeasured(self):
        frame, allocations, outcomes, ledger = inputs()
        for task in frame["tasks"][1:]:
            task["eligibility_status"] = "excluded_pre_assignment"
            task["exclusion_reason"] = "duplicate"
        allocations = assign(frame)
        outcomes["outcomes"] = outcomes["outcomes"][:1]
        ledger["task_costs"] = ledger["task_costs"][:1]
        report = audit_costs(frame, allocations, outcomes, ledger)
        self.assertEqual(report["overall"]["assigned"], 1)
        self.assertEqual(len(report["by_arm"]), 4)
        empty = [v for v in report["by_arm"].values() if v["assigned"] == 0]
        self.assertEqual(len(empty), 3)
        self.assertTrue(all(v["human_active_minutes_total"] is None for v in empty))
        self.assertTrue(all(v["observed_event_cost_usd"] is None for v in empty))

    def test_measured_per_task_cost_and_predeclared_budgets(self):
        report = audit_costs(*inputs())
        rows = {row["task_id"]: row for row in report["tasks"]}
        first = rows["synthetic-T01"]
        self.assertEqual(first["human_active_minutes"], 30)
        self.assertEqual(first["model_calls"], 2)
        self.assertEqual(first["tool_calls"], 1)
        self.assertEqual(first["retries"], 1)
        self.assertEqual(first["input_tokens"], 175)
        self.assertEqual(first["cached_input_tokens"], 10)
        self.assertEqual(first["recorded_event_wall_minutes"], 8)
        self.assertEqual(first["observed_event_cost_usd"], "0.006")
        self.assertEqual(first["cost_by_basis_usd"]["synthetic"], "0.006")
        self.assertEqual(first["budget_alerts"]["retries"], "exceeded")
        self.assertEqual(first["budget_alerts"]["event_cost_usd"], "exceeded")
        self.assertEqual(first["budget_alerts"]["human_minutes"], "within")
        self.assertEqual(rows["synthetic-T06"]["budget_alerts"]["human_minutes"], "exceeded")
        self.assertEqual(rows["synthetic-T02"]["observed_event_cost_usd"], "0")
        self.assertEqual(rows["synthetic-T02"]["input_tokens"], 0)

    def test_partial_and_missing_are_never_zero(self):
        report = audit_costs(*inputs())
        rows = {row["task_id"]: row for row in report["tasks"]}
        pending = rows["synthetic-T05"]
        self.assertEqual(pending["observed_agent_events"], 1)
        self.assertEqual(pending["human_active_minutes"], 6)
        self.assertIsNone(pending["tool_calls"])
        self.assertIsNone(pending["observed_event_cost_usd"])
        self.assertEqual(pending["budget_alerts"]["event_cost_usd"], "unknown")
        missing = rows["synthetic-T03"]
        for field in ("human_active_minutes", "model_calls", "input_tokens",
                      "recorded_event_wall_minutes", "observed_event_cost_usd"):
            self.assertIsNone(missing[field])

    def test_agent_concurrency_uses_wall_time_union_not_sum(self):
        frame, allocations, outcomes, ledger = inputs()
        first = ledger["task_costs"][0]
        new_event = copy.deepcopy(first["agent_events"][0])
        new_event.update(event_id="synthetic-E-concurrent",
                         started_at_utc="2026-10-11T12:04:00Z",
                         ended_at_utc="2026-10-11T12:06:00Z",
                         input_tokens=0, output_tokens=0, cached_input_tokens=0,
                         amount_usd="0")
        first["agent_events"].append(new_event)
        summary = audit_costs(frame, allocations, outcomes, ledger)
        self.assertEqual(summary["tasks"][0]["recorded_event_wall_minutes"], 8)
        self.assertEqual(summary["tasks"][0]["model_calls"], 3)

    def test_cross_task_actor_overlap_rejected(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][1]["human_intervals"][0]["actor_slot"] = "slot-01"
        with self.assertRaisesRegex(CostAuditError, "overlapping human"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_human_interval_mismatch_rejected(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["human_intervals"][0]["ended_at_utc"] = "2026-10-11T12:09:00Z"
        with self.assertRaisesRegex(CostAuditError, "disagree"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_missing_and_excluded_tasks_cannot_be_silently_skipped(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"].pop()
        with self.assertRaisesRegex(CostAuditError, "every randomized task"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][-1]["task_id"] = "synthetic-T09"
        with self.assertRaisesRegex(CostAuditError, "excluded"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_never_accept_raw_prompt_or_identity_fields(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["prompt"] = "SECRET"
        with self.assertRaisesRegex(CostAuditError, "unexpected"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][0]["source_code"] = "raw private code"
        with self.assertRaisesRegex(CostAuditError, "unexpected"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["human_intervals"][0]["actor_slot"] = "name@example.org"
        with self.assertRaisesRegex(CostAuditError, "pseudonym"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_token_validation_and_cache_consistency(self):
        for field, value in (
            ("input_tokens", True), ("output_tokens", -1), ("cached_input_tokens", 1000)
        ):
            frame, allocations, outcomes, ledger = inputs()
            ledger["task_costs"][0]["agent_events"][0][field] = value
            with self.assertRaises(CostAuditError):
                audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][1]["input_tokens"] = 3
        with self.assertRaisesRegex(CostAuditError, "non-model"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_event_identity_time_and_double_billing(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][5]["agent_events"][0]["event_id"] = "synthetic-E01"
        with self.assertRaisesRegex(CostAuditError, "duplicate event"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][0]["started_at_utc"] = "2026-10-11T11:00:00Z"
        with self.assertRaisesRegex(CostAuditError, "after frame lock"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][2]["amount_usd"] = "0.01"
        with self.assertRaisesRegex(CostAuditError, "double-bill"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_price_precision_unknown_cost_and_coverage(self):
        for amount in (0.3, "NaN", "-1.0", "1e6", "0.1234567"):
            frame, allocations, outcomes, ledger = inputs()
            ledger["task_costs"][0]["agent_events"][0]["amount_usd"] = amount
            with self.assertRaises(CostAuditError):
                audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][0]["amount_usd"] = None
        ledger["task_costs"][0]["agent_events"][0]["cost_basis"] = None
        with self.assertRaisesRegex(CostAuditError, "complete monetary coverage"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["coverage"]["human"] = "missing"
        with self.assertRaisesRegex(CostAuditError, "missing human"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_structured_enum_injections_fail_as_validation_errors(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["coverage"]["events"] = []
        with self.assertRaises(CostAuditError):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][0]["kind"] = {"unknown": True}
        with self.assertRaises(CostAuditError):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["human_intervals"][0]["category"] = []
        with self.assertRaises(CostAuditError):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["agent_events"][0]["cost_basis"] = {}
        with self.assertRaises(CostAuditError):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_budget_must_precede_assignment(self):
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["budget"]["locked_at_utc"] = "2026-10-11T12:05:00Z"
        with self.assertRaisesRegex(CostAuditError, "budget must be locked"):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["task_costs"][0]["budget"]["max_retries"] = -1
        with self.assertRaises(CostAuditError):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_trial_outcome_audit_and_protocol_id_bindings(self):
        frame, allocations, outcomes, ledger = inputs()
        outcomes["outcomes"][0]["security_gate"] = "unknown"
        with self.assertRaises(TrialError):
            audit_costs(frame, allocations, outcomes, ledger)
        frame, allocations, outcomes, ledger = inputs()
        ledger["protocol_id"] = "altered"
        with self.assertRaisesRegex(CostAuditError, "disagrees"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_self_declared_pilot_cannot_bill_synthetic_costs(self):
        frame, _, outcomes, ledger = inputs()
        frame["dataset_kind"] = "pilot"
        frame["ethics_review_ref"] = "SYNTHETIC-ONLY/not-real-consent"
        for task in frame["tasks"]:
            task["source_kind"] = "opt_in"
            task["consent_ref"] = "SYNTHETIC-ONLY/not-real-consent"
        allocations = assign(frame)
        outcomes["dataset_kind"] = "pilot"
        outcomes["frame_sha256"] = allocations["frame_sha256"]
        ledger["dataset_kind"] = "pilot"
        with self.assertRaisesRegex(CostAuditError, "cost basis"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_after_closure_followup_cannot_masquerade_as_in_trial_time(self):
        frame, allocations, outcomes, ledger = inputs()
        task = ledger["task_costs"][0]
        task["human_intervals"].append({
            "actor_slot": "slot-01",
            "category": "followup",
            "started_at_utc": "2026-10-11T13:10:00Z",
            "ended_at_utc": "2026-10-11T13:20:00Z",
        })
        with self.assertRaisesRegex(CostAuditError, "unknown work category"):
            audit_costs(frame, allocations, outcomes, ledger)

    def test_cli_duplicate_json_fields_and_nan_rejected(self):
        frame, assignment, outcomes, ledger = inputs()
        with tempfile.TemporaryDirectory() as temp:
            tmp = Path(temp)
            allocations_path = tmp / "allocations.json"
            allocations_path.write_text(json.dumps(assignment), encoding="utf-8")
            ledger_path = tmp / "ledger.json"
            output = tmp / "report.json"
            command = [
                sys.executable, "-m", "trending_study.task_costs",
                "--frame", str(FIXTURES / "trial_frame.synthetic.json"),
                "--assignments", str(allocations_path),
                "--outcomes", str(FIXTURES / "trial_outcomes.synthetic.json"),
                "--input", str(ledger_path), "--output", str(output),
            ]
            source_text = json.dumps(ledger)
            duplicate = source_text.replace(
                '"schema_version": "1.0"',
                '"schema_version": "1.0", "schema_version": "1.0"',
                1,
            )
            ledger_path.write_text(duplicate, encoding="utf-8")
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("duplicate JSON key", run.stderr)
            self.assertFalse(output.exists())
            ledger_path.write_text(source_text.replace(
                '"max_human_minutes": 35', '"max_human_minutes": NaN', 1,
            ), encoding="utf-8")
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("nonfinite/nonstandard", run.stderr)
            self.assertFalse(output.exists())

    def test_write_once_cli_and_alias_protection(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "cost-report.json"
            allocations = Path(temp) / "allocations.json"
            frame, assignment, outcomes, ledger = inputs()
            allocations.write_text(json.dumps(assignment), encoding="utf-8")
            command = [
                sys.executable, "-m", "trending_study.task_costs",
                "--frame", str(FIXTURES / "trial_frame.synthetic.json"),
                "--assignments", str(allocations),
                "--outcomes", str(FIXTURES / "trial_outcomes.synthetic.json"),
                "--input", str(FIXTURES / "task_costs.synthetic.json"),
                "--output", str(output),
            ]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads(output.read_text())["overall"]["assigned"], 8)
            before = output.read_bytes()
            retry = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(retry.returncode, 0)
            self.assertEqual(output.read_bytes(), before)
            alias = command.copy()
            alias[-1] = str(FIXTURES / "task_costs.synthetic.json")
            collision = subprocess.run(alias, capture_output=True, text=True)
            self.assertNotEqual(collision.returncode, 0)
            self.assertEqual(read("task_costs.synthetic.json"), ledger)


if __name__ == "__main__":
    unittest.main()
