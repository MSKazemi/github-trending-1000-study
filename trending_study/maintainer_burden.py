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

from .data_integrity import MAX_FILE_BYTES, ResearchJSONError, load_research_json_file


class BurdenError(ValueError):
    pass

UPSTREAM = ("upstream_review", "upstream_support")
DOWNSTREAM = ("downstream_search", "downstream_implementation",
              "downstream_review_repair", "downstream_followup")
FIELDS = UPSTREAM + DOWNSTREAM
APPROVED_CONSENT = {"not_consented", "consented", "withdrawn"}
STATUS = {"pass", "fail", "unknown"}
_SHA = re.compile(r"[0-9a-f]{40,64}\Z")
# The input schema is provisional and intentionally restricted to declared,
# non-free-text metadata. Raw prompts, names and logs are not accepted.
_OPAQUE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
_STATE = re.compile(r"[a-z][a-z0-9_:-]{0,79}\Z")
CASE_FIELDS = frozenset((
    "schema_version", "synthetic", "case_id", "frame_commit",
    "opt_in_project_id", "consent_state", "human_review_state",
    "observed_at_utc", "task_type", "task_accepted_by_independent_reviewer",
    "declared_workflow", "human_time_minutes", "outcomes",
    "data_release_approval", "not_empirical_data",
))
OUTCOME_FIELDS = frozenset((
    "actionability", "newcomer_comprehension_pass", "followup_30_day",
    "followup_90_day", "security_or_privacy_incident",
))


def _utc(value):
    if not isinstance(value, str):
        raise BurdenError("observation requires explicit UTC timestamp")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        # The lower-level datetime ValueError can echo caller-controlled text.
        dt = None
    if dt is None:
        raise BurdenError("invalid timestamp")
    if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
        raise BurdenError("observation must use explicit UTC")
    if dt > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise BurdenError("future observation invalid")

