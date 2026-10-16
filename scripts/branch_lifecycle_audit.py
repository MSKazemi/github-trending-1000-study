#!/usr/bin/env python3
"""Read-only branch audit. Never merges, deletes or rewrites refs."""
import argparse
import json
import os
import re
import sys
from urllib.parse import quote
from urllib.request import Request, urlopen

def fetch(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "trending-study-branch-audit"}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urlopen(Request("https://api.github.com" + path, headers=headers), timeout=25) as response:
        return json.load(response)

def pages(path, get=fetch, max_pages=30):
    results = []
    for page in range(1, max_pages + 1):
        separator = "&" if "?" in path else "?"
        data = get(f"{path}{separator}per_page=100&page={page}")
        if not isinstance(data, list):
            raise RuntimeError("Invalid page; refusing partial inventory")
        results.extend(data)
        if len(data) < 100:
            return results
    raise RuntimeError("Too many pages; refusing partial inventory")

def classify(base, name, protected, open_prs, ahead):
    if name == base:
        return "keep-base"
    if protected:
        return "keep-protected"
    if open_prs:
        return "keep-open-pr"
    if ahead > 0:
        return "hold-unique-history"
    if ahead == 0:
        return "manual-prune-candidate"
    raise ValueError("Invalid ahead count")

def _open_pr_snapshot(prs, repo):
    """Build a strict PR-head inventory; unknown ownership cannot mean no PR."""
    open_heads, rows, seen = {}, set(), set()
    for pr in prs:
        if not isinstance(pr, dict) or type(pr.get("number")) is not int or pr["number"] <= 0:
            raise ValueError("Malformed open PR inventory")
        number = pr["number"]
        if number in seen:
            raise ValueError("Duplicate open PR number")
        seen.add(number)
        head = pr.get("head")
        if not isinstance(head, dict) or not isinstance(head.get("ref"), str) or not head["ref"]:
            raise ValueError("Malformed open PR head")
        owner = head.get("repo")
        if not isinstance(owner, dict) or not isinstance(owner.get("full_name"), str):
            raise ValueError("Unverifiable open PR head repository")
        full_name = owner["full_name"].lower()
        rows.add((number, head["ref"], full_name))
        if full_name == repo.lower():
            open_heads.setdefault(head["ref"], []).append(number)
    return open_heads, rows


def _quoted_branch(name):
    """Reject unsafe API-supplied refs; escape URL path separators correctly."""
    if (not isinstance(name, str) or
            not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}", name) or
            name.startswith("refs/") or name.endswith((".", "/")) or ".." in name or
            any(part in ("", ".", "..") for part in name.split("/"))):
        raise ValueError("Unsafe Git branch name in inventory")
    return quote(name, safe="/")


