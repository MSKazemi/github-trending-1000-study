# Harvey: provisional six-month technology intelligence screen (088)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](088-harvey.events.csv) and its [search log](088-harvey.search-log.md) are an AI-assisted first-pass screen of documentary sources. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 088
- **Research issue:** [#156](https://github.com/MSKazemi/github-trending-1000-study/issues/156). Evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item is minted here; candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):** The legal entity is Harvey AI Corporation, per the site copyright footer; the LAB repository licence reads "Harvey AI". Harvey sells a proprietary legal AI platform: Assistant, Vault, Knowledge, Agents/Agent Builder, Spaces, Command Center, Contract Intelligence and Horizon Scanning, with Word and Outlook add-ins. It is privately held and venture-funded. The co-founders are Winston Weinberg (CEO) and Gabe Pereyra (president). No parent company was found. Harvey announced two in-window acquisitions: Benchmark ([2026-07-16](https://www.harvey.ai/blog/y-combinator-backed-benchmark-joins-harvey), called its "third acquisition of 2026") and Guardrails AI ([2026-09-09](https://www.harvey.ai/blog/guardrails-ai-joins-harvey), called its "fourth"). The first two 2026 acquisitions were **not identified** in this screen. No filing-level corporate verification was done.
- **Product URL and company newsroom:** [harvey.ai](https://www.harvey.ai/), [blog](https://www.harvey.ai/blog), [newsroom](https://www.harvey.ai/newsroom), [sitemap](https://www.harvey.ai/sitemap.xml), [status page](https://status.harvey.ai/) ([Atom feed](https://status.harvey.ai/feed.atom)), GitHub org [harveyai](https://github.com/harveyai), whose main in-window repository is [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) (MIT).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). 43 ledger rows cover all seven calendar segments.
- **Source coverage:** The sitemap was used to enumerate in-window blog posts (several hundred, most of them SEO explainers). 77 in-window product, technical, research and company posts (plus one pre-window baseline post) were fetched as raw HTML, with `datePublished` read from each page. Also used: newsroom listing; GitHub API for `harveyai/harvey-labs` (releases, tags, issues, pull requests) and `guardrails-ai/guardrails`; PyPI JSON for `guardrails-ai`; the official status page; independent sources (TechCrunch, Bloomberg via Yahoo Finance, LawSites, Artificial Analysis, Vals AI); and the Hacker News Algolia API. The Bloomberg original returned HTTP 403. See the [search log](088-harvey.search-log.md).

## 1. Search and inclusion audit

This is a summary. Exact requests, opened URLs and exclusions are in the [search log](088-harvey.search-log.md). Search-engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | harvey.ai sitemap + raw HTML | all `/blog/` URLs, lastmod 2026-04-12..10-12 | several hundred (mostly SEO guides) | 77 in-window product/technical/research/company posts fetched | 31 rows | SEO explainers, customer wins, office openings, model-availability duplicates (log) | the sitemap omitted some newsroom posts, which were found through the newsroom page instead |
| 2026-10-16 | GitHub API | `harveyai` org repos; `harvey-labs` releases, tags, issues, PRs, CHANGELOG | 7 repos; 2 releases + 1 tag; ~190 issues/PRs | ~25 issues read | 8 rows | most issues not opened; individual reporters not named | author association is not proof of employment |
| 2026-10-16 | HN Algolia API | `Harvey AI`, `Harvey legal`, `harvey.ai`, `Legal Agent Benchmark` (window bounds) | 12 / 6 / 6 / 5 stories | all | 0 direct (used as leads) | vendor reposts, unrelated launches | low HN engagement; leads only |
| 2026-10-16 | web search (3 queries) | criticism/outage, funding, LAB critique | unknown | ~25 | 3 rows via fetched pages | aggregators and comparison blogs graded E0 and not used | Bloomberg 403; Artificial Lawyer not found |
| 2026-10-16 | status.harvey.ai | Atom feed + incident page | 2 in-window entries | 2 | 1 row | planned EU maintenance (Jul 19) not ledgered | page shows Jul–Oct 2026 only |

## 2. Verified company/product identity and baseline

Harvey is a proprietary, multi-model legal AI platform for law firms, in-house teams and professional-services firms. In the window it moved further from chat toward **agents**: a 500+ agent library, Agent Builder, matter-scoped Spaces and Memory in "Harvey II", and an in-house post-trained model, "Harvey Tenet". The **open-source surface is narrow but new**. [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) holds the Legal Agent Benchmark (LAB) tasks, rubrics and harness. The GitHub API reports it as MIT, created 2026-03-30, with its first public commit on 2026-05-06. Older org repos are archived forks or the earlier `biglaw-bench` (no licence detected). The **platform, models and BigLaw Bench scoring remain proprietary**, and the hold-out sets behind headline LAB scores are private.

Pre-window baseline (context only, not counted): TechCrunch reports a $200M round at an $11B valuation in March 2026 and an $8B valuation in December 2025 ([TechCrunch, 2026-09-09](https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/)). Harvey also published "Building Spectre", its internal cloud coding-agent platform, on [2026-04-07](https://www.harvey.ai/blog/building-spectre-internal-collaborative-cloud-agent-platform), five days before the window. **Post-window, excluded:** "Building a Frontier In-House Organization" (2026-10-13), "Legal Work Orchestration" and the Drakopoulos adoption post (2026-10-15), and the Artificial Analysis LAB-AA v1.1 leaderboard (current state on access, not dated in window).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Usage claim of 700,000+ tasks/day (Apr 14); Opus 4.7 at 90.9% on BigLaw Bench (Apr 16); embedding-reversal security post (Apr 30) | [blog](https://www.harvey.ai/blog/two-types-of-legal-work-one-agentic-platform), [blog](https://www.harvey.ai/blog/opus-4-7-now-live-in-harvey), [blog](https://www.harvey.ai/blog/how-harvey-secures-embeddings-at-scale) | none found | Review-table posts (Apr 15, 21), GPT-5.5 preview (Apr 23), Madrid/Dallas/Chicago office posts excluded |
| 2026-05 | 500+ agent library (May 5); **LAB open-sourced (May 6)**; LawSites critique (May 19); Command Center waitlist (May 20); LAB initial results <10% all-pass (May 26); open-weight post-training with Baseten (May 27); Opus 4.8 at 10.4% on LAB (May 28) | [LAB post](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark), [results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) | [LawSites, May 19](https://www.lawnext.com/2026/05/some-thoughts-on-harveys-launch-of-lab-an-open-source-long-horizon-benchmark-for-legal-ai-agents.html) | Transformation Office, agentic SOC, Contract Intelligence and Email Harvey were read but not ledgered |
| 2026-06 | Own cloud-agent runtime rationale (Jun 1); ISO 42001 (Jun 5); Connector Library with MCP in Early Access (Jun 8); **Fable 5 opt-in under different data-retention terms** (Jun 9); external redline-grading fix merged (Jun 11); LAB Contracts (Jun 12); Microsoft 365 Copilot agent (Jun 16); GLM-5.1 post-training (Jun 22) | [Fable 5](https://www.harvey.ai/blog/fable-5-now-available-in-harvey), [PR #76](https://github.com/harveyai/harvey-labs/pull/76) | Vals AI page attributes the PR #76 fix to Vals | Vault upload scaling, PitchBook, Singapore/Milan, Sonnet 5 excluded |
| 2026-07 | Artificial Analysis LAB-AA (Jul 7); GPT-5.6 Sol at 92.7% on BigLaw Bench vs 2.5% on LAB (Jul 9); judge field-order defect issue (Jul 11); Benchmark acquisition (Jul 16); LAB Diligence (Jul 17); Intapp ethical walls GA (Jul 23); LAB v1.0 tag (Jul 24) | [AA](https://artificialanalysis.ai/articles/harvey-lab-aa), [#106](https://github.com/harveyai/harvey-labs/issues/106) | Artificial Analysis (partnered) | Microsoft CELA deal, Opus 5, document-processing scale post and Chicago opening excluded |
| 2026-08 | AU-region full outage of ~20 min (Aug 14); Review Table model with Applied Compute (Aug 14); grader-error issue #145 (Aug 18); **Harvey II** (Aug 18); **Harvey Tenet** (Aug 20); unsatisfiable-criterion issue #149 (Aug 24) | [status](https://status.harvey.ai/incidents/01KZZCRZ8PQ8P3J6B1P8TM8EHZ), [Harvey II](https://www.harvey.ai/blog/introducing-harvey-ii), [Tenet](https://www.harvey.ai/blog/post-training-update-harvey-tenet) | GitHub issue reporters | Memory (Aug 26) folded into Harvey II; playbook builder, Outlook and audio/video posts excluded |
| 2026-09 | Everlaw partnership (Sep 3); RLM diligence agents (Sep 8); **Guardrails AI acquisition** and **$550M at $15.5B** (Sep 9); LAB v1.1.0 (Sep 18); **Bloomberg: gross margin −50% by June** (Sep 21); 3,000-customer claim (Sep 28) | [funding](https://www.harvey.ai/blog/harvey-raises-dollar550m-at-a-dollar155b-valuation-to-help-legal-teams-own-their-intelligence), [Guardrails](https://www.harvey.ai/blog/guardrails-ai-joins-harvey) | [TechCrunch Sep 9](https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/); [Bloomberg via Yahoo Sep 21](https://finance.yahoo.com/technology/ai/articles/openai-anthropic-costs-push-more-160523322.html) | Horizon Scanning, Fable 5.1, Squire Patton Boggs, GE Aerospace, Pro Bono, Word custom agents and agentic DMS search excluded |
| 2026-10-01..12 | LAB v1.2.0 grading fixes (Oct 1); connector permission engineering (Oct 1); **MCP Policy Engine** (Oct 7); TX-RAMP Level 2 (Oct 8); Vals AI LAB leaderboard update (Oct 12) | [v1.2.0](https://github.com/harveyai/harvey-labs/releases/tag/v1.2.0), [MCP](https://www.harvey.ai/blog/building-harveys-mcp-policy-engine), [Vals](https://vals.ai/benchmarks/hlab) | Vals AI (industry partner) | Boston (Oct 1), Legalscape (Oct 2), TC Energy (Oct 5), LexisNexis MTD workflow (Oct 7), Tokyo/Ogier (Oct 12) excluded or used in §5 |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](088-harvey.events.csv): 43 rows, IDs `CI2026-088-001`…`043`. Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-088-005 | 2026-05-06 | LAB open-sourced: 1,200+ tasks, 24 practice areas, 75,000+ rubric criteria, all-pass grading | MIT repo; hold-out sets private; task-count text inconsistent (1,200+ vs 1,250); README badge shows 2,010 tasks on access | [blog](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (first party) | [repo](https://github.com/harveyai/harvey-labs) via `gh api` | E2 (documentary) |
| CI2026-088-008 | 2026-05-26 | Frontier models <10% all-pass; top ~$50.90 and ~22 min per task | vendor-run on private hold-out | [blog](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) | AA and Vals use different harnesses | E1 |
| CI2026-088-014 | 2026-06-09 | Fable 5 opt-in: data retained by provider ~30 days, US-only processing, outside existing customer commitments | opt-in early access | [blog](https://www.harvey.ai/blog/fable-5-now-available-in-harvey) | none | E1 |
| CI2026-088-019 | 2026-07-07 | Independent re-implementation: best 14.2% all-pass; 13 of 28 models pass zero tasks | partnered; not comparable with v1.1 | [Artificial Analysis](https://artificialanalysis.ai/articles/harvey-lab-aa) | — | E2 (partnered) |
| CI2026-088-021/028/031 | 2026-07-11 / 08-18 / 08-24 | Public issues: judge field order flips verdicts; unreadable deliverables graded as content; unsatisfiable rubric criterion | #106 and #149 closed; #145 open but changelog fix in v1.2.0 | GitHub issues | v1.2.0 release notes | E2 (public record), not E3 |
| CI2026-088-030 | 2026-08-20 | Harvey Tenet: Kimi K3 + Fireworks post-training; ~2x base LAB completions | research preview; weight release not stated | [blog](https://www.harvey.ai/blog/post-training-update-harvey-tenet) | TechCrunch mention only | E1 |
| CI2026-088-034 | 2026-09-09 | Acquisition of Guardrails AI, maintainer of an Apache-2.0 framework | no stated plan for the OSS project; 0 default-branch commits 2026-09-08..10-16 | [blog](https://www.harvey.ai/blog/guardrails-ai-joins-harvey) | Guardrails copy, `gh api`, PyPI | E2 (documentary) |
| CI2026-088-037 | 2026-09-21 | Gross margin ~50% → ~−50% by June after the agent update, positive again after Tenet | anonymous sources; company declined specifics | [Bloomberg via Yahoo](https://finance.yahoo.com/technology/ai/articles/openai-anthropic-costs-push-more-160523322.html) | none | E1 (independent, anonymous-sourced) |
| CI2026-088-041 | 2026-10-07 | MCP Policy Engine: per-call mediation, info-flow limits, Tool Pinner, Rego via Regorus | internal; not evaluated externally | [blog](https://www.harvey.ai/blog/building-harveys-mcp-policy-engine) | [regorus](https://github.com/microsoft/regorus) exists | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agents | 500+ agent library and Agent Builder (May 5); custom agents in Word (Sep 23); Harvey II matter-scoped agents + Memory (Aug 18/26) | shipped (vendor) |
| Evaluation | LAB open benchmark (May 6) + Contracts (Jun 12), Diligence (Jul 17), Firm Knowledge extensions; v1.0 tag, v1.1.0, v1.2.0; third-party leaderboards (Artificial Analysis, Vals AI); BigLaw Bench remains proprietary | mixed: open harness/tasks, private hold-outs |
| Models | Routed third-party frontier models; in-house post-training (GLM-5.1/5.2 with Applied Compute, Qwen with Baseten, Kimi K3 with Fireworks → "Harvey Tenet") | research preview / vendor-stated |
| Integrations | Connector Library (Google Drive, Gmail native; MCP to iManage, NetDocuments, PitchBook, Intralinks, Datasite, Box); Microsoft 365 Copilot/Cowork; Intapp ethical walls GA; Everlaw (announced); LexisNexis MTD workflow; Legalscape | shipped / preview / announced |
| Security & governance | Embedding-reversal controls; MCP Policy Engine; ISO 42001; TX-RAMP Level 2; ethical-wall enforcement; Fable 5 data-retention exception disclosed | vendor-claimed |
| Licensing | `harvey-labs` MIT (GitHub API); platform proprietary; Guardrails `guardrails-ai` Apache-2.0 (PyPI 0.11.0, 2026-08-14) | observed |
| Maintenance signals | LAB CHANGELOG records score-affecting changes with comparability notes; 154 PRs by 2026-10-12 (92 by repo collaborators, 75 merged; 62 by others, 21 merged); Guardrails default branch quiet since acquisition | observed (GitHub API) |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Publish a leaderboard and "standards for normalizing submissions" for LAB | [2026-05-06](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) | "coming weeks" | partly delivered via Artificial Analysis (Jul 7) and Vals AI leaderboards | No normalization standard located in the repo by this screen |
| Expand LAB to all Biglaw practice areas, in-house and non-lawyer professional work, and training-oriented datasets | same | none stated | partly delivered (Contracts, Diligence, Firm Knowledge) | Private hold-outs limit external replication |
| "The strongest production agent deployments will be multi-model from the start." | [2026-05-26](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) | none | stated strategy | Bloomberg reports Harvey still needs Opus for its hardest tasks |
| Partner "with organizations to build specialized models around their own legal work" | [Harvey II, 2026-08-18](https://www.harvey.ai/blog/introducing-harvey-ii) | none | uncommitted | Tenet weights and licence not published |
| Scale compute to bring research "to production with new generalist models" | [Tenet, 2026-08-20](https://www.harvey.ai/blog/post-training-update-harvey-tenet) | none | tentative | No production availability date |
| "Rapidly scaling connectors in the coming months" | [2026-06-08](https://www.harvey.ai/blog/connector-library) | months | planned | Increases prompt-injection surface (vendor's own MCP post) |
| Open a Tokyo office in early 2027 | [2026-10-12](https://www.harvey.ai/blog/harvey-to-open-tokyo-office) | early 2027 | planned | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Domain vendors will open their **evaluation harnesses** but keep scoring hold-outs and products closed | LAB is MIT with private hold-outs; BigLaw Bench stays proprietary; the leaderboards come from partners | Openness may be marketing ("open source theatre" critique cited by LawSites) | Hold-out sets published or a neutral body administers scoring by 2028 | moderate for the pattern; low for durability |
| H2: Inference cost will push application vendors to post-train open-weight models | Tenet, GLM, Qwen and Kimi work; Bloomberg's margin report; vendor-reported ~$50/task frontier cost | Frontier prices may fall faster; model quality gap may persist (Opus still needed) | Harvey or peers revert to frontier-only routing by 2028 | low–moderate; margin data anonymous |
| H3: Rubric/judge defects will materially move all-pass scores, so benchmark versions need score-comparability changelogs | Issues #106, #145, #149 and others; Vals-contributed fix; CHANGELOG with comparability notes | Defects may be small relative to model differences | Re-scoring across versions shows rank stability within noise | moderate that defects exist; magnitude unknown |
| H4: Acquired open-source agent-safety projects will slow down after acquisition | Guardrails default branch had no commits for ~5 weeks after the deal (vs 77 in the prior ~14 weeks); hosted Hub inference was already being discontinued | Short window; maintenance may move to other branches or repos; summer cadence | Releases resume on PyPI at prior cadence by mid-2027 | low; n=1, short window |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Vendors turn agent workflows into published long-horizon task environments (Spectre internally; LAB externally) | Track whether trending agent repos ship task/rubric harnesses | Harnesses are promotional rather than used | Repository artefacts at pinned commits only |
| M2 accepted task quality | All-pass grading stays very low (<15%) while short-horizon scores exceed 90% | Use all-pass style acceptance in our own tasks; report criteria and all-pass separately | Strict grading may punish trivial omissions | Hidden tests authored independently; all attempts counted |
| M3 discoverability | $550M round, a brand campaign and adoption claims (3,000 customers) | Separate press volume from verified reuse | Press is not reuse | Stars/funding never used as an outcome |
| M4 verified third-party reuse | External PRs merged into harvey-labs (21 of 62 non-collaborator PRs); third-party leaderboards run it | Count independently executed runs with published artefacts | Partners are commercially linked to Harvey | Executed, reproducible runs only |
| M5 rights/security/provenance | MIT benchmark; proprietary platform; model data-retention exceptions; MCP prompt-injection controls | Licence and data-terms check before reuse of any benchmark task | Tasks may embed third-party documents with unclear rights (not checked) | Licence files at a pinned commit |
| M6 review/maintenance and lifecycle cost | Benchmark fixes (pandoc, judge order, rubric desyncs); token-cost pressure | Measure reviewer minutes per accepted task under two grading regimes | Agent-assisted review may absorb the cost | No kWh/CO2e inferred from GPUs, tokens or dollars |
| M7 actionable interventions | Version-pinned benchmark + score-comparability changelog; policy enforcement outside the model | See §8 | Adds process overhead without changing outcomes | Synthetic tasks until approval |

Company adoption claims (80% of Am Law 100, 3,000+ customers, 700,000 tasks/day) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), specifically the offline synthetic task-acceptance tooling (`trending_study.value_gate`, `trending_study.goldset` and the unit suite), run **network-free**. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Adopt LAB-style **all-pass acceptance with a versioned, score-affecting changelog** for the study's own small synthetic agent tasks. A task counts as accepted only if every pre-registered criterion passes. Any change to criteria, grader or fixtures that could move scores gets a dated CHANGELOG entry stating comparability. Reuse first: copy the documented *pattern* from `harvey-labs/CHANGELOG.md` (MIT) and the existing repo acceptance tests. Do not import the LAB harness or add a dependency.

**Treatment/control and frozen comparable task:** Freeze 10 small synthetic issues (for example validator edge cases and CSV-schema fixes). A person other than the agent operator writes **hidden acceptance criteria** (5–10 atomic checks per task) and keeps them out of agent context. Control: the current practice of reviewer judgement plus the unit suite. Treatment: the same review plus all-pass scoring against the frozen criteria, with any criterion edit logged and re-scoring both arms. Both arms use the same agent, model version, prompt and time budget, with order randomized per task. Accepted-task unit: one patch that passes the full unit suite, satisfies all criteria (treatment) or reviewer acceptance (control), and is merged without rework.

**Success and guardrails:** The primary measure is agreement between all-pass acceptance and an independent second reviewer's accept/reject verdict, across all 10 tasks including refusals and timeouts. Secondary: criteria found defective (unsatisfiable or leaking answers), counted as in LAB issues #149/#152. Guardrails: no network access during runs, no real credentials, no new dependency, full unit suite green, no paid API spend without the maintainer's approval. Measured human work: minutes to author criteria, minutes per review, minutes to fix defective criteria. No energy or CO2e estimate.

**Stop/reversal rule:** Stop and keep the control if all-pass acceptance agrees with the independent reviewer no better than the control does, or if criteria authoring plus fixing exceeds 15 minutes per task on average. Stop immediately if more than 2 of 10 tasks have a defective criterion discovered after scoring, because that signals the rubric is the bottleneck. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** the MIT `harvey-labs` repository with the v1.0 tag and releases v1.1.0/v1.2.0 (GitHub API); public defect reports and fixes; an independent re-implementation and a partner leaderboard of LAB-derived tasks; an AU outage of about 20 minutes (official status page); the Guardrails acquisition with matching copies on both companies' sites.
- **Claims/announcements only:** agent library size, BigLaw Bench and LAB scores, Tenet and other post-training results, ISO 42001 and TX-RAMP certifications, connector and usage counts, ARR, and customer and valuation figures. The future direction items are in §5.
- **Conjectures and unknowns:** H1–H4 in §6. Also unknown: whether Tenet weights will be released, the rights status of the documents embedded in LAB tasks, the first two acquisitions of 2026, and status history before July 2026.
- **Important contradictory or null evidence:** (a) valuation $15.5B (Harvey, TechCrunch) vs "$15.6 billion" (Bloomberg syndication; HN headline); (b) the Guardrails acquisition is dated Sep 8 on Guardrails' site but Sep 9 (`datePublished` 12:23Z) on Harvey's; (c) the Boston office post `datePublished` is 2026-10-01 but the newsroom list shows October 2; (d) LAB task count reads "more than 1,200" and "1,250" in the same post, while the README badge showed 2,010 on access (the extensions may explain this); (e) Opus 4.8 scores 10.4% on Harvey's LAB vs 7.5% (max) on Artificial Analysis LAB-AA, from different task sets, harnesses and judges, so they are not comparable; (f) the margin collapse is reported only from anonymous sources, and Harvey declined to give specifics; (g) a web-search summary claimed Sullivan & Cromwell apologized for AI errors in filings. That claim was **not** verified, it is not linked to Harvey in any source read, and it was not used.
- **#56 candidates (not minted):** LawSites 2026-05-19; Artificial Analysis 2026-07-07; TechCrunch 2026-09-09; Bloomberg via Yahoo Finance 2026-09-21; Vals AI leaderboard (mutable). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned, and syndicated copies must not be counted twice.
- **Figures confirmed against raw text:** the screening agent reports that it matched every number, date and quote in the ledger by `grep` against saved page text or GitHub/PyPI API output, except where a row says "not inspected". See the search log. This is the screening agent's own statement; the independent spot-check below re-verified 21 of 43 rows, not the whole ledger.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

Rows were re-fetched on 2026-10-16 (raw HTML from harvey.ai, Artificial Analysis, Vals AI, TechCrunch, Yahoo Finance syndication of Bloomberg and the status page; `gh api` for `harveyai/harvey-labs` and `guardrails-ai/guardrails`). Each date, figure and quote was matched against the raw text.

| Row | Outcome | Note |
|---|---|---|
| CI2026-088-001 | confirmed | `datePublished` 2026-04-14; "700,000+ tasks are executed daily, over 50 million terms are extracted weekly" |
| CI2026-088-002 | confirmed | 2026-04-16; 90.9% BigLaw Bench, 45% perfect; tone mismatch, overshoot on detail, non-standard citations |
| CI2026-088-005 | confirmed | 2026-05-06; "more than 1,200" and "1,250" tasks, 24 practice areas, over 75,000 criteria, no leaderboard at launch; first commit 2026-05-06T15:02:28Z; MIT |
| CI2026-088-008 | confirmed | 2026-05-26; 7.1/5.4/4.2/2.1/0.8%; ~$50.90 and ~22 min per task; "less than 10%"; no single model leads every area |
| CI2026-088-010 | confirmed | 2026-05-28; 10.4% LAB, 91.1% BigLaw Bench; AA 7.5% for Opus 4.8 (max) confirmed on the AA page |
| CI2026-088-014 | confirmed | 2026-06-09; 13.3% LAB, 93.4% BigLaw Bench; deletion "generally" after 30 days; processing in the United States |
| CI2026-088-015 | confirmed | PR #76 opened 2026-06-09T22:23Z, merged 2026-06-11T00:49Z, author association CONTRIBUTOR; Vals page says "We fixed that bug and merged it upstream" |
| CI2026-088-018 | confirmed | 2026-06-22; rubric pass 0.913, all-pass 0.126 (the "above GPT-5.5 xhigh and Opus 4.8 Max" applies to rubric pass rate, as the row says) |
| CI2026-088-019 | confirmed | 2026-07-07; 14.2%, 7.5% tie, 13 of 28 at zero, 120 private tasks, single Gemini 3.1 Pro judge, ~$1.3 vs ~$8.2 |
| CI2026-088-020 | confirmed | 2026-07-09; 92.7% BigLaw Bench, 2.5% LAB, EU/AU to be announced |
| CI2026-088-021 | confirmed | issue #106 opened 2026-07-11, closed 2026-08-24; `claude-sonnet-4-6`, temperature 0, three runs per arm |
| CI2026-088-022 | confirmed | 2026-07-16; "third acquisition of 2026", more than $100 million net-new ARR, more than 125 asset-management firms |
| CI2026-088-026 | confirmed | incident timestamps 2026-08-14T05:44:02Z and 06:04:29Z; "Full outage"; Assistant, Vault and Microsoft Add-ins (AU) |
| CI2026-088-030 | confirmed | 2026-08-20; GSPO, rank-64 LoRA, ~1,750 environments, ~150 B300 GPUs, 2 months; "almost twice", +9 and +2 percentage points |
| CI2026-088-031 | confirmed | issue #149 opened 2026-08-24, closed 2026-10-03; passed 0 times in 17 scored runs |
| CI2026-088-034 | corrected | Apache-2.0 (GitHub API), 250,000+ monthly downloads, Snowglobe and "fourth acquisition" confirmed; 0 commits from 2026-09-08 vs 77 from Jun 1 to Sep 8 reproduced. The post says the team joins Harvey's product and engineering organization and starts on its "Applied AI initiatives", not a unit named "Harvey Applied AI". The claim text is reworded |
| CI2026-088-035 | confirmed | 2026-09-09; $550M at $15.5B co-led by Diffusion and Lightspeed; 80% of Am Law 100; five of the Fortune 10; TechCrunch confirms $200M at $11B (March) and $8B (December) |
| CI2026-088-037 | confirmed | `datePublished` 2026-09-21; "$15.6 billion"; ~50% to -50% by June from "a person familiar"; positive again; twenty-fold token use; buys expertise from Mercor; still needs Opus for its hardest tasks |
| CI2026-088-038 | confirmed | 2026-09-28; more than 3,000 customers, 200,000 lawyers, 70 countries |
| CI2026-088-042 | confirmed | published 2026-10-08, effective September 22, 2026. The source says "public institutions of higher education", which the row paraphrases as "public universities" |
| CI2026-088-043 | confirmed | "Updated 10/12/2026"; Muse Spark 1.2 at 25.42%; internet disabled; final score is the average of the two judge task-pass rates |

Outcome counts: 20 confirmed, 1 corrected, 0 unverifiable, 0 wrong. No serious error was found. The Yahoo copy was used for the Bloomberg row because the Bloomberg original returned 403 to the screening agent; it was not re-requested here.

This is an AI-assisted spot-check, not a qualified human review.
