"""Command-line collection utilities, Python standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .pilot import (build_capture_manifest, evaluate_preflight,
                    validate_capture, write_json)

VERSION = "0.2.0"
GITHUB_HOST = "https://github.com"
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class TrendingParser(HTMLParser):
    """Extract h2 > a repository links nested in article.Box-row.

    This deliberately does not attempt a broad heuristic HTML extraction:
    layout changes should result in an explicit failure, not false observations.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.h2_depth = 0
        self.active_links = []
        self.repos = []

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "article" and "Box-row" in attr.get("class", "").split():
            self.article_depth += 1
        elif tag == "article" and self.article_depth:
            self.article_depth += 1
        if not self.article_depth:
            return
        if tag == "h2":
            self.h2_depth += 1
        if tag == "a" and self.h2_depth:
            self.active_links.append(attr.get("href", ""))

    def handle_endtag(self, tag):
        if not self.article_depth:
            return
        if tag == "h2" and self.h2_depth:
            self.h2_depth -= 1
        if tag == "article":
            self.article_depth -= 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)


def extract_repos(html):
    parser = TrendingParser()
    parser.feed(html)
    found = []
    seen = set()
    for href in parser.active_links:
        href = href.strip()
        if href.startswith("/"):
            name = href.strip("/")
        else:
            continue
        if REPO.fullmatch(name) and name not in seen:
            seen.add(name)
            found.append(name)
    if not found:
        raise ValueError("No Trending repository entries found; aborting rather than returning empty data")
    return found


def write_jsonl(path, rows):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def read_jsonl(path):
    with Path(path).open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Bad JSONL at line {number}") from exc


def capture(args):
    """One explicit network request; optional manifest records provenance at fetch."""
    if args.date != datetime.now(timezone.utc).date().isoformat():
        raise ValueError("Capture date must be today's UTC date; historic Trending pages cannot be backfilled")
    url = f"{GITHUB_HOST}/trending?since={args.window}"
    request = Request(
        url,
        headers={
            "User-Agent": "github-trending-1000-study-research/0.2 (+https://github.com/MSKazemi/github-trending-1000-study)",
            "Accept": "text/html",
        },
    )
    with urlopen(request, timeout=25) as response:
        raw = response.read(4_000_001)
        content_type = response.headers.get("Content-Type", "")
        response_date = response.headers.get("Date")
        http_status = getattr(response, "status", 200)
    captured_at = utc_now()
    if len(raw) > 4_000_000:
        raise ValueError("HTML response exceeds 4MB safety limit")
    if args.date != datetime.fromisoformat(captured_at).date().isoformat():
        raise ValueError("UTC day rolled over during capture; retry using the new UTC date")
    manifest = build_capture_manifest(
        raw=raw, output=args.output, window=args.window,
        captured_at_utc=captured_at, content_type=content_type,
        http_status=http_status, response_date_header=response_date,
    )
    if args.manifest_output and Path(args.manifest_output).resolve() == Path(args.output).resolve():
        raise ValueError("Manifest output must differ from the raw capture file")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_bytes(raw)
    if args.manifest_output:
        write_json(args.manifest_output, manifest)
    print(json.dumps({
        "source_url": manifest["source_url"],
        "sha256": manifest["source_sha256"],
        "bytes": manifest["bytes"],
        "captured_at_utc": manifest["captured_at_utc"],
        "path": args.output,
        "manifest_path": args.manifest_output,
        "provenance_warning": manifest["provenance_warning"],
    }))


def parse_trending(args):
    raw = Path(args.input).read_bytes()
    repos = extract_repos(raw.decode("utf-8"))
    # A locally stored capture may come from a past date; state only supplied metadata, never assert validated source date.
    rows = []
    now = utc_now()
    url = f"{GITHUB_HOST}/trending?since={args.window}"
    for rank, repository in enumerate(repos, 1):
        rows.append({"schema_version": "0.1", "repository": repository, "trending_url": url, "source_file": str(args.input), "source_sha256": hashlib.sha256(raw).hexdigest(), "collected_at_utc": now, "observation_date": args.date, "window": args.window, "rank": rank, "parser_version": VERSION, "language_filter": None, "parsed_at_utc": now, "capture_time_status": "unverified_parse_only", "eligible_for_confirmatory_cohort": False})
    write_jsonl(args.output, rows)
    print(f"Wrote {len(rows)} parse-only occurrences; capture timestamp NOT verified; not cohort eligible: {args.output}")


def pilot_parse(args):
    """Strictly parse a stored raw capture with its matching manifest."""
    if Path(args.input).resolve() == Path(args.output).resolve():
        raise ValueError("Refusing to overwrite raw source with parsed output")
    if Path(args.manifest).resolve() == Path(args.output).resolve():
        raise ValueError("Refusing to overwrite source manifest with parsed output")
    raw = Path(args.input).read_bytes()
    manifest_raw = Path(args.manifest).read_bytes()
    manifest = json.loads(manifest_raw.decode("utf-8"))
    rows, audit = validate_capture(raw, manifest, extract_repos=extract_repos)
    manifest_hash = hashlib.sha256(manifest_raw).hexdigest()
    for row in rows:
        row["source_file"] = str(args.input)
        row["source_manifest"] = str(args.manifest)
        row["source_manifest_sha256"] = manifest_hash
        row["parser_version"] = VERSION
    audit["source_manifest_sha256"] = manifest_hash
    if args.audit_output and Path(args.audit_output).resolve() in (
        Path(args.input).resolve(), Path(args.manifest).resolve(),
        Path(args.output).resolve(),
    ):
        raise ValueError("Audit output must differ from input, manifest and JSONL output")
    write_jsonl(args.output, rows)
    if args.audit_output:
        write_json(args.audit_output, audit)
    print(json.dumps(audit, sort_keys=True))


