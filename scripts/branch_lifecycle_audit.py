#!/usr/bin/env python3
"""Read-only branch audit. Never merges, deletes or rewrites refs."""
import argparse
import json
import os
import re
import sys
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

def audit(repo, base="main", get=fetch):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
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
    open_heads = {}
    for pr in prs:
        head = pr["head"]
        if head.get("repo") and head["repo"].get("full_name", "").lower() == repo.lower():
            open_heads.setdefault(head["ref"], []).append(pr["number"])
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
            if status not in ("identical", "behind", "ahead", "diverged") or type(ahead) is not int or type(behind) is not int or ahead < 0 or behind < 0 or (ahead == 0) != (status in ("identical", "behind")):
                raise ValueError("Inconsistent comparison for " + name)
        linked_prs = sorted(open_heads.get(name, []))
        rows.append({"branch": name, "sha": sha, "ahead": ahead, "behind": behind, "open_prs": linked_prs, "protected": protected, "decision": classify(base, name, protected, linked_prs, ahead)})
    if base not in seen:
        raise ValueError("Missing base from branch list")
    final_sha = base_sha()
    if final_sha != main_sha:
        for row in rows:
            if row["decision"] == "manual-prune-candidate":
                row["decision"] = "hold-base-moved-rerun"
    return {"repo": repo, "base": base, "base_sha": main_sha, "base_sha_at_end": final_sha, "read_only": True, "branch_count": len(rows), "open_pr_count": len(prs), "branches": rows}

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
