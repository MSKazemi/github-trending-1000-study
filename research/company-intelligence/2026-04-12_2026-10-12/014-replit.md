# Replit: provisional six-month technology intelligence screen (014)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report and its companion files are **provisional, AI-assisted documentary source leads**. The companion files are the [event ledger](014-replit.events.csv), the [search log](014-replit.search-log.md) and the [source-QC note](014-replit.source-qc-2026-10-16.md). A first version was merged under the maintainer's 2026-10-15 decision (precedent: PRs #67/#81/#86/#87/#93). No qualified human has reviewed any of it. Factual/link review, source-access/rights review and methods review are still pending. Merging is not scientific or security sign-off. Issue #80 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 014. Research issue: [#80](https://github.com/MSKazemi/github-trending-1000-study/issues/80).
- **Window:** 2026-04-12 to 2026-10-12 inclusive.
- **Screens:** first screens ran 2026-10-12 to 2026-10-15. This seven-segment upgrade and source QC ran on **2026-10-16**.
- **Not available:** search-run UTC times, full search-engine result counts, immutable page captures and an independent reviewer.
- **Status:** **30 dated source leads**, covering all seven calendar segments:
  - 11 pre-existing rows. All were re-opened on 2026-10-16; all were reachable and all dates matched.
  - 19 new rows.
  - These are documentary leads, not verified product behaviour, adoption or task outcomes.
