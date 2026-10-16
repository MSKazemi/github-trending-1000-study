#!/usr/bin/env python3
"""Read-only GitHub ruleset readback. Configuration match is NOT enforcement proof."""
import argparse
import copy
import json
from pathlib import Path
import os
import re
import sys
from urllib.request import Request, urlopen

from trending_study.data_integrity import decode_research_json, load_research_json_file


EXPECTED_CHECKS = frozenset((
    "test (3.10)", "test (3.12)", "test (3.13)", "test (3.14)",
    "research-artifacts",
))
PAYLOADS = (("main", "main.json", "branch"),
            ("archive", "branch-archive-tags.json", "tag"))


class RulesetAuditError(ValueError):
    """Configuration was absent, ambiguous, or different from reviewed policy."""


def _require(condition, message):
    if not condition:
        raise RulesetAuditError(message)


def _normalized_rules(rules):
    _require(isinstance(rules, list), "rules must be an array")
    result = {}
    for item in rules:
        _require(isinstance(item, dict) and isinstance(item.get("type"), str),
                 "malformed rule")
        kind = item["type"]
        _require(kind not in result, "duplicate rule type")
        parameters = copy.deepcopy(item.get("parameters"))
        if kind == "required_status_checks":
            _require(isinstance(parameters, dict), "missing status-check parameters")
            checks = parameters.get("required_status_checks")
            _require(isinstance(checks, list) and all(isinstance(x, dict) for x in checks),
                     "invalid status-check declarations")
            names = [x.get("context") for x in checks]
            _require(all(isinstance(s, str) and s for s in names)
                     and len(names) == len(set(names)), "duplicate or missing check context")
            parameters["required_status_checks"] = sorted(checks, key=lambda x: x["context"])
        elif kind == "pull_request":
            _require(isinstance(parameters, dict), "missing pull request parameters")
            methods = parameters.get("allowed_merge_methods")
            _require(isinstance(methods, list)
                     and all(isinstance(x, str) for x in methods)
                     and len(methods) == len(set(methods)), "invalid allowed merge methods")
            parameters["allowed_merge_methods"] = sorted(methods)
        result[kind] = parameters
    return result


def _check_reviewed_intent(proposed_main, proposed_archive):
    """Do not mark a weakened checked-in fixture as successful configuration."""
    _require(proposed_main.get("target") == "branch"
             and proposed_main.get("enforcement") == "active"
             and proposed_main.get("bypass_actors") == []
             and proposed_main.get("conditions") == {
                 "ref_name": {"include": ["refs/heads/main"], "exclude": []}},
             "reviewed main intent weakened")
    mr = _normalized_rules(proposed_main.get("rules"))
    _require(set(mr) == {"deletion", "non_fast_forward", "pull_request", "required_status_checks"},
             "reviewed main rule coverage weakened")
    pull = mr["pull_request"]
    _require(type(pull.get("required_approving_review_count")) is int
             and pull["required_approving_review_count"] >= 1
             and pull.get("dismiss_stale_reviews_on_push") is True
             and pull.get("require_last_push_approval") is True
             and pull.get("required_review_thread_resolution") is True,
             "review/approval requirement weakened")
    checks = mr["required_status_checks"]
    contexts = checks.get("required_status_checks", [])
    _require(checks.get("strict_required_status_checks_policy") is True
             and checks.get("do_not_enforce_on_create") is False
             and {c.get("context") for c in contexts} == EXPECTED_CHECKS
             and len(contexts) == len(EXPECTED_CHECKS)
             and all(type(c.get("integration_id")) is int and c["integration_id"] == 15368
                     for c in contexts), "current CI requirements weakened")
    _require(proposed_archive.get("target") == "tag"
             and proposed_archive.get("enforcement") == "active"
             and proposed_archive.get("bypass_actors") == []
             and proposed_archive.get("conditions") == {
                 "ref_name": {"include": ["refs/tags/branch-archive/**/*"], "exclude": []}},
             "archive scope or bypass weakened")
    ar = _normalized_rules(proposed_archive.get("rules"))
    _require(set(ar) == {"update", "deletion"}
             and isinstance(ar["update"], dict)
             and ar["update"].get("update_allows_fetch_and_merge") is False,
             "archive mutation protection weakened")


