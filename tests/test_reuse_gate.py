import copy
import unittest
from trending_study.reuse_gate import InvalidReuseAssessment, evaluate


CARD = {
    "schema_version": "1.0",
    "task": "Generate domain-aware config diff",
    "acceptance_test": "Compare known fixtures and verify expected output",
    "search_log": ["2026-10-11: searched npm, PyPI, GitHub for config diff"],
    "candidates": [{
        "name": "SYNTHETIC candidate (not a real package)",
        "source_url": "https://example.org/not-a-real-project",
        "functional_test": "unknown",
        "license_compatibility": "unknown",
        "security_review": "unknown",
        "maintenance_review": "unknown",
    }],
}


class ReuseGateTests(unittest.TestCase):
    def test_unknown_candidate_requires_evidence(self):
        result = evaluate(CARD)
        self.assertEqual(result["next_action"], "verify_existing_candidates")
        self.assertEqual(result["self_reported_qualified"], [])

    def test_no_logged_search_requires_search(self):
        card = copy.deepcopy(CARD)
        card["search_log"] = []
        self.assertEqual(evaluate(card)["next_action"], "search_before_generation")

    def test_missing_acceptance_stops(self):
        card = copy.deepcopy(CARD)
        card["acceptance_test"] = ""
        self.assertEqual(evaluate(card)["next_action"], "define_independent_task_test")

    def test_verified_candidate_suggests_trial_not_auto_install(self):
        card = copy.deepcopy(CARD)
        for k in ("functional_test", "license_compatibility", "security_review", "maintenance_review"):
            card["candidates"][0][k] = "verified"
        result = evaluate(card)
        self.assertEqual(result["next_action"], "trial_verified_reuse")
        self.assertIn("self-reported", result["reason"])

    def test_failed_license_excludes_candidate(self):
        card = copy.deepcopy(CARD)
        card["candidates"][0]["license_compatibility"] = "failed"
        result = evaluate(card)
        self.assertEqual(result["next_action"], "consider_minimal_new_implementation")
        self.assertEqual(result["failed_gates"]["SYNTHETIC candidate (not a real package)"], ["license_compatibility"])

    def test_invalid_status_refused(self):
        card = copy.deepcopy(CARD)
        card["candidates"][0]["functional_test"] = "probably"
        with self.assertRaises(InvalidReuseAssessment):
            evaluate(card)


if __name__ == "__main__":
    unittest.main()
