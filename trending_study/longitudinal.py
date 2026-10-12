"""Immutable, opt-in GitHub 30/90/180-day follow-up instrument (stdlib-only).

A prospective plan is derived from externally approved baseline rows. The
software cannot authenticate that approval. It does NOT enroll any cohort,
infer historical stars, authorize scraping, or claim environmental outcomes.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import uuid

from .safe_io import disjoint, publish_json, publish_jsonl, refuse_existing

PLAN_VERSION = "followup-plan-1.0"
EVENT_VERSION = "followup-event-1.0"
FOLLOWUP_DAYS = (30, 90, 180)
REPO_NAME = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
FINAL_STATES = frozenset(("ok", "missed_window", "late_observation"))
EVENT_STATES = FINAL_STATES | frozenset((
    "http_error", "not_found_or_private_or_renamed", "rate_limited",
    "access_denied", "unauthorized", "network_error", "invalid_response",
    "identity_mismatch", "not_public",
))


class FollowupError(ValueError):
    """Invalid prospective schedule, event ledger or command argument."""


def utc(value, field):
    if not isinstance(value, str) or not value.strip():
        raise FollowupError(f"{field}: missing timestamp")
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise FollowupError(f"{field}: invalid timestamp") from exc
    if stamp.tzinfo is None or stamp.utcoffset() != timedelta(0):
        raise FollowupError(f"{field}: UTC offset must be explicitly +00:00 or Z")
    return stamp.astimezone(timezone.utc)


def is_natural(value):
    return type(value) is int and value >= 0


def text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise FollowupError(f"{field}: required nonempty text")
    return value.strip()


def jsonl_data(raw, kind):
    try:
        lines = raw.decode("utf-8").splitlines()
        rows = [json.loads(line) for line in lines if line.strip()]
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FollowupError(f"{kind}: malformed UTF-8 JSONL") from exc
    if not rows or any(not isinstance(x, dict) for x in rows):
        raise FollowupError(f"{kind}: expected nonempty JSONL objects")
    return rows


def task_key(study_id, repository_id, baseline_time, horizon, grace, protocol):
    payload = json.dumps(
        [study_id, repository_id, baseline_time, horizon, grace, protocol],
        separators=(",", ":"), ensure_ascii=False,
    )
    return sha256(payload.encode("utf-8")).hexdigest()


def make_plan(raw_baselines, grace_days):
    """Create a deterministic schedule from *self-declared approved* rows.

    The source byte hash links the schedule to a particular immutable input.
    An approval reference is metadata, never cryptographic proof of approval.
    """
    if len(grace_days) != 3 or any(
        type(g) is not int or g < 0 or g > 60 for g in grace_days
    ):
        raise FollowupError("grace_days needs three explicit integers in [0, 60]")
    rows = jsonl_data(raw_baselines, "baseline")
    source_sha = sha256(raw_baselines).hexdigest()
    seen = set()
    cohort_identity = None
    records = []
    for index, row in enumerate(rows, 1):
        loc = f"baseline row {index}"
        rid = row.get("repository_id")
        if type(rid) is not int or rid <= 0 or rid in seen:
            raise FollowupError(f"{loc}: duplicate or invalid stable repository_id")
        seen.add(rid)
        if row.get("eligible_for_confirmatory_cohort") is not True:
            raise FollowupError(f"{loc}: not declared cohort eligible; pilot-only rows cannot be planned")
        if row.get("metadata_status") != "ok":
            raise FollowupError(f"{loc}: no successful baseline metadata snapshot")
        name = text(row.get("full_name_at_enrichment"), loc + " full_name")
        if not REPO_NAME.fullmatch(name):
            raise FollowupError(f"{loc}: invalid repository full name")
        stars = row.get("stars")
        if not is_natural(stars):
            raise FollowupError(f"{loc}: baseline stars missing or invalid")
        stamp = utc(row.get("enriched_at_utc"), loc + " enriched_at_utc")
        if stamp > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise FollowupError(f"{loc}: baseline snapshot appears to be in the future")
        digest = row.get("source_sha256")
        if not isinstance(digest, str) or not HEX64.fullmatch(digest):
            raise FollowupError(f"{loc}: verified source SHA-256 required")
        study_id = text(row.get("study_id"), loc + " study_id")
        approval = text(row.get("cohort_approval_ref"), loc + " cohort_approval_ref")
        protocol = text(row.get("protocol_commit"), loc + " protocol_commit")
        if not HEX40.fullmatch(protocol):
            raise FollowupError(f"{loc}: protocol_commit must be a fixed 40-hex SHA")
        identity = (study_id, approval, protocol)
        if cohort_identity is None:
            cohort_identity = identity
        elif identity != cohort_identity:
            raise FollowupError("cannot combine different study/protocol/approval frames in one schedule")
        for days, grace in zip(FOLLOWUP_DAYS, grace_days):
            due = stamp + timedelta(days=days)
            end = due + timedelta(days=grace)
            row_out = {
                "schema_version": PLAN_VERSION,
                "task_id": task_key(study_id, rid, stamp.isoformat(), days, grace, protocol),
                "study_id": study_id,
                "repository_id": rid,
                "full_name_at_baseline": name,
                "baseline_stars": stars,
                "baseline_at_utc": stamp.isoformat(),
                "baseline_capture_sha256": digest,
                "cohort_input_sha256": source_sha,
                "cohort_approval_ref": approval,
                "protocol_commit": protocol,
                "followup_days": days,
                "grace_days": grace,
                "scheduled_at_utc": due.isoformat(),
                "expires_at_utc": end.isoformat(),
                "approval_verification": "self_reported_not_authenticated_by_software",
            }
            records.append(row_out)
    records.sort(key=lambda r: (r["repository_id"], r["followup_days"]))
    return records


def load_plan(path):
    raw = Path(path).read_bytes()
    plan = jsonl_data(raw, "plan")
    by_id = {}
    cohort_identity = None
    repo_days = set()
    for row in plan:
        if row.get("schema_version") != PLAN_VERSION:
            raise FollowupError("unsupported plan version")
        rid, days, grace = row.get("repository_id"), row.get("followup_days"), row.get("grace_days")
        if type(rid) is not int or rid <= 0 or type(days) is not int or days not in FOLLOWUP_DAYS:
            raise FollowupError("plan has invalid ID or follow-up days")
        if (rid, days) in repo_days:
            raise FollowupError("plan repeats a repository/horizon")
        repo_days.add((rid, days))
        if type(grace) is not int or grace < 0 or grace > 60:
            raise FollowupError("plan has invalid grace duration")
        baseline = utc(row.get("baseline_at_utc"), "plan.baseline_at_utc")
        due = utc(row.get("scheduled_at_utc"), "plan.scheduled_at_utc")
        expiry = utc(row.get("expires_at_utc"), "plan.expires_at_utc")
        if due != baseline + timedelta(days=days) or expiry != due + timedelta(days=grace):
            raise FollowupError("plan has inconsistent dates")
        study = text(row.get("study_id"), "plan.study_id")
        protocol = text(row.get("protocol_commit"), "plan.protocol_commit")
        if not HEX40.fullmatch(protocol):
            raise FollowupError("plan protocol SHA missing or malformed")
        if row.get("task_id") != task_key(
            study, rid, baseline.isoformat(), days, grace, protocol
        ):
            raise FollowupError("plan task ID does not match immutable parameters")
        if not REPO_NAME.fullmatch(text(row.get("full_name_at_baseline"), "plan.full_name")):
            raise FollowupError("plan repository name is invalid")
        if not is_natural(row.get("baseline_stars")):
            raise FollowupError("plan has invalid baseline stars")
        if not isinstance(row.get("cohort_input_sha256"), str) or not HEX64.fullmatch(row["cohort_input_sha256"]):
            raise FollowupError("plan is missing source evidence hash")
        approval = text(row.get("cohort_approval_ref"), "plan.cohort_approval_ref")
        identity = (study, protocol, approval, row["cohort_input_sha256"])
        if cohort_identity is None:
            cohort_identity = identity
        elif identity != cohort_identity:
            raise FollowupError("plan has mixed cohort/protocol/source provenance")
        if row["task_id"] in by_id:
            raise FollowupError("duplicate follow-up task_id")
        by_id[row["task_id"]] = row
    return plan, by_id, sha256(raw).hexdigest()


def load_events(events_dir, plan_by_id, plan_digest):
    path = Path(events_dir)
    events = {key: [] for key in plan_by_id}
    if not path.exists():
        return events
    if not path.is_dir():
        raise FollowupError("events-dir exists but is not a directory")
    ids = set()
    for item in sorted(path.glob("*.json")):
        try:
            record = json.loads(item.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise FollowupError(f"invalid event file (quarantine; do not delete): {item}") from exc
        if not isinstance(record, dict) or record.get("schema_version") != EVENT_VERSION:
            raise FollowupError(f"unrecognized event file: {item}")
        key = record.get("task_id")
        if key not in events or record.get("plan_sha256") != plan_digest:
            raise FollowupError(f"event does not belong to the immutable plan: {item}")
        expected = plan_by_id[key]
        if (record.get("repository_id") != expected["repository_id"]
                or record.get("followup_days") != expected["followup_days"]):
            raise FollowupError(f"event identity or horizon mismatch: {item}")
        event_id = text(record.get("event_id"), "event_id")
        if event_id in ids:
            raise FollowupError("duplicate event_id")
        ids.add(event_id)
        if record.get("status") not in EVENT_STATES:
            raise FollowupError(f"unrecognized event status in {item}")
        utc(record.get("observed_at_utc"), "event.observed_at_utc")
        events[key].append(record)
    return events


def classification(task, histories, moment):
    if any(event["status"] == "ok" for event in histories):
        return "completed"
    if any(event["status"] in ("missed_window", "late_observation") for event in histories):
        return "missed"
    due = utc(task["scheduled_at_utc"], "scheduled_at_utc")
    expiry = utc(task["expires_at_utc"], "expires_at_utc")
    if moment > expiry:
        return "expired"
    if moment < due:
        return "upcoming"
    if any(utc(event["observed_at_utc"], "event timestamp").date() == moment.date()
           for event in histories):
        return "attempted_today"
    return "due"


def summary(plan, events, moment):
    statuses = {name: 0 for name in
                ("completed", "missed", "expired", "upcoming", "attempted_today", "due")}
    for task in plan:
        statuses[classification(task, events[task["task_id"]], moment)] += 1
    return {
        "schema_version": PLAN_VERSION,
        "as_of_utc": moment.isoformat(),
        "planned_tasks": len(plan),
        "counts": statuses,
        "note": "Counts reflect immutable logs; due and expired are not proof of observed samples.",
    }


def _headers_data(headers):
    def integer(name):
        value = headers.get(name) if headers is not None else None
        try:
            return int(value) if value is not None and str(value).isdigit() else None
        except (ValueError, TypeError):
            return None
    return {
        "response_date_header": headers.get("Date") if headers is not None else None,
        "rate_limit_remaining": integer("X-RateLimit-Remaining"),
        "rate_limit_reset_epoch": integer("X-RateLimit-Reset"),
    }


def _request_snapshot(task, name, opener, token, clock):
    """One official REST get; no retry or sleep, no arbitrary URL execution."""
    if not REPO_NAME.fullmatch(name):
        raise FollowupError("unsafe repository name")
    url = "https://api.github.com/repos/" + name
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-trending-1000-study/longitudinal-1.0",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(url, headers=headers)
    result = {
        "api_url": url,
        "http_status": None,
        "full_name_at_followup": None,
        "stars": None, "forks": None, "open_issues_including_prs": None,
        "observed_repository_id": None,
        "response_date_header": None,
        "rate_limit_remaining": None, "rate_limit_reset_epoch": None,
        "status": "network_error",
    }
    stop = False
    try:
        with opener(request, timeout=20) as response:
            result["http_status"] = getattr(response, "status", 200)
            result.update(_headers_data(response.headers))
            payload = response.read(1_000_001)
        if result["http_status"] != 200 or len(payload) > 1_000_000:
            result["status"] = "invalid_response"
            stop = True
        else:
            info = json.loads(payload.decode("utf-8"))
            if not isinstance(info, dict):
                raise ValueError("expected JSON object")
            actual_id = info.get("id")
            result["observed_repository_id"] = actual_id if type(actual_id) is int else None
            if actual_id != task["repository_id"] or type(actual_id) is not int:
                result["status"] = "identity_mismatch"
                stop = True
            elif info.get("private") is True:
                result["status"] = "not_public"
                stop = True
            else:
                current_name = info.get("full_name")
                if not isinstance(current_name, str) or not REPO_NAME.fullmatch(current_name):
                    raise ValueError("invalid returned repository name")
                for key in ("stargazers_count", "forks_count", "open_issues_count"):
                    if not is_natural(info.get(key)):
                        raise ValueError("missing/invalid GitHub counter")
                result.update({
                    "status": "ok",
                    "full_name_at_followup": current_name,
                    "stars": info["stargazers_count"],
                    "forks": info["forks_count"],
                    "open_issues_including_prs": info["open_issues_count"],
                })
    except HTTPError as exc:
        result["http_status"] = exc.code
        result.update(_headers_data(exc.headers))
        if exc.code in (404, 410):
            result["status"] = "not_found_or_private_or_renamed"
        elif exc.code == 429 or (exc.code == 403 and result["rate_limit_remaining"] == 0):
            result["status"] = "rate_limited"
            stop = True
        elif exc.code == 403:
            result["status"] = "access_denied"
            stop = True
        elif exc.code == 401:
            result["status"] = "unauthorized"
            stop = True
        else:
            result["status"] = "http_error"
            stop = exc.code >= 500
    except (URLError, OSError, TimeoutError):
        result["status"] = "network_error"
        stop = True
    except (UnicodeDecodeError, ValueError):
        result["status"] = "invalid_response"
        stop = True
    if result["rate_limit_remaining"] is not None and result["rate_limit_remaining"] <= 1:
        stop = True
    observed = clock()
    result["observed_at_utc"] = observed.isoformat()
    result["lag_seconds"] = round((observed - utc(task["scheduled_at_utc"], "due")).total_seconds(), 3)
    if result["status"] == "ok" and observed > utc(task["expires_at_utc"], "expires"):
        result["status"] = "late_observation"
    return result, stop


def _event(task, digest, stamp, *, status, **kwargs):
    return {
        "schema_version": EVENT_VERSION,
        "event_id": uuid.uuid4().hex,
        "plan_sha256": digest,
        "task_id": task["task_id"],
        "study_id": task["study_id"],
        "repository_id": task["repository_id"],
        "followup_days": task["followup_days"],
        "scheduled_at_utc": task["scheduled_at_utc"],
        "expires_at_utc": task["expires_at_utc"],
        "observed_at_utc": stamp.isoformat(),
        "status": status,
        **kwargs,
    }


def _record(events_dir, event):
    ts = utc(event["observed_at_utc"], "observed_at_utc").strftime("%Y%m%dT%H%M%S%f")
    name = f'{event["task_id"]}-{ts}-{event["event_id"]}.json'
    publish_json(Path(events_dir) / name, event)


@contextmanager
def exclusive_collector(events_dir):
    target = Path(events_dir)
    target.mkdir(parents=True, exist_ok=True)
    lock = target / ".followup.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise FollowupError("collector lock exists; inspect prior process before manually recovering") from exc
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(f"pid={os.getpid()} (not proof process is alive)\n")
        yield
    finally:
        # A crash leaves the lock for explicit manual incident review.
        lock.unlink(missing_ok=True)


def collect(plan_path, events_dir, *, allow_network=False, max_requests=5,
            max_events=10, opener=None, clock=None, token=None):
    """Bounded explicit run; never makes calls merely because status was queried."""
    if not allow_network:
        raise FollowupError("network collection requires explicit --confirm-network")
    if not (type(max_requests) is int and 1 <= max_requests <= 20):
        raise FollowupError("max_requests must be 1..20")
    if not (type(max_events) is int and 1 <= max_events <= 100):
        raise FollowupError("max_events must be 1..100")
    disjoint(plan_path, events_dir)
    plan, lookup, digest = load_plan(plan_path)
    opener = opener or urlopen
    clock = clock or (lambda: datetime.now(timezone.utc))
    token = os.environ.get("GITHUB_TOKEN", "") if token is None else token
    result = {"requests": 0, "new_events": 0, "stopped_early": False}
    with exclusive_collector(events_dir):
        events = load_events(events_dir, lookup, digest)
        for task in plan:
            now = clock()
            state = classification(task, events[task["task_id"]], now)
            if state not in ("expired", "due") or result["new_events"] >= max_events:
                continue
            if state == "expired":
                new = _event(
                    task, digest, now, status="missed_window",
                    http_status=None, stars=None,
                    reason="No valid observation before expiry; never substitute a late count.",
                )
            else:
                if result["requests"] >= max_requests:
                    break
                candidates = [
                    event for histories in events.values() for event in histories
                    if event["repository_id"] == task["repository_id"]
                    and event["status"] == "ok"
                    and isinstance(event.get("full_name_at_followup"), str)
                ]
                candidates.sort(key=lambda event: event["observed_at_utc"])
                name = (candidates[-1]["full_name_at_followup"] if candidates
                        else task["full_name_at_baseline"])
                detail, stop = _request_snapshot(task, name, opener, token, clock)
                new = _event(task, digest, utc(detail.pop("observed_at_utc"), "fetch time"),
                             status=detail.pop("status"), **detail)
                result["requests"] += 1
            _record(events_dir, new)
            events[task["task_id"]].append(new)
            result["new_events"] += 1
            if state == "due" and stop:
                result["stopped_early"] = True
                break
        result["summary"] = summary(plan, events, clock())
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prospective, opt-in GitHub follow-up records")
    sub = parser.add_subparsers(dest="command", required=True)
    planned = sub.add_parser("plan", help="Write a new deterministic schedule from human-approved baseline rows")
    planned.add_argument("--input", required=True)
    planned.add_argument("--output", required=True)
    planned.add_argument("--grace-days", type=int, nargs=3, required=True,
                         metavar=("D30", "D90", "D180"),
                         help="Explicit prespecified post-due grace days, e.g. 3 7 14")
    status = sub.add_parser("status", help="Offline schedule and immutable event-ledger summary")
    status.add_argument("--plan", required=True)
    status.add_argument("--events-dir", required=True)
    request = sub.add_parser("collect", help="Explicitly fetch a bounded set of due public repository snapshots")
    request.add_argument("--plan", required=True)
    request.add_argument("--events-dir", required=True)
    request.add_argument("--confirm-network", action="store_true",
                         help="Required affirmative opt-in; does not authorize unsanctioned cohort collection")
    request.add_argument("--max-requests", type=int, default=5)
    request.add_argument("--max-events", type=int, default=10)
    args = parser.parse_args(argv)
    try:
        if args.command == "plan":
            disjoint(args.input, args.output)
            refuse_existing(args.output)
            raw = Path(args.input).read_bytes()
            plan = make_plan(raw, args.grace_days)
            publish_jsonl(args.output, plan)
            output = {
                "planned_followups": len(plan),
                "distinct_stable_ids": len(plan) // 3,
                "source_sha256": sha256(raw).hexdigest(),
                "approval_warning": "Self-declared approval references were not independently authenticated.",
            }
        elif args.command == "status":
            plan, keys, digest = load_plan(args.plan)
            output = summary(plan, load_events(args.events_dir, keys, digest),
                             datetime.now(timezone.utc))
        else:
            output = collect(args.plan, args.events_dir,
                             allow_network=args.confirm_network,
                             max_requests=args.max_requests, max_events=args.max_events)
        print(json.dumps(output, sort_keys=True, indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
