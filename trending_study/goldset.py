"""Offline scientific guardrails for pooled reuse-candidate judgments.

All input judgments are supplied, not independently verified by this CLI.
A judged pool is NOT the universe of reusable software.
"""
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import re

from .data_integrity import ResearchJSONError, load_research_json_file


LABELS = {"viable", "not_viable", "unknown"}
GATE_ALLOWED = {"pass", "fail", "unknown"}
_SHA = re.compile(r"^[0-9a-f]{64}$")


class GoldsetError(ValueError):
    """Invalid methodological input; refuse potentially misleading statistics."""


def _record(x, name):
    if not isinstance(x, dict):
        raise GoldsetError(f"{name} must be an object")
    return x


def _list(x, name):
    if not isinstance(x, list):
        raise GoldsetError(f"{name} must be a list")
    return x


def _nonempty(x, name):
    if not isinstance(x, str) or not x.strip():
        raise GoldsetError(f"{name} must be a nonempty string")
    return x.strip()


def _date(x, name):
    text = _nonempty(x, name)
    try:
        value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        # Finish exception handling before raising our public error. Keeping
        # the original exception as a cause can expose a private raw timestamp
        # in full CI/telemetry tracebacks despite a safe top-level message.
        value = None
    if value is None:
        raise GoldsetError(f"{name} must be an ISO8601 date-time")
    if value.tzinfo is None or value.utcoffset() is None:
        raise GoldsetError(f"{name} must have a timezone")
    return value.astimezone(timezone.utc)


def _candidate(c, taskid, baseline):
    # Caller-supplied task/candidate IDs are untrusted, possibly sensitive.
    # Do not echo these values in errors or CLI stderr.
    _record(c, "candidate")
    # A pooled benchmark must not quietly accept embedded prompts, contact
    # records or undeclared fields that were never part of the reviewed schema.
    # Reject unknown *names* without printing those potentially private keys.
    if set(c) - {"id", "final_label", "reviewer_labels",
                  "available_since_utc", "gates", "evidence_ref",
                  "adjudicator_ref"}:
        raise GoldsetError("candidate: unsupported fields")
    cid = _nonempty(c.get("id"), "candidate.id")
    label = c.get("final_label")
    if not isinstance(label, str) or label not in LABELS:
        raise GoldsetError("candidate: final_label must be viable/not_viable/unknown")
    evidence = c.get("evidence_ref")
    if evidence is not None and not isinstance(evidence, str):
        raise GoldsetError("candidate: evidence_ref must be string or null")
    gates = _record(c.get("gates"), "gates")
    required = ("functional", "license", "security", "maintenance")
    permitted = set(required) | {"availability"}
    if set(gates) - permitted:
        raise GoldsetError("candidate: unsupported gate names")
    for k in required:
        if not isinstance(gates.get(k), str) or gates[k] not in GATE_ALLOWED:
            raise GoldsetError(f"candidate: gate {k} must be pass/fail/unknown")
    if ("availability" in gates and
            (not isinstance(gates["availability"], str) or gates["availability"] not in GATE_ALLOWED)):
        raise GoldsetError("candidate: availability must be pass/fail/unknown")
    release_time = c.get("available_since_utc")
    if release_time is not None and _date(release_time, "available_since_utc") > baseline:
        if label == "viable" or gates.get("availability") == "pass":
            raise GoldsetError("candidate: released after task baseline cannot be available")
    reviewers = _list(c.get("reviewer_labels"), "reviewer_labels")
    if len(reviewers) != 2 or any(not isinstance(r, str) or r not in LABELS for r in reviewers):
        raise GoldsetError("candidate: exactly two reviewer labels required")
    if label != "unknown" and all(r == "unknown" for r in reviewers):
        raise GoldsetError("candidate: two unknown reviewer labels cannot establish viability/nonviability")
    # A single abstaining reviewer must instead have a declared adjudicator;
    # keep original third-reviewer structural protocol (not a human attestation).
    if label == "viable":
        if (any(gates[k] != "pass" for k in required)
                or ("availability" in gates and gates["availability"] != "pass")):
            raise GoldsetError("candidate: viable without full passing gates")
        if release_time is None or not evidence or not evidence.strip():
            raise GoldsetError("candidate: viable without dated availability and evidence")
    elif label == "not_viable":
        # A version first available after task baseline is not a viable historical
        # alternative, even if its functional/security/license gates pass now.
        if "fail" not in gates.values() or not evidence or not evidence.strip():
            raise GoldsetError("candidate: not viable requires failure evidence")
    if reviewers[0] != reviewers[1] and label != "unknown":
        if not isinstance(c.get("adjudicator_ref"), str) or not c["adjudicator_ref"].strip():
            raise GoldsetError("candidate: disagreement needs adjudicator_ref")
    if reviewers[0] == reviewers[1] and reviewers[0] != "unknown":
        if label not in (reviewers[0], "unknown"):
            raise GoldsetError("candidate: final label contradicts both raters")
    return cid, label, reviewers


