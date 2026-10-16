"""Offline, source-bounded crates.io index pilot for issue #15.

This is a package NAME sampling frame, not a verified repository or task
cohort. The code NEVER retrieves, imports, installs or executes packages.
No claim of human authentication, registry completeness outside declared
directory slices, historical availability, or population prevalence follows.
"""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import re

from .data_integrity import ResearchJSONError, load_research_json_file
from .safe_io import publish_json

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
# Cargo releases use concrete X.Y.Z semantic versions; range selectors,
# moving tags, whitespace and semver operators cannot be cited as a pinned
# historical artifact. This syntactic check never proves release availability.
# SemVer core numbers must not have leading zeroes. Prerelease numeric
# identifiers have the same restriction; build identifiers may contain zeroes.
_SEMVER_NUMBER = r"(?:0|[1-9][0-9]*)"
CARGO_RELEASE = re.compile(
    _SEMVER_NUMBER + r"\." + _SEMVER_NUMBER + r"\." + _SEMVER_NUMBER +
    r"(?:-[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*)?"
    r"(?:\+[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*)?\Z"
)
NAME = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
IDENT = re.compile(r"^[A-Za-z0-9_-]{1,80}$")
INDEX = "rust-lang/crates.io-index"
SOURCE_KIND = "bounded_public_registry_index_listing"
POLICY = "sha256(seed|purl), first quota per directory"
GATES = {
    "fit": {"direct", "adapter", "no_fit", "unknown"},
    "functional": {"pass", "fail", "not_run"},
    "license": {"compatible", "incompatible", "unknown"},
    "security": {"acceptable", "unacceptable", "unknown"},
    "availability": {"before_baseline", "after_baseline", "unknown"},
}


class RegistryFrameError(ValueError):
    """Malformed data that cannot support an auditable registry pilot."""


def _keys(obj, allowed, label):
    if not isinstance(obj, dict) or set(obj) != set(allowed):
        raise RegistryFrameError(f"{label}: expected exactly {sorted(allowed)}")


def _string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise RegistryFrameError(f"{label}: nonempty string required")
    return value


def _utc(value, label):
    try:
        out = datetime.fromisoformat(_string(value, label).replace("Z", "+00:00"))
    except ValueError as exc:
        raise RegistryFrameError(f"{label}: invalid UTC time") from exc
    if out.tzinfo is None or out.utcoffset() != timedelta(0):
        raise RegistryFrameError(f"{label}: explicit UTC required")
    return out


def _digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def _sha(value, pattern, label):
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise RegistryFrameError(f"{label}: invalid SHA")
    return value


def _pinned_cargo_release(value):
    if (not isinstance(value, str) or len(value) > 128 or
            CARGO_RELEASE.fullmatch(value) is None):
        raise RegistryFrameError("version requires a concrete pinned Cargo release X.Y.Z")
    core_and_prerelease = value.split("+", 1)[0]
    if "-" in core_and_prerelease:
        prerelease = core_and_prerelease.split("-", 1)[1]
        if any(part.isdigit() and len(part) > 1 and part.startswith("0")
               for part in prerelease.split(".")):
            raise RegistryFrameError("version requires a concrete pinned Cargo release X.Y.Z")
    return value


def _git_tree_sha(rows):
    """Git tree-object SHA-1 of an all-blob (mode 100644) directory listing.

    Recomputing it offline binds every listed name and blob SHA, and the
    absence of unlisted entries, to the declared ``directory_tree_sha``. It
    checks internal consistency with that content address only; it does not
    prove the tree was actually served by the named upstream repository.
    """
    body = b"".join(
        b"100644 " + row["package_name"].encode("ascii") + b"\0" +
        bytes.fromhex(row["blob_sha"])
        for row in sorted(rows, key=lambda row: row["package_name"].encode("ascii")))
    return hashlib.sha1(b"tree %d\0" % len(body) + body).hexdigest()


def _hashable_text(value, label):
    if not isinstance(value, str):
        raise RegistryFrameError(f"{label}: string required")
    return value


