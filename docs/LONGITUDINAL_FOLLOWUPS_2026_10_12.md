# Longitudinal repository follow-ups — schedule, collect and audit

**Implemented:** 2026-10-12 for issue #4; **status:** offline/opt-in instrumentation, **not** a collected cohort, approved research trial, completed follow-up, or historical backfill. Python standard library only.

## Purpose and research boundary

Obtain actual point-in-time GitHub metadata approximately **+30, +90 and +180 days after a measured baseline snapshot**, keeping stable numeric repo IDs, observed times, explicit missing/error outcomes, raw provenance, and immutable event logs. Comparisons must report true elapsed time and follow-up-window failures; a fresh API response in January cannot be falsely assigned to an absent November snapshot.

**Important:** the source enrollment/status and written protocol must first be independently approved. The program checks documentary fields but **cannot authenticate** reviewer identities, source permissions, approved dates, or GitHub page truth. The current `pilot-parse` explicitly sets `eligible_for_confirmatory_cohort=false`, and these rows are deliberately rejected by this planner.

## Inputs: one write-once approved baseline JSONL

Each row requires:
- `repository_id`: immutable positive numeric GitHub repository ID, uniquely observed.
- `full_name_at_enrichment`: current `owner/repository`, may later rename/transfer.
- `metadata_status="ok"`, `stars`: nonnegative baseline star count, with **real** `enriched_at_utc` UTC. Follow-up time zero is the **time the star baseline was measured**, not the date a parser was run or a Trending page was initially displayed.
- `source_sha256`: SHA-256 of a previously preserved raw HTML capture; do not fake it.
- `eligible_for_confirmatory_cohort=true` only after genuine external adjudication; `study_id`, `protocol_commit` (40-hex git commit) and `cohort_approval_ref` with real review provenance.
- All rows must share study, protocol and approval. Any inconsistent or duplicate stable ID fails the entire schedule.

**This is a proposed input contract, not a migration that turns current pilot data into approved observations.** Existing pilot-only examples must stay excluded. See [data dictionary](DATA_DICTIONARY.md) and [protocol freeze gates](PROTOCOL_FREEZE_STATUS_2026_10_12.md).

A clearly **synthetic, non-enrolled fixture** is available at [`examples/followup_baseline.synthetic.jsonl`](../examples/followup_baseline.synthetic.jsonl) solely for local planner tests; do not run live collection against it or mistake fake approval references for signatures.

## Commands

```bash
# Offline demonstration only; the fixture is synthetic and NOT an approved cohort.
python -m trending_study.longitudinal plan \
  --input examples/followup_baseline.synthetic.jsonl \
  --output /tmp/followup-plan.synthetic.jsonl \
  --grace-days 3 7 14

python -m trending_study.longitudinal status \
  --plan /tmp/followup-plan.synthetic.jsonl \
  --events-dir /tmp/followup-events.synthetic
```

Grace days are **mandatory configuration choices** (one for each horizon), *not* empirical thresholds: the real study must prespecify window tolerances before outcomes. The plan is deterministic, sorted by stable ID and horizon, write-once, and each task ID depends on the protocol commit, baseline time and horizon. Retain original plan bytes; events bind to its SHA-256.

For an **externally approved, real** cohort *only*, after permission checks and at a due observation time:

```bash
python -m trending_study.longitudinal collect \
  --plan /path/to/real-approved-followup-plan.jsonl \
  --events-dir /path/to/new-immutable-events-directory \
  --confirm-network --max-requests 5 --max-events 10
```

The collector never fetches anything from `plan` or `status`, needs an explicit `--confirm-network`, has a bounded request/event budget and no aggressive retries or scheduling. A `GITHUB_TOKEN` can be supplied as an environment variable (never checked in). Calls use the **documented GitHub REST repository endpoint** `GET /repos/{owner}/{repo}`; each returned numeric ID must match the planned ID. On a verified rename or transfer the most recently verified name can be reused on later due dates. A 404 is **unknown unavailable/private/renamed**, not proof of deletion. No attempt is made to reconstruct historical counts from current star counts.

## Immutable event ledger and error semantics

- A unique `*.json` event file is published with write-once semantics per attempted due task; source JSONL is never modified.
- Every event carries the **plan digest**, immutable ID, due and expiry times, true observed UTC, GitHub response timestamp/header where present, HTTP status and surviving rate-limit metadata. Access tokens and raw responses are never logged.
- `ok` requires HTTP 200, exact matching repository ID, public repository and valid counters *within* the prespecified observation window. `open_issues_including_prs` must never be reported as pure issues.
- After the grace window, record `missed_window` with `stars=null` and **no HTTP request**. If a request completes late, record `late_observation` separately but exclude it from accepted in-window follow-up.
- `not_found_or_private_or_renamed`, `rate_limited`, `network_error`, `access_denied`, `identity_mismatch`, `invalid_response` and `not_public` are explicit outcomes. **Unknown is not zero.**
- Rerunning `collect` skips completed/missed tasks. A failed task is not retried again the same UTC day; an operator may retry on another day within the frozen window. Stop on rate limit, authorization or invalid identity/response. The collector leaves a local `.followup.lock` during a run; if a process crashes, inspect before manually removing a stale lock. Never run two collectors against the same ledger.

**Provenance limitation:** file hashes and self-declared approval references cannot prove GitHub served the payload, that the cohort was registered, or that a public repo ID remained available after transfer. API availability and client timestamps have clock/network error. Latency, censoring, missingness, inaccessible transitions, and interrupted runs must be analyzed; do not drop failed repos from denominators.

## Offline tests and study status

```bash
python -m unittest discover -s tests -v
```

