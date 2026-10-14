"""Offline regression: branch retirement must never run on push/PR/schedule."""
from pathlib import Path
import re
import unittest


WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github" / "workflows" / "retire-verified-branches.yml"
)


class RetirementWorkflowTriggerTests(unittest.TestCase):
    def test_retirement_is_manual_dispatch_only(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        match = re.search(r"(?m)^on:[ \t]*\n", text)
        self.assertIsNotNone(match, "explicit YAML event block is mandatory")
        subsequent = text[match.end():]
        # Only inspect actual top-level event entries, never incidental keys
        # inside the jobs or other unrelated YAML blocks.
        next_top = re.search(r"(?m)^[A-Za-z_][A-Za-z_0-9-]*:", subsequent)
        events_block = subsequent[:next_top.start()] if next_top else subsequent
        events = re.findall(r"(?m)^  ([a-z][a-z_]*):", events_block)
        self.assertEqual(events, ["workflow_dispatch"])

    def test_any_destructive_job_requires_visible_confirmation(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        if "--execute" in text:
            self.assertIn("--confirm", text)
            self.assertRegex(text, r"inputs\.mode\s*==\s*['\"]retire['\"]")


if __name__ == "__main__":
    unittest.main()