def _source(manifest):
    _keys(manifest, {"schema_version", "dataset_kind", "registry",
                     "index_commit_sha", "observed_at_utc", "segments"}, "manifest")
    if (manifest["schema_version"] != "1.0" or
            manifest["dataset_kind"] != SOURCE_KIND or
            manifest["registry"] != "crates.io"):
        raise RegistryFrameError("unsupported manifest version/kind/registry")
    commit = _sha(manifest["index_commit_sha"], HEX40, "index_commit_sha")
    observed = _utc(manifest["observed_at_utc"], "observed_at_utc")
    if observed > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise RegistryFrameError("future registry observation")
    segments = manifest["segments"]
    if not isinstance(segments, list) or not segments:
        raise RegistryFrameError("nonempty segments required")
    buckets, all_names = {}, set()
    allowed_segments = {"length2": "2", "length3_a": "3/a"}
    for segment in segments:
        _keys(segment, {"segment_id", "index_path", "directory_tree_sha",
                        "source_url", "declared_count", "entries"}, "segment")
        sid = _hashable_text(segment["segment_id"], "segment_id")
        path = segment["index_path"]
        if sid not in allowed_segments or allowed_segments[sid] != path or sid in buckets:
            raise RegistryFrameError("unsupported, duplicate or mismatched index directory")
        tree_sha = _sha(segment["directory_tree_sha"], HEX40, "directory tree")
        expected_url = (f"https://api.github.com/repos/{INDEX}/contents/"
                        f"{path}?ref={commit}")
        if segment["source_url"] != expected_url:
            raise RegistryFrameError("source URL must be pinned to exact index commit")
        rows = segment["entries"]
        if (not isinstance(rows, list) or not rows or
                type(segment["declared_count"]) is not int or
                len(rows) != segment["declared_count"]):
            raise RegistryFrameError("directory denominator mismatch")
        actual = set()
        for item in rows:
            _keys(item, {"package_name", "blob_sha"}, "index entry")
            name = item["package_name"]
            if (not isinstance(name, str) or NAME.fullmatch(name) is None or
                    len(name) != (2 if sid == "length2" else 3) or
                    (sid == "length3_a" and not name.startswith("a"))):
                raise RegistryFrameError("package name outside declared index namespace")
            _sha(item["blob_sha"], HEX40, "package index entry blob")
            if name in actual or name in all_names:
                raise RegistryFrameError("duplicate crate name")
            actual.add(name)
            all_names.add(name)
        if _git_tree_sha(rows) != tree_sha:
            raise RegistryFrameError("directory entries do not reproduce declared tree SHA")
        buckets[sid] = rows
    if set(buckets) != set(allowed_segments):
        raise RegistryFrameError("both prespecified directory slices required")
    return buckets


