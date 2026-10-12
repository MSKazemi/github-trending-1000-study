"""Offline pre-search issue screening preparation and conservative two-reviewer audit.

Structural safeguards only: submitted labels, timestamps and reviewer identities
are NOT independent human verification or permission for experimental enrollment.
The public source issue may already contain patch hints or complete solutions.
"""
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re

from .safe_io import disjoint, publish_json
from .task_intake import IntakeError, sample, utc


SCHEMA = "1.0"
RECHECK_KIND = "public_issue_metadata_recheck"
PACKET_KIND = "pre_search_task_screen_packet"
LABELS = {"screenable_for_spec_drafting", "exclude_candidate", "defer_unknown"}
REASONS = {"none", "unsafe", "rights", "scope", "underspecified", "nonreproducible",
           "leakage", "duplicate", "unknown", "other"}
LEAKAGE = {"suspected", "not_observed", "unknown"}
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
HASH = re.compile(r"[0-9a-f]{64}\Z")


class TaskScreenError(ValueError):
    """An issue screening artifact cannot be safely reconciled."""


def fingerprint(value):
    """SHA-256 of canonical UTF-8 JSON; independent of input file formatting."""
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _exact(value, keys, context):
    if not isinstance(value, dict) or set(value) != keys:
        raise TaskScreenError(f"{context}: unexpected/missing fields")


def _utc(value, context):
    try:
        return utc(value)
    except IntakeError as exc:
        raise TaskScreenError(f"{context}: {exc}") from exc


def _string(value, context, maxlen=512):
    if not isinstance(value, str) or not value.strip() or len(value) > maxlen:
        raise TaskScreenError(f"{context}: expected bounded nonempty text")
    if "\n" in value or "\r" in value:
        raise TaskScreenError(f"{context}: no multiline/private text")
    return value


def _selected(frame):
    try:
        sampled = sample(frame)
    except (IntakeError, KeyError, TypeError) as exc:
        raise TaskScreenError(f"invalid intake frame: {exc}") from exc
    selected = {
        row["task_id"]: row for row in sampled["ledger"]
        if row["selection_status"] == "selected_for_independent_task_screen"
    }
    source = {}
    for group in frame["sources"]:
        for issue in group["issues"]:
            key = f"GH-{issue['id']}"
            if key in selected:
                source[key] = issue
    if not selected or set(source) != set(selected):
        raise TaskScreenError("missing selected issue metadata")
    return sampled, selected, source


