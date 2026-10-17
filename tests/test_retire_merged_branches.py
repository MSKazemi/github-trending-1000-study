"""Offline negative tests for fail-closed, non-loss branch retirement."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
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
        self.pr_payload_override = None
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
        self.main_sha = "c" * 40
        self.main_reads = 0
        self.main_change_on_read = None
        self.archive_rules_installed = True
        self.archive_rules_enforcement = "active"
        self.archive_rules_bypass = []
        self.archive_rules_scope = "refs/tags/branch-archive/**/*"
        self.archive_rules_types = ["update", "deletion"]
        self.archive_rules_detail_reads = 0
        self.archive_rules_weaken_after = None

    def get(self, path):
        if path.startswith(f"/repos/{REPO}/rulesets?"):
            if not self.archive_rules_installed:
                return []
            return [{"id": 27, "name": "immutable-branch-archive-tags",
                     "target": "tag", "enforcement": self.archive_rules_enforcement,
                     "source": REPO}]
        if path == f"/repos/{REPO}/rulesets/27":
            self.archive_rules_detail_reads += 1
            changed = (self.archive_rules_weaken_after is not None and
                       self.archive_rules_detail_reads >= self.archive_rules_weaken_after)
            return {"id": 27, "name": "immutable-branch-archive-tags",
                    "target": "tag",
                    "enforcement": "evaluate" if changed else self.archive_rules_enforcement,
                    "source": REPO, "bypass_actors": self.archive_rules_bypass,
                    "conditions": {"ref_name": {"include": [self.archive_rules_scope],
                                                "exclude": []}},
                    "rules": [({"type": "update",
                               "parameters": {"update_allows_fetch_and_merge": False}}
                              if kind == "update" else {"type": kind})
                              for kind in self.archive_rules_types]}

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
            self.main_reads += 1
            live_sha = (("f" * 40) if self.main_change_on_read is not None
                        and self.main_reads >= self.main_change_on_read
                        else self.main_sha)
            return {"commit": {"sha": live_sha}}
        if "/compare/" in path:
            return {"status": "ahead" if self.ancestor else "diverged",
                    "behind_by": 0 if self.ancestor else 1}
        if "/branches/" in path:
            return {"protected": self.protected, "commit": {"sha": self.sha}}
        if "/pulls/123" in path:
            if self.pr_payload_override is not None:
                return copy.deepcopy(self.pr_payload_override)
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

    def test_direct_destructive_helper_requires_approved_main(self):
        fake = FakeClient()
        # Calling the lower-level helper must not bypass execute()'s
        # frozen-main approval check, even if all fake rulesets are active.
        with self.assertRaisesRegex(CleanupError, "approved main SHA"):
            retire_one(fake, REPO, item())
        self.assertEqual(fake.ref_checks, 0)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

        # An arbitrary repo argument must not reuse another client's token.
        with self.assertRaisesRegex(CleanupError, "repository differs"):
            retire_one(fake, "other/repo", item(),
                       expected_main_sha="c" * 40)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

        # A direct, explicitly pinned call still checks current main and
        # blocks before archive publication or leased deletion.
        fake.main_sha = "f" * 40
        self.assertEqual(retire_one(
            fake, REPO, item(), expected_main_sha="c" * 40
        ), "blocked_main_moved")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_changed_head_is_never_archived_or_deleted(self):
        fake = FakeClient()
        fake.sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "blocked_changed_ref")
        self.assertEqual(fake.posts, [])
        self.assertEqual(fake.deleted, [])

    def test_never_delete_protected_branch(self):
        fake = FakeClient()
        fake.protected = True
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "blocked_protected_or_changed")
        self.assertFalse(fake.deleted)

    def test_missing_or_null_nested_pr_repo_blocks_retirement_without_archive(self):
        # Merged PRs can have a deleted/absent head repository. That is
        # unverifiable, not permission to clean up a branch.
        valid = FakeClient().get(f"/repos/{REPO}/pulls/123")
        malformed = [
            [],
            {},
            dict(valid, head=None),
            dict(valid, base=None),
            dict(valid, head=dict(valid["head"], repo=None)),
            dict(valid, head=dict(valid["head"], repo=[])),
            dict(valid, head=dict(valid["head"], repo={})),
        ]
        for record in malformed:
            fake = FakeClient()
            fake.pr_payload_override = record
            with self.subTest(shape=str(record)[:65]):
                results = execute(plan(), fake)
                self.assertEqual(results[0]["status"],
                                 "blocked_pr_not_identical_and_merged")
                self.assertEqual(fake.posts, [])
                self.assertEqual(fake.deleted, [])

    def test_unmerged_or_changed_pr_is_blocked(self):
        for attr, bad in (("pr_merged", False), ("pr_head", "f" * 40)):
            fake = FakeClient()
            setattr(fake, attr, bad)
            with self.subTest(attr=attr):
                self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
                                 "blocked_pr_not_identical_and_merged")
                self.assertFalse(fake.deleted)

    def test_open_pr_blocks_branch_retirement(self):
        fake = FakeClient()
        fake.open = [{"number": 9}]
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "blocked_open_pr")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_existing_wrong_archival_tag_fails_closed(self):
        fake = FakeClient()
        fake.tag_sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "blocked_archive_tag_conflict")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_existing_correct_archival_tag_is_idempotently_reused(self):
        fake = FakeClient()
        fake.tag_sha = SHA
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "retired_with_archive_tag")
        self.assertFalse(fake.posts)
        self.assertEqual(len(fake.deleted), 1)

    def test_race_after_archive_blocks_delete(self):
        fake = FakeClient()
        fake.race_on_second_ref = True
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "blocked_raced_branch_update")
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
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
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
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
                         "blocked_new_open_pr")
        self.assertEqual(fake.open_checks, 2)
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)

    def test_repointed_archive_tag_after_initial_check_blocks_delete(self):
        fake = FakeClient()
        fake.archive_moved_after_first_check = True
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
                         "blocked_archive_changed_before_delete")
        self.assertEqual(fake.archive_checks, 2)
        self.assertEqual(fake.tag_sha, SHA)
        self.assertFalse(fake.deleted)

    def test_absent_branch_requires_exact_archived_original_sha(self):
        fake = FakeClient()
        fake.absent = True
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
                         "blocked_absent_without_archive")
        fake.tag_sha = "f" * 40
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
                         "blocked_absent_without_archive")
        fake.tag_sha = SHA
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40), "already_absent")

    def test_incomplete_open_pr_listing_is_not_assumed_empty(self):
        fake = FakeClient()
        fake.open = [{"number": n} for n in range(100)]
        self.assertEqual(retire_one(fake, REPO, item(), expected_main_sha="c" * 40),
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

    def test_disabled_retirement_fails_visibly_without_write_permission(self):
        workflow = Path(".github/workflows/retire-verified-branches.yml").read_text(
            encoding="utf-8")
        # A deliberate retire dispatch must not show a benign all-jobs-skipped
        # result. The only runnable retire-mode job must fail explicitly.
        guard = workflow.split("  retirement-blocked:", 1)[1].split(
            "\n  retire:", 1)[0]
        self.assertIn("inputs.mode == 'retire'", guard)
        self.assertIn("contents: read", guard)
        self.assertNotIn("contents: write", guard)
        self.assertIn("exit 1", guard)
        self.assertIn("::error::Branch retirement is disabled", guard)
        privileged = workflow.split("\n  retire:", 1)[1]
        self.assertIn("if: ${{ false &&", privileged)
        self.assertNotIn("\n  push:", workflow)

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

    def test_rest_client_rejects_bearer_redirects_without_network(self):
        # Python's default HTTPRedirectHandler copies normal Authorization
        # headers when Location changes the host. Only the initial verified
        # api.github.com request may receive our test bearer token.
        from urllib.error import HTTPError
        client = GitHubClient(REPO, "OFFLINE_FIXTURE_TOKEN")
        endpoint = f"/repos/{REPO}/branches/main"
        for location in ("https://other.invalid/collect-token",
                         "https://api.github.com/renamed/repository"):
            with self.subTest(location=location):
                response = HTTPError(
                    "https://api.github.com" + endpoint, 302, "Found",
                    {"Location": location}, None,
                )
                with patch("scripts.retire_merged_branches.build_opener") as maker:
                    maker.return_value.open.side_effect = response
                    with self.assertRaisesRegex(CleanupError, "HTTP 302"):
                        client.get(endpoint)
                    self.assertEqual(maker.call_count, 1)
                    handler = maker.call_args.args[0]
                    request = maker.return_value.open.call_args.args[0]
                    self.assertEqual(
                        request.full_url, "https://api.github.com" + endpoint
                    )
                    self.assertNotIn("Authorization", request.headers)
                    self.assertEqual(
                        request.unredirected_hdrs["Authorization"],
                        "Bearer OFFLINE_FIXTURE_TOKEN"
                    )
                    # A real opener invokes this method for HTTP redirects:
                    # returning None forces HTTPError, not a follow-up call.
                    self.assertIsNone(handler.redirect_request(
                        request, None, 302, "Found",
                        {"Location": location}, location
                    ))
                    self.assertEqual(maker.return_value.open.call_count, 1)

    def test_repo_dot_segments_are_rejected_before_any_api_or_git_use(self):
        # A broad owner/repo regex previously accepted '../name' and 'owner/..'.
        # These must never enter an authenticated GitHub API path or Git URL.
        for invalid in ("../name", "owner/..", "./name", "owner/.",
                        "/name", "owner/", "owner/../other", None):
            with self.subTest(repository=invalid):
                sample = plan()
                sample["repository"] = invalid
                with self.assertRaisesRegex(CleanupError, "invalid repository"):
                    validate_plan(sample)
                with self.assertRaisesRegex(CleanupError, "invalid repository"):
                    GitHubClient(invalid, "offline-only-fixture-token")

    def test_destructive_mode_requires_live_immutable_archive_ruleset(self):
        for key, value in (
            ("archive_rules_installed", False),
            ("archive_rules_enforcement", "evaluate"),
            ("archive_rules_bypass", [{"actor_id": 1, "actor_type": "RepositoryRole",
                                       "bypass_mode": "always"}]),
            ("archive_rules_scope", "refs/tags/branch-archive/*"),
            ("archive_rules_types", ["update"]),
            ("archive_rules_types", ["deletion"]),
        ):
            fake = FakeClient()
            setattr(fake, key, value)
            with self.subTest(missing_or_weakened=key), self.assertRaisesRegex(
                    CleanupError, "archive-tag ruleset"):
                execute(plan(), fake)
            self.assertFalse(fake.posts)
            self.assertFalse(fake.deleted)

    def test_direct_retire_one_cannot_bypass_live_archive_policy(self):
        fake = FakeClient()
        fake.archive_rules_installed = False
        with self.assertRaisesRegex(CleanupError, "archive-tag ruleset"):
            retire_one(fake, REPO, item(), expected_main_sha="c" * 40)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_archive_rules_changed_after_tag_creation_block_git_lease(self):
        fake = FakeClient()
        # One session-wide check, one prior to tag creation, then a final
        # verification after successful archive publication.
        fake.archive_rules_weaken_after = 3
        result = execute(plan(), fake)
        self.assertEqual(result[0]["status"], "error_CleanupError")
        self.assertEqual(fake.tag_sha, SHA)
        self.assertEqual(len(fake.posts), 1)
        self.assertFalse(fake.deleted)

    def test_read_only_inventory_is_available_without_installed_tag_rules(self):
        fake = FakeClient()
        fake.archive_rules_installed = False
        result = execute(plan(), fake, audit_only=True)
        self.assertEqual(result[0]["status"], "eligible_read_only")
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_stale_approved_main_aborts_before_tags_or_retirement(self):
        fake = FakeClient()
        fake.main_sha = "f" * 40
        with self.assertRaisesRegex(CleanupError, "approved main SHA moved"):
            execute(plan(), fake)
        self.assertEqual(fake.main_reads, 1)
        self.assertEqual(fake.ref_checks, 0)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_read_only_audit_also_refuses_stale_plan_main(self):
        fake = FakeClient()
        fake.main_sha = "f" * 40
        with self.assertRaisesRegex(CleanupError, "approved main SHA moved"):
            execute(plan(), fake, audit_only=True)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_main_moved_after_initial_preflight_blocks_archive(self):
        fake = FakeClient()
        fake.main_change_on_read = 2
        result = execute(plan(), fake)
        self.assertEqual(result[0]["status"], "blocked_main_moved")
        self.assertEqual(fake.main_reads, 2)
        self.assertFalse(fake.posts)
        self.assertFalse(fake.deleted)

    def test_main_moved_after_archive_blocks_final_leased_delete(self):
        fake = FakeClient()
        fake.main_change_on_read = 3
        result = execute(plan(), fake)
        self.assertEqual(result[0]["status"], "blocked_main_moved_before_delete")
        self.assertGreaterEqual(fake.main_reads, 3)
        self.assertEqual(fake.tag_sha, SHA)
        self.assertEqual(len(fake.posts), 1)
        self.assertFalse(fake.deleted)

    def test_privileged_plan_loader_rejects_duplicate_keys_and_nonstandard_numbers(self):
        baseline = json.dumps(plan())
        invalid = (
            baseline.replace('"schema_version": ', '"schema_version": "1.0", "schema_version": ', 1),
            baseline.replace('"merged_pr": 123', '"merged_pr": NaN', 1),
            baseline.replace('"merged_pr": 123', '"merged_pr": Infinity', 1),
            baseline.replace('"merged_pr": 123', '"merged_pr": 1.0', 1),
            baseline.replace('"merged_pr": 123', '"merged_pr": 999999999999999999999', 1),
            baseline.replace('"repository": ', '"PRIVATE_SECRET_MARKER": 1, "repository": ', 1),
        )
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "PRIVATE_PLAN_FILENAME_MARKER.json"
            for raw in invalid:
                with self.subTest(raw=raw[:36]):
                    source.write_text(raw, encoding="utf-8")
                    stderr = io.StringIO()
                    with patch("scripts.retire_merged_branches.GitHubClient") as client:
                        with redirect_stderr(stderr):
                            self.assertEqual(main(["--plan", str(source), "--audit-live"]), 2)
                    client.assert_not_called()
                    self.assertNotIn("PRIVATE_PLAN_FILENAME_MARKER", stderr.getvalue())
                    self.assertNotIn("PRIVATE_SECRET_MARKER", stderr.getvalue())

    def test_privileged_plan_loader_rejects_symlinks_nonregular_and_grown_files(self):
        with tempfile.TemporaryDirectory() as folder:
            parent = Path(folder)
            valid = parent / "safe-plan.json"
            valid.write_text(json.dumps(plan()), encoding="utf-8")
            symlink = parent / "PRIVATE_SYMLINK_MARKER.json"
            symlink.symlink_to(valid)
            oversized = parent / "oversized.json"
            oversized.write_text(" " * 35001, encoding="utf-8")
            for source in (symlink, parent, oversized):
                with self.subTest(kind=source.name):
                    stderr = io.StringIO()
                    with patch("scripts.retire_merged_branches.GitHubClient") as client:
                        with redirect_stderr(stderr):
                            self.assertEqual(main(["--plan", str(source), "--audit-live"]), 2)
                    client.assert_not_called()
                    self.assertNotIn("PRIVATE_SYMLINK_MARKER", stderr.getvalue())
            with patch("scripts.retire_merged_branches.GitHubClient") as client:
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(main(["--plan", str(valid)]), 0)
            client.assert_not_called()

    def test_repo_mismatch_stops_before_actions(self):
        fake = FakeClient()
        fake.repository = "another/repository"
        with self.assertRaisesRegex(CleanupError, "disagrees"):
            execute(plan(), fake)
        self.assertFalse(fake.deleted)

if __name__ == "__main__":
    unittest.main()
