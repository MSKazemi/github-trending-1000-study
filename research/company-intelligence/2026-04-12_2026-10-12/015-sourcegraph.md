# Sourcegraph — provisional six-month technology intelligence screen (015)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](015-sourcegraph.events.csv), [search log](015-sourcegraph.search-log.md) and [source-QC note](015-sourcegraph.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#81](https://github.com/MSKazemi/github-trending-1000-study/issues/81) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 015; [issue #81](https://github.com/MSKazemi/github-trending-1000-study/issues/81). Sector: AI coding agents, IDEs and code search. Study lens: existing-code discovery across large repositories.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; first screened 2026-10-12, source-checked 2026-10-14, **upgraded and re-checked 2026-10-16**. Exact UTC search-run times, complete search-engine result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** provisional dated documentary screen — **26 ledger rows** — the original 9 (all re-checked; 2 limitation corrections) plus 17 rows added on 2026-10-16 — covering all seven calendar segments. This is **not issue #81 completion** in the scientific sense, **not an independent benchmark**, and not exhaustive retrieval. **Human factual/methods review: pending.**
- **Official sources checked:** [Sourcegraph](https://sourcegraph.com/), [changelog](https://sourcegraph.com/changelog), [self-hosted release register](https://sourcegraph.com/changelog/releases), [featured changelog RSS](https://sourcegraph.com/changelog/featured.rss), [blog RSS](https://sourcegraph.com/blog/feed.rss), selected blog posts, and public GitHub metadata via read-only `gh api` ([src-cli](https://github.com/sourcegraph/src-cli), [zoekt](https://github.com/sourcegraph/zoekt), [SCIP](https://github.com/scip-code/scip), [EnterpriseBench](https://github.com/sourcegraph/EnterpriseBench), [CodeScaleBench](https://github.com/sourcegraph/CodeScaleBench)). **Claim grading** is company-watch E0–E4 per the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

Sourcegraph publishes a dense first-party changelog. One fetch of the changelog index on 2026-10-16 showed **35 dated in-window cards** (Apr 12–30: 3; May: 6; Jun: 7; Jul: 7; Aug: 7; Sep: 4; Oct 1–12: 1), the blog RSS **22 in-window posts**, and the self-hosted register **10 in-window releases** (7.2.0 Apr 24 … 8.0.0 Sep 17). These are mutable index counts, not a census of shipped capability. Ledger rows are a **purposive selection** relevant to code discovery, agent-facing APIs, review/maintenance workflows, rights and access, plus vendor benchmarks and stated direction. Six general web searches found **no** in-window article from five named independent trade outlets and **no** 2026 CVE for Sourcegraph — both are search misses, **not evidence of absence** (see [search log §C–D](015-sourcegraph.search-log.md)). Independent coverage found is limited to Business Wire syndications of a vendor press release.

## 2. Corporate/product identity and rights baseline

- **Entity:** Sourcegraph (code search, code intelligence, Deep Search, Batch Changes / Agentic Batch Changes, Cody Enterprise, MCP server). The [Sourcegraph/Amp post dated 2025-12-02](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies) says the two were *becoming* separate companies: Sourcegraph keeps code search under a new CEO; the co-founders found **Amp Inc.** for coding agents and remain on Sourcegraph's board. This is **out of window** and recorded only as the relationship baseline; Amp events belong to watchlist [016](016-amp-inc.md) and are not counted here. Legal completion of the separation and ownership were **not** verified against registry filings.
- **Licences (GitHub API, 2026-10-16):** [src-cli](https://github.com/sourcegraph/src-cli) Apache-2.0; [zoekt](https://github.com/sourcegraph/zoekt) Apache-2.0; SCIP protocol Apache-2.0, now at [scip-code/scip](https://github.com/scip-code/scip) (the old `sourcegraph/scip` path redirects; the `scip-code` org was created 2026-01-09, before the window — governance relationship to Sourcegraph unverified). The main product monorepo snapshot `sourcegraph/sourcegraph-public-snapshot` is archived with no SPDX licence detected; the current Sourcegraph server is **not** treated as open source here. Hosted features are governed by commercial terms, credits and AI-feature entitlements that were not reviewed.
- **Access/rights constraint (in window):** an [Aug 4 notice](https://sourcegraph.com/changelog/geographic-access-restrictions) says access is permitted in supported regions only, with a brownout on Aug 14 and a block after Aug 24 (PDT) for unsupported regions, citing law and AI-provider requirements. Any experiment must first confirm the operator's region is supported.
- **Cody:** no in-window Cody Enterprise end-of-life notice was found; the 2025 Cody Free/Pro changes are out of window. Cody status in 2026 remains **unknown** beyond the changelog references.

## 3. Seven-segment dated chronology

| Segment | Original rows (-001…-009) | Rows added 2026-10-16 (L-0NN = CI2026-015-0NN) | Availability / attribution limits |
|---|---|---|---|
| Apr 12–30 | [Apr 27 quantitative Deep Search](https://sourcegraph.com/changelog/2026-04-27) (-001) | L-010 Apr 20 smart hover **Beta** + Git-graph search; L-011 self-hosted 7.2.0 (Apr 24) | Roll-up page has no version line |
| May | [May 05 Compare **Beta**](https://sourcegraph.com/changelog/new-compare-page) (-002) | L-012 May 18 granular admin RBAC (7.3.0 same day) | Beta ≠ GA |
| June | [Jun 15 Deep Search finder subagent](https://sourcegraph.com/changelog/deep-search-finder) (-003); [Jun 29 Agentic Batch Changes **Beta**](https://sourcegraph.com/changelog/agentic-batch-changes-beta) (-004) | L-013 Jun 16 vendor benchmark (9 tasks); L-014 Jun 18 smart hover **GA** | -003 page discloses an earlier 2026 attempt was **reverted**; [Jun 30 blog](https://sourcegraph.com/blog/agentic-batch-changes-public-beta) = same launch |
| July | [Jul 20 Code Finder **Beta**](https://sourcegraph.com/changelog/2026-07-20) (-005); [Jul 27 Search Jobs API](https://sourcegraph.com/changelog/search-jobs-external-api) (-006) | L-015 Jul 2 Business Wire copy of beta launch; L-016 Jul 20 Compare **GA**; L-017 Jul 27 Deep Search context filters (experimental) | Wire copy is vendor-originated, not independent |
| August | [Aug 31 revision-aware Code Finder](https://sourcegraph.com/changelog/2026-08-31) (-007) | L-018 Aug 3 Deep Search guidance/skills + reports; L-019 Aug 4 geo-restriction; L-020 Aug 17 guided diff tour **Beta**; L-021 Aug 20 Code Finder **GA** | Aug 20 GA durable URL [code-finder-ga](https://sourcegraph.com/changelog/code-finder-ga) now verified (was unverified on Oct 14) |
| September | [Sep 14 Agentic Batch Changes](https://sourcegraph.com/changelog/agentic-batch-changes-ga) (-008); context: [self-hosted 8.0](https://sourcegraph.com/changelog/releases/8.0) | L-022 Sep 14 EnterpriseBench repo; L-023 Sep 16 per-merged-changeset pricing; L-024 Sep 17 self-hosted 8.0.0; L-025 Sep 21 direction essay | -008 body says "available for everyone to try", not literally "generally available"; promised self-hosted Sep 16 vs release dated Sep 17 (src-cli 8.0.0 at 2026-09-17T01:54Z, i.e. Sep 16 evening US Pacific — plausibly a time-zone difference, unresolved) |
| Oct 1–12 | [Oct 05 code intelligence in Compare](https://sourcegraph.com/changelog/codeintel-in-compare) (-009) | L-026 Oct 5 self-service commit-signing keys for Batch Changes | -009 page now says Cloud **and** self-hosted 8.1 (8.1.0 dated Oct 14, post-window) — see QC. [Oct 13 update](https://sourcegraph.com/changelog/latest) excluded |

`event_date_utc` stays blank in the ledger: displayed publication dates are not deployment timestamps.

### 3b. Leads added to the ledger on 2026-10-16

The 17 leads verified in this upgrade are now ledger rows **CI2026-015-010 … CI2026-015-026** in the [event ledger](015-sourcegraph.events.csv) (accessed 2026-10-16; the chronology's labels L-010 … L-026 map to the same numbers). The original nine rows keep their strict offline test checks; the new rows are checked for schema, scope and unique IDs/URLs only. Sources, by row: -010 [April 20th updates](https://sourcegraph.com/changelog/2026-04-20); -011 [release register](https://sourcegraph.com/changelog/releases) with [src-cli 7.2.0](https://github.com/sourcegraph/src-cli/releases/tag/7.2.0); -012 [May 18th updates](https://sourcegraph.com/changelog/2026-05-18); -013 [MCP benchmark blog](https://sourcegraph.com/blog/sourcegraph-mcp-and-a-cheaper-model-beat-a-mythos-class-model-alone) (vendor [results explorer](https://sourcegraph.github.io/CodeScaleBench/compare.html) not opened); -014 [smart hover GA](https://sourcegraph.com/changelog/smart-hover-summaries-ga); -015 [Business Wire copy on TechIntelPro](https://techintelpro.com/news/ai/enterprise-ai/sourcegraph-launches-agentic-batch-changes-for-ai-powered-large-scale-code-changes) (same launch as -004); -016 [Compare GA](https://sourcegraph.com/changelog/2026-07-20#compare-page-ga); -017 [July 27th updates](https://sourcegraph.com/changelog/2026-07-27); -018 [August 3rd updates](https://sourcegraph.com/changelog/2026-08-03); -019 [geographic access restrictions](https://sourcegraph.com/changelog/geographic-access-restrictions); -020 [August 17th updates](https://sourcegraph.com/changelog/2026-08-17); -021 [Code Finder GA](https://sourcegraph.com/changelog/code-finder-ga); -022 [EnterpriseBench](https://github.com/sourcegraph/EnterpriseBench); -023 [outcome-pricing blog](https://sourcegraph.com/blog/agentic-batch-changes-pricing); -024 [self-hosted 8.0](https://sourcegraph.com/changelog/releases/8.0) with [src-cli 8.0.0](https://github.com/sourcegraph/src-cli/releases/tag/8.0.0); -025 [The autonomous codebase](https://sourcegraph.com/blog/the-autonomous-codebase); -026 [October 5th updates](https://sourcegraph.com/changelog/2026-10-05). Key figures kept for readers: -013 reports mean reward 0.698 vs 0.568 on **9 vendor tasks**; -022's README says "WORK IN PROGRESS — RESULTS NOT VALIDATED"; -023 states no price.

## 4. Feature map — today vs newly delivered vs preview

| Capability cluster | Pre-window baseline | Delivered in window (vendor-reported) | Preview / announced only | Reuse/integration surface |
|---|---|---|---|---|
| Code discovery | Code Search, precise code intel (SCIP), Deep Search | Quantitative Deep Search (-001), finder subagent (-003), Code Finder GA (L-021), revision-aware Code Finder (-007), hover summaries GA (L-014) | Code Finder beta (-005), hover beta (L-010) | MCP server; [Search Jobs API](https://sourcegraph.com/changelog/search-jobs-external-api) with scoped tokens and JSONL (-006); src-cli (Apache-2.0) |
| Review | Commit/diff views | Compare GA (L-016), code intel in Compare (-009) | Compare beta (-002), guided diff tour (L-020) | Web UI only |
| Multi-repo change | Batch Changes | Agentic Batch Changes "available for everyone to try" (-008), commit-signing keys (L-026) | Beta (-004) | Batch specs, code-host PRs, CI-failure hooks; per-merged-changeset pricing (L-023) |
| Governance / rights | Site admin | RBAC (L-012), AGENTS.md-style guidance (L-018) | Context filters (L-017, experimental), geo-restriction (L-019) | Admin config; credit/entitlement terms |
| Evaluation artefacts | — | Vendor benchmarks: CodeScaleBench subset (L-013), EnterpriseBench (L-022) | — | Apache-2.0 benchmark repos — reusable as **task sources**, not as neutral evidence |

## 5. Stated direction versus shipped

| Dated first-party source | Stated intention | Classification |
|---|---|---|
| [Jun 29 beta](https://sourcegraph.com/changelog/agentic-batch-changes-beta) → [Sep 14 notice](https://sourcegraph.com/changelog/agentic-batch-changes-ga) | Orchestrate any single-repo agent task across all repositories with human approval and CI reaction | **Shipped per vendor** (Cloud, AI-feature customers; self-hosted 8.0) |
| [Sep 16 pricing](https://sourcegraph.com/blog/agentic-batch-changes-pricing) | Charge only for merged changesets | **Announced pricing model**; no price list verified |
| [Sep 21 essay](https://sourcegraph.com/blog/the-autonomous-codebase) | "Everything worth doing in an enterprise codebase starts with universal code visibility and code understanding"; scoped, authorized maintenance agents | **Vision**, no dated commitment |
| [Jul 20 Code Finder](https://sourcegraph.com/changelog/2026-07-20) | Code Finder billable with credits at GA | **Delivered** Aug 20 (L-021) |

No binding 2027–2031 Sourcegraph roadmap was found. **Analyst-only conditional scenarios:** (a) repository-scale retrieval as an agent tool may raise verified reuse of existing internal code — rival: equal results from `rg`/native search plus a well-scoped local agent; falsifier: no difference in independently accepted tasks per total cost. (b) Outcome-based pricing may align vendor incentives with merged changes — rival: incentivises many small mergeable PRs and shifts review burden to maintainers; falsifier: higher reviewer minutes or post-merge reverts per merged changeset.

**Counter-evidence and contradictions:** vendor-disclosed revert of the first finder-subagent attempt (-003); vendor benchmarks with n = 9 (L-013) and an explicitly "not validated" benchmark (L-022); -008 GA wording vs body text; Sep 16 vs Sep 17 self-hosted date; -009 availability wording changed after publication. No neutral replication, independent review or 2026 security advisory was found in this bounded search.

## 6. M1–M7 mapping

| Construct | What this screen offers | Prospective measurement (not done) |
|---|---|---|
| **M1** coding practice | MCP tools and Agentic Batch Changes change the agent workflow | Opt-in logs of agent tool calls with vs without remote code search |
| **M2** accepted quality | Compare/diff tour/code intel aim at review; human approval in batch changes | Hidden independently authored tests; reviewer acceptance of all attempts |
| **M3** discovery | Code Finder/Deep Search retrieve candidates inside an indexed codebase | Candidate precision/recall against a frozen, human-labelled gold set |
| **M4** verified reuse | Search Jobs API, src-cli, SCIP as reusable integration components | Trace actual imports/version pins of reused code, not search hits |
| **M5** reuse-first | Tools surface existing implementations before new code is written | Share of tasks solved by reuse vs new code, independently judged |
| **M6** rights/security/lifecycle cost | RBAC, context filters, geo-restriction, credit/outcome pricing | Setup, review and repair minutes; fees; access-control test cases. **No kWh/CO2e from tokens** |
| **M7** actionable interventions | One experiment below | Pre-registered, opt-in, independently graded |

## 7. One falsifiable reuse-first maintainer experiment (proposed, NOT executed)

**Question:** On this study's own repositories, does a *search-and-verify-existing-code* step using remote code search raise the share of **independently accepted** maintenance tasks solved by reusing existing code, per total human-plus-tool cost, compared with local search?

1. **Tasks:** freeze 12 real maintenance tasks from [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) issues (e.g. "find every place a CSV schema is validated and reuse one validator"), including ≥3 tasks where no reusable code exists. Hidden acceptance tests written by someone other than the solver.
2. **Comparator A:** `rg` + native GitHub code search + an agent restricted to local tools. **Comparator B:** the same plus Sourcegraph Code Finder/Search Jobs pinned to a revision — **only if** access, region support (L-019), terms and cost are approved in advance; never assume credentials.
3. **Primary endpoint:** independently accepted tasks / **all 12** (failures, abstentions and no-solution tasks stay in the denominator). **Secondary:** candidate precision vs a human-labelled list, wrong-reuse proposals, total search + review minutes, fees, licence issues, 30-day follow-up fixes.
4. **Stop rule:** stop B if any access-control or licence violation occurs, if acceptance is not higher than A, or if review minutes per accepted task exceed A by >25 %. Prefer the simpler local setup on ties. Report null results.

## 8. Limitations

- First-party sources dominate; the only non-vendor items found are syndicated copies of a vendor press release. No independent trade review, practitioner critique or 2026 advisory was found — **unknown**, not zero.
- Pages are mutable (e.g. -005 and -009 changed after publication); no archives or hashes were captured.
- Index counts come from one fetch; feeds are truncated (featured RSS begins mid-May).
- The 17 added rows were drafted and spot-checked by the same AI session; only 6 were re-read in the QC note.
- Ownership, licences of hosted services, entitlements and Cody status were not verified against contracts or registry filings.

## 9. Earlier screen (preserved)

The full prior texts are in git history ([PR #178](https://github.com/MSKazemi/github-trending-1000-study/pull/178), merge `2efbf2fbf7dabc9199945bc366baaaf7a2148b17`) and in the untouched [screen log](015-sourcegraph.screen-log.md).

- **2026-10-12 first pass:** a "partial" note with a seven-segment table marked "Not systematically screened" in every segment; one E0 lead, the [Sourcegraph changelog](https://sourcegraph.com/changelog); queries `"Sourcegraph" 2026 coding agent releases`, `"Sourcegraph" product changelog 2026`, `"Sourcegraph" 2026 roadmap` without hit counts; a direction hypothesis (retrieval, isolation and review may improve secure reuse; rival: orchestration shifts work to reviewers) and a proposed retrieval-comparison experiment. Links: [central mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md), [company method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [research grading](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md), [experimental design](../../../docs/REUSE_FIRST_EXPERIMENT.md).
- **2026-10-14 supplementary screen (PR #178):** nine selected first-party changelog leads (now CSV rows -001…-009), the [screen log](015-sourcegraph.screen-log.md), offline tests and a [scoped review note](../../../docs/reviews/2026-10-14-pr-178-sourcegraph-screen-review.md). It claimed: one row per segment at minimum; the Jun 30 blog duplicates the Jun 29 beta; the Aug 20 Code Finder GA entry lacked a durable URL (resolved here as L-021); the Oct 13 update is post-window; -009 was "Sourcegraph Cloud only" (not supported by the page as read on 2026-10-16 — see QC). Its open gates (archived dates, independent/critical reporting with hit counts, human review, an executed task experiment) remain open.

**2027 maintainer lesson (E0):** test whether a code-search tool adds *independently accepted* reuse value on your own frozen tasks before adopting it on vendor benchmarks or release volume.