def validate_recheck(frame, recheck):
    """Check a later *reported* REST metadata observation against the frozen intake."""
    sampled, selected, originals = _selected(frame)
    _exact(recheck, {"schema_version", "dataset_kind", "source_frame_sha256",
                     "rechecked_at_utc", "source_method", "records"}, "recheck")
    if recheck["schema_version"] != SCHEMA or recheck["dataset_kind"] != RECHECK_KIND:
        raise TaskScreenError("recheck: wrong schema/kind")
    if recheck["source_frame_sha256"] != sampled["reduced_frame_sha256"]:
        raise TaskScreenError("recheck: intake checksum mismatch")
    timestamp = _utc(recheck["rechecked_at_utc"], "rechecked_at_utc")
    if timestamp < _utc(frame["captured_at_utc"], "captured_at_utc"):
        raise TaskScreenError("recheck: performed before original intake")
    if timestamp > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise TaskScreenError("recheck: future timestamp")
    _string(recheck["source_method"], "source_method")
    rows = recheck["records"]
    if not isinstance(rows, list):
        raise TaskScreenError("recheck.records must be an array")
    seen = {}
    for row in rows:
        _exact(row, {"task_id", "issue_id", "source_url", "fetch_status", "state",
                     "updated_at_utc", "closed_at_utc", "source_error"}, "recheck row")
        tid = row["task_id"]
        if not isinstance(tid, str) or tid not in selected or tid in seen:
            raise TaskScreenError("recheck: unexpected or duplicate selected task ID")
        original = originals[tid]
        if type(row["issue_id"]) is not int or row["issue_id"] != original["id"]:
            raise TaskScreenError(f"{tid}: issue ID mismatch")
        if row["source_url"] != selected[tid]["source_url"]:
            raise TaskScreenError(f"{tid}: issue URL mismatch")
        if row["fetch_status"] == "observed":
            if row["state"] not in ("open", "closed") or row["source_error"] is not None:
                raise TaskScreenError(f"{tid}: inconsistent observed status")
            updated = _utc(row["updated_at_utc"], f"{tid}.updated_at_utc")
            if updated < _utc(original["updated_at_utc"], f"{tid}.original_update"):
                raise TaskScreenError(f"{tid}: updated timestamp moved backwards")
            if updated > timestamp:
                raise TaskScreenError(f"{tid}: updated after recheck")
            closed = row["closed_at_utc"]
            if row["state"] == "open" and closed is not None:
                raise TaskScreenError(f"{tid}: open issue cannot have closed_at_utc")
            if row["state"] == "closed":
                closure = _utc(closed, f"{tid}.closed_at_utc")
                if closure < _utc(frame["captured_at_utc"], "captured_at_utc") or closure > timestamp:
                    raise TaskScreenError(f"{tid}: incompatible closure date")
        elif row["fetch_status"] == "unavailable":
            if (row["state"] != "unknown" or row["updated_at_utc"] is not None or
                    row["closed_at_utc"] is not None or
                    row["source_error"] not in ("not_found", "access_denied", "rate_limited", "fetch_error")):
                raise TaskScreenError(f"{tid}: unavailable must remain unknown")
        else:
            raise TaskScreenError(f"{tid}: invalid fetch status")
        seen[tid] = row
    if set(seen) != set(selected):
        raise TaskScreenError(f"recheck: incomplete selected set; missing {sorted(set(selected)-set(seen))}")
    return sampled, selected, originals, seen


def prepare(frame, recheck):
    """Build a frozen-identity reviewer packet, NOT a human review or accepted task."""
    sampled, selected, originals, checked = validate_recheck(frame, recheck)
    entries = []
    for tid in sorted(selected):
        info, source, later = selected[tid], originals[tid], checked[tid]
        changed = (later["fetch_status"] == "observed" and
                   _utc(later["updated_at_utc"], "rechecked_update") >
                   _utc(source["updated_at_utc"], "initial_update"))
        entries.append({
            "task_id": tid, "repository": info["repository"],
            "issue_id": info["issue_id"], "issue_number": info["issue_number"],
            "source_url": info["source_url"],
            "initial_updated_at_utc": source["updated_at_utc"],
            "recheck_fetch_status": later["fetch_status"],
            "recheck_issue_state": later["state"],
            "metadata_updated_since_intake": changed if later["fetch_status"] == "observed" else None,
            "review_state": "unreviewed",
            "reuse_opportunity": "unknown",
            "task_acceptance": "not_frozen",
        })
    result = {"schema_version": SCHEMA, "dataset_kind": PACKET_KIND,
              "source_frame_sha256": sampled["reduced_frame_sha256"],
              "source_recheck_sha256": fingerprint(recheck),
              "captured_at_utc": frame["captured_at_utc"],
              "rechecked_at_utc": recheck["rechecked_at_utc"],
              "selected_count": len(entries), "candidates": entries,
              "human_independence_verified": False,
              "experiment_enrollment": "blocked",
              "warning": "Packet preparation and API metadata do not establish task suitability, "
                         "independent human review, absent solution leakage, consent, or gold tests."}
    result["packet_sha256"] = fingerprint(result)
    return result


