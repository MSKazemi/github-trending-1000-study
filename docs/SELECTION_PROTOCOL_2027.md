# Repository eligibility, sampling, controls and selection — draft v0.2

**As-of:** 2026-10-11. **Research target:** evidence-based guidance for 2027. **Status:** proposal, NOT preregistered, no empirical cohort sampled. This document supersedes the approximate 12-week recruitment window in earlier drafts once the protocol is frozen; record the change in the decision ledger.

## The critical separation

1. **Eligibility and sampling:** Which repos are observed, included, and analyzed? Must be determined before observing their future outcomes.
2. **Exposure:** Was a repository seen on the *captured* GitHub Trending page? Did a verified coding-agent trace appear? Neither is a quality label.
3. **Predictors/confounders:** Age, past growth, language, project type, baseline star count, maintainer type, repo maturity, past releases and exposure channels.
4. **Outcomes:** Verified user-task benefit, 30/90/180-day growth, support quality, maintenance cost, independently attributable integration. **Never select the main cohort using future outcomes.**

Do not filter the 1,000 down to repositories with AGENTS.md, >100 stars, flashy READMEs or apparent success. That would make the question circular.

## Primary recruitment protocol (prospective)
- **Pilot:** 2026-10-15 through 2026-10-31 (17 UTC dates); *not included* in confirmatory cohort or statistical outcomes.
- **Primary enrollment:** **2026-11-01 through 2027-04-30** (181 UTC dates). Six months balances seasonality against feasibility and allows last +180-day assessments in October 2027. This is a **budget and feasibility hypothesis**, not a power-optimized period. Pilot may force a versioned change before enrollment.
- **Observation surfaces:** three unfiltered global pages per collection date (daily, weekly, monthly) and six prespecified **daily** language pages (Python, TypeScript, JavaScript, Go, Rust, Java): **nine configured surfaces per day** if access is permitted. Chosen as a deliberate multilingual panel, not a probability sample of all languages. Publish exact URLs and HTTP/robots/access review. No aggressive automatic scraping without permission.
- **Capture schedule:** one specified UTC time each day for the eligible pages, with actual timestamps, failed captures and downtime preserved. Daily sampling does NOT record every hourly Trending appearance; flag interval-censoring. Weekly/monthly views overlap temporally; **do not count as independent daily samples**.
- **Eligible trending appearance:** an actual parsed repository row on a saved, validated, dated public GitHub Trending capture. Include **all** displayed rows from the sampled surfaces; do not rank-pick. Retain page length, displayed rank and source window. A row on a stale capture is not a current observation.
- **Unique eligible repository:** first verified public appearance during main enrollment, reconciled to an immutable numeric GitHub repository ID. If API temporarily fails, keep an unresolved pending row; do NOT silently replace it. If later deleted/private, retain record and attrition reason. Mirrors, forks, archived and non-executable curated lists are **flagged and stratified**, not retrospectively dropped.
- **Primary target:** **1,000 unique observed trending repositories**. Capture the *full* eligible frame with provenance and baseline metadata at first sight. If >1,000, draw exactly 1,000 with a preregistered fixed pseudorandom seed and proportional allocation across enrollment month × first-observation source panel, without seeing any future outcome or agent evidence; retain inclusion probabilities. For less than 1,000, publish the true N and perform pilot-based design reassessment **before** analyzing results.
- **Project types:** library / end-user application / CLI / developer framework / dataset / research artifact / educational example / curated list / infrastructure / template / other. A usefulness measure valid for a CLI may be not-applicable for a list.
- **Selection metrics:** date and source-page eligibility, numeric repository ID, target quota and prespecified month × source-panel stratum. Baseline stars/age/language/type are **matching/confounding features**, not minimum popularity gates. **Agent trace status is NOT a primary inclusion gate.**

## Control cohort (independent, not 'definitely never trending')
- Target **1,000 other public repositories** selected from a **documented candidate frame** (e.g. predeclared GH Archive event-based candidate generator plus official API verification), aligned with primary cohort first-observation calendar weeks. The REST search API is capped at 1,000 returns per query and relevance-ranked: it is NOT uniform GitHub sampling.
- Sample controls **before** checking subsequent outcomes, with stable IDs, reproducible segmentation/seed, eligibility ledger and full probability/coverage caveats.
- Match on *pre-observation* language, project type, creation-age bins, log(1+baseline stars), age-adjusted activity and week; test common support and standardized differences; distinguish exploratory matched contrasts from causal estimates.
- 'Not seen trending in our captures' is a precise label; **not** 'never trended'. Mark crossover if a control is subsequently observed on selected Trending pages, and conduct treatment/exposure sensitivity analysis.
- Do not classify control projects lacking agent traces as verified human-only; treat as **unknown AI usage**.

