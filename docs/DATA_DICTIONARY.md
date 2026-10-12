# Data dictionary (schema v0.1)

## Trending observation (JSONL, one row per visible occurrence)
| Field | Type | Meaning |
|---|---|---|
| schema_version | string | Record layout version |
| repository | string | Canonical `owner/name` as displayed; mutable across renames |
| trending_url | string | Source page URL |
| source_file | string | Local capture filename |
| source_sha256 | string | SHA-256 hex digest of capture bytes |
| collected_at_utc | string | UTC ISO8601 collection instant |
| observation_date | string | YYYY-MM-DD date of observation; operator-specified |
| window | enum | `daily`, `weekly`, `monthly` |
| rank | integer | Order of parsed entry in captured document (not global GitHub rank) |
| parser_version | string | Parsing implementation version |
| language_filter | string or null | Optional *requested* Trending language filter, not necessarily repo language |

## Repository metadata snapshot (JSONL)
Observation fields retained, plus:
| Field | Type | Meaning |
|---|---|---|
| repository_id | int or null | Stable GitHub repo ID at enrichment time |
| full_name_at_enrichment | string or null | GitHub API full_name (may reflect rename) |
| enriched_at_utc | string | UTC ISO8601 time of API request |
| stars | int or null | Current stargazers_count; **not** historical at observation date |
| forks | int or null | Current forks_count |
| open_issues | int or null | GitHub open_issues_count includes PRs, not a pure issue count |
| primary_language | string or null | GitHub-detected primary language |
| created_at | string or null | GitHub creation timestamp |
| pushed_at | string or null | Latest push timestamp |
| archived | bool or null | GitHub archived state |
| fork | bool or null | Whether fork |
| description | string or null | Public repo description |
| topics | list[string] | Public topic labels |
| metadata_status | string | `ok` or explicit failure code |
| metadata_error | string or null | Safe diagnostic without credentials |

Null = unavailable or uncollected, **not zero**. Raw snapshots should be checksummed. For publication, review GitHub platform requirements and minimize redistribution of individual-level information.

## Future versioned tables
- `repository_features`: ID, effective timestamp, extractor version, each boolean feature plus assessment provenance.
- `followups`: repository ID, scheduled vs actual UTC snapshot dates, counts and status.
- `cohort_membership`: fixed random seed, frame boundaries, inclusion and exclusions.
- `analysis_results`: script SHA, preregistration version, cohort snapshot digest and numerical results.

A file in `data/processed/` does **not** automatically represent a validated dataset of 1,000 repositories.

## Proposed separate AI development sub-study schema — NOT part of public Trending observations
These fields belong to an **opt-in, access-controlled** task dataset and should not be published as row-level identifiable data by default.

| Field | Type | Meaning / validity |
|---|---|---|
| task_id | random pseudonymous ID | Stable within consented study, no GitHub identity embedded |
| project_type | enum/string | CLI/library/app/dataset/research/etc.; applicability |
| new_vs_existing_code | enum | New project vs modification of existing code |
| task_type | enum | Bugfix/feature/docs/refactor/security/etc. |
| treatment_assignment | enum | Randomized AI-allowed/no-AI when feasible, else observational status |
| observed_assistance | enum/null | Verified opt-in workflow record; different from assignment |
| planned_acceptance_sha | SHA/text ID | Frozen before assignment to prevent outcome manipulation |
| task_started_utc, task_closed_utc | ISO8601 | Wall clock, including unfinished tasks |
| human_*_minutes | numeric/null | Planning/prompt/review/repair/shipping/30–90d support; nonoverlap |
| agent_wall_minutes | numeric/null | Report separately; concurrency may overlap human time |
| input_tokens, output_tokens, cached_tokens | int/null | Provider-reported where accessible; not comparable across versions without accounting |
| accepted | bool/null | Independently validated against predeclared criteria |
| failure_severity | enum/null | Predeclared severity rubric, missing distinct from zero |
| independent_user_attempts, independent_user_successes | int/null | Fixed user task & eligible denominator with consent |
| verified_repeat_use | int/null | Only when an auditable consented method exists |
| security_review_state | enum | Passing checks != no vulnerabilities |
| completed_followup_days | int/null | Actual observation exposure and censoring |
| model_and_tool_version | string/null | Only with permission and identifiable-risk assessment |

