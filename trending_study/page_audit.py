"""Independent, source-linked page annotation comparison for Trending pilot QA.

All metrics refer ONLY to reviewer-declared visible rows on supplied pages.
The program neither authenticates human review nor approves cohort enrollment.
No network calls, third-party packages, or implicit source collection.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

from .__main__ import extract_repos, inspect_trending_structure, valid_repo
from .pilot import PilotValidationError, _utc_timestamp, validate_capture
from .safe_io import disjoint, publish_once, refuse_existing

AUDIT_VERSION = "1.0"
WINDOWS = ("daily", "weekly", "monthly")
REVIEWER_CODE = re.compile(r"^[A-Za-z0-9_-]{2,64}$")


class PageAuditError(ValueError):
    """Source or independent-label comparison cannot be trusted."""


def _obj(value, field):
    if not isinstance(value, dict):
        raise PageAuditError(f"{field} must be an object")
    return value


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise PageAuditError(f"{field} must be nonempty text")
    return value


def _json(path):
    raw = Path(path).read_bytes()
    if len(raw) > 1_000_000:
        raise PageAuditError(f"JSON document too large: {path}")
    try:
        return json.loads(raw.decode("utf-8")), hashlib.sha256(raw).hexdigest()
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PageAuditError(f"Invalid UTF-8 JSON document: {path}") from exc


def _contained_path(root, value, field):
    """Inputs are explicit local files beneath the index's directory."""
    name = Path(_text(value, field))
    if name.is_absolute():
        raise PageAuditError(f"{field} must be relative to index directory")
    resolved = (root / name).resolve()
    if not resolved.is_relative_to(root):
        raise PageAuditError(f"{field} escapes index directory")
    if not resolved.is_file():
        raise PageAuditError(f"{field} is not an existing file")
    return resolved


def _review_rows(rows, field):
    if not isinstance(rows, list):
        raise PageAuditError(f"{field}.rows must be a list")
    result = []
    seen = set()
    for expected_rank, row in enumerate(rows, 1):
        _obj(row, f"{field}.rows[{expected_rank}]")
        rank = row.get("rank")
        repo = row.get("repository")
        if type(rank) is not int or rank != expected_rank:
            raise PageAuditError(f"{field}: ranks must be 1..N without gaps")
        if not valid_repo(repo):
            raise PageAuditError(f"{field}: invalid repository identity")
        key = repo.casefold()
        if key in seen:
            raise PageAuditError(f"{field}: repeated repository name")
        seen.add(key)
        result.append((rank, key))
    return result


def _annotated_gold(annotation, manifest):
    """Compare two independent declarations, retain unresolved disagreements."""
    _obj(annotation, "annotation")
    if annotation.get("schema_version") != AUDIT_VERSION:
        raise PageAuditError("unsupported annotation schema")
    if annotation.get("source_sha256") != manifest["source_sha256"]:
        raise PageAuditError("annotation source SHA256 differs from capture")
    if annotation.get("source_url") != manifest["source_url"]:
        raise PageAuditError("annotation source URL differs from capture")
    if annotation.get("annotation_scope") != "all_visible_repository_rows":
        raise PageAuditError("annotation must declare whole visible-repository-row scope")
    reviewers = annotation.get("reviewers")
    if not isinstance(reviewers, list) or len(reviewers) != 2:
        raise PageAuditError("exactly two independent reviewer declarations are required")
    signed = []
    ids = set()
    moment = _utc_timestamp(manifest["captured_at_utc"], "captured_at_utc")
    for n, reviewer in enumerate(reviewers, 1):
        field = f"reviewers[{n}]"
        _obj(reviewer, field)
        code = reviewer.get("reviewer_code")
        if not isinstance(code, str) or not REVIEWER_CODE.fullmatch(code):
            raise PageAuditError(f"{field}.reviewer_code must be a pseudonymous code")
        if code in ids:
            raise PageAuditError("reviewer codes must be distinct")
        ids.add(code)
        if reviewer.get("declares_independent_blinded_annotation") is not True:
            raise PageAuditError(f"{field} must explicitly declare independent blinded annotation")
        if reviewer.get("complete_visible_row_scan") is not True:
            raise PageAuditError(f"{field} must declare a complete visible-row scan")
        stamp = _utc_timestamp(reviewer.get("reviewed_at_utc"), field + ".reviewed_at_utc")
        if stamp < moment:
            raise PageAuditError(f"{field} was dated before the capture")
        signed.append(_review_rows(reviewer.get("rows"), field))
    if signed[0] != signed[1]:
        a = dict(signed[0])
        b = dict(signed[1])
        disagreement_ranks = sorted(k for k in a.keys() | b.keys() if a.get(k) != b.get(k))
        return None, disagreement_ranks
    return signed[0], []


