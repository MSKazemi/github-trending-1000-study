"""Regression coverage for conservative, offline research-artifact integrity checks."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.check_research_artifacts import IntegrityError, audit_repository, validate_text


class ResearchArtifactQualityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ("examples", "references", "research-notes"):
            (self.root / name).mkdir()
        (self.root / "examples" / "case.json").write_text(
            '{"outer":{"one":1},"items":[1,2]}', encoding="utf-8"
        )
        (self.root / "examples" / "events.jsonl").write_text(
            '{"record":"a"}\n{"record":"b"}\n', encoding="utf-8"
        )
        (self.root / "references" / "registry.csv").write_text(
            'name,notes\n"a,b","line 1\nline 2"\n', encoding="utf-8"
        )

    def test_valid_artifact_tree_and_quoted_multiline_csv(self):
        result = audit_repository(self.root)
        self.assertEqual(result["files"], 3)
        self.assertEqual(result["json"], 1)
        self.assertEqual(result["jsonl"], 1)
        self.assertEqual(result["csv"], 1)
        self.assertEqual(result["logical_records"], 4)

    def test_duplicate_nested_json_fields_rejected(self):
        file = self.root / "examples" / "case.json"
        file.write_text('{"record":{"version":1,"version":2}}', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "duplicate JSON object key"):
            audit_repository(self.root)

    def test_nonstandard_nan_and_infinity_rejected(self):
        file = self.root / "examples" / "case.json"
        for bad in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(value=bad):
                file.write_text('{"energy":' + bad + '}', encoding="utf-8")
                with self.assertRaisesRegex(IntegrityError, "nonstandard JSON"):
                    audit_repository(self.root)

    def test_truncated_json_and_nonobject_root_rejected(self):
        file = self.root / "examples" / "case.json"
        file.write_text('{"a":', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "case.json"):
            audit_repository(self.root)
        file.write_text("42", encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "top level"):
            audit_repository(self.root)

    def test_jsonl_bad_blank_and_duplicate_rows_rejected(self):
        file = self.root / "examples" / "events.jsonl"
        for bad in ('{"k":1}\n\n{"k":2}\n', '{"k":1,"k":2}\n', '42\n'):
            with self.subTest(raw=bad):
                file.write_text(bad, encoding="utf-8")
                with self.assertRaises(IntegrityError):
                    audit_repository(self.root)

    def test_csv_duplicate_headers_and_ragged_rows_rejected(self):
        file = self.root / "references" / "registry.csv"
        for bad in ("id,ID\n1,2\n", "id,value\n1,2,3\n", ",value\n1,2\n", ""):
            with self.subTest(raw=bad):
                file.write_text(bad, encoding="utf-8")
                with self.assertRaises(IntegrityError):
                    audit_repository(self.root)

    def test_reject_symlink_and_invalid_utf8(self):
        source = self.root / "examples" / "case.json"
        alias = self.root / "research-notes" / "external.json"
        try:
            alias.symlink_to(source)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks not supported by this test filesystem")
        with self.assertRaisesRegex(IntegrityError, "symlink forbidden"):
            audit_repository(self.root)
        alias.unlink()
        source.write_bytes(b"\xff\xfe\x00")
        with self.assertRaisesRegex(IntegrityError, "case.json"):
            audit_repository(self.root)

    def test_missing_directories_and_limits_fail_closed(self):
        with self.assertRaisesRegex(IntegrityError, "file exceeds"):
            audit_repository(self.root, max_file_bytes=1)
        (self.root / "references").rename(self.root / "renamed")
        with self.assertRaisesRegex(IntegrityError, "missing data directory"):
            audit_repository(self.root)

    def test_cli_bounded_clean_and_failure_codes(self):
        path = Path(__file__).resolve().parents[1] / "scripts" / "check_research_artifacts.py"
        cmd = [sys.executable, str(path), "--root", str(self.root)]
        good = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertEqual(
            json.loads(good.stdout)["status"], "syntax_checked_not_scientifically_validated"
        )
        (self.root / "examples" / "case.json").write_text(
            '{"unsafe":NaN}', encoding="utf-8"
        )
        bad = subprocess.run(cmd, capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn("artifact integrity gate failed", bad.stderr)

    def test_reject_unrecognized_file_suffix_in_direct_validator(self):
        with self.assertRaisesRegex(IntegrityError, "unsupported file suffix"):
            validate_text(Path("fixture.txt"), "not json")


if __name__ == "__main__":
    unittest.main()
