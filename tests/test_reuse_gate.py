import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
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

    def test_cli_stays_equivalent_on_committed_synthetic_assessment(self):
        fixture = Path(__file__).resolve().parents[1] / (
            "examples/reuse_check.example.json")
        proc = subprocess.run(
            [sys.executable, "-m", "trending_study.reuse_gate",
             "--input", str(fixture)],
            capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result, evaluate(json.loads(fixture.read_text(encoding="utf-8"))))
        self.assertEqual(result["next_action"], "verify_existing_candidates")
        self.assertNotIn("automatic_install_approved", result)

    def test_cli_rejects_duplicate_gate_and_nonstandard_numeric_inputs(self):
        original = (Path(__file__).resolve().parents[1] /
                    "examples/reuse_check.example.json").read_text(encoding="utf-8")
        duplicate = original.replace(
            '"functional_test": "unknown"',
            '"functional_test": "failed", "functional_test": "verified"', 1)
        self.assertIn('"functional_test": "verified"', duplicate)
        for raw in (duplicate, '{"x":NaN}', '{"x":Infinity}',
                    '{"x":1e999}', '{"x":1e-999}'):
            with self.subTest(raw=raw[:70]), tempfile.TemporaryDirectory() as folder:
                source = Path(folder) / "PRIVATE_SOURCE_FRAME.json"
                source.write_text(raw, encoding="utf-8")
                proc = subprocess.run(
                    [sys.executable, "-m", "trending_study.reuse_gate",
                     "--input", str(source)],
                    capture_output=True, text=True,
                )
                self.assertEqual(proc.returncode, 2)
                self.assertIn("invalid or unsafe reuse assessment JSON input", proc.stderr)
                self.assertNotIn("PRIVATE_SOURCE_FRAME", proc.stderr)
                self.assertNotIn("functional_test", proc.stderr)
                self.assertNotIn("Traceback", proc.stderr)
                self.assertFalse(proc.stdout.strip())

    def test_cli_refuses_nonregular_and_oversized_inputs_without_path_leak(self):
        fixture = Path(__file__).resolve().parents[1] / (
            "examples/reuse_check.example.json")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            link = root / "PRIVATE_SYMLINK.json"
            link.symlink_to(fixture)
            big = root / "PRIVATE_TOO_BIG.json"
            big.write_bytes(b" " * (16 * 1024 * 1024 + 1))
            for source in (link, root, big):
                with self.subTest(source=source.name):
                    proc = subprocess.run(
                        [sys.executable, "-m", "trending_study.reuse_gate",
                         "--input", str(source)],
                        capture_output=True, text=True,
                    )
                    self.assertEqual(proc.returncode, 2)
                    self.assertIn("invalid or unsafe reuse assessment JSON input", proc.stderr)
                    self.assertNotIn("PRIVATE_", proc.stderr)
                    self.assertNotIn("Traceback", proc.stderr)
                    self.assertFalse(proc.stdout.strip())

    def test_invalid_status_refused(self):
        card = copy.deepcopy(CARD)
        card["candidates"][0]["functional_test"] = "probably"
        with self.assertRaises(InvalidReuseAssessment):
            evaluate(card)


if __name__ == "__main__":
    unittest.main()
