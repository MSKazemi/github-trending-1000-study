"""Compare *supplied, authenticated elsewhere* ordered GitHub Trending snapshots.

Never infers the hidden GitHub Trending algorithm or reconstructs historical pages.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


class DriftError(ValueError):
    pass


def _validate(page):
    if not isinstance(page, dict):
        raise DriftError("snapshot must be an object")
    if page.get("window") not in ("daily", "weekly", "monthly"):
        raise DriftError("window must be daily/weekly/monthly")
    lang = page.get("language")
    if lang is not None and (not isinstance(lang, str) or not lang):
        raise DriftError("language must be null or a nonempty string")
    stamp = page.get("observed_at_utc")
    if not isinstance(stamp, str):
        raise DriftError("observed_at_utc required")
    try:
        dt = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise DriftError("invalid timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset() != timezone.utc.utcoffset(dt):
        raise DriftError("timestamp must be UTC with an explicit offset")
    ids = page.get("repository_ids")
    if not isinstance(ids, list) or not ids:
        raise DriftError("nonempty ordered repository_ids list required")
    if any(type(x) is not int or x <= 0 for x in ids) or len(set(ids)) != len(ids):
        raise DriftError("IDs must be positive, unique, immutable numeric IDs")
    if page.get("source_sha256") is None:
        raise DriftError("source_sha256 provenance required (not verified by tool)")
    digest = page["source_sha256"]
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise DriftError("source_sha256 must be a lowercase SHA-256 digest")
    return dt, ids


def compare(payload):
    if not isinstance(payload, dict):
        raise DriftError("expected object")
    a, b = payload.get("before"), payload.get("after")
    t0, left = _validate(a)
    t1, right = _validate(b)
    if a["window"] != b["window"] or a.get("language") != b.get("language"):
        raise DriftError("comparisons must share window and language surface")
    if t0 >= t1:
        raise DriftError("before snapshot must precede after snapshot")
    common = set(left) & set(right)
    n = len(common)
    union = len(set(left) | set(right))
    jaccard = n / union
    tau = None
    if n >= 2:
        l = [x for x in left if x in common]
        pos = {x: i for i, x in enumerate(right) if x in common}
        inversions = sum(pos[l[i]] > pos[l[j]] for i in range(n) for j in range(i + 1, n))
        tau = 1 - 4 * inversions / (n * (n - 1))
    p = payload.get("rbo_p", 0.9)
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not (0 < p < 1):
        raise DriftError("rbo_p must be strictly between 0 and 1")
    rbo = None
    if len(left) == len(right):
        k = len(left)
        overlap = 0
        weighted = 0.0
        sa, sb = set(), set()
        for d in range(1, k + 1):
            sa.add(left[d - 1])
            sb.add(right[d - 1])
            overlap = len(sa & sb)
            weighted += (overlap / d) * (p ** (d - 1))
        rbo = (1 - p) * weighted + (overlap / k) * (p ** k)
    return {"before_utc": t0.isoformat(), "after_utc": t1.isoformat(),
            "window": a["window"], "language": a.get("language"),
            "before_rows": len(left), "after_rows": len(right),
            "shared_ids": n, "jaccard": jaccard,
            "kendall_tau_shared_only": tau,
            "rbo_extrapolated_equal_depth": rbo,
            "rbo_p": p, "rbo_reason": None if rbo is not None else "unequal page lengths",
            "provenance_is_self_declared": True}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        result = compare(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
