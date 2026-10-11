"""Conservative, non-scoring decision aid for early open-source project ideas.

This is a *heuristic*, not a scientific effectiveness classifier. It never
reads private telemetry, contacts GitHub, or learns from fabricated examples.
"""
import argparse
import json
from pathlib import Path

SCHEMA_VERSION = "1.0"
EVIDENCE = {"none", "self-test", "external-interview", "independent-task", "repeat-use", "research-replication"}
RISKS = {"low", "medium", "high"}
SECURITY = {"not_done", "pass", "issues_found", "not_applicable"}
EFFORT_FIELDS = ("planning_minutes", "prompt_minutes", "review_minutes", "repair_minutes", "ship_minutes", "followup_minutes")


class InvalidCard(ValueError):
    """Invalid user-supplied project assessment."""


def _object(value, field):
    if not isinstance(value, dict):
        raise InvalidCard(f"{field} must be an object")
    return value


def _text(value, field):
    if not isinstance(value, str):
        raise InvalidCard(f"{field} must be a string")
    return value.strip()


def _nonnegative(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0 or value != value or value == float("inf"):
        raise InvalidCard(f"{field} must be a finite nonnegative number")
    return value


def evaluate(card):
    """Return a next-action recommendation, NOT a numerical value/quality score."""
    _object(card, "card")
    if card.get("schema_version") != SCHEMA_VERSION:
        raise InvalidCard("schema_version must be 1.0")
    project = _text(card.get("project_name"), "project_name")
    project_type = _text(card.get("project_type"), "project_type")
    if not project or not project_type:
        raise InvalidCard("project_name and project_type cannot be blank")
    target = _text(card.get("target_user"), "target_user")
    problem = _text(card.get("problem_statement"), "problem_statement")
    alternative = _text(card.get("existing_alternative"), "existing_alternative")
    differentiator = _text(card.get("differentiator"), "differentiator")
    acceptance = _text(card.get("acceptance_task"), "acceptance_task")

    risk = card.get("risk_level")
    review = card.get("security_review")
    if risk not in RISKS or review not in SECURITY:
        raise InvalidCard("risk_level or security_review is not a known value")

    evidence = _object(card.get("independent_evidence"), "independent_evidence")
    kind = evidence.get("kind")
    if kind not in EVIDENCE:
        raise InvalidCard("independent_evidence.kind is not a known value")
    count = _nonnegative(evidence.get("count"), "independent_evidence.count")
    if not isinstance(count, int):
        raise InvalidCard("independent_evidence.count must be an integer")

    task = _object(card.get("task_evaluation"), "task_evaluation")
    attempted = _nonnegative(task.get("attempted"), "task_evaluation.attempted")
    succeeded = _nonnegative(task.get("succeeded"), "task_evaluation.succeeded")
    if not isinstance(attempted, int) or not isinstance(succeeded, int) or succeeded > attempted:
        raise InvalidCard("task attempts and successes must be integers with succeeded <= attempted")
    if not isinstance(task.get("acceptance_criteria_frozen"), bool):
        raise InvalidCard("task_evaluation.acceptance_criteria_frozen must be true or false")

    cost = card.get("effort", {})
    _object(cost, "effort")
    known_effort = all(name in cost for name in EFFORT_FIELDS)
    human_minutes = None
    if known_effort:
        human_minutes = sum(_nonnegative(cost[name], "effort." + name) for name in EFFORT_FIELDS)
    for key, value in cost.items():
        if key in EFFORT_FIELDS or key in ("input_tokens", "output_tokens", "cached_tokens", "cash_cost"):
            _nonnegative(value, "effort." + key)
    known_tokens = "input_tokens" in cost and "output_tokens" in cost
    total_tokens = (cost["input_tokens"] + cost["output_tokens"]) if known_tokens else None
    if known_tokens and (not isinstance(cost["input_tokens"], int) or not isinstance(cost["output_tokens"], int)):
        raise InvalidCard("token counts must be integers")

    signals = []
    gaps = []
    if not target or not problem:
        next_action = "define_problem"
        gaps.append("Specify a real user and a concrete problem before generating code")
    elif not alternative or not differentiator:
        next_action = "compare_existing_alternatives"
        gaps.append("Compare reuse, extension or doing nothing before creating a new tool")
    elif not acceptance or not task["acceptance_criteria_frozen"]:
        next_action = "freeze_acceptance_task"
        gaps.append("Define and freeze an independent end-to-end acceptance task")
    elif review == "issues_found" or (risk in ("medium", "high") and review != "pass"):
        next_action = "security_review_before_release"
        gaps.append("Do not publish high-consequence functionality without adequate risk review")
    elif attempted > 0 and succeeded < attempted:
        next_action = "repair_and_retest"
        gaps.append("Some independent task attempts failed; fix observed usability or correctness gaps")
    elif attempted == 0:
        next_action = "run_independent_task_test"
        gaps.append("No predefined user task has yet been tested")
    elif kind in ("none", "self-test") or count == 0:
        next_action = "seek_independent_evidence"
        gaps.append("A maintainer-only successful demo cannot demonstrate independent usefulness")
    elif kind in ("external-interview", "independent-task"):
        next_action = "test_repeat_value"
        gaps.append("Initial independent evidence is not yet repeat-use or long-term viability evidence")
    else:
        next_action = "continue_with_followup"
        signals.append("Repeat-use or external research-replication evidence recorded; confirm quality and maintenance")

    evidence_level = "concept"
    if attempted > 0 and succeeded > 0:
        evidence_level = "task_demonstrated"
    if count > 0 and kind in ("independent-task", "repeat-use", "research-replication") and attempted > 0 and succeeded > 0:
        evidence_level = "externally_tested"
    if kind == "repeat-use" and count > 0:
        evidence_level = "reported_repeat_use_unverified"
    elif kind == "research-replication" and count > 0:
        evidence_level = "reported_research_replication_unverified"
    if not known_effort:
        gaps.append("Total human-active effort is unknown; do not treat it as zero")
    if not known_tokens:
        gaps.append("Token consumption is unknown; do not treat it as zero")
    if risk == "low" and review == "not_done":
        gaps.append("Security review has not been performed; low risk is self-declared")
    if kind in ("repeat-use", "research-replication"):
        gaps.append("Evidence was self-reported in this card, not independently audited")

    budgets = _object(card.get("budgets", {}), "budgets")
    alerts = []
    for name, actual in (("max_human_minutes", human_minutes), ("max_total_tokens", total_tokens)):
        if name in budgets:
            bound = _nonnegative(budgets[name], "budgets." + name)
            if actual is None:
                alerts.append(f"Cannot check {name}: relevant measurements are missing")
            elif actual > bound:
                alerts.append(f"Measured value exceeds self-imposed {name}; investigate before continuing")
    return {
        "schema_version": SCHEMA_VERSION,
        "project_name": project,
        "decision": next_action,
        "evidence_level": evidence_level,
        "task_attempts": attempted,
        "task_successes": succeeded,
        "reported_independent_evidence": {"kind": kind, "count": count},
        "human_active_minutes": human_minutes,
        "observed_input_plus_output_tokens": total_tokens,
        "budget_alerts": alerts,
        "reasons": signals + gaps,
        "disclaimer": "Heuristic next-action aid only. Not proof of product usefulness, efficacy or safety.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Evaluate an idea with a conservative evidence gate")
    parser.add_argument("--input", required=True, help="Project assessment JSON file")
    parser.add_argument("--output", help="Optional JSON output file; otherwise stdout")
    args = parser.parse_args(argv)
    try:
        result = evaluate(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        parser.exit(2, f"error: {exc}\n")
    payload = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
