"""Offline, synthetic/structural checks for the bounded #55 journal shortlist.

Passing this test does not authenticate publications, reviewers, PDF bytes or
scientific findings. Those require separate source/access/method assessment.
"""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "references" / "journal_open_access_2026_10_12.json"


class JournalShortlistContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(REGISTER.read_text(encoding="utf-8"))

    def test_complete_distinct_declared_shortlist(self):
        data = self.data
        self.assertEqual(data["schema_version"], "1.0")
        rows = data["articles"]
        self.assertEqual(len(rows), data["article_count"])
        self.assertEqual(len(rows), 7)
        self.assertEqual({r["id"] for r in rows}, {"J01", "J02", "J03", "J04", "J05", "J06", "J07"})
        self.assertEqual(len({r["doi"] for r in rows}), len(rows))

    def test_publisher_and_pdf_links_are_explicit_but_not_authenticated(self):
        for r in self.data["articles"]:
            with self.subTest(r=r["id"]):
                self.assertRegex(r["doi"], r"^10\\.[0-9]{4,9}/[^\\s]+$")
                self.assertEqual(r["doi_url"], "https://doi.org/" + r["doi"])
                for field in ("publisher_url", "pdf_url"):
                    url = urlsplit(r[field])
                    self.assertEqual(url.scheme, "https")
                    self.assertTrue(url.hostname)
                    self.assertIsNone(url.username)
                    self.assertIsNone(url.password)
                self.assertIn(r["pdf_type"], {"publisher_pdf", "author_manuscript"})
                self.assertEqual(r["pdf_access_check_status"], "not_checked_this_pass")
                self.assertIsNone(r["pdf_checksum_sha256"])
                self.assertEqual(r["license_review_status"], "not_checked_this_pass")
                self.assertFalse(r["verified_research_findings"])

    def test_category_specific_hypothesis_and_missing_human_signoff(self):
        data = self.data
        self.assertEqual(data["scope"], "targeted_non_systematic_journal_shortlist_not_empirical_results")
        self.assertFalse(data["independent_human_review_completed"])
        self.assertFalse(data["pdf_content_or_checksum_verified"])
        for row in data["articles"]:
            with self.subTest(id=row["id"]):
                self.assertTrue(row["article_type"])
                self.assertGreater(len(row["reason_for_inclusion"]), 25)
                self.assertGreater(len(row["proposed_falsifiable_maintainer_test"]), 25)
                self.assertEqual(row["independent_human_review_status"], "pending")
                self.assertEqual(row["full_text_method_extraction_status"], "pending")
                self.assertLessEqual(row["online_publication_date"], data["snapshot_date"])

    def test_navigation_and_provenance_disclosure(self):
        reading = (ROOT / "docs" / "READING_LIST_2027.md").read_text(encoding="utf-8")
        shortlist = (ROOT / "docs" / "OPEN_ACCESS_JOURNAL_EVIDENCE_2026_10_12.md").read_text(encoding="utf-8")
        self.assertIn("OPEN_ACCESS_JOURNAL_EVIDENCE_2026_10_12.md", reading)
        self.assertIn("journal_open_access_2026_10_12.json", reading)
        self.assertIn("journal_open_access_2026_10_12.json", shortlist)
        self.assertIn("independent scientific approval", shortlist)


if __name__ == "__main__":
    unittest.main()