def _score(predictions, gold):
    predicted = {(i, name.casefold()) for i, name in enumerate(predictions, 1)}
    expected = set(gold)
    tp = len(predicted & expected)
    fp = len(predicted - expected)
    fn = len(expected - predicted)
    p_by_name = {name: rank for rank, name in predicted}
    g_by_name = {name: rank for rank, name in expected}
    wrong_rank = sum(
        p_by_name[name] != g_by_name[name] for name in p_by_name.keys() & g_by_name.keys()
    )
    return {
        "true_positive_ranked_rows": tp,
        "false_positive_ranked_rows": fp,
        "false_negative_ranked_rows": fn,
        "wrong_rank_for_shared_identity": wrong_rank,
        "audited_page_precision": tp / (tp + fp) if tp + fp else None,
        "audited_page_recall": tp / (tp + fn) if tp + fn else None,
    }


def audit(index_path, *, synthetic=False):
    index_path = Path(index_path).resolve()
    index, index_hash = _json(index_path)
    _obj(index, "audit index")
    if index.get("schema_version") != AUDIT_VERSION:
        raise PageAuditError("unsupported index schema")
    pages = index.get("pages")
    if not isinstance(pages, list) or not pages:
        raise PageAuditError("audit index must list at least one captured page")
    if len(pages) > 300:
        raise PageAuditError("maximum 300 pages per local audit")
    base = index_path.parent
    processed = []
    all_inputs = [index_path]
    unique_captures = set()
    totals = dict(
        compared_pages=0,
        unresolved_reviewer_pages=0,
        parser_failed_pages=0,
        audited_gold_rows=0,
        true_positive_ranked_rows=0,
        false_positive_ranked_rows=0,
        false_negative_ranked_rows=0,
        wrong_rank_for_shared_identity=0,
    )
    compared_windows = set()
    for n, item in enumerate(pages, 1):
        _obj(item, f"pages[{n}]")
        raw_file = _contained_path(base, item.get("raw_file"), f"pages[{n}].raw_file")
        manifest_file = _contained_path(base, item.get("manifest_file"), f"pages[{n}].manifest_file")
        annotation_file = _contained_path(base, item.get("annotation_file"), f"pages[{n}].annotation_file")
        if len({raw_file, manifest_file, annotation_file}) != 3:
            raise PageAuditError("raw, manifest and annotation must be distinct files")
        all_inputs.extend((raw_file, manifest_file, annotation_file))
        manifest, manifest_hash = _json(manifest_file)
        _obj(manifest, "capture manifest")
        raw = raw_file.read_bytes()
        # Critical: validate_capture checks timestamp, URL, HTTP status, byte
        # count, SHA and UTF-8 BEFORE calling the structural parser.
        try:
            rows, internal_audit = validate_capture(
                raw, manifest, extract_repos=extract_repos,
                inspect_structure=inspect_trending_structure
            )
            predictions = [row["repository"] for row in rows]
            parser_status = "parsed_supported_layout"
            parser_error = None
        except PilotValidationError:
            raise
        except ValueError as exc:
            # This is a checked-provenance page with an unusable parser result,
            # not a zero-row page. Count every agreed visible row as missed.
            predictions = []
            parser_status = "failed_closed"
            parser_error = str(exc)[:250]
        key = (manifest["source_sha256"], manifest["source_url"], manifest["captured_at_utc"])
        if key in unique_captures:
            raise PageAuditError("same recorded capture included twice in audit")
        unique_captures.add(key)
        annotation, annotation_hash = _json(annotation_file)
        gold, differences = _annotated_gold(annotation, manifest)
        page_result = {
            "source_sha256": manifest["source_sha256"],
            "source_manifest_sha256": manifest_hash,
            "annotation_sha256": annotation_hash,
            "source_url": manifest["source_url"],
            "captured_at_utc": manifest["captured_at_utc"],
            "window": manifest["window"],
            "parser_status": parser_status,
            "parser_error": parser_error,
            "annotation_status": "two_declarations_agree" if gold is not None else "unresolved_reviewer_disagreement",
            "reviewer_disagreement_ranks": differences,
            "quality_status": "requires_external_review",
            "predicted_rows": len(predictions) if parser_status != "failed_closed" else 0,
            "agreed_gold_rows": len(gold) if gold is not None else None,
        }
        if gold is None:
            totals["unresolved_reviewer_pages"] += 1
            page_result["comparison"] = None
        else:
            totals["compared_pages"] += 1
            totals["audited_gold_rows"] += len(gold)
            compared_windows.add(manifest["window"])
            result = _score(predictions, gold)
            page_result["comparison"] = result
            for field in ("true_positive_ranked_rows", "false_positive_ranked_rows",
                          "false_negative_ranked_rows", "wrong_rank_for_shared_identity"):
                totals[field] += result[field]
            if parser_status == "failed_closed":
                totals["parser_failed_pages"] += 1
        processed.append(page_result)
    tp = totals["true_positive_ranked_rows"]
    fp = totals["false_positive_ranked_rows"]
    fn = totals["false_negative_ranked_rows"]
    coverage_floor = (
        len(processed) == totals["compared_pages"]
        and totals["audited_gold_rows"] >= 30
        and set(WINDOWS).issubset(compared_windows)
    )
    exact_match = (
        coverage_floor and fp == 0 and fn == 0 and totals["parser_failed_pages"] == 0
    )
    return {
        "schema_version": AUDIT_VERSION,
        "analysis_name": "github_trending_independent_page_qa",
        "analysis_status": "SYNTHETIC_FIXTURE" if synthetic else "UNVERIFIED_HUMAN_DECLARATIONS",
        "readiness": "requires_independent_review_and_source_access_approval",
        "index_sha256": index_hash,
        "page_count": len(processed),
        "pages": processed,
        "counts": totals,
        "compared_windows": sorted(compared_windows),
        "micro_precision_within_agreed_audit_frame": tp / (tp + fp) if tp + fp else None,
        "micro_recall_within_agreed_audit_frame": tp / (tp + fn) if tp + fn else None,
        "minimum_30_rows_three_unfiltered_windows_met": coverage_floor,
        "operational_exact_match_in_agreed_audit_frame": exact_match,
        "language_panel_audit_status": "not_supported_or_tested",
        "interpretation": [
            "Two reviewer records and blind/full-coverage declarations are self-reported; this CLI cannot authenticate humans or independent visual inspection.",
            "Per-row precision/recall apply ONLY to agreed annotated pages; unresolved disagreements are excluded and reported, not treated as negatives.",
            "An unusable parser produces no output: all agreed visible rows are operational false negatives, with precision undefined.",
            "The >=30-row rule is a minimum audit floor, not a confidence interval, representative sample, proof of capture authorization, or permission to enroll.",
            "No inferential CI is calculated because pages are convenience sampled and rows clustered; document per-page uncertainty and source coverage.",
            "Only unfiltered global daily/weekly/monthly pages are supported; separately validate language surfaces before using them.",
            "A checked SHA256 is local integrity evidence, not cryptographic attestation of GitHub-origin or the human labels.",
        ],
    }, all_inputs


