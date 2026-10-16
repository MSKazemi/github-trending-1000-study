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
            if "/branches/old" in path:
                return {"name": "old", "commit": {"sha": b}, "protected": False}
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


    def test_unchanged_tip_is_rechecked_and_remains_advisory_candidate(self):
        a, b = "a" * 40, "b" * 40
        detail_requests = []
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                return []
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            if "/branches/old" in path:
                detail_requests.append(path)
                return {"name": "old", "commit": {"sha": b}, "protected": False}
            if "/compare/" in path:
                return {"status": "behind", "ahead_by": 0, "behind_by": 9}
            self.fail(path)
        result = audit("o/r", get=fetch)
        self.assertEqual(detail_requests, ["/repos/o/r/branches/old"])
        self.assertEqual(result["branches"][1]["decision"], "manual-prune-candidate")
        self.assertEqual(result["branches"][1]["sha"], b)
        self.assertTrue(result["read_only"])

    def test_moved_or_newly_protected_tip_is_never_prune_candidate(self):
        a, b, c = "a" * 40, "b" * 40, "c" * 40
        for live_sha, protected in ((c, False), (b, True), (c, True)):
            with self.subTest(live_sha=live_sha, protected=protected):
                def fetch(path):
                    if "/branches?per_page" in path:
                        return [{"name": "main", "commit": {"sha": a}, "protected": False},
                                {"name": "old", "commit": {"sha": b}, "protected": False}]
                    if "/pulls?state" in path:
                        return []
                    if "/branches/main" in path:
                        return {"commit": {"sha": a}}
                    if "/branches/old" in path:
                        return {"name": "old", "commit": {"sha": live_sha},
                                "protected": protected}
                    if "/compare/" in path:
                        return {"status": "behind", "ahead_by": 0, "behind_by": 9}
                    self.fail(path)
                result = audit("o/r", get=fetch)
                self.assertEqual(result["branches"][1]["decision"],
                                 "hold-ref-or-protection-moved-rerun")
                # Never rewrite the original SHA to match a moved branch.
                self.assertEqual(result["branches"][1]["sha"], b)

    def test_new_open_pr_during_audit_blocks_candidate(self):
        a, b = "a" * 40, "b" * 40
        reads = [0]
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "old", "commit": {"sha": b}, "protected": False}]
            if "/pulls?state" in path:
                reads[0] += 1
                if reads[0] == 1:
                    return []
                return [{"number": 10, "head": {"ref": "old",
                                               "repo": {"full_name": "o/r"}}}]
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            if "/branches/old" in path:
                return {"name": "old", "commit": {"sha": b}, "protected": False}
            if "/compare/" in path:
                return {"status": "behind", "ahead_by": 0, "behind_by": 9}
            self.fail(path)
        report = audit("o/r", get=fetch)
        self.assertEqual(reads[0], 2)
        self.assertEqual(report["branches"][1]["decision"],
                         "hold-open-pr-inventory-moved-rerun")

    def test_missing_or_malformed_tip_recheck_fails_closed(self):
        a, b = "a" * 40, "b" * 40
        for detail in (None, {}, {"name": "old", "commit": {"sha": "wrong"},
                                   "protected": False}):
            with self.subTest(detail=detail):
                def fetch(path):
                    if "/branches?per_page" in path:
                        return [{"name": "main", "commit": {"sha": a}, "protected": False},
                                {"name": "old", "commit": {"sha": b}, "protected": False}]
                    if "/pulls?state" in path:
                        return []
                    if "/branches/main" in path:
                        return {"commit": {"sha": a}}
                    if "/branches/old" in path:
                        return detail
                    if "/compare/" in path:
                        return {"status": "behind", "ahead_by": 0, "behind_by": 9}
                    self.fail(path)
                with self.assertRaisesRegex(ValueError, "Cannot safely recheck"):
                    audit("o/r", get=fetch)

    def test_untrusted_branch_name_cannot_inject_query_into_detail_request(self):
        a, b = "a" * 40, "b" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False},
                        {"name": "bad?per_page=1", "commit": {"sha": b},
                         "protected": False}]
            if "/pulls?state" in path:
                return []
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            if "/compare/" in path:
                return {"status": "behind", "ahead_by": 0, "behind_by": 9}
            self.fail("untrusted branch was sent in a network request: " + path)
        with self.assertRaisesRegex(ValueError, "Unsafe Git branch name"):
            audit("o/r", get=fetch)

    def test_duplicate_pr_numbers_are_rejected_not_silently_merged(self):
        a = "a" * 40
        def fetch(path):
            if "/branches?per_page" in path:
                return [{"name": "main", "commit": {"sha": a}, "protected": False}]
            if "/pulls?state" in path:
                return [{"number": 10, "head": {"ref": "a",
                         "repo": {"full_name": "o/r"}}},
                        {"number": 10, "head": {"ref": "b",
                         "repo": {"full_name": "o/r"}}}]
            if "/branches/main" in path:
                return {"commit": {"sha": a}}
            self.fail(path)
        with self.assertRaisesRegex(ValueError, "Duplicate open PR"):
            audit("o/r", get=fetch)


if __name__ == "__main__":
    unittest.main()
