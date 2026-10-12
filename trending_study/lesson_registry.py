"""Conservative offline checks for a self-reported E0-E5 evidence/lesson ledger.

A passing document is not independently authenticated, peer reviewed or causal.
"""
import argparse
from datetime import datetime
import json
import math
from pathlib import Path
import re
from urllib.parse import urlparse


class LessonError(ValueError):
    pass


STATUSES = {"hypothesis", "exploratory", "validated_for_context",
            "inconclusive", "contradicted", "superseded"}
GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
SHA = re.compile(r"^[a-f0-9]{40}$")


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
    return dt


def _sources(row):
    sources = row.get("sources")
    if not isinstance(sources, list):
        raise LessonError("sources must be a list, possibly empty for E0")
    for entry in sources:
        if not isinstance(entry, dict):
            raise LessonError("source must be object")
        u = _nonempty(entry, "url")
        parsed = urlparse(u)
        if parsed.scheme != "https" or not parsed.netloc:
            raise LessonError("source must have HTTPS URL")
        _utc(entry, "published_at_utc")


def audit(data):
    if not isinstance(data, dict) or not isinstance(data.get("lessons"), list):
        raise LessonError("input must contain lessons list")
    ids, counts, needs_review = set(), {}, []
    for row in data["lessons"]:
        if not isinstance(row, dict):
            raise LessonError("lesson must be object")
        ident = _nonempty(row, "id")
        if ident in ids:
            raise LessonError("duplicate lesson ID")
        ids.add(ident)
        for k in ("title", "question", "population", "comparison",
                  "primary_outcome", "measurement_window", "applicability",
                  "risks", "stop_rule", "validity_threats"):
            _nonempty(row, k)
        status, grade = row.get("status"), row.get("evidence_grade")
        if status not in STATUSES or grade not in GRADES:
            raise LessonError("unsupported evidence grade or status")
        _sources(row)
        if status == "superseded":
            _nonempty(row, "superseded_by")
        if grade != "E0" and not row["sources"]:
            raise LessonError("E1-E5 require at least one dated source")
        if status == "validated_for_context":
            if grade not in {"E4", "E5"}:
                raise LessonError("validated status requires controlled/replicated evidence E4/E5")
            _nonempty(row, "observed_data_ref")
            analyst = _nonempty(row, "analyst")
            reviewer = _nonempty(row, "independent_reviewer")
            if analyst == reviewer:
                raise LessonError("analyst and reviewer must be distinct")
            _utc(row, "reviewed_at_utc")
            sha = _nonempty(row, "analysis_commit")
            if not SHA.fullmatch(sha):
                raise LessonError("analysis_commit must be 40 lowercase hex digits")
            n = row.get("sample_n")
            if type(n) is not int or n <= 0:
                raise LessonError("sample_n must be positive integer")
            estimate = row.get("effect_size")
            bounds = row.get("interval")
            if not isinstance(estimate, (int, float)) or isinstance(estimate, bool) or not math.isfinite(estimate):
                raise LessonError("numeric effect size required")
            if not isinstance(bounds, list) or len(bounds) != 2 or any(
                not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) for v in bounds
            ) or not (bounds[0] <= bounds[1]):
                raise LessonError("numeric ordered interval required")
            needs_review.append(ident)
        counts[status] = counts.get(status, 0) + 1
    return {"total": len(ids), "by_status": dict(sorted(counts.items())),
            "declared_validated_ids_needing_external_review": needs_review,
            "self_reported_sources_are_not_authenticated": True,
            "empirical_result_generated": False}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = audit(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
