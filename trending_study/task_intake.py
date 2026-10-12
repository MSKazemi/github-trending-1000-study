"""Offline issue-candidate sampling. Not a reviewed task benchmark."""
import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

class IntakeError(ValueError):
    pass

def utc(value):
    if not isinstance(value, str):
        raise IntakeError("UTC timestamp required")
    try:
        x = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as e:
        raise IntakeError("invalid UTC date") from e
    if x.tzinfo is None or x.utcoffset() != timezone.utc.utcoffset(x):
        raise IntakeError("timezone must be UTC")
    return x

def sample(frame):
    required = {"schema_version","dataset_kind","source_panel","captured_at_utc","selection_seed","per_repo_target","sources"}
    if not isinstance(frame,dict) or set(frame)!=required:
        raise IntakeError("unexpected frame fields")
    if frame["schema_version"]!="1.0" or frame["dataset_kind"]!="public_issue_intake_unreviewed":
        raise IntakeError("invalid schema or dataset kind")
    captured=utc(frame["captured_at_utc"])
    if captured > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise IntakeError("future capture time cannot represent an observed issue frame")
    if not isinstance(frame["source_panel"], str) or not frame["source_panel"].strip():
        raise IntakeError("source_panel must identify the actual sampling frame")
    seed=frame["selection_seed"]
    target=frame["per_repo_target"]
    if not isinstance(seed,str) or not seed.strip() or type(target)!=int or not 1<=target<=10:
        raise IntakeError("invalid seed or sample target")
    sources=frame["sources"]
    if not isinstance(sources,list) or not 1<=len(sources)<=20:
        raise IntakeError("invalid sources")
    seen_ids=set()
    seen_repos=set()
    records=[]
    counts=[]
    for source in sources:
        if not isinstance(source,dict) or set(source)!={"repository","api_url","per_page","page","issues"}:
            raise IntakeError("unexpected source fields")
        repo=source["repository"]
        if not isinstance(repo,str) or repo.count("/")!=1 or repo.lower() in seen_repos:
            raise IntakeError("invalid or duplicate repository")
        owner,name=repo.split("/")
        if (not owner or not name or owner in (".", "..") or name in (".", "..")
                or not all(c.isascii() and (c.isalnum() or c in "_.-") for c in owner+name)):
            raise IntakeError("unsafe repository")
        seen_repos.add(repo.lower())
        url=f"https://api.github.com/repos/{repo}/issues?state=open&sort=created&direction=desc&per_page=15&page=1"
        if source["api_url"]!=url or source["per_page"]!=15 or source["page"]!=1:
            raise IntakeError("unexpected collection frame")
        issues=source["issues"]
        if not isinstance(issues,list) or len(issues)>15:
            raise IntakeError("invalid issue page")
        eligible=[]
        local=[]
        last=None
        numbers=set()
        for issue in issues:
            keys={"id","number","html_url","state","created_at_utc","updated_at_utc","is_pull_request"}
            if not isinstance(issue,dict) or set(issue)!=keys:
                raise IntakeError("unexpected issue fields: avoid usernames/bodies")
            i,n=issue["id"],issue["number"]
            if type(i)!=int or i<1 or type(n)!=int or n<1 or i in seen_ids or n in numbers:
                raise IntakeError("invalid or duplicate issue")
            seen_ids.add(i)
            numbers.add(n)
            if type(issue["is_pull_request"])!=bool or issue["state"]!="open":
                raise IntakeError("invalid open issue metadata")
            suffix="pull" if issue["is_pull_request"] else "issues"
            expected=f"https://github.com/{repo}/{suffix}/{n}"
            if issue["html_url"].lower()!=expected.lower():
                raise IntakeError("issue URL mismatch")
            created=utc(issue["created_at_utc"])
            updated=utc(issue["updated_at_utc"])
            if created>updated or updated>captured or (last is not None and created>last):
                raise IntakeError("bad timestamps/order")
            last=created
            rank=hashlib.sha256(f"{seed}|{repo.lower()}|{i}".encode()).hexdigest()
            row={"task_id":f"GH-{i}","repository":repo,"issue_id":i,"issue_number":n,"source_url":expected,"selection_digest":rank,
                 "selection_status":"excluded_pr_not_issue" if issue["is_pull_request"] else None,
                 "task_spec_status":"not_frozen","independent_acceptance_status":"not_frozen",
                 "reuse_opportunity":"unknown","experiment_enrollment_status":"not_eligible_unreviewed"}
            local.append(row)
            if not issue["is_pull_request"]:
                eligible.append(row)
        for row in sorted(eligible,key=lambda x:(x["selection_digest"],x["issue_id"]))[:target]:
            row["selection_status"]="selected_for_independent_task_screen"
        for row in eligible:
            if row["selection_status"] is None:
                row["selection_status"]="eligible_issue_not_sampled"
        records.extend(local)
        counts.append({"repository":repo,"page_rows":len(local),"eligible":len(eligible),"selected":sum(x["selection_status"]=="selected_for_independent_task_screen" for x in local)})
    digest=hashlib.sha256(json.dumps(frame,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
    return {"schema_version":"1.0","dataset_kind":"public_issue_intake_unreviewed",
            "status":"exploratory_convenience_panel_not_preregistered","source_panel":frame["source_panel"],
            "captured_at_utc":frame["captured_at_utc"],"reduced_frame_sha256":digest,
            "per_repo":counts,"total_rows":len(records),
            "selected_issue_candidates":sum(r["selection_status"]=="selected_for_independent_task_screen" for r in records),
            "ledger":records,"warning":"Unreviewed public issue leads only; not frozen tasks, gold labels, random GitHub sample, or causal evidence."}

def main(argv=None):
    p=argparse.ArgumentParser(description="Offline pilot issue intake, no GitHub access")
    p.add_argument("--input",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args(argv)
    try:
        result=sample(json.loads(Path(a.input).read_text(encoding="utf-8")))
        out=Path(a.output)
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open("x",encoding="utf-8") as f:
            json.dump(result,f,indent=2)
            f.write("\n")
    except (OSError,ValueError,TypeError) as e:
        p.exit(2,f"error: {e}\n")
    print(json.dumps({"total_rows":result["total_rows"],"selected_issue_candidates":result["selected_issue_candidates"]}))

if __name__=="__main__":
    main()