The offline `examples/idea_card.example.json` is **synthetic** and excluded from any empirical cohort. Its `schema_version=1.0` describes an assessment *input*, not observed research evidence.


## Pilot capture manifest v1.0 (October 2026, separate from legacy observation v0.1)
| Field | Type | Meaning |
|---|---|---|
| schema_version | literal `1.0` | Manifest version, **not** observation-record schema |
| capture_method | `explicit_cli` | Single user-initiated request, not independently signed by GitHub |
| source_url | exact `https://github.com/trending?since=...` | Only unfiltered daily/weekly/monthly currently accepted |
| window / language_filter | enum / null | Time window, language panels **not supported** by this strict implementation |
| capture_date_utc / captured_at_utc | YYYY-MM-DD / UTC ISO8601 | Determined at fetch time and checked for consistency |
| source_sha256 / bytes | string / integer | Integrity of original raw HTML, checked at parse time |
| http_status / content_type | integer / string | Declared source response metadata; HTML and 200 required |
| response_date_header | string/null | Server response Date header when available, not independently authenticated |
| source_file_at_capture | path | Original stored source path, files may be relocated if bytes/hash unchanged |
| provenance_warning | string | Explicit source/clock limitation |

The `pilot-parse` schema `pilot-1.0` additionally records original `captured_at_utc`, `parsed_at_utc`, source manifest path and SHA, resolved rank, `metadata_identity_status=unresolved`, and `eligible_for_confirmatory_cohort=false`. A SHA match proves **local integrity**, not that the page is an authenticated GitHub archive. The legacy `parse-trending` v0.1 now explicitly labels `capture_time_status=unverified_parse_only` and `eligible_for_confirmatory_cohort=false`, even if a user supplies an observation date.

### Pilot study gate schema v1.0
`examples/pilot-preflight.example.json` contains eleven named documentary gates, each with `status=pending|blocked|verified`, `evidence_ref`, `reviewer`, and `reviewed_at_utc`. An entry marked verified without complete source/reviewer metadata is invalid. A complete document returns **ready_for_human_review**, never independent permission, formal preregistration or consent approval. See [SOP](PILOT_CAPTURE_AND_PREFLIGHT.md).

Actual captures, stable IDs, task logs and signed protocols are **not present** in this repository.


## Write-once storage and explicit failure states (implementation note 2026-10-12)

Source captures and parsed/enriched outputs are immutable file artifacts. The write-once publisher rejects existing paths and aliases, stages bytes before publication and never replaces stored observations. A partial raw+manifest pair is a **failed publication**, not a valid captured observation; a future error/attempt ledger must record the missing artifact and correction, not silently hide it. See [capture immutability contract](CAPTURE_IMMUTABILITY_2026_10_12.md). The research data schema and prospective cohort requirements remain unchanged.

## Proposed longitudinal follow-up plan and event schemas (2026-10-12, NOT data)

The standalone, [documented follow-up instrument](LONGITUDINAL_FOLLOWUPS_2026_10_12.md) uses a write-once JSONL plan (`schema_version=followup-plan-1.0`) and individual immutable JSON events (`schema_version=followup-event-1.0`).

