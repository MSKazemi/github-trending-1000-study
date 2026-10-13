"""Offline pre-install supply-chain evidence gate; never downloads/installs code.

All provenance, licence and security statuses are *supplied* and unverified.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlparse, unquote

FIELDS = ("registry_identity", "license_compatibility", "known_advisories",
          "release_provenance", "functional_fit", "maintenance_suitability")
STATES = {"pass", "fail", "unknown"}
_SHA = re.compile(r"^[0-9a-f]{64}$")


class PackageReviewError(ValueError):
    pass


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


def evaluate(data):
    if not isinstance(data, dict):
        raise PackageReviewError("expected object")
    candidate = data.get("candidate")
    if not isinstance(candidate, dict):
        raise PackageReviewError("candidate object required")
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
    if spdx is not None and (not isinstance(spdx, str) or not spdx.strip()):
        raise PackageReviewError("spdx_expression must be nonempty text or null if unknown")
    url = candidate.get("registry_url")
    if not isinstance(url, str):
        raise PackageReviewError("registry_url required")
    parsed = urlparse(url)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username is not None
            or parsed.password is not None or parsed.fragment or parsed.query):
        raise PackageReviewError("registry_url must be clean HTTPS without credentials/query/fragment")
    is_pypi = candidate["ecosystem"].casefold() == "pypi"
    if is_pypi:
        if re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?", candidate["package_name"]) is None:
            raise PackageReviewError("PyPI package_name must contain valid registry-name characters")
        parts = [unquote(p) for p in parsed.path.strip("/").split("/")]
        if (parsed.hostname != "pypi.org" or parsed.port not in (None, 443)
                or len(parts) != 3 or parts[0] != "project"
                or parts[1].casefold().replace("_", "-").replace(".", "-") !=
                   candidate["package_name"].casefold().replace("_", "-").replace(".", "-")
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
        normalize = lambda name: re.sub(r"[-_.]+", "-", name.casefold())
        if (normalize(from_purl.group(1)) != normalize(candidate["package_name"])
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
        if (not isinstance(cell, dict) or not isinstance(cell.get("status"), str)
                or cell["status"] not in STATES):
            raise PackageReviewError(f"{key} must declare pass/fail/unknown")
        if cell["status"] == "pass":
            source = cell.get("evidence_url")
            if not isinstance(source, str):
                raise PackageReviewError(f"{key} pass requires HTTPS evidence_url")
            evidence = urlparse(source)
            if (evidence.scheme != "https" or not evidence.hostname
                    or evidence.username is not None or evidence.password is not None
                    or evidence.fragment):
                raise PackageReviewError(f"{key} pass requires clean HTTPS evidence_url")
            if key == "license_compatibility" and (
                    not spdx or spdx.strip().upper() in {"NONE", "NOASSERTION"}):
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
