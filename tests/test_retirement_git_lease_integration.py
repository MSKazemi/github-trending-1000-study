"""Offline Git transport regression: never delete a moved branch ref.

This tests real Git receive-pack semantics against a disposable local bare
repository, without network access or permissions to alter GitHub.
"""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts.retire_merged_branches import GitHubClient


@unittest.skipUnless(shutil.which("git"), "git executable required")
class RetirementLeaseIntegrationTests(unittest.TestCase):
    def run_git(self, *args, cwd=None, ok=True):
        result = subprocess.run(
            ["git", *map(str, args)], cwd=cwd, env=self.env,
            capture_output=True, text=True, timeout=20, check=False,
        )
        if ok and result.returncode:
            self.fail("git command failed: " + result.stderr[:500])
        return result

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.remote = base / "remote.git"
        self.local = base / "work"
        self.env = os.environ.copy()
        self.env["GIT_TERMINAL_PROMPT"] = "0"
        self.env["GIT_CONFIG_NOSYSTEM"] = "1"
        self.run_git("init", "--bare", "-q", self.remote)
        self.run_git("init", "-q", self.local)
        self.run_git("-c", "user.name=Fixture", "-c",
                     "user.email=fixture@example.test",
                     "commit", "-q", "--allow-empty", "-m", "Initial",
                     cwd=self.local)
        self.first = self.run_git("rev-parse", "HEAD",
                                  cwd=self.local).stdout.strip()
        self.assertEqual(len(self.first), 40)
        self.run_git("push", "-q", self.remote,
                     "HEAD:refs/heads/audited", cwd=self.local)

    def remote_tip(self):
        return self.run_git("--git-dir", self.remote, "rev-parse",
                            "refs/heads/audited", ok=False)

    def leased_delete(self, expected_sha):
        return self.run_git("push", "--porcelain",
                            "--force-with-lease=refs/heads/audited:" + expected_sha,
                            self.remote, ":refs/heads/audited", cwd=self.local,
                            ok=False)

    def test_matching_sha_deletes_only_branch_and_preserves_archive(self):
        self.run_git("tag", "branch-archive/audited", self.first, cwd=self.local)
        self.run_git("push", "-q", self.remote,
                     "refs/tags/branch-archive/audited", cwd=self.local)
        result = self.leased_delete(self.first)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotEqual(self.remote_tip().returncode, 0)
        archive = self.run_git("--git-dir", self.remote, "rev-parse",
                               "refs/tags/branch-archive/audited").stdout.strip()
        self.assertEqual(archive, self.first)
        self.assertEqual(self.run_git("--git-dir", self.remote,
                                      "cat-file", "-t", archive).stdout.strip(),
                         "commit")

    def test_stale_sha_lease_fails_even_if_ref_changed_after_preflight(self):
        self.run_git("-c", "user.name=Fixture", "-c",
                     "user.email=fixture@example.test", "commit", "-q",
                     "--allow-empty", "-m", "Concurrent update", cwd=self.local)
        self.run_git("push", "-q", self.remote, "HEAD:refs/heads/audited",
                     cwd=self.local)
        newest = self.remote_tip().stdout.strip()
        self.assertNotEqual(newest, self.first)
        result = self.leased_delete(self.first)
        self.assertNotEqual(result.returncode, 0, "stale lease removed a moved ref")
        self.assertEqual(self.remote_tip().stdout.strip(), newest)

    def test_authenticated_transport_cannot_write_inherited_trace_files(self):
        # Exercise Git's real Trace2 behavior without making any network call.
        # The fixture header is intentionally not a usable credential.
        base = Path(self.temp.name)
        configured_trace = base / "configured-trace.json"
        inherited_trace = base / "inherited-trace.json"
        config = base / "gitconfig"
        config.write_text(
            "[trace2]\n\teventTarget = " + str(configured_trace)
            + "\n\tenvVars = GIT_CONFIG_VALUE_0\n", encoding="utf-8")
        real_run = subprocess.run

        def inspect_transport(command, **kwargs):
            env = kwargs["env"]
            self.assertFalse("GIT_TRACE2_ENV_VARS" in env)
            self.assertFalse("GIT_CURL_VERBOSE" in env)
            return real_run(["git", "version"], **kwargs)

        with patch.dict(os.environ, {
            "GIT_CONFIG_GLOBAL": str(config),
            "GIT_TRACE2_EVENT": str(inherited_trace),
            "GIT_TRACE2_ENV_VARS": "GIT_CONFIG_VALUE_0",
            "GIT_CURL_VERBOSE": "1",
        }), patch("scripts.retire_merged_branches.subprocess.run",
                  side_effect=inspect_transport):
            GitHubClient("owner/repository", "offline-only-fixture-token").delete_with_lease(
                "audited", self.first)
        self.assertFalse(inherited_trace.exists())
        self.assertFalse(configured_trace.exists())


if __name__ == "__main__":
    unittest.main()
