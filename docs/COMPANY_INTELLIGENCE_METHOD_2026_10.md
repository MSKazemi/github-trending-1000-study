# Company-intelligence research protocol: 100 AI software ecosystem organizations

**Protocol status:** draft / research tasks not completed. **Defined on:** 2026-10-12 (Europe/Rome). **Retrospective research window:** 2026-04-12 through 2026-10-12 inclusive, UTC dates (date filters should include final day). **Population:** editorial 100-entry [industry watchlist](AI_SOFTWARE_COMPANIES_100_WATCHLIST_2026-10-12.md), not a probability sample of companies, repositories or product users. An entry may be a subsidiary, formerly independent company, operating team or product brand; do not use it to count independent companies.

**Linked initiatives:** [#56 – 1,000-item evidence corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56); [#32 – evidence source monitoring](https://github.com/MSKazemi/github-trending-1000-study/issues/32); [#58 – conditional futures](https://github.com/MSKazemi/github-trending-1000-study/issues/58); [study mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md), [evidence lessons](EVIDENCE_TO_LESSON_PROTOCOL.md) and [forecast scenarios](FUTURE_SCENARIOS_2027_2031.md).

## Purpose

Study **what the 100 organizations shipped or changed, what they have publicly stated they intend to build, and where the broader industry might be moving**—without mistaking marketing for evidence, future intentions for delivered features, releases for actual adoption, or stars for independently verified reuse. Extract testable interventions to help maintainers build discoverable, secure, useful, sustainably maintained and externally reused software. Never make unsupported claims of CO2e savings or market success.

## Coverage rules and reproducible searches (one issue per company)

1. **Identity first:** verify the exact entity vs product, ownership/acquisitions and company/product name changes **as of 2026-10-12**. Follow both old and new product/company names and their official websites. Two watchlist rows may share a corporate parent (e.g. GitHub/Microsoft, Langfuse/ClickHouse); deduplicate events and avoid counting them as independent companies.
2. **Temporal bounds:** collect material with publication date in **2026-04-12…2026-10-12**; record **publication AND underlying event dates** separately. Products announced before that window may appear as contextual baseline but cannot count as within-window release. Future plans announced in-window are tagged **announced only**, not shipped. Mark later edits to already-published pages where detectable.
3. **Check official primary sources:** company site, changelog/release notes, product docs/version history, public roadmap, engineering blog, announcements, public GitHub projects/releases, credible regulatory filings/financial disclosures. The company homepage is a starting link, not proof.
4. **Check independent evidence:** relevant Reuters, AP, FT, Bloomberg, TechCrunch, The Register, Ars Technica, developer engineering publications, peer-reviewed or versioned research, third-party benchmarks with transparent tasks, and upstream OSS changelogs. Secondary reports about one company press release count as a **single event**, not independent confirmations of its performance.
5. **Systematic best-effort queries** (record exact query, search engine/site, search date, result counts and screened URLs): `"<COMPANY>" after:2026-04-11 before:2026-10-13 AI coding agent`, `"<COMPANY>" release notes 2026`, `"<PRODUCT>" roadmap 2026`, `site:<OFFICIAL_DOMAIN> after:2026-04-11 before:2026-10-13`, and targeted domain searches on news sites + GitHub releases. Search across **all six calendar months** (April partial, May, June, July, August, September, October partial), record "not found" rather than inventing activity. Include company mergers and security incidents, critical reporting and announced cancellations. No claim that every internet article was captured; state each source coverage limit.
6. **Collect eligible events individually:** canonical URL, exact title/author if supplied, publisher, product, company ID, publication date, event date, first-seen UTC, source class, direct evidence, claim, capabilities changed, availability (preview/GA/undisclosed), open/closed license where verified, geographic/plan limits, customer evidence if verifiable, explicit intentions, confidence, corrections/conflicts. Save enough to reproduce the attribution, not copyrighted article text.
7. **Extract the feature map**: coding and agentic capabilities, architecture, product integrations, APIs/SDKs, security/governance, data/knowledge reuse, evaluation/testing, pricing or open-source commitments (dated). Treat feature announcements as vendor claims until confirmed in release notes or independently exercised.
8. **Distinguish three direction classes**: (A) **delivered** and dated; (B) **publicly announced future intention** with quotation/link and commitment status; (C) **analyst conditional inference** with rationale, competing explanations, falsification indicators and horizon (2027–2031). A is not automatically verified functionality, B is not a guarantee, and C is not company strategy or fact.
9. **Link to study outcomes M1–M7** (not product popularity): changes in agent workflows, accepted task outcomes, discovery, verified third-party reuse, security/legal provenance, review+maintenance costs, whole lifecycle effects. Propose a comparable **test** and an explicit *no-effect/negative scenario* for each practically relevant insight.
10. **Publish company report** at `research/company-intelligence/2026-04-12_2026-10-12/NNN-company-slug.md` using [template](../templates/company_six_month_intelligence.md). Add a structured event index where possible and [news corpus IDs](../references/study_sources_2026.json) or a new immutable `NEWS-YYYY-NNNN` evidence item *only after that article has actually been read and verified*. Avoid copying a vendor's press release into several "independent" evidence records.

## Priorities and how to use the 100 issues

Each `[COMPANY-INTEL 2026 #NNN]` ticket is a **bounded data-collection task, not a completed intelligence report**. A completed issue includes the dated report and source log, explicit coverage and unknowns, independent counter-evidence if available, concrete product claims, future-intent attribution, verifiable insights/test cards for our GitHub repos, two-pass factual/link QA and a PR linked back to the issue. Do not mark an issue done because a generic article list or an LLM synthesis exists.

Recommended triage: begin with coding/reuse/search and security/verification cases, then model APIs, sandbox/evaluation infrastructure, then adjacent enterprise/application/cloud stacks. **This is practical triage, not a scientifically-derived ranking of companies.** The initial 100 issue index is in [company issue register](../references/ai_software_company_issue_index_2026-10-12.csv) (added after successful GitHub issue creation). Avoid more issues for sub-brands; use subsections within the owning company's issue.

## Required event ledger columns

`event_id,company_id,company_label,product,source_url,source_title,source_publisher,source_type,published_utc,event_date_utc,accessed_utc,kind,claim_summary,feature,availability,status,study_construct,limitation,confidence,duplicate_event_group,independent_check_url`.

**Allowed status**: shipped, preview, announced_only, reported_undetermined, reversed/cancelled, corrected, unavailable/unknown. Do not turn unavailable evidence into zero announcements. Do not infer product usage from GitHub stars, business valuation or funding. Missing dates/denominators stay missing. Avoid fabricated market shares and unsupported sustainability assertions.

## Evidence quality tiers

- **E0 unverified lead:** title/snippet, undocumented rumor or promotional teaser; cannot support final conclusions.
- **E1 first-party announcement:** supports *what company said and dated*, not actual quality/adoption.
- **E2 reproducible documentary verification:** changelog/docs/release version and/or independently readable artifact, with scope limitations.
- **E3 independent validated behavior:** documented controlled replication/test or neutral credible audit, reproducible tasks and denominator.
- **E4 replicated, generalizable evidence:** independent multi-context task outcomes with uncertainty and checked selection bias. Do not award E4 to marketing or news.

These are *company-watch working tiers*; when the study's existing evidence-to-lesson protocol defines another E0–E5 rating, translate fields explicitly and **do not silently replace that protocol**.

## Acceptance checklist for each company research issue

- [ ] Identity/ownership/brand history checked; date snapshot and source saved.
- [ ] All six calendar months checked and exact search log retained; gaps explicitly stated.
- [ ] Primary newsroom and product docs/changelog investigated; verifiable URL record.
- [ ] Independent high-quality reporting and conflicting evidence screened (or absence documented).
- [ ] Every central claim links to dated evidence; publication and event dates recorded; duplicate stories merged.
- [ ] Features marked shipped/preview/announced/unknown, with license, API and compatibility constraints if documented.
- [ ] Attributed company direction and 2027–2031 conditional scenarios separated, with disconfirming signals.
- [ ] M1–M7 study mapping and **one small falsifiable reuse-first repository experiment** included.
- [ ] Legal/security, privacy/permissions, review load, lifecycle energy and upstream impact limitations considered.
- [ ] Report and evidence index committed; factual/link spot check and human review performed; issue updated with PR URL.

## Safety and scope limits

Use authorized public information, respect access restrictions and robots/rate limits; do not evade paywalls, reveal personal developer data, scrape without permission, copy full copyrighted articles, imply employees endorsed conclusions, or silently overwrite previous snapshots. Prefer official and peer-reviewed sources; report vendor conflicts and independent counter-evidence without false equivalence. Company reports remain **observational descriptive intelligence**, not a new causal dataset or preregistration. Human confirmation is required for inferred practical recommendations.
