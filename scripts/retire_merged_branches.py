"""Safely retire only explicit, SHA-pinned, verified merged-PR branches.

Create and verify a permanent recovery tag before deletion. No branch
enumeration is used for deletion and no review/field-study claim is made.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

SHA = re.compile(r"[a-f0-9]{40}\Z")
BRANCH = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}\Z")
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ARCHIVE_PREFIX = "branch-archive/2026-10-13"

class CleanupError(ValueError):
    """Unsafe data, remote state or network result."""

class ApiNotFound(CleanupError):
    """Explicit 404, not a passed permission check."""

def _safe_name(s):
    if (not isinstance(s, str) or not BRANCH.fullmatch(s)
            or s in {"main", "master", "HEAD"}
            or any(p in ("", ".", "..") for p in s.split("/"))
            or s.endswith((".", "/")) or ".." in s or "@{" in s):
        raise CleanupError("invalid or protected branch name")
    return s

def _sha(s):
    if not isinstance(s, str) or not SHA.fullmatch(s):
        raise CleanupError("expected exact lower-case 40-hex commit SHA")
    return s

def validate_plan(plan):
    if not isinstance(plan, dict) or set(plan) != {
        "schema_version", "repository", "source_main_sha", "archive_prefix", "branches"
    }:
        raise CleanupError("unexpected cleanup plan schema")
    if plan["schema_version"] != "1.0":
        raise CleanupError("unsupported plan version")
    if not isinstance(plan["repository"], str) or not REPO.fullmatch(plan["repository"]):
        raise CleanupError("invalid repository")
    _sha(plan["source_main_sha"])
    if plan["archive_prefix"] != ARCHIVE_PREFIX:
        raise CleanupError("unapproved archive namespace")
    items = plan["branches"]
    if not isinstance(items, list) or not 1 <= len(items) <= 70:
        raise CleanupError("cleanup plan must list 1 to 70 approved branches")
    seen = set()
    for row in items:
        if not isinstance(row, dict) or set(row) != {
            "branch", "expected_sha", "merged_pr", "merge_commit_sha"
        }:
            raise CleanupError("missing or extra branch anchoring field")
        name = _safe_name(row["branch"])
        _sha(row["expected_sha"])
        _sha(row["merge_commit_sha"])
        if type(row["merged_pr"]) is not int or not 1 <= row["merged_pr"] <= 100000000:
            raise CleanupError("invalid merged PR number")
        if name in seen:
            raise CleanupError("duplicate cleanup branch")
        seen.add(name)
    return plan

class GitHubClient:
    """Bounded GitHub REST client; never logs tokens or response bodies."""

    def __init__(self, repository, token):
        if not token:
            raise CleanupError("GITHUB_TOKEN required for mutation")
        self.repository = repository
        self.token = token

    def request(self, method, path, payload=None):
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        req = Request("https://api.github.com" + path, data=data,
                      method=method, headers={
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "research-branch-retirement/1.0",
        })
        try:
            with urlopen(req, timeout=20) as response:
                raw = response.read(2_000_000)
                return json.loads(raw) if raw else None
        except HTTPError as exc:
            if exc.code == 404:
                raise ApiNotFound("GitHub resource not found") from None
            raise CleanupError(f"GitHub {method} returned HTTP {exc.code}") from None
        except (OSError, URLError) as exc:
            raise CleanupError(f"GitHub {method} connection failed ({type(exc).__name__})") from None
        except (ValueError, UnicodeError):
            raise CleanupError("malformed GitHub response") from None

    def get(self, path):
        return self.request("GET", path)

    def post(self, path, payload):
        return self.request("POST", path, payload)

    def delete(self, path):
        return self.request("DELETE", path)

def _git_ref(repo, branch):
    return f"/repos/{repo}/git/ref/heads/{quote(branch, safe='/')}"

def _tag_ref(repo, tag):
    return f"/repos/{repo}/git/ref/tags/{quote(tag, safe='/')}"

def _protected_branch(repo, branch):
    return f"/repos/{repo}/branches/{quote(branch, safe='/')}"

def _open_prs(repo, owner, branch):
    query = urlencode({"state": "open", "head": owner + ":" + branch,
                       "per_page": 100})
    return f"/repos/{repo}/pulls?{query}"

def retire_one(client, repo, item):
    """Fail closed if ref/PR/ownership/backup diverge from frozen plan."""
    name, sha, prno = item["branch"], item["expected_sha"], item["merged_pr"]
    ref_path = _git_ref(repo, name)
    try:
        ref = client.get(ref_path)
    except ApiNotFound:
        return "already_absent"
    if ref.get("object", {}).get("sha") != sha:
        return "blocked_changed_ref"
    branch = client.get(_protected_branch(repo, name))
    if (branch.get("protected") is not False
            or branch.get("commit", {}).get("sha") != sha):
        return "blocked_protected_or_changed"
    pr = client.get(f"/repos/{repo}/pulls/{prno}")
    if (pr.get("merged") is not True or pr.get("state") != "closed"
            or pr.get("head", {}).get("ref") != name
            or pr.get("head", {}).get("sha") != sha
            or pr.get("head", {}).get("repo", {}).get("full_name") != repo
            or pr.get("base", {}).get("ref") != "main"
            or pr.get("merge_commit_sha") != item["merge_commit_sha"]):
        return "blocked_pr_not_identical_and_merged"
    owner = repo.split("/", 1)[0]
    if client.get(_open_prs(repo, owner, name)):
        return "blocked_open_pr"
    tag = f"{ARCHIVE_PREFIX}/{name}"
    tag_path = _tag_ref(repo, tag)
    try:
        present = client.get(tag_path)
        if present.get("object", {}).get("sha") != sha:
            return "blocked_archive_tag_conflict"
    except ApiNotFound:
        client.post(f"/repos/{repo}/git/refs",
                    {"ref": "refs/tags/" + tag, "sha": sha})
    if client.get(tag_path).get("object", {}).get("sha") != sha:
        return "blocked_unverified_archive"
    # GitHub DELETE has no atomic compare-and-swap. Recheck as near as
    # possible; a race after this point requires repo-side write controls.
    if client.get(ref_path).get("object", {}).get("sha") != sha:
        return "blocked_raced_branch_update"
    if client.get(_open_prs(repo, owner, name)):
        return "blocked_new_open_pr"
    client.delete(ref_path.replace("/git/ref/", "/git/refs/"))
    return "retired_with_archive_tag"

def execute(plan, client):
    validate_plan(plan)
    if client.repository != plan["repository"]:
        raise CleanupError("GitHub repository does not match frozen plan")
    repo = plan["repository"]
    if client.get(f"/repos/{repo}").get("default_branch") != "main":
        raise CleanupError("default branch changed; abort cleanup")
    results = []
    for item in plan["branches"]:
        try:
            status = retire_one(client, repo, item)
        except CleanupError as exc:
            status = "error_" + type(exc).__name__
        print(f"#{item['merged_pr']} {item['branch']}: {status}", flush=True)
        results.append({"branch": item["branch"], "status": status})
    return results

def main(argv=None):
    parser = argparse.ArgumentParser(description="Archive and retire verified merged branches only")
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.plan.stat().st_size > 35000:
            raise CleanupError("cleanup plan exceeds 35 KB")
        plan = validate_plan(json.loads(args.plan.read_text(encoding="utf-8")))
        if not args.execute:
            print(f"DRY RUN: {len(plan['branches'])} pinned merged-PR branches; no network or changes")
            return 0
        client = GitHubClient(os.getenv("GITHUB_REPOSITORY", ""),
                              os.getenv("GITHUB_TOKEN", ""))
        records = execute(plan, client)
        blocked = [r for r in records if r["status"] not in
                   ("retired_with_archive_tag", "already_absent")]
        print(json.dumps({"retired": sum(r["status"] == "retired_with_archive_tag"
                                         for r in records),
                          "already_absent": sum(r["status"] == "already_absent"
                                                for r in records),
                          "needs_review": blocked}, indent=2))
        return 1 if blocked else 0
    except (CleanupError, ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
