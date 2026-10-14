"""Offline negative tests for fail-closed, non-loss branch retirement."""
import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from scripts.retire_merged_branches import (
    ARCHIVE_PREFIX, ApiNotFound, CleanupError, GitHubClient, execute, main,
    retire_one, validate_plan,
)

REPO = "MSKazemi/github-trending-1000-study"
SHA = "a" * 40
MERGE = "b" * 40
NAME = "fix/small-reviewed-change"

def item():
    return {"branch": NAME, "expected_sha": SHA,
            "merged_pr": 123, "merge_commit_sha": MERGE}

def plan():
    return {"schema_version": "1.0", "repository": REPO,
            "source_main_sha": "c" * 40, "archive_prefix": ARCHIVE_PREFIX,
            "branches": [item()]}

class FakeClient:
    def __init__(self):
        self.repository = REPO
        self.deleted = []
        self.posts = []
        self.open = []
        self.sha = SHA
        self.protected = False
        self.pr_merged = True
        self.pr_head = SHA
        self.tag_sha = None
        self.race_on_second_ref = False
        self.ref_checks = 0
        self.absent = False
        self.lease_race = False
        self.ancestor = True
        self.open_on_second_check = False
        self.open_checks = 0
        self.archive_moved_after_first_check = False
        self.archive_checks = 0

    def get(self, path):
        if path == f"/repos/{REPO}":
            return {"default_branch": "main"}
        if "/git/ref/tags/" in path:
            if self.tag_sha is None:
                raise ApiNotFound("not found")
            self.archive_checks += 1
            if self.archive_moved_after_first_check and self.archive_checks > 1:
                return {"object": {"sha": "f" * 40}}
            return {"object": {"sha": self.tag_sha}}
        if "/git/ref/heads/" in path:
            if self.absent:
                raise ApiNotFound("branch already retired")
            self.ref_checks += 1
            if self.race_on_second_ref and self.ref_checks == 2:
                return {"object": {"sha": "f" * 40}}
            return {"object": {"sha": self.sha}}
        if path == f"/repos/{REPO}/branches/main":
            return {"commit": {"sha": "c" * 40}}
        if "/compare/" in path:
            return {"status": "ahead" if self.ancestor else "diverged",
                    "behind_by": 0 if self.ancestor else 1}
        if "/branches/" in path:
            return {"protected": self.protected, "commit": {"sha": self.sha}}
        if "/pulls/123" in path:
            return {"merged": self.pr_merged,
                    "state": "closed", "head": {"ref": NAME, "sha": self.pr_head,
                                                   "repo": {"full_name": REPO}},
                    "base": {"ref": "main"}, "merge_commit_sha": MERGE}
        if "/pulls?" in path:
            self.open_checks += 1
            if self.open_on_second_check and self.open_checks > 1:
                return [{"number": 456}]
            return self.open
        raise AssertionError("unexpected GET: " + path)

    def post(self, path, payload):
        self.posts.append((path, payload))
        self.tag_sha = payload["sha"]
        return {"ref": payload["ref"], "object": {"sha": self.tag_sha}}

    def delete_with_lease(self, branch, expected_sha):
        if self.tag_sha != SHA:
            raise AssertionError("deleted without verified recovery tag")
        if self.lease_race:
            raise CleanupError("git compare-and-delete lease rejected")
        if self.sha != expected_sha or branch != NAME:
            raise AssertionError("unexpected SHA-leased delete")
        self.deleted.append("/git/refs/heads/" + branch)
        self.absent = True

