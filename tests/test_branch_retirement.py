"""Offline-only adversarial checks for safe branch retirement.

No real GitHub API is called and no branches or archive tags are created.
"""
import copy
import unittest

from scripts.retire_merged_branches import (
    CONFIRM, RetirementError, archive_batches, audit_live, check_manifest, retire,
)

MAIN = "a" * 40
BRANCH = "b" * 40
MERGE = "c" * 40
TREE = "d" * 40
ANCHOR = "e" * 40


def fixture():
    return {
        "schema_version": "1.0",
        "repository": "MSKazemi/github-trending-1000-study",
        "default_branch": "main",
        "archive_tag_prefix": "archive/branch-retirement-2026-10-13",
        "batch_size": 20,
        "candidate_count": 1,
        "candidates": [{
            "branch": "fix/merged-improvement", "sha": BRANCH,
            "merged_pr": 100, "merge_commit_sha": MERGE,
        }],
    }


class FakeGitHub:
    def __init__(self):
        self.calls = []
        self.refs = {
            "/git/ref/heads/main": {"object": {"sha": MAIN}},
            "/git/ref/heads/fix/merged-improvement": {"object": {"sha": BRANCH}},
        }
        self.protected = False
        self.open_heads = []
        self.merged = True
        self.ancestor = True
        self.tags = {}
        self.archive_commit = None

    def get(self, path, *, optional=False):
        self.calls.append(("GET", path))
        if path.startswith("/git/ref/"):
            value = self.refs.get(path)
            if value is None and not optional:
                raise RetirementError("missing ref")
            return value
        if path.startswith("/pulls?"):
            return [{"head": {"repo": {"full_name": "MSKazemi/github-trending-1000-study"},
                              "ref": name}} for name in self.open_heads]
        if path == "/pulls/100":
            return {
                "state": "closed" if self.merged else "open",
                "merged_at": "2026-10-13T10:00:00Z" if self.merged else None,
                "merge_commit_sha": MERGE,
                "head": {"ref": "fix/merged-improvement", "sha": BRANCH,
                         "repo": {"full_name": "MSKazemi/github-trending-1000-study"}},
                "base": {"ref": "main"},
            }
        if path == "/branches/fix/merged-improvement":
            return {"protected": self.protected}
        if path.startswith("/compare/"):
            return {"status": "ahead" if self.ancestor else "diverged",
                    "behind_by": 0 if self.ancestor else 1}
        if path == "/git/commits/" + MAIN:
            return {"tree": {"sha": TREE}}
        if path == "/git/commits/" + ANCHOR:
            return self.archive_commit
        if path.startswith("/git/ref/tags/"):
            return self.tags.get(path)
        raise AssertionError("unexpected GitHub GET " + path)

    def post(self, path, payload):
        self.calls.append(("POST", path))
        if path == "/git/commits":
            self.archive_commit = {
                "tree": {"sha": payload["tree"]},
                "parents": [{"sha": sha} for sha in payload["parents"]],
            }
            return {"sha": ANCHOR}
        if path == "/git/refs":
            self.tags["/git/ref/tags/" + payload["ref"].removeprefix("refs/tags/")] = {
                "object": {"sha": payload["sha"]}
            }
            return self.tags["/git/ref/tags/" + payload["ref"].removeprefix("refs/tags/")]
        raise AssertionError("unexpected GitHub POST " + path)

    def delete(self, path):
        self.calls.append(("DELETE", path))
        if path != "/git/ref/heads/fix/merged-improvement":
            raise AssertionError("unsafe deleted ref")
        del self.refs[path]


