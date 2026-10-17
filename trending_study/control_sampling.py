"""Strict offline, prospective control-candidate sampling for Study A (#3).

A seeded hash ranking is deterministic, not proof of random sampling from all
GitHub repositories. Input frames/labels are self-reported and no HTTP occurs.
"""
import argparse
from collections import Counter
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
import re

from .data_integrity import ResearchJSONError, load_research_json_file


class ControlFrameError(ValueError):
    """Invalid, ambiguous or outcome-leaking proposed control frame."""


ROOT = ("schema_version", "evidence_kind", "frozen_at_utc", "seed",
        "source_frames", "strata", "candidates", "observed_trending_repository_ids")
SOURCE = ("frame_id", "source_kind", "query", "source_sha256",
          "captured_at_utc", "coverage")
STRATUM = ("stratum_id", "frame_id", "language", "project_type",
           "age_bin", "stars_bin", "calendar_week", "quota")
CANDIDATE = ("repository_id", "stratum_id", "frame_id",
             "snapshot_at_utc", "eligibility_state")
KINDS = {"synthetic_fixture", "field_self_reported"}
STATES = {"eligible_preliminary", "unknown", "excluded"}
COVERAGE = {"bounded_page", "partial_index", "synthetic_only"}
HEX = re.compile(r"[0-9a-f]{64}\Z")
IDENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,79}\Z")
GROUP = re.compile(r"[a-z0-9][a-z0-9_+.-]{0,49}\Z")
WEEK = re.compile(r"(20[0-9]{2})-W(0[1-9]|[1-4][0-9]|5[0-3])\Z")
UTC = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z")


def _exact(value, fields, label):
    if not isinstance(value, dict) or set(value) != set(fields):
        raise ControlFrameError(label + " must contain only the exact specified fields")
    return value


def _date(value):
    if not isinstance(value, str) or not UTC.fullmatch(value):
        raise ControlFrameError("timestamps require strict UTC seconds and Z suffix")
    try:
        instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ControlFrameError("invalid UTC timestamp") from None
    if instant.utcoffset() != timedelta(0):
        raise ControlFrameError("timestamp is not UTC")
    return instant


def _id(value, label):
    if not isinstance(value, str) or not IDENT.fullmatch(value):
        raise ControlFrameError(label + " must be a bounded opaque ASCII identifier")
    return value


def _rid(value):
    if type(value) is not int or not 0 < value < 2 ** 63:
        raise ControlFrameError("repository_id must be a positive stable numeric ID")
    return value


def _stratum(row):
    _exact(row, STRATUM, "stratum")
    _id(row["stratum_id"], "stratum_id")
    _id(row["frame_id"], "frame_id")
    for field in ("language", "project_type", "age_bin", "stars_bin"):
        value = row[field]
        if not isinstance(value, str) or not GROUP.fullmatch(value):
            raise ControlFrameError("stratum dimension must be a bounded canonical label")
    week = row["calendar_week"]
    match = WEEK.fullmatch(week) if isinstance(week, str) else None
    if match is None:
        raise ControlFrameError("calendar_week requires ISO YYYY-Www")
    try:
        date.fromisocalendar(int(match.group(1)), int(match.group(2)), 1)
    except ValueError:
        raise ControlFrameError("invalid ISO calendar week") from None
    if type(row["quota"]) is not int or not 1 <= row["quota"] <= 10000:
        raise ControlFrameError("quota must be a prespecified positive bounded integer")
    return tuple(row[f] for f in ("frame_id", "language", "project_type",
                                  "age_bin", "stars_bin", "calendar_week"))


