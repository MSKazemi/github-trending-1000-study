# Tabnine — provisional six-month technology intelligence screen (019)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](019-tabnine.events.csv), [search log](019-tabnine.search-log.md) and [source-QC note](019-tabnine.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review are **pending**. Merging is not scientific or security sign-off; issue [#86](https://github.com/MSKazemi/github-trending-1000-study/issues/86) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 019; [issue #86](https://github.com/MSKazemi/github-trending-1000-study/issues/86). Sector: AI coding agents, IDEs and code search; study relevance: enterprise privacy and assistant governance.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened 2026-10-16**. Exact per-query UTC times, search result counts, hashed page captures and an independent reviewer are unavailable.
- **Status:** **19 dated source leads covering all seven calendar segments** (3 pre-existing + 16 added 2026-10-16); purposive, not exhaustive; not independently verified task outcomes. [Method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
- **Official channels checked:** [release notes](https://docs.tabnine.com/main/administering-tabnine/release-notes) (reachable), former [Tabnine blog](https://www.tabnine.com/blog/) and [product-news index](https://www.tabnine.com/blog/category/product-news/) (now redirecting; read via Internet Archive), public GitHub org [codota](https://github.com/codota), and the buyer's [Tricentis newsroom release](https://www.tricentis.com/news/tricentis-acquires-tabnine). Claim grading is company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](019-tabnine.search-log.md) records 5 executed web queries, 10 direct fetch groups (official docs, Wayback captures, `gh api`), per-segment inclusion/exclusion decisions and the queries that were planned but not run. Result counts are **unknown**, not zero. The earlier screens marked April, August, September and October as "not documented"; dated evidence now exists for every segment, which reflects a fuller search, **not** a change in Tabnine's activity.

**Access condition (2026-10-16, outside the window but material):** every tested `www.tabnine.com` URL — homepage, blog, pricing and all article pages — now returns HTTP 301 to a generic tricentis.com page. Tabnine-domain articles were checked only through Wayback captures; `docs.tabnine.com` still serves current release notes. The [source-QC note](019-tabnine.source-qc-2026-10-16.md) records the details.

**Exclusions:** "Governance You Can Trust: What's New in Tabnine 6.1" (displayed Apr 9, before the window); the Gartner "Visionary" post (a 2026 capture shows a conflicting displayed date of "May 28, 2025"); syndicated copies of the Tricentis release (Business Wire, SD Times, GovConWire, Intelligent CIO, 01net, Pulse2, IT Brief); an AI-bylined Futurum note; an aggregator's unopened "$500M" headline; v6.6.11 (Oct 14), which falls outside the window.

## 2. Corporate/product identity and rights baseline (as of 2026-10-12)

- **Entity:** Tabnine is an enterprise AI coding assistant; its public GitHub organisation is `codota`. Founding history and legal-entity details were not checked to filing level. On **2026-07-30** both [Tabnine](https://www.tabnine.com/blog/a-new-chapter-for-tabnine/) and the buyer [Tricentis](https://www.tricentis.com/news/tricentis-acquires-tabnine) stated that **Tricentis has acquired Tabnine**. They disclosed no terms. [Calcalist](https://www.calcalistech.com/ctechnews/article/1o1nf7vd3) reports an estimate of "tens of millions of dollars". No filing-level closing evidence was found. From 2026-07-30 onward, treat Tabnine as a **product line inside Tricentis**, not an independent company.
- **Products in window:** Tabnine Enterprise Agent and Chat (IDE plugins for VS Code/Cursor, JetBrains, Eclipse and Visual Studio); Tabnine CLI; the Enterprise Context Engine; the PR review agent; Code Review/Coaching (private beta at v6.1.0); and a "Tabnine CLI, powered by OpenCode" distribution. The products are offered as SaaS and as private/self-hosted or air-gapped installations (the v6.4.0 notes bundle offline docs for air-gapped installs).
- **OSS licences:** Tabnine's commercial platform is **closed source**. Public repos found: [tabnine-pr-agent](https://github.com/codota/tabnine-pr-agent) (**no licence detected** by the GitHub API) and [tabnine-opencode-public](https://github.com/codota/tabnine-opencode-public) (releases and issues only, **no licence detected**). The release notes cite PRs in `codota/opencode`, which is **not public** (404). The upstream agent [OpenCode](https://github.com/anomalyco/opencode) is **MIT**. The older IDE client repos `tabnine-vscode` (MIT) and `tabnine-nvim` are **archived**; the GitHub API does not expose when they were archived, so no event is dated.
- **Rights implication:** you can study Tabnine's reusable building blocks (OpenCode, MCP governance, hooks), but you cannot fork Tabnine's own wrapper code without a licence.

## 3. Seven-segment dated chronology

| Segment | In-window source evidence (displayed source dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 15 v6.1.0](https://docs.tabnine.com/main/administering-tabnine/release-notes): CLI Plan mode, sandboxing, extensions, Generalist Agent, BYOAI, cost API; [Apr 29 PR agent v2](https://github.com/codota/tabnine-pr-agent/releases/tag/v2); Apr 29 "May 2026 Product Update" (index listing only) | Code Review/Coaching is a private beta; the Apr 29 article body is unavailable |
| May | [May 6 April recap](https://www.tabnine.com/blog/april-recap-agents-you-can-trust/) (a recap of v6.1.0); May 12 v6.2.0: Cursor plugin, admin governance of CLI tools/MCP/guidelines | The vendor corrected its own v6.2.0 notes (feature "not ready yet"; CLI version 0.20.3→0.20.2) |
| June | Jun 7 v6.3.0: Eclipse agent, accepted-code logging, CLI hooks/skills/subagents, local indexing removed; [Jun 18 shared-memory essay](https://www.tabnine.com/blog/shared-memory-for-multi-agent-development/); [Jun 26 Context-Readiness essay](https://www.tabnine.com/blog/context-readiness-ai-coding-benchmark/) | The two essays are commentary, not releases |
| July | Jul 7 v6.4.0: service accounts, 1B-token/month fair-use limit, "Restrict YOLO mode"; Jul 30 acquisition ([Tabnine](https://www.tabnine.com/blog/a-new-chapter-for-tabnine/), [Tricentis](https://www.tricentis.com/news/tricentis-acquires-tabnine)); [Jul 31 Calcalist](https://www.calcalistech.com/ctechnews/article/1o1nf7vd3) | Two transaction-party statements describe **one** event; deal value is an estimate |
| August | [Aug 2 independent critique](https://www.beri.net/article/tricentis-tabnine-acquisition-air-gapped-coding-assistant-roadmap-risk); Aug 5 v6.5.0: fine-grained PATs, OIDC keyless model auth; [Aug 5 tabnine-opencode v0.4.1](https://github.com/codota/tabnine-opencode-public/releases/tag/tabnine-v0.4.1) | The Wayback `/blog/` index of 2026-09-09 shows **no Tabnine blog post after Jul 30** |
| September | Sep 15 v6.6.0: "Tabnine CLI, powered by OpenCode: Now available to all customers", a beta IDE agent, and a fix for CVE-2026-64642 ([GHSA](https://github.com/advisories/GHSA-6gpp-xcg3-4w24)); [Sep 24 tabnine-opencode v1.0.0](https://github.com/codota/tabnine-opencode-public/releases/tag/tabnine-v1.0.0) | The notes flag 6.6.0/6.6.1 as **"unstable"** |
| Oct 1–12 | Oct 4 v6.6.8: Gemini usage/cost double-count fixed and history restated; Oct 8 v6.6.9: read-only Jira access in the CLI, code-signed Windows installer | v6.6.11 (Oct 14) and the site redirect (observed Oct 16) are outside the window |

Per-segment row counts: Apr 3, May 2, Jun 3, Jul 4, Aug 3, Sep 2, Oct 2 (total 19). Most release-notes rows share one living docs URL. The version number and displayed date identify each row, but no hash pins them.

## 4. Feature map (shipped / preview / announced / unverified)

| Capability cluster | Status in window (vendor-reported) | Reuse/integration surface | Caveat |
|---|---|---|---|
| CLI agent safety: Plan mode, sandbox, tool-scope restriction, granular approvals, YOLO restriction, PAT-scoped YOLO | **Shipped** (v6.1.0 → v6.4.0 → v6.5.0) | admin console, `settings.json`, PAT scopes | Not exercised; no third-party security test |
| Governance: admin MCP allow-lists (wildcards), org/team guidelines, tool permissions, Run-Command/Web-Fetch policy | **Shipped** (v6.2.0, v6.3.0, v6.5.0) | MCP, guideline files | Policy enforcement only as vendor states |
| Cost/usage: token/cost API, per-team quotas, fair-use limit, analytics pages | **Shipped**; a cost-data **error** was corrected in v6.6.8 | REST usage APIs, CSV | Vendor telemetry was demonstrably wrong once; tokens ≠ energy |
| Provenance: accepted-code logging (off by default) | **Shipped** (v6.3.0) | CSV export | Logs acceptance, not correctness or reuse |
| Model freedom: self-managed models/BYOAI, OIDC keyless auth, team model assignment | **Shipped** (v6.1.0 → v6.5.0) | provider endpoints | Customer bears model choice/risk |
| Review: PR agent v2, agent-driven review replacing IDE Review/Test tabs | **Shipped** (PR agent); Code Review/Coaching **private beta** | GitHub/GitLab/Bitbucket CI templates | PR-agent repo has no licence |
| OpenCode-based CLI and IDE agent | CLI: **preview** in Aug, GA claim Sep 15. IDE agent: **beta** | `tabnine-opencode` launcher; upstream MIT | Wrapper source not public; versions flagged unstable |
| Enterprise Context Engine | Pre-existing: introduced in a Mar 5, 2026 post (before the window; seen only as an index listing; GA status not verified). Post-acquisition to be integrated into Tricentis QE platform (**announced_only** direction) | connected repos, Azure DevOps/TFVC indexer | Vendor outcome claims (2× accuracy, −80% tokens) are unaudited |
| Shared multi-agent memory | **Commentary only** (Jun 18) | — | Not a release |

## 5. Publicly stated direction versus shipped functionality

| Dated source | Stated intention | Classification |
|---|---|---|
| [May 6 recap](https://www.tabnine.com/blog/april-recap-agents-you-can-trust/) | "We've got some (really) bigger things coming next." | Vague teaser; **announced_only** with no scope |
| [Jul 30 Tabnine](https://www.tabnine.com/blog/a-new-chapter-for-tabnine/) / [Tricentis](https://www.tricentis.com/news/tricentis-acquires-tabnine) | The Context Engine "becomes part of the Tricentis Agentic Quality Engineering Platform"; "Existing customers will continue to receive support for the products they use today." | Integration is **announced**. "Support" is **not** a development or roadmap commitment for the coding assistant |
| [Aug 2 critique](https://www.beri.net/article/tricentis-tabnine-acquisition-air-gapped-coding-assistant-roadmap-risk) | Argues the standalone assistant and air-gapped roadmap are unaddressed | Independent opinion. **Partly contradicted** by continued releases (v6.5.0–v6.6.9 through Oct 8) and **partly consistent** with the blog going silent and the 2026-10-16 site redirect |
| Sep 15 v6.6.0 | Moved the CLI onto OpenCode for all customers | **Shipped** pivot from an in-house CLI to a wrapped OSS agent |

The data support two rival readings. (a) Tabnine is being kept as a maintained enterprise coding product under Tricentis. (b) Tricentis is harvesting the Context Engine and moving the assistant onto commodity OSS (OpenCode) with minimal investment. **Falsification signals:** an end-of-sale or end-of-life notice, release-notes cadence dropping below one feature release per quarter, or the air-gapped installer disappearing would support (b). A new major version with roadmap commitments would support (a).

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company strategy)

| Hypothesis | Rival cause | Disconfirming observation |
|---|---|---|
| Enterprise coding assistants converge on wrapping an OSS agent core (OpenCode) and differentiating through governance/context | Wrapping is a cost cut by the acquirer, not an industry pattern | Other vendors keep proprietary agent cores while Tabnine's wrapper stalls |
| Admin-side agent governance (MCP allow-lists, PAT-scoped autonomy) becomes a procurement requirement | Customers use generic CI/IAM controls instead | Independent buyers' RFPs do not ask for agent-level governance |
| Acquisition by a testing vendor moves "context" from code generation toward verification | Marketing reframing only | No measurable QE-agent features that use the Context Engine by 2027 |

## 7. M1–M7 study relevance

| Construct | Prospective measurement, not an inferred conclusion |
|---|---|
| **M1** coding practice | Opt-in comparison of Plan-mode/approval workflows against unrestricted agent runs on frozen tasks |
| **M2** accepted quality | Independently authored acceptance tests; count refusals and failures; do not use accepted-code logs as a quality measure |
| **M3** discovery | Context Engine claims are not discovery evidence; measure retrieval of the correct existing module on seeded tasks |
| **M4** verified third-party reuse | The OpenCode wrapping is a concrete **reuse of an MIT upstream** by a commercial vendor; trace whether fixes flow upstream (unknown) |
| **M5** reuse-first | Compare OpenCode as-is, Tabnine's OpenCode wrapper and an in-house CLI for the same governance tasks |
| **M6** lifecycle cost | Vendor token/cost data needed a retroactive correction (v6.6.8). Meter independently; **no token→CO2e conversion** |
| **M7** maintainer actions | Contract-level continuity safeguards (EOL notice, escrow) as a tested procurement checklist, not a growth tactic |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline only, using the synthetic [parser fixture](../../../tests/fixtures/trending.html). Live Trending capture stays **disabled**.

**Practice under test:** reuse an existing MIT agent (OpenCode, pinned version) plus a **repository-level, version-controlled permission policy** (an allow-list of tools/commands and a "plan-then-approve" step) instead of building or buying a bespoke governed agent.

- **Comparator A:** an unmodified pinned OpenCode release with default permissions.
- **Comparator B:** the same build with the checked-in policy (deny network, deny writes outside `trending_study/` and `tests/`, plan approval required).
- **Frozen tasks (preregistered):** 10 synthetic maintenance tasks on the parser and CLI (5 legitimate fixes, 3 that tempt out-of-scope writes, 2 with no valid solution). Hidden acceptance is a human-authored set of tests plus `python3 -m unittest discover -s tests`. The full denominator includes refused, failed and timed-out runs.
- **Endpoints:** primary is tasks accepted without any policy violation divided by all tasks. Secondary: violations attempted vs blocked, reviewer minutes, wall-clock time, metered CI minutes. Record tokens only as vendor-reported, provenance-tagged figures.
- **External-use signal:** publish the policy file. Count only consented external repos that adopt it **and** report a passing run; stars do not count.
- **Cost bound:** ≤ 4 human hours, ≤ 1 model/provider, no paid API added to project scripts.
- **Stop rule:** stop if B blocks a legitimate fix more than once, if any out-of-scope write passes in B, or if policy upkeep exceeds 30 minutes per month. If B is not better, keep A and record the null result.

**No trial executed; no effect estimated.**

## 9. Limitations

- All feature claims are **vendor-reported** (E1/E2). The only independent sources are one news estimate, one critical blog and one GitHub advisory record. None tests product behaviour.
- Tabnine blog content is now reachable only through third-party archive captures. Two rows rest on index listings only.
- Release notes are a living page that has corrected itself at least twice. Rows carry no immutable snapshot.
- Deal value, closing mechanics and post-acquisition headcount are unverified. The "$500M" figure was not used.
- No customer adoption, accepted-task quality, security effectiveness or energy effect was measured.
- Five web queries under a shared budget. Reuters/TechCrunch/The Register targeted searches were not run (see the [search log](019-tabnine.search-log.md)).

## 10. Earlier screen (preserved)

Earlier versions came from commits `dc2aec7`, `7ba740d`, `40ca8e0` and `5063d05` and PRs [#215](https://github.com/MSKazemi/github-trending-1000-study/pull/215) and [#233](https://github.com/MSKazemi/github-trending-1000-study/pull/233) (consolidated in `b90cecc`), with leads from [PR #199](https://github.com/MSKazemi/github-trending-1000-study/pull/199). Those versions were a **3-row "bounded primary-document evidence shortlist"**. They claimed:

- a May 6 recap describing "CLI agent plan/approval and sandbox capabilities" (`shipped`, E1);
- a June 18 shared-memory essay that is "commentary, not a software release" (`reported_undetermined`);
- the July 30 statement that "Tabnine has been acquired by Tricentis", with "closing/legal details still need independent buyer confirmation".

They listed Apr 12–30, August, September and Oct 1–12 as "Not documented in this limited screen". PR #199's two extra leads — the [Context-Readiness post](https://www.tabnine.com/blog/context-readiness-ai-coding-benchmark/) (labelled 2026-06-26) and the [Tricentis release](https://www.tricentis.com/news/tricentis-acquires-tabnine) — were held as uncounted leads. Both are now verified and counted (CI2026-019-008, -010). The 2026-10-14 desk check of the [product-news archive](https://www.tabnine.com/blog/category/product-news/) recorded that the July 30 article already redirected to Tricentis. That redirect now covers the whole site.

The earlier version also asked that no [#56 news-corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) IDs be created before review. This upgrade creates none. The earlier experiment compared external users reusing the study CLI with and without a read-only context navigation guide. It is superseded here by §8, and its text remains in git history. The original ledgers and the alternative screen are archived at [source-archives/019-tabnine.2026-10-12-source-ledger.csv](source-archives/019-tabnine.2026-10-12-source-ledger.csv) and [source-archives/019-tabnine.2026-10-13-first-screen.md](source-archives/019-tabnine.2026-10-13-first-screen.md).
