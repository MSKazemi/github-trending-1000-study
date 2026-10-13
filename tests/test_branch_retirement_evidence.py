"""Offline consistency checks for historical no-loss branch retirement provenance.

This tests only internally reported Git identifiers, not live GitHub state,
scientific findings, source permissions or archive tag immutability.
"""
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "research-notes/branch-retirement-2026-10-13.json"
PLAN = ROOT / "ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json"
SHA = re.compile(r"[a-f0-9]{40}\Z")


class BranchRetirementEvidenceTests(unittest.TestCase):
    def test_snapshot_matches_canonical_allowlist_and_archive_prefix(self):
        with SNAPSHOT.open(encoding="utf-8") as stream:
            historical = json.load(stream)
        with PLAN.open(encoding="utf-8") as stream:
            allowlist = json.load(stream)

        self.assertEqual(historical["repository"], allowlist["repository"])
        self.assertEqual(historical["snapshot_main_sha"],
                         allowlist["source_main_sha"])
        self.assertEqual(historical["archive_tag_prefix"],
                         allowlist["archive_prefix"])
        self.assertEqual(historical["candidate_count"],
                         len(historical["candidates"]))
        self.assertEqual(historical["held_count"], len(historical["held"]))
        self.assertEqual(historical["total_branches"],
                         len(historical["candidates"]) + len(historical["held"]))

        candidates = {item["branch"]: item for item in historical["candidates"]}
        held = {item["branch"]: item for item in historical["held"]}
        planned = {item["branch"]: item for item in allowlist["branches"]}
        self.assertEqual(len(candidates), len(historical["candidates"]))
        self.assertEqual(len(held), len(historical["held"]))
        self.assertTrue(set(candidates).isdisjoint(held))
        self.assertEqual(set(candidates), set(planned))

        for branch, item in candidates.items():
            with self.subTest(branch=branch):
                self.assertEqual(item["sha"], planned[branch]["expected_sha"])
                self.assertEqual(item["merged_pr"], planned[branch]["merged_pr"])
                self.assertEqual(item["merge_commit_sha"],
                                 planned[branch]["merge_commit_sha"])
                self.assertRegex(item["sha"], SHA)

        for branch, item in held.items():
            with self.subTest(branch=branch):
                self.assertRegex(item["sha"], SHA)
                self.assertTrue(item.get("reason"))

if __name__ == "__main__":
    unittest.main()
