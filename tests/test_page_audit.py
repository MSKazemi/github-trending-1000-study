"""Synthetic-only, offline tests for independent page annotation QA."""
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.page_audit import PageAuditError, audit, main, markdown_report
from trending_study.pilot import PilotValidationError, build_capture_manifest
from trending_study.safe_io import ProvenanceWriteError

CAPTURED = "2026-10-12T08:00:00+00:00"
REVIEWED = "2026-10-12T09:00:00+00:00"
ROWS = ["alpha-org/first-project", "example-user/another.repo"]


def render_page(repos, *, extra=""):
    return ("<!doctype html><html><body>" + "".join(
        f'<article class="Box-row"><h2><a href="/{repo}">{repo}</a></h2></article>'
        for repo in repos
    ) + extra + "</body></html>").encode("utf-8")


def ranked(names):
    return [{"rank": i, "repository": repo} for i, repo in enumerate(names, 1)]


def page_bundle(base, key="a", *, window="daily", repos=None, visible=None,
                alternate=None, raw=None):
    repos = ROWS if repos is None else repos
    visible = repos if visible is None else visible
    source = raw if raw is not None else render_page(repos)
    d = base / key
    d.mkdir(parents=True, exist_ok=True)
    (d / "raw.html").write_bytes(source)
    manifest = build_capture_manifest(
        raw=source, output=str(d / "raw.html"), window=window,
        captured_at_utc=CAPTURED, content_type="text/html; charset=UTF-8",
        http_status=200,
    )
    (d / "manifest.json").write_text(json.dumps(manifest))
    annotation = {
        "schema_version": "1.0",
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "source_url": manifest["source_url"],
        "annotation_scope": "all_visible_repository_rows",
        "reviewers": [
            {
                "reviewer_code": "SYNTH_A",
                "declares_independent_blinded_annotation": True,
                "complete_visible_row_scan": True,
                "reviewed_at_utc": REVIEWED,
                "rows": ranked(visible),
            },
            {
                "reviewer_code": "SYNTH_B",
                "declares_independent_blinded_annotation": True,
                "complete_visible_row_scan": True,
                "reviewed_at_utc": REVIEWED,
                "rows": ranked(visible if alternate is None else alternate),
            },
        ],
    }
    (d / "annotation.json").write_text(json.dumps(annotation))
    return dict(raw_file=f"{key}/raw.html", manifest_file=f"{key}/manifest.json",
                annotation_file=f"{key}/annotation.json")


def index_file(base, *pages):
    path = base / "index.json"
    path.write_text(json.dumps({"schema_version": "1.0", "pages": list(pages)}))
    return path


def update_json(path, update):
    obj = json.loads(path.read_text())
    update(obj)
    path.write_text(json.dumps(obj))


