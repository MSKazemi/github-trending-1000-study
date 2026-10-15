"""Synthetic offline file-input regressions for adoption bounds (#306)."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.data_integrity import ResearchJSONError, load_research_json_file


class AdoptionCLIInputGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_cli(self, path):
        return subprocess.run(
            [sys.executable, "-m", "trending_study.adoption_bounds", "--input", str(path)],
            capture_output=True, text=True, timeout=15,
        )

    def test_existing_synthetic_example_remains_valid(self):
        example = Path(__file__).resolve().parents[1] / "examples" / "adoption_signals.synthetic.json"
        process = self.run_cli(example)
        self.assertEqual(process.returncode, 0, process.stderr)
        report = json.loads(process.stdout)
        self.assertEqual(report["dataset_kind"], "synthetic")
        self.assertFalse(report["independent_review_authenticated"])

    def test_duplicate_private_key_hidden_in_cli_errors(self):
        path = self.root / "private-source-path.json"
        path.write_text('{"PRIVATE_CREDENTIAL_123": 1, "PRIVATE_CREDENTIAL_123": 2}', encoding="utf-8")
        process = self.run_cli(path)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("invalid or ambiguous JSON input", process.stderr)
        self.assertNotIn("PRIVATE_CREDENTIAL_123", process.stderr)
        self.assertNotIn(path.name, process.stderr)

    def test_nonfinite_and_extreme_json_are_rejected(self):
        path = self.root / "bad.json"
        for raw in (b'{"cards": NaN}', b'{"cards": Infinity}',
                    b'{"cards": 1e9999}', b'{"cards": 1e-9999}'):
            with self.subTest(raw=raw):
                path.write_bytes(raw)
                self.assertNotEqual(self.run_cli(path).returncode, 0)

    def test_invalid_utf8_is_rejected(self):
        path = self.root / "invalid.json"
        path.write_bytes(b'{"cards":"\xff"}')
        self.assertIn("invalid or ambiguous JSON input", self.run_cli(path).stderr)

    def test_symlinked_leaf_is_rejected(self):
        original = self.root / "real.json"
        original.write_text("{}", encoding="utf-8")
        alias = self.root / "alias.json"
        try:
            alias.symlink_to(original)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        self.assertIn("regular non-symlink", self.run_cli(alias).stderr)

    def test_fifo_is_rejected_without_hanging(self):
        if not hasattr(os, "mkfifo"):
            self.skipTest("FIFOs unavailable")
        fifo = self.root / "fifo.json"
        try:
            os.mkfifo(fifo)
        except OSError:
            self.skipTest("FIFOs unavailable")
        self.assertIn("regular non-symlink", self.run_cli(fifo).stderr)

    def test_actual_read_limit_is_enforced(self):
        path = self.root / "oversized.json"
        path.write_bytes(b'{"padding":"' + b"x" * 100 + b'"}')
        with self.assertRaisesRegex(ResearchJSONError, "byte limit"):
            load_research_json_file(path, max_bytes=32)

    def test_directory_is_not_an_input(self):
        self.assertIn("regular non-symlink", self.run_cli(self.root).stderr)

    def test_valid_nested_json_uses_existing_decoder(self):
        path = self.root / "nested.json"
        path.write_text('{"nested":[{"ok":true}]}', encoding="utf-8")
        self.assertEqual(load_research_json_file(path), {"nested":[{"ok":True}]})


if __name__ == "__main__":
    unittest.main()
