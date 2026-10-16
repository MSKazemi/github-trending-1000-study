"""Regression checks for uninstalled proposed branch/tag rulesets.

These checks protect reviewed JSON intent, not actual GitHub enforcement,
administrative permissions, or a qualified human security signoff.
"""
import json
from pathlib import Path
import re
import unittest

from trending_study.data_integrity import decode_research_json


ROOT = Path(__file__).resolve().parents[1]
OPS = ROOT / "ops" / "rulesets"
RUNBOOK = ROOT / "docs" / "ISSUE_248_RULESET_ADMIN_REVIEW.md"
REQUIRED_CHECKS = {
    "test (3.10)", "test (3.12)", "test (3.13)", "test (3.14)",
    "research-artifacts",
}


class ProposedRulesetTests(unittest.TestCase):
    @staticmethod
    def get_ruleset(name):
        # A ruleset with duplicate JSON keys has ambiguous security
        # semantics; never let last-key-wins parsing mask a weak override.
        return decode_research_json((OPS / name).read_bytes(), name)

    def test_main_rejects_unreviewed_or_stale_changes(self):
        ruleset = self.get_ruleset("main.json")
        self.assertEqual(ruleset["target"], "branch")
        self.assertEqual(ruleset["enforcement"], "active")
        self.assertEqual(ruleset["bypass_actors"], [])
        self.assertEqual(ruleset["conditions"]["ref_name"],
                         {"include": ["refs/heads/main"], "exclude": []})
        entries = {rule["type"]: rule for rule in ruleset["rules"]}
        self.assertEqual(len(entries), len(ruleset["rules"]),
                         "duplicate main security rule types forbidden")
        self.assertEqual(set(entries), {
            "deletion", "non_fast_forward", "pull_request",
            "required_status_checks",
        })
        pr = entries["pull_request"]["parameters"]
        self.assertEqual(pr["required_approving_review_count"], 1)
        self.assertIs(pr["dismiss_stale_reviews_on_push"], True)
        self.assertIs(pr["require_last_push_approval"], True)
        self.assertIs(pr["required_review_thread_resolution"], True)
        self.assertEqual(set(pr["allowed_merge_methods"]),
                         {"merge", "squash", "rebase"})
        checks = entries["required_status_checks"]["parameters"]
        self.assertIs(checks["strict_required_status_checks_policy"], True)
        self.assertIs(checks["do_not_enforce_on_create"], False)
        self.assertEqual(
            {entry["context"] for entry in checks["required_status_checks"]},
            REQUIRED_CHECKS,
        )
        self.assertEqual(len(checks["required_status_checks"]), len(REQUIRED_CHECKS))
        self.assertTrue(all(entry["integration_id"] == 15368
                            for entry in checks["required_status_checks"]))

    def test_archive_ref_updates_and_deletion_are_blocked(self):
        ruleset = self.get_ruleset("branch-archive-tags.json")
        self.assertEqual(ruleset["target"], "tag")
        self.assertEqual(ruleset["enforcement"], "active")
        self.assertEqual(ruleset["bypass_actors"], [])
        self.assertEqual(ruleset["conditions"]["ref_name"],
                         {"include": ["refs/tags/branch-archive/**/*"],
                          "exclude": []})
        entries = {rule["type"]: rule for rule in ruleset["rules"]}
        self.assertEqual(len(entries), len(ruleset["rules"]),
                         "duplicate archive security rule types forbidden")
        self.assertEqual(set(entries), {"update", "deletion"})
        self.assertIs(entries["update"]["parameters"]["update_allows_fetch_and_merge"],
                      False)

    def test_duplicate_security_json_keys_cannot_be_silently_overridden(self):
        # Exercise the same fail-closed decoder used by the ruleset fixture
        # loader. This is a lexical integrity test, not GitHub enforcement.
        for content in (
            b'{"enforcement":"disabled","enforcement":"active"}',
            b'{"bypass_actors":["admin"],"bypass_actors":[]}',
            b'{"rules":[{"type":"deletion","type":"pull_request"}]}',
        ):
            with self.subTest(content=content), self.assertRaises(ValueError):
                decode_research_json(content, "synthetic-ruleset.json")

    def test_admin_runbook_fails_closed_on_main_movement(self):
        text = RUNBOOK.read_text(encoding="utf-8")
        bash_blocks = re.findall(r"```bash\n(.*?)\n```", text, flags=re.S)
        self.assertGreaterEqual(len(bash_blocks), 3)
        shell = "\n".join(bash_blocks)
        # Historical SHA may remain as dated prose, never as an executable pin.
        self.assertNotIn("9dc35ea8784c909dcc397dee1dcfc1278793abcb", shell)
        self.assertIn("RULESET_EXPECTED_MAIN_SHA", shell)
        self.assertIn("rulesets-before-apply.json-stream", shell)
        self.assertIn("rulesets-after-archive.json-stream", shell)
        self.assertIn("archive-created.json", shell)
        self.assertIn("main-created.json", shell)
        self.assertIn('test "$actual_main_sha" = "$RULESET_EXPECTED_MAIN_SHA"', shell)


if __name__ == "__main__":
    unittest.main()
