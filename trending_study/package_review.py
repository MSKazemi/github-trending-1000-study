"""Offline pre-install supply-chain evidence gate; never downloads/installs code.

All provenance, licence and security statuses are *supplied* and unverified.
"""
import argparse
import ipaddress
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlparse

from .data_integrity import MAX_FILE_BYTES, ResearchJSONError, load_research_json_file

FIELDS = ("registry_identity", "license_compatibility", "known_advisories",
          "release_provenance", "functional_fit", "maintenance_suitability")
STATES = {"pass", "fail", "unknown"}
_SHA = re.compile(r"^[0-9a-f]{64}$")


class PackageReviewError(ValueError):
    pass


def _normalize_pypi_name(name):
    return re.sub(r"[-_.]+", "-", name.casefold())


def _date(raw, *, allow_future=False):
    if not isinstance(raw, str):
        raise PackageReviewError("UTC timestamp required")
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PackageReviewError("invalid timestamp") from exc
    if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
        raise PackageReviewError("timestamps require explicit UTC")
    if not allow_future and dt > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise PackageReviewError("timestamps cannot be future-dated")
    return dt

def _clean_https_url(url, field):
    """Reject ambiguous origins, malformed ports and hidden URL parameters.

    This only establishes a structurally clean URL; it does NOT authenticate
    a publisher, registry, license statement or an evidence artifact.
    """
    if (not isinstance(url, str) or not url or url != url.strip()
            or "\\" in url
            or any(ord(char) <= 32 or ord(char) == 127 for char in url)):
        raise PackageReviewError(f"{field} requires clean HTTPS URL without whitespace")
    try:
        parsed = urlparse(url)
        # Access .port to force validation of malformed/out-of-range port syntax.
        port = parsed.port
    except ValueError as exc:
        raise PackageReviewError(f"{field} has malformed HTTPS authority") from exc
    if port == 0:
        raise PackageReviewError(f"{field} has malformed HTTPS authority (port 0)")
    if (parsed.scheme != "https" or not parsed.hostname or parsed.netloc.endswith(":")
            or parsed.username is not None or parsed.password is not None
            or parsed.params or parsed.query or parsed.fragment):
        raise PackageReviewError(
            f"{field} requires clean HTTPS URL without credentials/parameters/query/fragment"
        )
    # Public evidence must not silently point reviewers or a future verifier at
    # a loopback, private or cloud-metadata endpoint. This is format-only:
    # DNS-based hosts are NOT resolved, allowlisted or safe to auto-fetch.
    host = parsed.hostname
    if (not host.isascii() or "%" in parsed.netloc or host.endswith(".")
            or host in ("localhost", "metadata.google.internal")
            or host.endswith((".localhost", ".local", ".internal"))):
        raise PackageReviewError(f"{field} requires a public evidence host")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None  # A domain, not a proof of public DNS resolution.
    if address is not None and not address.is_global:
        raise PackageReviewError(f"{field} requires a public evidence host")
    # libc / legacy URL clients can interpret 127.1, 2130706433,
    # 0x7f000001 or 0177.0.0.1 as IPv4 addresses even though
    # ipaddress.ip_address rejects these spellings. They are not
    # trustworthy DNS names for a reviewer-facing evidence ledger.
    ipv4_piece = r"(?:0[xX][0-9A-Fa-f]+|0[0-7]+|[0-9]+)"
    if (address is None and
            re.fullmatch(ipv4_piece + r"(?:\\." + ipv4_piece + r"){0,3}", host)):
        raise PackageReviewError(f"{field} requires a canonical public evidence host")
    return parsed


