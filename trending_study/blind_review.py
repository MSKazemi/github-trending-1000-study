"""Prepare blinded candidate packets and audit *self-reported* independent reviews.

The program never retrieves or executes third-party code, authenticates reviewers,
verifies external evidence, or converts unjudged candidates into negative labels.
Reviewers' recorded assertions are not an independent scientific gold standard.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


class ReviewError(ValueError):
    """Invalid, incomplete, or scientifically misleading review input."""


_SHA = re.compile(r"^[0-9a-f]{64}$")
_LABELS = {"viable", "not_viable", "unknown"}
_GATES = ("functional", "license", "security", "maintenance", "availability")
_STATES = {"pass", "fail", "unknown"}
_CHANNELS = {"local", "registry", "code_host", "lexical", "semantic", "expert", "deep_audit"}


def _exact(obj, fields, name):
    if not isinstance(obj, dict) or set(obj) != set(fields):
        raise ReviewError(f"{name} must have exactly: {', '.join(sorted(fields))}")
    return obj


def _string(value, name, max_length=1024):
    if not isinstance(value, str) or not value.strip() or len(value) > max_length:
        raise ReviewError(f"{name} must be nonempty text <= {max_length} characters")
    return value.strip()


def _sha(value, name):
    if not isinstance(value, str) or not _SHA.fullmatch(value):
        raise ReviewError(f"{name} must be lowercase SHA-256 hex")
    return value


def _utc(value, name):
    try:
        value = datetime.fromisoformat(_string(value, name).replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReviewError(f"{name} must be an ISO-8601 timestamp") from exc
    if value.tzinfo is None or value.utcoffset() != timezone.utc.utcoffset(value):
        raise ReviewError(f"{name} must use UTC")
    return value.astimezone(timezone.utc)


def _url(value, name):
    text = _string(value, name)
    parts = urlsplit(text)
    if parts.scheme != "https" or not parts.hostname or parts.username or parts.password or any(ch.isspace() for ch in text):
        raise ReviewError(f"{name} must be an HTTPS evidence URL without credentials")
    return text


def fingerprint(obj):
    """Digest a *parsed* pool; whitespace changes do not change the fingerprint."""
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True, allow_nan=False).encode("utf-8")).hexdigest()


def validate_pool(pool):
    _exact(pool, {"schema_version", "dataset_kind", "pool_id", "tasks"}, "pool")
    if pool["schema_version"] != "1.0" or pool["dataset_kind"] not in ("synthetic", "pilot", "observational"):
        raise ReviewError("pool schema_version=1.0; dataset_kind=synthetic/pilot/observational")
    _string(pool["pool_id"], "pool_id", 128)
    tasks = pool["tasks"]
    if not isinstance(tasks, list) or not 1 <= len(tasks) <= 200:
        raise ReviewError("tasks must contain 1..200 records")
    seen_tasks = set()
    indexes = {}
    for task in tasks:
        _exact(task, {"task_id", "task_ref", "baseline_utc", "spec_sha256", "acceptance_sha256",
                      "candidates", "retrieval_runs"}, "task")
        tid = _string(task["task_id"], "task_id", 128)
        if tid in seen_tasks:
            raise ReviewError(f"duplicate task_id {tid}")
        seen_tasks.add(tid)
        _url(task["task_ref"], "task_ref")
        baseline = _utc(task["baseline_utc"], "baseline_utc")
        _sha(task["spec_sha256"], "spec_sha256")
        _sha(task["acceptance_sha256"], "acceptance_sha256")
        candidates = task["candidates"]
        if not isinstance(candidates, list) or len(candidates) > 100:
            raise ReviewError(f"{tid}: candidates must be list <=100")
        seen_candidates = set()
        for candidate in candidates:
            _exact(candidate, {"candidate_id", "artifact_ref", "version_ref", "available_since_utc"}, "candidate")
            cid = _string(candidate["candidate_id"], "candidate_id", 128)
            if cid in seen_candidates:
                raise ReviewError(f"{tid}: duplicate candidate_id {cid}")
            seen_candidates.add(cid)
            _url(candidate["artifact_ref"], "artifact_ref")
            if candidate["version_ref"] is not None:
                _string(candidate["version_ref"], "version_ref", 128)
            if candidate["available_since_utc"] is not None:
                _utc(candidate["available_since_utc"], "available_since_utc")
        runs = task["retrieval_runs"]
        if not isinstance(runs, list) or len(runs) > 100:
            raise ReviewError(f"{tid}: retrieval_runs must be list <=100")
        run_names = set()
        pooled_candidate_ids = set()
        for run in runs:
            _exact(run, {"name", "channel", "searched_at_utc", "ranked_candidate_ids"}, "retrieval_run")
            name = _string(run["name"], "run.name", 128)
            if name in run_names:
                raise ReviewError(f"{tid}: duplicate run name {name}")
            run_names.add(name)
            if run["channel"] not in _CHANNELS:
                raise ReviewError(f"{tid}: unknown source channel")
            _utc(run["searched_at_utc"], "searched_at_utc")
            ranked = run["ranked_candidate_ids"]
            if not isinstance(ranked, list) or len(set(map(str, ranked))) != len(ranked):
                raise ReviewError(f"{tid}/{name}: duplicate/invalid ranking")
            if any(not isinstance(c, str) or c not in seen_candidates for c in ranked):
                raise ReviewError(f"{tid}/{name}: ranked candidate absent from pool")
            pooled_candidate_ids.update(ranked)
        if pooled_candidate_ids != seen_candidates:
            raise ReviewError(f"{tid}: every candidate must have a recorded retrieval/deep-audit channel")
        indexes[tid] = {c["candidate_id"]: c for c in candidates}
    return indexes


def prepare(pool):
    """Mask retrieval systems, their channel names, order and prior outcome labels."""
    validate_pool(pool)
    digest = fingerprint(pool)
    packets = []
    for task in pool["tasks"]:
        pairs = []
        for c in task["candidates"]:
            pairs.append({"candidate_id": c["candidate_id"], "artifact_ref": c["artifact_ref"],
                          "version_ref": c["version_ref"], "available_since_utc": c["available_since_utc"]})
        # Deterministic blinded order unrelated to rank or channel; use opaque candidate IDs.
        pairs.sort(key=lambda c: hashlib.sha256(
            (digest + "|" + task["task_id"] + "|" + c["candidate_id"]).encode()).hexdigest())
        packets.append({"task_id": task["task_id"], "task_ref": task["task_ref"],
                        "baseline_utc": task["baseline_utc"], "spec_sha256": task["spec_sha256"],
                        "acceptance_sha256": task["acceptance_sha256"], "candidates": pairs})
    return {"schema_version": "1.0", "dataset_kind": pool["dataset_kind"],
            "pool_sha256": digest, "reviewer_instructions":
                "Independent blinded assessment only. Source/rank removed; actual independence, functional tests and references require human verification.",
            "tasks": packets}


def _judgment(j, candidates, baseline, name):
    _exact(j, {"task_id", "candidate_id", "label", "gates", "evidence_refs", "decision_ref"}, name)
    cid = _string(j["candidate_id"], f"{name}.candidate_id", 128)
    if cid not in candidates:
        raise ReviewError(f"{name}: candidate not present in pool: {cid}")
    label = j["label"]
    if label not in _LABELS:
        raise ReviewError(f"{name}: invalid label")
    gates = _exact(j["gates"], _GATES, f"{name}.gates")
    evidence = _exact(j["evidence_refs"], _GATES, f"{name}.evidence_refs")
    for key in _GATES:
        if gates[key] not in _STATES:
            raise ReviewError(f"{name}: invalid {key} gate")
        if evidence[key] is not None:
            _string(evidence[key], f"{name}.{key}.evidence")
        if gates[key] != "unknown" and not evidence[key]:
            raise ReviewError(f"{name}: {key} pass/fail requires traceable evidence reference")
    if j["decision_ref"] is not None:
        _string(j["decision_ref"], f"{name}.decision_ref")
    if label != "unknown" and not j["decision_ref"]:
        raise ReviewError(f"{name}: non-unknown label requires decision_ref")
    candidate = candidates[cid]
    if (candidate["available_since_utc"] is not None
            and _utc(candidate["available_since_utc"], "available_since_utc") > baseline
            and gates["availability"] == "pass"):
        raise ReviewError(f"{name}: availability cannot pass: version released after task baseline")
    if label == "viable":
        if any(gates[k] != "pass" for k in _GATES):
            raise ReviewError(f"{name}: viable requires every gate to pass")
        if candidate["version_ref"] is None or candidate["available_since_utc"] is None:
            raise ReviewError(f"{name}: viable requires exact candidate version and dated availability")
        if _utc(candidate["available_since_utc"], "available_since_utc") > baseline:
            raise ReviewError(f"{name}: candidate released after task baseline")
    if label == "not_viable" and not any(v == "fail" for v in gates.values()):
        raise ReviewError(f"{name}: not_viable requires a documented failed gate")
    return cid


def _validate_submission(pool, value, slot, indexes):
    _exact(value, {"schema_version", "pool_sha256", "reviewer_slot", "reviewed_at_utc", "judgments"}, "review")
    if value["schema_version"] != "1.0" or value["pool_sha256"] != fingerprint(pool):
        raise ReviewError(f"{slot}: incompatible pool/version")
    if value["reviewer_slot"] != slot:
        raise ReviewError(f"expected reviewer_slot={slot}")
    reviewed_at = _utc(value["reviewed_at_utc"], "reviewed_at_utc")
    if reviewed_at < max(_utc(t["baseline_utc"], "baseline_utc") for t in pool["tasks"]):
        raise ReviewError(f"{slot}: review timestamp precedes latest frozen task baseline")
    rows = value["judgments"]
    if not isinstance(rows, list):
        raise ReviewError(f"{slot}.judgments must be an array")
    result = {}
    for j in rows:
        if not isinstance(j, dict):
            raise ReviewError(f"{slot}: invalid judgment")
        tid = _string(j.get("task_id"), f"{slot}.task_id", 128)
        if tid not in indexes:
            raise ReviewError(f"{slot}: task is not in pool")
        baseline = next(_utc(t["baseline_utc"], "baseline_utc") for t in pool["tasks"] if t["task_id"] == tid)
        cid = _judgment(j, indexes[tid], baseline, slot)
        key = (tid, cid)
        if key in result:
            raise ReviewError(f"{slot}: duplicate judgment {tid}/{cid}")
        result[key] = j
    return result


def _validate_adjudication(pool, value, indexes):
    if value is None:
        return {}
    _exact(value, {"schema_version", "pool_sha256", "adjudicator_slot", "adjudicated_at_utc", "decisions"}, "adjudication")
    if value["schema_version"] != "1.0" or value["pool_sha256"] != fingerprint(pool):
        raise ReviewError("adjudication: incompatible pool/version")
    if value["adjudicator_slot"] != "C":
        raise ReviewError("adjudicator must use independent third slot C")
    _utc(value["adjudicated_at_utc"], "adjudicated_at_utc")
    if not isinstance(value["decisions"], list):
        raise ReviewError("adjudication decisions must be a list")
    ret = {}
    for decision in value["decisions"]:
        if not isinstance(decision, dict):
            raise ReviewError("invalid adjudication record")
        tid = _string(decision.get("task_id"), "adjudication.task_id", 128)
        if tid not in indexes:
            raise ReviewError("adjudication: unknown task")
        baseline = next(_utc(t["baseline_utc"], "baseline_utc") for t in pool["tasks"] if t["task_id"] == tid)
        cid = _judgment(decision, indexes[tid], baseline, "adjudication")
        key = (tid, cid)
        if key in ret:
            raise ReviewError("duplicate adjudication")
        ret[key] = decision
    return ret


def _kappa(paired):
    """Nominal Cohen's kappa for the *submitted* categorical judgments only."""
    if not paired:
        return None
    n = len(paired)
    observed = sum(a == b for a, b in paired) / n
    ca = Counter(a for a, _ in paired)
    cb = Counter(b for _, b in paired)
    expected = sum(ca[x] * cb[x] for x in _LABELS) / (n * n)
    return None if expected == 1 else (observed - expected) / (1 - expected)


