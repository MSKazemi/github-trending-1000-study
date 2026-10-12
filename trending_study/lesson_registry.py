"""Strictly structural, offline lesson-card consistency checks; never scientific certification."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re

SHA = re.compile(r"^[a-f0-9]{40}$")
HASH = re.compile(r"^[a-f0-9]{64}$")
STATES = {"hypothesis", "exploratory", "validated_for_context", "inconclusive", "contradicted", "superseded"}


class LessonError(ValueError):
    pass


def _required_text(obj, key):
    val = obj.get(key)
    if not isinstance(val, str) or not val.strip():
        raise LessonError(f"{key}: nonempty string required")
    return val


def _utc(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise LessonError("reviewed_at_utc must be explicit UTC")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LessonError("invalid reviewer timestamp") from exc


def evaluate(payload):
    if not isinstance(payload, dict) or payload.get("schema_version") != "1.0":
        raise LessonError("expected schema_version 1.0")
    if payload.get("dataset_kind") not in {"synthetic", "self_reported"}:
        raise LessonError("dataset_kind is synthetic or self_reported")
    lessons = payload.get("lessons")
    if not isinstance(lessons, list):
        raise LessonError("lessons must be a list")
    ids = set()
    counts = {f"E{i}": 0 for i in range(6)}
    for row in lessons:
        if not isinstance(row, dict):
            raise LessonError("lesson must be object")
        for k in ("id", "rq", "claim", "population", "outcome", "measurement_window",
                  "validity_risks", "applicability", "practical_cost"):
            _required_text(row, k)
        key = row["id"]
        if key in ids:
            raise LessonError("duplicate lesson id")
        ids.add(key)
        grade, status = row.get("grade"), row.get("status")
        if grade not in counts or status not in STATES:
            raise LessonError("invalid grade or status")
        counts[grade] += 1
        sources = row.get("sources")
        if not isinstance(sources, list):
            raise LessonError("sources must be list")
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get("url"), str) or not source["url"].startswith("https://"):
                raise LessonError("source must have https URL")
            _required_text(source, "published_date")
            try:
                datetime.strptime(source["published_date"], "%Y-%m-%d")
            except ValueError as exc:
                raise LessonError("source date invalid") from exc
        if row.get("supersedes") is not None and (
            not isinstance(row["supersedes"], str) or row["supersedes"] == key
        ):
            raise LessonError("invalid supersedes reference")
        if grade != "E0":
            if not sources or not isinstance(row.get("analysis_commit"), str) or not SHA.fullmatch(row["analysis_commit"]):
                raise LessonError("E1+ needs sources and analysis commit")
            if not isinstance(row.get("data_sha256"), str) or not HASH.fullmatch(row["data_sha256"]):
                raise LessonError("E1+ needs immutable data checksum")
        if grade in {"E2", "E3", "E4", "E5"}:
            n = row.get("sample_n")
            if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
                raise LessonError("E2+ requires positive sample n")
            if isinstance(row.get("effect"), bool) or not isinstance(row.get("effect"), (int, float)):
                raise LessonError("E2+ requires numeric effect")
            interval = row.get("interval")
            if not isinstance(interval, list) or len(interval) != 2 or any(
                isinstance(v, bool) or not isinstance(v, (int, float)) for v in interval
            ) or not interval[0] <= row["effect"] <= interval[1]:
                raise LessonError("E2+ requires enclosing uncertainty interval")
        if grade in {"E4", "E5"} or status == "validated_for_context":
            _required_text(row, "reviewer_ref")
            _utc(row.get("reviewed_at_utc"))
        if status == "validated_for_context" and grade not in {"E4", "E5"}:
            raise LessonError("cannot mark lower grade validated")
    return {"schema_version": "1.0", "dataset_kind": payload["dataset_kind"],
            "structurally_checked": len(lessons), "grades": counts,
            "independent_verification": False, "validated_scientific_findings": None,
            "warning": "Self-reported evidence and reviewers are NOT authenticated; a structural pass is not an empirical scientific result."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    args = p.parse_args(argv)
    try:
        out = evaluate(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (LessonError, OSError, ValueError) as exc:
        p.exit(2, f"error: {exc}\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
