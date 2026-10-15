"""CLI input gate regression tests for fictional energy scenarios (#307)."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.energy_boundary import COMPONENTS


def example():
    def arm(value):
        return {name: {"evidence": "modeled", "source_ref": "synthetic example",
                       "kwh": value} for name in COMPONENTS}
    return {
        "functional_unit": {
            "task_id": "fictional-task", "horizon_days": 90,
            "boundary_description": "fictional fixed output",
            "reuse_task_accepted": True, "build_task_accepted": True,
        },
        "arms": {"reuse": arm(1), "build": arm(2)},
        "grid_intensity_gco2e_per_kwh": 100,
    }


class EnergyCLIInputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.file = Path(self.temp.name) / "energy.json"

    def cli(self, path):
        return subprocess.run(
            [sys.executable, "-m", "trending_study.energy_boundary", "--input", str(path)],
            capture_output=True, text=True, timeout=15,
        )

    def test_existing_scenario_stays_partial_and_synthetic(self):
        self.file.write_text(json.dumps(example()), encoding="utf-8")
        p = self.cli(self.file)
        self.assertEqual(p.returncode, 0, p.stderr)
        result = json.loads(p.stdout)
        self.assertEqual(result["net_kwh_reuse_minus_build"], -7)
        self.assertIsNone(result["net_gco2e_reuse_minus_build"])
        self.assertEqual(result["modeling_or_measurement_status"], "mixed_modeled_scenario_only")

    def test_duplicate_energy_key_is_rejected_and_private_key_redacted(self):
        self.file.write_text('{"PRIVATE_SECRET":1,"PRIVATE_SECRET":2}', encoding="utf-8")
        p = self.cli(self.file)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("invalid or ambiguous JSON input", p.stderr)
        self.assertNotIn("PRIVATE_SECRET", p.stderr)
        self.assertNotIn(self.file.name, p.stderr)

    def test_nonstandard_or_out_of_range_numbers_fail(self):
        for literal in ("NaN", "Infinity", "-Infinity", "1e99999", "1e-99999"):
            with self.subTest(literal=literal):
                self.file.write_text('{"grid_intensity_gco2e_per_kwh":'+literal+'}', encoding="utf-8")
                self.assertNotEqual(self.cli(self.file).returncode, 0)

    def test_non_utf8_json_fails(self):
        self.file.write_bytes(b'{"key":"\xff"}')
        self.assertIn("invalid or ambiguous JSON input", self.cli(self.file).stderr)

    def test_symlink_rejected(self):
        alias = self.file.parent / "symlink.json"
        self.file.write_text(json.dumps(example()), encoding="utf-8")
        try:
            alias.symlink_to(self.file)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unsupported")
        self.assertIn("regular non-symlink", self.cli(alias).stderr)

    def test_fifo_rejected_without_read_hang(self):
        if not hasattr(os, "mkfifo"):
            self.skipTest("FIFO unavailable")
        fifo = self.file.parent / "stream.json"
        try:
            os.mkfifo(fifo)
        except OSError:
            self.skipTest("FIFO unavailable")
        self.assertIn("regular non-symlink", self.cli(fifo).stderr)

    def test_oversized_actual_content_fails_before_parsing(self):
        self.file.write_bytes(b'{"padding":"' + b"x" * 1_000_001 + b'"}')
        self.assertIn("byte limit", self.cli(self.file).stderr)

    def test_unknown_energy_still_null_not_zero(self):
        payload = example()
        payload["arms"]["reuse"]["model_inference"] = {"evidence": "unavailable", "kwh": None}
        self.file.write_text(json.dumps(payload), encoding="utf-8")
        p = self.cli(self.file)
        self.assertEqual(p.returncode, 0, p.stderr)
        result = json.loads(p.stdout)
        self.assertIsNone(result["net_kwh_reuse_minus_build"])
        self.assertFalse(result["comparable"])


if __name__ == "__main__":
    unittest.main()