def summarize(cards):
    if not isinstance(cards, list) or not 1 <= len(cards) <= 10000:
        raise BurdenError("cases must be a bounded nonempty array")
    seen = set()
    complete = 0
    accepted_complete = 0
    unknown_total = 0
    observed_component_entries = 0
    known_partial_minutes = 0.0
    total_complete_minutes = 0.0
    synthetic_count = 0
    study_kinds = set()
    for card in cards:
        if (not isinstance(card, dict)
                or set(card) != CASE_FIELDS
                or card.get("schema_version") != "proposed-maintainer-externality-0.1"):
            raise BurdenError("invalid maintainer case schema or fields")
        key = card["case_id"]
        if not isinstance(key, str) or not _OPAQUE.fullmatch(key) or key in seen:
            raise BurdenError("unique bounded opaque case_id required")
        seen.add(key)
        if type(card.get("not_empirical_data")) is not bool:
            raise BurdenError("explicit not_empirical_data required")
        synthetic = card["not_empirical_data"]
        if type(card["synthetic"]) is not bool or card["synthetic"] != synthetic:
            raise BurdenError("conflicting synthetic dataset indicators")
        for field in ("opt_in_project_id", "task_type", "declared_workflow"):
            value = card[field]
            if not isinstance(value, str) or not _OPAQUE.fullmatch(value):
                raise BurdenError("metadata must use bounded opaque identifiers")
        for field in ("human_review_state", "data_release_approval"):
            value = card[field]
            if not isinstance(value, str) or not _STATE.fullmatch(value):
                raise BurdenError("invalid bounded review or release status")
        if (card["human_review_state"] != "pending"
                or card["data_release_approval"] != "pending"):
            # The proposed v0.1 schema must not self-certify a human signoff.
            raise BurdenError("v0.1 case cannot self-certify review or release")
        outcomes = card["outcomes"]
        if (not isinstance(outcomes, dict)
                or set(outcomes) != OUTCOME_FIELDS
                or any(not isinstance(v, str) or not _STATE.fullmatch(v)
                       for v in outcomes.values())):
            raise BurdenError("invalid bounded outcome schema")
        synthetic_count += synthetic
        study_kinds.add(synthetic)
        frame = card["frame_commit"]
        if not isinstance(frame, str) or not _OPAQUE.fullmatch(frame):
            raise BurdenError("invalid bounded frame commitment")
        if not synthetic and not _SHA.fullmatch(frame):
            raise BurdenError("real case requires a frozen 40/64-hex frame_commit")
        consent = card["consent_state"]
        if not isinstance(consent, str) or consent not in APPROVED_CONSENT:
            raise BurdenError("explicit consent_state required")
        if not synthetic and consent != "consented":
            # A withdrawn/no-consent case may be counted for denominator only,
            # never carry participant work timing data in exported JSON.
            pass
        if (not isinstance(card["task_accepted_by_independent_reviewer"], str)
                or card["task_accepted_by_independent_reviewer"] not in STATUS):
            raise BurdenError("accepted-task status must be pass/fail/unknown")
        if consent != "consented":
            # Withdrawal and non-consent permit only a denominator row. The
            # previous validator also allowed inferred task success and
            # downstream outcomes to survive despite the no-observation gate.
            if (card["task_accepted_by_independent_reviewer"] != "unknown"
                    or any(v not in ("unknown", "not_started")
                           for v in outcomes.values())):
                raise BurdenError("nonconsented case must not retain assessed outcomes")
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
            elif type(t) not in (int, float) or t < 0:
                raise BurdenError("human active minutes must be finite, nonnegative or null")
            else:
                try:
                    numeric = float(t)
                except (OverflowError, ValueError):
                    # Converting a huge untrusted integer can include the
                    # input text in a chained exception traceback.
                    numeric = None
                if numeric is None or not math.isfinite(numeric):
                    raise BurdenError("human active minutes must be finite, nonnegative or null")
                known.append(numeric)
        if consent != "consented" and known:
            raise BurdenError("unconsented/withdrawn case may not publish human work minutes")
        if synthetic and known and card.get("observed_at_utc") is not None:
            raise BurdenError("synthetic case may not claim actual observed timing")
        if not synthetic and consent == "consented" and known and card.get("observed_at_utc") is None:
            raise BurdenError("consented observed time needs source UTC timestamp")
        # Each input may be finite while summing multiple very large values
        # overflows IEEE-754 and silently produces Infinity in JSON output.
        row_minutes = sum(known)
        if not math.isfinite(row_minutes):
            raise BurdenError("human minute total exceeds finite numeric range")
        observed_component_entries += len(known)
        known_partial_minutes += row_minutes
        if not math.isfinite(known_partial_minutes):
            raise BurdenError("human minute total exceeds finite numeric range")
        unknown_total += len(absent)
        if not absent:
            complete += 1
            total_complete_minutes += row_minutes
            if not math.isfinite(total_complete_minutes):
                raise BurdenError("human minute total exceeds finite numeric range")
            if card["task_accepted_by_independent_reviewer"] == "pass":
                accepted_complete += 1
    if len(study_kinds) != 1:
        raise BurdenError("synthetic and real participant cases must never share one aggregate")
    return {"dataset_kind": "synthetic" if True in study_kinds else "self_reported_pilot",
            "case_count": len(cards), "synthetic_case_count": synthetic_count,
            "cases_with_complete_time_boundary": complete,
            "cases_with_accepted_outcome_and_complete_time": accepted_complete,
            "missing_component_entries": unknown_total,
            "observed_component_entries": observed_component_entries,
            # No observed human-work component is unknown, never a measured 0.
            "known_partial_minutes_not_a_total": (known_partial_minutes
                                                  if observed_component_entries else None),
            "complete_case_minutes_not_a_population_estimate": total_complete_minutes if complete else None,
            "overall_human_minutes": (total_complete_minutes
                                      if complete == len(cards) and synthetic_count == 0 else None),
            "synthetic_scenario_minutes": (total_complete_minutes
                                           if complete == len(cards) and synthetic_count == len(cards)
                                           else None),
            "per_accepted_task_minutes": None,
            "independent_review_authenticated": False,
            "approved_for_public_release": False,
            "warning": "Partial observations exclude unknown work: no total burden or saved energy claim unless complete consented comparable outcomes and independently authenticated reviewers exist."}

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    a = p.parse_args(argv)
    diagnostic = None
    try:
        # The same bounded, descriptor-checked, duplicate-key-rejecting reader
        # used by the repository's other offline research instruments.
        doc = load_research_json_file(a.input, max_bytes=MAX_FILE_BYTES)
        if isinstance(doc, dict) and "cases" in doc:
            # A batch envelope cannot silently carry raw interview material,
            # identities, or other undeclared private sidecar fields.
            if set(doc) != {"cases"}:
                raise BurdenError("invalid maintainer cases envelope")
            records = doc["cases"]
        else:
            records = [doc]
        result = summarize(records)
    except ResearchJSONError:
        # Decoder errors may contain private object keys or local filenames.
        diagnostic = "invalid or unsafe research JSON input"
    except BurdenError as exc:
        # Domain errors are fixed messages, never respondent values or IDs.
        diagnostic = str(exc)
    except (ValueError, TypeError, OSError, KeyError, OverflowError, RecursionError):
        diagnostic = "invalid maintainer burden input"
    # argparse.error() raises SystemExit. Calling it inside the above except
    # blocks chains raw JSON/source errors into a full formatted traceback.
    if diagnostic is not None:
        p.error(diagnostic)
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
