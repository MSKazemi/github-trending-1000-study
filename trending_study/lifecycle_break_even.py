"""Offline signed energy break-even *scenario*, not a life-cycle impact measurement.

No sensor reading, vendor inference estimate, consent, independent task match,
uncertainty interval, or carbon conclusion is established by this validator.
All included terms must be explicit; unknown never means zero.
"""
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re


TERMS = ("discovery", "development", "verification", "maintenance", "other")
BASES = {"synthetic", "metered", "calibrated", "modeled", "unknown"}
SHA = re.compile(r"[0-9a-f]{64}\Z")
NUM = re.compile(r"(?:0|[1-9][0-9]{0,8})(?:\.[0-9]{1,6})?\Z")
IDENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,99}\Z")


class BoundaryError(ValueError):
    """Reject an incomplete or ambiguous energy comparison."""


def _obj(value, keys, where):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise BoundaryError(f"{where}: expected exactly {sorted(keys)}")
    return value


def _id(value, where):
    if not isinstance(value, str) or not IDENT.fullmatch(value):
        raise BoundaryError(f"{where}: expected opaque nonempty identifier")
    return value


def _count(value, where):
    if type(value) is not int or value < 0:
        raise BoundaryError(f"{where}: expected nonnegative integer")
    return value


def _energy(record, name, kind):
    _obj(record, ("kwh", "basis", "evidence_ref"), name)
    basis = record["basis"]
    if basis not in BASES:
        raise BoundaryError(f"{name}: invalid evidence basis")
    if kind == "synthetic" and basis not in ("synthetic", "unknown"):
        raise BoundaryError(f"{name}: synthetic dataset must not claim meter evidence")
    if kind == "pilot" and basis == "synthetic":
        raise BoundaryError(f"{name}: pilot must not pass synthetic readings as observations")
    raw = record["kwh"]
    ref = record["evidence_ref"]
    if basis == "unknown":
        if raw is not None or ref is not None:
            raise BoundaryError(f"{name}: unknown must have null kwh and source")
        return None
    if not isinstance(raw, str) or not NUM.fullmatch(raw):
        raise BoundaryError(f"{name}: kwh must be a nonnegative decimal string")
    if not isinstance(ref, str) or not ref.strip():
        raise BoundaryError(f"{name}: known value needs an evidence reference")
    try:
        value = Decimal(raw)
    except InvalidOperation as exc:
        raise BoundaryError(f"{name}: invalid decimal") from exc
    return value


def _duplicate_key(pairs):
    found = {}
    for key, value in pairs:
        if key in found:
            raise BoundaryError(f"duplicate JSON key: {key}")
        found[key] = value
    return found


def _reject_constant(value):
    raise BoundaryError(f"nonstandard JSON constant {value}")


def _decimal(value):
    return format(value.quantize(Decimal("0.000001")), "f")


