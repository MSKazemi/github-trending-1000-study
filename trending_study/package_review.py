"""Offline pre-install supply-chain evidence gate; never downloads/installs code.

All provenance, licence and security statuses are *supplied* and unverified.
"""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re
from urllib.parse import urlparse

FIELDS = ("registry_identity", "license_compatibility", "known_advisories",
          "release_provenance", "functional_fit", "maintenance_suitability")
STATES = {"pass", "fail", "unknown"}
_SHA = re.compile(r"^[0-9a-f]{64}$")


class PackageReviewError(ValueError):
    pass


def _date(raw):
    if not isinstance(raw, str):
        raise PackageReviewError("UTC timestamp required")
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PackageReviewError("invalid timestamp") from exc
    if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
        raise PackageReviewError("timestamps require explicit UTC")
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
    spdx = candidate.get("spdx_expression")
    if spdx is not None and (not isinstance(spdx, str) or not spdx.strip()):
        raise PackageReviewError("spdx_expression must be nonempty text or null if unknown")
    url = candidate.get("registry_url")
    if not isinstance(url, str):
        raise PackageReviewError("registry_url required")
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username is not None:
        raise PackageReviewError("registry_url must be HTTPS and without embedded credentials")
    sha = candidate.get("artifact_sha256")
    if not isinstance(sha, str) or not _SHA.fullmatch(sha):
        raise PackageReviewError("exact artifact SHA-256 digest required")
    frozen = _date(data.get("task_frozen_at_utc"))
    release = _date(candidate.get("first_available_at_utc"))
    if release > frozen:
        return {"decision": "reject", "reason": "component released after frozen task",
                "failed_checks": ["temporal_availability"], "unknown_checks": [],
                "automatic_install_approved": False, "source_checks_self_declared": True}
    checks = data.get("checks")
    if not isinstance(checks, dict) or set(checks) != set(FIELDS):
        raise PackageReviewError("must declare every evidence check including unknowns")
    failed, unknown = [], []
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
            if evidence.scheme != "https" or not evidence.netloc or evidence.username is not None:
                raise PackageReviewError(f"{key} pass requires valid HTTPS evidence_url")
            if key == "license_compatibility" and not spdx:
                raise PackageReviewError("license pass requires a declared SPDX expression")
        if cell["status"] == "fail":
            failed.append(key)
        elif cell["status"] == "unknown":
            unknown.append(key)
    if failed:
        decision, reason = "reject", "one or more declared gates failed"
    elif unknown:
        decision, reason = "defer", "unknown evidence requires independent review"
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
