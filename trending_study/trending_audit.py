"""Offline frame coverage and leakage-guarded Trending rank-proxy audit.

This instrument does not fetch GitHub, verify self-reported hashes/approvals,
infer the hidden Trending algorithm, or measure population-level inclusion.
Its prediction target is ORDER AMONG ALREADY DISPLAYED REPOSITORIES, never
membership in an unobserved candidate universe.
"""
import argparse
import json
from pathlib import Path
import re
import stat

from .data_integrity import MAX_FILE_BYTES, ResearchJSONError, decode_research_json
from .trending_overlap import OverlapError, _capture, _utc

COVERAGE_VERSION = "trending-coverage-1.0"
PROXY_VERSION = "trending-rank-proxy-1.0"
KINDS = frozenset(("synthetic", "self_reported_audit"))
PREDICTORS = ("prior_7d_star_delta", "prior_stars", "prior_forks")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CAPTURE_FIELDS = frozenset((
    "capture_id", "captured_at_utc", "page_url", "window",
    "language_filter", "source_sha256", "repository_ids",
))
SURFACE_FIELDS = frozenset((
    "frame_id", "frame_as_of_utc", "frame_source_sha256", "frame_definition",
    "frame_sampling", "eligible_repository_ids", "capture",
))
FEATURE_FIELDS = frozenset((
    "repository_id", "recorded_at_utc", "feature_source_sha256",
    "prior_7d_star_delta", "prior_stars", "prior_forks",
))
PAGE_FIELDS = frozenset(("capture", "features"))
MAX_SURFACES = 50
MAX_FRAME_IDS = 10000
MAX_PAGES = 64


class TrendingAuditError(ValueError):
    """An offline research audit cannot safely interpret these inputs."""


def _fields(value, expected, label):
    if not isinstance(value, dict):
        raise TrendingAuditError(f"{label}: expected object")
    missing, unexpected = expected - value.keys(), value.keys() - expected
    if missing or unexpected:
        # Never echo field values: unknown keys may carry raw/private content.
        raise TrendingAuditError(
            f"{label}: missing={sorted(missing)}, unsupported={sorted(unexpected)}"
        )


def _text(value, label):
    if not isinstance(value, str) or not value.strip() or len(value) > 2000:
        raise TrendingAuditError(f"{label}: expected nonempty bounded text")
    if any(ord(ch) < 32 for ch in value):
        raise TrendingAuditError(f"{label}: control characters forbidden")
    return value.strip()


def _sha(value, label):
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise TrendingAuditError(f"{label}: expected lowercase SHA-256 hex")


def _identifiers(ids, label, limit):
    if not isinstance(ids, list) or not 0 < len(ids) <= limit:
        raise TrendingAuditError(f"{label}: expected 1..{limit} stable IDs")
    if any(type(x) is not int or x <= 0 for x in ids):
        raise TrendingAuditError(f"{label}: repository IDs must be positive integers")
    if len(set(ids)) != len(ids):
        raise TrendingAuditError(f"{label}: duplicate stable repository ID")
    return set(ids)


def _timestamp(value, label):
    try:
        return _utc(value, label)
    except OverlapError as exc:
        raise TrendingAuditError(str(exc)) from exc


def _capture_info(capture):
    _fields(capture, CAPTURE_FIELDS, "capture")
    try:
        return _capture(capture)
    except OverlapError as exc:
        raise TrendingAuditError(str(exc)) from exc


def _root(data, version, payload_field):
    _fields(data, {"schema_version", "dataset_kind", payload_field}, "root")
    if (data["schema_version"] != version or not isinstance(data["dataset_kind"], str)
            or data["dataset_kind"] not in KINDS):
        raise TrendingAuditError("unsupported schema_version or dataset_kind")


