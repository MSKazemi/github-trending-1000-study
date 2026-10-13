"""Conservative two-phase retirement of already-merged GitHub PR branches.

Audit is read-only. Retire requires explicit confirmation, runtime checks and
verified archive tags preserving the original branch commit ancestry. This
does NOT merge changes, review draft research, or rewrite main.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

_SHA = re.compile(r"^[a-f0-9]{40}$")
_BRANCH = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,180}$")
CONFIRM = "RETIRE_VERIFIED_MERGED_BRANCHES"
MAX_ITEMS = 80


class RetirementError(ValueError):
    pass


def check_manifest(data):
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise RetirementError("unsupported manifest schema")
    if data.get("repository") != "MSKazemi/github-trending-1000-study":
        raise RetirementError("repository does not match the locked cleanup target")
    if data.get("default_branch") != "main":
        raise RetirementError("default branch must be main")
    prefix = data.get("archive_tag_prefix")
    if not isinstance(prefix, str) or not re.fullmatch(
            r"archive/[A-Za-z0-9][A-Za-z0-9._/-]{0,120}", prefix):
        raise RetirementError("archive tag prefix invalid")
    if type(data.get("batch_size")) is not int or not 1 <= data["batch_size"] <= 20:
        raise RetirementError("archive batch size must be 1..20")
    items = data.get("candidates")
    if not isinstance(items, list) or not 1 <= len(items) <= MAX_ITEMS:
        raise RetirementError("candidate list must be nonempty and bounded")
    if type(data.get("candidate_count")) is not int or data["candidate_count"] != len(items):
        raise RetirementError("manifest candidate count mismatch")
    names = set()
    for row in items:
        if not isinstance(row, dict):
            raise RetirementError("candidate must be an object")
        name, sha, merge = row.get("branch"), row.get("sha"), row.get("merge_commit_sha")
        if (not isinstance(name, str) or not _BRANCH.fullmatch(name)
                or ".." in name or "//" in name or name.endswith(("/", ".", ".lock"))
                or name in {"main", "master"} or name.startswith(("archive/", "refs/"))
                or name in names):
            raise RetirementError("duplicate or unsafe retirement branch name")
        names.add(name)
        if any(not isinstance(v, str) or not _SHA.fullmatch(v) for v in (sha, merge)):
            raise RetirementError(f"{name}: exact lowercase commit SHAs required")
        if type(row.get("merged_pr")) is not int or row["merged_pr"] <= 0:
            raise RetirementError(f"{name}: positive merged PR number required")
    return sorted(items, key=lambda row: row["branch"])


def archive_batches(items, main_sha, prefix, batch_size):
    if not _SHA.fullmatch(main_sha):
        raise RetirementError("main must resolve to a full commit SHA")
    result = []
    for start in range(0, len(items), batch_size):
        chunk = items[start:start + batch_size]
        result.append({
            "tag": f"{prefix}-part-{start // batch_size + 1:02d}",
            "parents": [main_sha] + [row["sha"] for row in chunk],
            "branches": [row["branch"] for row in chunk],
        })
    return result


class GitHub:
    def __init__(self, repo, token):
        if repo != "MSKazemi/github-trending-1000-study" or not token:
            raise RetirementError("locked repository and GitHub token required")
        self.root = f"https://api.github.com/repos/{repo}"
        self.token = token

    def call(self, method, path, payload=None, *, optional=False):
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = Request(
            self.root + path, data=body, method=method,
            headers={
                "Authorization": "Bearer " + self.token,
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Content-Type": "application/json",
            },
        )
        try:
            with urlopen(request, timeout=25) as response:
                data = response.read()
                return json.loads(data) if data else None
        except HTTPError as exc:
            if optional and exc.code == 404:
                return None
            raise RetirementError(f"GitHub {method} {path}: HTTP {exc.code}") from exc
        except (URLError, TimeoutError, ValueError) as exc:
            raise RetirementError(f"GitHub {method} {path}: request/JSON failure") from exc

    def get(self, path, *, optional=False):
        return self.call("GET", path, optional=optional)

    def post(self, path, payload):
        return self.call("POST", path, payload)

    def delete(self, path):
        return self.call("DELETE", path)


def ref_path(branch):
    return "/git/ref/heads/" + quote(branch, safe="/")


def open_pr_heads(api):
    heads = set()
    for page in range(1, 12):
        items = api.get(f"/pulls?state=open&per_page=100&page={page}")
        if not isinstance(items, list):
            raise RetirementError("open PR list could not be validated")
        for pr in items:
            if pr.get("head", {}).get("repo", {}).get("full_name") == (
                    "MSKazemi/github-trending-1000-study"):
                heads.add(pr["head"]["ref"])
        if len(items) < 100:
            return heads
    raise RetirementError("open PR list exceeds audit pagination bound")


def audit_branch(api, row, main_sha, open_heads):
    branch = row["branch"]
    if branch in open_heads:
        raise RetirementError(f"{branch}: has an open pull request")
    ref = api.get(ref_path(branch))
    if not isinstance(ref, dict) or ref.get("object", {}).get("sha") != row["sha"]:
        raise RetirementError(f"{branch}: branch moved or disappeared since snapshot")
    meta = api.get("/branches/" + quote(branch, safe="/"))
    if not isinstance(meta, dict) or meta.get("protected") is not False:
        raise RetirementError(f"{branch}: protected or unknown branch protection")
    pr = api.get(f"/pulls/{row['merged_pr']}")
    if (not isinstance(pr, dict) or not pr.get("merged_at") or pr.get("state") != "closed"
            or pr.get("head", {}).get("ref") != branch
            or pr.get("head", {}).get("sha") != row["sha"]
            or pr.get("head", {}).get("repo", {}).get("full_name") != (
                "MSKazemi/github-trending-1000-study")
            or pr.get("base", {}).get("ref") != "main"
            or pr.get("merge_commit_sha") != row["merge_commit_sha"]):
        raise RetirementError(f"{branch}: merged PR evidence mismatched")
    comparison = api.get(
        f"/compare/{row['merge_commit_sha']}...{main_sha}")
    if (not isinstance(comparison, dict)
            or comparison.get("status") not in {"ahead", "identical"}
            or comparison.get("behind_by") != 0):
        raise RetirementError(f"{branch}: merge commit is not proven in current main")


def audit_live(api, data):
    items = check_manifest(data)
    main_ref = api.get("/git/ref/heads/main")
    main_sha = (main_ref or {}).get("object", {}).get("sha")
    if not isinstance(main_sha, str) or not _SHA.fullmatch(main_sha):
        raise RetirementError("cannot verify current main commit")
    open_heads = open_pr_heads(api)
    for row in items:
        audit_branch(api, row, main_sha, open_heads)
    return main_sha, items


def archive_all(api, items, main_sha, data):
    main = api.get("/git/commits/" + main_sha)
    tree = (main or {}).get("tree", {}).get("sha")
    if not isinstance(tree, str) or not _SHA.fullmatch(tree):
        raise RetirementError("cannot establish original main tree")
    batches = archive_batches(
        items, main_sha, data["archive_tag_prefix"], data["batch_size"])
    for batch in batches:
        path = "/git/ref/tags/" + quote(batch["tag"], safe="/")
        tag = api.get(path, optional=True)
        if tag is None:
            commit = api.post("/git/commits", {
                "message": (
                    "Archive original heads of already-merged PR branches.\n"
                    "Audit-only synthetic octopus ancestry; this is NOT a code merge."),
                "tree": tree,
                "parents": batch["parents"],
            })
            sha = (commit or {}).get("sha")
            if not isinstance(sha, str) or not _SHA.fullmatch(sha):
                raise RetirementError(f"{batch['tag']}: GitHub archive commit failed")
            api.post("/git/refs", {
                "ref": "refs/tags/" + batch["tag"], "sha": sha,
            })
            tag = api.get(path)
        anchor_sha = (tag or {}).get("object", {}).get("sha")
        anchor = api.get("/git/commits/" + str(anchor_sha))
        if (not isinstance(anchor, dict)
                or anchor.get("tree", {}).get("sha") != tree
                or [p.get("sha") for p in anchor.get("parents", [])] != batch["parents"]):
            raise RetirementError(f"{batch['tag']}: archive tag has wrong tree/parents")
    return [b["tag"] for b in batches]


def retire(api, data, confirmation):
    if confirmation != CONFIRM:
        raise RetirementError("destructive mode requires exact confirmation string")
    main_sha, items = audit_live(api, data)
    tags = archive_all(api, items, main_sha, data)
    # No deletion until ALL archive tags have been independently read back.
    if api.get("/git/ref/heads/main").get("object", {}).get("sha") != main_sha:
        raise RetirementError("main moved during archive publication")
    fresh_open = open_pr_heads(api)
    deleted = []
    for row in items:
        # Fail closed if a branch was repurposed while the archive was built.
        audit_branch(api, row, main_sha, fresh_open)
        api.delete(ref_path(row["branch"]))
        if api.get(ref_path(row["branch"]), optional=True) is not None:
            raise RetirementError(f"{row['branch']}: deletion did not persist")
        deleted.append(row["branch"])
    return {"retired": deleted, "count": len(deleted), "archive_tags": tags,
            "main_sha": main_sha, "data_not_modified": True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--mode", choices=("audit", "retire"), default="audit")
    parser.add_argument("--confirmation", default="")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
        items = check_manifest(data)
        if args.mode == "retire" and args.confirmation != CONFIRM:
            raise RetirementError("explicit confirmation is required before any API call")
        api = GitHub(data["repository"], os.environ.get("GITHUB_TOKEN"))
        if args.mode == "audit":
            current, verified = audit_live(api, data)
            report = {"mode": "audit", "eligible": len(verified),
                      "main_sha": current, "archive_tags_created": False,
                      "deleted": 0}
        else:
            report = retire(api, data, args.confirmation)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    except (RetirementError, OSError, ValueError, KeyError) as exc:
        print(f"branch retirement blocked: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
