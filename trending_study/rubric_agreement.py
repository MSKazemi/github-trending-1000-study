"""Offline inter-rater agreement for *supplied* documentation rubric labels.

This tool does not verify that two raters were human, independent or blinded,
or that the sample was prospectively selected.
"""
import argparse
from collections import Counter
import json
from pathlib import Path

LABELS = ("pass", "fail", "not_applicable")
ALLOWED = set(LABELS) | {"unknown"}


class RubricError(ValueError):
    pass


def _agreement(pairs):
    """Unweighted nominal Cohen kappa; undefined for empty or degenerate margins."""
    if not pairs:
        return {"n": 0, "observed_agreement": None, "chance_agreement": None,
                "cohens_kappa": None, "rater_a_counts": {}, "rater_b_counts": {}}
    n = len(pairs)
    pa = Counter(x for x, _ in pairs)
    pb = Counter(y for _, y in pairs)
    observed = sum(x == y for x, y in pairs) / n
    chance = sum(pa[k] * pb[k] for k in LABELS) / (n * n)
    return {"n": n, "observed_agreement": observed, "chance_agreement": chance,
            "cohens_kappa": (observed - chance) / (1 - chance) if n >= 2 and chance < 1 else None,
            "rater_a_counts": {k: pa[k] for k in LABELS},
            "rater_b_counts": {k: pb[k] for k in LABELS}}


def evaluate(data):
    if not isinstance(data, dict):
        raise RubricError("expected JSON object")
    a, b = data.get("rater_a"), data.get("rater_b")
    if (not all(isinstance(x, str) and x.strip() for x in (a, b))
            or a.strip().casefold() == b.strip().casefold()):
        raise RubricError("distinct nonempty rater identifiers required")
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise RubricError("nonempty records list required")
    seen, pairs, unknown, disputes = set(), [], 0, []
    by_type = {}
    for item in records:
        if not isinstance(item, dict):
            raise RubricError("each record must be an object")
        key = item.get("item_id")
        if not isinstance(key, str) or not key.strip() or key in seen:
            raise RubricError("item_id must be nonempty and unique")
        seen.add(key)
        if not isinstance(item.get("project_type"), str) or not item["project_type"].strip():
            raise RubricError("project_type required on every item")
        if not isinstance(item.get("criterion"), str) or not item["criterion"].strip():
            raise RubricError("criterion required on every item")
        x, y = item.get("rating_a"), item.get("rating_b")
        if not isinstance(x, str) or x not in ALLOWED or not isinstance(y, str) or y not in ALLOWED:
            raise RubricError("rating must be pass/fail/not_applicable/unknown")
        group = by_type.setdefault(item["project_type"], {"total": 0, "missing": 0, "pairs": []})
        group["total"] += 1
        if "unknown" in (x, y):
            unknown += 1
            group["missing"] += 1
            continue
        pairs.append((x, y))
        group["pairs"].append((x, y))
        if x != y:
            disputes.append(key)
    overall = _agreement(pairs)
    strata = {}
    for name, group in sorted(by_type.items()):
        stats = _agreement(group["pairs"])
        strata[name] = {"total": group["total"], "excluded_unknown": group["missing"],
                        "jointly_rated": stats["n"],
                        "observed_agreement": stats["observed_agreement"],
                        "cohens_kappa": stats["cohens_kappa"]}
    return {"total": len(records), "rated_pairs": overall["n"], "excluded_unknown": unknown,
            "disagreement_ids": disputes, "observed_agreement": overall["observed_agreement"],
            "chance_agreement": overall["chance_agreement"],
            "cohens_kappa": overall["cohens_kappa"],
            "rater_a_counts": overall["rater_a_counts"], "rater_b_counts": overall["rater_b_counts"],
            "by_project_type": strata,
            "reason": ("no jointly rated items" if not pairs else
                       "fewer than two jointly rated items" if len(pairs) < 2 else
                       "chance agreement is one" if overall["cohens_kappa"] is None else None),
            "warning": "Complete-case kappa is descriptive; missing/NA composition, prevalence and genuine reviewer independence require separate review."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        result = evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
