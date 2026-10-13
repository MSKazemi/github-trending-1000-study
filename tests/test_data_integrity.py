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

    def test_csv_quoted_commas_and_exact_width_without_mutation(self):
        with tempfile.TemporaryDirectory() as root:
            csvfile = self._artifact(root, "rows.csv",
                                     b'id,title,source\n1,"quoted, value",test\n2,other,verified\n')
            data = csvfile.read_bytes()
            result = validate_repository(root)
            self.assertEqual(result["validated_files"], 1)
            self.assertEqual(result["csv_data_rows"], 2)
            self.assertEqual(result["json_documents_or_jsonl_records"], 0)
            self.assertEqual(result["total_research_records"], 2)
            self.assertEqual(csvfile.read_bytes(), data)

    def test_csv_bad_headers_and_width_fail(self):
        invalid = (
            (b'id,ID\n1,2\n', "duplicate CSV header"),
            (b'id, \n1,2\n', "nonempty header"),
            (b'id,title\n1,a,b\n', "expected 2"),
            (b'id,title\n1\n', "expected 2"),
            (b'id,title\n', "no data records"),
            (b'id,title\n1,"unclosed\n', "malformed CSV"),
        )
        for raw, reason in invalid:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "invalid.csv", raw)
                with self.assertRaisesRegex(ResearchJSONError, reason):
                    validate_repository(root)

    def test_csv_invalid_utf8_embedded_nul_and_symlink_blocked(self):
        for raw, message in ((b'id,value\n1,\xff\n', "invalid UTF-8"),
                             (b'id,value\n1,\x00\n', "NUL")):
            with self.subTest(message=message), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "row.csv", raw)
                with self.assertRaisesRegex(ResearchJSONError, message):
                    validate_repository(root)
        with tempfile.TemporaryDirectory() as root:
            outside = Path(root) / "outside.csv"
            outside.write_text("id,value\n1,2\n", encoding="utf-8")
            folder = Path(root) / "examples"
            folder.mkdir()
            (folder / "link.csv").symlink_to(outside)
            with self.assertRaisesRegex(ResearchJSONError, "symlinks"):
                validate_repository(root)

    def test_numeric_underflow_and_huge_integer_rejected(self):
        for raw, message in ((b'{"tiny":1e-999}', "underflow"),
                             (b'{"big":' + b'9' * 1025 + b'}', "1024 digit")):
            with self.subTest(message=message), tempfile.TemporaryDirectory() as root:
                self._artifact(root, "numeric.json", raw)
                with self.assertRaisesRegex(ResearchJSONError, message):
                    validate_repository(root)

    def test_cumulative_file_and_count_limits(self):
        with tempfile.TemporaryDirectory() as root:
            self._artifact(root, "first.json", b'{"id":1}')
            self._artifact(root, "second.json", b'{"id":2}')
            with patch.object(data_integrity, "MAX_FILES", 1):
                with self.assertRaisesRegex(ResearchJSONError, "file count"):
                    validate_repository(root)
            with patch.object(data_integrity, "MAX_TOTAL_BYTES", 10):
                with self.assertRaisesRegex(ResearchJSONError, "cumulative"):
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


if __name__ == "__main__":
    unittest.main()
