"""Synthetic negative cases for provisional research-news records."""
import copy
import json
from pathlib import Path
import unittest

from trending_study.news_corpus import validate_directory, validate_records

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "references" / "ai-era-news" / "items"


class NewsCorpusTests(unittest.TestCase):
    def setUp(self):
        path = ITEMS / "NEWS-2026-0001.json"
        self.item = json.loads(path.read_text(encoding="utf-8"))

    def test_all_committed_items_pass_structural_validation(self):
        result = validate_directory(ITEMS)
        self.assertGreaterEqual(result["records"], 20)
        self.assertEqual(result["distinct_urls"], result["records"])
        self.assertEqual(result["evidence_status"], "provisional_structural_validation_only")

    def test_initial_tranche_has_six_source_organizations_and_multiple_views(self):
        records = [json.loads(p.read_text(encoding="utf-8"))
                   for p in sorted(ITEMS.glob("NEWS-*.json"))]
        self.assertGreaterEqual(len({r["publisher"] for r in records}), 6)
        self.assertGreaterEqual(len({t for r in records for t in r["topics"]}), 6)
        self.assertTrue(all(r["review_status"] == "pending" for r in records))
        self.assertTrue(all(r["independent_reviewer"] is None for r in records))
        self.assertTrue(all(r["fulltext_stored"] is False for r in records))

    def test_duplicate_canonical_source_even_with_tracking_query(self):
        copied = copy.deepcopy(self.item)
        copied["id"] = "NEWS-2026-0099"
        copied["canonical_url"] += "?ref=duplicated"
        with self.assertRaisesRegex(ValueError, "duplicate canonical"):
            validate_records([(self.item["id"] + ".json", self.item),
                              (copied["id"] + ".json", copied)])

    def test_reject_wrong_filename_or_id(self):
        with self.assertRaisesRegex(ValueError, "filename and ID"):
            validate_records([("wrong.json", self.item)])

    def test_reject_unknown_fields_and_future_publication(self):
        bad = copy.deepcopy(self.item)
        bad["raw_article_body"] = "unsafe copied content"
        with self.assertRaisesRegex(ValueError, "fields"):
            validate_records([(bad["id"] + ".json", bad)])
        bad = copy.deepcopy(self.item)
        bad["original_publication_date"] = "2099-01-01"
        with self.assertRaisesRegex(ValueError, "future"):
            validate_records([(bad["id"] + ".json", bad)])

    def test_reject_insecure_url_and_false_human_review(self):
        bad = copy.deepcopy(self.item)
        bad["canonical_url"] = "http://example.com"
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            validate_records([(bad["id"] + ".json", bad)])
        bad = copy.deepcopy(self.item)
        bad["independent_reviewer"] = "not-a-real-review"
        with self.assertRaisesRegex(ValueError, "pending independent review"):
            validate_records([(bad["id"] + ".json", bad)])


if __name__ == "__main__":
    unittest.main()