def select_registry(manifest, plan):
    """Sample package identifiers independent of stars, Trending or adoption.

    Fixed slices are not a population-representative draw of all Rust packages.
    The documented seed is not authenticated as random or prospectively locked.
    """
    buckets = _source(manifest)
    _keys(plan, {"schema_version", "dataset_kind", "index_commit_sha",
                 "declared_at_utc", "seed", "policy", "quotas"}, "plan")
    if plan["schema_version"] != "1.0" or plan["dataset_kind"] != "registry_slice_sampling_plan":
        raise RegistryFrameError("unsupported sampling plan")
    if plan["index_commit_sha"] != manifest["index_commit_sha"] or plan["policy"] != POLICY:
        raise RegistryFrameError("sampling plan/source mismatch")
    declared = _utc(plan["declared_at_utc"], "declared_at_utc")
    if declared > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise RegistryFrameError("future-dated sampling plan")
    seed = _string(plan["seed"], "seed")
    quotas = plan["quotas"]
    if (not isinstance(quotas, dict) or set(quotas) != set(buckets) or
            any(type(v) is not int or v <= 0 or v > len(buckets[k])
                for k, v in quotas.items())):
        raise RegistryFrameError("quota invalid or greater than observed denominator")
    queue, strata = [], []
    for sid in sorted(buckets):
        rows = buckets[sid]
        order = sorted(rows, key=lambda r: (
            hashlib.sha256(f"{seed}|pkg:cargo/{r['package_name']}".encode()).hexdigest(),
            r["package_name"]))
        n = len(rows)
        strata.append({"stratum": sid, "registry_entries": n,
                       "sampled_leads": quotas[sid],
                       "nominal_within_slice_fraction": quotas[sid] / n})
        for entry in order[:quotas[sid]]:
            path = "2" if sid == "length2" else "3/a"
            name = entry["package_name"]
            queue.append({
                "package_id": f"pkg:cargo/{name}",
                "registry_index_url": f"https://github.com/{INDEX}/blob/"
                                      f"{manifest['index_commit_sha']}/{path}/{name}",
                "registry_blob_sha": entry["blob_sha"],
                "stratum": sid,
                "repository_id": None,
                "project_type": "unknown",
                "repo_created_year": None,
                "baseline_visibility": "unknown",
                "task_fit": "unknown",
                "human_review": "not_started",
            })
    return {
        "schema_version": "1.0", "dataset_kind": "unreviewed_registry_leads",
        "source_manifest_sha256": _digest(manifest),
        "selection_plan_sha256": _digest(plan),
        "registry_index_commit_sha": manifest["index_commit_sha"],
        "observed_at_utc": manifest["observed_at_utc"],
        "declared_at_utc": plan["declared_at_utc"],
        "registry_directory_denominator": sum(len(x) for x in buckets.values()),
        "selected_package_leads": len(queue),
        "strata": strata, "selected": queue,
        "external_repo_crosswalk_count": 0,
        "source_listings_independently_authenticated": False,
        "seed_independence_authenticated": False,
        "population_prevalence_eligible": False,
        "verified_task_component_pairs": 0,
        "limitation": "Actual pinned registry directory names, NOT an authenticated "
                      "full-registry or GitHub-repository frame. All repository IDs, "
                      "task fits, licensing, release times and human review are unknown.",
    }


def prepare_pair_packet(selection, tasks, nominations, manifest, plan):
    """Bind independently frozen tasks to *nominated* selected leads.

    Nominations are proposals, not judged pair outcomes. No auto-generated
    'fit' inference or acceptance; no package installation.
    """
    # Re-derive the complete selection, not merely its caller-supplied source
    # and plan hashes. This detects edited/off-frame leads while leaving actual
    # source authenticity and prospective plan locking to external reviewers.
    expected_selection = select_registry(manifest, plan)
    if _digest(selection) != _digest(expected_selection):
        raise RegistryFrameError("selection does not match original manifest and plan")
    allowed = {r["package_id"] for r in selection["selected"]}
    if len(allowed) != len(selection["selected"]):
        raise RegistryFrameError("selection contains duplicate packages")
    task_map = {}
    if not isinstance(tasks, list) or not tasks:
        raise RegistryFrameError("independent tasks required")
    for task in tasks:
        _keys(task, {"task_id", "baseline_utc", "spec_sha256",
                     "acceptance_sha256", "source_ref"}, "task")
        tid = _string(task["task_id"], "task_id")
        if IDENT.fullmatch(tid) is None or tid in task_map:
            raise RegistryFrameError("duplicate or invalid task ID")
        baseline = _utc(task["baseline_utc"], "baseline_utc")
        if baseline > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise RegistryFrameError("future task baseline")
        for key in ("spec_sha256", "acceptance_sha256"):
            _sha(task[key], HEX64, key)
        _string(task["source_ref"], "source_ref")
        task_map[tid] = task
    if not isinstance(nominations, list):
        raise RegistryFrameError("nominations must be an array")
    seen, seen_combination = set(), set()
    rows = []
    for n in nominations:
        _keys(n, {"pair_id", "task_id", "package_id", "version",
                  "release_evidence_ref", "repository_id", "identity_evidence_ref"},
              "nomination")
        pid = _string(n["pair_id"], "pair_id")
        tid = _hashable_text(n["task_id"], "task_id")
        pkg = _hashable_text(n["package_id"], "package_id")
        if (IDENT.fullmatch(pid) is None or pid in seen or tid not in task_map or
                pkg not in allowed or (tid, pkg) in seen_combination):
            raise RegistryFrameError("duplicate or out-of-frame task/component nomination")
        seen.add(pid)
        seen_combination.add((tid, pkg))
        version = n["version"]
        if version is not None:
            _pinned_cargo_release(version)
        rid = n["repository_id"]
        if rid is not None and (type(rid) is not int or rid <= 0):
            raise RegistryFrameError("repository_id must be stable positive GitHub ID or null")
        for field in ("release_evidence_ref", "identity_evidence_ref"):
            if n[field] is not None:
                _string(n[field], field)
        # No provisional feasibility when dated availability or identity are absent.
        rows.append(dict(n))
    packet = {
        "schema_version": "1.0", "dataset_kind": "unreviewed_task_component_pairs",
        "selection_plan_sha256": selection["selection_plan_sha256"],
        "selection_source_sha256": selection["source_manifest_sha256"],
        "independent_task_claims_unverified": True,
        "nominated_pair_count": len(rows), "tasks": list(task_map.values()),
        "pairs": sorted(rows, key=lambda x: x["pair_id"]),
    }
    packet["packet_sha256"] = _digest(packet)
    return packet


