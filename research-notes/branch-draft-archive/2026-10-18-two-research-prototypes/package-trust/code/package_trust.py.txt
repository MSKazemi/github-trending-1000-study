"""Offline assertions for proposed package reuse. Never execute or trust the candidate."""
import argparse
import json
from pathlib import Path
from datetime import datetime
import re

SHA = re.compile(r"^[a-f0-9]{40}$")
GATES = ("identity", "license", "security", "provenance", "maintenance", "functional")
STATES = {"pass", "fail", "unknown"}


class PackageTrustError(ValueError):
    pass


def evaluate(payload):
    if not isinstance(payload, dict) or payload.get("schema_version") != "1.0":
        raise PackageTrustError("expected schema_version 1.0")
    if payload.get("dataset_kind") not in {"synthetic", "self_reported"}:
        raise PackageTrustError("dataset_kind must be synthetic or self_reported")
    candidates = payload.get("candidates")
    if not isinstance(candidates, list):
        raise PackageTrustError("candidates must be list")
    output, seen = [], set()
    for c in candidates:
        if not isinstance(c, dict):
            raise PackageTrustError("candidate must be object")
        for key in ("purl", "version", "ecosystem", "registry_url", "release_url", "source_commit", "captured_at_utc"):
            if not isinstance(c.get(key), str) or not c[key].strip():
                raise PackageTrustError(f"{key} required")
        if not c["purl"].startswith("pkg:") or "@"+c["version"] not in c["purl"]:
            raise PackageTrustError("purl must contain exact version")
        if c["purl"] in seen:
            raise PackageTrustError("duplicate candidate purl")
        seen.add(c["purl"])
        for link in ("registry_url", "release_url"):
            if not c[link].startswith("https://"):
                raise PackageTrustError(f"{link} must use https")
        if not SHA.fullmatch(c["source_commit"]):
            raise PackageTrustError("source commit must be pinned full hex SHA")
        try:
            ts = datetime.fromisoformat(c["captured_at_utc"].replace("Z", "+00:00"))
            if not c["captured_at_utc"].endswith("Z") or ts.utcoffset().total_seconds() != 0:
                raise ValueError("not UTC")
        except (ValueError, AttributeError) as exc:
            raise PackageTrustError("captured_at_utc must be ISO UTC") from exc
        gates, evidence = c.get("gates"), c.get("evidence")
        if not isinstance(gates, dict) or set(gates) != set(GATES) or any(x not in STATES for x in gates.values()):
            raise PackageTrustError("all six gates require pass/fail/unknown")
        if not isinstance(evidence, dict):
            raise PackageTrustError("evidence must be an object")
        for k in GATES:
            if gates[k] == "pass" and (not isinstance(evidence.get(k), str) or not evidence[k].startswith("https://")):
                raise PackageTrustError(f"self-reported passing {k} needs evidence URL")
        decision = ("block_candidate" if "fail" in gates.values() else
                    "review_required" if "unknown" in gates.values() else
                    "ready_for_independent_review")
        output.append({"purl": c["purl"], "decision": decision,
                       "unresolved_gates": [k for k in GATES if gates[k] == "unknown"],
                       "failed_gates": [k for k in GATES if gates[k] == "fail"]})
    return {"schema_version": "1.0", "candidates": output, "auto_install_allowed": False,
            "independently_verified": False, "disclaimer":
            "Evidence URLs and gate labels are SELF-REPORTED and NOT fetched, authenticated or security certified."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    args = p.parse_args(argv)
    try:
        out = evaluate(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (PackageTrustError, OSError, ValueError) as exc:
        p.exit(2, f"error: {exc}\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
