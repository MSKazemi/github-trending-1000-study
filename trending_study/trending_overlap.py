"""Descriptive, offline stability of two *audited* Trending page lists.

No claim of recovering GitHub's algorithm, complete eligible universe, or
independently verified page contents. Only the supplied lists are compared.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, unquote, urlsplit

_SHA = re.compile(r"^[0-9a-f]{64}$")
_WINDOWS = {"daily", "weekly", "monthly"}


class OverlapError(ValueError):
    pass


def _utc(value, name):
    if not isinstance(value, str):
        raise OverlapError(f"{name}: expected UTC timestamp")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise OverlapError(f"{name}: invalid timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset() != timezone.utc.utcoffset(dt):
        raise OverlapError(f"{name}: timestamp must have UTC offset")
    if dt > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise OverlapError(f"{name}: cannot be in the future")
    return dt


def _capture(obj):
    if not isinstance(obj, dict):
        raise OverlapError("each capture must be an object")
    for field in ("capture_id", "page_url"):
        if not isinstance(obj.get(field), str) or not obj[field].strip():
            raise OverlapError(f"capture.{field} is required")
    if obj.get("window") not in _WINDOWS:
        raise OverlapError("capture.window must be daily/weekly/monthly")
    lang = obj.get("language_filter")
    if lang is not None and (not isinstance(lang, str) or not lang.strip()):
        raise OverlapError("language_filter must be null or a nonempty string")
    # A string prefix alone is not evidence of the requested GitHub surface:
    # it also accepts /trending-evil, userinfo and inconsistent since= values.
    parsed = urlsplit(obj["page_url"])
    if (parsed.scheme != "https" or parsed.hostname != "github.com"
            or parsed.username is not None or parsed.password is not None
            or parsed.port not in (None, 443) or parsed.fragment):
        raise OverlapError("page_url must be a clean HTTPS github.com URL")
    path = parsed.path.rstrip("/")
    if lang is None:
        if path != "/trending":
            raise OverlapError("unfiltered page_url must use /trending")
    else:
        if not (path.startswith("/trending/") and len(path) > len("/trending/")):
            raise OverlapError("filtered page_url requires /trending/<language>")
        declared = re.sub(r"\s+", "-", lang.strip()).casefold()
        observed = unquote(path[len("/trending/"):]).casefold()
        if declared != observed:
            raise OverlapError("page_url language path disagrees with language_filter")
    query = parse_qs(parsed.query, keep_blank_values=True)
    if query.get("since") != [obj["window"]]:
        raise OverlapError("page_url since parameter must match window")
    if not isinstance(obj.get("source_sha256"), str) or not _SHA.fullmatch(obj["source_sha256"]):
        raise OverlapError("capture.source_sha256 must be 64 hex characters")
    timestamp = _utc(obj.get("captured_at_utc"), "captured_at_utc")
    ranks = obj.get("repository_ids")
    if not isinstance(ranks, list) or not ranks:
        raise OverlapError("repository_ids must contain all displayed ranks, not an empty subset")
    if any(isinstance(x, bool) or not isinstance(x, int) or x <= 0 for x in ranks):
        raise OverlapError("repository_ids must be positive stable numeric GitHub IDs")
    if len(ranks) != len(set(ranks)):
        raise OverlapError("duplicate stable IDs within a page; investigate capture")
    return timestamp, ranks


def evaluate(data, persistence=0.9):
    """Report within-filter overlap; all proportions refer to the two page lists."""
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise OverlapError("schema_version must be 1.0")
    if data.get("dataset_kind") not in {"synthetic", "self_reported_audit"}:
        raise OverlapError("dataset_kind must be synthetic or self_reported_audit")
    if isinstance(persistence, bool) or not isinstance(persistence, (int, float)) or not 0 < persistence < 1:
        raise OverlapError("persistence must be strictly between zero and one")
    pair = data.get("captures")
    if not isinstance(pair, list) or len(pair) != 2:
        raise OverlapError("exactly two captures are required")
    (t0, a), (t1, b) = [_capture(x) for x in pair]
    if t0 >= t1:
        raise OverlapError("captures must be chronologically ordered")
    if pair[0]["capture_id"] == pair[1]["capture_id"]:
        raise OverlapError("capture IDs must differ")
    comparable = ("window", "language_filter", "page_url")
    if any(pair[0][key] != pair[1][key] for key in comparable):
        raise OverlapError("different filter/window/page URL; compare only matched surfaces")
    set_a, set_b = set(a), set(b)
    common = set_a & set_b
    union = set_a | set_b
    a_pos = {repo: index for index, repo in enumerate(a)}
    b_pos = {repo: index for index, repo in enumerate(b)}
    ordered = sorted(common, key=a_pos.__getitem__)
    concordant = discordant = 0
    for i, one in enumerate(ordered):
        for two in ordered[i + 1:]:
            if b_pos[one] < b_pos[two]:
                concordant += 1
            else:
                discordant += 1
    total_pairs = concordant + discordant
    depth = max(len(a), len(b))
    discounted = 0.0
    last_prefix_agreement = 0.0
    for d in range(1, depth + 1):
        last_prefix_agreement = len(set(a[:d]) & set(b[:d])) / d
        discounted += (1 - persistence) * (persistence ** (d - 1)) * last_prefix_agreement
    # Reuse the uniquely useful metric from competing PR #188 rather than
    # creating a second CLI. Tail extrapolation is only defined here when
    # both observed lists end at the same depth: it ASSUMES last-depth
    # agreement persists into unobserved ranks, not measured future overlap.
    rbo_extrapolated = (
        discounted + (persistence ** depth) * last_prefix_agreement
        if len(a) == len(b) else None
    )
    return {
        "schema_version": "1.0",
        "dataset_kind": data["dataset_kind"],
        "capture_ids": [x["capture_id"] for x in pair],
        "window": pair[0]["window"],
        "language_filter": pair[0]["language_filter"],
        "captured_at_utc": [x["captured_at_utc"] for x in pair],
        "page_sizes": [len(a), len(b)],
        "common_unique_ids": len(common),
        "union_unique_ids": len(union),
        "jaccard": len(common) / len(union),
        "kendall_tau_on_common": ((concordant - discordant) / total_pairs if total_pairs else None),
        "kendall_comparable_pairs": total_pairs,
        "discounted_prefix_overlap_lower_bound": discounted,
        "rbo_extrapolated_equal_depth": rbo_extrapolated,
        "rbo_extrapolation_reason": (
            None if rbo_extrapolated is not None else "unequal observed page lengths"
        ),
        "prefix_persistence": persistence,
        "comparison_depth": depth,
        "eligible_for_confirmatory_cohort": False,
        "interpretation": (
            "Descriptive page-list comparison only. No independently authenticated "
            "page audit, candidate-frame denominator, algorithm recovery, user value, "
            "or causal inference. The discounted prefix bound omits unknown "
            "tail mass; equal-depth RBO extrapolation assumes, but does not "
            "measure, continued last-depth agreement."
        ),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--persistence", type=float, default=0.9)
    args = parser.parse_args(argv)
    try:
        report = evaluate(json.loads(Path(args.input).read_text(encoding="utf-8")), args.persistence)
    except (OverlapError, OSError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
