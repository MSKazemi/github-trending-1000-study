"""Offline task-frame randomization and all-assigned-task pilot audit.

This utility validates user-supplied data but cannot prove a real frame was
prospectively locked, consent obtained, or acceptance independently assessed.
Never run experimental code, download packages, or infer causal effects here.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import re

from .safe_io import disjoint, publish_json


ARMS = ("human_usual", "human_reuse_first", "agent_usual", "agent_reuse_first")
BLOCK = ("language", "project_type", "difficulty", "experience_band")
EXCLUSION_REASONS = {"safety_prohibited", "duplicate", "out_of_scope"}
STATUSES = {"accepted", "failed", "abandoned", "refused", "pending"}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
FRAME_KEYS = {"schema_version", "dataset_kind", "protocol_id", "frame_source_ref", "frame_locked_at_utc", "randomization_seed", "design", "ethics_review_ref", "tasks"}
TASK_KEYS = {"task_id", "family_id", "cluster_id", "baseline_utc", "spec_sha256", "acceptance_sha256", "independent_acceptance_ref", "language", "project_type", "difficulty", "experience_band", "source_kind", "consent_ref", "eligibility_status", "exclusion_reason"}
OUTCOME_KEYS = {"task_id", "status", "human_active_minutes", "closed_at_utc", "independent_review_ref", "security_gate", "rights_gate", "protocol_deviation"}


class TrialError(ValueError):
    """Invalid input that would undermine the proposed experimental denominator."""


def _obj(value, name):
    if not isinstance(value, dict):
        raise TrialError(f"{name} must be a JSON object")
    return value


def _keys(value, allowed, name):
    extra = set(value) - allowed
    if extra:
        raise TrialError(f"{name}: unexpected field(s): {', '.join(sorted(extra))}")


def _name(value, name):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise TrialError(f"{name} must be a pseudonymous, nonempty identifier (max 80 characters)")
    return value


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise TrialError(f"{name} must be a nonempty string")
    return value.strip()


def _utc(value, name):
    raw = _text(value, name)
    try:
        timestamp = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise TrialError(f"{name} must be an ISO8601 UTC timestamp") from exc
    if timestamp.tzinfo is None or timestamp.utcoffset() != timedelta(0):
        raise TrialError(f"{name} must explicitly use UTC")
    return timestamp.astimezone(timezone.utc)


def _sha(value, name):
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise TrialError(f"{name} must be a lowercase SHA-256 digest")


def _hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def _frame(frame):
    _obj(frame, "frame")
    _keys(frame, FRAME_KEYS, "frame")
    if frame.get("schema_version") != "1.0" or frame.get("design") != "factorial_2x2":
        raise TrialError("expected schema_version=1.0 and design=factorial_2x2")
    kind = frame.get("dataset_kind")
    if kind not in ("synthetic", "pilot"):
        raise TrialError("dataset_kind must be synthetic or pilot; confirmatory registration is not supported")
    _name(frame.get("protocol_id"), "protocol_id")
    _text(frame.get("frame_source_ref"), "frame_source_ref")
    locked = _utc(frame.get("frame_locked_at_utc"), "frame_locked_at_utc")
    seed = frame.get("randomization_seed")
    if isinstance(seed, bool) or not isinstance(seed, int) or not (0 <= seed < 2**63):
        raise TrialError("randomization_seed must be a nonnegative integer smaller than 2**63")
    if kind == "pilot":
        if locked > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise TrialError("pilot frame lock timestamp cannot be in the future")
        _text(frame.get("ethics_review_ref"), "ethics_review_ref")
    elif frame.get("ethics_review_ref") is not None:
        raise TrialError("synthetic frame must have null ethics_review_ref")
    tasks = frame.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise TrialError("tasks must be a nonempty list including preassignment exclusions")
    seen_ids = set()
    cluster_blocks = {}
    family_clusters = {}
    eligible = 0
    for task in tasks:
        _obj(task, "task")
        _keys(task, TASK_KEYS, "task")
        tid = _name(task.get("task_id"), "task_id")
        if tid in seen_ids:
            raise TrialError(f"duplicate task_id {tid}")
        seen_ids.add(tid)
        cluster = _name(task.get("cluster_id"), f"{tid}.cluster_id")
        family = _name(task.get("family_id"), f"{tid}.family_id")
        baseline = _utc(task.get("baseline_utc"), f"{tid}.baseline_utc")
        if baseline > locked:
            raise TrialError(f"{tid}: baseline is later than locked frame")
        for field in ("spec_sha256", "acceptance_sha256"):
            _sha(task.get(field), f"{tid}.{field}")
        _text(task.get("independent_acceptance_ref"), f"{tid}.independent_acceptance_ref")
        block = tuple(_name(task.get(key), f"{tid}.{key}") for key in BLOCK)
        if cluster in cluster_blocks and cluster_blocks[cluster] != block:
            raise TrialError(f"cluster_id {cluster} spans different blocking strata")
        cluster_blocks[cluster] = block
        if family in family_clusters and family_clusters[family] != cluster:
            raise TrialError(f"family_id {family} appears in multiple clusters (potential carryover)")
        family_clusters[family] = cluster
        if kind == "synthetic":
            if task.get("source_kind") != "synthetic" or task.get("consent_ref") is not None:
                raise TrialError(f"{tid}: synthetic source_kind required and consent_ref must be null")
        elif task.get("source_kind") != "opt_in":
            raise TrialError(f"{tid}: pilot source_kind must be opt_in")
        else:
            _text(task.get("consent_ref"), f"{tid}.consent_ref")
        status = task.get("eligibility_status")
        if status == "eligible":
            if task.get("exclusion_reason") is not None:
                raise TrialError(f"{tid}: eligible task cannot have exclusion_reason")
            eligible += 1
        elif status == "excluded_pre_assignment":
            if task.get("exclusion_reason") not in EXCLUSION_REASONS:
                raise TrialError(f"{tid}: preassignment exclusion requires a prespecified reason")
        else:
            raise TrialError(f"{tid}: eligibility_status must be eligible/excluded_pre_assignment")
    if not eligible:
        raise TrialError("frame has no eligible tasks")
    return locked


def assign(frame):
    """Deterministic cluster randomization within blocks; no reuse-availability selection."""
    _frame(frame)
    cluster_tasks = defaultdict(list)
    blocks = {}
    excluded = []
    for task in frame["tasks"]:
        if task["eligibility_status"] == "eligible":
            cid = task["cluster_id"]
            cluster_tasks[cid].append(task)
            blocks[cid] = tuple(task[field] for field in BLOCK)
        else:
            excluded.append({"task_id": task["task_id"], "reason": task["exclusion_reason"]})
    by_block = defaultdict(list)
    for cid, block in blocks.items():
        by_block[block].append(cid)
    allocations = {}
    for block, cids in sorted(by_block.items()):
        # Hash-ranked clusters and per-batch arms are deterministic on all Python versions.
        # Balanced to within one *cluster* per arm within each prespecified block.
        prefix = f"{frame['randomization_seed']}:{_hash(list(block))}:"
        cids = sorted(cids, key=lambda cid: (hashlib.sha256((prefix + cid).encode()).hexdigest(), cid))
        for index, cid in enumerate(cids):
            batch = index // len(ARMS)
            cycle = sorted(ARMS, key=lambda arm: hashlib.sha256((prefix + str(batch) + ':' + arm).encode()).hexdigest())
            allocations[cid] = cycle[index % len(ARMS)]
    assigned = []
    for cid, tasks in cluster_tasks.items():
        for task in tasks:
            assigned.append({"task_id": task["task_id"], "cluster_id": cid,
                             "stratum": {key: task[key] for key in BLOCK}, "arm": allocations[cid]})
    assigned.sort(key=lambda x: x["task_id"])
    excluded.sort(key=lambda x: x["task_id"])
    return {
        "schema_version": "1.0", "dataset_kind": frame["dataset_kind"],
        "protocol_id": frame["protocol_id"], "design": frame["design"],
        "frame_sha256": _hash(frame), "frame_locked_at_utc": frame["frame_locked_at_utc"],
        "randomization_seed": frame["randomization_seed"],
        "assigned": assigned, "excluded_before_assignment": excluded,
        "allocation_counts": dict(sorted(Counter(row["arm"] for row in assigned).items())),
        "warning": "Offline planned assignment only. Real prospectivity, consent and independent acceptance require external review.",
    }


def audit(frame, assignments, outcomes):
    """Audit the all-assigned-task ITT denominator; no significance or energy claim."""
    expected = assign(frame)
    if assignments != expected:
        raise TrialError("assignments disagree with recalculated locked-frame assignment")
    _obj(outcomes, "outcomes")
    required = {"schema_version", "dataset_kind", "protocol_id", "outcomes"}
    if not required.issubset(outcomes) or set(outcomes) - required - {"frame_sha256"}:
        raise TrialError("outcomes must contain schema_version/dataset_kind/protocol_id/outcomes; optional frame_sha256")
    if expected["dataset_kind"] == "pilot" and "frame_sha256" not in outcomes:
        raise TrialError("pilot outcomes require frame_sha256 binding to the assigned task frame")
    if "frame_sha256" in outcomes and outcomes["frame_sha256"] != expected["frame_sha256"]:
        raise TrialError("outcomes.frame_sha256 does not match assigned task frame")
    for key in ("schema_version", "dataset_kind", "protocol_id"):
        if outcomes.get(key) != expected[key]:
            raise TrialError(f"outcomes.{key} mismatches frame")
    rows = outcomes["outcomes"]
    if not isinstance(rows, list):
        raise TrialError("outcomes.outcomes must be a list")
    actual = {}
    locked = _utc(frame["frame_locked_at_utc"], "frame_locked_at_utc")
    for record in rows:
        _obj(record, "outcome")
        _keys(record, OUTCOME_KEYS, "outcome")
        tid = _name(record.get("task_id"), "outcome.task_id")
        if tid in actual:
            raise TrialError(f"duplicate outcome for {tid}")
        actual[tid] = record
        status = record.get("status")
        if status not in STATUSES:
            raise TrialError(f"{tid}: invalid status")
        minutes = record.get("human_active_minutes")
        if minutes is not None and (isinstance(minutes, bool) or not isinstance(minutes, (int, float)) or not (0 <= minutes < float('inf'))):
            raise TrialError(f"{tid}: human_active_minutes must be nonnegative finite number or null")
        closed = record.get("closed_at_utc")
        if status == "pending":
            if closed is not None:
                raise TrialError(f"{tid}: pending must have null closed_at_utc")
        elif closed is None or _utc(closed, f"{tid}.closed_at_utc") < locked:
            raise TrialError(f"{tid}: non-pending outcome must close after frame lock")
        if status == "accepted":
            _text(record.get("independent_review_ref"), f"{tid}.independent_review_ref")
            if record.get("security_gate") != "pass" or record.get("rights_gate") != "pass":
                raise TrialError(f"{tid}: accepted outcome requires independent safety/rights passes")
        else:
            if record.get("security_gate") not in ("pass", "fail", "unknown", None) or record.get("rights_gate") not in ("pass", "fail", "unknown", None):
                raise TrialError(f"{tid}: invalid gate")
        deviation = record.get("protocol_deviation")
        if deviation is not None and (not isinstance(deviation, str) or not deviation.strip()):
            raise TrialError(f"{tid}: protocol_deviation must be nonempty string or null")
    assigned_ids = {r["task_id"] for r in expected["assigned"]}
    if set(actual) != assigned_ids:
        raise TrialError(f"every assigned task needs an outcome record, including pending/refused; missing={sorted(assigned_ids - set(actual))}, unexpected={sorted(set(actual) - assigned_ids)}")
    def summarize(arm_rows):
        if not arm_rows:
            return {"assigned": 0, "accepted": 0, "status_counts": {}, "accepted_rate_lower": None,
                    "accepted_rate_upper": None, "human_active_minutes_total": None, "accepted_per_human_hour": None}
        counts = Counter(r["status"] for r in arm_rows)
        elapsed = [r.get("human_active_minutes") for r in arm_rows]
        complete = all(t is not None for t in elapsed)
        total = sum(elapsed) if complete else None
        successes = counts["accepted"]
        n = len(arm_rows)
        return {"assigned": n, "accepted": successes, "status_counts": dict(sorted(counts.items())),
                "accepted_rate_lower": successes / n,
                "accepted_rate_upper": (successes + counts["pending"]) / n,
                "human_active_minutes_total": total,
                "accepted_per_human_hour": (successes * 60 / total if total is not None and total > 0 and counts["pending"] == 0 else None)}

    by_arm = {arm: summarize([actual[r["task_id"]] for r in expected["assigned"] if r["arm"] == arm]) for arm in ARMS}
    by_workflow = {
        mode: summarize([actual[r["task_id"]] for r in expected["assigned"] if r["arm"].endswith(mode)])
        for mode in ("usual", "reuse_first")
    }
    return {
        "schema_version": "1.0", "dataset_kind": expected["dataset_kind"], "protocol_id": expected["protocol_id"],
        "frame_sha256": expected["frame_sha256"], "sampled_tasks": len(frame["tasks"]),
        "preassignment_exclusions": len(expected["excluded_before_assignment"]),
        "all_assigned_tasks": len(expected["assigned"]), "outcome_records": len(actual),
        "missing_human_minutes": sum(actual[i].get("human_active_minutes") is None for i in assigned_ids),
        "pending_count": sum(actual[i]["status"] == "pending" for i in assigned_ids),
        "by_arm": by_arm, "by_workflow": by_workflow,
        "warning": "Descriptive synthetic/pilot audit only; no causal effect, preregistration, safety certification or energy/carbon result.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline reuse-first trial frame, allocation and outcome audit")
    commands = parser.add_subparsers(dest="command", required=True)
    allocation = commands.add_parser("assign", help="validate prospective frame and write deterministic assignment")
    allocation.add_argument("--frame", required=True)
    allocation.add_argument("--output", required=True)
    checks = commands.add_parser("audit", help="validate all assigned outcomes and show descriptive ITT audit")
    checks.add_argument("--frame", required=True)
    checks.add_argument("--assignments", required=True)
    checks.add_argument("--outcomes", required=True)
    args = parser.parse_args(argv)
    try:
        frame = json.loads(Path(args.frame).read_text(encoding="utf-8"))
        if args.command == "assign":
            artifact = assign(frame)
            # Publication is exclusive and staged: no input/output alias, no
            # overwrite race between a preflight check and writing the plan.
            disjoint(args.frame, args.output)
            target = Path(args.output)
            publish_json(target, artifact)
            print(json.dumps({"assigned": len(artifact["assigned"]), "excluded_pre_assignment": len(artifact["excluded_before_assignment"]), "frame_sha256": artifact["frame_sha256"], "path": str(target)}))
        else:
            assignments = json.loads(Path(args.assignments).read_text(encoding="utf-8"))
            outcomes = json.loads(Path(args.outcomes).read_text(encoding="utf-8"))
            print(json.dumps(audit(frame, assignments, outcomes), indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, OverflowError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
