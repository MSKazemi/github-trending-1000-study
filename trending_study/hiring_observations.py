"""Offline proposed requisition observation ledger; never fetches or authorizes sources."""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, unquote, urlsplit

from .data_integrity import MAX_FILE_BYTES, ResearchJSONError, load_research_json_file
from .safe_io import ProvenanceWriteError, disjoint, publish_json
from .task_intake import IntakeError, utc

VERSION = "hiring-observations-1.0"
IDENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
STATUSES = frozenset(("listed_live", "index_only", "indexed_text_only", "inaccessible",
                      "not_listed_in_bounded_search", "removed_or_redirected",
                      "identity_conflict", "explicitly_closed"))
OBS_FIELDS = frozenset(("observation_id", "source_id", "employer_id", "requisition_id",
    "location_variant_id", "canonical_url", "observed_at_utc", "accessed_at_utc",
    "recorded_at_utc", "source_status", "http_status", "content_sha256",
    "missing_reason", "closure_evidence_ref", "posted_at_utc", "posting_date_basis",
    "relation_kind", "linkage_status", "linked_requisition_id", "link_evidence_ref"))


class HiringObservationError(ValueError):
    """The proposed offline observation contract was violated."""


def _fields(value, expected, label):
    if not isinstance(value, dict) or set(value) != set(expected):
        # Unknown keys may contain private content: do not echo them.
        raise HiringObservationError(f"{label}: unsupported or missing fields")


def _id(value, label):
    if not isinstance(value, str) or IDENT.fullmatch(value) is None:
        raise HiringObservationError(f"{label}: bounded opaque identifier required")
    return value


def _stamp(value, label):
    try:
        return utc(value)
    except IntakeError as exc:
        raise HiringObservationError(f"{label}: explicit UTC timestamp required") from exc


# RFC-style DNS labels allow interior hyphens, but not labels beginning or
# ending with '-' or empty labels. This is a lexical check, not DNS lookup or
# source permission. Undotted internal-test fixtures remain structurally valid.
_DNS_LABEL = r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?"
DNS_HOST = re.compile(rf"{_DNS_LABEL}(?:\.{_DNS_LABEL})*\Z")


def _url(value):
    if (not isinstance(value, str) or len(value) > 1500 or
            any(ord(c) < 33 for c in value) or "\\" in value):
        raise HiringObservationError("source URL: invalid bounded HTTPS URL")
    try:
        p = urlsplit(value)
        host = p.hostname
        if (p.scheme != "https" or not host or p.netloc != host or
                (len(host) > 253 or DNS_HOST.fullmatch(host) is None) or
                p.fragment or not p.path.startswith("/")):
            raise ValueError
        # This is a public-source metadata protocol, not a DNS verifier.
        # Reject literal local/metadata hosts; future automated collection
        # needs an explicit allowlist and connection-time source review.
        if (host == "localhost" or host.endswith((".localhost", ".local", ".internal"))
                or host.endswith(".")):
            raise ValueError
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            address = None
        if address is not None and not address.is_global:
            raise ValueError
        # Decode then canonicalize: percent-escaped aliases and traversal are rejected.
        if unquote(p.path) != p.path or any(x in (".", "..") for x in p.path.split("/")):
            raise ValueError
        if "//" in p.path or (p.path != "/" and p.path.endswith("/")):
            raise ValueError
        # Python 3.10 rejects parse_qsl("", strict_parsing=True); no query is
        # valid. Keep strict parsing for every nonempty query, including '&'.
        query = parse_qsl(p.query, keep_blank_values=True, strict_parsing=True) if p.query else []
        allowed = {"gh_jid", "jid", "job_id", "requisition_id"}
        if (any(k not in allowed or IDENT.fullmatch(v) is None for k, v in query)
                or len({k for k, v in query}) != len(query)
                or query != sorted(query) or p.query != "&".join(k + "=" + v for k, v in query)
                or p.geturl() != value):
            raise ValueError
        return p
    except ValueError as exc:
        raise HiringObservationError("source URL: canonical HTTPS without credentials required") from exc


def _optional_id(value, label):
    if value is not None:
        _id(value, label)