class BranchRetirementTests(unittest.TestCase):
    def test_bounded_manifest_cannot_include_main_or_duplicate_refs(self):
        for bad in ("main", "master", "../escape", "feature//bad",
                    "refs/heads/forged", "archive/protected"):
            data = fixture()
            data["candidates"][0]["branch"] = bad
            with self.subTest(bad=bad), self.assertRaises(RetirementError):
                check_manifest(data)
        data = fixture()
        data["candidates"].append(copy.deepcopy(data["candidates"][0]))
        data["candidate_count"] = 2
        with self.assertRaisesRegex(RetirementError, "duplicate"):
            check_manifest(data)

    def test_malformed_head_and_repository_are_rejected(self):
        for key, value in (("sha", "deadbeef"), ("merged_pr", True),
                           ("merge_commit_sha", "z" * 40)):
            data = fixture()
            data["candidates"][0][key] = value
            with self.subTest(key=key), self.assertRaises(RetirementError):
                check_manifest(data)
        data = fixture()
        data["repository"] = "another-owner/another-repo"
        with self.assertRaisesRegex(RetirementError, "repository"):
            check_manifest(data)

    def test_audit_only_reads_and_requires_merged_ancestry(self):
        api = FakeGitHub()
        main, rows = audit_live(api, fixture())
        self.assertEqual(main, MAIN)
        self.assertEqual(len(rows), 1)
        self.assertTrue(all(method == "GET" for method, _ in api.calls))

    def test_branch_movement_or_protection_blocks_all_writes(self):
        for condition in ("moved", "protected", "open", "not_merged", "not_ancestor"):
            with self.subTest(condition=condition):
                api = FakeGitHub()
                if condition == "moved":
                    api.refs["/git/ref/heads/fix/merged-improvement"] = {
                        "object": {"sha": "f" * 40}}
                elif condition == "protected":
                    api.protected = True
                elif condition == "open":
                    api.open_heads = ["fix/merged-improvement"]
                elif condition == "not_merged":
                    api.merged = False
                else:
                    api.ancestor = False
                with self.assertRaises(RetirementError):
                    retire(api, fixture(), CONFIRM)
                self.assertFalse(any(method in ("POST", "DELETE") for method, _ in api.calls))

    def test_wrong_confirmation_has_no_side_effect(self):
        api = FakeGitHub()
        with self.assertRaisesRegex(RetirementError, "confirmation"):
            retire(api, fixture(), "YES")
        self.assertEqual(api.calls, [])

    def test_archive_tag_verified_before_branch_is_deleted(self):
        api = FakeGitHub()
        result = retire(api, fixture(), CONFIRM)
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["main_sha"], MAIN)
        self.assertEqual(api.archive_commit["tree"]["sha"], TREE)
        self.assertEqual([x["sha"] for x in api.archive_commit["parents"]],
                         [MAIN, BRANCH])
        self.assertEqual(len(result["archive_tags"]), 1)
        delete_index = next(i for i, x in enumerate(api.calls) if x[0] == "DELETE")
        self.assertIn(("GET", "/git/commits/" + ANCHOR), api.calls[:delete_index])
        self.assertNotIn("/git/ref/heads/fix/merged-improvement", api.refs)

    def test_archive_tag_mismatch_stops_all_deletion(self):
        api = FakeGitHub()
        tag = "archive/branch-retirement-2026-10-13-part-01"
        api.tags["/git/ref/tags/" + tag] = {"object": {"sha": ANCHOR}}
        api.archive_commit = {
            "tree": {"sha": TREE}, "parents": [{"sha": MAIN}, {"sha": "f" * 40}],
        }
        with self.assertRaisesRegex(RetirementError, "wrong tree/parents"):
            retire(api, fixture(), CONFIRM)
        self.assertFalse(any(method == "DELETE" for method, _ in api.calls))

    def test_archive_groups_cover_each_branch_once(self):
        rows = [{"branch": f"feature/{i}", "sha": f"{i:040x}"}
                for i in range(60)]
        groups = archive_batches(rows, MAIN, "archive/dated", 20)
        self.assertEqual([len(g["branches"]) for g in groups], [20, 20, 20])
        self.assertEqual([g["parents"][0] for g in groups], [MAIN] * 3)
        self.assertEqual(sum(len(g["branches"]) for g in groups), 60)
        self.assertEqual(len(set(g["tag"] for g in groups)), 3)

    def test_original_manifest_is_not_mutated(self):
        data = fixture()
        before = copy.deepcopy(data)
        retire(FakeGitHub(), data, CONFIRM)
        self.assertEqual(data, before)


if __name__ == "__main__":
    unittest.main()