- **Official channels checked:**
  - [replit.com](https://replit.com/);
  - the [blog](https://replit.com/blog), which pages 1–2 cover completely for this window;
  - the weekly [docs changelog](https://docs.replit.com/updates), 26 in-window pages;
  - public code under [github.com/replit](https://github.com/replit).
- **Methods:** [company protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) and [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). The company-watch E0–E2 grades used here are **not** the lesson-evidence grades of the [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](014-replit.search-log.md) records two kinds of screen:

- **Census of two first-party channels.** The blog index has 29 in-window posts. The weekly changelog has 113 in-window item headings.
- **Targeted reads.** Individual posts, five general web searches, and read-only GitHub API calls.

**Main gaps in the earlier screens:**

- April 12–30 and May had only partial coverage. October 1–12 had **no** row, and an earlier note said it was "not documented".
- October has **no blog posts** in the window. It is covered here only by the Oct 2 and Oct 9 weekly changelogs and one independent report.

The ledger is a **purposive selection** of material events. It is not a release census or a rate of innovation. Search totals, screened-hit counts and excluded-hit denominators for the web searches are **unknown**, not zero.

**Out-of-window items, explicitly excluded:**

| Date | Item | Note |
|---|---|---|
| Mar 11, 2026 | Agent 4 launch and the $400M round ([blog index p.3](https://replit.com/blog/category/all/3)) | Valuation seen only in secondary search results |
| Jul 2025 | Production-database deletion incident | Pre-window |
| Oct 13, 2026 | Solutions Partners post | Post-window |
| 2022 | `crosis` security advisory | Pre-window |

## 2. Corporate/product identity and rights baseline

- **Company and products.** Replit operates a hosted, browser-and-desktop development platform: Replit Agent (prompt-to-app), Workspace/IDE, Deployments/publishing, databases, connectors and enterprise administration.
- **Legal entity.** The legal parent and ownership were **not checked against filings**. The [upm LICENSE.md](https://github.com/replit/upm) names the copyright holder as "Neoreason d/b/a Repl.it". In the window, Replit acquired **Atta**, a business-analysis/charting startup ([Sep 25](https://replit.com/blog/replit-acquires-atta)); terms were not disclosed.
- **Open-source licences (GitHub API, 2026-10-16).**
  - Replit publishes many supporting components:
    - MIT: [river](https://github.com/replit/river), [nixmodules](https://github.com/replit/nixmodules), [rippkgs](https://github.com/replit/rippkgs), [codemirror-vim](https://github.com/replit/codemirror-vim), [crosis](https://github.com/replit/crosis), [replit-cursor-plugin](https://github.com/replit/replit-cursor-plugin) (created 2026-09-30) and [replit-gemini-extension](https://github.com/replit/replit-gemini-extension);
    - ISC: [replit-py](https://github.com/replit/replit-py);
    - [upm](https://github.com/replit/upm): GitHub reports "Other"; its LICENSE.md starts "MIT License" and points to additional `LICENSES`.
  - Some active repositories have **no detected licence**: `ruspty`, `codemirror-interact`, `replit-object-storage-python`.
  - **The hosted Agent, Workspace, Deployments and Security products are proprietary services.** Nothing above licenses them.
  - Rayfin, the "open-source SDK" in the Microsoft Fabric post, is published by **Microsoft** ([microsoft/rayfin](https://github.com/microsoft/rayfin), MIT), not by Replit.
- **Portable artefacts that matter for reuse.**
  - `SKILL.md` Skills ([Jun 10](https://replit.com/blog/custom-skills)), importable from public GitHub ([Aug 21 changelog](https://docs.replit.com/updates/2026/08/21/changelog)).
  - A Replit MCP server ([Aug 14 changelog](https://docs.replit.com/updates/2026/08/14/changelog)).
  - These are documented interfaces. Their behaviour was not tested.

## 3. Seven-segment dated chronology

| Segment | In-window source evidence (displayed publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 17 changelog](https://docs.replit.com/updates/2026/04/17/changelog): Agent as MCP listing on Google Cloud Marketplace and Opus 4.7 in Power mode. [Apr 21 Security Agent](https://replit.com/blog/meet-replit-security-agent). [Apr 22 Auto-Protect](https://replit.com/blog/auto-protect). [Apr 29 App Monitoring](https://replit.com/blog/app-monitoring) | Auto-Protect is **opt-in, off by default**; the user applies the patch and republishes. Security Agent has no GA/beta label. |
| May | [May 6 Private Publishing + External Access Tokens](https://replit.com/blog/secure-more-apps). [May 7 Security Center 2.0](https://replit.com/blog/security-center). [May 8 independent summary of RedAccess research](https://www.freevacy.com/news/wired/study-finds-security-gaps-in-thousands-of-vibe-coded-apps/7362) (via WIRED). [May 21 Enterprise self-serve](https://replit.com/blog/enterprise-self-serve) | Enterprise self-serve already appears in the [May 15 changelog](https://docs.replit.com/updates/2026/05/15/changelog), so there is a **date discrepancy**. The RedAccess figures pool four platforms. |
| June | [Jun 1 Microsoft Fabric/Rayfin](https://replit.com/blog/microsoft-fabric). [Jun 3 SEO Agent](https://replit.com/blog/seo-agent). [Jun 9 Package Firewall](https://replit.com/blog/package-firewall). [Jun 10 Skills & Custom Instructions](https://replit.com/blog/custom-skills). [Jun 10 Databricks public preview](https://replit.com/blog/databricksjune2026). [Jun 17 Replit in Claude](https://replit.com/blog/replit-claude). [Jun 23 Agent evaluation](https://replit.com/blog/evaluating-and-improving-agent-at-scale) | The Databricks integration is in **public preview**. The evaluation post reports no numbers. |
| July | [Jul 16 "Self-Driving Company"](https://replit.com/blog/self-driving-company): a stated direction. [Jul 24 changelog](https://docs.replit.com/updates/2026/07/24/changelog): cloud price cut effective Aug 1. [Jul 29 Replit Design](https://replit.com/blog/introducing-replit-design) | The Jul 16 post is **announced_only** (intent). The price cut was announced with a future effective date. |
| August | [Aug 14 changelog](https://docs.replit.com/updates/2026/08/14/changelog): MCP server. [Aug 16 governance](https://replit.com/blog/new-enterprise-governance-tools). [Aug 17 black-box pen tests](https://replit.com/blog/black-box-pen-tests). [Aug 18 Free Mode](https://replit.com/blog/replit-introduces-free-mode). [Aug 21 changelog](https://docs.replit.com/updates/2026/08/21/changelog): Skills import from GitHub and Routines. [Aug 26 Intelligent Model Routing](https://replit.com/blog/intelligent-model-routing) | The Admin API is **beta**. In the Aug 16 post the Compliance API and Workspace Settings are **announced only**. |
| September | [Sep 10 Databricks GA](https://replit.com/blog/databricks2026). [Sep 11 changelog](https://docs.replit.com/updates/2026/09/11/changelog): Compliance API prompt text. [Sep 25 Atta acquisition](https://replit.com/blog/replit-acquires-atta). [Sep 29 "Free the models"](https://replit.com/blog/free-the-models) | The Databricks post was **updated Oct 13** (post-window) and its title changed. The Atta post was updated Oct 4. |
| Oct 1–12 | [Oct 2 changelog](https://docs.replit.com/updates/2026/10/02/changelog): Enterprise Workspace settings and new models. [Oct 9 changelog](https://docs.replit.com/updates/2026/10/09/changelog): Replit Desktop for Windows **private preview** (event Oct 7 per [RuntimeWire](https://runtimewire.com/article/replit-windows-desktop-app-preview-local-builds)) | No blog posts in this segment. The [Oct 13 Solutions Partners post](https://replit.com/blog/introducing-replit-solutions-partners) is **excluded**. |

The [CSV](014-replit.events.csv) holds the 30 rows. In it:

- `published_utc` is the displayed source date. It is not an archived UTC timestamp.
- `event_date_utc` is filled only where a source gives a distinct date: the Aug 1 pricing change and the Oct 7 Windows preview.
- An `independent_check_url` that points to another Replit page is **documentary corroboration**, not an independent audit.

## 4. Feature map: today vs newly delivered vs preview vs unverified

| Cluster | Newly delivered in window (vendor-stated) | Preview / announced only | Not verified / counter-evidence |
|---|---|---|---|
| **Agent workflow and models** | Skills (`SKILL.md`) + Custom Instructions (Jun 10). Skills import from GitHub, Routines (Aug 21). Free Mode on GPT-5.6 Luna (Aug 18). Automatic model routing (Aug 26). Self-allocated subagents (Sep 29). New models (Apr 17, Oct 2) | none found | The 65% cost cut for routing and the DeepSWE 72% / Terminal-Bench 49% figures are **vendor-run**. Model swaps change behaviour with no user-side version pin. |
| **Exposure for reuse/integration** | Google Cloud Marketplace MCP listing (Apr 17). Claude connector (Jun 17). Replit MCP server for ChatGPT/Claude/Slack/any MCP client (Aug 14), extended to desktop clients (Sep 11). Fabric deploy target (Jun 1/5). Databricks GA (Sep 10) | Databricks U2M public preview (Jun 10). Windows local builds private preview (Oct 9) | Counterparty statements from Anthropic, Microsoft, NVIDIA and Databricks were not checked. External agents that can **publish** apps widen the permission surface. |
| **Security tooling** | Security Agent (Apr 21). Auto-Protect, opt-in (Apr 22). Security Center 2.0 (May 7). Package Firewall, default on, Socket (Jun 9). Black-box automated pen tests (Aug 17) | microVM migration "currently rolling out" ([Apr 20](https://replit.com/blog/defense-in-depth-how-replit-secures-every-layer-of-the-vibe-coding-stack)) | **Independent counter-evidence:** RedAccess research (May) found over 5,000 exposed vibe-coded apps across Lovable, Replit, Base44 and Netlify. The pooled figure gives no Replit-specific rate. No detection or false-negative rates have been published for any Replit scanner. |
| **Access, governance and privacy** | Private Publishing for Core/Starter + External Access Tokens (May 6). Audit Logs to SIEM (Aug 16). Compliance API prompt retrieval (Sep 11). Workspace settings (Oct 2). Workspace region choice for Pro (Aug 14) | Admin API **beta** (Aug 16) | Retrieving prompt content from employees raises consent questions. Whether any control was enabled in a real deployment is unknown. |
| **Operations and cost** | App Monitoring with read-only agent DB diagnosis (Apr 29). Enterprise self-serve (May 21). Scheduled DB backups (Sep 4 changelog) | Cloud price cut effective Aug 1 (announced Jul 24) | No bills observed. Prices are **not** energy or lifecycle cost. |
| **Design and analysis** | Replit Design, the successor to Canvas (Jul 29). SEO Agent (Jun 3). Atta interactive charts (Sep 25) | none found | "Inline charts" already appear in the **Aug 14** changelog, before the acquisition post. Whether those charts used Atta is unresolved. |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Stated intention (quoted or paraphrased) | Later evidence in window | Classification |
|---|---|---|---|
| [Apr 20 Defense in Depth](https://replit.com/blog/defense-in-depth-how-replit-secures-every-layer-of-the-vibe-coding-stack) | "currently rolling out a replacement of our entire container-based infrastructure with microVMs"; a broader announcement is planned | No dated microVM GA announcement found in the window | **In-progress claim, unverified** |
| [Aug 16 Govern Replit at scale](https://replit.com/blog/new-enterprise-governance-tools) | Workspace Settings "end of the week"; Compliance API "end of August" | Compliance API in the [Sep 11 changelog](https://docs.replit.com/updates/2026/09/11/changelog). Model controls across Workspaces in the [Aug 21 changelog](https://docs.replit.com/updates/2026/08/21/changelog). Full Workspace settings in the [Oct 2 changelog](https://docs.replit.com/updates/2026/10/02/changelog) | **Delivered later than stated** (by changelog date; rollout date unknown) |
| [Jul 16 Self-Driving Company](https://replit.com/blog/self-driving-company) | "We want to bring this new way of working to all of our users", with "policy, permissions, security, and cost controls" | Routines (Aug 21), governance (Aug 16 to Oct 2) and Atta analysis (Sep 25) are *consistent with* this intent. No dated commitment exists. | **Aspiration** |
| [Sep 25 Atta](https://replit.com/blog/replit-acquires-atta) | Recurring investigations feeding slides and team work (vision) | Only interactive charts shipped | **Vision, not delivered** |
| [Sep 29 Free the models](https://replit.com/blog/free-the-models) | Less prescriptive harnesses scale better as models improve (design philosophy) | Model menu changes on Oct 2 | **Engineering position**, vendor-benchmarked |

No source found sets a binding 2027–2031 roadmap.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company strategy)

| Testable scenario | Rival explanation | Disconfirming observation |
|---|---|---|
| Portable `SKILL.md` and MCP exposure make agent practices reusable across vendors | Skills are interpreted differently per harness/model; portability is nominal | The same skill file yields materially different acceptance on two harnesses with a frozen task |
| On-by-default supply-chain and pen-test scanning lowers exposure of generated apps | Exposure is driven by public-by-default publishing and user misconfiguration that scanners do not catch | Independent scans of comparable apps show no difference in unauthenticated-data exposure |
| Agent-driven governance (audit/compliance APIs) is a prerequisite for enterprise agent adoption | Adoption is driven by price and bundling (Free Mode, self-serve), not governance | Uptake indicators do not track governance releases; this needs data we do not have |

## 7. M1–M7 study relevance

| Construct | What this screen offers | What it does **not** establish |
|---|---|---|
| **M1** workflow evolution | Dated shifts toward chat-first "Conversations", Routines, subagents and model routing | Actual user adoption |
| **M2** accepted quality/review | Vendor evaluation methods (ViBench, A/B) and scanning tools | Independently accepted task outcomes |
| **M3** discovery | SEO Agent and default `robots.txt`/sitemap generation | Real traffic or reuse |
| **M4** verified external reuse | MCP server, Claude connector and Marketplace listing as integration surfaces | Any verified downstream use |
| **M5** reuse vs rebuild | `SKILL.md` import from GitHub; Package Firewall on dependency installs; MIT-licensed components | Licence compliance of imported skills; scanner precision |
| **M6** lifecycle cost | Price changes (Free Mode, Aug 1 cloud cut, routing cost claim) | kWh/CO2e (none invented); total human review minutes |
| **M7** ethical maintainer growth | Governance/privacy controls; public-vs-private publishing debate | Any growth effect |

## 8. One falsifiable reuse-first maintainer experiment (proposal, not executed)

**Practice tested:** reuse one **existing**, narrowly scoped `SKILL.md` that points an agent at this repository's existing CLI, instead of letting the agent write a new parser or helper.

- **Repository:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline only. The task uses the committed synthetic [parser fixture](../../../tests/fixtures/trending.html) and the existing `trending_study` CLI. Live `capture` stays **disabled**, and no Replit-hosted copy is made.
- **Comparator.**
  - **A:** the current README/AGENTS.md only.
  - **B:** A plus one pinned `SKILL.md` that names the existing CLI commands and the "reuse before rebuild" rule.
  - Run both on the same agent/model version, in a clean checkout, on 8 frozen tasks. 4 tasks are solvable by reuse; 2 have no reusable solution; 2 are distractors where the skill should **not** fire.
- **Acceptance test.** A person other than the agent author writes hidden tests before any run. Pass means:
  - the output JSONL validates against the existing schema;
  - no new module duplicates `trending_study` parsing (checked by diff review);
  - the full unit suite stays green.
- **Primary endpoint:** independently accepted tasks out of all 8 assigned, counting refusals and timeouts.
- **Secondary endpoints:** false skill activations on distractors, new lines of code, reviewer minutes and billed tokens where available.
- **Verified external-use signal:** one consenting outside user runs task 1 from the README with the skill and reports pass/fail on the hidden test. Stars and views do not count.
- **Cost cap:** about 4 maintainer hours and a fixed token budget set in advance.
- **Stop rule:**
  - Stop early if B's accepted-task rate is not higher than A's.
  - Stop early if B fires on either distractor.
  - Stop early if B adds reviewer time without fewer duplicated modules.
  - In any of these cases, keep A and record the null result. No energy or carbon claim is made.

## 9. Limitations

- **Mostly first-party evidence.** 27 of 30 rows rest on Replit-controlled pages. Three have independent secondary sources (-020 TheCondia, -022 RuntimeWire, -023 Freevacy/WIRED), and these mostly relay claims. **No E3 evidence** exists: no independent test or audit of any feature.
- **Pages change.** Several pages were updated after the window (Databricks Oct 13, Atta Oct 4), and three ledger titles differ from the live titles (see the [QC note](014-replit.source-qc-2026-10-16.md)). No archived captures exist.
- **Weak or inaccessible sources.** The independent security row (-023) comes from an aggregator with an ambiguous date format. Axios and eWeek returned HTTP 403, and the CEO response quoted in search snippets was not verified.
- **Not checked:** counterparty confirmations, plan/region entitlements, the Visa investment claim (aggregator only), Replit's own status-page incident history, and legal-entity filings.
- **Not a sample.** The 100-company watchlist is an editorial list, not a random sample.
- **Unknown and not imputed:** search hit denominators, adoption, accepted-code quality, security efficacy, cost and energy.

## Earlier screen (preserved)

Earlier versions of this report came from several PRs:

- closed-unmerged PR [#196](https://github.com/MSKazemi/github-trending-1000-study/pull/196), with 3 JSON leads;
- original PR #212, with 6 leads (`CI-014-01`..`06`);
- draft PR [#230](https://github.com/MSKazemi/github-trending-1000-study/pull/230), with 3 later-screen leads plus Auto-Protect;
- preservation PR [#300](https://github.com/MSKazemi/github-trending-1000-study/pull/300).

These were consolidated into an 11-row canonical CSV and merged on 2026-10-15 as a provisional screen.

**What that version claimed.** Every row was a vendor document (E0/E1). Apr 12–30, May and Oct 1–12 were described as "not documented in this limited screen". The Package Firewall "8,000 packages daily" figure is a vendor counter with an unknown denominator. The 65% routing cost claim is unreplicated. Search denominators were unknown. An 8-step newcomer-onboarding A/B experiment (README vs AGENTS.md + task card) was proposed. The 2026-10-15 spot-check found no date or claim mismatch, and this upgrade confirms that for all 11 rows.

**Earlier full texts.** Git history holds the earlier versions. The following files keep the originals unchanged; they are provenance, not corroboration:

- [PR #212 original report](source-archives/014-replit.2026-10-12-pr-212-original-report.md) (Git blob `87eba24d0a013bcdccce9105e50f3df4f9b5a98a`; also pinned at [preservation head 4425557](https://github.com/MSKazemi/github-trending-1000-study/blob/4425557fbb54f8e137dfa69afbfa4cb94dbc9e48/research/company-intelligence/2026-04-12_2026-10-12/source-archives/014-replit.2026-10-12-pr-212-original-report.md));
- [PR #196 original report](source-archives/014-replit.2026-10-12-pr-196-original-report.md);
- [#196 first-pass JSON](source-archives/014-replit.2026-10-12-first-pass.events.json);
- [PR #230 first-screen Markdown](source-archives/014-replit.2026-10-13-first-screen.md);
- [initial 22-column ledger](source-archives/014-replit.2026-10-12-source-ledger.csv);
- the [2026-10-14 query checkpoint and 2026-10-15 secondary-source QA](source-audits/014-replit.2026-10-14-qa.md), which first cited the [Axios May 7 report](https://www.axios.com/2026/05/07/loveable-replit-vibe-coding-privacy).

**Not done.** No [#56 news-corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) IDs were minted.
