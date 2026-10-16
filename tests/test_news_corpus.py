"""Synthetic negative cases for provisional research-news records."""
import copy
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from trending_study import news_corpus
import unittest

from trending_study.news_corpus import validate_directory, validate_records
from trending_study.data_integrity import decode_research_json

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "tests" / "fixtures" / "news_corpus"


class NewsCorpusTests(unittest.TestCase):
    def setUp(self):
        path = ITEMS / "NEWS-2026-0001.json"
        self.item = json.loads(path.read_text(encoding="utf-8"))

    def test_all_committed_items_pass_structural_validation(self):
        result = validate_directory(ITEMS)
        self.assertEqual(result["records"], 1)
        self.assertEqual(result["distinct_urls"], result["records"])
        self.assertEqual(result["evidence_status"], "provisional_structural_validation_only")

    def test_fixture_is_explicitly_synthetic_and_never_self_reviewed(self):
        self.assertEqual(self.item["screening_status"], "synthetic_test_only")
        self.assertEqual(self.item["source_review_status"], "not_inspected_synthetic_fixture")
        self.assertIn("Synthetic", self.item["publisher"])
        self.assertEqual(self.item["review_status"], "pending")
        self.assertIsNone(self.item["independent_reviewer"])
        self.assertFalse(self.item["fulltext_stored"])

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

    def test_repeated_query_parameter_order_selects_distinct_sources(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?step=first&step=second"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report?step=second&step=first"
        # Sorting (key,value) pairs would falsely collapse these two ordered
        # selectors. The validator may not discard either source lead.
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

    def test_repeated_query_with_trackers_still_deduplicates(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = (
            "https://example.org/report?step=first&utm_source=email&step=second"
        )
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = (
            "https://EXAMPLE.org/report?step=first&step=second&gclid=abc"
        )
        with self.assertRaisesRegex(ValueError, "duplicate canonical"):
            validate_records([(first["id"] + ".json", first),
                              (second["id"] + ".json", second)])

    def test_unique_query_parameter_order_remains_normalized(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?a=1&b=2"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report?b=2&a=1"
        with self.assertRaisesRegex(ValueError, "duplicate canonical"):
            validate_records([(first["id"] + ".json", first),
                              (second["id"] + ".json", second)])

    def test_raw_percent_encoded_selector_variants_are_not_false_duplicates(self):
        # parse_qsl would decode these to identical (key, value) tuples,
        # although a server may route raw encodings to distinct documents.
        for query_a, query_b in (
            ("id=alpha%2Fbeta", "id=alpha/beta"),
            ("term=hello+world", "term=hello%20world"),
            ("ref=%2e", "ref=."),
        ):
            first = copy.deepcopy(self.item)
            second = copy.deepcopy(self.item)
            first["canonical_url"] = "https://example.org/report?" + query_a
            second["id"] = "NEWS-2026-0099"
            second["canonical_url"] = "https://example.org/report?" + query_b
            with self.subTest(first=query_a, second=query_b):
                result = validate_records([(first["id"] + ".json", first),
                                           (second["id"] + ".json", second)])
                self.assertEqual(result["distinct_urls"], 2)

    def test_decoded_duplicate_query_keys_preserve_raw_order(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?id=one&%69d=two"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report?%69d=two&id=one"
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

    def test_encoded_tracker_key_is_not_removed_without_source_review(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report?id=1"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report?id=1&utm%5Fsource=email"
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

    def test_trailing_slash_can_select_distinct_source_documents(self):
        first = copy.deepcopy(self.item)
        second = copy.deepcopy(self.item)
        first["canonical_url"] = "https://example.org/report"
        second["id"] = "NEWS-2026-0099"
        second["canonical_url"] = "https://example.org/report/"
        # Paths may be distinct resources: dedup should not discard either
        # provisional source lead without a content-level human review.
        result = validate_records([(first["id"] + ".json", first),
                                   (second["id"] + ".json", second)])
        self.assertEqual(result["distinct_urls"], 2)

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
                # Rejection must not echo user-controlled duplicate key names.
                with self.assertRaisesRegex(ValueError, "invalid or ambiguous research JSON"):
                    validate_directory(folder)
                # The fixed CLI diagnostic hides it, but the canonical decoder
                # rule named by ``expected`` must be what rejected the input.
                with self.assertRaisesRegex(ValueError, expected):
                    decode_research_json(raw.encode("utf-8"), "synthetic news input")

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

    def test_unexpected_json_filename_is_not_silently_skipped(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "missing_id.json"
            path.write_text(json.dumps(self.item), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unexpected JSON"):
                validate_directory(root)

    def test_nested_directory_and_non_record_file_are_not_silently_skipped(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / "nested").mkdir()
            with self.assertRaisesRegex(ValueError, "nested news directories"):
                validate_directory(base)
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / "NEWS-2026-0001.json").write_text(
                json.dumps(self.item), encoding="utf-8",
            )
            (base / "NOT_REVIEWED.txt").write_text("unreviewed", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unexpected non-record"):
                validate_directory(base)

    def test_reject_ambiguous_percent_escape_and_backslash(self):
        for url in ("https://example.org/news/%xx",
                    "https://example.org/news/%",
                    "https://example.org\\\\other/news"):
            with self.subTest(url=url):
                bad = copy.deepcopy(self.item)
                bad["canonical_url"] = url
                with self.assertRaisesRegex(ValueError, "canonical URL"):
                    validate_records([(bad["id"] + ".json", bad)])

    def test_actual_vendor_citation_is_not_authenticated_by_synthetic_schema(self):
        copied = copy.deepcopy(self.item)
        copied["canonical_url"] = "https://example.org/claims/never-visited"
        copied["screening_status"] = "included_provisional_single_reviewer"
        copied["source_review_status"] = "web_primary_page_inspected_not_independently_fact_checked"
        result = validate_records([(copied["id"] + ".json", copied)])
        self.assertEqual(result["evidence_status"],
                         "provisional_structural_validation_only")

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
