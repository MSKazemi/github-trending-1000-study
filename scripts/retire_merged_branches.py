"""Safely retire only explicit, SHA-pinned, verified merged-PR branches.

Create and verify a permanent recovery tag before deletion. No branch
enumeration is used for deletion and no review/field-study claim is made.
"""
import argparse
import base64
import json
import os
from pathlib import Path
import re
import subprocess
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
            or s in {"main", "master", "HEAD"} or s.startswith("refs/")
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


    def delete_with_lease(self, branch, expected_sha):
        """Atomically delete only the exact expected remote ref (Git receive-pack)."""
        branch = _safe_name(branch)
        expected_sha = _sha(expected_sha)
        # Use ephemeral, narrowly scoped Git configuration. Never put the token
        # in the URL, command arguments, output or a persistent credentials file.
        basic = base64.b64encode(
            ("x-access-token:" + self.token).encode("utf-8")
        ).decode("ascii")
        # Git traces may write directly to inherited file targets, bypassing
        # captured stdout/stderr. Trace2 can explicitly log environment values,
        # including the ephemeral Authorization configuration below.
        # Inherited Git config can change transport behavior, enable helpers,
        # or expose our ephemeral HTTP header. A privileged cleanup job must not
        # trust the runner's system/global config or GIT_CONFIG_PARAMETERS.
        env = {key: value for key, value in os.environ.items()
               if not key.startswith(("GIT_TRACE", "GIT_CONFIG_"))
               and key != "GIT_CURL_VERBOSE"}
        env.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_TRACE": "0",
            "GIT_TRACE_CURL": "0",
            "GIT_TRACE2": "0",
            "GIT_TRACE2_EVENT": "0",
            "GIT_TRACE2_PERF": "0",
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "http.https://github.com/.extraheader",
            "GIT_CONFIG_VALUE_0": "AUTHORIZATION: basic " + basic,
        })
        command = [
            "git", "-c", "credential.helper=",
            # Never run a repository-supplied pre-push hook with the secret
            # present in the child environment. Git documents /dev/null as
            # the supported hooksPath disable target.
            "-c", "core.hooksPath=" + os.devnull, "push", "--porcelain",
            "--force-with-lease=refs/heads/" + branch + ":" + expected_sha,
            "https://github.com/" + self.repository + ".git",
            ":refs/heads/" + branch,
        ]
        try:
            result = subprocess.run(
                command, env=env, input="", text=True,
                capture_output=True, timeout=45, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise CleanupError("SHA-leased git push could not complete") from exc
        if result.returncode != 0:
            # Never print remote output, which may contain untrusted or
            # sensitive text. A stale lease must leave the branch intact.
            raise CleanupError("SHA lease rejected, or deletion denied by GitHub")

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

def retire_one(client, repo, item, *, audit_only=False):
    """Fail closed if ref/PR/ownership/backup diverge from frozen plan."""
    name, sha, prno = item["branch"], item["expected_sha"], item["merged_pr"]
    ref_path = _git_ref(repo, name)
    try:
        ref = client.get(ref_path)
    except ApiNotFound:
        # An absent branch is not evidence of preserved history. Even on a
        # retry, require its exact original commit to remain archived.
        archive = _tag_ref(repo, f"{ARCHIVE_PREFIX}/{name}")
        try:
            saved = client.get(archive)
        except ApiNotFound:
            return "blocked_absent_without_archive"
        return ("already_absent" if saved.get("object", {}).get("sha") == sha
                else "blocked_absent_without_archive")
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
    open_prs = client.get(_open_prs(repo, owner, name))
    if not isinstance(open_prs, list) or len(open_prs) >= 100:
        return "blocked_incomplete_open_pr_check"
    if open_prs:
        return "blocked_open_pr"

    main = client.get(f"/repos/{repo}/branches/main")
    main_sha = (main or {}).get("commit", {}).get("sha")
    if not isinstance(main_sha, str) or not SHA.fullmatch(main_sha):
        return "blocked_unverifiable_main"
    ancestry = client.get(
        f"/repos/{repo}/compare/{item['merge_commit_sha']}...{main_sha}"
    )
    if (not isinstance(ancestry, dict)
            or ancestry.get("status") not in ("ahead", "identical")
            or ancestry.get("behind_by") != 0):
        return "blocked_merge_not_in_main"
    tag = f"{ARCHIVE_PREFIX}/{name}"
    tag_path = _tag_ref(repo, tag)
    if audit_only:
        # A preflight must disclose a conflicting existing recovery tag now,
        # not report eligibility and defer the conflict to destructive mode.
        # The absence of a tag is expected before the approved archive step.
        try:
            archived = client.get(tag_path)
        except ApiNotFound:
            return "eligible_read_only"
        if (not isinstance(archived, dict)
                or not isinstance(archived.get("object"), dict)
                or archived["object"].get("sha") != sha):
            return "blocked_archive_tag_conflict"
        return "eligible_read_only"
    try:
        present = client.get(tag_path)
        if present.get("object", {}).get("sha") != sha:
            return "blocked_archive_tag_conflict"
    except ApiNotFound:
        client.post(f"/repos/{repo}/git/refs",
                    {"ref": "refs/tags/" + tag, "sha": sha})
    if client.get(tag_path).get("object", {}).get("sha") != sha:
        return "blocked_unverified_archive"
    # Preflight before the final remote compare-and-delete transaction.
    # Only the subsequent git receive-pack lease can exclude a late writer.
    if client.get(ref_path).get("object", {}).get("sha") != sha:
        return "blocked_raced_branch_update"
    fresh_open_prs = client.get(_open_prs(repo, owner, name))
    if not isinstance(fresh_open_prs, list) or len(fresh_open_prs) >= 100:
        return "blocked_incomplete_open_pr_check"
    if fresh_open_prs:
        return "blocked_new_open_pr"
    # Archive verification must be as late as the ref lease: a deleted or
    # repointed tag must not be silently treated as valid backup evidence.
    try:
        late_archive = client.get(tag_path)
    except ApiNotFound:
        return "blocked_archive_disappeared_before_delete"
    if (not isinstance(late_archive, dict)
            or late_archive.get("object", {}).get("sha") != sha):
        return "blocked_archive_changed_before_delete"
    client.delete_with_lease(name, sha)
    try:
        client.get(ref_path)
    except ApiNotFound:
        return "retired_with_archive_tag"
    return "blocked_branch_still_present"

def execute(plan, client, *, audit_only=False):
    validate_plan(plan)
    if client.repository != plan["repository"]:
        raise CleanupError("GITHUB_REPOSITORY disagrees with approved cleanup plan")
    repo = plan["repository"]
    if client.get(f"/repos/{repo}").get("default_branch") != "main":
        raise CleanupError("default branch changed; abort cleanup")
    results = []
    for item in plan["branches"]:
        try:
            status = retire_one(client, repo, item, audit_only=audit_only)
        except CleanupError as exc:
            status = "error_" + type(exc).__name__
        print(f"#{item['merged_pr']} {item['branch']}: {status}", flush=True)
        results.append({"branch": item["branch"], "status": status})
    return results

def main(argv=None):
    parser = argparse.ArgumentParser(description="Archive and retire verified merged branches only")
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--audit-live", action="store_true",
                        help="Verify live remote state without any writes")
    parser.add_argument("--confirm", default="",
                        help="Exact operator confirmation for destructive mode")
    args = parser.parse_args(argv)
    try:
        if args.plan.stat().st_size > 35000:
            raise CleanupError("cleanup plan exceeds 35 KB")
        plan = validate_plan(json.loads(args.plan.read_text(encoding="utf-8")))
        if args.execute and args.audit_live:
            raise CleanupError("choose exactly one mode")
        if args.execute and args.confirm != "RETIRE_VERIFIED_MERGED_BRANCHES":
            raise CleanupError("destructive mode requires exact confirmation")
        if not args.execute and not args.audit_live:
            print(f"DRY RUN: {len(plan['branches'])} pinned merged-PR branches; no network or changes")
            return 0
        client = GitHubClient(os.getenv("GITHUB_REPOSITORY", ""),
                              os.getenv("GITHUB_TOKEN", ""))
        records = execute(plan, client, audit_only=args.audit_live)
        accepted = ({"eligible_read_only", "already_absent"} if args.audit_live
                    else {"retired_with_archive_tag", "already_absent"})
        blocked = [r for r in records if r["status"] not in accepted]
        print(json.dumps({"eligible_read_only": sum(r["status"] == "eligible_read_only"
                                                    for r in records),
                          "retired": sum(r["status"] == "retired_with_archive_tag"
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
