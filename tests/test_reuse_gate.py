import copy
from contextlib import redirect_stderr
import io
import traceback
from unittest.mock import patch
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from trending_study.reuse_gate import InvalidReuseAssessment, evaluate, main


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

    def test_cli_private_reader_errors_have_no_exception_context(self):
        # A sanitized error printed inside except can still leak private input
        # through SystemExit.__context__ in structured traceback telemetry.
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            missing = root / "PRIVATE_REUSE_INPUT_NOT_FOUND.json"
            malformed = root / "PRIVATE_DUPLICATE_GATE.json"
            malformed.write_text('{"PRIVATE_GATE":1,"PRIVATE_GATE":2}', encoding="utf-8")
            for source in (missing, malformed):
                with self.subTest(source=source.name):
                    stderr = io.StringIO()
                    with redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
                        main(["--input", str(source)])
                    error = caught.exception
                    self.assertEqual(error.code, 2)
                    self.assertIsNone(error.__cause__)
                    self.assertIsNone(error.__context__)
                    self.assertNotIn("PRIVATE_", stderr.getvalue() +
                                     "".join(traceback.format_exception(error)))

    def test_cli_evaluator_error_does_not_chain_private_input(self):
        with tempfile.TemporaryDirectory() as folder:
            src = Path(folder) / "PRIVATE_ASSESSMENT.json"
            src.write_text(json.dumps(CARD), encoding="utf-8")
            with patch("trending_study.reuse_gate.evaluate",
                       side_effect=ValueError("PRIVATE_NESTED_DETAIL")):
                stderr = io.StringIO()
                with redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
                    main(["--input", str(src)])
            error = caught.exception
            self.assertEqual(error.code, 2)
            self.assertIsNone(error.__cause__)
            self.assertIsNone(error.__context__)
            self.assertIn("invalid reuse assessment fields", stderr.getvalue())
            self.assertNotIn("PRIVATE_", stderr.getvalue() +
                             "".join(traceback.format_exception(error)))

    def test_duplicate_names_do_not_overwrite_failed_gate_evidence(self):
        for duplicate_name in ("SYNTHETIC candidate (not a real package)",
                               "synthetic CANDIDATE (not a real package)",
                               " SYNTHETIC candidate (not a real package) "):
            card = copy.deepcopy(CARD)
            card["candidates"][0]["license_compatibility"] = "failed"
            another = copy.deepcopy(card["candidates"][0])
            another["name"] = duplicate_name
            for gate in ("functional_test", "license_compatibility",
                         "security_review", "maintenance_review"):
                another[gate] = "verified"
            card["candidates"].append(another)
            with self.subTest(name=duplicate_name):
                with self.assertRaisesRegex(
                        InvalidReuseAssessment, "duplicate normalized candidate"):
                    evaluate(card)

    def test_invalid_nested_state_types_are_controlled_validation_failures(self):
        for state in ([], {}, ["verified"], {"private": "PRIVATE_GATE"}):
            card = copy.deepcopy(CARD)
            card["candidates"][0]["security_review"] = state
            with self.subTest(state=type(state).__name__):
                with self.assertRaisesRegex(
                        InvalidReuseAssessment, "security_review"):
                    evaluate(card)

    def test_candidate_fields_and_count_are_bounded_without_losing_distinct_rows(self):
        card = copy.deepcopy(CARD)
        duplicate = copy.deepcopy(card["candidates"][0])
        duplicate["private_password"] = "PRIVATE_PASSWORD_MARKER"
        card["candidates"].append(duplicate)
        with self.assertRaisesRegex(InvalidReuseAssessment, "unsupported fields"):
            evaluate(card)
        card = copy.deepcopy(CARD)
        card["candidates"][0]["name"] = "Long" * 200
        with self.assertRaisesRegex(InvalidReuseAssessment, "bounded text"):
            evaluate(card)
        card = copy.deepcopy(CARD)
        card["candidates"] = [
            dict(card["candidates"][0], name=f"SYNTHETIC-{i}")
            for i in range(101)
        ]
        with self.assertRaisesRegex(InvalidReuseAssessment, "bounded list"):
            evaluate(card)
        card = copy.deepcopy(CARD)
        negative = copy.deepcopy(card["candidates"][0])
        negative["name"] = "SYNTHETIC different candidate"
        negative["license_compatibility"] = "failed"
        card["candidates"].append(negative)
        result = evaluate(card)
        self.assertEqual(result["candidate_count"], 2)
        self.assertEqual(result["unresolved"], [CARD["candidates"][0]["name"]])
        self.assertEqual(result["failed_gates"], {
            "SYNTHETIC different candidate": ["license_compatibility"]})

    def test_cli_returns_bounded_error_for_unhashable_gate_status(self):
        with tempfile.TemporaryDirectory() as folder:
            card = copy.deepcopy(CARD)
            card["candidates"][0]["functional_test"] = ["verified"]
            source = Path(folder) / "PRIVATE_CARD.json"
            source.write_text(json.dumps(card), encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, "-m", "trending_study.reuse_gate",
                 "--input", str(source)],
                capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 2)
            self.assertIn("functional_test", proc.stderr)
            self.assertNotIn("PRIVATE_CARD", proc.stderr)
            self.assertNotIn("Traceback", proc.stderr)

    def test_invalid_status_refused(self):
        card = copy.deepcopy(CARD)
        card["candidates"][0]["functional_test"] = "probably"
        with self.assertRaises(InvalidReuseAssessment):
            evaluate(card)


if __name__ == "__main__":
    unittest.main()
