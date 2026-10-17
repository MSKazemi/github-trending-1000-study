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
import stat
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

SHA = re.compile(r"[a-f0-9]{40}\Z")
BRANCH = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}\Z")
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ARCHIVE_PREFIX = "branch-archive/2026-10-13"

class CleanupError(ValueError):
    """Unsafe data, remote state or network result."""

class ApiNotFound(CleanupError):
    """Explicit 404, not a passed permission check."""


def _safe_repo(repository):
    """Reject dot-segment API paths before using the approved repo identity."""
    if (not isinstance(repository, str) or not REPO.fullmatch(repository)
            or any(part in (".", "..") for part in repository.split("/"))):
        raise CleanupError("invalid repository")
    return repository


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
    _safe_repo(plan["repository"])
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

def _load_strict_plan(path):
    """Read one bounded regular JSON plan without following leaf symlinks.

    This privileged standalone script is executed by file path in Actions, so
    it cannot reliably import the package-level research JSON loader. Apply
    the same fail-closed checks here rather than trusting stat-then-read.
    """
    path = Path(path)
    if path.is_symlink():
        raise CleanupError("cleanup plan must be a non-symlink regular file")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    flags |= getattr(os, "O_NONBLOCK", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError:
        raise CleanupError("cannot safely open cleanup plan") from None
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise CleanupError("cleanup plan must be a regular file")
        if info.st_size > 35000:
            raise CleanupError("cleanup plan exceeds 35 KB")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            raw = stream.read(35001)
        if len(raw) > 35000:
            raise CleanupError("cleanup plan exceeds 35 KB")
    except OSError:
        raise CleanupError("cannot safely read cleanup plan") from None
    finally:
        os.close(descriptor)

    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise CleanupError("ambiguous duplicate cleanup plan field")
            result[key] = value
        return result

    def reject_number(_literal):
        raise CleanupError("unsupported cleanup plan numeric literal")

    def bounded_integer(literal):
        # Only the positive, <=100,000,000 merged_pr field uses JSON numbers.
        if len(literal.lstrip("-")) > 9:
            raise CleanupError("cleanup plan integer exceeds bound")
        return int(literal)

    try:
        return json.loads(
            raw.decode("utf-8"), object_pairs_hook=unique_keys,
            parse_constant=reject_number, parse_float=reject_number,
            parse_int=bounded_integer,
        )
    except (ValueError, UnicodeError, OverflowError, RecursionError):
        # Parser messages might contain attacker-controlled keys or paths.
        raise CleanupError("invalid or ambiguous cleanup plan JSON") from None


class _RejectAuthenticatedRedirect(HTTPRedirectHandler):
    """Fail closed on HTTP 30x rather than forwarding GitHub bearer tokens."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # urllib's default redirect handler copies Authorization to a newly
        # constructed Request, including when Location names another host.
        # GitHub API operations must never authorize such a redirect.
        return None


class GitHubClient:
    """Bounded GitHub REST client; never logs tokens or response bodies."""

    def __init__(self, repository, token):
        if not token:
            raise CleanupError("GITHUB_TOKEN required for mutation")
        self.repository = _safe_repo(repository)
        self.token = token

    def request(self, method, path, payload=None):
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        req = Request("https://api.github.com" + path, data=data,
                      method=method, headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "research-branch-retirement/1.0",
        })
        # Defense in depth: even if redirect policy changes, never copy the
        # bearer token onto an automatically constructed redirected request.
        req.add_unredirected_header("Authorization", "Bearer " + self.token)
        try:
            # urllib's default HTTPRedirectHandler retains Authorization on
            # off-host redirects. Reject all redirects for this privileged
            # API client, including same-host aliases and renamed repos.
            with build_opener(_RejectAuthenticatedRedirect()).open(
                    req, timeout=20) as response:
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
        # Drop every inherited Git control variable, not only trace/config:
        # GIT_SSL_NO_VERIFY can disable TLS verification and GIT_ASKPASS or
        # GIT_EXEC_PATH can invoke untrusted local programs with the ephemeral
        # Authorization header available in their inherited environment.
        # Re-introduce only deliberately chosen GIT_* controls below.
        env = {key: value for key, value in os.environ.items()
               if not key.startswith("GIT_")
               and key not in ("SSH_ASKPASS", "SSH_ASKPASS_REQUIRE")}
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

def _require_immutable_archive_ruleset(client, repo):
    """Read back active archive-tag protection; never infer enforcement from CI."""
    root = f"/repos/{repo}/rulesets"
    rows, seen = [], set()
    for page in range(1, 11):
        current = client.get(
            f"{root}?includes_parents=true&per_page=100&page={page}"
        )
        if not isinstance(current, list):
            raise CleanupError("archive-tag ruleset inventory unavailable")
        for entry in current:
            if (not isinstance(entry, dict)
                    or type(entry.get("id")) is not int
                    or entry["id"] <= 0 or entry["id"] in seen):
                raise CleanupError("archive-tag ruleset inventory ambiguous")
            seen.add(entry["id"])
            rows.append(entry)
        if len(current) < 100:
            break
    else:
        raise CleanupError("archive-tag ruleset listing incomplete")
    matches = [entry for entry in rows
               if entry.get("name") == "immutable-branch-archive-tags"]
    if len(matches) != 1:
        raise CleanupError("archive-tag ruleset missing or duplicated")
    summary = matches[0]
    if (summary.get("source") != repo or summary.get("target") != "tag"
            or summary.get("enforcement") != "active"):
        raise CleanupError("archive-tag ruleset not active for expected repository")
    live = client.get(f"{root}/{summary['id']}")
    if (not isinstance(live, dict)
            or type(live.get("id")) is not int
            or live["id"] != summary["id"]
            or live.get("name") != summary["name"]
            or live.get("source") != repo
            or live.get("target") != "tag"
            or live.get("enforcement") != "active"
            or live.get("bypass_actors") != []
            or live.get("conditions") != {
                "ref_name": {"include": ["refs/tags/branch-archive/**/*"],
                             "exclude": []}}):
        raise CleanupError("archive-tag ruleset readback lacks strict protection")
    rules = live.get("rules")
    if not isinstance(rules, list):
        raise CleanupError("archive-tag ruleset rules missing")
    kinds = {}
    for rule in rules:
        if (not isinstance(rule, dict)
                or not isinstance(rule.get("type"), str)
                or rule["type"] in kinds):
            raise CleanupError("archive-tag ruleset rule invalid or duplicated")
        kinds[rule["type"]] = rule
    if (set(kinds) != {"update", "deletion"}
            or not isinstance(kinds["update"].get("parameters"), dict)
            or kinds["update"]["parameters"].get(
                "update_allows_fetch_and_merge") is not False):
        raise CleanupError("archive-tag ruleset mutation restrictions absent")


def retire_one(client, repo, item, *, audit_only=False, expected_main_sha=None):
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
    # The approval plan pins a specific observed main. A later fast-forward
    # must not silently enlarge the originally reviewed deletion scope.
    if expected_main_sha is not None and main_sha != expected_main_sha:
        return "blocked_main_moved"
    ancestry = client.get(
        f"/repos/{repo}/compare/{item['merge_commit_sha']}...{main_sha}"
    )
    if (not isinstance(ancestry, dict)
            or ancestry.get("status") not in ("ahead", "identical")
            or ancestry.get("behind_by") != 0):
        return "blocked_merge_not_in_main"
    tag = f"{ARCHIVE_PREFIX}/{name}"
    tag_path = _tag_ref(repo, tag)
    if not audit_only:
        _require_immutable_archive_ruleset(client, repo)
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
    if expected_main_sha is not None:
        # The main ref can move while tags are being prepared. This extra
        # check reduces stale-plan risk; it is not an atomic multi-ref lease.
        fresh_main = client.get(f"/repos/{repo}/branches/main")
        if (not isinstance(fresh_main, dict)
                or not isinstance(fresh_main.get("commit"), dict)
                or fresh_main["commit"].get("sha") != expected_main_sha):
            return "blocked_main_moved_before_delete"
    # The tag rules could change while the archive is created. Check again
    # immediately before the final SHA-leased branch mutation.
    _require_immutable_archive_ruleset(client, repo)
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
    metadata = client.get(f"/repos/{repo}")
    if not isinstance(metadata, dict) or metadata.get("default_branch") != "main":
        raise CleanupError("default branch changed; abort cleanup")
    # source_main_sha must be an enforcement precondition, not decorative
    # manifest metadata. Abort before creating even a recovery tag.
    main = client.get(f"/repos/{repo}/branches/main")
    if (not isinstance(main, dict)
            or not isinstance(main.get("commit"), dict)
            or main["commit"].get("sha") != plan["source_main_sha"]):
        raise CleanupError("approved main SHA moved; freeze and re-review plan")
    # A destructive session must stop before any tag is created if immutable
    # archive protection was never installed by the repository administrator.
    if not audit_only:
        _require_immutable_archive_ruleset(client, repo)
    results = []
    for item in plan["branches"]:
        try:
            status = retire_one(client, repo, item, audit_only=audit_only,
                                expected_main_sha=plan["source_main_sha"])
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
        plan = validate_plan(_load_strict_plan(args.plan))
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
    except CleanupError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except (ValueError, OSError):
        # Never expose local private plan paths or embedded field names.
        print("error: invalid cleanup input or remote operation", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
