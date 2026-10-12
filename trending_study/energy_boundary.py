"""Offline energy accounting across declared matched accepted software tasks.

No tokens-to-energy conversion. No claim of full SCI or cloud inference coverage.
"""
import argparse
import json
from pathlib import Path
import math

COMPONENTS = ("local_development", "ci", "model_inference", "runtime",
              "maintenance", "embodied", "upstream_support")
EVIDENCE = {"measured", "modeled", "unavailable"}


class EnergyError(ValueError):
    pass


def _nonnegative(x, name):
    if type(x) not in (int, float) or not math.isfinite(x) or x < 0:
        raise EnergyError(f"{name} must be nonnegative finite number")
    return float(x)


def _arm(row, name):
    if not isinstance(row, dict):
        raise EnergyError(f"{name} must be object")
    if set(row) != set(COMPONENTS):
        raise EnergyError(f"{name} must declare all seven energy components, including unknowns")
    known, missing, modeled = 0.0, [], []
    for key in COMPONENTS:
        cell = row[key]
        if (not isinstance(cell, dict) or not isinstance(cell.get("evidence"), str)
                or cell["evidence"] not in EVIDENCE):
            raise EnergyError(f"{name}.{key}: evidence must be measured/modeled/unavailable")
        source = cell.get("source_ref")
        if cell["evidence"] == "unavailable":
            if cell.get("kwh") is not None:
                raise EnergyError("unavailable evidence cannot assign numeric kWh")
            missing.append(key)
            continue
        if not isinstance(source, str) or not source.strip():
            raise EnergyError("reported kWh requires a source_ref/measurement configuration")
        known += _nonnegative(cell.get("kwh"), key)
        if cell["evidence"] == "modeled":
            modeled.append(key)
    return known, missing, modeled


def compare(data):
    if not isinstance(data, dict):
        raise EnergyError("expected JSON object")
    task = data.get("functional_unit")
    if not isinstance(task, dict):
        raise EnergyError("functional_unit object required")
    if not isinstance(task.get("task_id"), str) or not task["task_id"].strip():
        raise EnergyError("fixed task_id required")
    horizon = task.get("horizon_days")
    if type(horizon) is not int or horizon <= 0:
        raise EnergyError("positive maintenance horizon required")
    if not isinstance(task.get("boundary_description"), str) or not task["boundary_description"].strip():
        raise EnergyError("explicit workload/system boundary description required")
    for k in ("reuse_task_accepted", "build_task_accepted"):
        if type(task.get(k)) is not bool:
            raise EnergyError(f"{k} must be boolean (not unknown)")
    if not (task["reuse_task_accepted"] and task["build_task_accepted"]):
        return {"comparable": False, "reason": "equivalent independently accepted output not established",
                "net_kwh_reuse_minus_build": None, "net_gco2e_reuse_minus_build": None}
    arms = data.get("arms")
    if not isinstance(arms, dict) or set(arms) != {"reuse", "build"}:
        raise EnergyError("arms must contain exactly reuse and build")
    r, rm, rmodel = _arm(arms["reuse"], "reuse")
    b, bm, bmodel = _arm(arms["build"], "build")
    out = {"comparable": not (rm or bm), "functional_unit_id": task["task_id"],
           "horizon_days": horizon, "known_kwh_reuse": r, "known_kwh_build": b,
           "missing_reuse": rm, "missing_build": bm,
           "modeled_reuse": rmodel, "modeled_build": bmodel,
           "net_kwh_reuse_minus_build": None, "net_gco2e_reuse_minus_build": None,
           "boundary_is_self_declared": True}
    intensity = data.get("grid_intensity_gco2e_per_kwh")
    if intensity is not None:
        intensity = _nonnegative(intensity, "grid_intensity")
    if out["comparable"]:
        out["net_kwh_reuse_minus_build"] = r - b
        if intensity is not None:
            out["net_gco2e_reuse_minus_build"] = (r - b) * intensity
        out["reason"] = "complete declared boundary; external validation and uncertainty still required"
    else:
        out["reason"] = "at least one unknown component; partial totals cannot establish net benefit"
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = compare(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
