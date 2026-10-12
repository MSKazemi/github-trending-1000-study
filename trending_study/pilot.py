"""Pilot capture provenance and scientific enrollment preflight (stdlib only).

This records user-initiated snapshots and checks internal consistency. A valid
checksum cannot prove that GitHub originally served an alleged page.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

MANIFEST_SCHEMA = "1.0"
MAX_CAPTURE_BYTES = 4_000_000
WINDOWS = ("daily", "weekly", "monthly")
PILOT_GATES = (
    "source_access_review",
    "capture_schedule",
    "capture_manifest_instrumented",
    "parser_audit",
)
CONFIRMATORY_EXTRA_GATES = (
    "stable_identity_resolution",
    "independent_task_frame",
    "task_acceptance_freeze",
    "sample_size_power",
    "privacy_consent",
    "preregistration",
    "independent_methods_review",
)
GATE_STATES = ("pending", "blocked", "verified")


class PilotValidationError(ValueError):
    """A capture or preflight item has invalid, missing or contradictory data."""


def _obj(value, field):
    if not isinstance(value, dict):
        raise PilotValidationError(f"{field} must be an object")
    return value


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise PilotValidationError(f"{field} must be a nonempty string")
    return value.strip()


def _utc_timestamp(value, field):
    s = _text(value, field)
    try:
        parsed = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PilotValidationError(f"{field} must be an ISO8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise PilotValidationError(f"{field} must have a UTC timezone")
    if parsed.utcoffset().total_seconds() != 0:
        raise PilotValidationError(f"{field} must be explicitly UTC")
    return parsed.astimezone(timezone.utc)


def canonical_trending_url(window):
    if window not in WINDOWS:
        raise PilotValidationError("window must be daily, weekly or monthly")
    return "https://github.com/trending?since=" + window


def build_capture_manifest(*, raw, output, window, captured_at_utc,
                           content_type, http_status=200, response_date_header=None):
    """Build metadata at fetch time, before subsequent parsing or enrichment."""
    if not isinstance(raw, bytes) or not (0 < len(raw) <= MAX_CAPTURE_BYTES):
        raise PilotValidationError("raw capture must be 1 byte to 4 MB")
    moment = _utc_timestamp(captured_at_utc, "captured_at_utc")
    if isinstance(http_status, bool) or http_status != 200:
        raise PilotValidationError("only successful HTTP 200 responses may be captured")
    if not isinstance(content_type, str) or "text/html" not in content_type.lower():
        raise PilotValidationError("HTTP content type must be text/html")
    if response_date_header is not None and not isinstance(response_date_header, str):
        raise PilotValidationError("response_date_header must be string or null")
    return {
        "schema_version": MANIFEST_SCHEMA,
        "capture_method": "explicit_cli",
        "source_url": canonical_trending_url(window),
        "window": window,
        "language_filter": None,
        "capture_date_utc": moment.date().isoformat(),
        "captured_at_utc": moment.isoformat(),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "http_status": http_status,
        "content_type": content_type,
        "response_date_header": response_date_header,
        "source_file_at_capture": str(output),
        "provenance_warning": "Client-recorded timestamp and SHA-256, not an authenticated GitHub attestation.",
    }


def validate_manifest_integrity(raw, manifest):
    """Check capture byte integrity and canonical source metadata only.

    Does not authenticate GitHub, prove a timestamp, or validate page layout.
    Kept independent of the parser so human auditing can also inspect rejected
    pages without misclassifying them as successful captures.
    """
    _obj(manifest, "capture manifest")
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise PilotValidationError("unsupported capture manifest schema")
    if manifest.get("capture_method") != "explicit_cli":
        raise PilotValidationError("capture_method must be explicit_cli; manually authored snapshots need separate review")
    window = manifest.get("window")
    expected = canonical_trending_url(window)
    url = _text(manifest.get("source_url"), "source_url")
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.netloc != "github.com" or parts.path != "/trending" or parts.fragment:
        raise PilotValidationError("source_url must be the exact GitHub Trending page")
    query = parse_qs(parts.query)
    if query != {"since": [window]} or url != expected:
        raise PilotValidationError("unsupported source URL/filter; URL must match unfiltered window")
    if manifest.get("language_filter") is not None:
        raise PilotValidationError("language pages need a separately versioned parser/manifest protocol")
    moment = _utc_timestamp(manifest.get("captured_at_utc"), "captured_at_utc")
    if manifest.get("capture_date_utc") != moment.date().isoformat():
        raise PilotValidationError("capture date conflicts with actual UTC capture timestamp")
    if not isinstance(raw, bytes) or not (0 < len(raw) <= MAX_CAPTURE_BYTES):
        raise PilotValidationError("capture bytes must be 1 to 4 MB")
    byte_count = manifest.get("bytes")
    if isinstance(byte_count, bool) or not isinstance(byte_count, int) or byte_count != len(raw):
        raise PilotValidationError("manifest byte count does not match capture")
    digest = hashlib.sha256(raw).hexdigest()
    if manifest.get("source_sha256") != digest:
        raise PilotValidationError("manifest SHA-256 does not match raw capture")
    if manifest.get("http_status") != 200:
        raise PilotValidationError("source HTTP status is not successful")
    if "text/html" not in str(manifest.get("content_type", "")).lower():
        raise PilotValidationError("capture is not declared HTML")
    try:
        html = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise PilotValidationError("non-UTF-8 HTML cannot be parsed safely") from exc
    return window, url, moment, digest, html


def validate_capture(raw, manifest, *, extract_repos, inspect_structure=None):
    """Validate a local capture and return rows with capture and parse time separated.

    Does not independently authenticate the remote origin or sample eligibility.
    Only unfiltered /trending?since=... pages are supported in this first pilot.
    """
    window, url, moment, digest, html = validate_manifest_integrity(raw, manifest)
    repos = extract_repos(html)
    if not repos:
        raise PilotValidationError("No Trending rows")
    # A selector-consistency check is not independent live-page coverage evidence.
    layout = inspect_structure(html) if inspect_structure else None
    if layout and (layout["selector_box_row_count"] != len(repos)
                   or layout["extracted_repository_count"] != len(repos)):
        raise PilotValidationError("supported selector and parsed row counts disagree")
    parse_time = datetime.now(timezone.utc).isoformat()
    rows = []
    for rank, name in enumerate(repos, 1):
        rows.append({
            "schema_version": "pilot-1.0",
            "repository": name,
            "rank": rank,
            "trending_url": url,
            "observation_date": moment.date().isoformat(),
            "captured_at_utc": moment.isoformat(),
            "parsed_at_utc": parse_time,
            "collected_at_utc": moment.isoformat(),
            "window": window,
            "language_filter": None,
            "source_sha256": digest,
            "source_bytes": len(raw),
            "source_provenance": "self_recorded_capture_sha256_checked",
            "metadata_identity_status": "unresolved",
            "eligible_for_confirmatory_cohort": False,
        })
    audit = {
        "manifest_schema_version": MANIFEST_SCHEMA,
        "capture_date_utc": moment.date().isoformat(),
        "captured_at_utc": moment.isoformat(),
        "source_sha256": digest,
        "source_url": url,
        "window": window,
        "page_rows": len(rows),
        "unique_displayed_names": len(set(repos)),
        "parser_qa_status": "requires_independent_manual_audit",
        "selector_box_row_count": (layout["selector_box_row_count"] if layout else None),
        "structural_parser_status": (
            layout["structural_parser_status"] if layout else "not_separately_instrumented"
        ),
        "structural_scope_warning": (
            "Supported article.Box-row structure only; off-selector rows "
            "and live GitHub layout require independent audit."
        ),
        "stable_repository_id_status": "unresolved",
        "cohort_enrollment_status": "not_enrolled",
        "note": "SHA integrity verified locally; upstream origin and identity not independently authenticated.",
    }
    return rows, audit


def evaluate_preflight(card, *, stage="confirmatory"):
    """Check evidence completeness, never issue ethical/academic authorization."""
    _obj(card, "preflight")
    if card.get("schema_version") != MANIFEST_SCHEMA:
        raise PilotValidationError("unsupported preflight schema")
    if stage not in ("pilot", "confirmatory"):
        raise PilotValidationError("stage must be pilot or confirmatory")
    _text(card.get("study_id"), "study_id")
    gates = _obj(card.get("gates"), "gates")
    required = PILOT_GATES + (CONFIRMATORY_EXTRA_GATES if stage == "confirmatory" else ())
    invalid = []
    pending = []
    blocked = []
    verified = []
    for name in required:
        gate = gates.get(name)
        if gate is None:
            pending.append(name)
            continue
        _obj(gate, "gates." + name)
        status = gate.get("status")
        if status not in GATE_STATES:
            raise PilotValidationError("gates." + name + " status must be pending, blocked or verified")
        if status == "verified":
            for field in ("evidence_ref", "reviewer", "reviewed_at_utc"):
                _text(gate.get(field), "gates." + name + "." + field)
            _utc_timestamp(gate["reviewed_at_utc"], "gates." + name + ".reviewed_at_utc")
            verified.append(name)
        elif status == "blocked":
            blocked.append(name)
        else:
            pending.append(name)
    decision = "ready_for_human_review" if not pending and not blocked else "not_ready"
    return {
        "study_id": card["study_id"],
        "stage": stage,
        "decision": decision,
        "required_gate_count": len(required),
        "verified": verified,
        "pending": pending,
        "blocked": blocked,
        "disclaimer": (
            "Self-declared documentary gate checklist only; human reviewers must authenticate "
            "evidence and sign off. This is NOT formal ethics approval, preregistration, "
            "authorized scraping, study enrollment, or data collection."
        ),
    }


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