def evaluate(data):
    if not isinstance(data, dict) or set(data) != {"candidate", "task_frozen_at_utc", "checks"}:
        raise PackageReviewError("expected exact package review fields; unknown fields forbidden")
    candidate = data.get("candidate")
    allowed_candidate = {"ecosystem", "package_name", "version", "registry_url",
                         "artifact_sha256", "first_available_at_utc", "spdx_expression",
                         "purl", "source_commit"}
    if not isinstance(candidate, dict) or set(candidate) - allowed_candidate:
        raise PackageReviewError("candidate must be an object without unsupported/private fields")
    for key in ("ecosystem", "package_name", "version"):
        if not isinstance(candidate.get(key), str) or not candidate[key].strip():
            raise PackageReviewError(f"candidate.{key} required")
    version = candidate["version"]
    # A pinned version must be a single release identifier, not a selector.
    # Do not put escaped "\\t" / "\\n" in a character set: this would reject
    # legitimate release names containing the letters t and n.
    if (version.casefold() in {"latest", "head", "main", "master", "stable", "*"}
            or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+!-]{0,127}", version) is None):
        raise PackageReviewError("candidate.version must be a pinned exact release")
    spdx = candidate.get("spdx_expression")
    if spdx is not None and (
            not isinstance(spdx, str) or not spdx.strip() or len(spdx) > 512
            or any((ord(ch) < 32 and ch != " ") or ord(ch) == 127 for ch in spdx)):
        raise PackageReviewError("spdx_expression must be bounded single-line text or null")
    parsed = _clean_https_url(candidate.get("registry_url"), "registry_url")
    is_pypi = candidate["ecosystem"].casefold() == "pypi"
    if is_pypi:
        if re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?", candidate["package_name"]) is None:
            raise PackageReviewError("PyPI package_name must contain valid registry-name characters")
        # Accept only literal ASCII path segments. Percent-escaped UTF-8 can
        # casefold to an unrelated ASCII package name (e.g. long-s to "s"),
        # so decoded-name equality alone is not safe identity binding.
        if not parsed.path.isascii() or "%" in parsed.path:
            raise PackageReviewError("PyPI registry URL requires literal ASCII path segments")
        parts = parsed.path.strip("/").split("/")
        if (parsed.hostname != "pypi.org" or parsed.port not in (None, 443)
                or len(parts) != 3 or parts[0] != "project"
                or _normalize_pypi_name(parts[1]) !=
                   _normalize_pypi_name(candidate["package_name"])
                or parts[2] != candidate["version"]):
            raise PackageReviewError("PyPI registry URL must match official host, exact name and version")
    # Optional Package URL and source commit (ported from superseded #186).
    # These are structural identity assertions, never registry authentication.
    purl = candidate.get("purl")
    if purl is not None:
        if not isinstance(purl, str) or not is_pypi:
            raise PackageReviewError("purl syntax binding is implemented for PyPI only")
        from_purl = re.fullmatch(r"pkg:pypi/([A-Za-z0-9._-]+)@([A-Za-z0-9][A-Za-z0-9._+!-]{0,127})", purl)
        if not from_purl:
            raise PackageReviewError("purl must be exact pkg:pypi/name@version")
        if (_normalize_pypi_name(from_purl.group(1)) !=
                _normalize_pypi_name(candidate["package_name"])
                or from_purl.group(2) != candidate["version"]):
            raise PackageReviewError("purl conflicts with pinned PyPI identity/version")
    source_commit = candidate.get("source_commit")
    if source_commit is not None and (
            not isinstance(source_commit, str)
            or re.fullmatch(r"[0-9a-f]{40}", source_commit) is None):
        raise PackageReviewError("source_commit must be a pinned lowercase full Git SHA or null")
    if "artifact_sha256" not in candidate:
        raise PackageReviewError("artifact_sha256 must be explicitly known or null (unknown)")
    sha = candidate["artifact_sha256"]
    if sha is not None and (not isinstance(sha, str) or not _SHA.fullmatch(sha)):
        raise PackageReviewError("artifact_sha256 must be a lowercase SHA-256 digest or null")
    frozen = _date(data.get("task_frozen_at_utc"))
    release = _date(candidate.get("first_available_at_utc"), allow_future=True)
    # Validate every input gate even for a temporally ineligible component:
    # do not let an early return mask malformed or omitted review evidence.
    temporally_ineligible = release > frozen
    checks = data.get("checks")
    if not isinstance(checks, dict) or set(checks) != set(FIELDS):
        raise PackageReviewError("must declare every evidence check including unknowns")
    # An unresolved release artifact is not a failed package and must never
    # become "review_ready" solely through self-declared six passing checks.
    failed, unknown = (["temporal_availability"] if temporally_ineligible else []), (
        ["artifact_sha256"] if sha is None else [])
    for key in FIELDS:
        cell = checks[key]
        if (not isinstance(cell, dict) or set(cell) - {"status", "evidence_url"}
                or not isinstance(cell.get("status"), str)
                or cell["status"] not in STATES):
            raise PackageReviewError(f"{key} must declare pass/fail/unknown without unknown fields")
        # A failing/unknown gate can carry a corroborating source, but its URL
        # must not hide a credential or arbitrary URL payload either. Absent or
        # null means the source is unknown, which only a pass cannot accept.
        if cell.get("evidence_url") is not None:
            _clean_https_url(cell["evidence_url"], f"{key} evidence_url")
        elif cell["status"] == "pass":
            raise PackageReviewError(f"{key} pass requires an evidence_url")
        if cell["status"] == "pass":
            if key == "license_compatibility" and (
                    not spdx or re.search(
                        r"(?<![A-Za-z0-9_.-])(?:NONE|NOASSERTION)(?![A-Za-z0-9_.-])",
                        spdx, re.I)):
                # SPDX 3.0.1 forbids NONE/NOASSERTION in compound license
                # expressions. A sentinel anywhere is not a license grant.
                raise PackageReviewError("license pass requires an actual SPDX license expression, not NONE/NOASSERTION")
        if cell["status"] == "fail":
            failed.append(key)
        elif cell["status"] == "unknown":
            unknown.append(key)
    # Official host/name/version matching is only implemented for PyPI;
    # unbound ecosystems cannot be marked review_ready on asserted claims.
    if not is_pypi:
        unknown.append("official_registry_identity_binding")
    if failed:
        decision, reason = "reject", "temporal unavailability or declared gate failure"
    elif unknown:
        decision, reason = "defer", "unknown or unsupported identity evidence requires review"
    else:
        decision, reason = "review_ready", "self-declared checks need independent verification"
    return {"decision": decision, "reason": reason, "failed_checks": failed,
            "unknown_checks": unknown, "automatic_install_approved": False,
            "source_checks_self_declared": True}


def evaluate_file(path):
    """Read one bounded regular artifact via the shared strict research reader."""
    try:
        data = load_research_json_file(path, max_bytes=MAX_FILE_BYTES)
    except ResearchJSONError as exc:
        if str(exc) == "invalid or ambiguous JSON input":
            # The shared reader already hides duplicate keys, nesting-limit
            # context and filenames; keep this tool's established diagnostic.
            raise PackageReviewError(
                "input must be strict UTF-8 JSON without duplicate keys or invalid numbers"
            ) from None
        # Remaining shared-reader messages are fixed and contain no path.
        raise PackageReviewError(str(exc)) from exc
    return evaluate(data)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = evaluate_file(args.input)
    except (OSError, ValueError, RecursionError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