def pilot_preflight(args):
    """Document gate completeness; never call it a signed or approved study."""
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    summary = evaluate_preflight(data, stage=args.stage)
    print(json.dumps(summary, sort_keys=True, indent=2))
    if args.require_ready and summary["decision"] != "ready_for_human_review":
        raise RuntimeError("Pilot/confirmatory prerequisites are not complete. Human signoff is still required.")


def enrich(args):
    token = os.environ.get("GITHUB_TOKEN", "")
    result = []
    for row in read_jsonl(args.input):
        name = row.get("repository", "")
        if not REPO.fullmatch(name):
            raise ValueError(f"Unsafe repository identifier: {name!r}")
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "github-trending-1000-study-research/0.1"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(f"https://api.github.com/repos/{name}", headers=headers)
        record = dict(row)
        record["enriched_at_utc"] = utc_now()
        try:
            with urlopen(request, timeout=20) as response:
                info = json.load(response)
            record.update({"repository_id": info.get("id"), "full_name_at_enrichment": info.get("full_name"), "stars": info.get("stargazers_count"), "forks": info.get("forks_count"), "open_issues": info.get("open_issues_count"), "primary_language": info.get("language"), "created_at": info.get("created_at"), "pushed_at": info.get("pushed_at"), "archived": info.get("archived"), "fork": info.get("fork"), "description": info.get("description"), "topics": info.get("topics", []), "metadata_status": "ok", "metadata_error": None})
        except HTTPError as exc:
            record.update({"metadata_status": f"http_{exc.code}", "metadata_error": "GitHub API returned an HTTP error; check rate limits and access"})
            if exc.code in (403, 429):
                result.append(record)
                write_jsonl(args.output, result)
                raise RuntimeError("Rate limit or access restriction; saved partial results, stopping safely") from exc
        except URLError as exc:
            record.update({"metadata_status": "network_error", "metadata_error": type(exc.reason).__name__})
        result.append(record)
    write_jsonl(args.output, result)
    print(f"Wrote {len(result)} point-in-time metadata snapshots to {args.output}")


def summarize(args):
    rows = list(read_jsonl(args.input))
    print(json.dumps({"occurrences": len(rows), "distinct_repository_names": len({r.get("repository") for r in rows}), "note": "Distinct names are not stable repository IDs and cannot certify a study cohort"}, indent=2))


def main(argv=None):
    parser = argparse.ArgumentParser(description="GitHub Trending 1000 Study research CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    cp = sub.add_parser("capture", help="Fetch one currently observed public Trending HTML page")
    cp.add_argument("--date", required=True, help="UTC observation date (today only)")
    cp.add_argument("--window", required=True, choices=("daily", "weekly", "monthly"))
    cp.add_argument("--output", required=True)
    cp.add_argument("--manifest-output", help="Write SHA-256/UTC source manifest at capture time (required for pilot validation)")
    cp.set_defaults(func=capture)
    pp = sub.add_parser("parse-trending", help="Parse saved HTML to audit-friendly JSONL")
    pp.add_argument("--input", required=True)
    pp.add_argument("--date", required=True)
    pp.add_argument("--window", required=True, choices=("daily", "weekly", "monthly"))
    pp.add_argument("--output", required=True)
    pp.set_defaults(func=parse_trending)
    vp = sub.add_parser("pilot-parse", help="Validate one capture+manifest and parse pilot-only rows with true capture time")
    vp.add_argument("--input", required=True)
    vp.add_argument("--manifest", required=True)
    vp.add_argument("--output", required=True)
    vp.add_argument("--audit-output", help="Optional structured audit summary JSON")
    vp.set_defaults(func=pilot_parse)
    pf = sub.add_parser("pilot-preflight", help="Check documented scientific readiness without claiming authorization")
    pf.add_argument("--input", required=True)
    pf.add_argument("--stage", choices=("pilot", "confirmatory"), default="confirmatory")
    pf.add_argument("--require-ready", action="store_true", help="Fail with nonzero exit if gates are not documented as verified")
    pf.set_defaults(func=pilot_preflight)
    ep = sub.add_parser("enrich", help="Fetch current public GitHub API metadata")
    ep.add_argument("--input", required=True)
    ep.add_argument("--output", required=True)
    ep.set_defaults(func=enrich)
    sp = sub.add_parser("summarize", help="Count appearances and distinct displayed names")
    sp.add_argument("--input", required=True)
    sp.set_defaults(func=summarize)
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except (ValueError, OSError, HTTPError, URLError, RuntimeError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