Unit tests use synthetic, clearly marked baselines and mocked API responses for stable IDs, renames, identity mismatch, rate limiting, interrupted/missed windows, immutability, safe resume and CLI planning. They do not prove experimental scientific validity or capture completeness.

**Next scientific dependencies:** #2 real-page independent rank/completeness audit and access permission; #3 verified sampling/power; #21 externally adjudicated reuse tasks; reviewer-signed consolidated protocol. See [integrated mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

## Event-ledger replay validation — 2026-10-12 integrity hardening

This issue-#4 follow-up hardening makes `status`, `collect` resume, and any later export **fail closed when event records contradict their own frozen plan**. It does not change the network opt-in or permit enrollment.

- Every `followup-event-1.0` JSON record must contain the exact fields emitted by the collector for an API attempt, or the separate `missed_window` field set. Unexpected keys (including accidental confidential data) and missing required fields are rejected; event IDs remain 32-character lowercase hexadecimal values.
- A replayed event must match its plan SHA, task ID, study ID, repository ID, horizon and *exact stored* scheduled/expiry timestamps; UTC time and reported lag must agree. An `ok` event cannot be before due or after expiry. `late_observation` and `missed_window` require observation after the frozen expiry.
- `ok` and `late_observation` require HTTP 200, the same immutable repository ID, a canonical GitHub owner/repository name, and nonnegative integer star/fork/issue+PR counters. The API response must explicitly say `"private": false` (JSON boolean), not omit `private` or supply a string/integer: ambiguous visibility becomes `invalid_response`, while `"private": true` becomes `not_public`. Other statuses must not carry success counters. A `missed_window` record must not masquerade as an HTTP request.
- The collector refuses replay if a task contains multiple terminal outcomes, a recorded request occurs after a terminal outcome, or multiple HTTP attempts for one task share the same UTC date. Missingness-only events do not count as HTTP attempts. Symlinked event JSON files are rejected because they are not reliably immutable file artifacts.
- Valid original v1.0 records written by the collector retain the same format. Malformed or manually modified records are **not repaired, deleted, counted as zero, or silently excluded**: the operator must quarantine/investigate the ledger with its original bytes preserved. Recovery requires a documented incident and new, reviewed data version.

**Scope and evidence:** these are local structural consistency guards, not tamper-proof cryptographic signatures. An attacker or operator could still forge a self-consistent unsigned record; official GitHub source authentication, original HTTP logs, actual source access permission, human review, proper time synchronization and external protocol approval remain separate. The offline tests create fictional positive, negative, late, missing, duplicate and damaged events; **no real follow-up collection occurred** in this change.

Run `python -m unittest discover -s tests -v`. Do not treat successful tests as human verification of historical GitHub measurements.


## 2026-10-15 issue #4 completion hardening: fail-closed raw input and safe resume

This is an **engineering-only** correction to the existing version-1 follow-up plan and event collector. It retains the public CLI, stable ID/horizon schedule, event schemas, explicit network consent and original write-once semantics. It does **not** unlock source capture, retroactively approve the cohort, validate research participants or imply real follow-ups have happened.

- **Strict input parsing:** Baseline and frozen plan JSONL, replayed event JSON, and simulated/real REST JSON responses reject duplicate object keys, NaN/Infinity, numeric overflow/underflow and invalid UTF-8 through the shared offline research JSON decoder. Parser error messages for user-controlled data are bounded so private JSON keys are not echoed to the terminal.
- **Bounded reads and file types:** Baseline/plan files are limited to the same **16 MiB** byte limit as the repository's common research validator. Each event JSON is limited to **1 MiB**, with a maximum of **25,000 event files** plus the collector lock. The opened file descriptor is checked as a regular file, and reads stop at limit+1 bytes, catching growth after pre-open metadata. Symlinks and FIFOs are rejected; nonblocking/nofollow flags apply where the platform supports them. This protects **leaf files, not hostile ancestor-directory replacement**.
- **Complete frozen plan contract:** Every repository must have exactly the three **30/90/180-day tasks**, with stable per-repository baseline counters, timestamp, source digest and shared cohort/horizon grace. A self-declared approval flag cannot be upgraded to a claimed authenticated human reviewer by editing a JSON field. Missing/unexpected plan fields are rejected.
- **No invisible ledger entries:** A \`status\` or \`collect\` run fails closed if the event folder is a symlink or contains unrecognized files/directories (including interrupted \`.capture-pending-*\` files), malformed event JSON, duplicate IDs or unrecognized/unsupported task keys. The **one** known \`.followup.lock\` file is tolerated during a running collector, but it cannot be forged as a successful observation.
- **API semantics:** A JSON response with duplicate \`id\`/counter fields or malformed numeric values yields **\`invalid_response\`**, with no accepted star/fork counters. HTTP request totals remain bounded; explicit \`--confirm-network\` is unchanged. None of the adversarial synthetic tests issues a live HTTP request.
- **Operator recovery:** On malformed input or an unexpected temporary file, **stop and preserve the original bytes** for manual incident review. Do not simply delete the offending evidence and continue; if necessary create a new versioned plan or investigated derivation with an explicit provenance crosswalk.

Reproduction from the checkout:

\`\`\`bash
python -m unittest tests.test_longitudinal tests.test_longitudinal_input_integrity -v
python -m unittest discover -s tests -v
python -m trending_study.data_integrity --root .
python scripts/check_research_artifacts.py --root .
\`\`\`

**Scientific validity boundary:** Passing CI establishes only internal schema/replay correctness. Without independently authorized original GitHub Trending captures, actual enrolled baseline timestamps, approved protocol and true 30/90/180-day observations, there is **no observed study cohort, growth estimate, retention estimate, emissions effect or causal result**. Those are separate future fieldwork obligations and must be left incomplete in the roadmap.
