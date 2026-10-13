"""Conservative offline checks for a self-reported E0-E5 evidence/lesson ledger.

A passing document is not independently authenticated, peer reviewed or causal.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import re
from urllib.parse import urlsplit


class LessonError(ValueError):
    pass


STATUSES = {"hypothesis", "exploratory", "validated_for_context",
            "inconclusive", "contradicted", "superseded"}
GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
SHA = re.compile(r"^[a-f0-9]{40}$")
HASH = re.compile(r"^[a-f0-9]{64}$")


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
    for entry in sources:
        if not isinstance(entry, dict):
            raise LessonError("source must be object")
        u = _nonempty(entry, "url")
        parsed = urlsplit(u)
        if (parsed.scheme != "https" or not parsed.hostname or parsed.username
                or parsed.password or parsed.fragment or u != u.strip()):
            raise LessonError("source must be a clean HTTPS URL without credentials or fragment")
        _utc(entry, "published_at_utc")


def audit(data):
    if (not isinstance(data, dict) or data.get("schema_version") != "1.0"
            or data.get("dataset_kind") not in {"synthetic", "self_reported"}
            or not isinstance(data.get("lessons"), list)):
        raise LessonError("input must have v1.0, synthetic/self_reported kind and lessons list")
    ids, counts, needs_review, grade_counts = set(), {}, [], {f"E{i}": 0 for i in range(6)}
    for row in data["lessons"]:
        if not isinstance(row, dict):
            raise LessonError("lesson must be object")
        ident = _nonempty(row, "id")
        if ident in ids:
            raise LessonError("duplicate lesson ID")
        ids.add(ident)
        for k in ("title", "question", "population", "comparison",
                  "primary_outcome", "measurement_window", "applicability",
                  "intervention_or_feature", "negative_findings", "practical_cost",
                  "suggested_experiment", "risks", "stop_rule", "validity_threats"):
            _nonempty(row, k)
        status, grade = row.get("status"), row.get("evidence_grade")
        if (not isinstance(status, str) or status not in STATUSES or
                not isinstance(grade, str) or grade not in GRADES):
            raise LessonError("unsupported evidence grade or status")
        grade_counts[grade] += 1
        _sources(row)
        if status == "hypothesis" and grade != "E0":
            raise LessonError("hypothesis status must remain E0")
        if status == "superseded":
            target = _nonempty(row, "superseded_by")
            if target == ident:
                raise LessonError("superseded_by cannot self-reference")
        if grade != "E0":
            if not row["sources"]:
                raise LessonError("E1-E5 require at least one dated source")
            if not SHA.fullmatch(_nonempty(row, "analysis_commit")):
                raise LessonError("E1-E5 require 40-hex analysis_commit")
            if not HASH.fullmatch(_nonempty(row, "data_sha256")):
                raise LessonError("E1-E5 require 64-hex frozen source/data SHA256")
        if grade in {"E2", "E3", "E4", "E5"}:
            n = row.get("sample_n")
            if type(n) is not int or n <= 0:
                raise LessonError("E2-E5 require positive sample_n")
            estimate = row.get("effect_size")
            bounds = row.get("interval")
            if (not isinstance(estimate, (int, float)) or isinstance(estimate, bool)
                    or not math.isfinite(estimate)):
                raise LessonError("E2-E5 require finite effect_size")
            if (not isinstance(bounds, list) or len(bounds) != 2
                    or any(not isinstance(v, (int, float)) or isinstance(v, bool)
                           or not math.isfinite(v) for v in bounds)
                    or not bounds[0] <= estimate <= bounds[1]):
                raise LessonError("E2-E5 require finite interval enclosing effect_size")
        if grade in {"E4", "E5"}:
            analyst = _nonempty(row, "analyst")
            reviewer = _nonempty(row, "independent_reviewer")
            if analyst.strip().casefold() == reviewer.strip().casefold():
                raise LessonError("analyst and reviewer references must be distinct")
            _utc(row, "reviewed_at_utc")
        if status == "validated_for_context":
            if grade not in {"E4", "E5"}:
                raise LessonError("validated status requires controlled/replicated evidence E4/E5")
            _nonempty(row, "observed_data_ref")
            needs_review.append(ident)
        counts[status] = counts.get(status, 0) + 1
    return {"schema_version": "1.0", "dataset_kind": data["dataset_kind"],
            "total": len(ids), "by_status": dict(sorted(counts.items())),
            "by_grade": grade_counts,
            "declared_validated_ids_needing_external_review": needs_review,
            "self_reported_sources_are_not_authenticated": True,
            "empirical_result_generated": False,
            "independent_verification": False,
            "scientific_status": "structural_validation_only_not_accepted_evidence"}


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
