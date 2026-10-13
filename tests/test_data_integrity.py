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

    def test_csv_quoted_multiline_and_header_only_are_syntax_valid(self):
        with tempfile.TemporaryDirectory() as root:
            csv_file = self._artifact(
                root, "evidence.csv",
                b'name,notes\r\n"a,b","first line\nsecond line"\r\n'
                b'other,"with \"\"quoted\"\" words"\r\n',
            )
            result = validate_repository(root)
            self.assertEqual(result["validated_files"], 1)
            self.assertEqual(result["json_documents_or_jsonl_records"], 0)
            self.assertEqual(result["csv_data_records"], 2)
            self.assertEqual(result["total_logical_records"], 2)
            self.assertIn(b"first line", csv_file.read_bytes())
            csv_file.write_bytes(b"name,notes\n")
            empty = validate_repository(root)
            self.assertEqual(empty["csv_data_records"], 0)
            self.assertFalse(empty["authenticated_research_evidence"])

    def test_csv_duplicate_casefold_headers_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            for content in (b"id,ID\n1,2\n", b"id, id \n1,2\n"):
                with self.subTest(content=content):
                    self._artifact(root, "evidence.csv", content)
                    with self.assertRaisesRegex(ResearchJSONError, "repeated CSV header"):
                        validate_repository(root)

    def test_csv_ragged_row_blank_header_and_unsafe_nul_fail(self):
        for content, reason in (
            (b"id,val\n1,2,3\n", "CSV record"),
            (b"id,val\n1\n", "CSV record"),
            (b",val\n1,2\n", "blank CSV header"),
            (b"", "blank CSV header"),
            (b"id,val\n1,\x00\n", "embedded NUL"),
        ):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "data.csv", content)
                with self.assertRaisesRegex(ResearchJSONError, reason):
                    validate_repository(root)

    def test_csv_malformed_quoting_invalid_utf8_and_symlink_fail(self):
        for content, reason in (
            (b'id,val\n1,"unfinished\n', "malformed CSV"),
            (b'id,val\n1,\xff\n', "invalid UTF-8"),
        ):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "data.csv", content)
                with self.assertRaisesRegex(ResearchJSONError, reason):
                    validate_repository(root)
        with tempfile.TemporaryDirectory() as root:
            csv_file = self._artifact(root, "good.csv", b"id,val\n1,2\n")
            link = csv_file.parent / "alias.csv"
            link.symlink_to(csv_file)
            with self.assertRaisesRegex(ResearchJSONError, "symlinks"):
                validate_repository(root)

    def test_cli_csv_failure_uses_nonzero_exit_without_modifying_source(self):
        with tempfile.TemporaryDirectory() as root:
            source = self._artifact(root, "source.csv", b"id,ID\n1,2\n")
            before = source.read_bytes()
            cp = subprocess.run(
                [sys.executable, "-m", "trending_study.data_integrity", "--root", root],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(cp.returncode, 2)
            self.assertIn("repeated CSV header", cp.stderr)
            self.assertEqual(source.read_bytes(), before)

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


if __name__ == "__main__":
    unittest.main()
