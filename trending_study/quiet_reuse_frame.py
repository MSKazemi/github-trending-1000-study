"""Deterministic, outcome-blind selection from an externally supplied OSS frame.

This cannot establish whether the registry frame is complete, unbiased or real.
"""
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse


class FrameError(ValueError):
    pass


def _utc(value):
    if not isinstance(value, str):
        raise FrameError("explicit UTC timestamp required")
    try:
        out = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise FrameError("invalid UTC timestamp") from exc
    if out.utcoffset() is None or out.utcoffset().total_seconds() != 0:
        raise FrameError("timestamps must be explicit UTC")
    return out


def select(frame):
    if not isinstance(frame, dict):
        raise FrameError("frame must be object")
    cutoff = _utc(frame.get("frozen_at_utc"))
    if cutoff > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise FrameError("frozen sampling frame cannot be future-dated")
    seed = frame.get("seed")
    if not isinstance(seed, str) or not seed.strip():
        raise FrameError("frozen nonempty seed required")
    rows, quotas = frame.get("repositories"), frame.get("quotas")
    if not isinstance(rows, list) or not rows:
        raise FrameError("nonempty independent frame required")
    if not isinstance(quotas, dict) or not quotas or any(
        not isinstance(k, str) or not k or type(v) is not int or v <= 0
        for k, v in quotas.items()
    ):
        raise FrameError("predeclared positive integer quota per stratum required")
    seen, buckets = set(), {k: [] for k in quotas}
    # Whitelist observed-at-freeze identity fields: a blacklist cannot prevent
    # undisclosed outcome proxies being silently introduced under new key names.
    allowed = {"repository_id", "package_id", "stratum", "source_url", "snapshot_at_utc"}
    for row in rows:
        if not isinstance(row, dict) or set(row) != allowed:
            raise FrameError("sampling row must contain only prespecified pre-outcome fields")
        rid = row.get("repository_id")
        if type(rid) is not int or rid <= 0 or rid in seen:
            raise FrameError("numeric positive unique repository ID required")
        seen.add(rid)
        stratum = row.get("stratum")
        if not isinstance(stratum, str) or stratum not in quotas:
            raise FrameError("each row must use a predeclared stratum")
        for field in ("package_id", "source_url"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise FrameError("package_id and source_url required")
        url = urlparse(row["source_url"])
        if (url.scheme != "https" or not url.hostname or url.username is not None
                or url.password is not None or url.fragment):
            raise FrameError("source_url must be clean HTTPS without credentials/fragment")
        if _utc(row.get("snapshot_at_utc")) > cutoff:
            raise FrameError("future snapshot cannot be used in frozen selection")
        buckets[stratum].append(row)
    # Order is independent of input order; no star/reuse/trending-based ordering.
    selected, sizes = [], {}
    for stratum in sorted(buckets):
        available = buckets[stratum]
        size = len(available)
        sizes[stratum] = size
        scored = sorted(available, key=lambda r: (
            hashlib.sha256(f"{seed}:{r['repository_id']}".encode()).hexdigest(),
            r["repository_id"]))
        for row in scored[:quotas[stratum]]:
            selected.append({"repository_id": row["repository_id"],
                             "package_id": row["package_id"], "stratum": stratum,
                             "nominal_sampling_fraction": min(quotas[stratum], size) / size})
        # Every recorded stratum must be in the frame; no zero-size divisions.
        if size == 0:
            raise FrameError("predeclared stratum has no members: " + stratum)
    canonical = json.dumps(sorted(rows, key=lambda x: x["repository_id"]),
                           sort_keys=True, separators=(",", ":")).encode()
    return {"frame_records": len(rows),
            "frame_content_sha256": hashlib.sha256(canonical).hexdigest(),
            "frozen_at_utc": cutoff.isoformat(),
            "stratum_sizes": sizes,
            "strata_with_insufficient_members": sorted(
                k for k in quotas if sizes[k] < quotas[k]),
            "selected": selected, "source_frame_independence_unverified": True,
            "nominal_fraction_is_not_a_population_weight": True,
            "random_seed_independence_unverified": True,
            "eligible_for_population_prevalence_claim": False}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = select(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
