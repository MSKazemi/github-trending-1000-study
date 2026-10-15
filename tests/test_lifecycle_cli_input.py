"""Fail-closed lifecycle scenario CLI JSON input regressions (#308)."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_lifecycle_break_even import scenario


class LifecycleScenarioInputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.file = Path(self.temp.name) / "scenario.json"

    def cli(self, path):
        return subprocess.run(
            [sys.executable, "-m", "trending_study.lifecycle_break_even", "--input", str(path)],
            capture_output=True, text=True, timeout=15,
        )

    def test_prior_synthetic_scenario_keeps_exact_crossover(self):
        self.file.write_text(json.dumps(scenario()), encoding="utf-8")
        p = self.cli(self.file)
        self.assertEqual(p.returncode, 0, p.stderr)
        r = json.loads(p.stdout)
        self.assertEqual(r["crossing"]["last_integer_n_reuse_lower"], 266)
        self.assertEqual(r["crossing"]["first_integer_n_build_lower"], 267)
        self.assertEqual(r["calculation_status"], "scenario_only_no_uncertainty_interval")

    def test_private_duplicate_key_does_not_leak(self):
        self.file.write_text('{"VERY_PRIVATE_LABEL":1,"VERY_PRIVATE_LABEL":2}', encoding="utf-8")
        p = self.cli(self.file)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("invalid or ambiguous JSON input", p.stderr)
        self.assertNotIn("VERY_PRIVATE_LABEL", p.stderr)
        self.assertNotIn(self.file.name, p.stderr)

    def test_nonfinite_overflow_and_bad_encoding_are_rejected(self):
        for raw in (b'{"n": NaN}', b'{"n": Infinity}', b'{"n":1e9999}',
                    b'{"n":1e-9999}', b'{"n":"\xff"}'):
            with self.subTest(raw=raw):
                self.file.write_bytes(raw)
                self.assertIn("invalid or ambiguous JSON input", self.cli(self.file).stderr)

    def test_leaf_symlink_rejected(self):
        self.file.write_text(json.dumps(scenario()), encoding="utf-8")
        alias = self.file.parent / "alias.json"
        try:
            alias.symlink_to(self.file)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        self.assertIn("regular non-symlink", self.cli(alias).stderr)

    def test_fifo_rejected_without_block(self):
        if not hasattr(os, "mkfifo"):
            self.skipTest("FIFO unavailable")
        fifo = self.file.parent / "pipe.json"
        try:
            os.mkfifo(fifo)
        except OSError:
            self.skipTest("FIFO unavailable")
        self.assertIn("regular non-symlink", self.cli(fifo).stderr)

    def test_oversize_file_rejected_even_if_valid_json(self):
        self.file.write_bytes(b'{"padding":"' + b"x" * 1_000_001 + b'"}')
        self.assertIn("byte limit", self.cli(self.file).stderr)

    def test_directory_is_not_a_regular_json_input(self):
        self.assertIn("regular non-symlink", self.cli(self.file.parent).stderr)

    def test_missing_energy_remains_null_not_saving(self):
        d = scenario()
        d["strategies"]["reuse"]["pre_run"]["maintenance"] = {
            "kwh": None, "basis": "unknown", "evidence_ref": None,
        }
        self.file.write_text(json.dumps(d), encoding="utf-8")
        p = self.cli(self.file)
        self.assertEqual(p.returncode, 0, p.stderr)
        report = json.loads(p.stdout)
        self.assertIsNone(report["points"][0]["delta_build_minus_reuse_kwh"])
        self.assertEqual(report["calculation_status"], "incomplete_no_point_estimate")


if __name__ == "__main__":
    unittest.main()
