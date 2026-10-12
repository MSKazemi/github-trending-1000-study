# Pilot and confirmatory protocol gate status — 2026-10-12

**Actual status:** preparation / methods implementation; **NOT ready** for confirmatory enrollment. Do not infer a scheduled data collection or completed 1,000-repository sample. This document is a dated qualitative reading of repository evidence, **not a completed independent audit** or a verified checklist filed by reviewers.

## What was implemented in the feature PR
- A SHA-256 + UTC capture manifest emitted by one explicitly invoked GitHub Trending `capture` request, with source/HTTP metadata recorded at collection time.
- A strict `pilot-parse` validator that checks raw bytes against the recorded manifest and preserves capture time separate from parse time; outputs flagged as **not enrolled**.
- An example preflight manifest with every item **pending** and a `pilot-preflight` command that fails when a strict `--require-ready` is requested.
- Offline synthetic tests for checksum tampering, inconsistent dates, unsupported filters, source URL spoofing, legacy parse-only labeling and documentary review gates.

## Required scientific gates — currently unresolved

| Gate | Evidence needed before mark verified | Status |
|---|---|---|
| source_access_review | reviewed access rules / Terms for intended capture cadence | **Pending** |
| capture_schedule | actual UTC surface/frequency plan and permitted access | **Pending** |
| capture_manifest_instrumented | source code + CI + human on-source instrument check | **Pending human verification** |
| parser_audit | real rendered/raw page review of >=30 entries across supported surfaces | **Pending** |
| stable_identity_resolution | verified numeric GitHub repository IDs/dedup and missing reason | **Pending** |
| independent_task_frame | frozen independent tasks that do not select on discovered solution | **Pending** |
| task_acceptance_freeze | independent tests and blinded adjudicator instructions | **Pending** |
| sample_size_power | pilot-derived uncertainty, realistic N and detectable effect | **Pending** |
| privacy_consent | authorized human task logs, retention and rights/ethics checks | **Pending** |
| preregistration | timestamped signed immutable plan; external record where appropriate | **Pending** |
| independent_methods_review | named qualified reviewer consent and dated signature | **Pending** |

## What cannot be claimed yet
- The pilot was performed, the 9-surface panel is implemented or recurring capture permitted.
- 1,000 unique Trending repositories have been observed/verified.
- Any agent/SEO/reuse feature **causes** GitHub Trending appearance or sustained adoption.
- A human-task randomized experiment was run or its outcomes are reliable.
- Fewer tokens or duplicate lines produced environmental savings.
- The proposed 2026-11-01 enrollment date is frozen; it can be amended if gates remain blocked.

## Next actual actions and owners needed
1. Human reviewer checks legal/platform source access and defines permitted scope.
2. Collect one permitted source page after an explicit request, verify parser against it; audit >=30 real rows.
3. Implement permitted multi-surface provenance and numeric GitHub IDs with resilient failure logging (issues #2 and #4).
4. Recruit independent gold-label and statistics reviewers (issues #21 and #27); define task frame and sample simulation (issue #3).
5. Freeze an approved pilot-adapted protocol and registration **before** treating any capture as inferential enrollment.
6. If it cannot be done before November 1, revise the schedule in a dated amendment, not a post-hoc backfill.

See [pilot commands](PILOT_CAPTURE_AND_PREFLIGHT.md), [draft protocol](PREREGISTRATION_DRAFT_2027.md), [project issue #27](https://github.com/MSKazemi/github-trending-1000-study/issues/27).


## 2026-10-12 addendum — independent QA tool exists, genuine parser-audit gate still pending

The repository now has `trending_study/page_audit.py` and a `audit-pages` CLI for checking two blind, complete-page lists against a saved GitHub Trending manifest and computing TP/FP/FN (including parser rejection). **No real source capture or independent human 30-row audit occurred** in the current implementation session. Existing sample, access and consent gates stay pending; a passing synthetic 36-row test is not empirical source verification. [Detailed QA procedure](INDEPENDENT_PAGE_AUDIT_2026_10_12.md).