def evaluate(payload):
    """Compute signed energy scenarios only when all in-boundary terms are known."""
    keys = ("schema_version", "dataset_kind", "functional_unit_id",
            "task_spec_sha256", "acceptance_sha256", "horizon_days",
            "boundary_id", "excluded_terms", "n_uses", "strategies")
    _obj(payload, keys, "input")
    if payload["schema_version"] != "1.0" or payload["dataset_kind"] not in ("synthetic", "pilot"):
        raise BoundaryError("schema must be 1.0 with synthetic or pilot dataset_kind")
    for name in ("functional_unit_id", "boundary_id"):
        _id(payload[name], name)
    for name in ("task_spec_sha256", "acceptance_sha256"):
        if not isinstance(payload[name], str) or not SHA.fullmatch(payload[name]):
            raise BoundaryError(f"{name}: expected lowercase SHA-256")
    _count(payload["horizon_days"], "horizon_days")
    excluded = payload["excluded_terms"]
    if not isinstance(excluded, list) or any(not isinstance(x, str) or not x.strip() for x in excluded):
        raise BoundaryError("excluded_terms: expected list of named omissions")
    if len(set(excluded)) != len(excluded) or any(x in (*TERMS, "runtime_per_use") for x in excluded):
        raise BoundaryError("excluded_terms: duplicate or already-included term")
    uses = payload["n_uses"]
    if not isinstance(uses, list) or not uses or len(uses) > 100:
        raise BoundaryError("n_uses: expected 1 to 100 workload counts")
    for n in uses:
        _count(n, "n_uses")
    if len(set(uses)) != len(uses) or uses != sorted(uses):
        raise BoundaryError("n_uses must be unique and sorted")
    arms = _obj(payload["strategies"], ("build", "reuse"), "strategies")
    sums = {}
    missing = []
    for arm in ("build", "reuse"):
        record = _obj(arms[arm], ("pre_run", "runtime_per_use"), arm)
        pre = _obj(record["pre_run"], TERMS, arm + ".pre_run")
        known = []
        for name in TERMS:
            value = _energy(pre[name], f"{arm}.{name}", payload["dataset_kind"])
            if value is None:
                missing.append(f"{arm}.{name}")
            else:
                known.append(value)
        runtime = _energy(record["runtime_per_use"], arm + ".runtime_per_use", payload["dataset_kind"])
        if runtime is None:
            missing.append(arm + ".runtime_per_use")
        sums[arm] = (sum(known, Decimal(0)), runtime)
    result = {
        "schema_version": "1.0",
        "dataset_kind": payload["dataset_kind"],
        "boundary_id": payload["boundary_id"],
        "functional_unit_id": payload["functional_unit_id"],
        "horizon_days": payload["horizon_days"],
        "scope": "partial_declared_boundary" if excluded else "declared_boundary_not_lifecycle_certified",
        "excluded_terms": excluded,
        "missing_included_terms": missing,
        "calculation_status": "incomplete_no_point_estimate" if missing else "scenario_only_no_uncertainty_interval",
        "points": [],
        "crossing": None,
        "warning": "Self-reported input; no audited equivalence, real measurement, uncertainty bound or causal/carbon inference. Include failures, rebound and omitted terms in any real study.",
    }
    if missing:
        for n in uses:
            result["points"].append({"n_uses": n, "build_kwh": None,
                                     "reuse_kwh": None, "delta_build_minus_reuse_kwh": None})
        return result
    b_pre, b_run = sums["build"]
    r_pre, r_run = sums["reuse"]
    for n in uses:
        build = b_pre + n * b_run
        reuse = r_pre + n * r_run
        result["points"].append({
            "n_uses": n, "build_kwh": _decimal(build),
            "reuse_kwh": _decimal(reuse),
            "delta_build_minus_reuse_kwh": _decimal(build - reuse),
        })
    fixed_delta = b_pre - r_pre
    slope = b_run - r_run
    if fixed_delta > 0 and slope < 0:
        result["crossing"] = {"kind": "reuse_lower_below_threshold",
                              "n_uses_equal": _decimal(-fixed_delta / slope)}
    elif fixed_delta < 0 and slope > 0:
        result["crossing"] = {"kind": "reuse_lower_above_threshold",
                              "n_uses_equal": _decimal(-fixed_delta / slope)}
    elif fixed_delta >= 0 and slope >= 0:
        result["crossing"] = {"kind": "reuse_never_higher_for_nonnegative_n", "n_uses_equal": None}
    else:
        result["crossing"] = {"kind": "reuse_never_lower_for_nonnegative_n", "n_uses_equal": None}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline declared-boundary build-vs-reuse energy scenario")
    parser.add_argument("--input", required=True, help="explicit boundary scenario JSON")
    args = parser.parse_args(argv)
    try:
        path = Path(args.input)
        if path.stat().st_size > 1_000_000:
            raise BoundaryError("input exceeds 1 MB")
        payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_duplicate_key,
                             parse_constant=_reject_constant)
        result = evaluate(payload)
    except (ValueError, TypeError, OSError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
