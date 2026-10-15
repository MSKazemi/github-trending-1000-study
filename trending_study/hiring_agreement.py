"""Offline agreement for supplied hiring labels; no authenticated human study.

Uses the existing rubric kappa engine, structural validators, strict JSON
reader and write-once storage. Never fetches sources or grants research rights.
"""
import argparse
from collections import Counter
import csv
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat

from .blind_review import _exact, _utc, fingerprint
from .data_integrity import decode_research_json
from .rubric_agreement import _agreement
from .safe_io import ProvenanceWriteError, disjoint, publish_once

SCHEMA = "hiring-223-v1"
SAMPLE = "hiring-223-direct-read-candidates-2026-10-14"
CODEBOOK = "hiring-223-codebook-v1.0.0"
THEMES = ("agent_runtime", "context_memory", "evaluation_quality", "rl_training",
          "sandbox_security", "enterprise_integrations", "inference_efficiency",
          "developer_reuse", "platform_infrastructure", "agent_operations", "other")
PRIMARY_THEMES = dict(zip(("agent_harness", "context_memory", "evaluations", "rl_post_training",
                          "security", "enterprise_integration", "inference_efficiency",
                          "reuse_discovery", "platform", "operations", "other"), THEMES))
ABSTENTIONS = ("uncertain", "not_reviewable")
DECISIONS = ("present", "absent") + ABSTENTIONS
SOURCES = ("references/ai_hiring_job_leads_source_audit_2026-10-13.csv",
           "references/ai_hiring_expansion_leads_2026-10-13.csv")
MAX_BYTES = 1024 * 1024
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,63}\Z")
COUNTERINTERPRETATIONS = ("none", "ambiguous_text", "access_failure", "overlapping_tasks")


class HiringError(ValueError):
    """Malformed or inconsistent structural assertions."""


def _enum(value, choices, name):
    if not isinstance(value, str) or value not in choices:
        raise HiringError(f"{name}: invalid choice")
    return value


def _identifier(value, name):
    if (not isinstance(value, str) or not IDENTIFIER.fullmatch(value)
            or value.casefold() in ("unknown", "none")):
        raise HiringError(f"{name}: bounded ASCII pseudonym/reference required")
    return value


