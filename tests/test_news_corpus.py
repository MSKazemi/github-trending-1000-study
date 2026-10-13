"""Synthetic negative cases for provisional research-news records."""
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from trending_study import news_corpus
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
        copied["canonical_url"] += "?utm_source=duplicated"
        with self.assertRaisesRegex(ValueError, "duplicate canonical"):
            validate_records([(self.item["id"] + ".json", self.item),
                              (copied["id"] + ".json", copied)])

    def test_query_selected_documents_are_not_false_duplicates(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?item=1"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report?item=2"
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

    def test_tracking_variants_of_same_query_selected_page_are_duplicates(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?id=1&utm_source=email"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://EXAMPLE.org/report?utm_medium=ad&id=1"
        with self.assertRaisesRegex(ValueError, "duplicate canonical"):
            validate_records([(first["id"] + ".json", first),
                              (second["id"] + ".json", second)])

    def test_ref_is_preserved_when_it_may_select_source_version(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/doc?ref=release-a"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/doc?ref=release-b"
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

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

    def test_reject_compact_or_week_date_notation(self):
        for value in ("20261012", "2026-W42-1", "2026-10-12T00:00:00Z"):
            with self.subTest(date=value):
                bad = copy.deepcopy(self.item)
                bad["accessed_date_utc"] = value
                with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
                    validate_records([(bad["id"] + ".json", bad)])

    def test_case_distinct_url_paths_are_not_duplicate(self):
        copied = copy.deepcopy(self.item)
        copied["id"] = "NEWS-2026-0099"
        copied["canonical_url"] = self.item["canonical_url"].replace(
            "/news/", "/NEWS/", 1
        )
        # Hostname is case insensitive, URL path is not.
        self.assertNotEqual(copied["canonical_url"], self.item["canonical_url"])
        result = validate_records([(self.item["id"] + ".json", self.item),
                                   (copied["id"] + ".json", copied)])
        self.assertEqual(result["distinct_urls"], 2)

    def test_v1_does_not_self_certify_independent_review(self):
        for field, value in (
            ("review_status", "validated"),
            ("review_status", "independently_verified"),
            ("screening_status", "approved_by_commit"),
            ("source_review_status", "independent_review_complete"),
            ("independent_corrob_status", "corroborated"),
        ):
            with self.subTest(field=field, value=value):
                bad = copy.deepcopy(self.item)
                bad[field] = value
                with self.assertRaisesRegex(ValueError, "review"):
                    validate_records([(bad["id"] + ".json", bad)])

    def test_disallow_copyright_fulltext_or_malformed_source_url(self):
        fulltext = copy.deepcopy(self.item)
        fulltext["fulltext_stored"] = True
        with self.assertRaisesRegex(ValueError, "fulltext"):
            validate_records([(fulltext["id"] + ".json", fulltext)])
        for url in ("https://bad host.example/record",
                    "https://example.org/\nreport",
                    "https://example.org/\treport"):
            with self.subTest(url=repr(url)):
                bad = copy.deepcopy(self.item)
                bad["canonical_url"] = url
                with self.assertRaisesRegex(ValueError, "whitespace or controls"):
                    validate_records([(bad["id"] + ".json", bad)])

    def test_reject_malformed_canonical_authority_and_empty_userinfo(self):
        for source_url in (
            "https://@example.org/report",
            "https://:secret@example.org/report",
            "https://example.org:/report",
            "https://example.org:0/report",
            "https://example.org:bad/report",
            "https://example.org:65536/report",
            "https://[invalid/report",
        ):
            bad = copy.deepcopy(self.item)
            bad["canonical_url"] = source_url
            with self.subTest(url=source_url), self.assertRaisesRegex(
                    ValueError, "canonical|malformed"):
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


    def test_standalone_news_parser_rejects_duplicate_keys_and_nan(self):
        """The standalone CLI must agree with canonical research JSON gates."""
        for raw, expected in (
            ('{"id":1,"id":2}', "duplicate JSON object key"),
            ('{"energy":NaN}', "nonstandard JSON numeric constant"),
            ('{"energy":1e-9999}', "underflowing"),
        ):
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / "NEWS-2026-0001.json"
                path.write_text(raw, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, expected):
                    validate_directory(folder)

    def test_symlinked_news_input_and_root_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            outside = base / "outside.json"
            outside.write_text(json.dumps(self.item), encoding="utf-8")
            items = base / "items"
            items.mkdir()
            link = items / "NEWS-2026-0001.json"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unsupported")
            with self.assertRaisesRegex(ValueError, "symlink"):
                validate_directory(items)
            link.unlink()
            (items / "NEWS-2026-0001.json").write_text(
                json.dumps(self.item), encoding="utf-8",
            )
            alias = base / "alias"
            alias.symlink_to(items, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                validate_directory(alias)

    def test_bounded_source_read_does_not_rewrite_input(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "NEWS-2026-0001.json"
            path.write_text(json.dumps(self.item), encoding="utf-8")
            original = path.read_bytes()
            self.assertEqual(validate_directory(folder)["records"], 1)
            self.assertEqual(original, path.read_bytes())
            with patch.object(news_corpus, "MAX_FILE_BYTES", 10):
                with self.assertRaisesRegex(ValueError, "file-size limit"):
                    validate_directory(folder)



if __name__ == "__main__":
    unittest.main()