## Agent enrichment — separate from main probability sample
For reliable agent adoption comparisons, create a **nested, explicitly non-representative audit/oversample** of repositories with high-confidence agent traces, supplemented by documentation-only and no-detected-trace strata. Oversampling improves qualitative/predictive precision but any reported population prevalence must use appropriate weights and detection-sensitivity bounds. A separate **opt-in** task/user study collects directly confirmed agent use and genuine end-user outcomes; no observational public proxy can replace this.

## Historical comparison: include OLD GitHub projects
- 2024-01-01–2025-02-23: **pre-2025 wave reference**, **NOT 'no AI'** (Copilot, Cursor, Aider and other tools already existed).
- 2025-02-24–2025-09-30: early agent availability (Claude Code Feb 24; Codex CLI April, cloud May 16; Copilot coding agent May 19).
- 2025-10-01–2026-09-30: scaling/maturing (Codex GA Oct 6, 2025; desktop Feb 2, 2026). Window boundary is **calendar convenience**, not universal launch or treatment date.
- 2026-10-01–2026-10-31: prospective instrumentation/pilot period; pilot captures not inferential cohort.
- 2026-11-01–2027-04-30: contemporary recruited cohort.
- Through 2027-10-27: nominal last +180d observation for April 30 recruits; account for actual timestamps and leap/calendar arithmetic using datetime, not assuming months are 30 days. Final analysis late 2027.

Use GH Archive for available historical GitHub **events** (with dataset coverage limits), historic commit tree, and independent archival snapshots when they can be verified. GH Archive **does not** archive the GitHub Trending ranking pages. You cannot reconstruct historical Trending ranks just by counting old WatchEvents. Avoid historical star baselines reconstructed from **current** star totals.

## Sample size and power
1,000+1,000 is a **feasibility target**. The two-week pilot estimates unique capture yield, agent trace prevalence/precision, attrition, distribution tails and stratification overlap. Simulate statistical power, minimum detectable effect, uncertainty intervals and interactions **before** confirming N. If verified agent-positive prevalence is low, a separate powered nested study may need more observations; do not pretend 1,000 guarantees per-agent-category inference.

## Validation and auditing
- Pre-register panels/time/codes/eligibility and selection seed; publish every missed capture and discarded page.
- Double-review >=30 sampled page rows to measure capture precision/recall; additionally audit ambiguous repos/type. Repeat when page HTML changes.
- Dedupe using immutable GitHub ID, track renames/transfers, forks, private transitions and missingness.
- Publish a STROBE-style flow diagram and 95% intervals for rates, stratified N and inclusion probability; null/ineligible cannot be coded zero.
- For inferential comparisons, adjust for baseline traits with overlap checks, use chronological holdout, repository-clustered uncertainty and sensitivity to missingness/selection. **Trending creates collider/selection bias.**
- The final 2027 advice must be conditional on independently validated user value and lifecycle costs, not merely popularity or activity.

**Primary sources:** [launch and evidence timeline](AGENT_RELEASE_ADOPTION_TIMELINE.md), [metric register](METRIC_REGISTER_2027.md), [agent measurement](AGENT_ADOPTION_MEASUREMENT.md), [reading list](READING_LIST_2027.md).


## Collector-to-design gap (2026-10-12, NOT YET RESOLVED)
This proposed 9-surface daily panel is **not** presently implemented. The first strict pilot parser intentionally handles only the three unfiltered global `/trending?since=daily|weekly|monthly` pages and requires a matching capture-time SHA/UTC manifest; it does **not** verify six language-filtered pages or recurring access policies. Until those filters, permissions and human QA exist, no capture may be called part of the full planned frame. Original `parse-trending` has no verified capture time; it cannot satisfy this protocol's prospective first-exposure timestamp. If full-scope data collection or pilot power is not achievable by November 1, revise the actual start and register an amendment. [Detailed SOP](PILOT_CAPTURE_AND_PREFLIGHT.md), [unfrozen design](PREREGISTRATION_DRAFT_2027.md).