def audit(repo, base="main", get=fetch):
    # Reject relative-dot segments BEFORE composing any GitHub API route.
    # The broad repository-name alphabet alone would otherwise accept
    # '../name' or 'owner/..' as apparent owner/repo identities.
    if (not isinstance(repo, str) or
            not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or
            any(part in (".", "..") for part in repo.split("/"))):
        raise ValueError("Expected owner/repo")
    # The base comes from a CLI argument and must never alter API URL routes.
    if (not isinstance(base, str) or not re.fullmatch(
            r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}", base)
            or base.startswith("refs/") or ".." in base
            or any(part in ("", ".", "..") for part in base.split("/"))
            or base.endswith((".", "/"))):
        raise ValueError("Invalid base ref")
    prefix = "/repos/" + repo
    branches = pages(prefix + "/branches", get)
    prs = pages(prefix + "/pulls?state=open", get)
    def base_sha():
        branch = get(prefix + "/branches/" + base)
        sha = branch["commit"]["sha"]
        if not re.fullmatch("[0-9a-f]{40}", sha):
            raise ValueError("Invalid base SHA")
        return sha
    main_sha = base_sha()
    # Pagination and base lookup are separate REST requests. If the branch
    # listing saw another base commit, abort instead of suggesting stale
    # candidates: a later stable lookup alone cannot repair that snapshot.
    listed_base = [item for item in branches if item.get("name") == base]
    if (len(listed_base) != 1 or
            listed_base[0].get("commit", {}).get("sha") != main_sha):
        raise ValueError("Base SHA moved or missing during branch inventory")
    open_heads, original_prs = _open_pr_snapshot(prs, repo)
    rows, seen = [], set()
    for branch in branches:
        name = branch["name"]
        sha = branch["commit"]["sha"]
        if name in seen or not re.fullmatch("[0-9a-f]{40}", sha):
            raise ValueError("Malformed or duplicate ref")
        seen.add(name)
        protected = branch["protected"]
        if type(protected) is not bool:
            raise ValueError("Unknown protection")
        if name == base:
            ahead = behind = 0
        else:
            comparison = get(f"{prefix}/compare/{main_sha}...{sha}")
            ahead, behind = comparison["ahead_by"], comparison["behind_by"]
            status = comparison["status"]
            if (status not in ("identical", "behind", "ahead", "diverged")
                    or type(ahead) is not int or type(behind) is not int
                    or ahead < 0 or behind < 0
                    or (status == "identical" and (ahead != 0 or behind != 0))
                    or (status == "behind" and (ahead != 0 or behind <= 0))
                    or (status == "ahead" and (ahead <= 0 or behind != 0))
                    or (status == "diverged" and (ahead <= 0 or behind <= 0))):
                raise ValueError("Inconsistent comparison for " + name)
        linked_prs = sorted(open_heads.get(name, []))
        rows.append({"branch": name, "sha": sha, "ahead": ahead, "behind": behind, "open_prs": linked_prs, "protected": protected, "decision": classify(base, name, protected, linked_prs, ahead)})
    if base not in seen:
        raise ValueError("Missing base from branch list")

    # A listing and an ancestry comparison are NOT an atomic snapshot.
    # Before suggesting even a manual prune, re-read every candidate's exact
    # remote tip AND protection state. Do not use these checks as delete authority:
    # the separately approved SHA-leased retirement workflow owns mutation.
    candidates = [row for row in rows if row["decision"] == "manual-prune-candidate"]
    for row in candidates:
        detail = get(f"{prefix}/branches/{_quoted_branch(row['branch'])}")
        if (not isinstance(detail, dict) or detail.get("name") != row["branch"]
                or not isinstance(detail.get("commit"), dict)
                or not isinstance(detail["commit"].get("sha"), str)
                or not re.fullmatch("[0-9a-f]{40}", detail["commit"]["sha"])
                or type(detail.get("protected")) is not bool):
            raise ValueError("Cannot safely recheck prune-candidate branch")
        if (detail["commit"]["sha"] != row["sha"]
                or detail["protected"] != row["protected"]):
            row["decision"] = "hold-ref-or-protection-moved-rerun"

    if candidates:
        # Re-fetch all pages of open PRs: a PR created between the two reads
        # must not leave an outdated 'no open PR' conclusion in the report.
        latest_prs = pages(prefix + "/pulls?state=open", get)
        _, updated_prs = _open_pr_snapshot(latest_prs, repo)
        if updated_prs != original_prs:
            for row in candidates:
                if row["decision"] == "manual-prune-candidate":
                    row["decision"] = "hold-open-pr-inventory-moved-rerun"

    # Re-list the WHOLE paginated namespace, not just the candidate refs.
    # A concurrently added/deleted/retargeted source branch makes this a
    # moving inventory, not a no-loss census; never report a candidate ready.
    # A second read cannot guarantee atomicity, but it catches a common
    # inconsistent snapshot failure without any write API calls.
    latest_branches = pages(prefix + "/branches", get)
    latest_snapshot = set()
    for item in latest_branches:
        if (not isinstance(item, dict) or not isinstance(item.get("name"), str)
                or not isinstance(item.get("commit"), dict)
                or not isinstance(item["commit"].get("sha"), str)
                or not re.fullmatch("[0-9a-f]{40}", item["commit"]["sha"])
                or type(item.get("protected")) is not bool):
            raise ValueError("Malformed refreshed branch inventory")
        latest_snapshot.add((item["name"], item["commit"]["sha"], item["protected"]))
    if len(latest_snapshot) != len(latest_branches):
        raise ValueError("Duplicate refreshed branch inventory record")
    original_snapshot = {(row["branch"], row["sha"], row["protected"]) for row in rows}
    inventory_stable = latest_snapshot == original_snapshot
    if not inventory_stable:
        for row in candidates:
            if row["decision"] == "manual-prune-candidate":
                row["decision"] = "hold-branch-inventory-moved-rerun"

    final_sha = base_sha()
    if final_sha != main_sha:
        for row in rows:
            if row["decision"] == "manual-prune-candidate":
                row["decision"] = "hold-base-moved-rerun"
    return {"repo": repo, "base": base, "base_sha": main_sha,
            "base_sha_at_end": final_sha, "read_only": True,
            "branch_inventory_stable_at_second_read": inventory_stable,
            "branch_count": len(rows), "open_pr_count": len(prs), "branches": rows}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base", default="main")
    args = parser.parse_args()
    try:
        print(json.dumps(audit(args.repo, args.base), indent=2))
    except Exception as exc:
        print("Audit failed closed: " + type(exc).__name__, file=sys.stderr)
        sys.exit(2)
