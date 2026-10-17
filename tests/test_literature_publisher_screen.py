"""Offline structural regressions for the deliberately bounded 2026-10-16 screen.

Source/authorship, venue, rights and independent reviewer authenticity require
human review. These assertions do not validate a systematic search.
"""
import copy
import json
from pathlib import Path
import unittest

from trending_study.literature_ledger import LiteratureError, audit

INPUT = (Path(__file__).resolve().parents[1]
         / "references" / "literature_publisher_screen_2026-10-16.json")


class PublisherScreenPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(INPUT.read_text(encoding="utf-8"))

    def test_record_counts_and_reproducible_run_links(self):
        actual = audit(self.payload)
        self.assertEqual(actual["search_runs"], 5)
        self.assertEqual(actual["screened_records"], 11)
        self.assertEqual(actual["decisions"], {
            "exclude": 1, "include": 8, "pending": 2,
        })
        self.assertTrue(actual["screening_is_self_reported"])
        self.assertFalse(actual["prisma_flow_authenticated"])
        self.assertTrue(actual["duplicate_detection_is_not_adjudication"])

    def test_versioned_same_study_is_flagged_not_silently_deduplicated(self):
        actual = audit(self.payload)
        self.assertEqual(actual["possible_duplicate_groups"][
            "doi:10.48550/arxiv.2601.18341"], [
            "LS20261016-06", "LS20261016-07",
        ])
        self.assertEqual(len(self.payload["records"]), 11)

    def test_all_included_items_have_source_and_full_candidate_extract(self):
        self.assertEqual(
            len({x["record_id"] for x in self.payload["records"]}), 11
        )
        for record in self.payload["records"]:
            if record["decision"] == "include":
                self.assertTrue(record["source_url"].startswith("https://"))
                self.assertTrue(all(record["study_extract"].get(k) for k in (
                    "design", "population", "outcome", "limitations")))
            if record["decision"] == "exclude":
                self.assertTrue(record["reason"])
        self.assertEqual(audit(self.payload)["decisions"]["include"], 8)

    def test_unknown_source_or_future_metadata_fail_closed(self):
        corrupted = copy.deepcopy(self.payload)
        corrupted["records"][0]["source_url"] = "https://reader:token@host.example/paper"
        with self.assertRaises(LiteratureError):
            audit(corrupted)
        corrupted = copy.deepcopy(self.payload)
        corrupted["records"][0]["publication_year"] = 2099
        with self.assertRaises(LiteratureError):
            audit(corrupted)
        corrupted = copy.deepcopy(self.payload)
        corrupted["records"][0]["run_id"] = "nonexistent"
        with self.assertRaises(LiteratureError):
            audit(corrupted)

    def test_no_unearned_inference_from_fixtures(self):
        self.assertFalse(audit(self.payload)["prisma_flow_authenticated"])
        self.assertTrue(all(
            x["source_type"] != "peer_reviewed"
            for x in self.payload["records"]
            if x["run_id"] == "METR_WEB"))
        self.assertTrue(all(
            x["decision"] == "pending"
            for x in self.payload["records"]
            if x["record_id"] in ("LS20261016-06", "LS20261016-07")))


if __name__ == "__main__":
    unittest.main()
