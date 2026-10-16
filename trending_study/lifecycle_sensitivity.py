"""Offline scenario-envelopes for the existing build-versus-reuse energy model.

A sensitivity envelope is NOT a confidence interval, carbon measurement,
causal effect, energy calibration or a complete environmental life cycle.
Scenarios must describe the same functional unit, acceptance, workload and
declared boundary. Unknown in any included term makes every range incomplete.
"""
import argparse
from decimal import Decimal
import json
import re

from .data_integrity import ResearchJSONError, load_research_json_file
from .lifecycle_break_even import BoundaryError, evaluate as evaluate_scenario

IDENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,99}\Z")
BIND = ("dataset_kind", "functional_unit_id", "task_spec_sha256",
        "acceptance_sha256", "horizon_days", "boundary_id",
        "excluded_terms", "n_uses")


def evaluate(payload):
    if not isinstance(payload, dict) or set(payload) != {
            "schema_version", "scenario_set_id", "scenarios"}:
        raise BoundaryError("scenario envelope: exact root fields required")
    if payload["schema_version"] != "1.0":
        raise BoundaryError("scenario envelope: version must be 1.0")
    set_id = payload["scenario_set_id"]
    if not isinstance(set_id, str) or not IDENT.fullmatch(set_id):
        raise BoundaryError("scenario_set_id must be an opaque bounded identifier")
    scenarios = payload["scenarios"]
    if not isinstance(scenarios, list) or not 2 <= len(scenarios) <= 16:
        raise BoundaryError("scenarios: require 2 to 16 explicitly distinct cases")
    seen, baseline, values, incomplete = set(), None, [], []
    for case in scenarios:
        if not isinstance(case, dict) or set(case) != {"scenario_id", "input"}:
            raise BoundaryError("each scenario needs exactly scenario_id and input")
        case_id = case["scenario_id"]
        if (not isinstance(case_id, str) or not IDENT.fullmatch(case_id)
                or case_id in seen):
            raise BoundaryError("scenario_id must be unique, bounded and opaque")
        seen.add(case_id)
        source = case["input"]
        # Run all the canonical schema/quantity/missingness checks before using
        # numerical results; this module never overrides the existing model.
        result = evaluate_scenario(source)
        binding = tuple(json.dumps(source[key], sort_keys=True)
                        for key in BIND)
        if baseline is None:
            baseline = binding
        elif binding != baseline:
            raise BoundaryError(
                "scenario inputs must share task, acceptance, horizon, "
                "boundary, omissions and exact workload counts")
        if result["calculation_status"] == "incomplete_no_point_estimate":
            incomplete.append({"scenario_id": case_id,
                               "missing_included_terms":
                               result["missing_included_terms"]})
        values.append((case_id, result))
    reference = scenarios[0]["input"]
    output = {
        "schema_version": "1.0",
        "scenario_set_id": set_id,
        "dataset_kind": reference["dataset_kind"],
        "functional_unit_id": reference["functional_unit_id"],
        "boundary_id": reference["boundary_id"],
        "horizon_days": reference["horizon_days"],
        "excluded_terms": list(reference["excluded_terms"]),
        "scenario_ids": [item[0] for item in values],
        "scenario_count": len(values),
        "calculation_status": (
            "incomplete_no_envelope" if incomplete else
            "deterministic_sensitivity_envelope_not_confidence_interval"),
        "missing_scenarios": incomplete,
        "points": [],
        "warning": (
            "Declared scenario range, NOT a statistical confidence interval "
            "or independent calibrated energy measurement. Unknown included "
            "terms block all estimates. Omitted provider inference, embodied "
            "hardware, deployment, rebound, water and upstream costs cannot "
            "be assumed zero; no carbon or causal impact is inferred."
        ),
    }
    for index, n in enumerate(reference["n_uses"]):
        if incomplete:
            output["points"].append({
                "n_uses": n, "delta_min_kwh": None,
                "delta_max_kwh": None,
                "direction_across_scenarios": "unknown",
            })
            continue
        deltas = [
            Decimal(result["points"][index]["delta_build_minus_reuse_kwh"])
            for _, result in values
        ]
        low, high = min(deltas), max(deltas)
        if low > 0:
            direction = "reuse_lower_in_every_supplied_scenario"
        elif high < 0:
            direction = "build_lower_in_every_supplied_scenario"
        elif low == 0 and high == 0:
            direction = "equal_in_every_supplied_scenario"
        else:
            direction = "mixed_or_zero_across_supplied_scenarios"
        output["points"].append({
            "n_uses": n, "delta_min_kwh": format(low, "f"),
            "delta_max_kwh": format(high, "f"),
            "direction_across_scenarios": direction,
        })
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True,
                        help="bounded synthetic or pilot scenario set JSON")
    args = parser.parse_args(argv)
    try:
        data = load_research_json_file(args.input, max_bytes=1_000_000)
        report = evaluate(data)
    except ResearchJSONError:
        parser.exit(2, "error: invalid or unsafe research JSON input\n")
    except OSError:
        parser.exit(2, "error: input filesystem operation failed\n")
    except (ValueError, TypeError, RecursionError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