def _matching_detail(actual, expected, expected_id, repo):
    _require(isinstance(actual, dict) and type(actual.get("id")) is int
             and actual["id"] == expected_id, "ruleset id mismatch")
    if "source" in actual:
        _require(actual["source"] == repo, "ruleset belongs to a different source")
    for field in ("name", "target", "enforcement", "bypass_actors", "conditions"):
        _require(actual.get(field) == expected.get(field), "live ruleset fields differ from reviewed intent")
    _require(_normalized_rules(actual.get("rules")) == _normalized_rules(expected.get("rules")),
             "live rules differ from reviewed intent")


def _pages(repo, get, limit=10):
    found = []
    seen = set()
    for page in range(1, limit + 1):
        path = f"/repos/{repo}/rulesets?includes_parents=true&per_page=100&page={page}"
        part = get(path)
        _require(isinstance(part, list), "ruleset pagination failed closed")
        for item in part:
            _require(isinstance(item, dict) and type(item.get("id")) is int
                     and item["id"] > 0 and item["id"] not in seen,
                     "duplicate or malformed listed ruleset")
            seen.add(item["id"])
            found.append(item)
        if len(part) < 100:
            return found
    raise RulesetAuditError("ruleset inventory exceeds bounded pagination")


def audit(repo, expected_main_sha, expected_main, expected_archive, get):
    """Inspect live policy via injected GET-only function; no mutations/approvals."""
    _require(isinstance(repo, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo)
             and all(x not in (".", "..") for x in repo.split("/")), "invalid repository")
    _require(isinstance(expected_main_sha, str)
             and re.fullmatch(r"[0-9a-f]{40}", expected_main_sha), "invalid pinned main SHA")
    _require(isinstance(expected_main, dict) and isinstance(expected_archive, dict),
             "reviewed payloads must be objects")
    _check_reviewed_intent(expected_main, expected_archive)
    main = get(f"/repos/{repo}/branches/main")
    _require(isinstance(main, dict) and isinstance(main.get("commit"), dict)
             and main["commit"].get("sha") == expected_main_sha
             and type(main.get("protected")) is bool,
             "main moved or protection readback malformed")
    rows = _pages(repo, get)
    ids = {}
    for key, filename, target in PAYLOADS:
        expected = expected_main if key == "main" else expected_archive
        matches = [x for x in rows if x.get("name") == expected.get("name")]
        _require(len(matches) <= 1, "ambiguous matching ruleset names")
        if matches:
            _require(matches[0].get("target") == target,
                     "matching ruleset changed target")
            if "source" in matches[0]:
                _require(matches[0]["source"] == repo, "unexpected inherited ruleset")
            ids[key] = matches[0]["id"]
    if not main["protected"] or len(ids) != len(PAYLOADS):
        return {"repository": repo, "main_sha": expected_main_sha,
                "configuration_status": "absent_or_partial",
                "main_protected": main["protected"],
                "matched_ruleset_names": sorted(ids),
                "independent_review_verified": False,
                "negative_enforcement_tests_verified": False,
                "read_only": True}
    for key, _, _ in PAYLOADS:
        actual = get(f"/repos/{repo}/rulesets/{ids[key]}")
        expected = expected_main if key == "main" else expected_archive
        _matching_detail(actual, expected, ids[key], repo)
    return {"repository": repo, "main_sha": expected_main_sha,
            "configuration_status": "matching_rulesets_observed_not_enforcement_proof",
            "main_protected": True, "main_ruleset_id": ids["main"],
            "archive_ruleset_id": ids["archive"],
            "required_checks": sorted(EXPECTED_CHECKS),
            "independent_review_verified": False,
            "negative_enforcement_tests_verified": False,
            "read_only": True}


def _get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "trending-study-ruleset-audit"}
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    with urlopen(Request("https://api.github.com" + path, headers=headers), timeout=15) as response:
        raw = response.read(1_000_001)
    if len(raw) > 1_000_000:
        raise RulesetAuditError("bounded GitHub response exceeded")
    return decode_research_json(raw, "GitHub ruleset readback")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--expected-main-sha", required=True)
    ap.add_argument("--payload-dir", default="ops/rulesets")
    args = ap.parse_args(argv)
    try:
        directory = Path(args.payload_dir)
        proposed_main = load_research_json_file(directory / "main.json", max_bytes=131072)
        proposed_archive = load_research_json_file(directory / "branch-archive-tags.json", max_bytes=131072)
        result = audit(args.repo, args.expected_main_sha, proposed_main, proposed_archive, _get)
    except (OSError, ValueError, RuntimeError, RecursionError):
        ap.exit(2, "error: ruleset audit failed closed; inspect reviewed configuration and live response\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["configuration_status"] == "absent_or_partial":
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
