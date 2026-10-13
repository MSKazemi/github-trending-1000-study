"""Offline negative tests for fail-closed, non-loss branch retirement."""
import copy
import unittest

from scripts.retire_merged_branches import (
    ARCHIVE_PREFIX, ApiNotFound, CleanupError, execute,
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

    def get(self, path):
        if path == f"/repos/{REPO}":
            return {"default_branch": "main"}
        if "/git/ref/tags/" in path:
            if self.tag_sha is None:
                raise ApiNotFound("not found")
            return {"object": {"sha": self.tag_sha}}
        if "/git/ref/heads/" in path:
            self.ref_checks += 1
            if self.race_on_second_ref and self.ref_checks == 2:
                return {"object": {"sha": "f" * 40}}
            return {"object": {"sha": self.sha}}
        if "/branches/" in path:
            return {"protected": self.protected, "commit": {"sha": self.sha}}
        if "/pulls/123" in path:
            return {"merged": self.pr_merged,
                    "state": "closed", "head": {"ref": NAME, "sha": self.pr_head,
                                                   "repo": {"full_name": REPO}},
                    "base": {"ref": "main"}, "merge_commit_sha": MERGE}
        if "/pulls?" in path:
            return self.open
        raise AssertionError("unexpected GET: " + path)

    def post(self, path, payload):
        self.posts.append((path, payload))
        self.tag_sha = payload["sha"]
        return {"ref": payload["ref"], "object": {"sha": self.tag_sha}}

    def delete(self, path):
        self.deleted.append(path)
        if self.tag_sha != SHA:
            raise AssertionError("deleted without verified recovery tag")
        return None

class BranchCleanupTests(unittest.TestCase):
    def test_approved_single_branch_backed_up_before_deletion(self):
        fake = FakeClient()
        result = execute(plan(), fake)
        self.assertEqual(result[0]["status"], "retired_with_archive_tag")
        self.assertEqual(len(fake.posts), 1)
        self.assertEqual(len(fake.deleted), 1)
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
