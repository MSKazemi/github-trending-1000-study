"""Offline, privacy-minimized cost audit tied to a frozen trial task denominator.

No telemetry is collected. All input must be supplied after an independently
authorized opt-in protocol; validation is not proof of consent or acceptance.
This tool never executes an agent, downloads dependencies, or estimates CO2.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import math
from pathlib import Path
import re

from .safe_io import disjoint, publish_json
from .trial import ARMS, TrialError, assign as trial_assign, audit as trial_audit


ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
PRICE = re.compile(r"(?:0|[1-9][0-9]{0,6})(?:\.[0-9]{1,6})?\Z")
COVERAGES = {"complete", "partial", "missing"}
HUMAN_CATEGORIES = {"plan", "prompt", "review", "repair", "ship", "other"}
KINDS = {"model_call", "tool_call", "ci_job", "retry", "idle"}
COST_BASES = {"provider_billed", "provider_estimate", "synthetic"}
ROOT_KEYS = {"schema_version", "dataset_kind", "protocol_id", "task_costs"}
TASK_KEYS = {"task_id", "coverage", "human_intervals", "agent_events", "budget"}
HUMAN_KEYS = {"actor_slot", "category", "started_at_utc", "ended_at_utc"}
EVENT_KEYS = {
    "event_id", "session_id", "kind", "started_at_utc", "ended_at_utc",
    "model_id", "tool_id", "input_tokens", "output_tokens",
    "cached_input_tokens", "amount_usd", "cost_basis",
}
BUDGET_KEYS = {
    "locked_at_utc", "max_human_minutes", "max_tool_calls",
    "max_retries", "max_event_cost_usd",
}


class CostAuditError(ValueError):
    """Rejected research expense record or unsafe incomplete denominator."""


def _object(value, name, keys):
    if not isinstance(value, dict):
        raise CostAuditError(f"{name} must be a JSON object")
    missing, extra = keys - set(value), set(value) - keys
    if missing or extra:
        raise CostAuditError(f"{name}: missing={sorted(missing)} unexpected={sorted(extra)}")
    return value


def _identifier(value, name):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise CostAuditError(f"{name} must be an opaque alphanumeric pseudonym, not free text")
    return value


def _timestamp(value, name):
    if not isinstance(value, str):
        raise CostAuditError(f"{name} must be a UTC ISO8601 timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CostAuditError(f"{name} must be a UTC ISO8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise CostAuditError(f"{name} must explicitly use UTC")
    return parsed.astimezone(timezone.utc)


def _interval(row, name, lower, upper):
    start = _timestamp(row.get("started_at_utc"), name + ".started_at_utc")
    end = _timestamp(row.get("ended_at_utc"), name + ".ended_at_utc")
    if not lower <= start < end or (upper is not None and end > upper):
        raise CostAuditError(f"{name}: interval must occur after frame lock and before task closure")
    return start, end


def _count(value, name):
    if value is not None and (type(value) is not int or value < 0):
        raise CostAuditError(f"{name} must be a nonnegative integer or null")
    return value


def _minutes(value, name):
    if value is not None and (
        isinstance(value, bool)
        or not isinstance(value, (float, int))
        or not math.isfinite(value)
        or value < 0
    ):
        raise CostAuditError(f"{name} must be a nonnegative finite number or null")
    return value


def _money(value, name):
    if value is None:
        return None
    if not isinstance(value, str) or not PRICE.fullmatch(value):
        raise CostAuditError(f"{name} must be a decimal string (up to six places) or null")
    return Decimal(value)


def _unique_json_fields(pairs):
    """Reject duplicate object keys rather than silently losing evidence."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise CostAuditError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _bad_json_constant(value):
    raise CostAuditError(f"nonfinite/nonstandard JSON constant {value!r}")


def _read_json(path):
    # Bound offline memory use; never transmit files or make network requests.
    if path.stat().st_size > 64 * 1024 * 1024:
        raise CostAuditError(f"input file exceeds 64 MiB limit: {path}")
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_json_fields,
        parse_constant=_bad_json_constant,
    )