class BranchCleanupTests(unittest.TestCase):
    def test_approved_single_branch_backed_up_before_deletion(self):
        fake = FakeClient()
        result = execute(plan(), fake)
        self.assertEqual(result[0]["status"], "retired_with_archive_tag")
        self.assertEqual(len(fake.posts), 1)
        self.assertEqual(len(fake.deleted), 1)
        self.assertTrue(fake.absent)
        self.assertIn("/git/refs/heads/fix/small-reviewed-change", fake.deleted[0])
        self.assertEqual(fake.posts[0][1]["ref"],
                         "refs/tags/" + ARCHIVE_PREFIX + "/" + NAME)
        self.assertEqual(fake.posts[0][1]["sha"], SHA)

    def test_changed_head_is_never_archived_or_deleted(self):
        fake = FakeClient()
        fake.sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item()), "blocked_changed_ref")
        self.assertEqual(fake.posts, [])
        self.assertEqual(fake.deleted, [])

    def test_never_delete_protected_branch(self):
        fake = FakeClient()
        fake.protected = True
        self.assertEqual(retire_one(fake, REPO, item()), "blocked_protected_or_changed")
        self.assertFalse(fake.deleted)

    def test_unmerged_or_changed_pr_is_blocked(self):
        for attr, bad in (("pr_merged", False), ("pr_head", "f" * 40)):
            fake = FakeClient()
            setattr(fake, attr, bad)
            with self.subTest(attr=attr):
                self.assertEqual(retire_one(fake, REPO, item()),
                                 "blocked_pr_not_identical_and_merged")
                self.assertFalse(fake.deleted)

    def test_open_pr_blocks_branch_retirement(self):
        fake = FakeClient()
        fake.open = [{"number": 9}]
        self.assertEqual(retire_one(fake, REPO, item()), "blocked_open_pr")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_existing_wrong_archival_tag_fails_closed(self):
        fake = FakeClient()
        fake.tag_sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item()), "blocked_archive_tag_conflict")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_existing_correct_archival_tag_is_idempotently_reused(self):
        fake = FakeClient()
        fake.tag_sha = SHA
        self.assertEqual(retire_one(fake, REPO, item()), "retired_with_archive_tag")
        self.assertFalse(fake.posts)
        self.assertEqual(len(fake.deleted), 1)

    def test_race_after_archive_blocks_delete(self):
        fake = FakeClient()
        fake.race_on_second_ref = True
        self.assertEqual(retire_one(fake, REPO, item()), "blocked_raced_branch_update")
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)

    def test_audit_live_cannot_create_archives_or_delete(self):
        fake = FakeClient()
        results = execute(plan(), fake, audit_only=True)
        self.assertEqual(results[0]["status"], "eligible_read_only")
        self.assertEqual(fake.posts, [])
        self.assertEqual(fake.deleted, [])

    def test_live_audit_blocks_wrong_archived_sha_without_writes(self):
        fake = FakeClient()
        fake.tag_sha = "f" * 40
        results = execute(plan(), fake, audit_only=True)
        self.assertEqual(results[0]["status"], "blocked_archive_tag_conflict")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_live_audit_accepts_matching_existing_archive(self):
        fake = FakeClient()
        fake.tag_sha = SHA
        results = execute(plan(), fake, audit_only=True)
        self.assertEqual(results[0]["status"], "eligible_read_only")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_not_in_current_main_history_blocks_even_merged_pr(self):
        fake = FakeClient()
        fake.ancestor = False
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_merge_not_in_main")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_atomic_remote_sha_lease_rejects_update_after_final_read(self):
        fake = FakeClient()
        fake.lease_race = True
        results = execute(plan(), fake)
        self.assertEqual(results[0]["status"], "error_CleanupError")
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)
        self.assertFalse(fake.absent)

    def test_new_open_pr_between_checks_blocks_sha_leased_delete(self):
        fake = FakeClient()
        fake.open_on_second_check = True
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_new_open_pr")
        self.assertEqual(fake.open_checks, 2)
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)

    def test_repointed_archive_tag_after_initial_check_blocks_delete(self):
        fake = FakeClient()
        fake.archive_moved_after_first_check = True
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_archive_changed_before_delete")
        self.assertEqual(fake.archive_checks, 2)
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)

    def test_absent_branch_requires_exact_archived_original_sha(self):
        fake = FakeClient()
        fake.absent = True
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_absent_without_archive")
        fake.tag_sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_absent_without_archive")
        fake.tag_sha = SHA
        self.assertEqual(retire_one(fake, REPO, item()), "already_absent")

    def test_incomplete_open_pr_listing_is_not_assumed_empty(self):
        fake = FakeClient()
        fake.open = [{"number": n} for n in range(100)]
        self.assertEqual(retire_one(fake, REPO, item()),
                         "blocked_incomplete_open_pr_check")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    @patch("scripts.retire_merged_branches.subprocess.run")
    def test_git_lease_uses_exact_expected_sha_and_no_token_arguments(self, runner):
        runner.return_value.returncode = 0
        client = GitHubClient(REPO, "offline-only-fixture-token")
        client.delete_with_lease(NAME, SHA)
        cmd = runner.call_args.args[0]
        env = runner.call_args.kwargs["env"]
        self.assertIn("--force-with-lease=refs/heads/" + NAME + ":" + SHA, cmd)
        self.assertEqual(cmd[-1], ":refs/heads/" + NAME)
        self.assertNotIn("offline-only-fixture-token", " ".join(cmd))
        self.assertTrue(env["GIT_CONFIG_VALUE_0"].startswith("AUTHORIZATION: basic "))
        self.assertEqual(env["GIT_TERMINAL_PROMPT"], "0")

    @patch("scripts.retire_merged_branches.subprocess.run")
    def test_failed_sha_lease_is_not_retried_or_force_deleted(self, runner):
        runner.return_value.returncode = 1
        client = GitHubClient(REPO, "offline-only-fixture-token")
        with self.assertRaisesRegex(CleanupError, "SHA lease rejected"):
            client.delete_with_lease(NAME, SHA)
        self.assertEqual(runner.call_count, 1)

    def test_privileged_retirement_workflow_is_manual_only(self):
        workflow = Path(".github/workflows/retire-verified-branches.yml").read_text(
            encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\n  push:", workflow)
        self.assertNotIn("\n  pull_request:", workflow)
        self.assertIn("inputs.mode == 'audit'", workflow)
        self.assertIn("inputs.mode == 'retire'", workflow)
        # The write-capable job must be disabled unless a repository admin
        # deliberately sets a separate variable after independent review.
        # The current integration cannot mint a write token through this job,
        # even if an administrator sets the approval variable. Activation
        # requires its own reviewed PR that removes the unconditional false.
        self.assertIn("if: ${{ false &&", workflow)
        self.assertIn("vars.BRANCH_RETIREMENT_APPROVED == 'true'", workflow)
        self.assertIn("github.repository == 'MSKazemi/github-trending-1000-study'", workflow)
        self.assertIn("inputs.confirmation == 'RETIRE_VERIFIED_MERGED_BRANCHES'", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("contents: write", workflow)

    def test_cli_destructive_mode_requires_exact_confirmation(self):
        self.assertEqual(main([
            "--plan", "ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json",
            "--execute",
        ]), 2)

    def test_plan_rejects_duplicate_unknown_or_default_branches(self):
        for bad in ("main", "a/../b", "refs/heads/foo", "a//b", "branch..old"):
            p = plan()
            p["branches"][0]["branch"] = bad
            with self.subTest(branch=bad), self.assertRaises(CleanupError):
                validate_plan(p)
        p = plan()
        p["branches"].append(copy.deepcopy(p["branches"][0]))
        with self.assertRaisesRegex(CleanupError, "duplicate"):
            validate_plan(p)

    def test_plan_requires_exact_shas_and_no_extra_fields(self):
        for key in ("expected_sha", "merge_commit_sha"):
            p = plan()
            p["branches"][0][key] = "deadbeef"
            with self.subTest(key=key), self.assertRaises(CleanupError):
                validate_plan(p)
        p = plan()
        p["delete_all"] = True
        with self.assertRaises(CleanupError):
            validate_plan(p)

    def test_repo_mismatch_stops_before_actions(self):
        fake = FakeClient()
        fake.repository = "another/repository"
        with self.assertRaisesRegex(CleanupError, "disagrees"):
            execute(plan(), fake)
        self.assertFalse(fake.deleted)

if __name__ == "__main__":
    unittest.main()