def _submission(packet, submission, slot):
    _exact(submission, {"schema_version", "packet_sha256", "reviewer_slot",
                        "reviewer_ref", "reviewed_at_utc", "decisions"}, f"review {slot}")
    if (submission["schema_version"] != SCHEMA or
            submission["packet_sha256"] != packet["packet_sha256"] or
            submission["reviewer_slot"] != slot):
        raise TaskScreenError(f"review {slot}: packet/version/slot mismatch")
    reviewer = _string(submission["reviewer_ref"], f"reviewer {slot}", 80)
    if not IDENTIFIER.fullmatch(reviewer) or reviewer.casefold() == "unknown":
        raise TaskScreenError(f"review {slot}: invalid pseudonymous reviewer ref")
    timestamp = _utc(submission["reviewed_at_utc"], f"review {slot} UTC")
    if timestamp < _utc(packet["rechecked_at_utc"], "recheck UTC"):
        raise TaskScreenError(f"review {slot}: backdated before metadata recheck")
    if timestamp > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise TaskScreenError(f"review {slot}: future review")
    if not isinstance(submission["decisions"], list):
        raise TaskScreenError(f"review {slot}: decisions must be an array")
    expected = {candidate["task_id"] for candidate in packet["candidates"]}
    observations = {}
    for row in submission["decisions"]:
        _exact(row, {"task_id", "label", "reason_code", "leakage_signal",
                     "issue_status_check", "evidence_ref"}, f"review {slot} decision")
        tid = row["task_id"]
        if not isinstance(tid, str) or tid not in expected or tid in observations:
            raise TaskScreenError(f"review {slot}: unexpected or duplicate task ID")
        label, reason = row["label"], row["reason_code"]
        if label not in LABELS or reason not in REASONS:
            raise TaskScreenError(f"review {slot}: invalid decision/reason")
        if label == "screenable_for_spec_drafting" and reason != "none":
            raise TaskScreenError(f"review {slot}: screenable cannot have exclusion reason")
        if label == "exclude_candidate" and reason in ("none", "unknown"):
            raise TaskScreenError(f"review {slot}: exclusion requires evidence-based reason")
        if label == "defer_unknown" and reason == "none":
            raise TaskScreenError(f"review {slot}: defer must disclose unknown/other reason")
        if row["leakage_signal"] not in LEAKAGE:
            raise TaskScreenError(f"review {slot}: invalid leakage indicator")
        if row["issue_status_check"] not in ("open", "closed", "unavailable", "unknown"):
            raise TaskScreenError(f"review {slot}: invalid issue status")
        if label == "screenable_for_spec_drafting" and row["issue_status_check"] == "unavailable":
            raise TaskScreenError(f"review {slot}: unavailable issue cannot be screened in")
        if row["evidence_ref"] is not None:
            _string(row["evidence_ref"], f"review {slot} evidence ref", 512)
        elif label != "defer_unknown":
            raise TaskScreenError(f"review {slot}: non-unknown decision requires evidence ref")
        observations[tid] = row
    return reviewer, timestamp, observations


