"""Blind two-reviewer page QA against locally hashed capture manifests.

The *reviewers*, not this program, must inspect each captured page independently
and annotate all visible repository rows. Input attestations are self-reported:
automated agreement never constitutes validated GitHub data or study approval.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from .pilot import _utc_timestamp, validate_manifest_integrity

AUDIT_VERSION = "1.0"
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
WINDOWS = ("daily", "weekly", "monthly")


class PageAuditError(ValueError):
    """Invalid reference, duplicate capture, impossible label, or source data."""


def _object(value, name):
    if not isinstance(value, dict):
        raise PageAuditError(f"{name} must be an object")
    return value


def _name(value, label):
    if not isinstance(value, str) or not value.strip():
        raise PageAuditError(f"{label} must be nonempty text")
    return value.strip()


def _labels(annotation, manifest, moment):
    _object(annotation, "reviewer annotation")
    if annotation.get("schema_version") != AUDIT_VERSION:
        raise PageAuditError("reviewer schema must be 1.0")
    reviewer = _name(annotation.get("reviewer_id"), "reviewer_id")
    if annotation.get("blind_to_parser_output") is not True:
        raise PageAuditError("reviewer must attest blind annotation before parser comparison")
    stamp = _utc_timestamp(annotation.get("reviewed_at_utc"), "reviewed_at_utc")
    if stamp < moment:
        raise PageAuditError("reviewed_at_utc predates the original capture")
    for field in ("source_sha256", "source_url", "captured_at_utc", "window"):
        if annotation.get(field) != manifest.get(field):
            raise PageAuditError(f"reviewer annotation {field} disagrees with capture manifest")
    lines = annotation.get("rows")
    if not isinstance(lines, list) or not lines:
        raise PageAuditError("reviewer must enumerate every visible row, including first and last")
    result = []
    seen = set()
    for expected_rank, entry in enumerate(lines, 1):
        _object(entry, "reviewer row")
        rank = entry.get("rank")
        if isinstance(rank, bool) or not isinstance(rank, int) or rank != expected_rank:
            raise PageAuditError("reviewer row ranks must be contiguous, ordered, and 1-based")
        repo = _name(entry.get("repository"), "row.repository")
        if not REPO.fullmatch(repo) or any(part in (".", "..") for part in repo.split("/")):
            raise PageAuditError(f"invalid canonical owner/repo label at row {rank}")
        if repo.casefold() in seen:
            raise PageAuditError("duplicate repository in human annotation")
        seen.add(repo.casefold())
        result.append(repo)
    return reviewer, result


def _score(gold, predicted):
    matched = sum(a == b for a, b in zip(gold, predicted))
    # Rank plus identity must both be equal; a wrong rank is FP and FN.
    return {
        "gold_rows": len(gold),
        "emitted_rows": len(predicted),
        "correct_identity_at_rank": matched,
        "false_positives_including_rank_errors": len(predicted) - matched,
        "false_negatives_including_rank_errors": len(gold) - matched,
        "precision_on_emitted_rows": matched / len(predicted) if predicted else None,
        "effective_rank_recall": matched / len(gold),
        "mismatched_ranks": [
            i for i in range(1, max(len(gold), len(predicted)) + 1)
            if (gold[i - 1] if i <= len(gold) else None)
            != (predicted[i - 1] if i <= len(predicted) else None)
        ],
    }


def _adjudicated_reference(annotations, manifest, moment, left_id, right_id,
                          left, right, disputed, adjudicator):
    """Validate optional C review without changing already agreed A/B ranks.

    This checks a self-reported record, not whether three humans are independent.
    Existing A/B labels are never rewritten, and an extra C label is not permitted
    to manufacture rows that neither A nor B disputed.
    """
    if not disputed:
        raise PageAuditError("adjudication is only allowed when A/B disagree")
    _object(adjudicator, "adjudicator annotation")
    declared = adjudicator.get("disagreement_ranks")
    if (not isinstance(declared, list) or
            any(type(rank) is not int for rank in declared) or
            declared != disputed):
        raise PageAuditError("adjudicator must list the exact disputed A/B ranks")
    reason = adjudicator.get("adjudication_reason")
    if not isinstance(reason, str) or not reason.strip() or len(reason) > 500:
        raise PageAuditError("adjudication_reason must be 1..500 characters")
    c_id, c_rows = _labels(adjudicator, manifest, moment)
    if c_id.casefold() in (left_id.casefold(), right_id.casefold()):
        raise PageAuditError("adjudicator ID must differ from both A/B reviewer IDs")
    c_time = _utc_timestamp(adjudicator.get("reviewed_at_utc"),
                            "adjudicator reviewed_at_utc")
    a_time = _utc_timestamp(annotations[0].get("reviewed_at_utc"),
                            "reviewer A reviewed_at_utc")
    b_time = _utc_timestamp(annotations[1].get("reviewed_at_utc"),
                            "reviewer B reviewed_at_utc")
    if c_time <= max(a_time, b_time):
        raise PageAuditError("adjudication must be recorded after both A/B reviews")
    for i in range(max(len(left), len(right), len(c_rows))):
        a = left[i] if i < len(left) else None
        b = right[i] if i < len(right) else None
        c = c_rows[i] if i < len(c_rows) else None
        if a == b and c != a:
            raise PageAuditError("adjudicator cannot change an agreed A/B rank")
    return c_id, c_rows


def assess_page(raw, manifest, annotations, *, extract_repos, adjudicator=None):
    """Return comparison, never a scientific signoff."""
    window, url, moment, digest, html = validate_manifest_integrity(raw, manifest)
    if not isinstance(annotations, list) or len(annotations) != 2:
        raise PageAuditError("two independent, separate reviewer annotation records are required")
    left_id, left = _labels(annotations[0], manifest, moment)
    right_id, right = _labels(annotations[1], manifest, moment)
    if left_id.casefold() == right_id.casefold():
        raise PageAuditError("two distinct reviewer IDs are required")
    disagreement_ranks = [
        i for i in range(1, max(len(left), len(right)) + 1)
        if (left[i - 1] if i <= len(left) else None)
        != (right[i - 1] if i <= len(right) else None)
    ]
    result = {
        "window": window,
        "source_url": url,
        "captured_at_utc": moment.isoformat(),
        "source_sha256": digest,
        "reviewer_ids": [left_id, right_id],
        "reviewer_a_count": len(left),
        "reviewer_b_count": len(right),
        "reviewer_agreement": left == right,
        "annotation_disagreement_ranks": disagreement_ranks,
        "reference_resolution": ("a_b_agreement" if left == right else "unresolved"),
        "adjudicator_id": None,
        "adjudicated_disagreement_ranks": [],
        "labels_resolved": left == right,
        "eligible_for_confirmatory_cohort": False,
    }
    gold = left
    if adjudicator is not None:
        c_id, gold = _adjudicated_reference(
            annotations, manifest, moment, left_id, right_id,
            left, right, disagreement_ranks, adjudicator,
        )
        result.update({
            "reference_resolution": "c_adjudicated",
            "adjudicator_id": c_id,
            "adjudicated_disagreement_ranks": disagreement_ranks,
            "labels_resolved": True,
        })
    if not result["labels_resolved"]:
        result.update({
            "page_status": "unresolved_reviewer_disagreement",
            "parser_status": "not_scored_awaiting_independent_adjudication",
            "gold_rows": None,
            "emitted_rows": None,
            "correct_identity_at_rank": None,
            "precision_on_emitted_rows": None,
            "effective_rank_recall": None,
        })
        return result
    try:
        predicted = extract_repos(html)
        if not isinstance(predicted, list):
            raise PageAuditError("extract_repos must produce a list")
    except ValueError as exc:
        result.update({
            "page_status": "parser_rejected_capture",
            "parser_status": "rejected",
            "parser_error": str(exc)[:800],
            **_score(gold, []),
        })
        return result
    result.update(_score(gold, predicted))
    result.update({
        "page_status": ("exact_rank_identity_agreement" if predicted == gold
                        else "detected_missing_or_wrong_rows"),
        "parser_status": "emitted",
    })
    return result


def assess_bundle(bundle, *, loader, extract_repos, min_rows=30):
    """Score captured pages with two separately attested complete-page labels.

    loader receives a path from each entry and returns bytes; the CLI resolves
    paths against the bundle's own directory.
    """
    _object(bundle, "audit bundle")
    if bundle.get("schema_version") != AUDIT_VERSION:
        raise PageAuditError("audit bundle schema must be 1.0")
    kind = bundle.get("evidence_kind")
    if kind not in ("synthetic_fixture", "field_self_reported"):
        raise PageAuditError("evidence_kind must be synthetic_fixture or field_self_reported")
    if isinstance(min_rows, bool) or not isinstance(min_rows, int) or min_rows < 30:
        raise PageAuditError("min_rows cannot be below the 30-row pilot QA minimum")
    entries = bundle.get("pages")
    if not isinstance(entries, list) or not entries:
        raise PageAuditError("pages must be a nonempty list")
    seen_captures = set()
    pages = []
    for i, p in enumerate(entries, 1):
        _object(p, f"pages[{i}]")
        raw_path = _name(p.get("raw_path"), "raw_path")
        manifest_path = _name(p.get("manifest_path"), "manifest_path")
        raw = loader(raw_path)
        manifest = json.loads(loader(manifest_path).decode("utf-8"))
        if not isinstance(raw, bytes):
            raise PageAuditError("loader must return raw bytes")
        page = assess_page(raw, manifest, p.get("reviewers"), extract_repos=extract_repos,
                           adjudicator=p.get("adjudicator"))
        key = (page["source_sha256"], page["source_url"], page["captured_at_utc"])
        if key in seen_captures:
            raise PageAuditError("duplicate capture included more than once")
        seen_captures.add(key)
        page["page_number"] = i
        page["raw_path"] = raw_path
        page["manifest_path"] = manifest_path
        pages.append(page)
    agreed = [p for p in pages if p["reviewer_agreement"]]
    resolved = [p for p in pages if p["labels_resolved"]]
    scored = [p for p in resolved if p["gold_rows"] is not None]
    total_gold = sum(p["gold_rows"] for p in scored)
    total_tp = sum(p["correct_identity_at_rank"] for p in scored)
    total_emitted = sum(p["emitted_rows"] for p in scored)
    unresolved = len(pages) - len(resolved)
    windows = sorted({p["window"] for p in agreed})
    resolved_windows = sorted({p["window"] for p in resolved})
    same_all = (unresolved == 0 and all(
        p["page_status"] == "exact_rank_identity_agreement" for p in pages
    ))
    threshold_met = total_gold >= min_rows and set(WINDOWS).issubset(resolved_windows)
    documentary_ready = same_all and threshold_met
    return {
        "schema_version": AUDIT_VERSION,
        "evidence_kind": kind,
        "audit_generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "pages_supplied": len(pages),
        "pages_with_agreed_annotations": len(agreed),
        "pages_with_adjudicated_annotations": sum(
            p["reference_resolution"] == "c_adjudicated" for p in pages
        ),
        "pages_with_resolved_annotations": len(resolved),
        "pages_with_unresolved_annotation_disagreements": unresolved,
        "pages_parser_rejected": sum(p["parser_status"] == "rejected" for p in resolved),
        "windows_with_agreed_labels": windows,
        "windows_with_resolved_labels": resolved_windows,
        "audited_gold_rows": total_gold,
        "correct_identity_at_rank": total_tp,
        "emitted_rows": total_emitted,
        "false_positives_including_rank_errors": total_emitted - total_tp,
        "false_negatives_including_rank_errors": total_gold - total_tp,
        "precision_on_emitted_rows": total_tp / total_emitted if total_emitted else None,
        "effective_rank_recall_including_parser_abstentions": total_tp / total_gold if total_gold else None,
        "coverage_minimum_rows": min_rows,
        "coverage_minimum_met": threshold_met,
        "all_pages_exactly_matched": same_all,
        "automated_documentary_check": "pass" if documentary_ready else "blocked",
        "scientific_status": ("synthetic_only_not_empirical_evidence" if kind == "synthetic_fixture"
                              else "self_reported_requires_independent_human_and_source_review"),
        "eligible_for_confirmatory_cohort": False,
        "limitations": (
            "All labels and reviewer independence are self-reported and NOT verified by this program; "
            "capture SHA is not GitHub attestation. Page-specific nonrandom QA cannot establish "
            "population recall or validate an unimplemented language filter. Two-reviewer agreement "
            "does not establish human independence or correctness; a proposed C adjudication is " 
            "also self-reported, never proof of independent review. A research lead must authenticate "
            "original captures, annotation method, platform permission and disagreements."
        ),
        "pages": pages,
    }


def markdown_report(report):
    """Render only derived, safe aggregate figures; never human-review attestations.

    The Markdown is a derivative view of the canonical versioned JSON report.
    Do not include free-form source URLs, paths or reviewer notes in a report
    intended for easy copying/sharing.
    """
    def cell(value):
        if value is None:
            return "unresolved"
        if isinstance(value, bool):
            return "yes" if value else "no"
        if isinstance(value, float):
            return f"{value:.4f}"
        return str(value)

    totals = [
        ("Evidence kind", report["evidence_kind"]),
        ("Scientific status", report["scientific_status"]),
        ("Pages submitted", report["pages_supplied"]),
        ("Pages with A/B agreement", report["pages_with_agreed_annotations"]),
        ("Pages resolved by C", report["pages_with_adjudicated_annotations"]),
        ("Unresolved pages", report["pages_with_unresolved_annotation_disagreements"]),
        ("Gold rows on resolved pages", report["audited_gold_rows"]),
        ("Exact rank and identity matches", report["correct_identity_at_rank"]),
        ("False positives incl. rank errors", report["false_positives_including_rank_errors"]),
        ("False negatives incl. rank errors", report["false_negatives_including_rank_errors"]),
        ("Precision of emitted rows", report["precision_on_emitted_rows"]),
        ("Effective rank recall incl. rejections", report["effective_rank_recall_including_parser_abstentions"]),
        ("30-row/three-window coverage", report["coverage_minimum_met"]),
        ("Automated documentary check", report["automated_documentary_check"]),
        ("Confirmatory cohort eligible", False),
    ]
    lines = [
        "# Offline Trending page-QA review summary",
        "",
        "**Evidence is self-reported or synthetic, not authenticated by this tool.** "
        "A documentary pass is neither permission to collect GitHub pages nor "
        "independent human review, preregistration or cohort eligibility.",
        "",
        "| Field | Derived result |", "|---|---|",
    ]
    lines.extend(f"| {label} | {cell(value)} |" for label, value in totals)
    lines.extend([
        "",
        "## Page-level disposition",
        "",
        "| Page | Window | A/B agree | Reference | Gold rows | Emitted | Matched ranks | Status |",
        "|---:|---|---|---|---:|---:|---:|---|",
    ])
    for page in report["pages"]:
        lines.append(
            f"| {cell(page['page_number'])} | {cell(page['window'])} | "
            f"{cell(page['reviewer_agreement'])} | {cell(page['reference_resolution'])} | "
            f"{cell(page['gold_rows'])} | {cell(page['emitted_rows'])} | "
            f"{cell(page['correct_identity_at_rank'])} | {cell(page['page_status'])} |"
        )
    lines.extend([
        "",
        "Unresolved A/B disagreement remains unscored; a valid C decision is "
        "only a *documentary* resolution of disputed ranks. This Markdown "
        "is not a second report schema; preserve the write-once JSON source of truth.",
        "",
    ])
    return "\n".join(lines)


def audit_bundle_file(path, *, extract_repos, min_rows=30):
    path = Path(path)
    bundle = json.loads(path.read_text(encoding="utf-8"))
    root = path.parent.resolve()
    def read(name):
        # Bundle paths are local descendants of the audit directory. Prevent
        # untrusted input from reading arbitrary files through '..' or links.
        if not isinstance(name, str) or not name.strip():
            raise PageAuditError("bundle file path must be nonempty text")
        candidate = Path(name)
        if candidate.is_absolute():
            raise PageAuditError("absolute capture paths are not allowed in audit bundle")
        resolved = (root / candidate).resolve(strict=True)
        if not resolved.is_relative_to(root):
            raise PageAuditError("audit bundle path escapes the audit directory")
        if resolved.stat().st_size > 4_000_000:
            raise PageAuditError("audit input exceeds 4MB maximum")
        return resolved.read_bytes()
    return assess_bundle(bundle, loader=read, extract_repos=extract_repos, min_rows=min_rows)
