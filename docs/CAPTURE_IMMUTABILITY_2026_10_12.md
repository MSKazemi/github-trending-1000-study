# Capture and derived-artifact immutability: safety contract (2026-10-12)

**Scope:** implementation slice of [issue #4](https://github.com/MSKazemi/github-trending-1000-study/issues/4) after repository audit finding A01. **Status:** offline tooling; not a permitted live collection, not a parser accuracy study, and not preregistration.

## Why write-once is necessary

A capture is primary evidence. Re-running a command must not silently replace:
- a raw HTML capture;
- its capture-time SHA-256 manifest;
- a parsed observation JSONL;
- a pilot audit JSON; or
- an enrichment JSONL.

A pre-existing source and derived output must never be the same path, even via a symlink or relative path alias. The runner now rejects existing destinations and input/output collisions **before making any HTTP request**. A fixed date in a tutorial cannot recreate a historical Trending page.

## What is implemented

- `trending_study.safe_io.publish_once` stages complete file contents in the destination directory, fsyncs them, and creates each final destination using `os.link` (exclusive creation). It never uses overwrite-capable `os.replace` or write-text-on-existing-target semantics.
- `capture` checks paths and now **hard-blocks live Trending requests before networking** while source-access review is pending. Its preserved, synthetically mocked internal path would compute a manifest at fetch time and stage raw + manifest together only after a *future independently reviewed permission/code amendment*. See [source-access decision](SOURCE_ACCESS_DECISION_2026-10-13.md).
- `parse-trending`, `pilot-parse` and `enrich` refuse collisions and preexisting output, preserving raw data on error.
- Synthetic unit tests exercise byte-for-byte preservation, network-free refusal, source/derived path aliases, interrupted publication and successful source/manifest checksum integrity.
- `pilot-parse` continues to mark observations **not enrolled**: a valid checksum is not proof the real page has complete/correct rankings.

## Important limit: two destinations are not one atomic transaction

Filesystem operations create *each* final path atomically, but **the raw+manifest pair is NOT one atomic filesystem transaction**. If a disk failure or permission change occurs after publishing the first file, the successful file remains untouched and the command raises an explicit **partial bundle** error. Do not automatically delete it, replace it, or treat it as valid evidence. Inspect both filenames, the source checksum, capture timestamp and command logs. Preserve partial evidence and record an incident. A truly all-or-none multilevel transaction would require a new storage/manifest protocol, not a misleading use of rename.

The method relies on same-filesystem hard links. On unsupported mount/file systems it fails closed. Staging files are cleaned up on ordinary exceptions, but a process crash may leave `.capture-pending-*` files; never classify those as validated captures. This tool does not provide concurrency locking across collaborators, exactly-once remote retrieval, GitHub attestation, or a durable job queue.

## Runbook for operators

1. Inspect [ethical access constraints](ETHICS.md) and [pilot prerequisites](PILOT_CAPTURE_AND_PREFLIGHT.md). **Do not start automated recurring scraping** or confirmatory collection by default.
2. **Currently blocked:** the following command is a **future conditional example, not an action to execute now**. The CLI returns nonzero before any HTTP request, even with a valid UTC date. Only after an independently authorized and reviewed re-enable may an operator use a fresh UTC day and unique filename:

```bash
UTC_DAY="$(date -u +%F)"
python -m trending_study capture --date "$UTC_DAY" --window daily \
  --output "data/raw/$UTC_DAY-daily.html" \
  --manifest-output "data/raw/$UTC_DAY-daily.manifest.json"
```

3. Keep raw and manifest immutable. When they both exist, verify their SHA-256 with the pilot parser. Choose **new filenames** for the derived JSONL and audit, never ones previously used:

```bash
python -m trending_study pilot-parse \
  --input "data/raw/$UTC_DAY-daily.html" \
  --manifest "data/raw/$UTC_DAY-daily.manifest.json" \
  --output "data/processed/$UTC_DAY-daily.pilot.jsonl" \
  --audit-output "data/processed/$UTC_DAY-daily.pilot.audit.json"
```

4. If a path already exists, the safe action is **stop, inspect, and use a new attempt identifier**, not erase it. If only one file in a pair exists, quarantine the partial bundle with incident notes; do not claim a completed observation.
5. Preserve API rate-limit metadata and retry/error tracking in the later [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4) longitudinal follow-up work. **This PR does not yet implement a durable snapshot/resume queue.**

## Reproducibility and testing

Run `python -m unittest discover -s tests -v` on Python 3.10 and 3.12 (CI). All regression fixtures are synthetic and offline; no real-world number of captured repositories or measured method quality is claimed.

**Next gate:** finish trusted numeric repository IDs, point-in-time follow-ups and error logging (#4); independently validate actual parser recall/completeness on sufficient permitted real pages (#2), and freeze the protocol before any enrollment.
