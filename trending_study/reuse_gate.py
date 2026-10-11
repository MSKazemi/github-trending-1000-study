"""Evidence-first reuse decision aid.

This offline heuristic checks *documented evidence*, not live dependency safety,
carbon reductions, true code equivalence, or popularity.
"""
import argparse
import json
from pathlib import Path


class InvalidReuseAssessment(ValueError):
    pass


GOOD = "verified"
BAD = "failed"
UNKNOWN = "unknown"
STATES = {GOOD, BAD, UNKNOWN}


def _text(obj, key):
    val = obj.get(key)
    if not isinstance(val, str):
        raise InvalidReuseAssessment(f"{key} must be a string")
    return val.strip()


def evaluate(assessment):
    """Recommend next *evidence gate*, not an automatic dependency install."""
    if not isinstance(assessment, dict) or assessment.get("schema_version") != "1.0":
        raise InvalidReuseAssessment("Expected schema_version 1.0 assessment object")
    name = _text(assessment, "task")
    acceptance = _text(assessment, "acceptance_test")
    if not name:
        raise InvalidReuseAssessment("Task must not be empty")
    search = assessment.get("search_log")
    if not isinstance(search, list) or any(not isinstance(x, str) for x in search):
        raise InvalidReuseAssessment("search_log must be a list of documented searches")
    candidates = assessment.get("candidates")
    if not isinstance(candidates, list):
        raise InvalidReuseAssessment("candidates must be a list")
    audited = []
    for i, item in enumerate(candidates):
        if not isinstance(item, dict):
            raise InvalidReuseAssessment(f"candidates[{i}] must be an object")
        n = _text(item, "name")
        source = _text(item, "source_url")
        if not n or not source:
            raise InvalidReuseAssessment(f"candidates[{i}] needs name and source_url")
        gates = {}
        for key in ("functional_test", "license_compatibility", "security_review", "maintenance_review"):
            state = item.get(key)
            if state not in STATES:
                raise InvalidReuseAssessment(f"candidates[{i}].{key} must be one of verified/failed/unknown")
            gates[key] = state
        audited.append({"name": n, "source_url": source, "gates": gates})
    qualified = [x for x in audited if all(v == GOOD for v in x["gates"].values())]
    uncertain = [x for x in audited if BAD not in x["gates"].values() and any(v == UNKNOWN for v in x["gates"].values())]
    failed = [x for x in audited if BAD in x["gates"].values()]

    if not acceptance:
        action = "define_independent_task_test"
        reason = "Freeze what user value means before browsing or generating new code"
    elif not search:
        action = "search_before_generation"
        reason = "Search and record prior code, packages and upstream projects before writing new code"
    elif qualified:
        action = "trial_verified_reuse"
        reason = "At least one candidate has all *self-reported* evidence gates marked verified; independently check before integration"
    elif uncertain:
        action = "verify_existing_candidates"
        reason = "Existing candidates have unresolved functional, license, security or maintenance evidence"
    elif not candidates:
        action = "expand_candidate_search"
        reason = "No candidates yet; expand time-boxed search before deciding to build"
    else:
        action = "consider_minimal_new_implementation"
        reason = "Current candidates failed one or more gates; compare with smaller upstream contribution or minimal build"

    return {
        "schema_version": "1.0",
        "task": name,
        "next_action": action,
        "reason": reason,
        "candidate_count": len(audited),
        "self_reported_qualified": [x["name"] for x in qualified],
        "unresolved": [x["name"] for x in uncertain],
        "failed_gates": {x["name"]: [k for k, v in x["gates"].items() if v == BAD] for x in failed},
        "disclaimer": (
            "This is a static self-reported evidence-check heuristic, NOT actual verification, "
            "license/security advice, task-completion evidence or measured energy/CO2 savings."
        ),
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="Offline reuse-first evidence gate")
    p.add_argument("--input", required=True, help="JSON assessment file")
    args = p.parse_args(argv)
    try:
        result = evaluate(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        p.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