def evaluate_coverage(data):
    """Observed-in-supplied-frame fraction, separately for each page/filter.

    This is NOT a population probability, even if frame_sampling claims a
    probability sample. The software cannot verify frame independence.
    """
    _root(data, COVERAGE_VERSION, "surfaces")
    surfaces = data["surfaces"]
    if not isinstance(surfaces, list) or not 0 < len(surfaces) <= MAX_SURFACES:
        raise TrendingAuditError("surfaces must contain 1..50 declared frames")
    seen = set()
    reports = []
    for item in surfaces:
        _fields(item, SURFACE_FIELDS, "surface")
        frame_id = _text(item["frame_id"], "frame_id")
        if frame_id in seen:
            raise TrendingAuditError("duplicate frame_id")
        seen.add(frame_id)
        _sha(item["frame_source_sha256"], "frame_source_sha256")
        definition = _text(item["frame_definition"], "frame_definition")
        sampling = _text(item["frame_sampling"], "frame_sampling")
        frame_time = _timestamp(item["frame_as_of_utc"], "frame_as_of_utc")
        capture_time, observed_order = _capture_info(item["capture"])
        if frame_time > capture_time:
            raise TrendingAuditError("frame was defined after target capture")
        eligible = _identifiers(
            item["eligible_repository_ids"], "eligible_repository_ids",
            MAX_FRAME_IDS,
        )
        observed = set(observed_order)
        overlap = eligible & observed
        reports.append({
            "frame_id": frame_id,
            "window": item["capture"]["window"],
            "language_filter": item["capture"]["language_filter"],
            "capture_id": item["capture"]["capture_id"],
            "capture_at_utc": item["capture"]["captured_at_utc"],
            "frame_as_of_utc": item["frame_as_of_utc"],
            "frame_source_sha256": item["frame_source_sha256"],
            "capture_source_sha256": item["capture"]["source_sha256"],
            "frame_definition": definition,
            "frame_sampling": sampling,
            "denominator_predeclared_frame_ids": len(eligible),
            "numerator_observed_frame_ids": len(overlap),
            "frame_ids_not_on_page": len(eligible - observed),
            "page_ids_outside_frame": len(observed - eligible),
            "observed_page_ids": len(observed),
            "frame_observed_fraction": len(overlap) / len(eligible),
        })
    # A filtered and an unfiltered page are different observational surfaces.
    # Never sum denominators across potentially overlapping language frames.
    reports.sort(key=lambda r: r["frame_id"])
    return {
        "schema_version": COVERAGE_VERSION,
        "dataset_kind": data["dataset_kind"],
        "surfaces": reports,
        "denominator_scope": "per_predeclared_frame_only",
        "cross_language_population_coverage": None,
        "eligible_for_confirmatory_cohort": False,
        "independent_verification": False,
        "interpretation": (
            "Fraction of supplied frame IDs visible on each supplied page. "
            "Frame completeness, sampling probabilities, live page evidence, "
            "coverage of all GitHub repositories and fairness are unverified. "
            "Do not combine language denominators or infer missing population."
        ),
    }


def _feature_rows(features, capture, capture_time):
    ranked = capture["repository_ids"]
    if not isinstance(features, list) or len(features) != len(ranked):
        raise TrendingAuditError("features must have exactly one row per displayed ID")
    by_id = {}
    for row in features:
        _fields(row, FEATURE_FIELDS, "feature")
        repo_id = row["repository_id"]
        if type(repo_id) is not int or repo_id <= 0 or repo_id in by_id:
            raise TrendingAuditError("feature repository_id invalid or duplicate")
        observed = _timestamp(row["recorded_at_utc"], "recorded_at_utc")
        if observed >= capture_time:
            raise TrendingAuditError("feature observation is not earlier than ranking target")
        _sha(row["feature_source_sha256"], "feature_source_sha256")
        for feature in PREDICTORS:
            value = row[feature]
            if type(value) is not int or (feature != "prior_7d_star_delta" and value < 0):
                raise TrendingAuditError(f"{feature}: require valid integer; unknown is not zero")
        by_id[repo_id] = row
    if set(by_id) != set(ranked):
        raise TrendingAuditError("feature IDs do not match the target page IDs")
    return by_id


def _pairwise_score(ranked, by_id, predictor):
    # Each page contributes one macro-averaged score so large pages do not
    # dominate selection/evaluation. Tied proxy values earn 0.5 credit, never
    # a fabricated strict rank ordering.
    correct_twice = ties = 0
    for index, left in enumerate(ranked):
        value = by_id[left][predictor]
        for right in ranked[index + 1:]:
            other = by_id[right][predictor]
            if value > other:
                correct_twice += 2
            elif value == other:
                correct_twice += 1
                ties += 1
    pairs = len(ranked) * (len(ranked) - 1) // 2
    return {"pairs": pairs, "feature_ties": ties,
            "pairwise_accuracy": correct_twice / (2 * pairs)}