def audit(pool, review_a, review_b, adjudication=None):
    """Resolve only supplied reviewed pairs; export conservative input for goldset.py."""
    indexes = validate_pool(pool)
    a = _validate_submission(pool, review_a, "A", indexes)
    b = _validate_submission(pool, review_b, "B", indexes)
    c = _validate_adjudication(pool, adjudication, indexes)
    if adjudication and _utc(adjudication["adjudicated_at_utc"], "adjudicated_at_utc") < max(
            _utc(review_a["reviewed_at_utc"], "reviewed_at_utc"),
            _utc(review_b["reviewed_at_utc"], "reviewed_at_utc")):
        raise ReviewError("adjudication timestamp precedes individual reviews")
    paired = []
    statuses = Counter()
    records = []
    compiled = []
    for task in pool["tasks"]:
        tid = task["task_id"]
        converted = []
        channels = sorted({r["channel"] for r in task["retrieval_runs"]})
        for candidate in task["candidates"]:
            cid = candidate["candidate_id"]
            key = (tid, cid)
            one, two = a.get(key), b.get(key)
            if one and two:
                paired.append((one["label"], two["label"]))
            if key in c and (one is None or two is None or one["label"] == two["label"]):
                raise ReviewError("adjudication is permitted only for a double-reviewed disagreement")
            if one is None or two is None:
                state, decisive = "missing_independent_review", None
            elif one["label"] != two["label"]:
                decisive = c.get(key)
                state = "adjudicated_disagreement" if decisive else "unresolved_disagreement"
            else:
                decisive = one
                state = "reviewer_agreement"
            final_label = decisive["label"] if decisive else "unknown"
            # Adjudication may explicitly defer as unknown rather than force a decision.
            if decisive and decisive["label"] == "unknown":
                state += "_unknown"
            statuses[state] += 1
            records.append({"task_id": tid, "candidate_id": cid, "review_a": one["label"] if one else None,
                            "review_b": two["label"] if two else None, "provisional_label": final_label,
                            "status": state, "adjudication_ref": c[key]["decision_ref"] if key in c else None})
            converted.append({"id": cid, "final_label": final_label,
                              "reviewer_labels": [one["label"] if one else "unknown", two["label"] if two else "unknown"],
                              "available_since_utc": candidate["available_since_utc"],
                              # Carry the dated availability gate through to the pooled
                              # evaluator. Without this dimension an availability-only
                              # failure becomes a false unsupported 'not_viable' label.
                              "gates": {k: decisive["gates"][k] for k in _GATES}
                                      if decisive and final_label != "unknown" else
                                      {k: "unknown" for k in _GATES},
                              "evidence_ref": decisive["decision_ref"] if decisive and final_label != "unknown" else None,
                              **({"adjudicator_ref": c[key]["decision_ref"]} if key in c and final_label != "unknown" else {})})
        compiled.append({"task_id": tid, "baseline_utc": task["baseline_utc"],
                         "spec_sha256": task["spec_sha256"], "acceptance_sha256": task["acceptance_sha256"],
                         "candidates": converted,
                         "systems": [{"name": run["name"], "ranked_candidate_ids": run["ranked_candidate_ids"]}
                                     for run in task["retrieval_runs"]]})
    if set(c) - set((rec["task_id"], rec["candidate_id"]) for rec in records):
        raise ReviewError("adjudication references missing pair")
    gold = {"schema_version": "1.0", "dataset_kind": pool["dataset_kind"], "tasks": compiled}
    return {"schema_version": "1.0", "dataset_kind": pool["dataset_kind"],
            "pool_sha256": fingerprint(pool), "pairs": len(records), "double_reviewed": len(paired),
            "raw_agreement": sum(x == y for x, y in paired) / len(paired) if paired else None,
            "cohen_kappa": _kappa(paired), "status_counts": dict(sorted(statuses.items())),
            "provisional_labels": dict(sorted(Counter(r["provisional_label"] for r in records).items())),
            "tasks_with_fewer_than_two_distinct_channels": [t["task_id"] for t in pool["tasks"]
                if len({r["channel"] for r in t["retrieval_runs"]}) < 2],
            "records": records, "goldset_input": gold,
            "disclaimer": "Offline structural validation of reviewer-supplied assertions ONLY; not verified human independence, real evidence, complete retrieval recall, tested code, or measured benefits."}


def _json_file(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_new(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline blinded-reuse review packet and judgment auditor")
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare", help="Create a rank-blinded packet from a frozen task/candidate pool")
    prep.add_argument("--pool", required=True)
    prep.add_argument("--output", required=True)
    au = sub.add_parser("audit", help="Audit independently prepared judgments; no live verification")
    au.add_argument("--pool", required=True)
    au.add_argument("--review-a", required=True)
    au.add_argument("--review-b", required=True)
    au.add_argument("--adjudication")
    au.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        pool = _json_file(args.pool)
        if args.command == "prepare":
            result = prepare(pool)
        else:
            result = audit(pool, _json_file(args.review_a), _json_file(args.review_b),
                           _json_file(args.adjudication) if args.adjudication else None)
        _write_new(args.output, result)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps({"output": args.output, "pool_sha256": result["pool_sha256"],
                      "dataset_kind": result["dataset_kind"]}))


if __name__ == "__main__":
    main()
