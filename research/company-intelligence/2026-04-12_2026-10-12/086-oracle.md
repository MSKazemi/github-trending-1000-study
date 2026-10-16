# Oracle: provisional six-month technology intelligence screen (086)

> **PROVISIONAL, AI-assisted, not human-reviewed (2026-10-16).** This report, its [event ledger](086-oracle.events.csv) and its [search log](086-oracle.search-log.md) are an AI-assisted documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a validated task outcome, an exhaustive search, an endorsement, or a security or scientific sign-off.

- **Company watchlist ID:** 086, Oracle (slug `oracle`).
- **Research issue:** [#154](https://github.com/MSKazemi/github-trending-1000-study/issues/154). Corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). The ledger rows are candidate leads for #56. No `NEWS-YYYY-NNNN` items were created.
- **Product URL and channels:** [oracle.com/artificial-intelligence](https://www.oracle.com/artificial-intelligence/) (starting page), [newsroom](https://www.oracle.com/news/) and its [news sitemap](https://www.oracle.com/news.xml), [OCI release notes](https://docs.oracle.com/en-us/iaas/releasenotes/), [security alerts](https://www.oracle.com/security-alerts/), GitHub organisations [oracle](https://github.com/oracle), [oracle-samples](https://github.com/oracle-samples) and [graalvm](https://github.com/graalvm), and [OpenJDK](https://openjdk.org/) (Oracle-sponsored community).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were read on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass. Factual reviewer and review date are **pending**.
- **Status:** screened (provisional). 40 dated ledger rows cover all seven calendar segments.
- **Scope:** the issue's angle (database-proximate enterprise AI), narrowed to OCI Generative AI, Oracle AI Database agents, Fusion agent tooling, developer SDKs, drivers and MCP servers, Java/GraalVM, security advisories, developer-access changes and contrary coverage. Oracle Health, hospitality, retail, financial-services verticals, analyst rankings and data-centre community statements were screened out on purpose.
- **Evidence grades:** the ledger uses the company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md). No row is above E2.

## 1. Search and inclusion audit

The full request log is in the [search log](086-oracle.search-log.md). Web search was not used (budget exhausted). Discovery came from:

1. **Oracle's news sitemap** (134 in-window URLs, screened by title; 15 opened).
2. **OCI release-note service indexes:** 49 in-window Generative AI notes and 41 Autonomous Database Serverless notes, with the AI-relevant ones opened.
3. **Oracle security-alert pages:** two quarterly CPUs, four monthly CSPUs and one out-of-band alert, all downloaded.
4. **GitHub API** release lists for 17 Oracle repositories, plus commits and PRs.
5. **Hacker News Algolia API** (242 in-window "Oracle" stories) for independent and contrary leads, then the linked articles where reachable and allowed by robots.txt.

**Main gaps:**
- blogs.oracle.com returned HTTP 403, so Oracle's engineering blogs are not covered.
- Reuters and WSJ were paywalled.
- The Register disallows generic agents in robots.txt, so it was not used.
- SEC EDGAR was deliberately not contacted.
- Oracle AI World 2026 (Oct 25–28) falls after the window.

Result counts that were not returned by an API are **unknown, not zero**.

## 2. Verified company/product identity and baseline

- **Entity:** Oracle Corporation, "(NYSE: ORCL)", per the [Q4 FY26 release](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/). Publicly listed; filing-level ownership was **not checked** (EDGAR not accessed).
- **Leadership:** the [Sep 29 release](https://www.oracle.com/news/announcement/oracle-extends-fusion-agentic-applications-with-introduction-of-fusion-claw-2026-09-29/) quotes Mike Sicilia as "CEO, Oracle". An unread Forbes headline listed on Hacker News refers to an Oracle "co-CEO". The leadership structure is **unresolved here**.
- **Brand names in use in the window:**
  - "Oracle AI Database" / "Autonomous AI Database" (26ai).
  - "OCI Generative AI", also called "OCI Enterprise AI" in the Jul 30 release.
  - "Oracle AI Agent Studio for Fusion Applications" and "Fusion Agentic Applications".
  - "Oracle Backend with Firebase APIs (Fusabase)": a Firebase-compatible JS SDK, repository created 2026-05-14.
  - No acquisition of a scoped brand was verified.
- **Pre-window baseline (context, not counted):**
  - The OpenJDK *Interim Policy on Generative AI* is dated 9 April 2026. It bans LLM-generated content in contributions and allows private use for comprehension, debugging and review. Its text did not change in the window (Wayback diff).
  - Enterprise AI Agents in OCI Generative AI reached GA on 2026-03-31.
  - The March 20 Security Alert for CVE-2026-21992.
- **Licences checked (current files, not historical):**
  - UPL-1.0: oracle/mcp, oracle/skills, java-select-ai and go-oracledb.
  - Apache-2.0: agent-spec and wayflow.
  - Dual UPL-1.0/Apache-2.0: rust-oracledb LICENSE.txt and oracledb 26.0.0 on PyPI, although GitHub shows NOASSERTION for both.
  - Proprietary cloud services: OCI Generative AI, Select AI, Fusion Claw and Console AI.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs `CI2026-086-NNN`) | Independent / contrary reporting | Notes |
|---|---|---|---|
| 2026-04-12..30 | 001 GraalVM AI coding-assistant policy; 002 April CPU (481 patches); 003 AI Database Agent for Gemini Enterprise | none in-window (OpenJDK ban is pre-window) | No OCI Generative AI release note in this span |
| 2026-05 | 004 Grok 4.3 on OCI; 005 python-oracledb 4.0.0 (SQL-injection helpers); 006 versioned guardrails; 007 first monthly CSPU; 008 xAI tools incl. code_interpreter | none read | May 1 Department of War agreement read as context only |
| 2026-06 | 009 PeopleSoft CVE-2026-35273 alert (9.8); 012 Always Free Arm allowance halved; 013 June CSPU; 015 Deep Data Security | 010 Ars Technica: exploited as a zero-day since May 27; 011 InfoQ: OpenJDK bans vs GraalVM allows AI contributions; 014 BBC: about 21,000 fewer staff, AI cited | |
| 2026-07 | 016 Select AI agents over A2A; 018 AI-native builder + AI Studio Skill (announced); 019 July CPU (1448 patches); 020 managed MCP server for database agent tools; 021 Console AI preview; 022 Responses API background mode; 023 Cohere alias retirement; 024 Gemini in Agent Studio (planned) | 017 heise: S&P downgrade to BBB- | |
| 2026-08 | 025 rust-oracledb beta; 026 Generative AI in US Gov/DoD clouds; 027 August CSPU (943); 028 NL2SQL model selection | none read | Free-tier enforcement date (Aug 18) only from a third-party blog |
| 2026-09 | 029 IAM per-model restriction; 030 python-oracledb 26.0.0 (year versioning); 031 Q1 FY27 results; 032 Agent Spec drops CrewAI adapter over a dependency CVE; 033 Java 27; 034 September CSPU (673); 035 Select AI for Java; 036 smart model router; 037 Fusion Claw | OpenJDK project page confirms the JDK 27 GA date (033) | |
| 2026-10-01..12 | 038 Document Understanding MCP server; 039 Console AI availability; 040 MCP dependency security remediation | none read | Oct 13 Select AI–Gemini note and Oct 20 CPU are out of window |

## 4. Dated event evidence and capabilities

All 40 rows are in the [CSV](086-oracle.events.csv). The clusters that matter most for the study:

| Cluster | What the cited documents support | What they do **not** support |
|---|---|---|
| **AI-generated contribution governance** (001, 011) | Two Oracle-run projects take opposite positions under the same contributor agreement. OpenJDK bans generative-AI content in contributions (policy dated Apr 9), citing reviewer burden, safety and IP. GraalVM (Apr 14) permits AI-assisted contributions if the human can "explain, defend, or maintain" them, with attribution optional. | Any measured effect on review load, defects or contributor numbers. Whether OpenJDK's planned Skara checkbox was deployed was not verified. Detection of AI content is described by OpenJDK itself as generally "impossible". |
| **Database-proximate agents** (003, 015, 016, 020, 028, 035) | Select AI agent teams can be exposed through a managed A2A server (Jul 7) and their tools through a managed MCP server (Jul 28). They can be exported/imported as JSON and shared across schemas. Deep Data Security adds identity-aware row/column authorization "for AI-powered workloads". NL2SQL defaults to openai.gpt-oss-120b. A Java SDK followed (docs Sep 22, GitHub v1.0.0 Sep 30). | Accuracy of NL-to-SQL, safety of exposing database tools to external agents, or real adoption. All are E2 release notes or E1 press claims. |
| **Fusion agent tooling** (018, 024, 037) | Jul 14: an "AI Studio Skill" for building Fusion agentic apps with VS Code, Git and coding agents (Codex, Claude Code named), plus a public GitHub repository of templates, both **announced**. Sep 29: Fusion Claw, a governed runtime with "Outcome Receipts", and 25 apps stated as available. | Delivery of the promised repository: `oracle/skills/fusion/SKILL.md` is still a placeholder on 2026-10-16, and `oracle-samples/fusion-ai-skills` (Aug 21) is an A-Team skill library whose link to the promise is unconfirmed. No independent evaluation of the "full auto" mode. |
| **OCI Generative AI platform** (004, 006, 008, 022, 023, 026, 029, 036) | A very fast third-party model catalogue (49 notes in five months). An OpenAI-compatible Responses API with background mode and xAI tools including code execution. Semantically versioned guardrails. IAM per-model restriction (inference only). Cross-region routing. | Guardrail efficacy: Oracle's own disclaimer says performance "may vary". Model aliases do retire (023), so "latest" pins carry maintenance cost. |
| **Open-source SDKs, drivers and MCP** (005, 025, 030, 032, 038, 040) | Drivers moved to year-based major versions: python-oracledb 26.0.0 and node-oracledb 7→26. New pure Go and Rust drivers are in beta. Agent Spec removed its CrewAI adapter because of a CVE in a pinned dependency (Chroma DB 1.1.0). oracle/mcp has 34 MCP server directories, and its Oct 9 remediation PR lists remaining dependency gaps. | Quality or uptake of any driver or MCP server; none was executed. |
| **Security cadence** (002, 007, 009, 010, 013, 019, 027, 034) | A new monthly CSPU programme started May 28 alongside quarterly CPUs. Patch counts per bundle: 481 (Apr), 35, 245, 1448 (Jul), 943, 673 (Sep). A PeopleSoft 9.8 flaw was exploited from May 27 per Mandiant/Ars, before the Jun 10 alert, which offered mitigations. Advisory revisions corrected versions and CVSS after release. | That more patches means less secure code; the reason for the July jump is not stated. Exploitation figures are attacker and Google claims, reported second-hand. |
| **Developer access and financial context** (012, 014, 017, 031) | The Always Free Arm allowance was halved in the docs (between Wayback snapshots of 2026-06-05 and 2026-06-12). Q1 FY27: more than 300,000 GPUs delivered, negative USD 5B free cash flow, USD 20B equity raised. S&P cut the rating to BBB-. BBC reports roughly 21,000 fewer staff, with AI deployment cited in the annual report. | Any causal link between the financial strain, the free-tier cut and AI tooling. Workforce figures are not productivity evidence. |

## 5. What the company says it intends to do

| Close paraphrase or short quote (≤25 words) | Link/date | Horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| "A new public GitHub repository will provide templates, starter projects, sample applications, reusable assets, and reference architectures" for Fusion Agentic Applications | [2026-07-14](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) | unstated | planned | Fusion skill folder still a placeholder on 2026-10-16 |
| Gemini models "planned" for Oracle AI Agent Studio; Oracle "plans to use Gemini models" for embedded AI in Fusion and NetSuite | [2026-07-30](https://www.oracle.com/news/announcement/oracle-to-make-gemini-models-available-2026-07-30/) | unstated | planned | Fusion Claw (Sep 29) already says it is powered by Gemini and OpenAI models |
| Fusion Claw: "support for additional frontier models planned over time" | [2026-09-29](https://www.oracle.com/news/announcement/oracle-extends-fusion-agentic-applications-with-introduction-of-fusion-claw-2026-09-29/) | unstated | tentative | |
| Oracle is "executing on a roadmap to bring comparable capabilities" (post-quantum crypto) to JDK releases with long-term support | [2026-09-15](https://www.oracle.com/news/announcement/oracle-releases-java-27-and-strengthens-post-quantum-cryptography-support-2026-09-15/) | unstated | planned | No target LTS version or date |
| Oracle "will propose" a full generative-AI policy to the OpenJDK Governing Board "in due course" | [openjdk.org/legal/ai](https://openjdk.org/legal/ai) (dated 2026-04-09, pre-window) | unstated | planned | No full policy seen by 2026-10-16 |
| CSPUs on the third Tuesday of Feb, Mar, May, Jun, Aug, Sep, Nov, Dec; pre-release announcement the Thursday before | [security-alerts index](https://www.oracle.com/security-alerts/) (read 2026-10-16) | ongoing | announced | The first CSPU (May 28) was a Thursday |
| Console AI: "We plan to add more home regions" | [2026-08-25 note](https://docs.oracle.com/iaas/releasenotes/console/consoleai-preview-oc1-aug-2026.htm) | unstated | planned | |

These are company statements. They are not forecasts by this study and not delivered features.

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher, not Oracle)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence |
|---|---|---|---|---|
| H1. Large vendor-run open-source projects will keep **divergent** AI-contribution rules (ban vs. accountability) for years, and no shared standard will emerge | 001, 011; OpenJDK still on an "interim" policy six months later | OpenJDK may adopt a GraalVM-like accountability policy once IP litigation settles | OpenJDK's full policy permits AI-assisted code, **or** GraalVM tightens to a ban, before 2028 | medium (2027); low beyond |
| H2. Enterprise agents will be exposed mainly through **open protocols (MCP/A2A) wrapped around proprietary runtimes**, so lock-in shifts from APIs to data and governance layers | 016, 020, 032, 037, 038 | Protocol support may be a checklist feature with little real cross-vendor traffic | Independent audits find almost no external A2A/MCP clients calling Oracle-hosted agents | low |
| H3. Database-side authorization (row/column, identity-aware) becomes a common control for agent data access, beyond prompt-level guardrails | 006, 015, 029 | Application-layer policy engines may stay dominant; guardrails may suffice for many cases | Agent incident reports show database-level controls did not reduce data leakage compared with app-layer controls | low |
| H4. Monthly-plus-quarterly patch bundles of rising size raise the **maintenance cost** of on-premises Oracle dependencies | 002, 007, 013, 019, 027, 034; 009/010 zero-day | Bundle size may reflect better scanning (more third-party CVEs), not more risk; cloud customers are patched by Oracle | Patch counts fall back, **or** measured customer patch effort per quarter stays flat | medium for 2026; unknown later |
| H5. Free developer resources shrink when AI-infrastructure spending pressures cash flow, reducing organic onboarding to the vendor's stack | 012, 017, 031 | The free-tier cut may be capacity management or abuse control unrelated to finance | Oracle restores or raises Always Free limits while capex stays high | low |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding-workflow change | Repos adopting agent skills/plugins (oracle/skills ships a Claude Code marketplace); projects adopting ban vs. accountability policies (001, 011) | Count dated policy and skill files in sampled repos at t0 and follow-ups | Files exist without changing practice | File presence is not usage |
| **M2** accepted quality and review cost | Projects with accountability rules vs. bans show different review minutes per accepted PR | The section 8 experiment; matched-project comparison | Policy is not enforced; no difference | AI authorship cannot be reliably detected (OpenJDK says so itself); do not infer it from style |
| **M3** discovery | Vendor SDKs found via vendor docs and events, not organic search; free-tier cuts may reduce first-time onboarding | Referral sources where observable; onboarding funnel only with consent | Free tier is irrelevant to the target users | Stars and HN points are not adoption |
| **M4** verified reuse | Claimed integrations (Gemini Enterprise agent, A2A/MCP, AI Studio Skill) | Trace one consented, working downstream integration per claim | Announced items never ship (018 still pending) | Vendor partner lists count as E1 only |
| **M5** reuse-first, rights and security | Dependency CVE forcing adapter removal (032); year-based versioning breaking pin ranges (030); licence-field NOASSERTION vs files | Licence/advisory/pinning audit of Oracle Python/JS dependencies | Audit finds no actionable issue | Current licence files are not historical licences |
| **M6** lifecycle human and energy cost | Patch-bundle volume (H4); model alias retirements (023); migration to year versions | Log human minutes per upgrade or migration | Costs trivial for small repos | No token-to-CO2e conversion; capex and GPU counts are not energy measurements |
| **M7** actionable interventions | The section 8 experiment | Preregistered pilot with a stop rule | Null result is kept | Small N; no generalisation |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The run uses offline synthetic tests only; the live Trending `capture` stays disabled under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md).

**Candidate practice (not yet validated):** a GraalVM-style **contributor-accountability gate**, adapted from the policy recorded in 001. Every PR must answer three fixed questions in the author's own words before review:
1. What changed and why?
2. How was it verified? (commands run, exit codes)
3. Which existing test or document will catch a regression?

The reviewer rejects any PR whose author cannot answer a follow-up question about the change. The gate deliberately contains **no AI-attribution or disclosure field**. The owner forbids AI contributor attribution, and authorship detection is unreliable.

**Comparator:** the current [PR template](../../../.github/pull_request_template.md) and merge gates, unchanged.

**Frozen task set and functional unit:**
- 12 small, pre-written repository tasks, such as validator rule additions, ledger-schema checks and documentation-consistency fixes.
- Each task has **hidden acceptance tests written by a human before the trial** and kept out of any agent's context.
- Tasks are assigned alternately to the two arms in a fixed, pre-registered order.
- **Functional unit:** one task independently accepted by the hidden tests and a human reviewer. **Every** assigned task counts in the denominator, including abandoned and rejected ones.

**Guardrails:**
- The full unit suite plus `check_research_artifacts.py` must pass before a task can be accepted.
- Any new dependency fails the task unless the reuse gate passes.
- No live network collection.
- No paid API spend without the owner's approval.
- Pinned tool versions are recorded at the start.

**Measured human work:**
- Reviewer minutes per accepted task.
- Review rounds per PR.
- Author minutes spent answering the gate.
- Post-merge reverts or fix-up commits within 30 days.

Energy is **not measured**, and no carbon figure is computed.

**Stop/reversal rule:**
- Stop and do not adopt if, compared with the comparator:
  - the gate adds more than 10 author-minutes per PR on median, **or**
  - accepted tasks fall by 2 or more out of 6, **or**
  - review minutes per accepted task do not fall by at least 20% with no increase in 30-day reverts.
- A null or negative result is recorded as such.
- **No trial has been run; no effect is claimed.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (E2 documentary):**
  - OCI release notes: guardrail versions, xAI tools, background mode, alias retirement, Gov/DoD regions, NL2SQL, IAM model restriction, smart router, Console AI preview and availability.
  - Autonomous AI Database notes: Deep Data Security, A2A, the MCP server and agent framework, and Select AI for Java.
  - Security: two CPUs, four CSPUs and the PeopleSoft alert.
  - GitHub releases and commits: python-oracledb 4.0.0 and 26.0.0, rust-oracledb beta, Agent Spec 26.3.1, java-select-ai 1.0.0, GraalVM CODING_ASSISTANTS.md, oracle/mcp PRs #390 and #487.
  - Java 27 GA (confirmed on openjdk.org).
  - The Always Free documentation change (Wayback).
- **Claims/announcements only (E1):**
  - AI Database Agent for Gemini Enterprise.
  - The AI-native builder, the AI Studio Skill and the promised public repository.
  - Gemini in Agent Studio.
  - Fusion Claw and its 25 apps.
  - Q1 FY27 figures.
- **Conjectures and unknowns:**
  - The section 6 hypotheses.
  - Whether the Fusion templates repository has shipped.
  - Whether OpenJDK's Skara checkbox is live.
  - Why July's CPU was about three times April's.
  - Whether Console AI left its pre-production terms.
  - Exact date of the free-tier documentation change.
  - Oracle engineering-blog content (inaccessible).
- **Important contradictory or null evidence:**
  - PeopleSoft exploited about two weeks before Oracle's alert, with mitigation rather than a full patch reported (010).
  - OpenJDK's ban vs. GraalVM's permission under the same contributor agreement (011).
  - Oracle's own guardrail disclaimer (006).
  - The S&P downgrade and negative free cash flow (017, 031).
  - About 21,000 fewer staff, with AI cited (014).
  - Free-tier halving (012).
  - Promised repository not yet visible (018).
  - Licence-field NOASSERTION vs licence files.
  - The CSPU schedule vs the actual first release day.
- **EDGAR not used:** no SEC filing is cited. EDGAR requires a declared contact identity, and this screen sends no personal identifiers.
- **Reviewer links and audit date:** pending. A human reviewer should:
  - spot-check at least 10 rows, including 009–012, 018, 019 and 032;
  - read the Mandiant/Google report behind 010;
  - check whether the July 14 repository exists under another name;
  - re-run the Wayback diffs for 011 and 012.

Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