class IndependentPageAuditTests(unittest.TestCase):
    def test_two_agreeing_declarations_are_perfect_within_synthetic_frame(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            idx = index_file(base, page_bundle(base))
            result, inputs = audit(idx, synthetic=True)
            counts = result["counts"]
            self.assertEqual(counts["compared_pages"], 1)
            self.assertEqual(counts["audited_gold_rows"], 2)
            self.assertEqual(counts["true_positive_ranked_rows"], 2)
            self.assertEqual(counts["false_negative_ranked_rows"], 0)
            self.assertEqual(result["micro_precision_within_agreed_audit_frame"], 1.0)
            self.assertEqual(result["micro_recall_within_agreed_audit_frame"], 1.0)
            self.assertFalse(result["minimum_30_rows_three_unfiltered_windows_met"])
            self.assertIn("independent_review", result["readiness"])
            self.assertEqual(result["analysis_status"], "SYNTHETIC_FIXTURE")
            self.assertEqual(len(inputs), 4)
            self.assertIn("NOT VERIFIED", markdown_report(result))

    def test_partial_positive_parse_detected_by_independent_off_selector_label(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            extra = '<article class="redesigned"><h2><a href="/quiet/missed">third</a></h2></article>'
            source = render_page(ROWS, extra=extra)
            row = page_bundle(base, raw=source, visible=ROWS + ["quiet/missed"])
            result, _ = audit(index_file(base, row), synthetic=True)
            self.assertEqual(result["counts"]["true_positive_ranked_rows"], 2)
            self.assertEqual(result["counts"]["false_negative_ranked_rows"], 1)
            self.assertAlmostEqual(result["micro_recall_within_agreed_audit_frame"], 2 / 3)
            self.assertEqual(result["counts"]["parser_failed_pages"], 0)

    def test_structural_parser_refusal_counts_operational_false_negatives(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = render_page([ROWS[0]]) + b""
            source = source.replace(b"</body></html>",
                                    b'<article class="Box-row"><p>broken</p></article></body></html>')
            row = page_bundle(base, raw=source, visible=ROWS)
            result, _ = audit(index_file(base, row))
            self.assertEqual(result["counts"]["parser_failed_pages"], 1)
            self.assertEqual(result["counts"]["false_negative_ranked_rows"], 2)
            self.assertIsNone(result["micro_precision_within_agreed_audit_frame"])
            self.assertEqual(result["micro_recall_within_agreed_audit_frame"], 0.0)
            self.assertEqual(result["pages"][0]["parser_status"], "failed_closed")

    def test_rank_mismatch_is_fp_and_fn_not_disguised_as_match(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            idx = index_file(base, page_bundle(base, visible=list(reversed(ROWS))))
            result, _ = audit(idx)
            counts = result["counts"]
            self.assertEqual(counts["true_positive_ranked_rows"], 0)
            self.assertEqual(counts["false_positive_ranked_rows"], 2)
            self.assertEqual(counts["false_negative_ranked_rows"], 2)
            self.assertEqual(counts["wrong_rank_for_shared_identity"], 2)

    def test_rater_disagreement_retained_not_scored_or_silently_repaired(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            idx = index_file(base, page_bundle(base, alternate=[ROWS[0], "different/repo"]))
            result, _ = audit(idx)
            self.assertEqual(result["counts"]["unresolved_reviewer_pages"], 1)
            self.assertEqual(result["counts"]["compared_pages"], 0)
            self.assertIsNone(result["pages"][0]["comparison"])
            self.assertEqual(result["pages"][0]["reviewer_disagreement_ranks"], [2])
            self.assertIsNone(result["micro_recall_within_agreed_audit_frame"])
            self.assertFalse(result["operational_exact_match_in_agreed_audit_frame"])

    def test_three_windows_and_30_rows_floor_is_not_human_approval(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            repos = [f"org/repo{i}" for i in range(10)]
            pages = [
                page_bundle(base, str(i), window=window, repos=repos)
                for i, window in enumerate(("daily", "weekly", "monthly"))
            ]
            result, _ = audit(index_file(base, *pages))
            self.assertEqual(result["counts"]["audited_gold_rows"], 30)
            self.assertTrue(result["minimum_30_rows_three_unfiltered_windows_met"])
            self.assertTrue(result["operational_exact_match_in_agreed_audit_frame"])
            self.assertEqual(result["readiness"],
                             "requires_independent_review_and_source_access_approval")
            self.assertEqual(result["language_panel_audit_status"], "not_supported_or_tested")

    def test_capture_tampering_fails_before_comparison(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            bundle = page_bundle(base)
            (base / "a" / "raw.html").write_bytes(b"Tampered after manifest")
            with self.assertRaisesRegex(PilotValidationError, "SHA-256|byte count"):
                audit(index_file(base, bundle))

    def test_forged_annotation_hash_or_source_url_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            path = base / "a" / "annotation.json"
            update_json(path, lambda a: a.update(source_sha256="0" * 64))
            with self.assertRaisesRegex(PageAuditError, "SHA256"):
                audit(index_file(base, b))
            update_json(path, lambda a: a.update(source_sha256=hashlib.sha256(
                (base / "a" / "raw.html").read_bytes()).hexdigest(),
                source_url="https://github.com.evil.test/trending"))
            with self.assertRaisesRegex(PageAuditError, "URL differs"):
                audit(index_file(base, b))

    def test_not_blinded_or_not_full_scan_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            path = base / "a" / "annotation.json"
            update_json(path, lambda a: a["reviewers"][0].update(
                declares_independent_blinded_annotation=False))
            with self.assertRaisesRegex(PageAuditError, "independent blinded"):
                audit(index_file(base, b))
            update_json(path, lambda a: a["reviewers"][0].update(
                declares_independent_blinded_annotation=True,
                complete_visible_row_scan=False))
            with self.assertRaisesRegex(PageAuditError, "complete visible"):
                audit(index_file(base, b))

    def test_duplicate_rater_identity_or_invalid_rank_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            path = base / "a" / "annotation.json"
            update_json(path, lambda a: a["reviewers"][1].update(reviewer_code="SYNTH_A"))
            with self.assertRaisesRegex(PageAuditError, "distinct"):
                audit(index_file(base, b))
            update_json(path, lambda a: (
                a["reviewers"][1].update(reviewer_code="SYNTH_B"),
                a["reviewers"][0]["rows"][0].update(rank=2)))
            with self.assertRaisesRegex(PageAuditError, "ranks must"):
                audit(index_file(base, b))

    def test_review_timestamp_before_capture_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            update_json(base / "a" / "annotation.json",
                        lambda a: a["reviewers"][0].update(
                            reviewed_at_utc="2026-10-11T09:00:00+00:00"))
            with self.assertRaisesRegex(PageAuditError, "before the capture"):
                audit(index_file(base, b))

    def test_duplicate_capture_in_index_cannot_inflate_denominator(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            with self.assertRaisesRegex(PageAuditError, "included twice"):
                audit(index_file(base, b, b))

    def test_index_cannot_read_outside_declared_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            b = page_bundle(base)
            b["raw_file"] = "../secret.html"
            with self.assertRaisesRegex(PageAuditError, "escapes"):
                audit(index_file(base, b))

    def test_cli_writes_two_write_once_artifacts_with_no_remote_requests(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            idx = index_file(base, page_bundle(base))
            output = base / "output.json"
            markdown = base / "output.md"
            argv = ["--index", str(idx), "--output", str(output),
                    "--markdown", str(markdown), "--synthetic"]
            with redirect_stdout(io.StringIO()):
                main(argv)
            report = json.loads(output.read_text())
            self.assertEqual(report["analysis_status"], "SYNTHETIC_FIXTURE")
            self.assertEqual(report["counts"]["true_positive_ranked_rows"], 2)
            self.assertIn("SYNTHETIC_FIXTURE", markdown.read_text())
            orig = output.read_bytes()
            with self.assertRaises(ProvenanceWriteError):
                main(argv)
            self.assertEqual(output.read_bytes(), orig)

    def test_cli_subprocess_reports_synthetic_not_empirical(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            idx = index_file(base, page_bundle(base))
            p = subprocess.run([
                sys.executable, "-m", "trending_study.page_audit",
                "--index", str(idx), "--output", str(base / "qa.json"),
                "--synthetic",
            ], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(json.loads(p.stdout)["analysis_status"], "SYNTHETIC_FIXTURE")


if __name__ == "__main__":
    unittest.main()
