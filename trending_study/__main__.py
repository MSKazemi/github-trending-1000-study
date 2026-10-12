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

from .pilot import (build_capture_manifest, evaluate_preflight, validate_capture)
from .safe_io import (disjoint, refuse_existing, publish_once, publish_json,
                      publish_jsonl, jsonl_bytes)
from .page_audit import audit_bundle_file

VERSION = "0.4.0"
GITHUB_HOST = "https://github.com"
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def valid_repo(name):
    """Reject noncanonical path segments even if they match the character regex."""
    return (isinstance(name, str) and bool(REPO.fullmatch(name))
            and all(part not in (".", "..") for part in name.split("/")))


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class TrendingParser(HTMLParser):
    """Check that EVERY supported article.Box-row has exactly one repo heading.

    A positive subset is never considered a successful parse when a supported
    article is malformed. This is structural self-consistency, NOT an independent
    audit of GitHub's live or changing page layout.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.h2_depth = 0
        self.article_rows = 0
        self.heading_count = 0
        self.header_links = []
        self.repos = []
        self.errors = []
        self._seen = set()

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "article":
            if self.article_depth:
                self.article_depth += 1
                self.errors.append(f"nested article inside Box-row #{self.article_rows}")
                return
            if "Box-row" in attr.get("class", "").split():
                self.article_depth = 1
                self.article_rows += 1
                self.heading_count = 0
                self.header_links = []
                self.h2_depth = 0
                return
        if not self.article_depth:
            return
        if tag == "h2":
            self.h2_depth += 1
            self.heading_count += 1
        elif tag == "a" and self.h2_depth:
            self.header_links.append(attr.get("href", ""))

    def handle_endtag(self, tag):
        if not self.article_depth:
            return
        if tag == "h2":
            if not self.h2_depth:
                self.errors.append(f"unmatched h2 in Box-row #{self.article_rows}")
            else:
                self.h2_depth -= 1
        elif tag == "article":
            self.article_depth -= 1
            if not self.article_depth:
                self._finalize_row()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def _finalize_row(self):
        row = self.article_rows
        if self.h2_depth or self.heading_count != 1 or len(self.header_links) != 1:
            self.errors.append(
                f"Box-row #{row} has {self.heading_count} h2 and "
                f"{len(self.header_links)} header links (expected exactly one of each)"
            )
            return
        href = self.header_links[0].strip()
        name = href.strip("/") if href.startswith("/") else ""
        if not href.startswith("/") or not valid_repo(name):
            self.errors.append(f"Box-row #{row} has unsupported or malformed repository link")
            return
        key = name.casefold()
        if key in self._seen:
            self.errors.append(f"duplicate repository in supported Box-row #{row}")
            return
        self._seen.add(key)
        self.repos.append(name)

    def check(self):
        if self.article_depth:
            self.errors.append("HTML ended with an unclosed Box-row article")
        if not self.article_rows:
            raise ValueError("No supported Trending article.Box-row elements found")
        if self.errors or len(self.repos) != self.article_rows:
            details = "; ".join(self.errors[:4]) or "row-count inconsistency"
            raise ValueError(
                f"Trending structural completeness failed: "
                f"{len(self.repos)}/{self.article_rows} valid Box-row entries; {details}"
            )


def _parse_supported_trending_layout(html):
    parser = TrendingParser()
    parser.feed(html)
    parser.close()
    parser.check()
    return parser


def inspect_trending_structure(html):
    """Internal selector coverage only, NOT human-confirmed live-page recall."""
    p = _parse_supported_trending_layout(html)
    return {
        "selector_box_row_count": p.article_rows,
        "extracted_repository_count": len(p.repos),
        "structural_parser_status": "matched_selector_rows_consistent",
        "limitation": "Off-selector rows and upstream layout changes still need independent page QA.",
    }


def extract_repos(html):
    """One repo per supported article; fail closed on duplicates or partial rows."""
    return _parse_supported_trending_layout(html).repos


def write_jsonl(path, rows):
    """Write a *new* complete JSONL artifact; never replace research records."""
    publish_jsonl(path, rows)


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
    # Reject repeated capture filenames and path aliases *before* network access.
    disjoint(args.output, args.manifest_output)
    refuse_existing(args.output, args.manifest_output)
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
    artifacts = [(args.output, raw)]
    if args.manifest_output:
        artifacts.append((
            args.manifest_output,
            (json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
        ))
    publish_once(artifacts)
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
    disjoint(args.input, args.output)
    refuse_existing(args.output)
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
    disjoint(args.input, args.manifest, args.output, args.audit_output)
    refuse_existing(args.output, args.audit_output)
    raw = Path(args.input).read_bytes()
    manifest_raw = Path(args.manifest).read_bytes()
    manifest = json.loads(manifest_raw.decode("utf-8"))
    rows, audit = validate_capture(
        raw, manifest, extract_repos=extract_repos,
        inspect_structure=inspect_trending_structure,
    )
    manifest_hash = hashlib.sha256(manifest_raw).hexdigest()
    for row in rows:
        row["source_file"] = str(args.input)
        row["source_manifest"] = str(args.manifest)
        row["source_manifest_sha256"] = manifest_hash
        row["parser_version"] = VERSION
    audit["source_manifest_sha256"] = manifest_hash
    artifacts = [(args.output, jsonl_bytes(rows))]
    if args.audit_output:
        artifacts.append((
            args.audit_output,
            (json.dumps(audit, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
        ))
    publish_once(artifacts)
    print(json.dumps(audit, sort_keys=True))

def audit_pages(args):
    """Compare two independently annotated visible row lists with raw captures.

    This reports documentary consistency, not proof of human independence,
    GitHub origin, permissible scraping or approval for cohort enrollment.
    """
    disjoint(args.bundle, args.output)
    refuse_existing(args.output)
    report = audit_bundle_file(args.bundle, extract_repos=extract_repos,
                               min_rows=args.min_rows)
    publish_json(args.output, report)
    print(json.dumps({
        "audit_output": args.output,
        "evidence_kind": report["evidence_kind"],
        "pages": report["pages_supplied"],
        "agreed_gold_rows": report["audited_gold_rows"],
        "automated_documentary_check": report["automated_documentary_check"],
        "scientific_status": report["scientific_status"],
        "eligible_for_confirmatory_cohort": False,
    }, sort_keys=True))
    if args.require_consistent and report["automated_documentary_check"] != "pass":
        raise ValueError("Independent page QA is incomplete or inconsistent; "
                         "report retained, cohort enrollment remains blocked.")


def pilot_preflight(args):
    """Document gate completeness; never call it a signed or approved study."""
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    summary = evaluate_preflight(data, stage=args.stage)
    print(json.dumps(summary, sort_keys=True, indent=2))
    if args.require_ready and summary["decision"] != "ready_for_human_review":
        raise RuntimeError("Pilot/confirmatory prerequisites are not complete. Human signoff is still required.")


def enrich(args):
    disjoint(args.input, args.output)
    refuse_existing(args.output)
    token = os.environ.get("GITHUB_TOKEN", "")
    result = []
    for row in read_jsonl(args.input):
        name = row.get("repository", "")
        if not valid_repo(name):
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
    qa = sub.add_parser("audit-pages", help="Compare raw captures to two complete, blinded independent row annotations")
    qa.add_argument("--bundle", required=True, help="Local audit bundle index with capture/manifest paths and both reviewer labels")
    qa.add_argument("--output", required=True, help="Write-once JSON audit report")
    qa.add_argument("--min-rows", type=int, default=30, help="Documentary full-page row threshold (default: 30 across windows)")
    qa.add_argument("--require-consistent", action="store_true", help="Return nonzero for incomplete/mismatched annotations or parser outputs")
    qa.set_defaults(func=audit_pages)
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
