"""Offline descriptive task-usefulness audit; no recruitment or human authentication.

This validator does not randomize participants, verify the external acceptance
test, confer ethics approval, or interpret a synthetic example as real data.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import math
from pathlib import Path
import re

class UsefulnessError(ValueError):
    pass

_SHA = re.compile(r"[a-f0-9]{64}\Z")
_STATUS = {"pass", "fail", "unknown", "not_applicable"}
_ARCHETYPES = {"cli", "library", "research_artifact", "application"}

def _utc(value):
    if not isinstance(value, str):
        raise UsefulnessError("observation needs explicit UTC timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise UsefulnessError("invalid UTC observation timestamp") from exc
    if result.utcoffset() is None or result.utcoffset().total_seconds() != 0:
        raise UsefulnessError("observation timestamp must explicitly use UTC")
    if result > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise UsefulnessError("observation cannot be future-dated")

def summarize(card):
    if not isinstance(card, dict) or card.get("schema_version") != "proposed-usefulness-task-0.1":
        raise UsefulnessError("unsupported usefulness-task schema")
    if type(card.get("synthetic")) is not bool or type(card.get("not_empirical_data")) is not bool:
        raise UsefulnessError("synthetic and not_empirical_data must be explicit booleans")
    synthetic = card["synthetic"]
    if card["not_empirical_data"] != synthetic:
        raise UsefulnessError("synthetic example and empirical claims must not be conflated")
    if card.get("archetype") not in _ARCHETYPES:
        raise UsefulnessError("unsupported project archetype")
    if not isinstance(card.get("task_id"), str) or not card["task_id"].strip():
        raise UsefulnessError("task_id is required")
    if not isinstance(card.get("fixed_requirements_sha256"), str) or not _SHA.fullmatch(card["fixed_requirements_sha256"]):
        raise UsefulnessError("frozen task SHA-256 required")
    for field in ("frozen_acceptance_ref", "functional_unit", "project_version"):
        if not isinstance(card.get(field), str) or not card[field].strip():
            raise UsefulnessError(field + " required for matched functional unit")
    arms = card.get("arms")
    if not isinstance(arms, list) or len(arms) != 2 or any(not isinstance(x, str) or not x.strip() for x in arms) or arms[0] == arms[1]:
        raise UsefulnessError("exactly two distinct declared arms required")
    if not synthetic and (card.get("approval_status") != "approved"
                          or card.get("human_review_and_consent") in (None, "not performed")):
        raise UsefulnessError("real observations require externally approved protocol/consent records")
    attempts = card.get("attempts")
    if not isinstance(attempts, list):
        raise UsefulnessError("attempts list required (empty is not a negative study)")
    ids, participants = set(), set()
    counts = {x: 0 for x in sorted(_STATUS)}
    withdrawn = 0
    for a in attempts:
        if not isinstance(a, dict):
            raise UsefulnessError("attempt must be an object")
        aid, pid = a.get("attempt_id"), a.get("participant_id")
        if any(not isinstance(x, str) or not x.strip() for x in (aid, pid)) or aid in ids:
            raise UsefulnessError("unique attempt_id and pseudonymous participant_id required")
        ids.add(aid)
        participants.add(pid)
        if a.get("assigned_arm") not in arms or type(a.get("task_attempted")) is not bool:
            raise UsefulnessError("attempt arm and attempted status required")
        status = a.get("accepted")
        if not isinstance(status, str) or status not in _STATUS:
            raise UsefulnessError("accepted must be pass/fail/unknown/not_applicable")
        consent = a.get("consent_state")
        if synthetic:
            if consent != "not_applicable_synthetic":
                raise UsefulnessError("fictional attempts must not claim real consent")
        elif consent not in {"consented", "withdrawn"}:
            raise UsefulnessError("consent must be explicit or withdrawn for real data")
        if consent == "withdrawn":
            withdrawn += 1
            if status != "unknown" or a.get("time_to_first_success_minutes") is not None:
                raise UsefulnessError("withdrawn record may not publish outcome/time")
        if status == "not_applicable":
            # A structural inapplicability decision must be recorded rather
            # than silently removing a failed assigned attempt from the rate.
            if a["task_attempted"]:
                raise UsefulnessError("attempted task cannot become not_applicable")
            why = a.get("inapplicability_reason")
            if not isinstance(why, str) or not why.strip():
                raise UsefulnessError("not_applicable requires documented inapplicability_reason")
        if not a["task_attempted"] and status in {"pass", "fail"}:
            raise UsefulnessError("unattempted task cannot have pass/fail")
        minutes = a.get("time_to_first_success_minutes")
        if minutes is not None and (status != "pass" or type(minutes) not in (int, float)
                                    or not math.isfinite(minutes) or minutes < 0):
            raise UsefulnessError("time_to_first_success requires finite nonnegative passing attempt")
        if status == "pass" and minutes is None:
            raise UsefulnessError("passing attempt needs recorded success time")
        stamp = a.get("observed_at_utc")
        if not synthetic and consent == "consented" and status in {"pass", "fail"} and stamp is None:
            raise UsefulnessError("real completed outcomes need observed UTC timestamp")
        if stamp is not None:
            _utc(stamp)
        counts[status] += 1
    denom = counts["pass"] + counts["fail"] + counts["unknown"]
    lo = counts["pass"] / denom if denom else None
    hi = (counts["pass"] + counts["unknown"]) / denom if denom else None
    return {"task_id": card["task_id"], "dataset_kind": "synthetic" if synthetic else "self_reported_pilot",
            "attempts": len(attempts), "distinct_participant_refs": len(participants),
            "counts": counts, "withdrawn_count": withdrawn, "applicable_assigned_denominator": denom,
            "pass_fraction_logical_lower": lo, "pass_fraction_logical_upper": hi,
            "bounds_are_not_confidence_intervals": True, "human_independence_authenticated": False,
            "empirical_study_accepted": False,
            "warning": "Logical unknown-outcome bounds only. Real consent, task validity, randomization and clustered uncertainty require independent verification."}

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    args = p.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = summarize(data)
    except (OSError, ValueError, TypeError) as exc:
        p.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
