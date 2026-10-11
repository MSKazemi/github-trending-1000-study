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

VERSION = "0.1.0"
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
    if args.date != datetime.now(timezone.utc).date().isoformat():
        raise ValueError("Capture date must be today's UTC date; historic Trending pages cannot be backfilled")
    url = f"{GITHUB_HOST}/trending?since={args.window}"
    request = Request(url, headers={"User-Agent": "github-trending-1000-study-research/0.1 (+https://github.com/MSKazemi/github-trending-1000-study)", "Accept": "text/html"})
    with urlopen(request, timeout=25) as response:
        raw = response.read(4_000_001)
        if len(raw) > 4_000_000:
            raise ValueError("HTML response exceeds 4MB safety limit")
    if not raw:
        raise ValueError("Empty response")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_bytes(raw)
    print(json.dumps({"source_url": url, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "captured_at_utc": utc_now(), "path": args.output}))


def parse_trending(args):
    raw = Path(args.input).read_bytes()
    repos = extract_repos(raw.decode("utf-8"))
    # A locally stored capture may come from a past date; state only supplied metadata, never assert validated source date.
    rows = []
    now = utc_now()
    url = f"{GITHUB_HOST}/trending?since={args.window}"
    for rank, repository in enumerate(repos, 1):
        rows.append({"schema_version": "0.1", "repository": repository, "trending_url": url, "source_file": str(args.input), "source_sha256": hashlib.sha256(raw).hexdigest(), "collected_at_utc": now, "observation_date": args.date, "window": args.window, "rank": rank, "parser_version": VERSION, "language_filter": None})
    write_jsonl(args.output, rows)
    print(f"Wrote {len(rows)} occurrences (not unique study sample) to {args.output}")


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
    cp.set_defaults(func=capture)
    pp = sub.add_parser("parse-trending", help="Parse saved HTML to audit-friendly JSONL")
    pp.add_argument("--input", required=True)
    pp.add_argument("--date", required=True)
    pp.add_argument("--window", required=True, choices=("daily", "weekly", "monthly"))
    pp.add_argument("--output", required=True)
    pp.set_defaults(func=parse_trending)
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
