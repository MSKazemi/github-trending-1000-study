"""Offline audit of an *independent*, whole-page Trending visual annotation.

No web requests, no automated human reviews and no cohort enrollment.
The saved capture/manifest are checked by the existing strict pilot parser.
Actual reviewers, source access and independence require external verification.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from .__main__ import extract_repos, inspect_trending_structure
from .pilot import validate_capture
from .safe_io import disjoint, publish_json, refuse_existing

REVIEW_VERSION = "page-qa-review-1.0"
REPORT_VERSION = "page-qa-report-1.0"
SUMMARY_VERSION = "page-qa-summary-1.0"
SOURCE_KINDS = frozenset(("synthetic", "pilot"))
WINDOWS = frozenset(("daily", "weekly", "monthly"))
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
REVIEW_FIELDS = frozenset((
    "schema_version", "dataset_kind", "reviewer_slot", "reviewer_ref",
    "reviewed_at_utc", "source_sha256", "manifest_sha256",
    "coverage", "inspection_mode", "rows", "decision_note",
))
ROW_FIELDS = frozenset(("rank", "repository", "note"))


class PageQAError(ValueError):
    """Invalid or methodologically incomplete page QA data."""


def _exact(data, fields, label):
    if not isinstance(data, dict) or set(data) != fields:
        raise PageQAError(f"{label} must have exactly these fields: {sorted(fields)}")
    return data


def _string(value, label, maximum=512):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise PageQAError(f"{label} must be nonempty text at most {maximum} characters")
    return value.strip()


def _utc(value, label):
    raw = _string(value, label, 80)
    try:
        result = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PageQAError(f"{label} must be an ISO-8601 UTC timestamp") from exc
    if result.tzinfo is None or result.utcoffset() != timezone.utc.utcoffset(result):
        raise PageQAError(f"{label} must be explicitly UTC")
    return result


def _sha(value, label):
    if not isinstance(value, str) or SHA256.fullmatch(value) is None:
        raise PageQAError(f"{label} must be lowercase SHA-256")
    return value


def _repo(value):
    if not isinstance(value, str) or REPO.fullmatch(value) is None:
        return False
    return all(part not in (".", "..") for part in value.split("/"))


def _rows(value, label):
    if not isinstance(value, list) or not 1 <= len(value) <= 100:
        raise PageQAError(f"{label} needs 1..100 consecutive displayed rows")
    result = []
    for rank, row in enumerate(value, 1):
        _exact(row, ROW_FIELDS, f"{label}[{rank}]")
        if type(row["rank"]) is not int or row["rank"] != rank:
            raise PageQAError(f"{label}[{rank}] has missing, duplicate or reordered rank")
        identity, note = row["repository"], row["note"]
        if identity is not None and not _repo(identity):
            raise PageQAError(f"{label}[{rank}] has invalid repository identity")
        if identity is None:
            _string(note, f"{label}[{rank}].note")
        elif note is not None and (not isinstance(note, str) or len(note) > 512):
            raise PageQAError(f"{label}[{rank}].note must be text or null")
        result.append(identity)
    return result


def validate_review(review, slot, *, raw_sha, manifest_sha, capture_time):
    _exact(review, REVIEW_FIELDS, f"review {slot}")
    if review["schema_version"] != REVIEW_VERSION:
        raise PageQAError("review schema version mismatch")
    if review["dataset_kind"] not in SOURCE_KINDS:
        raise PageQAError("review dataset_kind must be synthetic or pilot")
    if review["reviewer_slot"] != slot:
        raise PageQAError(f"expected reviewer slot {slot}")
    reviewer = _string(review["reviewer_ref"], f"review {slot} pseudonymous reference", 128)
    if reviewer == "unknown":
        raise PageQAError("review must have a distinct pseudonymous source reference")
    _sha(review["source_sha256"], "review source digest")
    _sha(review["manifest_sha256"], "review manifest digest")
    if review["source_sha256"] != raw_sha or review["manifest_sha256"] != manifest_sha:
        raise PageQAError(f"review {slot} is not bound to these immutable capture bytes")
    if _utc(review["reviewed_at_utc"], f"review {slot} time") < capture_time:
        raise PageQAError(f"review {slot} time precedes its claimed capture time")
    if review["coverage"] != "all_displayed_rows":
        raise PageQAError("review must explicitly cover the full displayed page")
    required_mode = ("synthetic_fixture" if review["dataset_kind"] == "synthetic"
                     else "independent_rendered_saved_capture")
    if review["inspection_mode"] != required_mode:
        raise PageQAError(f"review {slot}: incorrect inspection mode for dataset_kind")
    note = review["decision_note"]
    if slot == "C":
        _string(note, "adjudication decision_note")
    elif note is not None:
        raise PageQAError("A/B reviewers cannot submit adjudication decision_note")
    identities = _rows(review["rows"], f"review {slot}.rows")
    return reviewer, identities


def _conflicts(a, b):
    conflicts = []
    absent = object()  # Missing rows differ from explicitly unreadable rows.
    for rank in range(1, max(len(a), len(b)) + 1):
        one = a[rank - 1] if rank <= len(a) else absent
        two = b[rank - 1] if rank <= len(b) else absent
        if one != two:
            conflicts.append(rank)
    return conflicts


def _count_matches(predicted, reference, *, with_rank):
    def pairs(values):
        return Counter(
            (rank, name.casefold()) if with_rank else name.casefold()
            for rank, name in enumerate(values, 1)
        )
    p, g = pairs(predicted), pairs(reference)
    tp = sum((p & g).values())
    fp = sum((p - g).values())
    fn = sum((g - p).values())
    return {
        "tp": tp, "fp": fp, "fn": fn,
        "precision": (tp / (tp + fp)) if tp + fp else None,
        "recall": (tp / (tp + fn)) if tp + fn else None,
    }


def audit(raw, manifest_bytes, review_a, review_b, adjudication=None):
    """One page: human-provided, claimed independent labels vs parsed rows.

    Parser rejection blocks the run; no synthetic data are silently promoted.
    Third-party reviewer identity or completeness cannot be authenticated here.
    """
    if not isinstance(raw, bytes) or not isinstance(manifest_bytes, bytes):
        raise PageQAError("raw capture and manifest must be exact bytes")
    try:
        manifest = json.loads(manifest_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PageQAError("invalid UTF-8 JSON capture manifest") from exc
    # Existing strict path validates source bytes, window, time, URL and layout.
    # An unsupported/rejected layout is a hard QA blocker, not a zero-row sample.
    parsed, structural = validate_capture(
        raw, manifest, extract_repos=extract_repos,
        inspect_structure=inspect_trending_structure,
    )
    raw_sha = hashlib.sha256(raw).hexdigest()
    manifest_sha = hashlib.sha256(manifest_bytes).hexdigest()
    captured_at = _utc(manifest["captured_at_utc"], "manifest captured_at_utc")
    ref_a, rows_a = validate_review(
        review_a, "A", raw_sha=raw_sha, manifest_sha=manifest_sha,
        capture_time=captured_at,
    )
    ref_b, rows_b = validate_review(
        review_b, "B", raw_sha=raw_sha, manifest_sha=manifest_sha,
        capture_time=captured_at,
    )
    if ref_a == ref_b:
        raise PageQAError("A and B must use distinct reviewer references")
    if review_a["dataset_kind"] != review_b["dataset_kind"]:
        raise PageQAError("reviewers disagree on dataset_kind")
    kind = review_a["dataset_kind"]
    disputed = _conflicts(rows_a, rows_b)
    reference = rows_a if not disputed else None
    status = "agreed" if not disputed else "disagreement_needs_adjudication"
    adjudicator_ref = None
    if adjudication is not None:
        if not disputed and all(name is not None for name in rows_a):
            raise PageQAError("adjudication only allowed for disagreement or ambiguity")
        if adjudication.get("dataset_kind") != kind:
            raise PageQAError("adjudicator dataset_kind differs from A/B")
        adjudicator_ref, rows_c = validate_review(
            adjudication, "C", raw_sha=raw_sha, manifest_sha=manifest_sha,
            capture_time=captured_at,
        )
        if adjudicator_ref in (ref_a, ref_b):
            raise PageQAError("adjudicator reference must be distinct from A and B")
        if _utc(adjudication["reviewed_at_utc"], "adjudicator time") < max(
            _utc(review_a["reviewed_at_utc"], "A review time"),
            _utc(review_b["reviewed_at_utc"], "B review time"),
        ):
            raise PageQAError("adjudication cannot predate either independent review")
        for rank in range(1, min(len(rows_a), len(rows_b), len(rows_c)) + 1):
            one, two = rows_a[rank - 1], rows_b[rank - 1]
            if one is not None and one == two and rows_c[rank - 1] != one:
                raise PageQAError("adjudicator cannot change an agreed resolved rank")
        reference = rows_c
        status = "adjudicated"
    if reference is not None and any(identity is None for identity in reference):
        status = "ambiguous_reference"
        reference = None
    if reference is not None and not reference:
        raise PageQAError("human reference cannot be an empty page")
    predicted = [row["repository"] for row in parsed]
    metric = None
    if reference is not None:
        metric = {
            "manual_visible_rows": len(reference),
            "parsed_rows": len(predicted),
            "rank_and_identity": _count_matches(predicted, reference, with_rank=True),
            "identity_only": _count_matches(predicted, reference, with_rank=False),
            "full_page_exact_match": [x.casefold() for x in predicted] == [
                x.casefold() for x in reference
            ],
        }
    exact = metric is not None and metric["full_page_exact_match"]
    return {
        "schema_version": REPORT_VERSION,
        "dataset_kind": kind,
        "source_sha256": raw_sha,
        "manifest_sha256": manifest_sha,
        "source_url": manifest["source_url"],
        "capture_date_utc": manifest["capture_date_utc"],
        "window": manifest["window"],
        "reviewer_a_ref": ref_a,
        "reviewer_b_ref": ref_b,
        "adjudicator_ref": adjudicator_ref,
        "reviewer_a_visible_rows": len(rows_a),
        "reviewer_b_visible_rows": len(rows_b),
        "disputed_rank_count": len(disputed),
        "disputed_ranks": disputed,
        "reference_resolution": status,
        "metrics": metric,
        "structural_selector_rows": structural["selector_box_row_count"],
        "qa_status": (
            "synthetic_only" if kind == "synthetic" else
            "blocked_independent_review" if metric is None else
            "parser_mismatch_needs_revision" if not exact else
            "requires_external_human_signoff"
        ),
        "cohort_enrollment_status": "not_enrolled",
        "warning": (
            "Reviewer independence, source access permission and exact human page "
            "coverage are external claims, not authenticated by this CLI. A correct "
            "synthetic score does not verify a real page, sampling frame, or cohort."
        ),
    }


def aggregate(reports):
    """Aggregate validated report-shaped *claims*, never certify real human audit."""
    if not isinstance(reports, list) or not reports:
        raise PageQAError("at least one page-QA report required")
    seen = set()
    kinds, windows = set(), set()
    pages = []
    total_rows = 0
    tp = fp = fn = 0
    unresolved = 0
    for report in reports:
        required = {
            "schema_version", "dataset_kind", "source_sha256", "manifest_sha256",
            "source_url", "capture_date_utc", "window", "reviewer_a_ref",
            "reviewer_b_ref", "adjudicator_ref", "reviewer_a_visible_rows",
            "reviewer_b_visible_rows", "disputed_rank_count", "disputed_ranks",
            "reference_resolution", "metrics", "structural_selector_rows",
            "qa_status", "cohort_enrollment_status", "warning",
        }
        _exact(report, required, "page QA report")
        if report["schema_version"] != REPORT_VERSION or report["dataset_kind"] not in SOURCE_KINDS:
            raise PageQAError("unexpected page QA version/kind")
        _sha(report["source_sha256"], "capture SHA")
        _sha(report["manifest_sha256"], "manifest SHA")
        if report["window"] not in WINDOWS:
            raise PageQAError("unsupported audit window")
        if report["manifest_sha256"] in seen:
            raise PageQAError("same immutable capture cannot count as multiple audited pages")
        seen.add(report["manifest_sha256"])
        if report["cohort_enrollment_status"] != "not_enrolled":
            raise PageQAError("audit report cannot claim enrolled observations")
        kinds.add(report["dataset_kind"])
        windows.add(report["window"])
        metric = report["metrics"]
        expected_status = (
            "synthetic_only" if report["dataset_kind"] == "synthetic" else
            "blocked_independent_review" if metric is None else
            "requires_external_human_signoff" if metric.get("full_page_exact_match") is True else
            "parser_mismatch_needs_revision"
        )
        if report["qa_status"] != expected_status:
            raise PageQAError("audit dataset kind and result status disagree")
        if metric is None:
            unresolved += 1
        else:
            if (type(metric.get("manual_visible_rows")) is not int
                or type(metric.get("parsed_rows")) is not int
                or metric["manual_visible_rows"] < 1
                or metric["parsed_rows"] < 1):
                raise PageQAError("invalid report row denominator")
            totals = metric.get("rank_and_identity")
            if not isinstance(totals, dict) or any(type(totals.get(k)) is not int or totals[k] < 0
                                                   for k in ("tp", "fp", "fn")):
                raise PageQAError("invalid TP/FP/FN in aggregate input")
            if (totals["tp"] + totals["fp"] != metric["parsed_rows"]
                or totals["tp"] + totals["fn"] != metric["manual_visible_rows"]):
                raise PageQAError("inconsistent report confusion denominators")
            total_rows += metric["manual_visible_rows"]
            tp += totals["tp"]
            fp += totals["fp"]
            fn += totals["fn"]
        pages.append({"window": report["window"], "capture_sha256": report["source_sha256"],
                      "reference_resolution": report["reference_resolution"],
                      "manual_visible_rows": metric["manual_visible_rows"] if metric else None})
    if len(kinds) != 1:
        raise PageQAError("synthetic and pilot reports must never share an aggregate")
    kind = next(iter(kinds))
    has_coverage = not unresolved and total_rows >= 30 and windows == WINDOWS
    outcome_status = (
        "synthetic_only" if kind == "synthetic" else
        "blocked_independent_review" if unresolved else
        "parser_mismatch_needs_revision" if fp or fn else
        "insufficient_documentary_coverage" if not has_coverage else
        "external_scientific_signoff_required"
    )
    return {
        "schema_version": SUMMARY_VERSION, "dataset_kind": kind,
        "pages": pages, "page_count": len(pages),
        "audited_manual_rows": total_rows,
        "unresolved_pages": unresolved, "windows_observed": sorted(windows),
        "rank_and_identity": {
            "tp": tp, "fp": fp, "fn": fn,
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None,
        } if not unresolved else None,
        "documentary_minimum": (
            "synthetic_not_applicable" if kind == "synthetic" else
            ("met_on_self_reported_inputs" if has_coverage else "not_met")
        ),
        "cohort_enrollment_status": "not_enrolled",
        "status": outcome_status,
        "warning": (
            "Aggregate recomputes metrics from input reports but does not authenticate "
            "their original HTML, actual review independence, open-access/permission "
            "status or sampling coverage. Human evidence audit and signoff remain mandatory."
        ),
    }


def main(argv=None):
    cli = argparse.ArgumentParser(description="Offline independent Trending page-QA evidence audit")
    sub = cli.add_subparsers(dest="command", required=True)
    one = sub.add_parser("audit", help="Compare two manual full-page reviews with a saved captured page")
    one.add_argument("--raw", required=True)
    one.add_argument("--manifest", required=True)
    one.add_argument("--review-a", required=True)
    one.add_argument("--review-b", required=True)
    one.add_argument("--adjudication")
    one.add_argument("--output", required=True)
    many = sub.add_parser("aggregate", help="Report multi-page/documentary 30-row coverage")
    many.add_argument("--inputs", required=True, nargs="+")
    many.add_argument("--output", required=True)
    args = cli.parse_args(argv)
    try:
        if args.command == "audit":
            paths = [args.raw, args.manifest, args.review_a, args.review_b]
            if args.adjudication:
                paths.append(args.adjudication)
            disjoint(*paths, args.output)
            refuse_existing(args.output)
            result = audit(
                Path(args.raw).read_bytes(), Path(args.manifest).read_bytes(),
                json.loads(Path(args.review_a).read_text(encoding="utf-8")),
                json.loads(Path(args.review_b).read_text(encoding="utf-8")),
                json.loads(Path(args.adjudication).read_text(encoding="utf-8"))
                if args.adjudication else None,
            )
        else:
            disjoint(*args.inputs, args.output)
            refuse_existing(args.output)
            result = aggregate([json.loads(Path(p).read_text(encoding="utf-8"))
                                for p in args.inputs])
        publish_json(args.output, result)
        print(json.dumps({
            "output": args.output,
            "status": result.get("qa_status", result.get("status")),
            "cohort_enrollment_status": result["cohort_enrollment_status"],
        }))
    except (OSError, ValueError, TypeError) as exc:
        cli.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