def _review(packet, report, slot):
    _keys(report, {"schema_version", "packet_sha256", "reviewer_ref",
                   "reviewed_at_utc", "decisions"}, f"review {slot}")
    if report["schema_version"] != "1.0" or report["packet_sha256"] != packet["packet_sha256"]:
        raise RegistryFrameError("review not bound to exact pair packet")
    ref = _string(report["reviewer_ref"], "reviewer_ref")
    if IDENT.fullmatch(ref) is None or ref.lower() == "unknown":
        raise RegistryFrameError("reviewer reference must be limited pseudonym")
    reviewed = _utc(report["reviewed_at_utc"], "reviewed_at_utc")
    if reviewed > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise RegistryFrameError("future-dated review")
    # Even when a report contains only negative or unknown votes, it cannot
    # have judged a task that was not frozen until after the review date.
    # This is a structural chronology check, NOT authentication of review.
    if any(reviewed < _utc(task["baseline_utc"], "task baseline") for task in packet["tasks"]):
        raise RegistryFrameError("review predates at least one frozen task baseline")
    if not isinstance(report["decisions"], list):
        raise RegistryFrameError("decisions array required")
    expected = {x["pair_id"] for x in packet["pairs"]}
    found = {}
    for item in report["decisions"]:
        _keys(item, set(GATES) | {"pair_id", "evidence_ref", "test_evidence_ref"}, "review decision")
        pid = _hashable_text(item["pair_id"], "pair_id")
        if pid not in expected or pid in found:
            raise RegistryFrameError("unrecognized/duplicate review pair")
        for field, values in GATES.items():
            if not isinstance(item[field], str) or item[field] not in values:
                raise RegistryFrameError(f"invalid {field} judgment")
        for field in ("evidence_ref", "test_evidence_ref"):
            if item[field] is not None:
                _string(item[field], field)
        if (item["functional"] == "pass" and
                (item["test_evidence_ref"] is None or item["evidence_ref"] is None)):
            raise RegistryFrameError("functional pass requires review AND test evidence")
        found[pid] = item
    return ref, found


