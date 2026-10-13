"""Privacy-preserving offline aggregation of *consented* active work minutes.

No recruitment, timing, identity verification, or causal environmental result
occurs in this tool. Never publish a named maintainer performance ranking.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import re

class BurdenError(ValueError):
    pass

UPSTREAM = ("upstream_review", "upstream_support")
DOWNSTREAM = ("downstream_search", "downstream_implementation",
              "downstream_review_repair", "downstream_followup")
FIELDS = UPSTREAM + DOWNSTREAM
APPROVED_CONSENT = {"not_consented", "consented", "withdrawn"}
STATUS = {"pass", "fail", "unknown"}
_SHA = re.compile(r"[0-9a-f]{40,64}\Z")

def _utc(value):
    if not isinstance(value, str):
        raise BurdenError("observation requires explicit UTC timestamp")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise BurdenError("invalid timestamp") from exc
    if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
        raise BurdenError("observation must use explicit UTC")
    if dt > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise BurdenError("future observation invalid")

def summarize(cards):
    if not isinstance(cards, list) or not cards:
        raise BurdenError("nonempty cases array required")
    seen = set()
    complete = 0
    accepted_complete = 0
    unknown_total = 0
    known_partial_minutes = 0.0
    total_complete_minutes = 0.0
    synthetic_count = 0
    study_kinds = set()
    for card in cards:
        if not isinstance(card, dict) or card.get("schema_version") != "proposed-maintainer-externality-0.1":
            raise BurdenError("invalid maintainer case schema")
        key = card.get("case_id")
        if not isinstance(key, str) or not key.strip() or key in seen:
            raise BurdenError("unique nonempty case_id required")
        seen.add(key)
        if type(card.get("not_empirical_data")) is not bool:
            raise BurdenError("explicit not_empirical_data required")
        synthetic = card["not_empirical_data"]
        synthetic_count += synthetic
        study_kinds.add(synthetic)
        if not synthetic and (
                not isinstance(card.get("frame_commit"), str)
                or not _SHA.fullmatch(card["frame_commit"])):
            raise BurdenError("real case requires a frozen 40/64-hex frame_commit")
        consent = card.get("consent_state")
        if consent not in APPROVED_CONSENT:
            raise BurdenError("explicit consent_state required")
        if not synthetic and consent != "consented":
            # A withdrawn/no-consent case may be counted for denominator only,
            # never carry participant work timing data in exported JSON.
            pass
        if card.get("task_accepted_by_independent_reviewer") not in STATUS:
            raise BurdenError("accepted-task status must be pass/fail/unknown")
        if card.get("observed_at_utc") is not None:
            if consent != "consented":
                raise BurdenError("unconsented or withdrawn case cannot retain observation timestamp")
            _utc(card["observed_at_utc"])
        times = card.get("human_time_minutes")
        if not isinstance(times, dict) or set(times) != set(FIELDS):
            raise BurdenError("six nonoverlapping upstream/downstream time categories required")
        known = []
        absent = []
        for name in FIELDS:
            t = times[name]
            if t is None:
                absent.append(name)
            elif type(t) not in (int, float) or not math.isfinite(t) or t < 0:
                raise BurdenError("human active minutes must be finite, nonnegative or null")
            else:
                known.append(float(t))
        if consent != "consented" and known:
            raise BurdenError("unconsented/withdrawn case may not publish human work minutes")
        if synthetic and known and card.get("observed_at_utc") is not None:
            raise BurdenError("synthetic case may not claim actual observed timing")
        if not synthetic and consent == "consented" and known and card.get("observed_at_utc") is None:
            raise BurdenError("consented observed time needs source UTC timestamp")
        known_partial_minutes += sum(known)
        unknown_total += len(absent)
        if not absent:
            complete += 1
            total_complete_minutes += sum(known)
            if card["task_accepted_by_independent_reviewer"] == "pass":
                accepted_complete += 1
    if len(study_kinds) != 1:
        raise BurdenError("synthetic and real participant cases must never share one aggregate")
    return {"dataset_kind": "synthetic" if True in study_kinds else "self_reported_pilot",
            "case_count": len(cards), "synthetic_case_count": synthetic_count,
            "cases_with_complete_time_boundary": complete,
            "cases_with_accepted_outcome_and_complete_time": accepted_complete,
            "missing_component_entries": unknown_total,
            "known_partial_minutes_not_a_total": known_partial_minutes,
            "complete_case_minutes_not_a_population_estimate": total_complete_minutes if complete else None,
            "overall_human_minutes": total_complete_minutes if complete == len(cards) else None,
            "per_accepted_task_minutes": None,
            "independent_review_authenticated": False,
            "approved_for_public_release": False,
            "warning": "Partial observations exclude unknown work: no total burden or saved energy claim unless complete consented comparable outcomes and independently authenticated reviewers exist."}

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    a = p.parse_args(argv)
    try:
        doc = json.loads(a.input.read_text(encoding="utf-8"))
        result = summarize(doc["cases"] if isinstance(doc, dict) and "cases" in doc else [doc])
    except (ValueError, TypeError, OSError, KeyError) as exc:
        p.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
