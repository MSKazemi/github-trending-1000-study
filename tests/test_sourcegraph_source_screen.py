"""Offline checks for a *selected first-party source-lead ledger*, not fact QA.

Passing these tests does not establish a census, original publication dates,
vendor deployment, independent company verification or successful software reuse.
"""
import csv
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit
import unittest


ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "research/company-intelligence/2026-04-12_2026-10-12"
LEDGER = FOLDER / "015-sourcegraph.events.csv"
REPORT = FOLDER / "015-sourcegraph.md"
SCREEN = FOLDER / "015-sourcegraph.screen-log.md"
COLUMNS = ("event_id",
           "company_id",
           "company_label",
           "product",
           "source_url",
           "source_title",
           "source_publisher",
           "source_type",
           "published_utc",
           "event_date_utc",
           "accessed_utc",
           "kind",
           "claim_summary",
           "feature",
           "availability",
           "status",
           "study_construct",
           "limitation",
           "confidence",
           "duplicate_event_group",
           "independent_check_url")
STATUS = {"shipped", "preview", "announced_only", "reported_undetermined",
          "reversed/cancelled", "corrected", "unavailable/unknown"}
# The 9 rows merged in PR #178 keep their original strict checks.
ORIGINAL_IDS = ("CI2026-015-001", "CI2026-015-002", "CI2026-015-003",
                "CI2026-015-004", "CI2026-015-005", "CI2026-015-006",
                "CI2026-015-007", "CI2026-015-008", "CI2026-015-009")
WINDOW_START = date(2026, 4, 12)
WINDOW_END = date(2026, 10, 12)


def read_rows():
    with LEDGER.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(COLUMNS):
            raise AssertionError("unexpected event ledger schema")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values())
           for row in rows):
        raise AssertionError("incomplete or over-wide CSV record")
    return rows


class SourcegraphScreenTests(unittest.TestCase):
    def test_selected_leads_are_unique_dated_and_within_scope(self):
        rows = read_rows()
        self.assertGreaterEqual(len(rows), 9)
        originals = [row for row in rows if row["event_id"] in ORIGINAL_IDS]
        self.assertEqual({row["event_id"] for row in originals}, set(ORIGINAL_IDS))
        self.assertEqual(len(originals), 9)
        urls, ids, groups = set(), set(), set()
        for row in originals:
            with self.subTest(event=row["event_id"]):
                self.assertEqual(row["company_id"], "015")
                self.assertEqual(row["company_label"], "Sourcegraph")
                self.assertEqual(row["source_publisher"], "Sourcegraph")
                self.assertEqual(row["source_type"], "first_party_changelog")
                self.assertEqual(row["kind"], "dated_vendor_notice")
                self.assertEqual(row["accessed_utc"], "2026-10-14")
                self.assertEqual(row["confidence"], "E1_VENDOR_PAGE_ONLY")
                self.assertEqual(row["independent_check_url"], "")
                self.assertEqual(row["event_date_utc"], "")
                self.assertIn(row["status"], STATUS)
                self.assertTrue(row["limitation"].strip())
                self.assertTrue(row["source_title"].strip())
                self.assertTrue(row["study_construct"].strip())
                when = date.fromisoformat(row["published_utc"])
                self.assertGreaterEqual(when, WINDOW_START)
                self.assertLessEqual(when, WINDOW_END)
                parsed = urlsplit(row["source_url"])
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.hostname, "sourcegraph.com")
                self.assertFalse(parsed.username or parsed.password)
                self.assertIsNone(parsed.port)
                self.assertFalse(parsed.query or parsed.fragment)
                self.assertTrue(parsed.path.startswith("/changelog/"))
                for field, key in (("event_id", ids), ("source_url", urls),
                                   ("duplicate_event_group", groups)):
                    value = row[field].strip()
                    self.assertNotEqual(value, "")
                    self.assertNotIn(value, key)
                    key.add(value)

    def test_additional_rows_keep_schema_scope_and_unique_ids(self):
        # Rows appended after the original 9 (2026-10-16 upgrade) may cite other
        # source types, but must stay in scope; passing is not fact verification.
        rows = read_rows()
        ids, urls = set(), set()
        for row in rows:
            for field, key in (("event_id", ids), ("source_url", urls)):
                value = row[field].strip()
                self.assertNotEqual(value, "")
                self.assertNotIn(value, key)
                key.add(value)
        for row in rows:
            if row["event_id"] in ORIGINAL_IDS:
                continue
            with self.subTest(event=row["event_id"]):
                self.assertTrue(row["event_id"].startswith("CI2026-015-"))
                self.assertEqual(row["company_id"], "015")
                self.assertIn(row["status"], STATUS)
                when = date.fromisoformat(row["published_utc"])
                self.assertGreaterEqual(when, WINDOW_START)
                self.assertLessEqual(when, WINDOW_END)
                parsed = urlsplit(row["source_url"])
                self.assertEqual(parsed.scheme, "https")
                self.assertTrue(parsed.hostname)
                self.assertFalse(parsed.username or parsed.password)
                self.assertIsNone(parsed.port)
                self.assertTrue(row["source_title"].strip())
                self.assertTrue(row["limitation"].strip())
                self.assertTrue(row["study_construct"].strip())

    def test_all_seven_segments_have_selected_leads_not_full_search_counts(self):
        rows = [row for row in read_rows() if row["event_id"] in ORIGINAL_IDS]
        expected = {4, 5, 6, 7, 8, 9, 10}
        self.assertEqual({date.fromisoformat(r["published_utc"]).month
                          for r in rows}, expected)
        # This checks chosen rows only; there is no executed full-corpus denominator.
        screen = SCREEN.read_text(encoding="utf-8")
        self.assertIn("not a systematic or exhaustive search", screen)
        self.assertIn("hit counts: unavailable", screen)
        self.assertIn("2026-10-13", screen)  # excluded post-window update
        for month in ("April", "May", "June", "July", "August",
                      "September", "October"):
            self.assertIn(month, screen)

    def test_beta_and_ga_are_distinct_not_inferred_outcomes(self):
        rows = read_rows()
        by_id = {row["event_id"]: row for row in rows}
        self.assertEqual(by_id["CI2026-015-004"]["status"], "preview")
        self.assertEqual(by_id["CI2026-015-005"]["status"], "preview")
        self.assertEqual(by_id["CI2026-015-008"]["status"], "shipped")
        self.assertIn("cloud", by_id["CI2026-015-008"]["availability"])
        self.assertIn("E1", by_id["CI2026-015-008"]["confidence"])
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("not an independent benchmark", report)
        self.assertIn("Human factual/methods review: pending", report)
        self.assertIn("not issue #81 completion", report)


if __name__ == "__main__":
    unittest.main()
