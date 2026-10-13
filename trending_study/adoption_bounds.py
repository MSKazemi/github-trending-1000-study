"""Offline finite-panel adoption bounds, never a population adoption estimator.

Eligibility is signal-specific. Missing/withdrawn outcomes expand logical
bounds and cannot be recoded as a negative user or missing package.
"""
import argparse
from collections import defaultdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from urllib.parse import urlsplit

class AdoptionError(ValueError):
    pass

KNOWN = {"observed_verified", "observed_negative", "unknown",
         "not_applicable", "withdrawn"}

def _time(value):
    if not isinstance(value, str):
        raise AdoptionError("observed evidence requires UTC timestamp")
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AdoptionError("invalid UTC date") from exc
    if d.utcoffset() is None or d.utcoffset().total_seconds() != 0:
        raise AdoptionError("UTC timestamp must have zero offset")
    if d > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise AdoptionError("future observation is invalid")

def summarize(cards):
    if not isinstance(cards, list) or not cards:
        raise AdoptionError("nonempty list of per-repository cards required")
    seen = set()
    frames, kinds = set(), set()
    counts = defaultdict(lambda: {"eligible": 0, "na": 0, "verified": 0,
                                  "negative": 0, "unknown": 0, "withdrawn": 0})
    for card in cards:
        if not isinstance(card, dict) or card.get("schema_version") != "proposed-adoption-evidence-0.1":
            raise AdoptionError("invalid card schema")
        if type(card.get("synthetic")) is not bool or type(card.get("not_empirical_data")) is not bool:
            raise AdoptionError("synthetic and not_empirical_data booleans required")
        if card["not_empirical_data"] != card["synthetic"]:
            raise AdoptionError("synthetic cards cannot claim to be empirical")
        kinds.add(card["synthetic"])
        frame, repo = card.get("frame_id"), card.get("repository_id")
        if not isinstance(frame, str) or not frame.strip() or type(repo) is not int or repo <= 0:
            raise AdoptionError("frame ID and stable positive numeric repository ID required")
        frames.add(frame)
        if repo in seen:
            raise AdoptionError("repeated repository unit; cannot silently double-count")
        seen.add(repo)
        signals = card.get("signals")
        if not isinstance(signals, list) or not signals:
            raise AdoptionError("nonempty signals list required")
        names = set()
        for row in signals:
            if not isinstance(row, dict):
                raise AdoptionError("signal must be object")
            name, status = row.get("name"), row.get("status")
            if not isinstance(name, str) or not name.strip() or name in names:
                raise AdoptionError("unique nonempty signal name per repository required")
            names.add(name)
            if not isinstance(status, str) or status not in KNOWN:
                raise AdoptionError("invalid signal status")
            if type(row.get("observation_eligible")) is not bool:
                raise AdoptionError("boolean observation_eligible required")
            c = counts[name]
            if not row["observation_eligible"]:
                if status != "not_applicable":
                    raise AdoptionError("ineligible signal must be explicitly not_applicable")
                c["na"] += 1
                continue
            if status == "not_applicable":
                raise AdoptionError("applicable signal may not be not_applicable")
            c["eligible"] += 1
            if status in ("observed_verified", "observed_negative"):
                url = row.get("evidence_source_url")
                if not isinstance(url, str):
                    raise AdoptionError("observed outcome requires source URL")
                parsed = urlsplit(url)
                if (parsed.scheme != "https" or not parsed.hostname
                        or parsed.username is not None or parsed.password is not None
                        or parsed.fragment):
                    raise AdoptionError("observed evidence must have clean HTTPS URL")
                _time(row.get("observed_at_utc"))
                if not isinstance(row.get("independent_reviewer"), str) or not row["independent_reviewer"].strip():
                    raise AdoptionError("observed outcome requires declared independent reviewer")
                c["verified" if status == "observed_verified" else "negative"] += 1
            else:
                if row.get("evidence_source_url") is not None or row.get("observed_at_utc") is not None:
                    raise AdoptionError("unknown/withdrawn may not contain false verified observation")
                c[status] += 1
    if len(frames) != 1 or len(kinds) != 1:
        raise AdoptionError("mixed sampling frames or synthetic/real records are not comparable")
    results = {}
    for name, v in sorted(counts.items()):
        n = v["eligible"]
        lo = v["verified"] / n if n else None
        hi = (v["verified"] + v["unknown"] + v["withdrawn"]) / n if n else None
        results[name] = {**v, "observed": v["verified"] + v["negative"],
                         "logical_lower": lo, "logical_upper": hi}
    return {"frame_id": next(iter(frames)), "dataset_kind": "synthetic" if True in kinds else "self_reported",
            "repository_units": len(seen), "signals": results,
            "bounds_are_not_population_estimates_or_confidence_intervals": True,
            "independent_review_authenticated": False,
            "warning": "Only a logical unweighted bound within the declared finite eligible panel; frame coverage, independent review and missing-not-at-random mechanisms remain unverified."}

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    a = p.parse_args(argv)
    try:
        raw = json.loads(a.input.read_text(encoding="utf-8"))
        result = summarize(raw["cards"] if isinstance(raw, dict) and "cards" in raw else [raw])
    except (OSError, ValueError, TypeError, KeyError) as exc:
        p.error(str(exc))
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