def audit(data):
    """Validate submitted events and derive histories, without authenticating observations."""
    _fields(data, {"schema_version", "dataset_kind", "declared_at_utc", "study_start_utc",
                  "study_end_utc", "analysis_as_of_utc", "sources", "observations"}, "root")
    if data["schema_version"] != VERSION or data["dataset_kind"] not in ("synthetic", "self_reported_unverified"):
        raise HiringObservationError("unsupported schema or dataset kind")
    now = datetime.now(timezone.utc)
    declared, start, end, asof = [_stamp(data[k], k) for k in (
        "declared_at_utc", "study_start_utc", "study_end_utc", "analysis_as_of_utc")]
    if not declared <= start <= asof <= now or end < start or end-start > timedelta(days=366):
        raise HiringObservationError("invalid/future prospective window or analysis range")
    sources = data["sources"]
    observations = data["observations"]
    if not isinstance(sources, list) or not 1 <= len(sources) <= 50:
        raise HiringObservationError("sources: expected 1..50 declarations")
    if not isinstance(observations, list) or not 1 <= len(observations) <= 10000:
        raise HiringObservationError("observations: expected 1..10000 attempts")
    source_map, source_urls = {}, set()
    for source in sources:
        _fields(source, {"source_id", "employer_id", "index_url", "listing_host", "access_review_status"}, "source")
        sid = _id(source["source_id"], "source_id")
        _id(source["employer_id"], "employer_id")
        _url(source["index_url"])
        if source["access_review_status"] != "pending":
            raise HiringObservationError("this proposed instrument cannot certify source approval")
        if (sid in source_map or source["index_url"] in source_urls or
                _url("https://" + str(source["listing_host"]) + "/").hostname != source["listing_host"]):
            raise HiringObservationError("duplicate/alias source or invalid listing host")
        source_map[sid] = source
        source_urls.add(source["index_url"])
    seen, attempts, url_owner, histories, source_times = set(), set(), {}, {}, {}
    previous = None
    last_informative, instant_closures = {}, {}
    for obs in observations:
        _fields(obs, OBS_FIELDS, "observation")
        oid = _id(obs["observation_id"], "observation_id")
        sid = _id(obs["source_id"], "source_id")
        employer = _id(obs["employer_id"], "employer_id")
        req = _id(obs["requisition_id"], "requisition_id")
        variant = _id(obs["location_variant_id"], "location_variant_id")
        if oid in seen or sid not in source_map or employer != source_map[sid]["employer_id"]:
            raise HiringObservationError("duplicate observation or source/employer mismatch")
        seen.add(oid)
        stamp = _stamp(obs["observed_at_utc"], "observed_at_utc")
        accessed = _stamp(obs["accessed_at_utc"], "accessed_at_utc")
        recorded = _stamp(obs["recorded_at_utc"], "recorded_at_utc")
        if (stamp != accessed or not start <= stamp <= min(end, asof) or
                not stamp <= recorded <= min(now, asof) or recorded-stamp > timedelta(minutes=5)):
            raise HiringObservationError("future/backdated observation or noncontemporaneous recording")
        if ((previous is not None and stamp < previous) or
                (sid in source_times and stamp < source_times[sid])):
            raise HiringObservationError("observations must be chronologically ordered")
        previous = source_times[sid] = stamp
        key = (employer, req)
        attempt = (key, variant, stamp)
        if attempt in attempts:
            raise HiringObservationError("duplicate requisition/location attempt at same instant")
        attempts.add(attempt)
        parsed = _url(obs["canonical_url"])
        if parsed.hostname != source_map[sid]["listing_host"]:
            raise HiringObservationError("listing URL outside declared source host")
        if obs["canonical_url"] in url_owner and url_owner[obs["canonical_url"]] != key:
            raise HiringObservationError("source URL alias conflicts with requisition identity")
        url_owner[obs["canonical_url"]] = key
        status = obs["source_status"]
        if not isinstance(status, str) or status not in STATUSES:
            raise HiringObservationError("unsupported observed source status; disappearance is not filled")
        http = obs["http_status"]
        if http is not None and (type(http) is not int or not 100 <= http <= 599):
            raise HiringObservationError("http_status: integer 100..599 or null required")
        digest = obs["content_sha256"]
        if digest is not None and (not isinstance(digest, str) or SHA.fullmatch(digest) is None):
            raise HiringObservationError("content_sha256: invalid digest")
        missing = obs["missing_reason"]
        if status in ("listed_live", "explicitly_closed"):
            if http != 200 or digest is None or missing is not None:
                raise HiringObservationError("verified-shape live/closed observation needs 200/digest, no missing reason")
        elif missing != {"inaccessible": "content_unavailable", "index_only": "index_only",
                         "indexed_text_only": "index_only", "not_listed_in_bounded_search": "search_miss",
                         "removed_or_redirected": "redirect", "identity_conflict": "identity_unresolved"}[status]:
            raise HiringObservationError("missing observation requires explicit reason, never zero")
        if status == "inaccessible" and http == 200:
            raise HiringObservationError("inaccessible observation contradicts HTTP 200")
        _optional_id(obs["closure_evidence_ref"], "closure_evidence_ref")
        if (status == "explicitly_closed") != (obs["closure_evidence_ref"] is not None):
            raise HiringObservationError("closure requires explicit employer evidence only")
        if obs["posted_at_utc"] is None:
            if obs["posting_date_basis"] != "unknown":
                raise HiringObservationError("unknown posting date needs explicit unknown basis")
        elif (obs["posting_date_basis"] != "explicit_employer" or
                _stamp(obs["posted_at_utc"], "posted_at_utc") > stamp):
            raise HiringObservationError("posting date cannot replace actual observation time")
        relation, linkage = obs["relation_kind"], obs["linkage_status"]
        linked = obs["linked_requisition_id"]
        evidence = obs["link_evidence_ref"]
        _optional_id(linked, "linked_requisition_id")
        _optional_id(evidence, "link_evidence_ref")
        if relation == "none":
            if linkage != "none" or linked is not None or evidence is not None:
                raise HiringObservationError("unexpected linkage on unrelated observation")
        elif relation in ("reopening", "reposting"):
            if (linkage not in ("known", "unconfirmed") or linked is None or
                    ((linkage == "known") != (evidence is not None))):
                raise HiringObservationError("linkage requires known evidence or explicit uncertainty")
            prior = histories.get((employer, linked), [])
            if not prior or _stamp(prior[0]["observed_at_utc"], "prior") >= stamp:
                raise HiringObservationError("linkage must reference a previously observed employer requisition")
            if ((relation == "reposting" and linked == req) or
                    (relation == "reopening" and (linked != req or status != "listed_live" or
                     last_informative.get(key) != "explicitly_closed"))):
                raise HiringObservationError("reopening/reposting identity or status mismatch")
        else:
            raise HiringObservationError("unsupported relationship")
        prior = histories.get(key, [])
        if (status == "listed_live" and key in last_informative and
                last_informative[key] == "explicitly_closed" and relation != "reopening"):
            raise HiringObservationError("live return after explicit closure needs reopening record")
        instant_key = (key, stamp)
        is_closed = status == "explicitly_closed"
        if status in ("listed_live", "explicitly_closed"):
            if instant_key in instant_closures and instant_closures[instant_key] != is_closed:
                raise HiringObservationError("simultaneous location observations contradict requisition closure")
            instant_closures[instant_key] = is_closed
            last_informative[key] = status
        histories.setdefault(key, []).append(dict(obs))
    requisitions = []
    for (employer, req), rows in sorted(histories.items()):
        live = [r for r in rows if r["source_status"] == "listed_live"]
        informative = [r for r in rows if r["source_status"] in ("listed_live", "explicitly_closed")]
        closed = bool(informative and informative[-1]["source_status"] == "explicitly_closed")
        # A disappearance or 404 is NOT a closure event. Even when an
        # employer explicitly marks a requisition closed, its actual closure
        # timestamp remains unknown. Report at most the observed interval:
        # last definitely listed before this closure, first explicitly closed.
        closure_lower = closure_upper = None
        if closed:
            final_closed_at = _stamp(informative[-1]["observed_at_utc"], "closure")
            earlier_live = [
                r for r in informative
                if r["source_status"] == "listed_live"
                and _stamp(r["observed_at_utc"], "listed") < final_closed_at
            ]
            if earlier_live:
                closure_lower = earlier_live[-1]["observed_at_utc"]
            prior = (_stamp(closure_lower, "closure_lower")
                     if closure_lower is not None else None)
            closure_upper = next(
                r["observed_at_utc"] for r in informative
                if r["source_status"] == "explicitly_closed"
                and (prior is None or
                     _stamp(r["observed_at_utc"], "explicitly_closed") > prior)
            )
        variant_states, revisions = {}, 0
        for row in rows:
            variant = row["location_variant_id"]
            state = (row["source_status"], row["content_sha256"])
            if variant in variant_states and variant_states[variant] != state:
                revisions += 1
            variant_states[variant] = state
        requisitions.append({
            "employer_id": employer, "requisition_id": req,
            "location_variant_ids": sorted({r["location_variant_id"] for r in rows}),
            "first_observed_at_utc": rows[0]["observed_at_utc"],
            "last_observed_at_utc": rows[-1]["observed_at_utc"],
            "first_listed_observation_at_utc": live[0]["observed_at_utc"] if live else None,
            "last_listed_observation_at_utc": live[-1]["observed_at_utc"] if live else None,
            "observation_attempts": len(rows),
            "missing_attempts": sum(r["missing_reason"] is not None for r in rows),
            "last_observed_source_status": rows[-1]["source_status"],
            "right_censored": (not bool(closed)) if informative else None,
            "censoring_at_utc": informative[-1]["observed_at_utc"] if informative and not closed else None,
            "observation_window_end_utc": min(end, asof).isoformat(),
            "actual_closure_at_utc": None, "filled_positions": None,
            "closure_interval_last_listed_at_utc": closure_lower,
            "closure_interval_first_explicitly_closed_at_utc": closure_upper,
            "status_or_content_revision_count": revisions,
            "observations": rows,
        })
    digest = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    by_source = []
    for sid in sorted(source_map):
        source_rows = [r for r in observations if r["source_id"] == sid]
        by_source.append({"source_id": sid, "employer_id": source_map[sid]["employer_id"],
                          "observation_attempts": len(source_rows),
                          "missing_attempts": sum(r["missing_reason"] is not None for r in source_rows)})
    return {"schema_version": VERSION, "dataset_kind": data["dataset_kind"], "input_sha256": digest,
            "by_source": by_source,
            "observation_attempts": len(observations), "unique_requisition_keys": len(requisitions),
            "missing_attempts": sum(r["missing_attempts"] for r in requisitions),
            "requisitions": requisitions, "independent_verification": False,
            "source_access_approved": False, "human_methods_approved": False,
            "eligible_for_confirmatory_cohort": False,
            "interpretation": "Self-reported source changes only; no filled-job, hiring-rate, headcount or causal inference."}


def load(path, max_bytes=MAX_FILE_BYTES):
    """Read input through the shared bounded strict research JSON reader.

    ``load_research_json_file`` refuses leaf symlinks, FIFOs and other
    nonregular files, checks the opened descriptor and actual bytes read, and
    rejects duplicate keys, NaN/Infinity and numeric overflow. Its diagnostics
    are generic and never contain user-supplied keys or paths.
    """
    try:
        return load_research_json_file(path, max_bytes=max_bytes)
    except ResearchJSONError as exc:
        raise HiringObservationError(f"hiring observation input: {exc}") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        disjoint(args.input, args.output)
        result = audit(load(args.input))
        publish_json(args.output, result)
    except (OSError, ProvenanceWriteError):
        # Neither local/CI absolute paths nor private file names are useful to
        # validate submitted observations. Suppress low-level exception text.
        parser.error("input/output filesystem operation failed; path details withheld")
    except (ValueError, RecursionError) as exc:
        parser.error(str(exc))
    print(json.dumps({"output": str(args.output), "observation_attempts": result["observation_attempts"],
                      "scientific_acceptance": False}, sort_keys=True))


if __name__ == "__main__":
    main()