def markdown_report(report):
    c = report["counts"]
    lines = [
        "# GitHub Trending page parser: independent-annotation audit",
        "",
        "**" + report["analysis_status"] + " — NOT SCIENTIFIC SIGNOFF**",
        "",
        "| Field | Observed in supplied audit |",
        "|---|---:|",
    ]
    for k, v in c.items():
        lines.append(f"| {k.replace('_', ' ')} | {v} |")
    lines.extend([
        f"| Audited-frame precision | {report['micro_precision_within_agreed_audit_frame'] if report['micro_precision_within_agreed_audit_frame'] is not None else 'UNDEFINED'} |",
        f"| Audited-frame recall | {report['micro_recall_within_agreed_audit_frame'] if report['micro_recall_within_agreed_audit_frame'] is not None else 'UNDEFINED'} |",
        f"| >=30 rows across all 3 global windows | {report['minimum_30_rows_three_unfiltered_windows_met']} |",
        "| Independently verified GitHub capture and human review | NOT VERIFIED |",
        "| Language pages | NOT TESTED |",
        "",
        "## Per-capture evidence and error denominators",
        "",
        "| Capture SHA prefix | Window | Parser | Agreement | Visible rows | TP | FP | FN |",
        "|---|---|---|---|---:|---:|---:|---:|",
    ])
    for p in report["pages"]:
        m = p["comparison"] or {}
        value = lambda field: str(m[field]) if field in m else "—"
        lines.append(
            f"| {p['source_sha256'][:12]} | {p['window']} | {p['parser_status']} | "
            f"{p['annotation_status']} | {p['agreed_gold_rows'] if p['agreed_gold_rows'] is not None else 'UNRESOLVED'} "
            f"| {value('true_positive_ranked_rows')} | {value('false_positive_ranked_rows')} "
            f"| {value('false_negative_ranked_rows')} |"
        )
    lines.extend([
        "",
        "## Interpretation limitations",
        "",
        *("- " + limitation for limitation in report["interpretation"]),
        "",
        "The review and source-access gates remain open even if descriptive matches are perfect.",
        "",
    ])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline independent-annotation Trending parser QA (no enrollment)")
    parser.add_argument("--index", required=True, help="JSON index with raw/manifest/two-reviewer annotation files")
    parser.add_argument("--output", required=True, help="new write-once JSON audit report")
    parser.add_argument("--markdown", help="optional new write-once human-readable audit table")
    parser.add_argument("--synthetic", action="store_true", help="mark demonstration with synthetic annotations")
    args = parser.parse_args(argv)
    report, inputs = audit(args.index, synthetic=args.synthetic)
    disjoint(*inputs, args.output, args.markdown)
    refuse_existing(args.output, args.markdown)
    artifacts = [(args.output, (json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8"))]
    if args.markdown:
        artifacts.append((args.markdown, markdown_report(report).encode("utf-8")))
    publish_once(artifacts)
    print(json.dumps({
        "analysis_status": report["analysis_status"],
        "audited_pages": report["page_count"],
        "compared_pages": report["counts"]["compared_pages"],
        "minimum_coverage_floor_met": report["minimum_30_rows_three_unfiltered_windows_met"],
        "readiness": report["readiness"],
    }, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, PilotValidationError) as exc:
        sys.exit(f"error: {exc}")