def _canonical_hash(payload):
    # This is a manifest digest, not proof that the input was publicly frozen
    # before outcome inspection. Order of independent rows is immaterial.
    canonical = dict(payload)
    canonical["source_frames"] = sorted(payload["source_frames"], key=lambda x: x["frame_id"])
    canonical["strata"] = sorted(payload["strata"], key=lambda x: x["stratum_id"])
    canonical["candidates"] = sorted(payload["candidates"], key=lambda x: x["repository_id"])
    canonical["observed_trending_repository_ids"] = sorted(payload["observed_trending_repository_ids"])
    raw = json.dumps(canonical, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                     allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def sample(payload):
    """Select bounded provisional controls without assuming source completeness."""
    _exact(payload, ROOT, "control frame")
    if payload["schema_version"] != "1.0" or payload["evidence_kind"] not in KINDS:
        raise ControlFrameError("supported schema 1.0 and evidence kind required")
    freeze = _date(payload["frozen_at_utc"])
    if freeze > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise ControlFrameError("cannot freeze an input in the future")
    seed = _id(payload["seed"], "seed")
    sources = payload["source_frames"]
    strata = payload["strata"]
    candidates = payload["candidates"]
    observed = payload["observed_trending_repository_ids"]
    if not isinstance(sources, list) or not 1 <= len(sources) <= 100:
        raise ControlFrameError("source_frames must have 1 to 100 rows")
    if not isinstance(strata, list) or not 1 <= len(strata) <= 200:
        raise ControlFrameError("strata must have 1 to 200 rows")
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= 20000:
        raise ControlFrameError("candidates must have 1 to 20000 rows")
    if not isinstance(observed, list) or len(observed) > 20000:
        raise ControlFrameError("observed_trending_repository_ids must be a bounded list")

    frames = {}
    for row in sources:
        _exact(row, SOURCE, "source frame")
        fid = _id(row["frame_id"], "frame_id")
        if fid in frames:
            raise ControlFrameError("duplicate source frame ID")
        if row["source_kind"] not in {"github_rest_search_metadata", "synthetic"}:
            raise ControlFrameError("source_kind must identify a supported source")
        if row["coverage"] not in COVERAGE:
            raise ControlFrameError("coverage must disclose source-frame limits")
        if payload["evidence_kind"] == "field_self_reported" and row["source_kind"] != "github_rest_search_metadata":
            raise ControlFrameError("field frames cannot claim synthetic source rows")
        query = row["query"]
        if (not isinstance(query, str) or not 1 <= len(query) <= 500
                or query != query.strip() or any(ord(c) < 32 or ord(c) == 127 for c in query)):
            raise ControlFrameError("bounded, nonempty source query required")
        if not isinstance(row["source_sha256"], str) or not HEX.fullmatch(row["source_sha256"]):
            raise ControlFrameError("source frame requires exact SHA-256 digest")
        at = _date(row["captured_at_utc"])
        if at > freeze:
            raise ControlFrameError("post-freeze source frame is not prospective")
        frames[fid] = at

    groups, profiles = {}, set()
    for row in strata:
        profile = _stratum(row)
        sid = row["stratum_id"]
        if sid in groups or profile in profiles:
            raise ControlFrameError("duplicate stratum ID or overlapping source/profile")
        if row["frame_id"] not in frames:
            raise ControlFrameError("stratum references missing source frame")
        profiles.add(profile)
        groups[sid] = row

    trend_ids = set()
    for value in observed:
        rid = _rid(value)
        if rid in trend_ids:
            raise ControlFrameError("duplicate observed Trending repository ID")
        trend_ids.add(rid)

    buckets = {sid: [] for sid in groups}
    states = {sid: Counter() for sid in groups}
    repository_ids = set()
    for row in candidates:
        _exact(row, CANDIDATE, "candidate")
        rid = _rid(row["repository_id"])
        if rid in repository_ids:
            raise ControlFrameError("duplicate candidate repository ID across strata")
        repository_ids.add(rid)
        sid = _id(row["stratum_id"], "stratum_id")
        frame_id = _id(row["frame_id"], "frame_id")
        if sid not in groups or frame_id != groups[sid]["frame_id"]:
            raise ControlFrameError("candidate and frozen stratum source identity mismatch")
        if _date(row["snapshot_at_utc"]) > frames[frame_id]:
            raise ControlFrameError("post-source candidate metadata cannot enter frozen frame")
        if row["eligibility_state"] not in STATES:
            raise ControlFrameError("explicit preliminary/unknown/excluded eligibility required")
        if rid in trend_ids:
            states[sid]["observed_trending_held"] += 1
        elif row["eligibility_state"] == "unknown":
            states[sid]["unknown_held"] += 1
        elif row["eligibility_state"] == "excluded":
            states[sid]["ineligible_held"] += 1
        else:
            states[sid]["preliminarily_eligible"] += 1
            buckets[sid].append(rid)

    selected, diagnostics = [], []
    for sid in sorted(groups):
        row = groups[sid]
        eligible = buckets[sid]
        chosen = sorted(eligible, key=lambda rid: (
            hashlib.sha256(("control-v1|" + seed + "|" + sid + "|" + str(rid)).encode()).hexdigest(),
            rid))[:row["quota"]]
        size = len(eligible)
        for rid in chosen:
            selected.append({"repository_id": rid, "stratum_id": sid,
                             "source_frame_id": row["frame_id"],
                             "nominal_within_supplied_frame_fraction": len(chosen) / size})
        diagnostics.append({
            "stratum_id": sid, "source_frame_id": row["frame_id"],
            "language": row["language"], "project_type": row["project_type"],
            "age_bin": row["age_bin"], "stars_bin": row["stars_bin"],
            "calendar_week": row["calendar_week"], "quota": row["quota"],
            "supplied_candidates": sum(states[sid].values()),
            "preliminarily_eligible": size,
            "unknown_held": states[sid]["unknown_held"],
            "ineligible_held": states[sid]["ineligible_held"],
            "observed_trending_held": states[sid]["observed_trending_held"],
            "selected": len(chosen), "shortfall": row["quota"] - len(chosen),
        })
    return {
        "schema_version": "1.0", "evidence_kind": payload["evidence_kind"],
        "sampling_algorithm": "sha256_seed_stratum_stable_repository_id",
        "selection_plan_sha256": _canonical_hash(payload),
        "source_frame_count": len(frames), "source_rows": len(candidates),
        "supplied_observed_trending_ids": len(trend_ids),
        "quota_requested": sum(row["quota"] for row in strata),
        "selected_count": len(selected),
        "quota_fulfilled_in_supplied_frame": all(x["shortfall"] == 0 for x in diagnostics),
        "selected": selected, "strata": diagnostics,
        "source_frame_authenticity_unverified": True,
        "preliminary_eligibility_not_independently_verified": True,
        "not_seen_in_supplied_trending_ids_is_not_never_trending": True,
        "future_control_crossover_tracking_required": True,
        "inclusion_probabilities_not_estimated": True,
        "causal_or_population_inference_authorized": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args(argv)
    failure = None
    try:
        payload = load_research_json_file(args.input)
        output = sample(payload)
    except ResearchJSONError as exc:
        msg = str(exc)
        if msg == "invalid or ambiguous JSON input":
            failure = "strict UTF-8 JSON without duplicate keys or nonfinite numbers required"
        elif msg in {"input must be a regular non-symlink file",
                     "input must be a readable regular non-symlink file",
                     "input exceeds configured JSON byte limit",
                     "cannot safely read input file"}:
            failure = msg
        else:
            failure = "invalid or unsafe control frame input"
    except ControlFrameError as exc:
        failure = str(exc)
    except (OSError, RecursionError, OverflowError, TypeError, ValueError):
        failure = "invalid or unsafe control frame input"
    # Do not raise SystemExit while handling a possibly private decoder error.
    if failure is not None:
        parser.error(failure)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
