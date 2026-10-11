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
