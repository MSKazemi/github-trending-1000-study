"""Offline structural regression for a dated, non-executable branch inventory.

Passing does not prove current GitHub state, independent review, or preservation
of all research evidence. No network access or repository mutation is allowed.
"""
import json
from collections import Counter
from datetime import date
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "ops/branch-retirement/review-only-2026-10-14.json"
SHA = re.compile(r"[0-9a-f]{40}\Z")
REF = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}\Z")
STATUSES = {"default", "open_pr", "merged_unchanged", "merged_changed",
            "closed_unmerged"}


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


class BranchReconciliationSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(
            SNAPSHOT.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=lambda c: (_ for _ in ()).throw(ValueError(c)),
        )

    def test_snapshot_is_not_a_destructive_execution_manifest(self):
        data = self.data
        self.assertEqual(data["schema"], "review-only/v1")
        self.assertIs(data["do_not_execute"], True)
        self.assertEqual(data["repository"], "MSKazemi/github-trending-1000-study")
        self.assertRegex(data["source_main_sha"], SHA)
        date.fromisoformat(data["captured_day_utc"])
        self.assertNotIn("branches", data)
        self.assertNotIn("archive_prefix", data)
        self.assertNotIn("approval", data)

    def test_classification_counts_and_main_are_internally_consistent(self):
        data = self.data
        records = data["records"]
        self.assertTrue(records)
        self.assertEqual(set(data["classification_counts"]), STATUSES)
        actual = Counter(row["status"] for row in records)
        self.assertEqual(dict(actual), data["classification_counts"])
        self.assertEqual(sum(actual.values()), len(records))
        self.assertEqual(actual["default"], 1)
        self.assertEqual(actual["open_pr"], data["open_prs"])
        main = [row for row in records if row["status"] == "default"]
        self.assertEqual(main[0]["branch"], "main")
        self.assertEqual(main[0]["sha"], data["source_main_sha"])

    def test_provenance_and_branch_tips_are_unambiguous(self):
        records = self.data["records"]
        self.assertEqual(len(records), len({r["branch"] for r in records}))
        for row in records:
            with self.subTest(branch=row["branch"]):
                self.assertEqual(
                    set(row),
                    {"branch", "sha", "status", "pr", "pr_head_sha",
                     "merge_commit_sha", "protected"},
                )
                self.assertRegex(row["branch"], REF)
                self.assertNotIn("..", row["branch"])
                self.assertNotIn("//", row["branch"])
                self.assertRegex(row["sha"], SHA)
                self.assertIn(row["status"], STATUSES)
                self.assertIs(type(row["protected"]), bool)
                if row["status"] == "default":
                    self.assertIsNone(row["pr"])
                    self.assertIsNone(row["pr_head_sha"])
                    self.assertIsNone(row["merge_commit_sha"])
                    continue
                self.assertIs(type(row["pr"]), int)
                self.assertGreater(row["pr"], 0)
                self.assertRegex(row["pr_head_sha"], SHA)
                if row["status"] in ("open_pr", "closed_unmerged"):
                    self.assertIsNone(row["merge_commit_sha"])
                    self.assertEqual(row["sha"], row["pr_head_sha"])
                else:
                    self.assertRegex(row["merge_commit_sha"], SHA)
                    self.assertEqual(row["status"] == "merged_unchanged",
                                     row["sha"] == row["pr_head_sha"])


if __name__ == "__main__":
    unittest.main()
