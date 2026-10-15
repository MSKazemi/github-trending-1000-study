"""Synthetic standalone news-reader regressions; no source retrieval."""
from contextlib import redirect_stderr
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trending_study import news_corpus

FIXTURE = Path(__file__).parent / "fixtures/news_corpus/NEWS-2026-0001.json"


class NewsInputSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / FIXTURE.name
        self.path.write_bytes(FIXTURE.read_bytes())

    @unittest.skipUnless(hasattr(os, "O_NOFOLLOW"), "no-follow file opening required")
    def test_leaf_symlink_swap_before_open_is_rejected(self):
        target = self.root.parent / (self.root.name + "-external.json")
        target.write_bytes(FIXTURE.read_bytes())
        self.addCleanup(target.unlink)
        real_open = os.open

        def replace_file(path, flags, *args, **kwargs):
            if Path(path) == self.path:
                self.path.unlink()
                self.path.symlink_to(target)
            return real_open(path, flags, *args, **kwargs)

        with patch("trending_study.news_corpus.os.open", side_effect=replace_file):
            with self.assertRaises(ValueError) as raised:
                news_corpus.validate_directory(self.root)
        self.assertNotIsInstance(raised.exception, OSError)
        self.assertNotIn(str(self.root), str(raised.exception))
        self.assertNotIn(self.path.name, str(raised.exception))
        self.assertEqual(target.read_bytes(), FIXTURE.read_bytes())
        # The CLI must not echo the OS error's full private input path either.
        self.path.unlink()
        self.path.write_bytes(FIXTURE.read_bytes())
        error = io.StringIO()
        with patch("trending_study.news_corpus.os.open", side_effect=replace_file), \
                redirect_stderr(error), self.assertRaises(SystemExit) as exc:
            news_corpus.main(["--directory", str(self.root)])
        self.assertEqual(exc.exception.code, 2)
        self.assertIn("ordinary non-symlink", error.getvalue())
        self.assertNotIn(str(self.root), error.getvalue())
        self.assertNotIn(str(self.path), error.getvalue())
        self.assertNotIn("Errno", error.getvalue())
        self.assertNotIn("Traceback", error.getvalue())

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO support required")
    def test_fifo_swap_is_rejected_without_a_writer(self):
        real_open = os.open

        def replace_file(path, flags, *args, **kwargs):
            if Path(path) == self.path:
                self.path.unlink()
                os.mkfifo(self.path)
            return real_open(path, flags, *args, **kwargs)

        with patch("trending_study.news_corpus.os.open", side_effect=replace_file):
            with self.assertRaisesRegex(ValueError, "ordinary JSON file"):
                news_corpus.validate_directory(self.root)

    def test_growth_after_descriptor_stat_cannot_exceed_actual_read_limit(self):
        real_stat = os.fstat
        limit = self.path.stat().st_size

        def grow_file(descriptor):
            old = real_stat(descriptor)
            with self.path.open("ab") as stream:
                stream.write(b" " * 128)
            return old

        with patch.object(news_corpus, "MAX_FILE_BYTES", limit), patch(
            "trending_study.news_corpus.os.fstat", side_effect=grow_file
        ):
            with self.assertRaisesRegex(ValueError, "file-size limit"):
                news_corpus.validate_directory(self.root)

    def test_total_limit_counts_actual_bytes_not_stale_metadata(self):
        data = json.loads(FIXTURE.read_text())
        data["id"] = "NEWS-2026-0002"
        data["canonical_url"] = "https://example.org/another-synthetic-item"
        second = self.root / "NEWS-2026-0002.json"
        second.write_text(json.dumps(data))
        limit = self.path.stat().st_size + second.stat().st_size - 1
        with patch.object(news_corpus, "MAX_TOTAL_BYTES", limit):
            with self.assertRaisesRegex(ValueError, "total research artifact byte limit"):
                news_corpus.validate_directory(self.root)

    def test_cli_does_not_echo_duplicate_private_key_or_traceback(self):
        private_key = "PRIVATE-fixture-contact-token-name"
        # A valid JSON object with duplicate private keys reaches the strict
        # decoder; neither key nor source content belongs in CLI diagnostics.
        self.path.write_text('{"' + private_key + '":1,"' + private_key + '":2}')
        error = io.StringIO()
        with redirect_stderr(error), self.assertRaises(SystemExit) as exc:
            news_corpus.main(["--directory", str(self.root)])
        self.assertEqual(exc.exception.code, 2)
        self.assertIn("invalid or ambiguous research JSON", error.getvalue())
        self.assertNotIn(private_key, error.getvalue())
        self.assertNotIn("Traceback", error.getvalue())

    def test_undeclared_file_names_do_not_expose_private_path_details(self):
        for kind in ("unexpected_json", "unexpected_file", "nested", "symlink"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                (root / FIXTURE.name).write_bytes(FIXTURE.read_bytes())
                private = root / "PRIVATE-synthetic-person-name.json"
                if kind == "unexpected_json":
                    private.write_text('{}', encoding="utf-8")
                elif kind == "unexpected_file":
                    private = private.with_suffix(".txt")
                    private.write_text("unrelated", encoding="utf-8")
                elif kind == "nested":
                    private.mkdir()
                else:
                    try:
                        private.symlink_to(root / FIXTURE.name)
                    except (OSError, NotImplementedError):
                        self.skipTest("symlinks not available")
                with self.assertRaises(ValueError) as raised:
                    news_corpus.validate_directory(root)
                self.assertNotIn("PRIVATE", str(raised.exception))
                self.assertNotIn(str(root), str(raised.exception))

    def test_deep_json_fails_with_controlled_diagnostic(self):
        self.path.write_text("[" * 2000 + "0" + "]" * 2000)
        # C decoder recursion thresholds vary across supported interpreters;
        # either decoding or the record-shape gate must reject this input.
        with self.assertRaises(ValueError):
            news_corpus.validate_directory(self.root)
        with patch("trending_study.news_corpus.decode_research_json",
                   side_effect=RecursionError("PRIVATE synthetic input")):
            with self.assertRaisesRegex(ValueError, "invalid or ambiguous research JSON"):
                news_corpus.validate_directory(self.root)


if __name__ == "__main__":
    unittest.main()
