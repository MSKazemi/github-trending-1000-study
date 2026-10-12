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


def evaluate(data):
    if not isinstance(data, dict):
        raise RubricError("expected JSON object")
    a, b = data.get("rater_a"), data.get("rater_b")
    if not all(isinstance(x, str) and x.strip() for x in (a, b)) or a == b:
        raise RubricError("distinct nonempty rater identifiers required")
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise RubricError("nonempty records list required")
    seen, pairs, unknown, disputes = set(), [], 0, []
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
        if x not in ALLOWED or y not in ALLOWED:
            raise RubricError("rating must be pass/fail/not_applicable/unknown")
        if "unknown" in (x, y):
            unknown += 1
            continue
        pairs.append((x, y))
        if x != y:
            disputes.append(key)
    if not pairs:
        return {"total": len(records), "rated_pairs": 0,
                "excluded_unknown": unknown, "disagreement_ids": [],
                "observed_agreement": None, "chance_agreement": None,
                "cohens_kappa": None, "reason": "no jointly rated items"}
    n = len(pairs)
    pa = Counter(x for x, _ in pairs)
    pb = Counter(y for _, y in pairs)
    observed = sum(x == y for x, y in pairs) / n
    chance = sum(pa[k] * pb[k] for k in LABELS) / (n * n)
    kappa = (observed - chance) / (1 - chance) if chance < 1 else None
    return {"total": len(records), "rated_pairs": n, "excluded_unknown": unknown,
            "disagreement_ids": disputes, "observed_agreement": observed,
            "chance_agreement": chance, "cohens_kappa": kappa,
            "reason": None if kappa is not None else "chance agreement is one"}


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
