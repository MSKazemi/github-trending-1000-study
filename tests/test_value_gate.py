import copy
import unittest
from trending_study.value_gate import InvalidCard, evaluate


CARD = {
    "schema_version": "1.0",
    "project_name": "Synthetic CLI demo",
    "project_type": "cli",
    "target_user": "analysts who format two files a week",
    "problem_statement": "time-consuming manual diff inspection",
    "existing_alternative": "existing command-line diff tools",
    "differentiator": "preserve domain-specific annotations in output",
    "acceptance_task": "run CLI on fixture and verify annotated diff",
    "risk_level": "low",
    "security_review": "not_done",
    "independent_evidence": {"kind": "none", "count": 0},
    "task_evaluation": {"attempted": 0, "succeeded": 0, "acceptance_criteria_frozen": True},
    "effort": {},
    "budgets": {"max_human_minutes": 120},
}


class ValueGateTests(unittest.TestCase):
    def test_no_tests_no_confident_value_claim(self):
        result = evaluate(CARD)
        self.assertEqual(result["decision"], "run_independent_task_test")
        self.assertIsNone(result["human_active_minutes"])
        self.assertIsNone(result["observed_input_plus_output_tokens"])
        self.assertEqual(result["evidence_level"], "concept")

    def test_failed_task_blocks_scaling(self):
        card = copy.deepcopy(CARD)
        card["task_evaluation"]["attempted"] = 3
        card["task_evaluation"]["succeeded"] = 2
        card["independent_evidence"] = {"kind": "independent-task", "count": 3}
        self.assertEqual(evaluate(card)["decision"], "repair_and_retest")

    def test_security_issues_block_even_low_risk(self):
        card = copy.deepcopy(CARD)
        card["security_review"] = "issues_found"
        self.assertEqual(evaluate(card)["decision"], "security_review_before_release")

    def test_budget_and_synthetic_success(self):
        card = copy.deepcopy(CARD)
        card["task_evaluation"] = {"attempted": 2, "succeeded": 2, "acceptance_criteria_frozen": True}
        card["independent_evidence"] = {"kind": "independent-task", "count": 2}
        card["effort"] = {"planning_minutes": 60, "prompt_minutes": 30, "review_minutes": 45, "repair_minutes": 25, "ship_minutes": 15, "followup_minutes": 10, "input_tokens": 3000, "output_tokens": 2000}
        result = evaluate(card)
        self.assertEqual(result["decision"], "test_repeat_value")
        self.assertEqual(result["human_active_minutes"], 185)
        self.assertEqual(result["observed_input_plus_output_tokens"], 5000)
        self.assertTrue(result["budget_alerts"])

    def test_invalid_count_and_partial_acceptance(self):
        card = copy.deepcopy(CARD)
        card["task_evaluation"]["succeeded"] = 1
        with self.assertRaises(InvalidCard):
            evaluate(card)
        card = copy.deepcopy(CARD)
        card["independent_evidence"]["count"] = True
        with self.assertRaises(InvalidCard):
            evaluate(card)


if __name__ == "__main__":
    unittest.main()
