"""Offline scientific QA tests; all page bodies and reviewers are synthetic."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.page_qa import PageQAError, audit, aggregate
from trending_study.pilot import build_capture_manifest, PilotValidationError

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "trending.html"
CAPTURED = "2026-10-12T12:00:00+00:00"
NAMES = ("alpha-org/first-project", "example-user/another.repo")


def page(raw=None, *, window="daily", names=NAMES, kind="synthetic"):
    raw = FIXTURE.read_bytes() if raw is None else raw
    manifest = build_capture_manifest(
        raw=raw, output="SYNTHETIC-local-fixture.html", window=window,
        captured_at_utc=CAPTURED, content_type="text/html",
    )
    blob = (json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False)
            + "\n").encode("utf-8")
    reviews = []
    for slot, minute in (("A", 10), ("B", 11)):
        reviews.append({
            "schema_version": "page-qa-review-1.0",
            "dataset_kind": kind,
            "reviewer_slot": slot,
            "reviewer_ref": f"SYNTHETIC-rater-{slot}",
            "reviewed_at_utc": f"2026-10-12T12:{minute:02d}:00+00:00",
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "manifest_sha256": hashlib.sha256(blob).hexdigest(),
            "coverage": "all_displayed_rows",
            "inspection_mode": ("synthetic_fixture" if kind == "synthetic"
                                else "independent_rendered_saved_capture"),
            "rows": [{"rank": rank, "repository": identity, "note": None}
                     for rank, identity in enumerate(names, 1)],
            "decision_note": None,
        })
    return raw, blob, reviews[0], reviews[1]


def annotate_third(a, names, *, note="SYNTHETIC disagreement resolution"):
    c = copy.deepcopy(a)
    c["reviewer_slot"] = "C"
    c["reviewer_ref"] = "SYNTHETIC-rater-C"
    c["reviewed_at_utc"] = "2026-10-12T12:15:00+00:00"
    c["decision_note"] = note
    c["rows"] = [{"rank": rank, "repository": identity, "note": None}
                 for rank, identity in enumerate(names, 1)]
    return c


def synthetic_many(prefix, count):
    names = [f"{prefix}/repo-{i}" for i in range(1, count + 1)]
    raw = ("<!doctype html><html><body>"
           + "".join(
               f'<article class="Box-row"><h2><a href="/{name}">{name}</a></h2></article>'
               for name in names
           )
           + "</body></html>").encode("utf-8")
    return raw, names


class PageQATests(unittest.TestCase):
    def test_agreed_two_human_claims_are_synthetic_only(self):
        raw, manifest, a, b = page()
        result = audit(raw, manifest, a, b)
        self.assertEqual(result["reference_resolution"], "agreed")
        self.assertEqual(result["qa_status"], "synthetic_only")
        self.assertEqual(result["cohort_enrollment_status"], "not_enrolled")
        self.assertEqual(result["metrics"]["rank_and_identity"]["tp"], 2)
        self.assertEqual(result["metrics"]["rank_and_identity"]["fn"], 0)
        self.assertEqual(result["metrics"]["identity_only"]["recall"], 1)
        self.assertTrue(result["metrics"]["full_page_exact_match"])

    def test_off_selector_visible_row_becomes_false_negative(self):
        raw = FIXTURE.read_bytes().replace(
            b"</body>",
            b'<div class="new-layout"><a href="/other-org/hidden-row">other</a></div></body>',
        )
        names = list(NAMES) + ["other-org/hidden-row"]
        raw, manifest, a, b = page(raw, names=names)
        result = audit(raw, manifest, a, b)
        self.assertEqual(result["structural_selector_rows"], 2)
        self.assertEqual(result["metrics"]["manual_visible_rows"], 3)
        self.assertEqual(result["metrics"]["rank_and_identity"], {
            "tp": 2, "fp": 0, "fn": 1, "precision": 1.0, "recall": 2 / 3,
        })
        self.assertFalse(result["metrics"]["full_page_exact_match"])

    def test_rank_order_matters_even_if_identities_are_the_same(self):
        raw, manifest, a, b = page(names=list(reversed(NAMES)))
        result = audit(raw, manifest, a, b)
        self.assertEqual(result["metrics"]["rank_and_identity"]["tp"], 0)
        self.assertEqual(result["metrics"]["rank_and_identity"]["fp"], 2)
        self.assertEqual(result["metrics"]["rank_and_identity"]["fn"], 2)
        self.assertEqual(result["metrics"]["identity_only"]["tp"], 2)

    def test_reviewer_disagreement_blocks_metrics(self):
        raw, manifest, a, b = page()
        b["rows"][1]["repository"] = "independent/other-package"
        report = audit(raw, manifest, a, b)
        self.assertIsNone(report["metrics"])
        self.assertEqual(report["reference_resolution"], "disagreement_needs_adjudication")
        self.assertEqual(report["disputed_ranks"], [2])

    def test_independent_adjudicator_can_resolve_only_disputes(self):
        raw, manifest, a, b = page()
        b["rows"][1]["repository"] = "independent/other-package"
        c = annotate_third(a, NAMES)
        report = audit(raw, manifest, a, b, c)
        self.assertEqual(report["reference_resolution"], "adjudicated")
        self.assertEqual(report["metrics"]["rank_and_identity"]["tp"], 2)
        c["rows"][0]["repository"] = "changed/undisputed"
        with self.assertRaisesRegex(PageQAError, "agreed resolved rank"):
            audit(raw, manifest, a, b, c)

    def test_no_adjudication_without_disagreement(self):
        raw, manifest, a, b = page()
        with self.assertRaisesRegex(PageQAError, "only allowed"):
            audit(raw, manifest, a, b, annotate_third(a, NAMES))

    def test_ambiguous_row_cannot_create_false_complete_recall(self):
        raw, manifest, a, b = page()
        for review in (a, b):
            review["rows"][0] = {"rank": 1, "repository": None,
                                  "note": "SYNTHETIC row unreadable"}
        report = audit(raw, manifest, a, b)
        self.assertEqual(report["reference_resolution"], "ambiguous_reference")
        self.assertIsNone(report["metrics"])

    def test_unequal_row_count_blocks_if_added_row_is_ambiguous(self):
        raw, manifest, a, b = page()
        b["rows"].append({"rank": 3, "repository": None,
                          "note": "Additional displayed row uncertain"})
        report = audit(raw, manifest, a, b)
        self.assertIsNone(report["metrics"])

    def test_same_reviewer_cannot_fill_both_independent_slots(self):
        raw, manifest, a, b = page()
        b["reviewer_ref"] = a["reviewer_ref"]
        with self.assertRaisesRegex(PageQAError, "distinct reviewer"):
            audit(raw, manifest, a, b)

    def test_reviews_are_bound_to_raw_and_manifest_bytes(self):
        raw, manifest, a, b = page()
        b["source_sha256"] = "a" * 64
        with self.assertRaisesRegex(PageQAError, "not bound"):
            audit(raw, manifest, a, b)
        _, manifest, a, b = page()
        b["manifest_sha256"] = "a" * 64
        with self.assertRaisesRegex(PageQAError, "not bound"):
            audit(raw, manifest, a, b)

    def test_forged_capture_is_not_accepted(self):
        raw, manifest, a, b = page()
        damaged = raw.replace(b"alpha-org", b"other-org")
        with self.assertRaisesRegex(PilotValidationError, "SHA-256"):
            audit(damaged, manifest, a, b)

    def test_review_must_follow_claimed_capture(self):
        raw, manifest, a, b = page()
        a["reviewed_at_utc"] = "2026-10-12T11:59:59Z"
        with self.assertRaisesRegex(PageQAError, "precedes"):
            audit(raw, manifest, a, b)

    def test_reject_partial_annotations_invalid_ranks_and_extra_fields(self):
        raw, manifest, a, b = page()
        a["coverage"] = "selected_rows_only"
        with self.assertRaisesRegex(PageQAError, "full displayed"):
            audit(raw, manifest, a, b)
        _, _, a, b = page()
        a["rows"][1]["rank"] = 1
        with self.assertRaisesRegex(PageQAError, "rank"):
            audit(raw, manifest, a, b)
        _, _, a, b = page()
        a["rows"][0]["person_email"] = "not-publishable@example.test"
        with self.assertRaisesRegex(PageQAError, "exactly"):
            audit(raw, manifest, a, b)

    def test_synthetic_data_cannot_claim_real_visual_review(self):
        raw, manifest, a, b = page()
        a["inspection_mode"] = "independent_rendered_saved_capture"
        with self.assertRaisesRegex(PageQAError, "inspection mode"):
            audit(raw, manifest, a, b)

    def test_pilot_label_remains_self_declared_and_not_enrolled(self):
        raw, manifest, a, b = page(kind="pilot")
        result = audit(raw, manifest, a, b)
        self.assertEqual(result["qa_status"], "requires_external_human_signoff")
        self.assertEqual(result["cohort_enrollment_status"], "not_enrolled")

    def test_aggregate_30_rows_across_three_windows_remains_unapproved(self):
        reports = []
        for window, n in (("daily", 11), ("weekly", 10), ("monthly", 10)):
            raw, names = synthetic_many("simulated-" + window, n)
            raw, manifest, a, b = page(raw, window=window, names=names)
            reports.append(audit(raw, manifest, a, b))
        summary = aggregate(reports)
        self.assertEqual(summary["audited_manual_rows"], 31)
        self.assertEqual(summary["rank_and_identity"]["tp"], 31)
        self.assertEqual(summary["documentary_minimum"], "synthetic_not_applicable")
        self.assertEqual(summary["cohort_enrollment_status"], "not_enrolled")
        self.assertEqual(summary["windows_observed"], ["daily", "monthly", "weekly"])
        # Relabeling a synthetic result to "pilot" cannot bypass status guards.
        for report in reports:
            report["dataset_kind"] = "pilot"
        with self.assertRaisesRegex(PageQAError, "dataset kind and result status"):
            aggregate(reports)
        # These pilot-shaped files are STILL fictional in this test and do not
        # establish real reviewer independence or source permission.
        pilot_reports = []
        for window, n in (("daily", 11), ("weekly", 10), ("monthly", 10)):
            raw, names = synthetic_many("simulated-pilot-" + window, n)
            raw, manifest, a, b = page(raw, window=window, names=names, kind="pilot")
            pilot_reports.append(audit(raw, manifest, a, b))
        pilot_claims = aggregate(pilot_reports)
        self.assertEqual(pilot_claims["documentary_minimum"], "met_on_self_reported_inputs")
        self.assertEqual(pilot_claims["status"], "external_scientific_signoff_required")

    def test_pilot_mismatch_blocks_parser_approval_even_with_reviewed_rows(self):
        raw = FIXTURE.read_bytes().replace(
            b"</body>",
            b'<div class="new-layout"><a href="/other-org/hidden-row">third</a></div></body>',
        )
        names = list(NAMES) + ["other-org/hidden-row"]
        raw, manifest, a, b = page(raw, kind="pilot", names=names)
        report = audit(raw, manifest, a, b)
        self.assertEqual(report["qa_status"], "parser_mismatch_needs_revision")
        grouped = aggregate([report])
        self.assertEqual(grouped["status"], "parser_mismatch_needs_revision")
        self.assertEqual(grouped["cohort_enrollment_status"], "not_enrolled")

    def test_aggregate_rejects_same_capture_double_counting(self):
        raw, manifest, a, b = page()
        report = audit(raw, manifest, a, b)
        with self.assertRaisesRegex(PageQAError, "multiple audited pages"):
            aggregate([report, report])

    def test_aggregate_unresolved_page_blocks_numeric_comparison(self):
        raw, manifest, a, b = page()
        b["rows"][0]["repository"] = "different/name"
        report = audit(raw, manifest, a, b)
        result = aggregate([report])
        self.assertEqual(result["unresolved_pages"], 1)
        self.assertIsNone(result["rank_and_identity"])

    def test_aggregate_rejects_inconsistent_precision_denominators(self):
        raw, manifest, a, b = page()
        report = audit(raw, manifest, a, b)
        report["metrics"]["rank_and_identity"]["tp"] = 12
        with self.assertRaisesRegex(PageQAError, "inconsistent report confusion"):
            aggregate([report])

    def test_committed_synthetic_reviewer_examples_match_fixture_bytes(self):
        root = Path(__file__).resolve().parents[1]
        manifest = (root / "examples/page_qa_manifest.synthetic.json").read_bytes()
        review_a = json.loads((root / "examples/page_qa_review_A.synthetic.json").read_text())
        review_b = json.loads((root / "examples/page_qa_review_B.synthetic.json").read_text())
        raw = FIXTURE.read_bytes()
        result = audit(raw, manifest, review_a, review_b)
        self.assertEqual(result["qa_status"], "synthetic_only")
        self.assertEqual(result["metrics"]["rank_and_identity"]["tp"], 2)
        self.assertTrue(result["metrics"]["full_page_exact_match"])

    def test_cli_is_offline_and_immutable(self):
        raw, manifest, a, b = page()
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            (folder / "raw.html").write_bytes(raw)
            (folder / "capture.json").write_bytes(manifest)
            (folder / "a.json").write_text(json.dumps(a), encoding="utf-8")
            (folder / "b.json").write_text(json.dumps(b), encoding="utf-8")
            dest = folder / "report.json"
            cmd = [
                sys.executable, "-m", "trending_study.page_qa", "audit",
                "--raw", str(folder / "raw.html"),
                "--manifest", str(folder / "capture.json"),
                "--review-a", str(folder / "a.json"),
                "--review-b", str(folder / "b.json"),
                "--output", str(dest),
            ]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads(dest.read_text())["qa_status"], "synthetic_only")
            again = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertEqual(json.loads(dest.read_text())["metrics"]["parsed_rows"], 2)
            # The separate summary command is also offline/write-once.
            output = folder / "summary.json"
            grouped = subprocess.run([
                sys.executable, "-m", "trending_study.page_qa", "aggregate",
                "--inputs", str(dest), "--output", str(output),
            ], capture_output=True, text=True)
            self.assertEqual(grouped.returncode, 0, grouped.stderr)
            self.assertEqual(json.loads(output.read_text())["page_count"], 1)


if __name__ == "__main__":
    unittest.main()
