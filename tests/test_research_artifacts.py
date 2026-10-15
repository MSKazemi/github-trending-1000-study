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

    def test_optional_research_and_templates_json_are_validated(self):
        research = self.root / "research" / "company-intelligence"
        research.mkdir(parents=True)
        (research / "lead.json").write_text('{"source": "dated"}', encoding="utf-8")
        templates = self.root / "templates"
        templates.mkdir()
        review = templates / "review.jsonl"
        review.write_text('{"task": "t01"}\n', encoding="utf-8")
        result = audit_repository(self.root)
        self.assertEqual(result["files"], 5)
        self.assertEqual(result["json"], 2)
        self.assertEqual(result["jsonl"], 2)
        review.write_text('{"task": 1, "task": 2}\n', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "duplicate JSON object key"):
            audit_repository(self.root)

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

    def test_reject_float_overflow_and_underflow_without_silent_data_loss(self):
        file = self.root / "examples" / "case.json"
        for raw in ("1e10000", "-1e10000", "1e-10000", "-1e-10000"):
            with self.subTest(value=raw):
                file.write_text('{"numeric":' + raw + '}', encoding="utf-8")
                with self.assertRaisesRegex(IntegrityError, "overflows or underflows"):
                    audit_repository(self.root)

    def test_reject_extreme_integer_before_version_dependent_parser_failure(self):
        file = self.root / "examples" / "case.json"
        file.write_text('{"numeric":' + '9' * 1500 + '}', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "1024 digits"):
            audit_repository(self.root)

    def test_reject_nul_in_json_and_csv(self):
        for relative, content in (
            ("examples/case.json", '{"k":"a\\u0000b"}' + "\\x00"),
            ("references/registry.csv", "id,note\\n1,bad\\x00value\\n"),
        ):
            with self.subTest(path=relative):
                file = self.root / relative
                original = file.read_text(encoding="utf-8")
                try:
                    file.write_text(content.replace("\\x00", chr(0)).replace("\\n", chr(10)), encoding="utf-8")
                    with self.assertRaisesRegex(IntegrityError, "embedded NUL"):
                        audit_repository(self.root)
                finally:
                    file.write_text(original, encoding="utf-8")

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

    def test_cumulative_bytes_are_bounded_separately_from_per_file(self):
        with self.assertRaisesRegex(IntegrityError, "cumulative research artifacts"):
            audit_repository(self.root, max_total_bytes=12)

    def test_explicit_json_nesting_limit_is_cross_version_deterministic(self):
        for depth in (1, 127, 128):
            with self.subTest(accepted_depth=depth):
                raw = '[' * depth + '0' + ']' * depth
                self.assertEqual(validate_text(Path("safe.json"), raw), 1)
        with self.assertRaisesRegex(IntegrityError, "JSON nesting exceeds 128"):
            validate_text(Path("too-deep.json"), '[' * 129 + '0' + ']' * 129)

    def test_braces_and_escaped_quotes_inside_strings_do_not_count_as_nesting(self):
        raw = json.dumps({"literal": ('[{}] "' + chr(92) + ' end ') * 300})
        self.assertEqual(validate_text(Path("literal.json"), raw), 1)

    def test_deeply_nested_json_fails_as_controlled_integrity_error(self):
        file = self.root / "examples" / "case.json"
        file.write_text('{"nested":' + '[' * 1500 + '0' + ']' * 1500 + '}',
                        encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "case.json"):
            audit_repository(self.root)

    def test_csv_unterminated_quotes_fail_closed(self):
        file = self.root / "references" / "registry.csv"
        for value in ('id,note\n1,"unfinished\n', 'id,note\n1,"value"junk\n'):
            with self.subTest(value=value):
                file.write_text(value.replace("\\n", "\n"), encoding="utf-8")
                with self.assertRaisesRegex(IntegrityError, "registry.csv"):
                    audit_repository(self.root)

    def test_csv_symlink_file_is_rejected(self):
        source = self.root / "references" / "registry.csv"
        alias = self.root / "references" / "alias.csv"
        try:
            alias.symlink_to(source)
        except (OSError, NotImplementedError):
            self.skipTest("symlink unsupported on test filesystem")
        with self.assertRaisesRegex(IntegrityError, "symlink forbidden"):
            audit_repository(self.root)

    def test_csv_header_only_fails_consistently_in_both_validators(self):
        file = self.root / "references" / "registry.csv"
        file.write_text("id,note\n", encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "no data records"):
            audit_repository(self.root)
        # The independently maintained legacy validator must not disagree on
        # what counts as a valid baseline research data artifact.
        from trending_study.data_integrity import ResearchJSONError, validate_repository
        with self.assertRaisesRegex(ResearchJSONError, "no data records"):
            validate_repository(self.root)

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
