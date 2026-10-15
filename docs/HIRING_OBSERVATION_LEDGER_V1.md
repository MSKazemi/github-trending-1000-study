# Issue #222: offline requisition observation ledger v1.0

**2026-10-14 — proposed, unapproved instrument; no live collection.** Implements the structural observation requirements in [the longitudinal proposal](HIRING_INTELLIGENCE_LONGITUDINAL_AND_CODEBOOK.md) and [the draft requisition protocol](HIRING_LONGITUDINAL_PROTOCOL_2026-10-13.md), dependent on issue #220. It does not replace either proposal, choose a company sample, authorize an observation cadence, change causal hypotheses, apply an annotation codebook or certify hiring evidence. All committed events are synthetic.

The practical task is to check a supplied, append-only event ledger and retain every attempted observation, including errors, before a human considers longitudinal inference. Frozen acceptance requires actual UTC/access-time consistency, bounded prospective windows, employer/requisition identity with distinct location variants, all revisions, explicit uncertain linkage, missingness/censoring, strict private-field rejection, bounded reads and write-once reports. Actual source-access and methodological approval are external prerequisites; neither an agent nor this validator grants them.

```bash
python -m trending_study.hiring_observations \
  --input examples/hiring_observations.synthetic.json \
  --output /tmp/hiring-observation-report-new-attempt.json
python -m unittest discover -s tests -p test_hiring_observations.py -v
python -m unittest discover -s tests -v
```

Python 3.10+; standard library only. Choose a new output path for each attempt. The CLI never retrieves URLs, schedules monitoring, opens external evidence references, installs software or processes applicant data. Input is capped at the shared 16 MiB research limit; regular files only, descriptor `O_NOFOLLOW`/`O_NONBLOCK` opening, `fstat` verification and a bound on actual read bytes. Unsupported secure-opening platforms fail closed. Duplicate JSON keys, NaN/Infinity, numeric overflow/underflow and invalid UTF-8 fail before publication; decoder/private-key diagnostics are redacted. Input/output aliases and existing outputs are rejected through the existing write-once publisher. The protection applies to final-component symlinks; parent-directory trust and content authenticity are external responsibilities.

## Versioned input dictionary

`schema_version = hiring-observations-1.0`. Every object has **exactly** the documented fields. Extra fields, including applicant contacts, resumes, employee names, raw descriptions, private tokens, personal analyst IDs and alleged approval booleans, are rejected without echoing their names. IDs and evidence references are bounded opaque ASCII tokens (`[A-Za-z0-9][A-Za-z0-9_-]{0,79}`); do not put personal identifiers or secret values in them.

| Object | Fields | Contract |
| --- | --- | --- |
| Root | `schema_version`, `dataset_kind` | Version above; kind `synthetic` or `self_reported_unverified`; neither authenticates observations |
| Root | `declared_at_utc`, `study_start_utc`, `study_end_utc`, `analysis_as_of_utc` | Explicit UTC; declaration ≤ start ≤ analysis ≤ actual current UTC; end ≥ start; proposed window ≤366 days; end may be future because it is a plan |
| Root | `sources`, `observations` | 1–50 declared sources; 1–10,000 chronologically ordered observation attempts; resource bounds, not sampling rules |
| Source | `source_id`, `employer_id`, `index_url`, `listing_host`, `access_review_status` | Unique opaque source ID and source index URL; declared employer; canonical HTTPS index and listing host; access review must remain `pending` in this unapproved instrument |
| Observation | `observation_id`, `source_id`, `employer_id`, `requisition_id`, `location_variant_id`, `canonical_url` | Unique event ID; source must match employer/host; candidate identity is employer + requisition; location variants never manufacture additional requisitions |
| Observation | `observed_at_utc`, `accessed_at_utc`, `recorded_at_utc` | Observation equals actual *declared* access timestamp; within study window and analysis cutoff; recorded between access and access+5 minutes, never beyond analysis/current UTC |
| Observation | `source_status`, `http_status`, `content_sha256`, `missing_reason` | Enumerated source outcome below; HTTP integer 100–599 or null; permitted content checksum lowercase SHA256 or null; missing is explicit, never a fabricated zero |
| Observation | `closure_evidence_ref` | Non-null only for `explicitly_closed`; opaque reference to purported explicit employer closure evidence, not an authenticated review |
| Observation | `posted_at_utc`, `posting_date_basis` | Null + `unknown`, or explicit UTC date ≤ observed timestamp + `explicit_employer`; never substitute first-observed or today's date |
| Observation | `relation_kind`, `linkage_status`, `linked_requisition_id`, `link_evidence_ref` | `none`/`none`/null/null; or `reopening`/`reposting` with `known` + evidence or `unconfirmed` + null evidence; target must be an earlier observed requisition of same employer |

Source URLs reject credentials, fragments, insecure schemes, host-case aliases, escaped paths, trailing-slash aliases and traversal. Only bounded opaque `gh_jid`, `jid`, `job_id`, `requisition_id` query values are accepted, in sorted unique-key order. Tracking/authentication query parameters are not allowed. Query-free URLs are accepted without passing an empty string to Python 3.10's strict query parser; nonempty queries retain strict validation, and an empty trailing `?` or malformed separator is still rejected. This deliberately narrow representation may require a separately reviewed schema extension for additional ATS URL formats; do not strip meaningful source identity silently.

### Source status and missingness