def evaluate(payload, k=5):
    """Return per-task and system retrieval summaries with explicit unjudged bounds."""
    _record(payload, "payload")
    if set(payload) != {"schema_version", "dataset_kind", "tasks"}:
        raise GoldsetError("payload: unexpected or missing fields")
    if payload.get("schema_version") != "1.0" or payload.get("dataset_kind") not in ("synthetic", "pilot", "observational"):
        raise GoldsetError("expected schema_version=1.0 and dataset_kind synthetic/pilot/observational")
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise GoldsetError("k must be a positive integer")
    rows = []
    seen_taskids = set()
    for task in _list(payload.get("tasks"), "tasks"):
        _record(task, "task")
        if set(task) != {"task_id", "baseline_utc", "spec_sha256",
                         "acceptance_sha256", "candidates", "systems"}:
            raise GoldsetError("task: unexpected or missing fields")
        taskid = _nonempty(task.get("task_id"), "task_id")
        if taskid in seen_taskids:
            raise GoldsetError("duplicate task_id")
        seen_taskids.add(taskid)
        baseline = _date(task.get("baseline_utc"), "baseline_utc")
        if (payload["dataset_kind"] != "synthetic"
                and baseline > datetime.now(timezone.utc) + timedelta(minutes=5)):
            raise GoldsetError("pilot/observational task baseline cannot be future-dated")
        specsha = _nonempty(task.get("spec_sha256"), "spec_sha256")
        accsha = _nonempty(task.get("acceptance_sha256"), "acceptance_sha256")
        if not _SHA.fullmatch(specsha) or not _SHA.fullmatch(accsha):
            raise GoldsetError("task: specification/acceptance hashes must be lowercase SHA-256")
        candidates = {}
        agree = 0
        double_reviewed = 0
        for cand in _list(task.get("candidates"), "candidates"):
            cid, label, reviewers = _candidate(cand, taskid, baseline)
            if cid in candidates:
                raise GoldsetError("task: duplicate candidate id")
            candidates[cid] = label
            if reviewers[0] != "unknown" and reviewers[1] != "unknown":
                double_reviewed += 1
                if reviewers[0] == reviewers[1]:
                    agree += 1
        counts = {label: sum(v == label for v in candidates.values()) for label in LABELS}
        if counts["viable"]:
            opportunity = "viable_found_in_audited_pool"
        elif counts["unknown"]:
            opportunity = "unknown"
        else:
            opportunity = "none_found_in_audited_pool_not_global_absence"
        total_known_viable = counts["viable"]
        systems = []
        seen_sys = set()
        for system in _list(task.get("systems"), "systems"):
            _record(system, "system")
            if set(system) != {"name", "ranked_candidate_ids"}:
                raise GoldsetError("system: unexpected or missing fields")
            name = _nonempty(system.get("name"), "system.name")
            if name in seen_sys:
                raise GoldsetError("task: duplicate system")
            seen_sys.add(name)
            ranked = _list(system.get("ranked_candidate_ids"), "ranked_candidate_ids")
            if any(not isinstance(cid, str) or not cid.strip() for cid in ranked):
                raise GoldsetError("system: ranked candidate IDs must be nonempty strings")
            if len(set(ranked)) != len(ranked):
                raise GoldsetError("system: repeated candidate id")
            if any(cid not in candidates for cid in ranked):
                raise GoldsetError("system: unknown/unpooled candidate id; add it as unjudged instead of treating as irrelevant")
            top = ranked[:k]
            good = sum(candidates[cid] == "viable" for cid in top)
            missing = sum(candidates[cid] == "unknown" for cid in top)
            coverage = None if not top else (len(top)-missing)/len(top)
            systems.append({
                "name": name,
                "k": k,
                "returned_at_k": len(top),
                "unfilled_rank_slots_at_k": k - len(top),
                "judgment_coverage_of_returned": coverage,
                "unjudged_at_k": missing,
                "precision_at_k": good/k if missing == 0 else None,
                "precision_at_k_lower_bound": good/k,
                "precision_at_k_upper_bound": (good+missing)/k,
                "pooled_relative_recall_at_k": (good/total_known_viable if total_known_viable and missing == 0 else None),
                "warning": "P@K divides by K including missing rank slots; pooled relative recall is not absolute recall across all available software.",
            })
        rows.append({
            "task_id": taskid,
            "pool_total": len(candidates),
            "pool_verified_viable": counts["viable"],
            "pool_verified_not_viable": counts["not_viable"],
            "pool_unknown": counts["unknown"],
            "observed_opportunity": opportunity,
            "double_reviewed": double_reviewed,
            "raw_agreement": (agree/double_reviewed if double_reviewed else None),
            "systems": systems,
        })
    return {
        "schema_version": "1.0",
        "dataset_kind": payload["dataset_kind"],
        "task_count": len(rows),
        "results": rows,
        "disclaimer": "Input labels/evidence are self-provided and NOT verified by this program. Do not treat synthetic or pilot data as study findings; pool-relative recall is not population recall.",
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="Check and summarize an offline, adjudicated reuse candidate pool")
    p.add_argument("--input", required=True, help="JSON file containing tasks/candidates/systems")
    p.add_argument("--k", type=int, default=5)
    args = p.parse_args(argv)
    try:
        result = evaluate(load_research_json_file(args.input, max_bytes=1_000_000), k=args.k)
    except ResearchJSONError:
        # Never echo private duplicate-key text or input paths from the decoder.
        p.exit(2, "error: invalid or unsafe research JSON input\n")
    except OSError:
        p.exit(2, "error: input filesystem operation failed\n")
    except (ValueError, TypeError, RecursionError) as exc:
        p.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
