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

## Resuming from an event ledger: fail-closed acceptance (2026-10-12 correction)

Previously, an `ok` label in a syntactically valid event file could be counted as a completed 30/90/180-day observation even if that file omitted response counters/identity or placed the observation outside its permitted time window. An immutable filename and a matching plan digest alone cannot establish that a snapshot is usable.

The offline `status` and opt-in `collect` reader now **reject the entire inconsistent event ledger** before treating any event as a valid observation:

- Every event must match the frozen plan's study ID, due timestamp, expiry timestamp, repository ID and horizon; status names and UTC timestamps are checked.
- A completed `ok` requires observation **between due and expiry**, HTTP 200, exact expected numeric repository ID, safe repository name and nonnegative integer stars/forks/open-issues-including-PRs. GitHub's public/private field must be an explicit JSON boolean in the API response; missing or malformed visibility becomes `invalid_response`, not an accepted public snapshot.
- A late HTTP 200 with verified counters is labeled `late_observation` **only after expiry** and is never counted as completed. `missed_window` must be recorded only after expiry without fabricated HTTP status or counters. Error states cannot carry apparent successful counters.
- API URLs must have the official `https://api.github.com/repos/owner/repo` shape; `lag_seconds` must agree with recorded UTC times. Any malformed event requires **inspection and documented incident handling**; do not delete or edit source evidence merely to make the validator pass.

Example: after writing an authorized event, inspect the local ledger without network requests:

```bash
python -m trending_study.longitudinal status \
  --plan /path/to/frozen-plan.jsonl \
  --events-dir /path/to/immutable-events
```

This is **consistency validation, not authenticated GitHub response proof**. Someone could still construct a plausible matching ledger manually. Independently verify capture and API provenance, permissions and approval before using any record in confirmatory analysis. Existing historical/nonconforming events must be preserved and reviewed rather than silently rewritten or automatically upgraded.

**Provenance limitation:** file hashes and self-declared approval references cannot prove GitHub served the payload, that the cohort was registered, or that a public repo ID remained available after transfer. API availability and client timestamps have clock/network error. Latency, censoring, missingness, inaccessible transitions, and interrupted runs must be analyzed; do not drop failed repos from denominators.

## Offline tests and study status

```bash
python -m unittest discover -s tests -v
```

Unit tests use synthetic, clearly marked baselines and mocked API responses for stable IDs, renames, identity mismatch, rate limiting, interrupted/missed windows, immutability, safe resume and CLI planning. They do not prove experimental scientific validity or capture completeness.

**Next scientific dependencies:** #2 real-page independent rank/completeness audit and access permission; #3 verified sampling/power; #21 externally adjudicated reuse tasks; reviewer-signed consolidated protocol. See [integrated mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