| `source_status` | Requirements and interpretation |
| --- | --- |
| `listed_live` | Declared individual-page access, HTTP 200, permitted digest, missing reason null; source authenticity is not proved |
| `explicitly_closed` | HTTP 200, digest, missing reason null and explicit employer closure reference; not a filled position or an exact closure time |
| `index_only`, `indexed_text_only` | Missing reason `index_only`; not a verified live individual page |
| `inaccessible` | Missing reason `content_unavailable`; HTTP 200 is contradictory; HTTP null preserves unknown access outcome |
| `not_listed_in_bounded_search` | Missing reason `search_miss`; says nothing about completeness of source index or whether a job closed |
| `removed_or_redirected` | Missing reason `redirect`; not filled, closed or hired |
| `identity_conflict` | Missing reason `identity_unresolved`; quarantined source identity, no live observation or eligibility inference |

Duplicate event IDs, source aliases, employer/host mismatches, shared listing URLs assigned to different employer/requisition keys and duplicate same-instant requisition/location attempts fail. Source IDs are declarations, not authenticated employer or board identities. A source with no attempts remains in the source-level exposure report with an actual **event count** of zero, which is not a job count or a measured hiring outcome.

A `reopening` must refer to the same requisition whose **latest informative state** is explicitly closed and have a new `listed_live` observation. An old closure cannot justify another reopening label while the requisition is already known live. Return to live after closure requires such a record even if inaccessible attempts intervened. `reposting` must retain a distinct new requisition ID and reference an earlier same-employer requisition; it never merges histories. `known` means documented **as submitted**, not independently verified linkage. Unconfirmed linkages remain unconfirmed. Contradictory simultaneous location observations about requisition-wide explicit closure fail.

## Output dictionary and interpretation

The report retains the input canonical SHA256, dataset kind, total attempted events, `unique_requisition_keys` (declared identities, not independently verified real requisitions), `missing_attempts`, a `by_source` exposure/missingness report and one complete history per employer/requisition key.

Each history retains all original observation records, distinct `location_variant_ids`, first/last **attempt** timestamps, first/last **listed-page observation** timestamps or null, latest observed source status, attempt/missing counts and `status_or_content_revision_count`. Revisions compare successive observations **within the same location variant**; translated/location-specific digests are not automatically treated as revisions of another variant.

`right_censored=true` when the latest informative event is live, with `censoring_at_utc` equal to that actual last live observation. It does **not** assume a job stayed live through missing attempts or the study end. `right_censored=false` means an explicit employer closure was observed and no later live reopening exists; `actual_closure_at_utc` still remains null because observation time is not the closure's actual time. `right_censored=null` means no live/explicit-closure observation exists. `observation_window_end_utc` preserves the earlier of planned end and analysis cutoff independently of censoring time. `filled_positions` always remains null.

`independent_verification`, `source_access_approved`, `human_methods_approved`, and `eligible_for_confirmatory_cohort` always remain **false**. Green software tests are not authentication of people, source rights, source clock, prospective freezing, posted dates, chronology or empirical outcomes. Syntactically consistent fabricated records can still pass. The five-minute recording bound blocks declared retrospective reconstruction, but it cannot prove the timestamps were actually recorded then. Preserve externally reviewed original evidence and append every prior event to a new ledger version; without an independently retained previous ledger the validator cannot detect omitted history.

## Reuse and remaining gates

Time-boxed repository search on 2026-10-14 inspected `longitudinal`, `task_intake`, `lesson_registry`, `data_integrity`, `safe_io` and their tests. Reuse `task_intake.utc` (strict UTC), `data_integrity.decode_research_json` (JSON ambiguity safeguards), and `safe_io.disjoint/publish_json` (write-once publication); the descriptor pattern is consistent with `lesson_registry.audit_file`. The GitHub follow-up scheduler has repository-count/approved-cohort semantics and network calls, so it cannot safely model this offline requisition contract. The MIT repository's standard-library components meet these narrow needs without new dependencies; external discovery was restricted to Python's documented standard-library APIs and no claim of exhaustive package search is made. Relevant docs: [datetime](https://docs.python.org/3/library/datetime.html), [os.open](https://docs.python.org/3/library/os.html#os.open), [JSON](https://docs.python.org/3/library/json.html).

Before real prospective use, issue #220's company/source frame, official identity and URL mapping, current source Terms/robots/access/retention review, permitted observation cadence, independent human full-page QA, privacy/rights review and dated methods sign-off remain required. Broad company coverage, ambiguous-ID adjudication, collection failures, historical posting dates, hiring decisions and any causal/representative interpretation remain unvalidated. Issue #222's software contribution does not complete those empirical gates. AI assistance is disclosed; no human reviewers or live observations were simulated as real evidence.

## 2026-10-15 follow-up: CLI path redaction on failure

A focused code inspection of the existing prospective validator found that `argparse` could echo filesystem exception text for a missing input or existing write-once output, including full local paths and a synthetic private-looking filename. The command now reports a generic input/output failure for `OSError` and the existing shared `ProvenanceWriteError`, rather than exposing path details. The new synthetic regression checks a missing input and an existing protected destination and verifies both non-disclosure and unchanged existing bytes.

This improves diagnostics only: no source is accessed, vacancy state inferred, participant enrolled or historical posting date backfilled. Exact-head CI and independent methods/rights review remain separate gates before this PR is merged or #222 is called scientifically complete.
