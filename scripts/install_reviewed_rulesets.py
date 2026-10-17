#!/usr/bin/env python3
"""Opt-in, fail-closed GitHub ruleset installation for an independently reviewed admin.

Default is GET-only. Never run automatically from CI or treat JSON readback as
proof of server-side forbidden-operation rejection or scientific approval.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.request import Request, HTTPRedirectHandler, build_opener

from scripts import audit_github_rulesets as policy
from trending_study.data_integrity import decode_research_json, load_research_json_file


REPOSITORY = "MSKazemi/github-trending-1000-study"
PINNED_POLICY_BLOBS = {
    "main.json": "b2731cd693c0946193b4487ef84ce71f72878d26",
    "branch-archive-tags.json": "fbb632904a4badccfe5e0b69601c6347078d95b0",
}
LIMIT = 1_000_000


class InstallationError(ValueError):
    """An unsafe or ambiguous GitHub administrative precondition."""


def require(condition, message):
    if not condition:
        raise InstallationError(message)


def load_policies(directory):
    """Pin the exact Git blobs that were originally reviewed, not just names."""
    out = {}
    for filename, git_sha in PINNED_POLICY_BLOBS.items():
        path = Path(directory) / filename
        raw = path.read_bytes()
        require(len(raw) <= 131072, "policy input is too large")
        digest = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(digest == git_sha, "policy content differs from reviewed Git blob")
        out[filename] = load_research_json_file(path, max_bytes=131072)
    policy._check_reviewed_intent(out["main.json"], out["branch-archive-tags.json"])
    return out


class DenyRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class GitHub:
    """REST client with fixed GitHub host, no redirect and no token in arguments."""

    def __init__(self, token=None):
        self._token = token

    def _request(self, method, path, payload=None):
        require(path.startswith(f"/repos/{REPOSITORY}/"), "unapproved GitHub API route")
        require(method in ("GET", "POST"), "unapproved HTTP verb")
        if method == "POST":
            require(self._token, "admin bearer credential missing")
            require(path == f"/repos/{REPOSITORY}/rulesets", "unapproved administrative endpoint")
        raw = (json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
               if method == "POST" else None)
        req = Request("https://api.github.com" + path, data=raw, method=method,
                      headers={"Accept": "application/vnd.github+json",
                               "X-GitHub-Api-Version": "2022-11-28",
                               "Content-Type": "application/json",
                               "User-Agent": "trending-study-ruleset-operator"})
        if self._token:
            req.add_unredirected_header("Authorization", "Bearer " + self._token)
        try:
            with build_opener(DenyRedirect()).open(req, timeout=20) as response:
                body = response.read(LIMIT + 1)
                status = response.status
            require(len(body) <= LIMIT, "GitHub API response exceeds read limit")
            require(status in ((200,) if method == "GET" else (201,)),
                    "unexpected GitHub response status")
            return decode_research_json(body, "GitHub admin ruleset response")
        except (OSError, ValueError, RuntimeError, RecursionError):
            # Never include exception text or raw HTTP bodies: GitHub/auth
            # errors can contain sensitive values; an interrupted POST might
            # have succeeded, so do not blindly replay it.
            raise InstallationError("GitHub request failed or is ambiguous; inspect live state before retry") from None

    def get(self, path):
        return self._request("GET", path)

    def post(self, path, payload):
        return self._request("POST", path, payload)


def _check_ci(repo, sha, get):
    path = f"/repos/{repo}/commits/{sha}/check-runs?per_page=100"
    result = get(path)
    require(isinstance(result, dict) and isinstance(result.get("check_runs"), list)
            and type(result.get("total_count")) is int
            and result["total_count"] == len(result["check_runs"])
            and result["total_count"] <= 100,
            "check-run list is incomplete or malformed")
    matches = {}
    for item in result["check_runs"]:
        require(isinstance(item, dict), "malformed check-run entry")
        name = item.get("name")
        if name in policy.EXPECTED_CHECKS:
            require(name not in matches, "duplicate required check context")
            matches[name] = item
    require(set(matches) == policy.EXPECTED_CHECKS, "required GitHub Actions checks missing")
    for item in matches.values():
        app = item.get("app")
        require(item.get("head_sha") == sha
                and item.get("status") == "completed"
                and item.get("conclusion") == "success"
                and isinstance(app, dict)
                and type(app.get("id")) is int and app["id"] == 15368
                and app.get("slug") == "github-actions",
                "required check did not succeed on reviewed main via GitHub Actions")


def snapshot(client, sha, expected):
    """Admin preflight: exact main, approved policy, rulesets and fresh CI."""
    require(isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{40}", sha),
            "independently reviewed exact main SHA required")
    repo = client.get(f"/repos/{REPOSITORY}")
    require(isinstance(repo, dict) and repo.get("default_branch") == "main"
            and isinstance(repo.get("permissions"), dict)
            and repo["permissions"].get("admin") is True,
            "visible repository administrator permission required")
    branch = client.get(f"/repos/{REPOSITORY}/branches/main")
    require(isinstance(branch, dict) and isinstance(branch.get("commit"), dict)
            and branch["commit"].get("sha") == sha
            and type(branch.get("protected")) is bool,
            "main moved or branch protection could not be inspected")
    _check_ci(REPOSITORY, sha, client.get)
    rows = policy._pages(REPOSITORY, client.get)
    wanted = {expected["main.json"]["name"]: "main",
              expected["branch-archive-tags.json"]["name"]: "archive"}
    ids = {}
    for item in rows:
        name = item.get("name")
        require(name in wanted and item.get("source") == REPOSITORY,
                "unexpected/inherited ruleset: independent admin reconciliation required")
        key = wanted[name]
        require(key not in ids, "duplicate target ruleset")
        actual = client.get(f"/repos/{REPOSITORY}/rulesets/{item['id']}")
        policy._matching_detail(actual, expected["main.json"]
                                if key == "main" else expected["branch-archive-tags.json"],
                                item["id"], REPOSITORY)
        ids[key] = item["id"]
    # A protected=true flag alone is not evidence of approved, installed rules.
    # Conversely, legacy branch protection with no matching main ruleset
    # requires independent reconciliation before any automatic POST.
    require(branch["protected"] is ("main" in ids),
            "main protection disagrees with reviewed installed rulesets")
    status = ("complete" if set(ids) == {"main", "archive"} else
              "archive_only" if set(ids) == {"archive"} else
              "main_only" if set(ids) == {"main"} else
              "absent")
    return {"state": status, "ids": ids, "main_sha": sha, "main_protected": branch["protected"]}


def _same(client, sha, expected, expected_state, expected_ids):
    state = snapshot(client, sha, expected)
    require(state["state"] == expected_state and state["ids"] == expected_ids,
            "GitHub state moved: do not apply another ruleset")
    return state


def install(client, sha, policies, *, apply=False, review_ref=None, resume=False):
    """No write by default. Never automatically roll back a partial install."""
    policy._check_reviewed_intent(policies["main.json"], policies["branch-archive-tags.json"])
    require(not resume or apply, "resume requires explicit apply")
    if apply:
        require(isinstance(review_ref, str)
                and 8 <= len(review_ref) <= 200
                and re.fullmatch(r"[A-Za-z0-9:/#._-]+", review_ref),
                "explicit independently recorded security review reference required")
        # The reference is an operator assertion; this script cannot verify
        # the reviewer's actual independence, qualifications or approval.
    state = snapshot(client, sha, policies)
    require(state["state"] != "main_only", "unexpected main-only partial installation")
    if state["state"] == "complete":
        observed = policy.audit(REPOSITORY, sha, policies["main.json"],
                                policies["branch-archive-tags.json"], client.get)
        require(observed["configuration_status"] ==
                "matching_rulesets_observed_not_enforcement_proof",
                "live protection did not pass independent configuration readback")
        return _report(state, "already_installed", False)
    if not apply:
        return _report(state, "preflight_only", False)
    if state["state"] == "archive_only" and not resume:
        raise InstallationError("partial archive installation requires explicit --resume")
    require(state["state"] in ("absent", "archive_only"),
            "unsupported installation state")

    if state["state"] == "absent":
        _same(client, sha, policies, "absent", {})
        answer = client.post(f"/repos/{REPOSITORY}/rulesets",
                             policies["branch-archive-tags.json"])
        require(isinstance(answer, dict) and type(answer.get("id")) is int
                and answer["id"] > 0, "archive POST response ambiguous; inspect before retry")
        state = _same(client, sha, policies, "archive_only", {"archive": answer["id"]})
    else:
        state = _same(client, sha, policies, "archive_only", state["ids"])

    # Separate commit point: revalidate SHA, CI and exact archive policy before
    # main POST. API has no atomic pair-create transaction.
    _same(client, sha, policies, "archive_only", state["ids"])
    answer = client.post(f"/repos/{REPOSITORY}/rulesets", policies["main.json"])
    require(isinstance(answer, dict) and type(answer.get("id")) is int
            and answer["id"] > 0, "main POST response ambiguous; inspect before retry")
    state = _same(client, sha, policies, "complete",
                  {"archive": state["ids"]["archive"], "main": answer["id"]})
    observed = policy.audit(REPOSITORY, sha, policies["main.json"],
                            policies["branch-archive-tags.json"], client.get)
    require(observed["configuration_status"] ==
            "matching_rulesets_observed_not_enforcement_proof",
            "live rulesets installed but independent readback failed")
    return _report(state, "installed_configuration_only", True)


def _report(state, description, wrote):
    return {
        "repository": REPOSITORY, "reviewed_main_sha": state["main_sha"],
        "mode": description, "rulesets": state["ids"],
        "main_protected": state["main_protected"],
        "write_attempted": wrote,
        "independent_review_verified": False,
        "negative_enforcement_tests_verified": False,
        "administrator_review_reference_authenticity_verified": False,
        "issue_248_closed": False,
        "warning": "Live JSON configuration is not proof of denied unsafe GitHub operations.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--reviewed-main-sha", required=True)
    parser.add_argument("--payload-dir", default="ops/rulesets")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--review-ref")
    parser.add_argument("--resume", action="store_true",
                        help="explicitly resume a separately inspected archive-only state")
    args = parser.parse_args(argv)
    failure = None
    result = None
    try:
        require(args.repo == REPOSITORY, "unreviewed repository target")
        policies = load_policies(args.payload_dir)
        client = GitHub(os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN"))
        result = install(client, args.reviewed_main_sha, policies,
                         apply=args.apply, review_ref=args.review_ref, resume=args.resume)
    except (OSError, ValueError, RuntimeError, RecursionError, TypeError):
        failure = "Ruleset operation stopped; inspect live GitHub state and approved review before retry."
    # argparse raises SystemExit outside private HTTP/JSON handlers.
    if failure:
        parser.exit(2, "error: " + failure + "\n")
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
