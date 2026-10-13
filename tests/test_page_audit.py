"""Scientific QA fixtures: all page HTML and human labels here are synthetic."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.__main__ import extract_repos
from trending_study.page_audit import (
    PageAuditError, assess_page, assess_bundle, audit_bundle_file, markdown_report,
)
from trending_study.pilot import build_capture_manifest, PilotValidationError

STAMP = "2026-10-12T14:00:00+00:00"
REVIEWED = "2026-10-12T14:20:00+00:00"


def make_page(window="daily", n=12, off_selector=False, broken=False):
    names = [f"synthetic-org-{i}/sample-tool-{i}" for i in range(n)]
    articles = []
    for i, repo in enumerate(names):
        if broken and i == 1:
            articles.append('<article class="Box-row"><div>bad row</div></article>')
        else:
            cls = "ChangedTrendingRow" if off_selector and i == n - 1 else "Box-row"
            articles.append(f'<article class="{cls}"><h2>'
                            f'<a href="/{repo}">{repo}</a>'
                            '</h2></article>')
    raw = ('<!doctype html><html><body>' + ''.join(articles)
           + '</body></html>').encode("utf-8")
    manifest = build_capture_manifest(
        raw=raw, output=f"SYNTHETIC_{window}.html", window=window,
        captured_at_utc=STAMP, content_type="text/html",
    )
    def annotation(identity):
        return {
            "schema_version": "1.0",
            "reviewer_id": identity,
            "reviewed_at_utc": REVIEWED,
            "blind_to_parser_output": True,
            "source_sha256": manifest["source_sha256"],
            "source_url": manifest["source_url"],
            "captured_at_utc": manifest["captured_at_utc"],
            "window": window,
            "rows": [{"rank": i, "repository": repo}
                     for i, repo in enumerate(names, 1)],
        }
    return raw, manifest, [annotation(f"R1-{window}"), annotation(f"R2-{window}")]


def bundle_for(windows=("daily", "weekly", "monthly"), n=12):
    files = {}
    pages = []
    for window in windows:
        raw, manifest, reviewers = make_page(window=window, n=n)
        rp = f"{window}.html"
        mp = f"{window}.manifest.json"
        files[rp] = raw
        files[mp] = json.dumps(manifest).encode("utf-8")
        pages.append({
            "raw_path": rp,
            "manifest_path": mp,
            "reviewers": reviewers,
        })
    return {"schema_version": "1.0", "evidence_kind": "synthetic_fixture", "pages": pages}, files


class IndependentPageAuditTests(unittest.TestCase):
    def test_three_windows_36_synthetic_rows_does_not_claim_human_validation(self):
        bundle, files = bundle_for()
        result = assess_bundle(bundle, loader=files.__getitem__, extract_repos=extract_repos)
        self.assertEqual(result["audited_gold_rows"], 36)
        self.assertEqual(result["correct_identity_at_rank"], 36)
        self.assertEqual(result["pages_with_agreed_annotations"], 3)
        self.assertEqual(result["windows_with_agreed_labels"], ["daily", "monthly", "weekly"])
        self.assertEqual(result["automated_documentary_check"], "pass")
        self.assertEqual(result["effective_rank_recall_including_parser_abstentions"], 1.0)
        self.assertEqual(result["scientific_status"], "synthetic_only_not_empirical_evidence")
        self.assertFalse(result["eligible_for_confirmatory_cohort"])
        self.assertTrue(all(not p["eligible_for_confirmatory_cohort"] for p in result["pages"]))

    def test_off_selector_positive_subset_detected_by_independent_labels(self):
        raw, manifest, reviewers = make_page(n=5, off_selector=True)
        report = assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        self.assertEqual(report["page_status"], "detected_missing_or_wrong_rows")
        self.assertEqual(report["emitted_rows"], 4)
        self.assertEqual(report["gold_rows"], 5)
        self.assertEqual(report["false_negatives_including_rank_errors"], 1)
        self.assertEqual(report["effective_rank_recall"], 0.8)

    def test_truncated_or_malformed_row_is_a_parser_abstention_not_pass(self):
        raw, manifest, reviewers = make_page(n=4, broken=True)
        report = assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        self.assertEqual(report["page_status"], "parser_rejected_capture")
        self.assertEqual(report["emitted_rows"], 0)
        self.assertEqual(report["false_negatives_including_rank_errors"], 4)
        self.assertEqual(report["effective_rank_recall"], 0.0)
        self.assertIsNone(report["precision_on_emitted_rows"])

    def test_swapped_rank_counts_both_fp_and_fn(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][0]["repository"], reviewers[0]["rows"][1]["repository"] = (
            reviewers[0]["rows"][1]["repository"], reviewers[0]["rows"][0]["repository"]
        )
        reviewers[1] = copy.deepcopy(reviewers[0])
        reviewers[1]["reviewer_id"] = "second"
        report = assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        self.assertEqual(report["mismatched_ranks"], [1, 2])
        self.assertEqual(report["correct_identity_at_rank"], 2)
        self.assertEqual(report["false_positives_including_rank_errors"], 2)
        self.assertEqual(report["false_negatives_including_rank_errors"], 2)
        self.assertEqual(report["effective_rank_recall"], 0.5)

    def test_annotator_conflict_has_no_false_gold_truth(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[1]["rows"] = reviewers[1]["rows"][:-1]
        report = assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        self.assertFalse(report["reviewer_agreement"])
        self.assertEqual(report["page_status"], "unresolved_reviewer_disagreement")
        self.assertIsNone(report["gold_rows"])
        self.assertIsNone(report["effective_rank_recall"])
        self.assertEqual(report["annotation_disagreement_ranks"], [4])

    def test_same_reviewer_id_rejected(self):
        raw, manifest, reviewers = make_page()
        reviewers[1]["reviewer_id"] = reviewers[0]["reviewer_id"]
        with self.assertRaisesRegex(PageAuditError, "distinct"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)

    def test_one_reviewer_rejected(self):
        raw, manifest, reviewers = make_page()
        with self.assertRaisesRegex(PageAuditError, "two independent"):
            assess_page(raw, manifest, reviewers[:1], extract_repos=extract_repos)

    def test_annotation_missing_or_duplicate_rank_rejected(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][1]["rank"] = 1
        with self.assertRaisesRegex(PageAuditError, "contiguous"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][1]["repository"] = reviewers[0]["rows"][0]["repository"]
        with self.assertRaisesRegex(PageAuditError, "duplicate repository"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)

    def test_page_timestamp_and_checksum_are_bound_to_labels(self):
        raw, manifest, reviewers = make_page()
        reviewers[0]["source_sha256"] = "0" * 64
        with self.assertRaisesRegex(PageAuditError, "source_sha256"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)
        raw, manifest, reviewers = make_page()
        tampered = bytearray(raw)
        tampered[10] ^= 1
        with self.assertRaisesRegex(PilotValidationError, "SHA-256"):
            assess_page(bytes(tampered), manifest, reviewers, extract_repos=extract_repos)

    def test_review_at_time_before_capture_refused(self):
        raw, manifest, reviewers = make_page()
        reviewers[0]["reviewed_at_utc"] = "2026-10-11T00:00:00+00:00"
        with self.assertRaisesRegex(PageAuditError, "predates"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)

    def test_independent_review_attestation_is_required_not_verified(self):
        raw, manifest, reviewers = make_page()
        reviewers[0]["blind_to_parser_output"] = False
        with self.assertRaisesRegex(PageAuditError, "blind"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos)

    def test_thirty_rows_in_only_one_window_is_not_sufficient(self):
        b, files = bundle_for(windows=("daily",), n=33)
        report = assess_bundle(b, loader=files.__getitem__, extract_repos=extract_repos)
        self.assertEqual(report["audited_gold_rows"], 33)
        self.assertFalse(report["coverage_minimum_met"])
        self.assertEqual(report["automated_documentary_check"], "blocked")

    def test_three_windows_with_too_few_rows_is_not_sufficient(self):
        b, files = bundle_for(n=2)
        report = assess_bundle(b, loader=files.__getitem__, extract_repos=extract_repos)
        self.assertEqual(report["audited_gold_rows"], 6)
        self.assertFalse(report["coverage_minimum_met"])

    def test_30_row_minimum_cannot_be_overridden_downward(self):
        b, files = bundle_for()
        with self.assertRaisesRegex(PageAuditError, "30-row"):
            assess_bundle(b, loader=files.__getitem__,
                          extract_repos=extract_repos, min_rows=1)

    def test_duplicate_capture_cannot_inflate_audited_row_denominator(self):
        b, files = bundle_for()
        b["pages"].append(copy.deepcopy(b["pages"][0]))
        with self.assertRaisesRegex(PageAuditError, "duplicate capture"):
            assess_bundle(b, loader=files.__getitem__, extract_repos=extract_repos)

    def test_field_self_reported_never_auto_certifies_scientific_review(self):
        b, files = bundle_for()
        b["evidence_kind"] = "field_self_reported"
        out = assess_bundle(b, loader=files.__getitem__, extract_repos=extract_repos)
        self.assertEqual(out["automated_documentary_check"], "pass")
        self.assertEqual(out["scientific_status"], "self_reported_requires_independent_human_and_source_review")
        self.assertFalse(out["eligible_for_confirmatory_cohort"])

    def test_parser_rejection_reduces_total_effective_rank_recall(self):
        b, files = bundle_for()
        raw, manifest, annot = make_page(window="monthly", n=12, broken=True)
        files["monthly.html"] = raw
        files["monthly.manifest.json"] = json.dumps(manifest).encode("utf-8")
        b["pages"][-1]["reviewers"] = annot
        result = assess_bundle(b, loader=files.__getitem__, extract_repos=extract_repos)
        self.assertEqual(result["pages_parser_rejected"], 1)
        self.assertEqual(result["audited_gold_rows"], 36)
        self.assertEqual(result["correct_identity_at_rank"], 24)
        self.assertAlmostEqual(result["effective_rank_recall_including_parser_abstentions"], 2 / 3)
        self.assertEqual(result["automated_documentary_check"], "blocked")

    def test_cli_outputs_immutable_audit_without_source_network(self):
        b, files = bundle_for()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, body in files.items():
                (root / name).write_bytes(body)
            bundle_path = root / "bundle.json"
            report_path = root / "report.json"
            bundle_path.write_text(json.dumps(b), encoding="utf-8")
            cmd = [
                sys.executable, "-m", "trending_study", "audit-pages",
                "--bundle", str(bundle_path), "--output", str(report_path),
                "--require-consistent",
            ]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            output = json.loads(report_path.read_text())
            self.assertEqual(output["audited_gold_rows"], 36)
            self.assertEqual(output["evidence_kind"], "synthetic_fixture")
            oldhash = hashlib.sha256(report_path.read_bytes()).hexdigest()
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(oldhash, hashlib.sha256(report_path.read_bytes()).hexdigest())

    def test_bundle_cannot_read_absolute_or_escaping_paths(self):
        b, files = bundle_for()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, body in files.items():
                (root / name).write_bytes(body)
            p = root / "bundle.json"
            b["pages"][0]["raw_path"] = "../outside.html"
            p.write_text(json.dumps(b), encoding="utf-8")
            with self.assertRaises((PageAuditError, FileNotFoundError)):
                audit_bundle_file(p, extract_repos=extract_repos)
            b["pages"][0]["raw_path"] = str(root / "daily.html")
            p.write_text(json.dumps(b), encoding="utf-8")
            with self.assertRaisesRegex(PageAuditError, "absolute"):
                audit_bundle_file(p, extract_repos=extract_repos)

    def test_bundle_symlink_escape_is_rejected(self):
        b, files = bundle_for()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            audit_dir = root / "audit"
            audit_dir.mkdir()
            for name, body in files.items():
                (audit_dir / name).write_bytes(body)
            target = root / "outside.html"
            target.write_bytes(files["daily.html"])
            (audit_dir / "escape.html").symlink_to(target)
            b["pages"][0]["raw_path"] = "escape.html"
            p = audit_dir / "bundle.json"
            p.write_text(json.dumps(b), encoding="utf-8")
            with self.assertRaisesRegex(PageAuditError, "escapes"):
                audit_bundle_file(p, extract_repos=extract_repos)

    def test_require_consistent_fails_but_persists_mismatch_report(self):
        b, files = bundle_for()
        b["pages"][0]["reviewers"][0]["rows"][0]["repository"] = "different/label"
        b["pages"][0]["reviewers"][1]["rows"][0]["repository"] = "different/label"
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, body in files.items():
                (root / name).write_bytes(body)
            bp = root / "bundle.json"
            rp = root / "report.json"
            bp.write_text(json.dumps(b), encoding="utf-8")
            proc = subprocess.run([
                sys.executable, "-m", "trending_study", "audit-pages",
                "--bundle", str(bp), "--output", str(rp), "--require-consistent",
            ], capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            result = json.loads(rp.read_text(encoding="utf-8"))
            self.assertEqual(result["automated_documentary_check"], "blocked")
            self.assertFalse(result["eligible_for_confirmatory_cohort"])


    def _c_for(self, reviewers, disputed=(1,), use_second=True):
        c = copy.deepcopy(reviewers[1 if use_second else 0])
        c.update({
            "reviewer_id": "synthetic-third-reviewer",
            "reviewed_at_utc": "2026-10-12T14:35:00+00:00",
            "disagreement_ranks": list(disputed),
            "adjudication_reason": "Synthetic full-page reinspection of disputed rank.",
        })
        return c

    def test_optional_distinct_c_resolves_only_disputed_rank(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        c = self._c_for(reviewers)
        report = assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                             adjudicator=c)
        self.assertFalse(report["reviewer_agreement"])
        self.assertTrue(report["labels_resolved"])
        self.assertEqual(report["reference_resolution"], "c_adjudicated")
        self.assertEqual(report["adjudicator_id"], "synthetic-third-reviewer")
        self.assertEqual(report["annotation_disagreement_ranks"], [1])
        self.assertEqual(report["adjudicated_disagreement_ranks"], [1])
        self.assertEqual(report["page_status"], "exact_rank_identity_agreement")
        self.assertEqual(report["correct_identity_at_rank"], 4)
        self.assertFalse(report["eligible_for_confirmatory_cohort"])

    def test_adjudicated_pages_count_in_resolved_but_not_a_b_agreement(self):
        bundle, files = bundle_for()
        reviewers = bundle["pages"][0]["reviewers"]
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        bundle["pages"][0]["adjudicator"] = self._c_for(reviewers)
        report = assess_bundle(bundle, loader=files.__getitem__,
                               extract_repos=extract_repos)
        self.assertEqual(report["pages_with_agreed_annotations"], 2)
        self.assertEqual(report["pages_with_adjudicated_annotations"], 1)
        self.assertEqual(report["pages_with_resolved_annotations"], 3)
        self.assertEqual(report["pages_with_unresolved_annotation_disagreements"], 0)
        self.assertEqual(report["windows_with_agreed_labels"], ["monthly", "weekly"])
        self.assertEqual(report["windows_with_resolved_labels"],
                         ["daily", "monthly", "weekly"])
        self.assertEqual(report["audited_gold_rows"], 36)
        self.assertEqual(report["automated_documentary_check"], "pass")
        self.assertEqual(report["scientific_status"], "synthetic_only_not_empirical_evidence")
        self.assertFalse(report["eligible_for_confirmatory_cohort"])

    def test_review_timestamps_must_not_be_in_future(self):
        raw, manifest, reviewers = make_page(n=4)
        for slot in (0, 1):
            future = copy.deepcopy(reviewers)
            future[slot]["reviewed_at_utc"] = "2099-01-01T00:00:00+00:00"
            with self.subTest(slot=slot), self.assertRaisesRegex(PageAuditError, "future"):
                assess_page(raw, manifest, future, extract_repos=extract_repos)
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        c = self._c_for(reviewers)
        c["reviewed_at_utc"] = "2099-01-01T00:00:00+00:00"
        with self.assertRaisesRegex(PageAuditError, "future"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)

    def test_adjudication_rejects_same_identity_or_preceding_time(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        c = self._c_for(reviewers)
        c["reviewer_id"] = reviewers[0]["reviewer_id"].upper()
        with self.assertRaisesRegex(PageAuditError, "adjudicator ID"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)
        c = self._c_for(reviewers)
        c["reviewed_at_utc"] = REVIEWED
        with self.assertRaisesRegex(PageAuditError, "after both"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)

    def test_adjudication_rejects_modified_agreed_rank_or_unclaimed_extra(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        c = self._c_for(reviewers)
        c["rows"][1]["repository"] = "different/second-entry"
        with self.assertRaisesRegex(PageAuditError, "agreed A/B rank"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)
        c = self._c_for(reviewers)
        c["rows"].append({"rank": 5, "repository": "different/extra"})
        with self.assertRaisesRegex(PageAuditError, "agreed A/B rank"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)

    def test_adjudication_requires_exact_disagreement_list_reason_and_source(self):
        raw, manifest, reviewers = make_page(n=4)
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        for bad in (([True], "Synthetic review."),
                    ([2], "Synthetic review."),
                    ([1], ""),
                    ([1], "x" * 501)):
            with self.subTest(bad=bad[0], size=len(bad[1])):
                c = self._c_for(reviewers)
                c["disagreement_ranks"], c["adjudication_reason"] = bad
                with self.assertRaises(PageAuditError):
                    assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                                adjudicator=c)
        c = self._c_for(reviewers)
        c["source_sha256"] = "0" * 64
        with self.assertRaisesRegex(PageAuditError, "source_sha256"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)

    def test_cannot_add_adjudicator_to_unanimous_a_b_page(self):
        raw, manifest, reviewers = make_page(n=4)
        c = self._c_for(reviewers, disputed=())
        with self.assertRaisesRegex(PageAuditError, "only allowed"):
            assess_page(raw, manifest, reviewers, extract_repos=extract_repos,
                        adjudicator=c)

    def test_unresolved_disagreement_remains_unscored_with_partial_adjudication(self):
        bundle, files = bundle_for()
        bundle["pages"][0]["reviewers"][0]["rows"][0]["repository"] = "different/first-entry"
        bundle["pages"][1]["reviewers"][0]["rows"][0]["repository"] = "different/first-entry"
        bundle["pages"][0]["adjudicator"] = self._c_for(bundle["pages"][0]["reviewers"])
        report = assess_bundle(bundle, loader=files.__getitem__,
                               extract_repos=extract_repos)
        self.assertEqual(report["pages_with_unresolved_annotation_disagreements"], 1)
        self.assertEqual(report["pages_with_resolved_annotations"], 2)
        self.assertEqual(report["audited_gold_rows"], 24)
        self.assertEqual(report["automated_documentary_check"], "blocked")
        self.assertIsNone(report["pages"][1]["correct_identity_at_rank"])
        self.assertFalse(report["eligible_for_confirmatory_cohort"])


    def test_derived_markdown_keeps_original_json_as_source_of_truth(self):
        bundle, files = bundle_for()
        reviewers = bundle["pages"][0]["reviewers"]
        reviewers[0]["rows"][0]["repository"] = "different/first-entry"
        bundle["pages"][0]["adjudicator"] = self._c_for(reviewers)
        report = assess_bundle(bundle, loader=files.__getitem__,
                               extract_repos=extract_repos)
        markdown = markdown_report(report)
        self.assertIn("| Pages resolved by C | 1 |", markdown)
        self.assertIn("| Unresolved pages | 0 |", markdown)
        self.assertIn("| Confirmatory cohort eligible | no |", markdown)
        self.assertIn("synthetic_only_not_empirical_evidence", markdown)
        self.assertNotIn("synthetic-third-reviewer", markdown)
        self.assertNotIn("https://github.com/trending?", markdown)

    def test_optional_cli_markdown_is_write_once_and_does_not_overwrite_json(self):
        bundle, files = bundle_for()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, data in files.items():
                (root / name).write_bytes(data)
            inp, out, md = root / "bundle.json", root / "result.json", root / "summary.md"
            inp.write_text(json.dumps(bundle), encoding="utf-8")
            cmd = [
                sys.executable, "-m", "trending_study", "audit-pages",
                "--bundle", str(inp), "--output", str(out),
                "--markdown-output", str(md), "--require-consistent",
            ]
            first = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(report["audited_gold_rows"], 36)
            self.assertIn("Confirmatory cohort eligible | no", md.read_text())
            before_json, before_md = out.read_bytes(), md.read_bytes()
            again = subprocess.run(cmd, text=True, capture_output=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertEqual(out.read_bytes(), before_json)
            self.assertEqual(md.read_bytes(), before_md)

    def test_existing_markdown_path_blocks_partial_json_publication(self):
        bundle, files = bundle_for()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, data in files.items():
                (root / name).write_bytes(data)
            inp, out, md = root / "bundle.json", root / "result.json", root / "summary.md"
            inp.write_text(json.dumps(bundle), encoding="utf-8")
            md.write_bytes(b"preserved prior human notes\n")
            proc = subprocess.run([
                sys.executable, "-m", "trending_study", "audit-pages",
                "--bundle", str(inp), "--output", str(out),
                "--markdown-output", str(md),
            ], text=True, capture_output=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertFalse(out.exists())
            self.assertEqual(md.read_bytes(), b"preserved prior human notes\n")


if __name__ == "__main__":
    unittest.main()
