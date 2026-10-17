"""Verify the committed historical #277 snapshot, not live GitHub ref state."""
from pathlib import Path
import unittest
from scripts.check_archive_crosswalk_snapshot import check


class CommittedArchiveCrosswalkTests(unittest.TestCase):
    def test_manifest_git_blob_and_archived_rows_are_consistent(self):
        result = check(Path(__file__).resolve().parents[1])
        self.assertEqual(result["candidate_count"], 60)
        self.assertEqual(result["exact_archive_tags_observed"], 59)
        self.assertEqual(result["moved_branches_held"], 1)
        self.assertIs(result["historical_snapshot_only"], True)
        self.assertIs(result["deletion_authorized"], False)
