"""Integrity guard for quarantined issue #100 candidate evidence.

These checks pin a historical *authored* ledger, not the truth, rights, or
independent confirmation of any third-party product announcement.
"""
import csv
from datetime import date
import hashlib
import io
from pathlib import Path
import unittest

from scripts.check_research_artifacts import DATA_DIRS
from trending_study.data_integrity import SOURCE_DIRS


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "docs/reviews/2026-10-16-issue-100-provisional-changelog-ledger.csv"
CANONICAL = (
    ROOT / "research/company-intelligence/2026-04-12_2026-10-12/"
    "033-github.events.csv"
)
HISTORICAL_GIT_BLOB = "0e12d6d668423379f4aaf72d4c5da6938ca4c98c"


class HistoricalChangelogArchiveTests(unittest.TestCase):
    def read_csv(self, path):
        self.assertTrue(path.is_file(), f"missing tracked CSV: {path.name}")
        self.assertFalse(path.is_symlink(), f"symlink instead of CSV: {path.name}")
        content = path.read_bytes()
        rows = list(
            csv.reader(
                io.StringIO(content.decode("utf-8"), newline=""),
                strict=True,
            )
        )
        self.assertGreater(len(rows), 1)
        self.assertEqual(len(rows[0]), len(set(rows[0])))
        for number, row in enumerate(rows[1:], 2):
            self.assertEqual(
                len(row), len(rows[0]),
                f"{path.name} has incorrect column count at row {number}",
            )
        return content, rows[0], rows[1:]

    def test_historical_blob_is_byte_exact_and_noncanonical(self):
        content, columns, records = self.read_csv(ARCHIVE)
        git_object = b"blob " + str(len(content)).encode("ascii") + b"\\0" + content
        self.assertEqual(hashlib.sha1(git_object).hexdigest(), HISTORICAL_GIT_BLOB)
        self.assertEqual(len(columns), 21)
        self.assertEqual(len(records), 19)
        self.assertEqual(ARCHIVE.relative_to(ROOT).parts[0], "docs")
        self.assertNotIn("docs", SOURCE_DIRS)
        self.assertNotIn("docs", DATA_DIRS)

        fields = {name: i for i, name in enumerate(columns)}
        self.assertEqual(len(fields), 21)
        self.assertEqual(
            len({record[fields["event_id"]] for record in records}), 19
        )
        self.assertEqual({record[fields["company_id"]] for record in records}, {"033"})
        for record in records:
            published = date.fromisoformat(record[fields["published_utc"]])
            self.assertGreaterEqual(published, date(2026, 4, 12))
            self.assertLessEqual(published, date(2026, 10, 12))

    def test_canonical_urls_remain_separate_pending_human_review(self):
        _, archive_columns, archive_records = self.read_csv(ARCHIVE)
        _, canonical_columns, canonical_records = self.read_csv(CANONICAL)
        self.assertTrue(set(archive_columns).issubset(set(canonical_columns)))
        ai, ci = archive_columns.index("source_url"), canonical_columns.index("source_url")
        historical_urls = {record[ai] for record in archive_records}
        canonical_urls = {record[ci] for record in canonical_records}
        self.assertEqual(len(historical_urls), 19)
        self.assertFalse(
            historical_urls.intersection(canonical_urls),
            "review source identity/event collisions before promoting archived leads",
        )


if __name__ == "__main__":
    unittest.main()
