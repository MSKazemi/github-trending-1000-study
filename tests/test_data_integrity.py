"""Offline regressions for immutable research JSON inspection; all data synthetic."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from trending_study import data_integrity
from trending_study.data_integrity import ResearchJSONError, validate_repository


class ResearchDataIntegrityTests(unittest.TestCase):
    def _artifact(self, root, name, raw):
        path = Path(root) / "examples" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def test_accepts_valid_json_and_jsonl_without_rewriting(self):
        with tempfile.TemporaryDirectory() as root:
            first = self._artifact(root, "valid.json", b'{"root":{"id":1,"ok":true}}\n')
            second = self._artifact(root, "valid.jsonl", b'\n{"id":1}\n\n{"id":2}\n')
            before = (first.read_bytes(), second.read_bytes())
            result = validate_repository(root)
            self.assertEqual(result["validated_files"], 2)
            self.assertEqual(result["json_documents_or_jsonl_records"], 3)
            self.assertFalse(result["authenticated_research_evidence"])
            self.assertEqual(before, (first.read_bytes(), second.read_bytes()))

    def test_rejects_duplicate_keys_at_any_depth(self):
        invalid = (
            b'{"id":1,"id":2}',
            b'{"evidence":{"doi":"first","doi":"second"}}',
            b'[{"source":"a","source":"b"}]',
        )
        for raw in invalid:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "evidence.json", raw)
                with self.assertRaisesRegex(ResearchJSONError, "duplicate JSON object key"):
                    validate_repository(root)

    def test_rejects_non_finite_numeric_values(self):
        for raw in (b'{"x":NaN}', b'{"x":Infinity}', b'{"x":-Infinity}',
                    b'{"x":1e999}'):
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "evidence.json", raw)
                with self.assertRaisesRegex(ResearchJSONError, "non-finite|nonstandard"):
                    validate_repository(root)

    def test_jsonl_reports_exact_invalid_line(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "events.jsonl",
                           b'{"id":1}\n\n{"id":2,"id":3}\n')
            with self.assertRaisesRegex(ResearchJSONError,
                                         r"events\.jsonl:line 3.*duplicate"):
                validate_repository(root)

    def test_fails_closed_on_malformed_utf8_and_empty_jsonl(self):
        for name, raw, reason in (
            ("broken.json", b'{"name":"\xff"}', "invalid UTF-8"),
            ("empty.jsonl", b"\n \n", "empty JSONL"),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as root:
                self._artifact(root, name, raw)
                with self.assertRaisesRegex(ResearchJSONError, reason):
                    validate_repository(root)

    def test_oversized_file_is_not_silently_ignored(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "large.json", b'{"abc":12345}')
            with patch.object(data_integrity, "MAX_FILE_BYTES", 5):
                with self.assertRaisesRegex(ResearchJSONError, "inspection limit"):
                    validate_repository(root)

    def test_symlinked_record_and_directory_are_not_trusted(self):
        with tempfile.TemporaryDirectory() as root:
            outer = Path(root) / "outside.json"
            outer.write_text('{"id":1}', encoding="utf-8")
            self._artifact(root, "real.json", b'{"id":1}')
            (Path(root) / "examples" / "link.json").symlink_to(outer)
            with self.assertRaisesRegex(ResearchJSONError, "symlinks"):
                validate_repository(root)
        with tempfile.TemporaryDirectory() as root:
            outer_dir = Path(root) / "real_dir"
            outer_dir.mkdir()
            (outer_dir / "a.json").write_text('{"id":1}', encoding="utf-8")
            (Path(root) / "examples").symlink_to(outer_dir, target_is_directory=True)
            with self.assertRaisesRegex(ResearchJSONError, "symlink"):
                validate_repository(root)

    def test_absent_or_invalid_source_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaisesRegex(ResearchJSONError, "no .json"):
                validate_repository(root)
            self._artifact(root, "bad.json", b'{ "a": ')
            with self.assertRaises(ResearchJSONError):
                validate_repository(root)

    def test_cli_error_path_has_nonzero_exit_and_no_traceback(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "bad.json", b'{"id":1,"id":2}')
            cp = subprocess.run(
                [sys.executable, "-m", "trending_study.data_integrity",
                 "--root", root],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(cp.returncode, 2)
            self.assertIn("duplicate JSON object key", cp.stderr)
            self.assertNotIn("Traceback", cp.stderr)
            self.assertEqual(cp.stdout, "")


    def test_csv_header_only_is_not_accepted_as_real_observations(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "empty_sources.csv", b"id,title,source\n")
            with self.assertRaisesRegex(ResearchJSONError, "no data records"):
                validate_repository(root)

    def test_total_budget_and_file_limit_include_csv_and_json(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "first.json", b'{"id":1}')
            self._artifact(root, "second.csv", b'id,n\n1,2\n')
            with patch.object(data_integrity, "MAX_FILES", 1):
                with self.assertRaisesRegex(ResearchJSONError, "file count"):
                    validate_repository(root)
            with patch.object(data_integrity, "MAX_TOTAL_BYTES", 10):
                with self.assertRaisesRegex(ResearchJSONError, "cumulative"):
                    validate_repository(root)
            report = validate_repository(root)
            self.assertEqual(report["total_research_records"], 2)
            self.assertEqual(report["json_documents_or_jsonl_records"], 1)
            self.assertEqual(report["csv_data_rows"], 1)
            self.assertGreater(report["checked_bytes"], 10)

    def test_csv_multiline_and_commas_are_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            file = self._artifact(
                root, "vendor.csv",
                b'\xef\xbb\xbfcompany,notes\r\n"Acme, Inc.","line one\nline two"\r\n"OSS","reused"\r\n',
            )
            before = file.read_bytes()
            result = validate_repository(root)
            self.assertEqual(result["validated_files"], 1)
            self.assertEqual(result["validated_csv_files"], 1)
            self.assertEqual(result["csv_data_rows"], 2)
            self.assertEqual(result["json_documents_or_jsonl_records"], 0)
            self.assertEqual(file.read_bytes(), before)
            self.assertFalse(result["authenticated_research_evidence"])

    def test_csv_rejects_duplicate_and_blank_headers_and_ragged_rows(self):
        invalid = (
            (b"name, Name\nalpha,beta\n", "duplicate CSV header"),
            (b"name,\nalpha,beta\n", "blank names"),
            (b"name,count\nalpha,1,extra\n", "cells"),
            (b"name,count\nalpha\n", "cells"),
            (b"", "no header"),
            (b'name,notes\n"unterminated,field\n', "invalid CSV"),
        )
        for raw, message in invalid:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "invalid.csv", raw)
                with self.assertRaisesRegex(ResearchJSONError, message):
                    validate_repository(root)

    def test_csv_rejects_embedded_nul_and_malformed_utf8(self):
        for raw, message in (
            (b"name,note\nalpha,zero\x00byte\n", "embedded NUL"),
            (b"name,note\nalpha,\xff\n", "invalid UTF-8"),
        ):
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "unsafe.csv", raw)
                with self.assertRaisesRegex(ResearchJSONError, message):
                    validate_repository(root)

    def test_extreme_json_float_underflow_and_overflow_are_not_silent(self):
        for raw, message in (
            (b'{"energy":1e-10000}', "underflow"),
            (b'{"energy":-1e-10000}', "underflow"),
            (b'{"energy":1e10000}', "overflow"),
        ):
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "numbers.json", raw)
                with self.assertRaisesRegex(ResearchJSONError, message):
                    validate_repository(root)
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "valid.json", b'{"energy":0e-10000,"cost":1.5}')
            report = validate_repository(root)
            self.assertEqual(report["json_documents_or_jsonl_records"], 1)

    def test_giant_json_integer_is_rejected_on_all_supported_python_versions(self):
        with tempfile.TemporaryDirectory() as root:
            literal = ("9" * 1025).encode("ascii")
            self._artifact(root, "large_integer.json", b'{"n":' + literal + b'}')
            with self.assertRaisesRegex(ResearchJSONError, "1024 decimal digits"):
                validate_repository(root)

    def test_jsonl_numeric_data_loss_is_rejected_with_source_line(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "history.jsonl", b'{"id":1}\n{"energy":1e-9999}\n')
            with self.assertRaisesRegex(ResearchJSONError, "history.jsonl:line 2.*underflow"):
                validate_repository(root)


if __name__ == "__main__":
    unittest.main()
