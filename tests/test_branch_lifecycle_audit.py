"""Offline regression tests for read-only branch audit."""
import unittest
from scripts.branch_lifecycle_audit import audit, classify, pages

class BranchAuditTest(unittest.TestCase):
    def test_classification(self):
        self.assertEqual(classify("main", "main", False, [], 0), "keep-base")
        self.assertEqual(classify("main", "x", True, [], 0), "keep-protected")
        self.assertEqual(classify("main", "x", False, [3], 0), "keep-open-pr")
        self.assertEqual(classify("main", "x", False, [], 2), "hold-unique-history")
        self.assertEqual(classify("main", "x", False, [], 0), "manual-prune-candidate")

    def test_bad_pagination_fails_closed(self):
        with self.assertRaises(RuntimeError):
            pages("/repos/o/r/branches", lambda path: {"message": "bad"})
        with self.assertRaises(RuntimeError):
            pages("/repos/o/r/branches", lambda path: [{}] * 100, max_pages=1)

    def test_pinned_sha_and_base_movement(self):
        a, b, c = "a" * 40, "b" * 40, "c" * 40
        calls = [0]
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return []
            if "/branches/main" in path:
                calls[0] += 1
                return {"commit": {"sha": a if calls[0] == 1 else c}}
            if "/compare/" in path:
                self.assertIn(a + "..." + b, path)
                return {"status": "behind", "ahead_by": 0, "behind_by": 11}
            raise AssertionError(path)
        report = audit("o/r", get=fetch)
        self.assertTrue(report["read_only"])
        self.assertEqual(report["branches"][1]["decision"], "hold-base-moved-rerun")

    def test_malicious_base_ref_rejected_before_any_network(self):
        def fail_fetch(path):
            self.fail("network must not be called for invalid base")

        for ref in ("../issues", "refs/heads/main", "a//b", "a..b",
                    "main?per_page=1", "main#frag", "", "a/./b"):
            with self.subTest(ref=ref), self.assertRaisesRegex(ValueError, "Invalid base"):
                audit("o/r", base=ref, get=fail_fetch)

    def test_inconsistent_comparison_fails_closed(self):
        a, b = "a" * 40, "b" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return []
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            return {"status": "ahead", "ahead_by": 0, "behind_by": 0}
        with self.assertRaises(ValueError):
            audit("o/r", get=fetch)

    def test_base_sha_changed_during_paginated_inventory_fails_before_compare(self):
        a, b, c = "a" * 40, "b" * 40, "c" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return []
            if "/branches/main" in path:
                return {"commit": {"sha": c}}
            self.fail("moved base must fail before any branch comparison")
        with self.assertRaisesRegex(ValueError, "Base SHA moved"):
            audit("o/r", get=fetch)

    def test_unknown_open_pr_head_owner_cannot_be_silently_ignored(self):
        a, b = "a" * 40, "b" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return [{"number": 7, "head": {"ref": "old", "repo": None}}]
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            self.fail("unknown owner must fail before comparisons")
        with self.assertRaisesRegex(ValueError, "Unverifiable open PR head repository"):
            audit("o/r", get=fetch)

    def test_inconsistent_comparison_status_with_zero_divergence_rejected(self):
        a, b = "a" * 40, "b" * 40
        for status, ahead, behind in (("behind", 0, 0),
                                      ("ahead", 1, 1),
                                      ("diverged", 1, 0),
                                      ("identical", 0, 2)):
            def fetch(path):
                if "/branches?per_page" in path:
                    return [{"name": "main", "commit": {"sha": a}, "protected": False},
                            {"name": "old", "commit": {"sha": b}, "protected": False}]
                if "/pulls?state" in path:
                    return []
                if "/branches/main" in path:
                    return {"commit": {"sha": a}}
                return {"status": status, "ahead_by": ahead, "behind_by": behind}
            with self.subTest(status=status), self.assertRaisesRegex(
                    ValueError, "Inconsistent comparison"):
                audit("o/r", get=fetch)

    def test_known_open_pr_same_repository_is_never_prune_candidate(self):
        a, b = "a" * 40, "b" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return [{"number": 9, "head": {
                    "ref": "old", "repo": {"full_name": "o/r"}}}]
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            return {"status": "behind", "ahead_by": 0, "behind_by": 11}
        report = audit("o/r", get=fetch)
        self.assertEqual(report["branches"][1]["decision"], "keep-open-pr")
        self.assertEqual(report["branches"][1]["open_prs"], [9])


if __name__ == "__main__":
    unittest.main()
