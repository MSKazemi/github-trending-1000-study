"""No-loss historical source archiving checks. No network or research approval."""
import csv
from hashlib import sha1
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "research-notes/branch-draft-archive/issue-100-2026-10-16"
BLOBS = {
    "033-github.events.csv.txt": "0e12d6d668423379f4aaf72d4c5da6938ca4c98c",
    "033-github.md": "55bfd1fbc52157445beca89787197df25b31ceea",
    "033-github.search-log.md": "4d237225ec142388dc4ae90c4529e70b6578e007",
}


def git_blob(raw):
    """Reproduce Git's blob SHA-1 framing for exact original byte comparison."""
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


class HistoricalIssue100SourcePreservationTests(unittest.TestCase):
    def test_all_three_original_git_blobs_survive_unchanged(self):
        for filename, expected in BLOBS.items():
            with self.subTest(file=filename):
                self.assertEqual(git_blob((ARCHIVE / filename).read_bytes()), expected)

    def test_nineteen_records_are_still_noncanonical_vendor_leads(self):
        with (ARCHIVE / "033-github.events.csv.txt").open(
                encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, strict=True))
        self.assertEqual(len(rows), 19)
        self.assertEqual(
            len({row["event_id"] for row in rows}), 19)
        self.assertEqual(
            len({row["source_url"] for row in rows}), 19)
        self.assertEqual(
            {row["source_type"] for row in rows}, {"first_party_changelog"})
        self.assertTrue(all(
            "2026-04-12" <= row["published_utc"] <= "2026-10-12"
            for row in rows))
        self.assertEqual(
            {row["accessed_utc"] for row in rows}, {"2026-10-16"})
        self.assertEqual(
            {row["status"] for row in rows},
            {"shipped", "preview", "announced_only"})

    def test_archival_notes_explicitly_refuse_canonical_promotion(self):
        notes = (ARCHIVE / "README.md").read_text(encoding="utf-8")
        self.assertIn("Do not ingest this folder", notes)
        self.assertIn("all 19 draft", notes)
        self.assertIn("source branch", notes)


if __name__ == "__main__":
    unittest.main()
