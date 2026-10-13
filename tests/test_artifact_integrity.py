"""Offline negative-path tests for CI's tracked-artifact integrity gate."""
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts.check_artifact_integrity import audit, inspect, tracked_files


class ArtifactIntegrityTests(unittest.TestCase):
    def test_valid_python_and_nested_json(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "valid.py").write_text("from pathlib import Path\nx = Path('a')\n",
                                           encoding="utf-8")
            (root / "valid.json").write_text(
                '{"items": [{"name": "ok", "metadata": {"scope": null}}]}',
                encoding="utf-8",
            )
            result = audit(root, ["valid.py", "valid.json"])
            self.assertTrue(result["ok"], result["errors"])
            self.assertEqual(result["checked"], {"python": 1, "json": 1})

    def test_duplicate_keys_nested_are_not_silently_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "bad.json").write_text(
                '{"evidence": {"citation": "one", "citation": "two"}}',
                encoding="utf-8",
            )
            result = audit(root, ["bad.json"])
            self.assertFalse(result["ok"])
            self.assertIn("duplicate JSON object key", result["errors"][0])

    def test_nonstandard_and_nonfinite_numbers_refused(self):
        for raw in ('{"n": NaN}', '{"n": Infinity}', '{"n": -Infinity}',
                    '{"n": 1e9999}'):
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                (root / "bad.json").write_text(raw, encoding="utf-8")
                self.assertIsNotNone(inspect(root, "bad.json"))

    def test_syntax_error_in_unimported_python_file_blocks_merge(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "new.py").write_text("def broken(:\n    pass\n", encoding="utf-8")
            result = audit(root, ["new.py"])
            self.assertFalse(result["ok"])
            self.assertIn("SyntaxError", result["errors"][0])

    def test_bad_utf8_is_not_accepted_or_replaced(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "bad.json").write_bytes(b'{"name":"\xff"}')
            self.assertIn("UnicodeDecodeError", inspect(root, "bad.json"))

    def test_missing_file_and_unsafe_parent_path_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertIn("missing", inspect(root, "missing.py"))
            self.assertIn("unsafe path", inspect(root, "../outside.py"))

    def test_external_symlink_cannot_escape_checkout(self):
        with tempfile.TemporaryDirectory() as rootdir, tempfile.TemporaryDirectory() as external:
            root = Path(rootdir)
            external_path = Path(external) / "outside.json"
            external_path.write_text('{"safe": true}', encoding="utf-8")
            link = root / "alias.json"
            try:
                link.symlink_to(external_path)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks are unavailable in the test environment")
            self.assertIn("symlink escapes", inspect(root, "alias.json"))

    def test_duplicate_tracked_paths_are_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "ok.json").write_text('{"ok": true}', encoding="utf-8")
            result = audit(root, ["ok.json", "ok.json"])
            self.assertFalse(result["ok"])
            self.assertTrue(any("duplicate tracked file path" in e for e in result["errors"]))

    def test_tracked_files_uses_index_not_untracked_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "-C", str(root), "init", "-q"],
                           check=True, capture_output=True)
            (root / "subdir").mkdir()
            (root / "subdir" / "retained.json").write_text(
                '{"source": "tracked"}', encoding="utf-8")
            (root / "untracked.json").write_text(
                '{"source": "not yet committed"}', encoding="utf-8")
            (root / "retained.py").write_text(
                "assert True\\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "--",
                            "subdir/retained.json", "retained.py"],
                           check=True, capture_output=True)
            self.assertEqual(set(tracked_files(root)),
                             {"subdir/retained.json", "retained.py"})

    def test_ignore_unsupported_file_suffix_without_accessing_it(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            result = audit(root, ["missing.md"])
            self.assertTrue(result["ok"])
            self.assertEqual(result["checked"], {"python": 0, "json": 0})


if __name__ == "__main__":
    unittest.main()
