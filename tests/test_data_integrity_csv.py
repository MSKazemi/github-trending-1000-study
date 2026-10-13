"""Synthetic-only CSV integrity regression tests for the canonical evidence validator."""
import tempfile
from pathlib import Path
import unittest

from trending_study.data_integrity import ResearchJSONError, validate_repository


class ResearchCSVIntegrityTests(unittest.TestCase):
    def _fixture(self, text=None, raw=None):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        base = root / "references"
        base.mkdir()
        csv = base / "sources.csv"
        if raw is not None:
            csv.write_bytes(raw)
        else:
            csv.write_text(text or "name,url\nexample,https://example.org\n", encoding="utf-8")
        return root, csv

    def test_quoted_comma_and_multiline_are_not_split(self):
        content = 'name,description\n"work,item","line 1\nline 2"\n'
        root, file = self._fixture(text=content)
        before = file.read_bytes()
        result = validate_repository(root)
        self.assertEqual(result["validated_csv_files"], 1)
        self.assertEqual(result["validated_csv_rows"], 1)
        self.assertEqual(result["json_documents_or_jsonl_records"], 0)
        self.assertEqual(file.read_bytes(), before)
        self.assertFalse(result["authenticated_research_evidence"])

    def test_existing_json_is_still_audited(self):
        root, file = self._fixture()
        (file.parent / "metadata.json").write_text('{"id":1}', encoding="utf-8")
        result = validate_repository(root)
        self.assertEqual(result["validated_files"], 2)
        self.assertEqual(result["json_documents_or_jsonl_records"], 1)
        self.assertEqual(result["validated_csv_rows"], 1)

    def test_header_collisions_are_blocked(self):
        for text in ("ID,id\n1,2\n", " id , ID \n1,2\n", ",value\n1,2\n", ""):
            with self.subTest(text=text):
                root, _ = self._fixture(text=text if text else " ")
                with self.assertRaisesRegex(ResearchJSONError, "CSV requires|duplicate CSV"):
                    validate_repository(root)

    def test_ragged_csv_and_invalid_quoting_are_blocked(self):
        for text in ("a,b\n1\n", "a,b\n1,2,3\n", 'a,b\n"unclosed,2\n'):
            with self.subTest(text=text):
                root, _ = self._fixture(text=text)
                with self.assertRaises(ResearchJSONError):
                    validate_repository(root)

    def test_nul_and_invalid_utf8_are_blocked(self):
        for raw in (b"a,b\n1,\x00\n", b"a,b\n1,\xff\n"):
            with self.subTest(raw=raw):
                root, _ = self._fixture(raw=raw)
                with self.assertRaises(ResearchJSONError):
                    validate_repository(root)

    def test_symlinked_csv_is_not_accepted(self):
        root, original = self._fixture()
        alias = root / "references" / "alias.csv"
        try:
            alias.symlink_to(original)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks not available")
        with self.assertRaisesRegex(ResearchJSONError, "symlinks"):
            validate_repository(root)

    def test_csv_is_structural_not_proof_of_reuse(self):
        root, _ = self._fixture(text="repo,verified\nfictional,yes\n")
        result = validate_repository(root)
        self.assertFalse(result["authenticated_research_evidence"])
        self.assertFalse(result["modifies_artifacts"])


if __name__ == "__main__":
    unittest.main()