def _canonical_hash(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")).hexdigest()


def _union_minutes(intervals):
    """Count wall time once even if multiple agents execute concurrently."""
    if not intervals:
        return 0.0
    length = timedelta()
    end = None
    for start, stop in sorted(intervals):
        if end is None or start >= end:
            length += stop - start
            end = stop
        elif stop > end:
            length += stop - end
            end = stop
    return round(length.total_seconds() / 60, 3)


def _budget_status(actual, maximum):
    if maximum is None:
        return "not_set"
    if actual is None:
        return "unknown"
    return "exceeded" if actual > maximum else "within"


def _parse_budget(budget, locked):
    if budget is None:
        return None
    _object(budget, "budget", BUDGET_KEYS)
    date = _timestamp(budget["locked_at_utc"], "budget.locked_at_utc")
    if date > locked:
        raise CostAuditError("budget must be locked no later than frame lock (self-reported)")
    _minutes(budget["max_human_minutes"], "budget.max_human_minutes")
    _count(budget["max_tool_calls"], "budget.max_tool_calls")
    _count(budget["max_retries"], "budget.max_retries")
    _money(budget["max_event_cost_usd"], "budget.max_event_cost_usd")
    return budget


def _summarize(rows):
    if not rows:
        return {
            "assigned": 0, "accepted": 0, "status_counts": {},
            "human_active_minutes_total": None, "model_calls_total": None,
            "tool_calls_total": None, "retries_total": None,
            "token_totals": {"input_tokens": None, "output_tokens": None, "cached_input_tokens": None},
            "observed_event_cost_usd": None, "cost_by_basis_usd": None,
            "cost_per_accepted_task_usd": None, "accepted_per_human_hour": None,
            "missing_human_tasks": 0, "missing_event_tasks": 0,
            "missing_monetary_tasks": 0,
        }
    accepted = sum(row["status"] == "accepted" for row in rows)
    def total_or_unknown(field):
        fields = [row[field] for row in rows]
        return sum(fields) if all(v is not None for v in fields) else None

    minutes = total_or_unknown("human_active_minutes")
    model_calls = total_or_unknown("model_calls")
    tool_calls = total_or_unknown("tool_calls")
    retries = total_or_unknown("retries")
    tokens = {
        key: total_or_unknown(key)
        for key in ("input_tokens", "output_tokens", "cached_input_tokens")
    }
    costs = [row["observed_event_cost_usd"] for row in rows]
    cost = sum((Decimal(v) for v in costs), Decimal("0")) if all(v is not None for v in costs) else None
    by_basis = defaultdict(lambda: Decimal("0"))
    if cost is not None:
        for row in rows:
            for basis, value in row["cost_by_basis_usd"].items():
                by_basis[basis] += Decimal(value)
    return {
        "assigned": len(rows),
        "accepted": accepted,
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "human_active_minutes_total": minutes,
        "model_calls_total": model_calls,
        "tool_calls_total": tool_calls,
        "retries_total": retries,
        "token_totals": tokens,
        "observed_event_cost_usd": str(cost) if cost is not None else None,
        "cost_by_basis_usd": ({k: str(v) for k, v in sorted(by_basis.items())} if cost is not None else None),
        "cost_per_accepted_task_usd": (
            str((cost / Decimal(accepted)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))
            if cost is not None and accepted > 0 else None
        ),
        "accepted_per_human_hour": (
            round(60 * accepted / minutes, 6)
            if minutes is not None and minutes > 0
            and not any(row["status"] == "pending" for row in rows) else None
        ),
        "missing_human_tasks": sum(row["human_active_minutes"] is None for row in rows),
        "missing_event_tasks": sum(row["model_calls"] is None for row in rows),
        "missing_monetary_tasks": sum(row["observed_event_cost_usd"] is None for row in rows),
    }


def audit_costs(frame, assignments, outcomes, ledger):
    """Audit *all assigned tasks* against the existing independent-outcome ledger."""
    assignment = trial_assign(frame)
    trial_audit(frame, assignments, outcomes)  # includes status/gate and all-task checks
    _object(ledger, "ledger", ROOT_KEYS)
    for key, expected in (
        ("schema_version", "1.0"),
        ("dataset_kind", assignment["dataset_kind"]),
        ("protocol_id", assignment["protocol_id"]),
    ):
        if ledger.get(key) != expected:
            raise CostAuditError(f"ledger.{key} disagrees with audited trial")
    records = ledger["task_costs"]
    if not isinstance(records, list):
        raise CostAuditError("task_costs must be a list")
    if len(records) > 10000:
        raise CostAuditError("task_costs exceeds bounded offline audit limit")
    outcomes_by_id = {row["task_id"]: row for row in outcomes["outcomes"]}
    arms = {row["task_id"]: row["arm"] for row in assignment["assigned"]}
    if len(records) != len(arms):
        raise CostAuditError("every randomized task needs one cost record, including failed/refused/pending")
    global_event_ids = set()
    actor_intervals = defaultdict(list)
    rows = []
    locked = _timestamp(frame["frame_locked_at_utc"], "frame_locked_at_utc")
    seen_tasks = set()

    for task in records:
        _object(task, "task_cost", TASK_KEYS)
        tid = _identifier(task["task_id"], "task_id")
        if tid not in arms or tid in seen_tasks:
            raise CostAuditError(f"task_id {tid} is unknown, excluded, or duplicated")
        seen_tasks.add(tid)
        coverage = _object(task["coverage"], f"{tid}.coverage", {"human", "events", "monetary"})
        if any(not isinstance(v, str) or v not in COVERAGES for v in coverage.values()):
            raise CostAuditError(f"{tid}: coverage must be complete/partial/missing")
        outcome = outcomes_by_id[tid]
        closed = outcome["closed_at_utc"]
        upper = _timestamp(closed, f"{tid}.closed_at_utc") if closed is not None else None

        humans = task["human_intervals"]
        if not isinstance(humans, list) or len(humans) > 100000:
            raise CostAuditError(f"{tid}: human_intervals must be a bounded list")
        if coverage["human"] == "missing" and humans:
            raise CostAuditError(f"{tid}: missing human coverage cannot contain intervals")
        minutes = 0.0
        for index, item in enumerate(humans):
            name = f"{tid}.human_intervals[{index}]"
            _object(item, name, HUMAN_KEYS)
            actor = _identifier(item["actor_slot"], name + ".actor_slot")
            if not isinstance(item["category"], str) or item["category"] not in HUMAN_CATEGORIES:
                raise CostAuditError(f"{name}: unknown work category")
            start, end = _interval(item, name, locked, upper)
            minutes += (end - start).total_seconds() / 60
            actor_intervals[actor].append((start, end, tid))
        minutes = round(minutes, 3) if coverage["human"] == "complete" else None
        recorded = outcome.get("human_active_minutes")
        if minutes is not None and (
            recorded is None or not math.isclose(minutes, recorded, abs_tol=0.02)
        ):
            raise CostAuditError(f"{tid}: complete human intervals disagree with trial outcome minutes")

        events = task["agent_events"]
        if not isinstance(events, list) or len(events) > 100000:
            raise CostAuditError(f"{tid}: agent_events must be a bounded list")
        if coverage["events"] == "missing" and events:
            raise CostAuditError(f"{tid}: missing event coverage cannot contain events")
        model_count = tool_count = retry_count = 0
        token_totals = {"input_tokens": 0, "output_tokens": 0, "cached_input_tokens": 0}
        token_unknown = set()
        costs_by_basis = defaultdict(lambda: Decimal("0"))
        observed_cost = Decimal("0")
        cost_unknown = False
        spans = []
        for index, event in enumerate(events):
            name = f"{tid}.agent_events[{index}]"
            _object(event, name, EVENT_KEYS)
            eid = _identifier(event["event_id"], name + ".event_id")
            _identifier(event["session_id"], name + ".session_id")
            if eid in global_event_ids:
                raise CostAuditError(f"duplicate event_id {eid}")
            global_event_ids.add(eid)
            kind = event["kind"]
            if not isinstance(kind, str) or kind not in KINDS:
                raise CostAuditError(f"{name}: unsupported event kind")
            spans.append(_interval(event, name, locked, upper))
            model = event["model_id"]
            tool = event["tool_id"]
            if kind == "model_call":
                _identifier(model, name + ".model_id")
                if tool is not None:
                    raise CostAuditError(f"{name}: model_call must have null tool_id")
                model_count += 1
                for key in token_totals:
                    count = _count(event[key], name + "." + key)
                    if count is None:
                        token_unknown.add(key)
                    else:
                        token_totals[key] += count
                if (event["input_tokens"] is not None
                    and event["cached_input_tokens"] is not None
                    and event["cached_input_tokens"] > event["input_tokens"]):
                    raise CostAuditError(f"{name}: cached input cannot exceed total input tokens")
            else:
                if model is not None or any(event[key] is not None for key in token_totals):
                    raise CostAuditError(f"{name}: non-model event cannot claim model tokens/model_id")
                if kind in ("tool_call", "ci_job"):
                    _identifier(tool, name + ".tool_id")
                    tool_count += int(kind == "tool_call")
                elif tool is not None:
                    raise CostAuditError(f"{name}: retry/idle must have null tool_id")
                retry_count += int(kind == "retry")
            amount = _money(event["amount_usd"], name + ".amount_usd")
            basis = event["cost_basis"]
            if kind in ("retry", "idle"):
                if amount is not None or basis is not None:
                    raise CostAuditError(f"{name}: retries/idle cannot independently double-bill events")
            elif amount is None:
                if basis is not None:
                    raise CostAuditError(f"{name}: unknown amount requires null basis")
                cost_unknown = True
            else:
                if not isinstance(basis, str) or basis not in COST_BASES or (
                    ledger["dataset_kind"] != "synthetic" and basis == "synthetic"
                ):
                    raise CostAuditError(f"{name}: cost basis must identify provenance")
                observed_cost += amount
                costs_by_basis[basis] += amount
        complete_events = coverage["events"] == "complete"
        complete_money = complete_events and coverage["monetary"] == "complete"
        if complete_money and cost_unknown:
            raise CostAuditError(f"{tid}: complete monetary coverage conflicts with unknown event costs")
        if coverage["monetary"] == "missing" and any(
            event["amount_usd"] is not None for event in events
        ):
            raise CostAuditError(f"{tid}: missing monetary coverage cannot contain amounts")

        metrics = {
            "task_id": tid,
            "arm": arms[tid],
            "status": outcome["status"],
            "coverage": dict(coverage),
            "human_active_minutes": minutes,
            "observed_agent_events": len(events),
            "recorded_event_wall_minutes": _union_minutes(spans) if complete_events else None,
            "model_calls": model_count if complete_events else None,
            "tool_calls": tool_count if complete_events else None,
            "retries": retry_count if complete_events else None,
            "observed_event_cost_usd": str(observed_cost) if complete_money else None,
            "cost_by_basis_usd": (
                {k: str(v) for k, v in sorted(costs_by_basis.items())}
                if complete_money else None
            ),
        }
        for key in token_totals:
            metrics[key] = token_totals[key] if complete_events and key not in token_unknown else None

        budget = _parse_budget(task["budget"], locked)
        if budget is None:
            metrics["budget_alerts"] = None
        else:
            cap = _money(budget["max_event_cost_usd"], "budget.max_event_cost_usd")
            metrics["budget_alerts"] = {
                "human_minutes": _budget_status(minutes, budget["max_human_minutes"]),
                "tool_calls": _budget_status(metrics["tool_calls"], budget["max_tool_calls"]),
                "retries": _budget_status(metrics["retries"], budget["max_retries"]),
                "event_cost_usd": _budget_status(
                    Decimal(metrics["observed_event_cost_usd"])
                    if metrics["observed_event_cost_usd"] is not None else None, cap
                ),
            }
        rows.append(metrics)

    if seen_tasks != set(arms):
        raise CostAuditError(f"all assigned tasks required, missing={sorted(set(arms) - seen_tasks)}")
    # One human actor's overlapping intervals across tasks would inflate human hours.
    # Separate actor aliases for the same person cannot be detected by the tool.
    for actor, spans in actor_intervals.items():
        ordered = sorted(spans)
        for previous, current in zip(ordered, ordered[1:]):
            if current[0] < previous[1]:
                raise CostAuditError(f"overlapping human intervals for actor_slot {actor}")

    rows.sort(key=lambda row: row["task_id"])
    return {
        "schema_version": "1.0",
        "dataset_kind": assignment["dataset_kind"],
        "protocol_id": assignment["protocol_id"],
        "frame_sha256": assignment["frame_sha256"],
        "outcomes_canonical_sha256": _canonical_hash(outcomes),
        "ledger_canonical_sha256": _canonical_hash(ledger),
        "trial_status": "synthetic_demonstration" if assignment["dataset_kind"] == "synthetic"
                        else "self_declared_opt_in_pilot_not_independently_verified",
        "overall": _summarize(rows),
        "by_arm": {
            arm: _summarize([row for row in rows if row["arm"] == arm])
            for arm in ARMS
        },
        "tasks": rows,
        "limitations": [
            "Input is precollected offline; validation cannot authenticate consent, time logs, human identity separation or independent task acceptance.",
            "Complete is self-declared; no agent-model or cloud provider automatically instrumented.",
            "Known-only costs are billed/estimated/synthetic event amounts, not whole-task human, CI, subscription, energy or carbon costs.",
            "Unknown/partial values stay null; output denominators include failed, abandoned, refused and pending tasks.",
            "Concurrent event durations are unioned within tasks; human actor-slot overlap is rejected, but aliases cannot be independently linked.",
            "Do not infer a causal effect, universal model token accounting, productivity improvement or CO2 savings.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline, fail-closed opt-in task cost ledger audit")
    parser.add_argument("--frame", required=True, type=Path)
    parser.add_argument("--assignments", required=True, type=Path)
    parser.add_argument("--outcomes", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path, help="Precollected redacted task-cost ledger")
    parser.add_argument("--output", type=Path, help="New write-once JSON report; stdout if omitted")
    args = parser.parse_args(argv)
    try:
        if args.output:
            disjoint(args.frame, args.assignments, args.outcomes, args.input, args.output)
        frame = _read_json(args.frame)
        allocations = _read_json(args.assignments)
        outcomes = _read_json(args.outcomes)
        ledger = _read_json(args.input)
        report = audit_costs(frame, allocations, outcomes, ledger)
        if args.output:
            publish_json(args.output, report)
        else:
            print(json.dumps(report, sort_keys=True, indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(2, f"task cost audit rejected: {exc}\n")


if __name__ == "__main__":
    main()
