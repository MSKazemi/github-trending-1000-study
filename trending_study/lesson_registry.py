"""Conservative offline checks for a self-reported E0-E5 evidence/lesson ledger.

A passing document is not independently authenticated, peer reviewed or causal.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
import os
from pathlib import Path
import re
import stat
from urllib.parse import urlsplit

from .data_integrity import MAX_FILE_BYTES, decode_research_json


class LessonError(ValueError):
    pass


STATUSES = {"hypothesis", "exploratory", "validated_for_context",
            "inconclusive", "contradicted", "superseded"}
GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
SHA = re.compile(r"^[a-f0-9]{40}$")
HASH = re.compile(r"^[a-f0-9]{64}$")
VERSIONS = {"1.0", "1.1"}
KINDS = {"synthetic", "self_reported"}
RESULT_KINDS = {"not_estimated", "estimated", "null_compatible"}
REQUIRED_TEXT = (
    "title", "question", "population", "comparison", "primary_outcome",
    "measurement_window", "applicability", "intervention_or_feature",
    "negative_findings", "practical_cost", "suggested_experiment",
    "risks", "stop_rule", "validity_threats",
)
LESSON_FIELDS = set(REQUIRED_TEXT) | {
    "id", "status", "evidence_grade", "sources", "superseded_by",
    "analysis_commit", "data_sha256", "sample_n", "effect_size", "interval",
    "analyst", "independent_reviewer", "reviewed_at_utc", "observed_data_ref",
    "research_question_id", "observed_at_utc", "result_kind",
    "effect_unit", "null_value", "interval_level", "analysis_method",
    "review_record_ref",
}


def _known_fields(row, allowed, context):
    unexpected = set(row) - allowed
    if unexpected:
        # Do not echo values: unexpected fields may contain secrets or raw logs.
        raise LessonError(f"{context} contains unsupported field(s): "
                          + ", ".join(sorted(unexpected)))


def _finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        # math.isfinite(10**400) raises OverflowError: reject it as an
        # invalid estimate, not as an unhandled CLI exception.
        return math.isfinite(float(value))
    except (OverflowError, ValueError):
        return False



def _nonempty(row, key):
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise LessonError(f"{key} must be nonempty string")
    return value


def _utc(row, key):
    s = _nonempty(row, key)
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LessonError(f"{key} invalid UTC timestamp") from exc
    if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
        raise LessonError(f"{key} must use explicit UTC")
    if dt > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise LessonError(f"{key} cannot be future-dated")
    return dt


def _sources(row):
    sources = row.get("sources")
    if not isinstance(sources, list):
        raise LessonError("sources must be a list, possibly empty for E0")
    seen_urls = set()
    for entry in sources:
        if not isinstance(entry, dict):
            raise LessonError("source must be object")
        _known_fields(entry, {"url", "published_at_utc"}, "source")
        u = _nonempty(entry, "url")
        try:
            parsed = urlsplit(u)
            port = parsed.port
        except ValueError as exc:
            raise LessonError("source contains malformed HTTPS authority") from exc
        if (parsed.scheme != "https" or not parsed.hostname or parsed.username
                or parsed.password or parsed.fragment or u != u.strip()
                or any(c.isspace() or ord(c) < 32 for c in u)
                or (port is not None and not 1 <= port <= 65535)):
            raise LessonError("source must be a clean HTTPS URL without credentials or fragment")
        if u in seen_urls:
            raise LessonError("duplicate source URL in one lesson")
        seen_urls.add(u)
        _utc(entry, "published_at_utc")


def audit(data):
    if (not isinstance(data, dict) or data.get("schema_version") not in VERSIONS
            or not isinstance(data.get("dataset_kind"), str)
            or data["dataset_kind"] not in KINDS
            or not isinstance(data.get("lessons"), list)):
        raise LessonError("input requires v1.0/v1.1, synthetic/self_reported kind and lessons list")
    _known_fields(data, {"schema_version", "dataset_kind", "lessons"}, "registry")
    v11 = data["schema_version"] == "1.1"
    ids, counts, needs_review, grade_counts = set(), {}, [], {f"E{i}": 0 for i in range(6)}
    supersessions = {}
    for row in data["lessons"]:
        if not isinstance(row, dict):
            raise LessonError("lesson must be object")
        _known_fields(row, LESSON_FIELDS, "lesson")
        ident = _nonempty(row, "id")
        if ident != ident.strip():
            raise LessonError("lesson ID cannot contain surrounding whitespace")
        if ident in ids:
            raise LessonError("duplicate lesson ID")
        ids.add(ident)
        for k in REQUIRED_TEXT:
            _nonempty(row, k)
        status, grade = row.get("status"), row.get("evidence_grade")
        if (not isinstance(status, str) or status not in STATUSES or
                not isinstance(grade, str) or grade not in GRADES):
            raise LessonError("unsupported evidence grade or status")
        grade_counts[grade] += 1
        _sources(row)
        if v11:
            _nonempty(row, "research_question_id")
            result_kind = row.get("result_kind")
            if result_kind not in RESULT_KINDS:
                raise LessonError("v1.1 requires explicit result_kind")
            if grade in {"E0", "E1"}:
                if (result_kind != "not_estimated" or row.get("effect_size") is not None
                        or row.get("interval") is not None
                        or row.get("interval_level") is not None
                        or row.get("null_value") is not None):
                    raise LessonError("E0/E1 cannot present an estimated effect or CI")
            elif result_kind == "not_estimated":
                raise LessonError("E2-E5 require an explicitly estimated result")
            if grade == "E0" and row.get("sample_n") is not None:
                raise LessonError("E0 must retain unknown sample_n as null")
        if status == "hypothesis" and grade != "E0":
            raise LessonError("hypothesis status must remain E0")
        if v11 and status != "superseded" and row.get("superseded_by") is not None:
            raise LessonError("superseded_by requires status=superseded")
        if status == "superseded":
            target = _nonempty(row, "superseded_by")
            if target == ident:
                raise LessonError("superseded_by cannot self-reference")
            if v11:
                supersessions[ident] = target
        if grade != "E0":
            if not row["sources"]:
                raise LessonError("E1-E5 require at least one dated source")
            if not SHA.fullmatch(_nonempty(row, "analysis_commit")):
                raise LessonError("E1-E5 require 40-hex analysis_commit")
            if not HASH.fullmatch(_nonempty(row, "data_sha256")):
                raise LessonError("E1-E5 require 64-hex frozen source/data SHA256")
            if v11:
                _nonempty(row, "observed_data_ref")
                _utc(row, "observed_at_utc")
        if grade in {"E2", "E3", "E4", "E5"}:
            n = row.get("sample_n")
            if type(n) is not int or n <= 0:
                raise LessonError("E2-E5 require positive sample_n")
            estimate = row.get("effect_size")
            bounds = row.get("interval")
            if not _finite_number(estimate):
                raise LessonError("E2-E5 require finite effect_size")
            if (not isinstance(bounds, list) or len(bounds) != 2
                    or any(not _finite_number(v) for v in bounds)
                    or not bounds[0] <= estimate <= bounds[1]):
                raise LessonError("E2-E5 require finite interval enclosing effect_size")
            if v11:
                _nonempty(row, "effect_unit")
                _nonempty(row, "analysis_method")
                level = row.get("interval_level")
                if not _finite_number(level) or not 0 < level < 1:
                    raise LessonError("E2-E5 require interval_level strictly between 0 and 1")
                null_value = row.get("null_value")
                if not _finite_number(null_value):
                    raise LessonError("E2-E5 require a finite explicit null_value")
                contains_null = bounds[0] <= null_value <= bounds[1]
                if result_kind == "null_compatible" and not contains_null:
                    raise LessonError("null_compatible requires an interval containing null_value")
                if result_kind == "estimated" and contains_null:
                    raise LessonError("estimated interval overlaps null_value; declare null_compatible")
        if grade in {"E4", "E5"}:
            analyst = _nonempty(row, "analyst")
            reviewer = _nonempty(row, "independent_reviewer")
            if analyst.strip().casefold() == reviewer.strip().casefold():
                raise LessonError("analyst and reviewer references must be distinct")
            reviewed = _utc(row, "reviewed_at_utc")
            if v11:
                _nonempty(row, "review_record_ref")
                if reviewed < _utc(row, "observed_at_utc"):
                    raise LessonError("review must not predate observed evidence")
        if status == "validated_for_context":
            if data["dataset_kind"] == "synthetic":
                raise LessonError("synthetic records cannot declare validated status")
            if grade not in {"E4", "E5"}:
                raise LessonError("validated status requires controlled/replicated evidence E4/E5")
            _nonempty(row, "observed_data_ref")
            needs_review.append(ident)
        counts[status] = counts.get(status, 0) + 1
    if v11:
        # A supersession must resolve in this frozen registry. Keep history,
        # but do not accept missing targets or referential cycles.
        for start, target in supersessions.items():
            if target not in ids:
                raise LessonError("superseded_by must reference a lesson in this registry")
            visited = {start}
            node = target
            while node in supersessions:
                if node in visited:
                    raise LessonError("superseded_by contains a cycle")
                visited.add(node)
                node = supersessions[node]
    return {"schema_version": data["schema_version"], "dataset_kind": data["dataset_kind"],
            "total": len(ids), "by_status": dict(sorted(counts.items())),
            "by_grade": grade_counts,
            "declared_validated_ids_needing_external_review": needs_review,
            "independently_verified_lesson_count": 0,
            "v1_0_legacy_input": not v11,
            "self_reported_sources_are_not_authenticated": True,
            "empirical_result_generated": False,
            "independent_verification": False,
            "scientific_status": "structural_validation_only_not_accepted_evidence"}


def audit_file(path):
    """Load exactly one bounded, strict JSON artifact and audit its claims."""
    path = Path(path)
    if path.is_symlink():
        raise LessonError("input must be a regular non-symlink file")
    # Open without following a last-component symlink and inspect the opened
    # descriptor, not a separately stat-ed path that could be replaced.
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise LessonError("input must be a readable regular non-symlink file") from exc
    with os.fdopen(descriptor, "rb") as stream:
        metadata = os.fstat(stream.fileno())
        if not stat.S_ISREG(metadata.st_mode):
            raise LessonError("input must be a regular non-symlink file")
        if metadata.st_size > MAX_FILE_BYTES:
            raise LessonError("input exceeds research JSON byte limit")
        raw = stream.read(MAX_FILE_BYTES + 1)
        if len(raw) > MAX_FILE_BYTES:
            raise LessonError("input exceeds research JSON byte limit")
    return audit(decode_research_json(raw, path.name))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = audit_file(args.input)
    except (OSError, ValueError, RecursionError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
