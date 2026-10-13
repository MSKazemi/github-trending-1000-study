# Hiring intelligence: longitudinal data and coding protocol (proposal v0.1)

**2026-10-13 | Status: proposed, not preregistered | Related issues:** #222, #223, #224.

## Unit and frame
- Unit A: an **individual public requisition** (stable employer/job-board ID where possible), not an observed location or reposting URL.
- Unit B: a *requisition-observation* at an actual recorded UTC time, including an explicit access outcome. Do not infer a historical posting date from the first time this study found the ad.
- Unit C: an optional company-period panel, only after the company source frame, collection exposure and corporate parent identity are frozen. Never treat a curated 18-row sample as a denominator of all jobs.
- Candidate set: official employers' careers pages/linked authorized applicant tracking systems; no staff identities, resumes, personal applicant information, restricted APIs or unauthorized scraping.

## Prospectively required observations
`observation_id,source_query,source_index_url,requisition_id,canonical_url,company_id,parent_company_id,job_title,team,location,source_status,observed_at_utc,posted_at_utc_if_explicit,posting_date_basis,content_hash_if_permitted,content_access_level,source_restrictions_checked,job_description_verified,analyst_id,review_status`.

Distinguish `listed_live` (official individual page actually retrieved), `index_only`, `indexed_text_only`, `inaccessible`, `not_listed_in_bounded_search`, `removed_or_redirected`, and `identity_conflict`. A role disappearing is **not** proof of being filled. A 403, ATS error or search miss is **not** zero employment or closure. Record missing value as null and why missing; do not convert to zero. Only quote an explicit company posting date if visible.

## Time and de-duplication
1. Create versioned write-once observation records, not mutable one-row-per-requisition histories. Track actual UTC access time at retrieval, no backdated baseline.
2. Exact employer requisition ID+company is default candidate identity; investigate identical titles/location variants and reused IDs manually. Keep a canonicalization crosswalk and unresolved collisions.
3. Record transitions as **observed source changes**; infer neither hiring nor recruitment speed. Observe censoring and errors, preserve unsuccessful attempts in exposure denominator.
4. Never poll a site until its access rules have been reviewed and a bounded cadence approved. No credential bypass, scraping of restricted pages or full copyrighted descriptions in public datasets.

## Coding taxonomy v0.1 (not validated)
Labels (multilabel allowed): `agent_harness`, `sandbox_security`, `agent_evaluation`, `model_training_rl`, `long_horizon_memory`, `code_search_reuse`, `enterprise_identity_governance`, `integration_developer_tools`, `inference_cost_efficiency`, `agent_observability_operations`, `other`, `insufficient_evidence`.

For each role, assign categories based on *explicit responsibilities*, not just title or analyst inference; retain short evidence paraphrase and corresponding source section. A title-only lead gets `insufficient_evidence` for responsibility coding. Exclude identity-conflict and inaccessible records from thematic inference until adjudication. It is valid for a job to receive multiple labels or no substantive label.

## Independent coding design
Freeze both a source list and versioned codebook before coding. Two **actually independent human coders** read permissible source material without seeing each other's labels, then a third reviewer adjudicates disagreements against documented rubrics. For multilabel codes, report per-label confusion tables and agreement (Cohen kappa with prevalence/imbalance disclosed); macro summaries only with eligible denominators. Preserve original non-adjudicated labels, role omissions and disagreement records. Do not fabricate coders or inter-rater agreement from an LLM's outputs. Stratify by firm/source-access to avoid overrepresenting a single company.

## Triangulation design
For every coded hiring theme, form a testable dated record with (1) role evidence and when actually observed; (2) separately dated product/release or public code artifact; (3) independent test/evaluation, if possible; (4) contradiction or no match; and (5) conditional 2027–2031 prediction and falsifier. **A vendor release is neither proof of hiring causation nor independent confirmation that a described agent works.** Avoid post-hoc selection of only themes that subsequently shipped. Track negative cases and time windows.

## Four practical questions for reusable-software research
- Do agents discover and incorporate suitable existing packages more often when given an explicit repository search interface and license/security checks?
- Does a constrained execution harness improve independent task correctness per total human review hour on matched tasks?
- Do published, reproducible task evaluations predict independent downstream integration, rather than just developer attention?
- Can portable task/context contracts reduce repeated agent reimplementation across repositories without higher lifecycle costs?

Each is a *hypothesis*, not a result. Freeze tasks, acceptance criteria, sample eligibility, tool versions and analysis before collecting outcomes; separate successful reuse from textual similarity. Follow the existing [reuse-first protocol](REUSE_FIRST_EXPERIMENT.md), [ethics](ETHICS.md), [company intelligence method](COMPANY_INTELLIGENCE_METHOD_2026_10.md) and [evidence grading](EVIDENCE_TO_LESSON_PROTOCOL.md).

## Publication gate
No claims of representativeness or company rankings from raw role counts. Publish exposure log, missingness by company and date, de-duplication review, source-permission decision, independent coding results, genuine longitudinal records and a preregistered inferential analysis separately. Current pilot has *none* of the evidence needed to claim trends in job counts or impact on engineering value.