def audit(frame, recheck, review_a, review_b, adjudication=None):
    """Audit supplied reports, never attest that reviewers are real or independent."""
    packet = prepare(frame, recheck)
    ra, time_a, a = _submission(packet, review_a, "A")
    rb, time_b, b = _submission(packet, review_b, "B")
    if ra.casefold() == rb.casefold():
        raise TaskScreenError("distinct independent reviewer references required")
    if adjudication is not None:
        rc, time_c, c = _submission(packet, adjudication, "C")
        if (rc.casefold() in (ra.casefold(), rb.casefold())
                or time_c <= max(time_a, time_b)):
            raise TaskScreenError("adjudicator must be distinct and act strictly after reviews")
    else:
        c = {}
    rows = []
    counts = Counter()
    double = agree = 0
    all_ids = [record["task_id"] for record in packet["candidates"]]
    for tid in all_ids:
        first, second, third = a.get(tid), b.get(tid), c.get(tid)
        if first and second:
            double += 1
            if first["label"] == second["label"]:
                agree += 1
        if third and (not first or not second or first["label"] == second["label"]):
            raise TaskScreenError("adjudication allowed only for two-reviewer label disagreement")
        if first is None or second is None:
            status, label = "missing_independent_review", "defer_unknown"
        elif first["label"] != second["label"]:
            if third:
                status, label = "adjudicated_provisional", third["label"]
            else:
                status, label = "unresolved_disagreement", "defer_unknown"
        elif first["label"] == "defer_unknown":
            status, label = "concordant_unknown", "defer_unknown"
        else:
            status, label = "concordant_provisional", first["label"]
        reported_leakage = [row["leakage_signal"] for row in (first, second, third) if row]
        leakage = ("suspected" if "suspected" in reported_leakage else
                   "not_observed" if reported_leakage and all(x == "not_observed" for x in reported_leakage)
                   else "unknown")
        # Conflicting or unavailable public source status cannot produce a
        # screenable label, even if two unverified reviewer reports agree.
        # Defer rather than exclude: preserve the original sampling denominator.
        candidate = next(item for item in packet["candidates"] if item["task_id"] == tid)
        if label == "screenable_for_spec_drafting" and (
                candidate["recheck_fetch_status"] != "observed"
                or candidate["recheck_issue_state"] != "open"
                or any(report["issue_status_check"] != "open"
                       for report in (first, second, third) if report)):
            status, label = "deferred_source_status", "defer_unknown"
        counts[status] += 1
        rows.append({"task_id": tid, "review_a": first["label"] if first else None,
                     "review_b": second["label"] if second else None,
                     "adjudication": third["label"] if third else None,
                     "screening_status": status, "provisional_label": label,
                     "reported_leakage": leakage, "accepted_task": False,
                     "reuse_opportunity": "unknown"})
    if set(c) - set(all_ids):
        raise TaskScreenError("adjudication refers to non-candidate")
    return {"schema_version": SCHEMA, "dataset_kind": "pre_search_screen_audit",
            "packet_sha256": packet["packet_sha256"], "total_candidates": len(all_ids),
            "double_reviewed": double, "raw_agreement": agree/double if double else None,
            "status_counts": dict(sorted(counts.items())),
            "reported_leakage_suspected": sum(x["reported_leakage"] == "suspected" for x in rows),
            "records": rows, "human_independence_verified": False,
            "task_specs_frozen": False, "accepted_tasks": 0,
            "experimental_enrollment": "blocked",
            "disclaimer": "Supplied reviewer statements are not authenticated human independence, "
                          "verified facts, task acceptance, consent, preregistration or reuse evidence."}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline issue screening, no network calls")
    commands = parser.add_subparsers(dest="command", required=True)
    for cmd in ("prepare", "audit"):
        sub = commands.add_parser(cmd)
        sub.add_argument("--frame", required=True)
        sub.add_argument("--recheck", required=True)
        sub.add_argument("--output", required=True)
        if cmd == "audit":
            sub.add_argument("--review-a", required=True)
            sub.add_argument("--review-b", required=True)
            sub.add_argument("--adjudication")
    args = parser.parse_args(argv)
    try:
        inputs = [args.frame, args.recheck]
        if args.command == "audit":
            inputs.extend([args.review_a, args.review_b, args.adjudication])
        disjoint(*[p for p in inputs if p], args.output)
        frame = json.loads(Path(args.frame).read_text(encoding="utf-8"))
        recheck = json.loads(Path(args.recheck).read_text(encoding="utf-8"))
        if args.command == "prepare":
            output = prepare(frame, recheck)
        else:
            a = json.loads(Path(args.review_a).read_text(encoding="utf-8"))
            b = json.loads(Path(args.review_b).read_text(encoding="utf-8"))
            c = (json.loads(Path(args.adjudication).read_text(encoding="utf-8"))
                 if args.adjudication else None)
            output = audit(frame, recheck, a, b, c)
        publish_json(args.output, output)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps({"dataset_kind": output["dataset_kind"],
                      "count": output.get("selected_count", output.get("total_candidates")),
                      "human_independence_verified": False}))


if __name__ == "__main__":
    main()