| Record | Fields | Meaning and guard |
|---|---|---|
| Baseline input | `repository_id`, `full_name_at_enrichment`, `enriched_at_utc`, `stars`, `source_sha256` | Verified point-in-time metadata baseline, immutable ID and provenance; rejects pilot-ineligible inputs |
| Cohort intent | `study_id`, `protocol_commit`, `cohort_approval_ref`, `eligible_for_confirmatory_cohort` | Self-reported references only; software cannot authenticate actual external approval |
| Schedule | `task_id`, `followup_days`, `grace_days`, `scheduled_at_utc`, `expires_at_utc`, `cohort_input_sha256` | Deterministically derived baseline+horizon and declared window; plan SHA links all event files |
| Event identity | `event_id`, `plan_sha256`, `task_id`, `repository_id`, `observed_at_utc`, `status` | Immutable, strictly scoped event. No matching ID/plan => not accepted |
| API outcome | `http_status`, `api_url`, `full_name_at_followup`, `stars`, `forks`, `open_issues_including_prs`, `observed_repository_id` | Only successful on-time HTTP 200, public and stable-ID match counts as accepted snapshot |
| Rate/quality | `rate_limit_remaining`, `rate_limit_reset_epoch`, `response_date_header`, `lag_seconds` | Header values may be null; timestamp lag must be reported |
| Failure/attrition | `missed_window`, `late_observation`, `not_found_or_private_or_renamed`, `rate_limited`, `identity_mismatch` | Missing is **not** zero, and 404 does not prove deletion |

Counter deltas can be negative. No follow-up in this schema currently constitutes an empirical result.

## Supported-selector completeness diagnostic (2026-10-12, NOT live QA)

Strict pilot audit includes `selector_box_row_count` (number of matched `article.Box-row` elements in the **saved** HTML), `structural_parser_status` (`matched_selector_rows_consistent` or `not_separately_instrumented` when no inspector supplied), and `structural_scope_warning`. Every supported article must contribute exactly one validated, nonduplicate repository and preserve its rank. The original `parser_qa_status` stays `requires_independent_manual_audit`. **Selector coverage is not total visible-page recall.** See [verification plan](PARSER_STRUCTURE_QA_2026_10_12.md).

## Follow-up event replay contract (2026-10-12 hardening; not empirical data)

The published event schema remains `followup-event-1.0` with `event_id` (32 lowercase hexadecimal characters), plan/task/study/ID/horizon keys, exact scheduled and expiry timestamp copies, and one UTC observation timestamp. Only two exhaustive field sets are permitted on replay: **(1)** an API attempt with all declared HTTP/request/counter/header/lag fields, or **(2)** an expired `missed_window` with `reason`, `http_status=null`, and `stars=null`. Unrecognized or partial records fail auditing instead of being labeled successes.

`ok` requires observed time inside the planned window plus HTTP 200, stable ID match, canonical repo name, nonnegative integer counters and an explicit `private=false` boolean from the GitHub API response. A missing/non-boolean `private` field is an invalid response, not proof of a public repository. `late_observation` retains otherwise successful evidence outside expiry but **never counts as on-time completion**. Other HTTP/network/identity statuses cannot carry success counters. A replay may not contain multiple terminal outcomes or two request attempts for the same task on one UTC date. The loader rejects symlinked JSON records. Explicit failures remain in the ledger; no unknown may be silently converted to zero.

These rules check **internal JSON consistency**. They cannot authenticate externally supplied API payloads, human approvals, third-party user consent, real elapsed time or data provenance. See [longitudinal operations and limitations](LONGITUDINAL_FOLLOWUPS_2026_10_12.md).


## Independent page QA report v1.0 (2026-10-12, NOT empirical outcome schema)
A separate offline `audit-pages` source-validation report has `schema_version=1.0`, `evidence_kind=synthetic_fixture|field_self_reported`, `pages[]`, capture manifest SHA/source URL/window/UTC, `reviewer_ids` (pseudonyms), `reviewer_agreement`, `annotation_disagreement_ranks`, per-page `page_status` and `parser_status`, `correct_identity_at_rank`, `gold_rows`, `emitted_rows`, `false_positives_including_rank_errors`, `false_negatives_including_rank_errors`, `precision_on_emitted_rows`, `effective_rank_recall`; and cross-page totals, `coverage_minimum_met`, `automated_documentary_check` and `scientific_status`. Page disagreements produce null scores; rejected pages contribute zero emitted rows and their agreed labels to missed operational coverage. `eligible_for_confirmatory_cohort=false` **always**. Note that QA counts use exact *rank AND identity*, not independent unique repository IDs or overall Github prevalence. See [definitions and limitations](INDEPENDENT_PAGE_AUDIT_2026_10_12.md).