def audit_pair_reviews(packet, review_a, review_b, manifest, plan):
    """Summarize *submitted* reviews, NEVER authenticate real humans.

    The packet fingerprint is self-computed, so the packet is re-bound to the
    original manifest and plan: its selection hashes must equal a fresh
    ``select_registry(manifest, plan)`` and every pair must name a selected
    lead. This checks artifact consistency, not source authenticity.
    """
    _keys(packet, {"schema_version", "dataset_kind", "selection_plan_sha256",
                   "selection_source_sha256", "independent_task_claims_unverified",
                   "nominated_pair_count", "tasks", "pairs", "packet_sha256"}, "packet")
    if (packet["schema_version"] != "1.0" or
            packet["independent_task_claims_unverified"] is not True or
            not isinstance(packet["tasks"], list) or not packet["tasks"] or
            not isinstance(packet["pairs"], list) or
            type(packet["nominated_pair_count"]) is not int or
            packet["nominated_pair_count"] != len(packet["pairs"])):
        raise RegistryFrameError("invalid packet schema or pair denominator")
    for field in ("selection_plan_sha256", "selection_source_sha256", "packet_sha256"):
        _sha(packet[field], HEX64, field)
    task_ids = set()
    for task in packet["tasks"]:
        _keys(task, {"task_id", "baseline_utc", "spec_sha256",
                     "acceptance_sha256", "source_ref"}, "packet task")
        tid = _string(task["task_id"], "task_id")
        if IDENT.fullmatch(tid) is None or tid in task_ids:
            raise RegistryFrameError("duplicate or invalid packet task ID")
        task_ids.add(tid)
        if _utc(task["baseline_utc"], "baseline_utc") > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise RegistryFrameError("future task baseline")
        for field in ("spec_sha256", "acceptance_sha256"):
            _sha(task[field], HEX64, field)
        _string(task["source_ref"], "source_ref")
    pair_ids, combinations = set(), set()
    for pair in packet["pairs"]:
        _keys(pair, {"pair_id", "task_id", "package_id", "version",
                    "release_evidence_ref", "repository_id", "identity_evidence_ref"}, "packet pair")
        pid = _string(pair["pair_id"], "pair_id")
        tid = _string(pair["task_id"], "task_id")
        pkg = _string(pair["package_id"], "package_id")
        if (IDENT.fullmatch(pid) is None or pid in pair_ids or tid not in task_ids or
                (tid, pkg) in combinations):
            raise RegistryFrameError("duplicate or out-of-task-frame packet pair")
        pair_ids.add(pid)
        combinations.add((tid, pkg))
        if not pkg.startswith("pkg:cargo/") or NAME.fullmatch(pkg[len("pkg:cargo/"):]) is None:
            raise RegistryFrameError("invalid cargo package identifier")
        rid = pair["repository_id"]
        if rid is not None and (type(rid) is not int or rid <= 0):
            raise RegistryFrameError("repository_id must be stable positive GitHub ID or null")
        if pair["version"] is not None:
            _pinned_cargo_release(pair["version"])
        for field in ("release_evidence_ref", "identity_evidence_ref"):
            if pair[field] is not None:
                _string(pair[field], field)
    if (packet.get("dataset_kind") != "unreviewed_task_component_pairs" or
            packet.get("packet_sha256") != _digest({
                k: v for k, v in packet.items() if k != "packet_sha256"})):
        raise RegistryFrameError("invalid or changed pair packet fingerprint")
    frame = select_registry(manifest, plan)
    in_frame = {row["package_id"] for row in frame["selected"]}
    if (packet["selection_plan_sha256"] != frame["selection_plan_sha256"] or
            packet["selection_source_sha256"] != frame["source_manifest_sha256"] or
            any(pair["package_id"] not in in_frame for pair in packet["pairs"])):
        raise RegistryFrameError("pair packet does not match original manifest and plan")
    a_ref, a = _review(packet, review_a, "A")
    b_ref, b = _review(packet, review_b, "B")
    if a_ref.casefold() == b_ref.casefold():
        raise RegistryFrameError("independent slots need distinct reviewer references")
    status, complete, provisional, disagreements = [], 0, 0, 0
    for pair in packet["pairs"]:
        pid = pair["pair_id"]
        first, second = a.get(pid), b.get(pid)
        label = "unreviewed"
        if first and second:
            complete += 1
            if any(first[key] != second[key] for key in GATES):
                label = "disagreement_or_needs_adjudication"
                disagreements += 1
            elif (all(first[key] == value for key, value in (
                    ("functional", "pass"), ("license", "compatible"),
                    ("security", "acceptable"), ("availability", "before_baseline")))
                  and first["fit"] in ("direct", "adapter")
                  and all(x is not None for x in (
                      pair["version"], pair["release_evidence_ref"],
                      pair["repository_id"], pair["identity_evidence_ref"]))):
                label = "concordant_provisional_fit_only"
                provisional += 1
            elif any(first[key] in values for key, values in (
                    ("fit", {"no_fit"}), ("functional", {"fail"}),
                    ("license", {"incompatible"}), ("security", {"unacceptable"}),
                    ("availability", {"after_baseline"}))):
                label = "concordant_negative_or_incompatible"
            else:
                label = "concordant_unknown_or_not_run"
        elif first or second:
            label = "single_review_only"
        status.append({"pair_id": pid, "status": label})
    return {
        "schema_version": "1.0", "dataset_kind": "pair_review_structural_audit",
        "packet_sha256": packet["packet_sha256"],
        "nominated_pairs": len(status),
        "two_reports_present": complete, "unresolved_disagreements": disagreements,
        "concordant_provisional_fit": provisional,
        "still_needed_for_50_provisional": max(0, 50-provisional),
        # Submitted matching labels alone can NEVER reduce the issue's 50
        # genuinely human-validated-pair acceptance denominator.
        "externally_authenticated_human_pairs": 0,
        "still_needed_for_50_authenticated_human_pairs": 50,
        "reviewers_authenticated_as_real_independent_humans": False,
        "meets_issue_15_scientific_acceptance": False,
        "pair_statuses": status,
        "limitation": "Self-supplied reviewer references cannot authenticate people, "
                      "independent acceptance tests, licenses, GitHub identity, or "
                      "version-level security. At least 50 truly human-adjudicated "
                      "pairs and independent provenance audit remain required.",
    }


