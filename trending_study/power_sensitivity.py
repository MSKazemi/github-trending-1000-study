"""Offline, synthetic *approximation* of power for binary accepted-task outcomes.

Only an unadjusted 2x2 factorial, independent equally sized clusters, common ICC
and a balanced reuse-first main-effect contrast are represented. This is NOT a
power calculation for accepted tasks / human-active hour (the proposed primary
endpoint); that requires pilot joint outcome/time variance and a signed analysis
plan. No real participants or results are read or generated.
"""
import argparse
import json
import math
from pathlib import Path
import re
from statistics import NormalDist

from .trial import ARMS


ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
DECIMAL = re.compile(r"(?:0|1)(?:\.[0-9]{1,6})?\Z")
OUTCOME = "independently_accepted_binary_all_assigned"
ESTIMAND = "reuse_first_minus_usual_marginal_acceptance_probability"


class PowerPlanError(ValueError):
    """Incomplete or mathematically inadmissible synthetic sensitivity scenario."""


def _record(value, keys, name):
    if not isinstance(value, dict):
        raise PowerPlanError(f"{name} must be an object")
    missing = set(keys) - set(value)
    extra = set(value) - set(keys)
    if missing or extra:
        raise PowerPlanError(f"{name}: missing={sorted(missing)} unexpected={sorted(extra)}")
    return value


def _decimal_string(value, name, *, inclusive_zero=False, inclusive_one=False):
    if not isinstance(value, str) or not DECIMAL.fullmatch(value):
        raise PowerPlanError(f"{name} must be a plain decimal string in [0,1]")
    number = float(value)
    if not ((number > 0 or (inclusive_zero and number == 0))
            and (number < 1 or (inclusive_one and number == 1))):
        raise PowerPlanError(f"{name}: value outside allowed probability interval")
    return number


def _integer(value, name, low, high):
    if type(value) is not int or not low <= value <= high:
        raise PowerPlanError(f"{name} must be integer between {low} and {high}")
    return value


def _read_unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PowerPlanError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _reject_constant(value):
    raise PowerPlanError(f"nonstandard JSON constant {value!r}")


def evaluate(payload):
    """Describe normal-theory binary outcome sensitivity; never prescribe trial N."""
    _record(payload, ("schema_version", "dataset_kind", "outcome", "estimand",
                      "two_sided_alpha", "scenarios"), "input")
    if (payload["schema_version"] != "1.0" or payload["dataset_kind"] != "synthetic"
            or payload["outcome"] != OUTCOME or payload["estimand"] != ESTIMAND):
        raise PowerPlanError("only schema 1.0, synthetic binary all-assigned reuse-first contrast is supported")
    alpha = _decimal_string(payload["two_sided_alpha"], "two_sided_alpha")
    scenarios = payload["scenarios"]
    if not isinstance(scenarios, list) or not 1 <= len(scenarios) <= 25:
        raise PowerPlanError("scenarios must have 1 to 25 entries")
    norm = NormalDist()
    critical = norm.inv_cdf(1 - alpha / 2)
    results = []
    seen = set()
    for item in scenarios:
        _record(item, ("scenario_id", "clusters_per_arm", "tasks_per_cluster",
                       "intracluster_correlation", "arm_acceptance_probabilities"), "scenario")
        sid = item["scenario_id"]
        if not isinstance(sid, str) or not ID.fullmatch(sid) or sid in seen:
            raise PowerPlanError("scenario IDs must be unique opaque identifiers")
        seen.add(sid)
        clusters = _integer(item["clusters_per_arm"], f"{sid}.clusters_per_arm", 30, 10000)
        size = _integer(item["tasks_per_cluster"], f"{sid}.tasks_per_cluster", 1, 1000)
        rho = _decimal_string(item["intracluster_correlation"],
                              f"{sid}.intracluster_correlation", inclusive_zero=True)
        if rho >= 1:
            raise PowerPlanError(f"{sid}: ICC must be less than 1")
        raw = _record(item["arm_acceptance_probabilities"], ARMS,
                      f"{sid}.arm_acceptance_probabilities")
        p = {arm: _decimal_string(raw[arm], f"{sid}.{arm}") for arm in ARMS}
        n = clusters * size
        deff = 1 + (size - 1) * rho
        effective_n = n / deff
        # Balanced marginal factorial reuse effect: ((HR-HU)+(AR-AU))/2.
        delta = (p["human_reuse_first"] - p["human_usual"]
                 + p["agent_reuse_first"] - p["agent_usual"]) / 2
        # Four independently randomized arms; variance of mean of two
        # differences is 1/4 the sum of the four arm variances.
        variance = sum(p[a] * (1 - p[a]) for a in ARMS) / (4 * effective_n)
        se = math.sqrt(variance)
        z = abs(delta) / se
        approx_power = norm.cdf(z - critical) + norm.cdf(-z - critical)
        results.append({
            "scenario_id": sid,
            "clusters_per_arm": clusters,
            "tasks_per_cluster": size,
            "total_assigned_tasks_assumed": 4 * n,
            "design_effect": round(deff, 8),
            "effective_tasks_per_arm_approx": round(effective_n, 6),
            "assumed_marginal_effect_reuse_minus_usual": round(delta, 8),
            "assumed_se": round(se, 8),
            "two_sided_alpha": alpha,
            "normal_approx_rejection_probability": round(approx_power, 6),
            "estimand_sign": ("reuse_higher" if delta > 0 else
                              "reuse_lower" if delta < 0 else "equal_assumed_rates"),
        })
    return {
        "schema_version": "1.0",
        "dataset_kind": "synthetic",
        "outcome": OUTCOME,
        "estimand": ESTIMAND,
        "power_method": "large_sample_normal_cluster_design_effect_sensitivity",
        "covered_primary_throughput_endpoint": False,
        "results": results,
        "warning": (
            "Assumed success probabilities/ICC, equal cluster sizes, independent arms and a normal approximation. "
            "Not a Monte Carlo simulation, empirical estimate, sample-size recommendation, "
            "confirmatory power analysis, trial result or approved protocol. "
            "Fails to model accepted tasks per human-active hour, refusal/missingness mechanisms, "
            "cost/safety, task-stratum imbalance, unequal clusters, crossover and time-outcome covariance. "
            "Use pilot data, independent statistical review and a frozen model before enrollment."
        ),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Synthetic cluster/factorial binary-acceptance power sensitivity")
    parser.add_argument("--input", required=True, help="bounded synthetic planning JSON")
    args = parser.parse_args(argv)
    try:
        path = Path(args.input)
        if path.stat().st_size > 512 * 1024:
            raise PowerPlanError("input exceeds 512 KiB")
        payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_read_unique,
                             parse_constant=_reject_constant)
        output = evaluate(payload)
    except (ValueError, TypeError, OSError, OverflowError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