def evaluate_proxy(data):
    """Select ONE predeclared ranking feature on past pages; score future pages.

    No feature weight, split point, or predictor choice is tuned against the
    holdout. Feature snapshots must predate each page. Overlap in repository
    identity across train/holdout is forbidden to limit memorization leakage.
    """
    _fields(
        data, {"schema_version", "dataset_kind", "protocol_locked_at_utc",
               "protocol_reference", "pages"}, "root",
    )
    if (data["schema_version"] != PROXY_VERSION
            or not isinstance(data["dataset_kind"], str)
            or data["dataset_kind"] not in KINDS):
        raise TrendingAuditError("unsupported schema_version or dataset_kind")
    locked = _timestamp(data["protocol_locked_at_utc"], "protocol_locked_at_utc")
    _text(data["protocol_reference"], "protocol_reference")
    pages = data["pages"]
    if not isinstance(pages, list) or not 4 <= len(pages) <= MAX_PAGES:
        raise TrendingAuditError("proxy needs 4..64 chronological pages")
    seen_ids = set()
    train, heldout = [], []
    train_repos, heldout_repos = set(), set()
    previous_time = None
    surface_key = None
    for page in pages:
        _fields(page, PAGE_FIELDS, "page")
        cap = page["capture"]
        timestamp, ranks = _capture_info(cap)
        if len(ranks) < 2:
            raise TrendingAuditError("rank proxy needs at least 2 IDs per page")
        if previous_time is not None and timestamp <= previous_time:
            raise TrendingAuditError("page captures must be strictly chronological")
        previous_time = timestamp
        ident = cap["capture_id"]
        if ident in seen_ids:
            raise TrendingAuditError("duplicate capture_id")
        seen_ids.add(ident)
        key = (cap["page_url"], cap["window"], cap["language_filter"])
        if surface_key is None:
            surface_key = key
        elif key != surface_key:
            raise TrendingAuditError("all proxy pages must target one matched surface")
        feats = _feature_rows(page["features"], cap, timestamp)
        if timestamp == locked:
            raise TrendingAuditError("no target capture may equal the protocol lock time")
        if timestamp < locked:
            train.append((cap, feats))
            train_repos.update(ranks)
        else:
            heldout.append((cap, feats))
            heldout_repos.update(ranks)
    if len(train) < 2 or len(heldout) < 2:
        raise TrendingAuditError("need at least two pre-lock and two post-lock pages")
    if train_repos & heldout_repos:
        raise TrendingAuditError("cross-split repository ID reuse leaks rank identity")

    candidate_scores = {}
    for predictor in PREDICTORS:
        scores = [
            _pairwise_score(cap["repository_ids"], feats, predictor)["pairwise_accuracy"]
            for cap, feats in train
        ]
        candidate_scores[predictor] = sum(scores) / len(scores)
    # Stable tie-breaker: fixed documented PREDICTORS order; no holdout tuning.
    selected = max(PREDICTORS, key=candidate_scores.__getitem__)
    heldout_scores = []
    for cap, feats in heldout:
        score = _pairwise_score(cap["repository_ids"], feats, selected)
        heldout_scores.append({"capture_id": cap["capture_id"],
            "captured_at_utc": cap["captured_at_utc"],
            "n_displayed_repositories": len(cap["repository_ids"]), **score})
    return {
        "schema_version": PROXY_VERSION,
        "dataset_kind": data["dataset_kind"],
        "protocol_locked_at_utc": data["protocol_locked_at_utc"],
        "protocol_reference": data["protocol_reference"],
        "window": surface_key[1],
        "language_filter": surface_key[2],
        "train_pages": len(train),
        "heldout_pages": len(heldout),
        "train_unique_repository_ids": len(train_repos),
        "heldout_unique_repository_ids": len(heldout_repos),
        "predeclared_predictor_order": list(PREDICTORS),
        "train_macro_accuracy_by_predictor": candidate_scores,
        "selected_predictor_train_only": selected,
        "train_selected_macro_accuracy": candidate_scores[selected],
        "heldout_page_scores": heldout_scores,
        "heldout_macro_pairwise_accuracy": (
            sum(x["pairwise_accuracy"] for x in heldout_scores) / len(heldout_scores)
        ),
        "holdout_frozen_by_external_review": False,
        "selection_universe_known": False,
        "independent_verification": False,
        "eligible_for_confirmatory_cohort": False,
        "interpretation": (
            "Chronological, page-conditioned single-feature prediction of "
            "relative order among ALREADY DISPLAYED repositories, using only "
            "pre-capture metadata. Fixed candidate predictors are selected "
            "only on pre-lock pages; page-macro pairwise accuracy and tied "
            "feature pairs are descriptive. No future stars, inclusion "
            "prediction, inferred algorithm weights or causal effect. "
            "Protocol lock/source hashes are not independently authenticated."
        ),
    }


def load_offline_json(path):
    """Read one bounded regular file using the repository's shared JSON gate."""
    path = Path(path)
    if path.is_symlink() or not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
        raise TrendingAuditError("input must be an existing regular non-symlink file")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise TrendingAuditError("input exceeds the strict research JSON byte limit")
    try:
        return decode_research_json(path.read_bytes(), path.name)
    except ResearchJSONError as exc:
        raise TrendingAuditError("malformed strict research JSON: " + str(exc)) from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("coverage", "proxy"))
    parser.add_argument("--input", type=Path, required=True)
    options = parser.parse_args(argv)
    try:
        data = load_offline_json(options.input)
        output = evaluate_coverage(data) if options.mode == "coverage" else evaluate_proxy(data)
    except (TrendingAuditError, OverlapError, OSError, RecursionError) as exc:
        parser.error(str(exc))
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