def _read_bytes(path):
    """Bounded regular-file read; reject symlinks in every path component."""
    path = Path(os.path.abspath(path))
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise HiringError("symlink input paths are not accepted")
    flags = os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(path, flags)
        with os.fdopen(fd, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise HiringError("regular file required")
            raw = stream.read(MAX_BYTES + 1)
    except OSError:
        # Neither confidential input paths nor platform errors belong in logs.
        raise HiringError("input must be a readable bounded regular file") from None
    if len(raw) > MAX_BYTES:
        raise HiringError("input exceeds 1 MiB")
    return raw


def load_document(path):
    raw = _read_bytes(path)
    try:
        value = decode_research_json(raw, "hiring input")
    except (ValueError, RecursionError):
        # The shared decoder can otherwise echo arbitrary duplicate object
        # keys from confidential coder notes. Keep a fixed, safe CLI error.
        raise HiringError("invalid or ambiguous strict UTF-8 JSON") from None
    pending = [(value, 0)]
    nodes = 0
    while pending:
        item, depth = pending.pop()
        nodes += 1
        if depth > 20 or nodes > 20000:
            raise HiringError("JSON depth/node limit exceeded")
        if isinstance(item, dict):
            pending.extend((v, depth + 1) for v in item.values())
        elif isinstance(item, list):
            pending.extend((v, depth + 1) for v in item)
    return value, hashlib.sha256(raw).hexdigest()


def load_json(path):
    return load_document(path)[0]


def derive_frame(root):
    """Project source ledgers into candidate identities, never analyst theme votes."""
    sources, items = [], []
    for index, relative in enumerate(SOURCES):
        raw = _read_bytes(Path(root) / relative)
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
        rows = list(reader)
        if len(rows) != (18 if index == 0 else 6):
            raise HiringError("source ledger row denominator changed; new frame version required")
        sources.append({"path": relative, "sha256": hashlib.sha256(raw).hexdigest(), "rows": len(rows)})
        for number, row in enumerate(rows, 1):
            if index == 0:
                if row["seed_row"] != str(number):
                    raise HiringError("source seed order changed")
                status = {"read": "selected_pending_recheck", "read_indexed_text": "index_text_only",
                          "identity_hold": "identity_hold"}.get(row["content_verification"])
                url = row["individual_official_url"]
                date = row["source_observation_date_utc"]
            else:
                status = {"official_individual_page": "direct_access_unconfirmed",
                          "official_individual_search_index": "index_text_only"}.get(row["source_evidence_class"])
                url = row["official_url"]
                date = row["collection_date_utc"]
            if status is None or date != "2026-10-13":
                raise HiringError("source evidence/date changed; review frame version")
            items.append({"item_id": f"{'S' if index == 0 else 'E'}{number:02}",
                          "source_index": index, "row_number": number, "source_url": url,
                          "source_observed_date_utc": date, "source_status": status,
                          "selected": status == "selected_pending_recheck"})
    if [x["item_id"] for x in items if x["selected"]] != [f"S{x:02}" for x in (1,2,3,4,5,6,9,10,12)]:
        raise HiringError("candidate selection changed; new reviewed frame version required")
    return {"schema_version": SCHEMA, "dataset_kind": "candidate_leads", "sample_id": SAMPLE,
            "codebook_version": CODEBOOK, "sources": sources, "items": items}


def verify_frame(frame, root="."):
    # Exact derivation rejects extra/private fields, fabricated candidates,
    # duplicate IDs and altered source statuses or hashes, including bool/int aliases.
    expected = derive_frame(root)
    if fingerprint(frame) != fingerprint(expected):
        raise HiringError("frame must exactly match preserved source-ledger projection")
    return {"frame_sha256": fingerprint(frame), "source_frame_n": 24, "selected_n": 9,
            "status_counts": dict(Counter(x["source_status"] for x in frame["items"])),
            "human_independence_verified": False, "research_enrollment": "blocked"}


def prepare(frame, reviewer_id="pending_reviewer", root="."):
    verify_frame(frame, root)
    _identifier(reviewer_id, "reviewer_id")
    return {"schema_version": SCHEMA, "sample_id": SAMPLE, "frame_sha256": fingerprint(frame),
            "dataset_kind": "self_reported", "reviewer_id": reviewer_id,
            "reviewed_at_utc": None, "human_attested": False,
            "ratings": [{"item_id": x["item_id"], "source_access": "unavailable",
                         "source_checked_at_utc": None,
                         "themes": dict.fromkeys(THEMES, "not_reviewable"),
                         "primary_task": "not_reviewable", "evidence_ref": None,
                         "counterinterpretation": "access_failure"}
                        for x in frame["items"] if x["selected"]]}


def _time(value, name):
    timestamp = _utc(value, name)
    if timestamp > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise HiringError(f"{name}: future timestamp")
    if timestamp < datetime(2026, 10, 13, tzinfo=timezone.utc):
        raise HiringError(f"{name}: before source-ledger observation date")
    return timestamp


def _review(frame, data):
    _exact(data, {"schema_version", "sample_id", "frame_sha256", "dataset_kind", "reviewer_id",
                  "reviewed_at_utc", "human_attested", "ratings"}, "review")
    if data["schema_version"] != SCHEMA or data["sample_id"] != SAMPLE or data["frame_sha256"] != fingerprint(frame):
        raise HiringError("review frame/sample/version mismatch")
    _enum(data["dataset_kind"], ("synthetic", "self_reported"), "dataset_kind")
    _identifier(data["reviewer_id"], "reviewer_id")
    if type(data["human_attested"]) is not bool:
        raise HiringError("human_attested must be boolean")
    if data["dataset_kind"] == "self_reported" and not data["human_attested"]:
        raise HiringError("self-reported reviews require explicit human attestation (not authentication)")
    if data["dataset_kind"] == "synthetic" and data["human_attested"]:
        raise HiringError("synthetic reviewers must not claim to be human")
    reviewed = _time(data["reviewed_at_utc"], "reviewed_at_utc")
    expected = {x["item_id"] for x in frame["items"] if x["selected"]}
    rows = data["ratings"]
    if not isinstance(rows, list) or len(rows) > len(expected):
        raise HiringError("ratings must contain at most nine candidates")
    result = {}
    for row in rows:
        _exact(row, {"item_id", "source_access", "source_checked_at_utc", "themes", "primary_task",
                     "evidence_ref", "counterinterpretation"}, "rating")
        tid = _enum(row["item_id"], expected, "item_id")
        if tid in result:
            raise HiringError("duplicate rating")
        _enum(row["source_access"], ("read", "unavailable"), "source_access")
        if _time(row["source_checked_at_utc"], "source_checked_at_utc") > reviewed:
            raise HiringError("source check after review")
        _identifier(row["evidence_ref"], "evidence_ref")
        _enum(row["counterinterpretation"], COUNTERINTERPRETATIONS, "counterinterpretation")
        _exact(row["themes"], THEMES, "themes")
        for label in row["themes"].values():
            _enum(label, DECISIONS, "theme decision")
        primary = _enum(row["primary_task"], tuple(PRIMARY_THEMES) + ABSTENTIONS, "primary_task")
        if row["source_access"] == "unavailable":
            if primary != "not_reviewable" or any(x != "not_reviewable" for x in row["themes"].values()):
                raise HiringError("inaccessible source cannot supply positive/negative/uncertain votes")
        elif primary == "not_reviewable" or "not_reviewable" in row["themes"].values():
            raise HiringError("read body cannot be marked not_reviewable")
        if primary in PRIMARY_THEMES and row["themes"][PRIMARY_THEMES[primary]] != "present":
            raise HiringError("primary task requires its corresponding theme present")
        result[tid] = row
    return result


def _statistics(pairs, labels):
    binary = labels == ("present", "absent")
    rated = [(a, b) for a, b in pairs if a in labels and b in labels]
    stats = _agreement(rated, labels=labels)
    stats["reason"] = ("no jointly rated items" if not rated else
                       "fewer than two jointly rated items" if len(rated) < 2 else
                       "chance agreement is one" if stats["cohens_kappa"] is None else None)
    stats["selected_n"] = len(pairs)
    stats["excluded_n"] = len(pairs) - len(rated)
    stats["rater_a_exclusions"] = {k: sum(a == k for a, _ in pairs) for k in (None,) + ABSTENTIONS}
    stats["rater_b_exclusions"] = {k: sum(b == k for _, b in pairs) for k in (None,) + ABSTENTIONS}
    # JSON keys are explicit, never a None/null key coerced to a misleading label.
    for key in ("rater_a_exclusions", "rater_b_exclusions"):
        stats[key]["missing"] = stats[key].pop(None)
    if binary:
        counts = Counter(rated)
        pp, pa, ap, aa = (counts[(a,b)] for a,b in (("present","present"),("present","absent"),
                                                   ("absent","present"),("absent","absent")))
        stats["confusion"] = dict(zip(("PP", "PA", "AP", "AA"), (pp,pa,ap,aa)))
        stats["positive_agreement"] = 2*pp/(2*pp+pa+ap) if 2*pp+pa+ap else None
        stats["negative_agreement"] = 2*aa/(2*aa+pa+ap) if 2*aa+pa+ap else None
    return stats


def analyze(frame, review_a, review_b, adjudication=None, root="."):
    verify_frame(frame, root)
    a, b = _review(frame, review_a), _review(frame, review_b)
    if review_a["reviewer_id"].casefold() == review_b["reviewer_id"].casefold():
        raise HiringError("distinct reviewer pseudonyms required")
    if review_a["dataset_kind"] != review_b["dataset_kind"]:
        raise HiringError("do not mix synthetic and self-reported reviews")
    records, pairs, disputes = [], {k: [] for k in THEMES + ("primary_task",)}, {}
    for item in frame["items"]:
        tid = item["item_id"]
        entry = {"item_id": tid, "source_status": item["source_status"], "selected": item["selected"]}
        entry.update({"review_a": a.get(tid), "review_b": b.get(tid)})
        records.append(entry)
        if not item["selected"]:
            continue
        for code in pairs:
            x = a.get(tid, {}).get("primary_task") if code == "primary_task" else a.get(tid, {}).get("themes", {}).get(code)
            y = b.get(tid, {}).get("primary_task") if code == "primary_task" else b.get(tid, {}).get("themes", {}).get(code)
            pairs[code].append((x,y))
            if x is not None and y is not None and x != y:
                disputes[(tid,code)] = {"item_id": tid, "code": code, "review_a": x, "review_b": y}
    decisions = []
    if adjudication is not None:
        _exact(adjudication, {"schema_version", "sample_id", "frame_sha256", "review_a_sha256", "review_b_sha256",
                             "dataset_kind", "adjudicator_id", "adjudicated_at_utc", "predictions_unseen_attested", "decisions"}, "adjudication")
        for key, expected in (("schema_version",SCHEMA),("sample_id",SAMPLE),("frame_sha256",fingerprint(frame)),
                              ("review_a_sha256",fingerprint(review_a)),("review_b_sha256",fingerprint(review_b)),
                              ("dataset_kind",review_a["dataset_kind"])):
            if adjudication[key] != expected:
                raise HiringError("adjudication source bindings mismatch")
        cid = _identifier(adjudication["adjudicator_id"], "adjudicator_id")
        if cid.casefold() in (review_a["reviewer_id"].casefold(), review_b["reviewer_id"].casefold()):
            raise HiringError("third distinct adjudicator required")
        if adjudication["predictions_unseen_attested"] is not True:
            raise HiringError("explicit predictions-unseen attestation required (not authenticated)")
        if _time(adjudication["adjudicated_at_utc"], "adjudicated_at_utc") <= max(
                _time(review_a["reviewed_at_utc"], "review A"), _time(review_b["reviewed_at_utc"], "review B")):
            raise HiringError("adjudication must follow both reviews")
        if not isinstance(adjudication["decisions"], list) or len(adjudication["decisions"]) > len(disputes):
            raise HiringError("invalid adjudication decision list")
        seen = set()
        for row in adjudication["decisions"]:
            _exact(row, {"item_id", "code", "decision", "evidence_ref"}, "adjudication decision")
            tid = _enum(row["item_id"], [x["item_id"] for x in frame["items"] if x["selected"]], "adjudication item")
            code = _enum(row["code"], tuple(pairs), "adjudication code")
            key = (tid,code)
            if key not in disputes or key in seen:
                raise HiringError("adjudication only for unique actual A/B disputes")
            _enum(row["decision"], tuple(PRIMARY_THEMES)+ABSTENTIONS if code == "primary_task" else DECISIONS, "adjudicated decision")
            _identifier(row["evidence_ref"], "adjudication evidence_ref")
            seen.add(key)
            decisions.append(row.copy())
    # Consensus/adjudication is a separate view, never a reliability input.
    chosen = {(x["item_id"], x["code"]): x["decision"] for x in decisions}
    def final(tid, code):
        if (tid, code) in chosen:
            return chosen[(tid, code)]
        one, two = a.get(tid), b.get(tid)
        if one is None or two is None:
            return None
        x = one["primary_task"] if code == "primary_task" else one["themes"][code]
        y = two["primary_task"] if code == "primary_task" else two["themes"][code]
        return x if x == y else None
    for row in decisions:
        tid = row["item_id"]
        primary = final(tid, "primary_task")
        if primary in PRIMARY_THEMES and final(tid, PRIMARY_THEMES[primary]) != "present":
            raise HiringError("adjudicated primary requires a resolved corresponding present theme")
    resolved = {(x["item_id"], x["code"]) for x in decisions if x["decision"] not in ABSTENTIONS}
    # Missing coder rows are not disagreements: they never enter `disputes`.
    # A report must not call adjudication complete while a selected item has
    # no A/B paired submission, even if all *submitted* labels agree.
    selected_ids = [x["item_id"] for x in frame["items"] if x["selected"]]
    missing_a = [tid for tid in selected_ids if tid not in a]
    missing_b = [tid for tid in selected_ids if tid not in b]
    unpaired = [tid for tid in selected_ids if tid not in a or tid not in b]
    pending_disputes = [v for k, v in disputes.items() if k not in resolved]
    adjudication_status = ("incomplete_reviews" if unpaired else
                           "partial" if pending_disputes else "complete")
    return {"schema_version": SCHEMA, "dataset_kind": review_a["dataset_kind"], "frame_sha256": fingerprint(frame),
            "review_a_sha256": fingerprint(review_a), "review_b_sha256": fingerprint(review_b),
            "adjudication_sha256": fingerprint(adjudication) if adjudication is not None else None,
            "source_frame_n": len(frame["items"]), "selected_n": len(selected_ids),
            "review_submission": {"review_a_n": len(a), "review_b_n": len(b),
                                  "paired_selected_n": len(selected_ids) - len(unpaired),
                                  "missing_a_item_ids": missing_a, "missing_b_item_ids": missing_b,
                                  "unpaired_selected_item_ids": unpaired},
            "human_independence_verified": False, "source_rights_verified": False, "research_enrollment": "blocked",
            "per_theme": {k: _statistics(pairs[k], ("present","absent")) for k in THEMES},
            "primary_task": _statistics(pairs["primary_task"], tuple(PRIMARY_THEMES)),
            "records": records, "disagreements": list(disputes.values()),
            "adjudication": {"decisions": decisions, "status": adjudication_status,
                             "pending": pending_disputes,
                             "missing_rating_item_ids": unpaired},
            "warning": "Structural self-report audit only; synthetic ratings are fictional; no authenticated humans, rights, current ads, or empirical results."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("verify-frame", "pack", "analyze"):
        p = sub.add_parser(name)
        p.add_argument("--frame", required=True, type=Path)
        p.add_argument("--root", default=".", type=Path)
        if name != "verify-frame":
            p.add_argument("--output", required=True, type=Path)
        if name == "pack":
            p.add_argument("--reviewer-id", default="pending_reviewer")
        if name == "analyze":
            p.add_argument("--coder-a", required=True, type=Path)
            p.add_argument("--coder-b", required=True, type=Path)
            p.add_argument("--adjudication", type=Path)
    args = parser.parse_args(argv)
    try:
        frame, raw_frame_sha = load_document(args.frame)
        verification = verify_frame(frame, args.root)
        verification["raw_frame_sha256"] = raw_frame_sha
        if args.command == "verify-frame":
            print(json.dumps(verification, sort_keys=True))
            return
        inputs = [args.frame] + [args.root / path for path in SOURCES]
        if args.command == "pack":
            result = prepare(frame, args.reviewer_id, args.root)
        else:
            inputs += [args.coder_a, args.coder_b, args.adjudication]
            a, raw_a_sha = load_document(args.coder_a)
            b, raw_b_sha = load_document(args.coder_b)
            c, raw_c_sha = load_document(args.adjudication) if args.adjudication else (None, None)
            result = analyze(frame, a, b, c, args.root)
            result["raw_input_sha256"] = {"frame": raw_frame_sha, "coder_a": raw_a_sha,
                                          "coder_b": raw_b_sha, "adjudication": raw_c_sha}
        disjoint(args.output, *inputs)
        payload = (json.dumps(result, sort_keys=True, indent=2, allow_nan=False)+"\n").encode()
        publish_once([(args.output,payload)])
        print(json.dumps({"output_created": True, "frame_sha256": verification["frame_sha256"],
                          "research_enrollment": "blocked"}))
    except (OSError, ProvenanceWriteError):
        parser.exit(2, "error: input/output filesystem operation failed; details withheld\n")
    except (ValueError, TypeError, KeyError, RecursionError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    main()