def _read(path):
    """Read one CLI input with the shared bounded strict research JSON reader.

    ``load_research_json_file`` refuses leaf symlinks, FIFOs/special files and
    oversized or grown inputs, and its diagnostics never echo paths or keys.
    """
    try:
        return load_research_json_file(path)
    except ResearchJSONError as exc:
        if str(exc) == "invalid or ambiguous JSON input":
            raise RegistryFrameError(
                "registry input must be unambiguous strict UTF-8 JSON") from None
        # Remaining shared-reader messages are fixed and contain no path.
        raise RegistryFrameError(f"registry {exc}") from None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    s = sub.add_parser("select")
    s.add_argument("--manifest", required=True)
    s.add_argument("--plan", required=True)
    s.add_argument("--output", required=True)
    p = sub.add_parser("prepare-pairs")
    p.add_argument("--selection", required=True)
    p.add_argument("--manifest", required=True)
    p.add_argument("--plan", required=True)
    p.add_argument("--tasks", required=True)
    p.add_argument("--nominations", required=True)
    p.add_argument("--output", required=True)
    a = sub.add_parser("audit-pairs")
    a.add_argument("--packet", required=True)
    a.add_argument("--review-a", required=True)
    a.add_argument("--review-b", required=True)
    a.add_argument("--manifest", required=True)
    a.add_argument("--plan", required=True)
    a.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        if args.mode == "select":
            result = select_registry(_read(args.manifest), _read(args.plan))
        elif args.mode == "prepare-pairs":
            result = prepare_pair_packet(_read(args.selection),
                                         _read(args.tasks), _read(args.nominations),
                                         _read(args.manifest), _read(args.plan))
        else:
            result = audit_pair_reviews(_read(args.packet),
                                        _read(args.review_a), _read(args.review_b),
                                        _read(args.manifest), _read(args.plan))
        publish_json(args.output, result)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "output": args.output, "dataset_kind": result["dataset_kind"],
        "scientific_acceptance": False}, sort_keys=True))


if __name__ == "__main__":
    main()
