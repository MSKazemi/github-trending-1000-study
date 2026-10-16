# Hiring posting longitudinal protocol — draft v0.1 (#222)

**Status:** prospective methods proposal, NOT an observed longitudinal panel or authorized automated crawl. Baseline initial pilot: [source audit](../references/ai_hiring_job_leads_source_audit_2026-10-13.csv). Enrollment and observation permissions must be approved before automated monitoring.

## Research unit and identifiers
The main analytic unit is a **unique employer requisition**, not a URL, location option, city, or extracted search result. Keep both `raw_listing_id` (source-page identity) and `requisition_id` (the company's stable ID where provided). Maintain an explicit uncertain identity group if no stable ID is available. Record parent company and operating team separately. URL changes and aliases must not manufacture newly hired people. The original source row must remain traceable.

## Append-only observations
Suggested schema: `schema_version,observation_id,source_id,company_id,parent_id,requisition_id,listing_variant_id,canonical_url,observed_at_utc,observed_status,posting_date_explicit,posting_date_precision,last_modified_explicit,source_access_status,http_status_if_authorized,collection_method,content_digest_if_permitted,source_verification,provenance_note,codebook_version,analyst_id_pseudonym`. All `observed_at_utc` timestamps are recorded at actual observation, not imputed. A digest is local integrity evidence, not proof of the provider's version.

Allowed `observed_status`: `listed` (official source presents job); `not_listed_in_complete_checked_index` (only after a documented complete permitted index); `not_found_single_url` (unconfirmed); `closed_explicit` (employer directly declares); `redirected`; `inaccessible`; `unknown`. **Do not interpret `not_found_single_url` as filled or closed.** A search index snippet cannot establish `listed` on a live date.

## Time and censoring
First observed is *first captured by researchers*, not first posted; last observed is not job close date. Closure is an interval-censored event unless the employer supplies a precise timestamp. Reopened/reposted: preserve original and new requisition IDs and link them with reviewed relationship `same_requisition` / `new_requisition` / `uncertain`. Requisitions still listed at study end are right-censored, not failures; inaccessible sites are missing, not zeros.

## QA and permissions
1. Review source Terms, robots, allowed endpoints, licensing and retention policy. Prefer official APIs, voluntary hand curation or provider-exported listings. Do not bypass access controls or schedule crawling by default.
2. Freeze a company/site/source-frame and query plan including an explicit unsuccessful-query log. Pilot using a small number of permitted sources. Record UTC, query and date precision.
3. Validate exact fields (ISO8601 UTC, enum membership, duplicate observation IDs, monotone per-source captures, source URLs); preserve rejected observations with reason. Snapshot any retained external content only after rights review; store paraphrases otherwise.
4. Two independent researchers manually audit a prespecified sample against official links, company identity, requisition linkage and censorship status. Reconcile and publish a correction log.
5. Report attempted pages, accessible pages, explicit closings, broken/missing pages, unique requisitions, duplicates, selection gaps and censoring by company; no estimates of filled seats from disappearing ads.
6. Never apply historical visibility to jobs listed only after the pilot. Source uncertainty is not model input imputed as zero.

## Proposed scientific analysis
A descriptive company-time panel could compare **predeclared proportions of *observed roles*** by category with uncertainty, adjustment for company scope, location, collection intensity, site redesign, and recruitment cycles. Raw job counts are **not** hiring budgets or headcount growth. Without a known complete sample frame, publish only qualitative purposive-source findings. Product predictions require independent time-stamped product/release confirmation.

## Exit gates
Protocol/rights approval, pilot source capture, validation test fixtures, identity adjudication, independent reviewer QA, source accessibility audit and prespecified company-frame coverage all remain **pending**. No human review or benchmark was performed merely by writing this protocol.


## 2026-10-16: explicit-only interval-censored closure evidence (issue #222)

The read-only offline `trending_study.hiring_observations` derives two additive output fields per requisition:

- `closure_interval_last_listed_at_utc`: latest independently **claimed** observed live-listing timestamp before the final explicit employer closed signal (if there is one), or null if the role was already marked closed when first observed.
- `closure_interval_first_explicitly_closed_at_utc`: first **claimed** employer-explicit closure observation after the final live listing, or null if the last informative state was not explicitly closed.

These endpoints bound a **reported observation interval**, not a precise actual position close date. Status `inaccessible`, `removed_or_redirected`, `index_only`, `not_listed_in_bounded_search` and an HTTP failure remain *missingness/censoring*, never actual closure. Reopening resets the interval when a later genuinely listed observation occurs; a later explicit closure is analyzed against that last listed date, not an earlier closure. `actual_closure_at_utc` and `filled_positions` remain **null unconditionally**, and access/ethics/independent-review flags remain false.

Public employer/source URL metadata now rejects literal localhost, `.local`, `.internal` and non-global IP hosts before analysis. This is not DNS verification or authorization to scrape; future source collection requires formal permission and safe source allowlisting. The synthetic `example.invalid` documentation fixture remains supported for offline reproducibility.

**Reproduce:** `python -m unittest tests.test_hiring_closure_interval -v` and `python -m unittest discover -s tests -v`. Test cases cover explicit closure intervals, inferred unknown lower bounds, inaccessible/disappeared sources, reopening and later reclosure, nonpublic hosts and false-independent-review safeguards.

**Still required before issue #222 closure:** approved source rights and retention/ethics processes under #220; an actual prospective, bounded permitted and date-stamped panel; human-checked requisition and location identities; true source captures/provenance; independent methods reviewer and observed changes with censoring/attrition reporting. The software's claimed employer status is **not authenticated** by a unit test. Do not call a vacancy filled because its public listing disappeared.

**Practical repository lesson:** when tracking vendors, GitHub issues, package versions or jobs, model first/last **observed** time separately from the real event date. Never turn a missing webpage into a positive outcome or backfill historical states from current metadata.
