"""Synthetic Git-index regression tests for the issue #244 offline CI gate."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from scripts.check_research_artifacts import IntegrityError, audit_tracked_code_json


class TrackedCodeJSONIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        (self.root / "arbitrary" / "nested").mkdir(parents=True)
        (self.root / ".hidden").mkdir()
        (self.root / "arbitrary" / "nested" / "good.py").write_text(
            "raise RuntimeError('must not be executed by syntax gate')\n",
            encoding="utf-8",
        )
        (self.root / ".hidden" / "good.json").write_text(
            '{"items":[{"id":1}]}', encoding="utf-8"
        )
        self.git("add", "--", "arbitrary/nested/good.py", ".hidden/good.json")

    def git(self, *args):
        result = subprocess.run(
            ["git", "-C", str(self.root), *args], capture_output=True, text=True,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def test_checks_hidden_and_nested_files_without_executing_python(self):
        before = [
            (self.root / "arbitrary/nested/good.py").read_bytes(),
            (self.root / ".hidden/good.json").read_bytes(),
        ]
        result = audit_tracked_code_json(self.root)
        self.assertEqual(result["files"], 2)
        self.assertEqual(result["python"], 1)
        self.assertEqual(result["json"], 1)
        self.assertGreater(result["checked_bytes"], 0)
        self.assertEqual(before, [
            (self.root / "arbitrary/nested/good.py").read_bytes(),
            (self.root / ".hidden/good.json").read_bytes(),
        ])

    def test_ignores_untracked_invalid_files_but_checks_newly_staged_ones(self):
        bad = self.root / "arbitrary" / "untracked.py"
        bad.write_text("def invalid(:\n", encoding="utf-8")
        self.assertEqual(audit_tracked_code_json(self.root)["files"], 2)
        self.git("add", "--", "arbitrary/untracked.py")
        with self.assertRaisesRegex(IntegrityError, "invalid syntax"):
            audit_tracked_code_json(self.root)

    def test_rejects_unimported_python_syntax_errors_anywhere(self):
        path = self.root / "arbitrary/nested/good.py"
        path.write_text("def broken(:\n    pass\n", encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "good.py"):
            audit_tracked_code_json(self.root)

    def test_compiler_rejects_contextual_syntax_errors_ast_would_miss(self):
        path = self.root / "arbitrary/nested/good.py"
        for source in ("return 1\n", "break\n", "nonlocal x\n"):
            with self.subTest(source=source):
                path.write_text(source, encoding="utf-8")
                with self.assertRaisesRegex(IntegrityError, "good.py"):
                    audit_tracked_code_json(self.root)

    def test_rejects_duplicate_nested_json_keys_outside_data_directories(self):
        path = self.root / ".hidden/good.json"
        path.write_text('{"study":{"status":"unknown","status":"verified"}}', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "duplicate JSON object key"):
            audit_tracked_code_json(self.root)

    def test_untrusted_duplicate_key_is_not_echoed_from_worktree_or_index(self):
        path = self.root / ".hidden/good.json"
        secret = "secret-private-json-key-DO-NOT-LOG"
        payload = '{"' + secret + '":1,"' + secret + '":2}'
        # Failing checked-out input cannot print the content-derived key.
        path.write_text(payload, encoding="utf-8")
        with self.assertRaises(IntegrityError) as output:
            audit_tracked_code_json(self.root)
        self.assertIn("duplicate JSON object key", str(output.exception))
        self.assertNotIn(secret, str(output.exception))
        # A malformed staged blob must be equally private when worktree is valid.
        self.git("add", "--", ".hidden/good.json")
        path.write_text('{"repaired":true}', encoding="utf-8")
        with self.assertRaises(IntegrityError) as staged:
            audit_tracked_code_json(self.root)
        self.assertIn("Git index blob", str(staged.exception))
        self.assertNotIn(secret, str(staged.exception))

    def test_rejects_nan_infinity_underflow_and_overflow_in_tracked_json(self):
        path = self.root / ".hidden/good.json"
        for value in ("NaN", "Infinity", "-Infinity", "1e9999", "1e-9999"):
            with self.subTest(value=value):
                path.write_text('{"number":' + value + '}', encoding="utf-8")
                with self.assertRaises(IntegrityError):
                    audit_tracked_code_json(self.root)

    def test_rejects_non_utf8_and_truncated_json(self):
        path = self.root / ".hidden/good.json"
        for raw in (b'{"x":"\xff"}', b'{"incomplete":', b'{"unbalanced": [}'):
            with self.subTest(raw=raw):
                path.write_bytes(raw)
                with self.assertRaisesRegex(IntegrityError, "good.json"):
                    audit_tracked_code_json(self.root)

    def test_json_scalars_are_valid_syntax_outside_research_schema(self):
        # The tracked gate checks JSON syntax, not research-specific root schemas.
        (self.root / ".hidden/good.json").write_text("42\n", encoding="utf-8")
        self.assertEqual(audit_tracked_code_json(self.root)["json"], 1)

    def test_rejects_tracked_symlink_even_when_target_is_inside_checkout(self):
        alias = self.root / "arbitrary" / "alias.py"
        try:
            alias.symlink_to("nested/good.py")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks not supported")
        self.git("add", "--", "arbitrary/alias.py")
        with self.assertRaisesRegex(IntegrityError, "nonregular or unmerged"):
            audit_tracked_code_json(self.root)

    def test_rejects_unmerged_index_stage_even_without_a_worktree_file(self):
        # An unresolved index stage is not a valid committed checkout. Refuse it
        # before attempting to parse any file bytes.
        oid = self.git("hash-object", "-w", "--", ".hidden/good.json").stdout.strip()
        operation = subprocess.run(
            ["git", "-C", str(self.root), "update-index", "--index-info"],
            input=f"100644 {oid} 2\tconflicted.json\n",
            capture_output=True, text=True, timeout=20,
        )
        self.assertEqual(operation.returncode, 0, operation.stderr)
        with self.assertRaisesRegex(IntegrityError, "nonregular or unmerged"):
            audit_tracked_code_json(self.root)

    def test_rejects_symlinked_parent_even_with_regular_index_mode(self):
        tracked_parent = self.root / "arbitrary" / "nested"
        real_parent = self.root / "moved_original"
        tracked_parent.rename(real_parent)
        try:
            tracked_parent.symlink_to(real_parent, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("directory symlinks not supported")
        with self.assertRaisesRegex(IntegrityError, "symlinked parent directory"):
            audit_tracked_code_json(self.root)

    def test_python_encoding_cookie_is_honored_without_execution(self):
        # PEP 263 permits a non-UTF-8 Python source only when it declares its
        # encoding; the gate checks Python language syntax, not JSON rules.
        path = self.root / "arbitrary" / "nested" / "good.py"
        path.write_bytes(b"# coding: latin-1\nvalue = '\xe9'\n")
        self.assertEqual(audit_tracked_code_json(self.root)["python"], 1)
        path.write_bytes(b"value = '\xe9'\n")
        with self.assertRaisesRegex(IntegrityError, "good.py"):
            audit_tracked_code_json(self.root)

    def test_ancestor_symlink_swap_after_precheck_cannot_escape_checkout(self):
        # Deliberately replace an indexed parent *after* is_symlink reports
        # False. An ordinary path-based os.open follows the new ancestor link
        # and silently validates unrelated outside bytes instead of the file.
        import os
        if (not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY")
                or os.open not in os.supports_dir_fd):
            self.skipTest("POSIX descriptor-relative no-follow opening unavailable")
        tracked_parent = self.root / "arbitrary" / "nested"
        relocated_parent = self.root / "original_nested"
        outside = self.root / "outside_not_indexed"
        outside.mkdir()
        (outside / "good.py").write_text("different = True\n", encoding="utf-8")
        original_is_symlink = Path.is_symlink
        swapped = False

        def switch_after_check(path):
            nonlocal swapped
            observed = original_is_symlink(path)
            if path == tracked_parent and not swapped:
                tracked_parent.rename(relocated_parent)
                try:
                    tracked_parent.symlink_to(outside, target_is_directory=True)
                except (OSError, NotImplementedError):
                    relocated_parent.rename(tracked_parent)
                    self.skipTest("directory symlinks unavailable")
                swapped = True
            return observed

        with mock.patch.object(Path, "is_symlink", switch_after_check):
            with self.assertRaisesRegex(IntegrityError, "good.py"):
                audit_tracked_code_json(self.root)
        self.assertTrue(swapped)

    def test_rejects_fifo_replacing_tracked_regular_file_without_blocking(self):
        import os
        if not hasattr(os, "mkfifo"):
            self.skipTest("FIFO unavailable")
        path = self.root / "arbitrary/nested/good.py"
        path.unlink()
        try:
            os.mkfifo(path)
        except OSError:
            self.skipTest("FIFO creation unavailable")
        with self.assertRaisesRegex(IntegrityError, "not a regular file"):
            audit_tracked_code_json(self.root)

    def test_rejects_over_limit_file_even_when_size_grows(self):
        path = self.root / "arbitrary/nested/good.py"
        path.write_bytes(b"x" * 33)
        with self.assertRaisesRegex(IntegrityError, "file exceeds"):
            audit_tracked_code_json(self.root, max_file_bytes=32)

    def test_rejects_total_byte_limit_without_scanning_unbounded_input(self):
        with self.assertRaisesRegex(IntegrityError, "tracked artifact total"):
            audit_tracked_code_json(self.root, max_total_bytes=2)

    def test_rejects_git_tracked_file_missing_from_worktree(self):
        (self.root / ".hidden/good.json").unlink()
        with self.assertRaisesRegex(IntegrityError, "good.json"):
            audit_tracked_code_json(self.root)

    def test_rejects_non_repository_and_non_top_level_root(self):
        with tempfile.TemporaryDirectory() as other:
            with self.assertRaisesRegex(IntegrityError, "Git index"):
                audit_tracked_code_json(other)
        with self.assertRaisesRegex(IntegrityError, "Git top-level"):
            audit_tracked_code_json(self.root / "arbitrary")

    def test_enforces_per_file_and_total_byte_limits(self):
        with self.assertRaisesRegex(IntegrityError, "file exceeds"):
            audit_tracked_code_json(self.root, max_file_bytes=1)
        with self.assertRaisesRegex(IntegrityError, "tracked artifact total"):
            audit_tracked_code_json(self.root, max_total_bytes=1)

    def test_handles_newline_filename_without_splitting_git_index(self):
        special = self.root / "arbitrary" / "with\nnewline.json"
        special.write_text('{"valid":true}', encoding="utf-8")
        self.git("add", "--", "arbitrary/with\nnewline.json")
        self.assertEqual(audit_tracked_code_json(self.root)["json"], 2)
        special.write_text('{"valid":NaN}', encoding="utf-8")
        with self.assertRaises(IntegrityError) as ctx:
            audit_tracked_code_json(self.root)
        self.assertIn("with\\nnewline.json", str(ctx.exception))

    def test_invalid_staged_json_cannot_hide_behind_valid_worktree(self):
        path = self.root / ".hidden" / "good.json"
        path.write_text('{"status":"unknown","status":"verified"}', encoding="utf-8")
        self.git("add", "--", ".hidden/good.json")
        path.write_text('{"status":"unknown"}', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "Git index blob"):
            audit_tracked_code_json(self.root)

    def test_invalid_staged_python_cannot_hide_behind_valid_worktree(self):
        path = self.root / "arbitrary" / "nested" / "good.py"
        path.write_text("return 1\n", encoding="utf-8")
        self.git("add", "--", "arbitrary/nested/good.py")
        path.write_text("x = 1\n", encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "Git index blob"):
            audit_tracked_code_json(self.root)

    def test_valid_staged_and_modified_worktree_both_pass(self):
        path = self.root / ".hidden" / "good.json"
        path.write_text('{"staged":true}', encoding="utf-8")
        self.git("add", "--", ".hidden/good.json")
        path.write_text('{"working":true}', encoding="utf-8")
        result = audit_tracked_code_json(self.root)
        self.assertEqual(result["files"], 2)
        self.assertGreater(result["index_checked_bytes"], 0)

    def test_staged_blob_byte_limit_is_independent_of_worktree(self):
        path = self.root / ".hidden" / "good.json"
        path.write_text('{"long":"' + 'x' * 100 + '"}', encoding="utf-8")
        self.git("add", "--", ".hidden/good.json")
        path.write_text('{}', encoding="utf-8")
        with self.assertRaisesRegex(IntegrityError, "Git index blob exceeds"):
            audit_tracked_code_json(self.root, max_file_bytes=90)

    def test_rejects_empty_index_without_false_success(self):
        self.git("rm", "-q", "--cached", ".hidden/good.json", "arbitrary/nested/good.py")
        with self.assertRaisesRegex(IntegrityError, "no Git-tracked"):
            audit_tracked_code_json(self.root)

    def test_cli_retains_research_check_and_adds_tracked_metrics(self):
        for dirname in ("examples", "references", "research-notes"):
            (self.root / dirname).mkdir()
        (self.root / "examples" / "sample.json").write_text(
            '{"synthetic":true}', encoding="utf-8"
        )
        script = Path(__file__).resolve().parents[1] / "scripts" / "check_research_artifacts.py"
        result = subprocess.run(
            [sys.executable, str(script), "--root", str(self.root),
             "--tracked-code-json"],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(
            report["status"], "syntax_checked_not_scientifically_validated"
        )
        self.assertEqual(report["tracked_code_json"]["files"], 2)
        self.assertEqual(report["files"], 1)

    def test_cli_failure_output_never_echoes_secret_like_duplicate_key(self):
        # Synthetic token-shaped key; CI job logs are treated as public.
        secret = "ghp_SECRETTOKEN"
        for dirname in ("examples", "references", "research-notes"):
            (self.root / dirname).mkdir()
        (self.root / "examples" / "sample.json").write_text(
            '{"synthetic":true}', encoding="utf-8"
        )
        path = self.root / ".hidden" / "good.json"
        path.write_text('{"' + secret + '":1,"' + secret + '":2}', encoding="utf-8")
        self.git("add", "--", ".hidden/good.json")
        script = Path(__file__).resolve().parents[1] / "scripts" / "check_research_artifacts.py"
        result = subprocess.run(
            [sys.executable, str(script), "--root", str(self.root),
             "--tracked-code-json"],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate JSON object key", result.stderr)
        self.assertNotIn(secret, result.stderr)
        self.assertNotIn(secret, result.stdout)


if __name__ == "__main__":
    unittest.main()
