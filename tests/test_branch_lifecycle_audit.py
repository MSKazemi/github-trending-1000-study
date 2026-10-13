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

if __name__ == "__main__":
    unittest.main()
