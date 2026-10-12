"""Fail-closed parser structural checks; all input pages are synthetic."""
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from trending_study.__main__ import (
    extract_repos, inspect_trending_structure, pilot_parse, valid_repo,
)
from trending_study.pilot import build_capture_manifest

FIXTURE = Path(__file__).parent / "fixtures" / "trending.html"


def article(href="/team/repo", *, heading=True):
    head = f'<h2><a href="{href}">team / repo</a></h2>' if heading else "<p>No header</p>"
    return f'<article class="Box-row">{head}</article>'


def html(*rows):
    return "<html><body>" + "".join(rows) + "</body></html>"


class CompleteTrendingParserTests(unittest.TestCase):
    def test_valid_one_to_one_rows_and_nested_markup(self):
        page = html(
            '<article class="Box-row"><h2><a href="/first/repo">'
            '<svg></svg><span>first</span>/<span>repo</span></a></h2></article>',
            article("/second/tools"),
        )
        self.assertEqual(extract_repos(page), ["first/repo", "second/tools"])
        structure = inspect_trending_structure(page)
        self.assertEqual(structure["selector_box_row_count"], 2)
        self.assertEqual(structure["extracted_repository_count"], 2)
        self.assertIn("independent page QA", structure["limitation"])

    def test_positive_subset_with_missing_header_fails(self):
        page = html(article("/first/valid"), article(heading=False))
        with self.assertRaisesRegex(ValueError, "1/2 valid"):
            extract_repos(page)

    def test_duplicate_articles_are_quarantined_not_silently_rank_shifted(self):
        with self.assertRaisesRegex(ValueError, "duplicate repository"):
            extract_repos(html(article("/first/repo"), article("/first/repo")))
        with self.assertRaisesRegex(ValueError, "duplicate repository"):
            extract_repos(html(article("/FIRST/REPO"), article("/first/repo")))

    def test_two_header_links_are_ambiguous(self):
        page = html('<article class="Box-row"><h2>'
                    '<a href="/first/repo">first</a><a href="/other/repo">other</a>'
                    '</h2></article>')
        with self.assertRaisesRegex(ValueError, "2 header links"):
            extract_repos(page)

    def test_two_headings_cannot_map_to_one_repo(self):
        page = html('<article class="Box-row"><h2><a href="/first/repo">a</a></h2>'
                    '<h2><a href="/second/repo">b</a></h2></article>')
        with self.assertRaisesRegex(ValueError, "2 h2"):
            extract_repos(page)

    def test_malformed_and_offsite_repos_rejected(self):
        for name in ("https://evil.invalid/owner/repo", "/../repo",
                     "/user/..", "//evil.invalid/owner/repo", "/user/repo?tab=issues"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "malformed repository link"):
                    extract_repos(html(article(name)))
        self.assertFalse(valid_repo("user/.."))
        self.assertFalse(valid_repo("../repo"))

    def test_truncated_supported_article_fails(self):
        page = "<html><body>" + article("/first/good") + '<article class="Box-row"><h2><a href="/two/three">'
        with self.assertRaisesRegex(ValueError, "unclosed Box-row"):
            extract_repos(page)

    def test_nested_article_is_considered_untrusted(self):
        page = html('<article class="Box-row"><h2><a href="/first/repo">ok</a></h2>'
                    '<article><p>unexpected nested article</p></article></article>')
        with self.assertRaisesRegex(ValueError, "nested article"):
            extract_repos(page)

    def test_off_selector_layout_change_is_not_inferred_to_be_complete(self):
        with self.assertRaisesRegex(ValueError, "No supported Trending"):
            extract_repos(html('<article class="TrendingRow"><h2>'
                               '<a href="/owner/repo">repo</a></h2></article>'))

    def test_unrelated_footer_and_non_box_article_not_counted(self):
        page = html(article("/owner/repo"),
                    '<article class="marketing-card"><h2>Get started</h2></article>',
                    '<footer><a href="/settings/profile">footer</a></footer>')
        self.assertEqual(extract_repos(page), ["owner/repo"])

    def test_missing_box_row_is_not_turned_into_nice_zero_results(self):
        with self.assertRaises(ValueError):
            extract_repos('<html><div>challenge</div></html>')

    def test_pilot_parser_rejects_partial_html_before_any_output(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            capture = root / "raw.html"
            mf = root / "raw.manifest.json"
            rows_path = root / "rows.jsonl"
            audit_path = root / "audit.json"
            raw = html(article("/one/ok"), article(heading=False)).encode("utf-8")
            capture.write_bytes(raw)
            m = build_capture_manifest(
                raw=raw, output=str(capture), window="daily",
                captured_at_utc="2026-10-12T10:30:00+00:00",
                content_type="text/html; charset=UTF-8",
            )
            mf.write_text(json.dumps(m))
            arguments = type("Args", (), {
                "input": str(capture), "manifest": str(mf),
                "output": str(rows_path), "audit_output": str(audit_path),
            })()
            with self.assertRaisesRegex(ValueError, "structural completeness"):
                with redirect_stdout(io.StringIO()):
                    pilot_parse(arguments)
            self.assertFalse(rows_path.exists())
            self.assertFalse(audit_path.exists())
            self.assertEqual(hashlib.sha256(capture.read_bytes()).hexdigest(),
                             m["source_sha256"])

    def test_pilot_audit_reports_internal_structure_not_human_recall(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            capture = root / "raw.html"
            mf = root / "raw.manifest.json"
            rows_path = root / "rows.jsonl"
            audit_path = root / "audit.json"
            raw = FIXTURE.read_bytes()
            capture.write_bytes(raw)
            mf.write_text(json.dumps(build_capture_manifest(
                raw=raw, output=str(capture), window="daily",
                captured_at_utc="2026-10-12T10:30:00+00:00",
                content_type="text/html",
            )))
            arguments = type("Args", (), {
                "input": str(capture), "manifest": str(mf),
                "output": str(rows_path), "audit_output": str(audit_path),
            })()
            with redirect_stdout(io.StringIO()):
                pilot_parse(arguments)
            audit = json.loads(audit_path.read_text())
            self.assertEqual(audit["selector_box_row_count"], 2)
            self.assertEqual(audit["page_rows"], 2)
            self.assertEqual(audit["structural_parser_status"], "matched_selector_rows_consistent")
            self.assertEqual(audit["parser_qa_status"], "requires_independent_manual_audit")
            self.assertEqual(audit["cohort_enrollment_status"], "not_enrolled")


if __name__ == "__main__":
    unittest.main()
