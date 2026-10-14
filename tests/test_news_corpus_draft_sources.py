"""Draft corpus structure check: not a verification of any news publisher claim.

This test intentionally belongs to source PR #59 until independent reviewers
confirm its 20 provisional records and their underlying sources.
"""
from pathlib import Path
import unittest

from trending_study.news_corpus import validate_directory

ITEMS = Path(__file__).resolve().parents[1] / "references" / "ai-era-news" / "items"


class ProvisionalNewsCorpusStructureTests(unittest.TestCase):
    def test_all_draft_source_records_are_parseable_and_still_unverified(self):
        report = validate_directory(ITEMS)
        self.assertEqual(report["records"], len(list(ITEMS.glob("NEWS-*.json"))))
        self.assertGreaterEqual(report["records"], 20)
        self.assertEqual(report["distinct_urls"], report["records"])
        self.assertEqual(report["evidence_status"],
                         "provisional_structural_validation_only")


if __name__ == "__main__":
    unittest.main()
