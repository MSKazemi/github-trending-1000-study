# Sonar — provisional six-month technology intelligence screen (095)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](095-sonar.events.csv) and [search log](095-sonar.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 095
- **Research issue:** [#163](https://github.com/MSKazemi/github-trending-1000-study/issues/163); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates are listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** The legal entity on the site footer is **SonarSource Sàrl** (Swiss; press datelines from Geneva and Austin). The brand is "Sonar" ([sonar.com](https://www.sonar.com) and [sonarsource.com](https://www.sonarsource.com/)). The [about page](https://www.sonarsource.com/company/about/) lists Olivier Gaudin as Founder & Chairman and Tariq Shaukat as CEO. No acquisition **of** Sonar was found. Sonar acquired **Gitar** in the window (2026-05-21). Pre-window acquisitions named in Sonar's own pages: AutoCodeRover (NUS research agent, 2025) and Tidelift. No public listing was found, so the company is presumably privately held. Sonar's coverage page links a 2023 TechCrunch funding story, which was not read. Filing-level ownership and investor data were **not** verified, and SEC/EDGAR was not contacted.
- **Product URL and company newsroom:** [press releases](https://www.sonarsource.com/company/press-releases/), [blog RSS](https://www.sonarsource.com/blog/rss.xml) (last 20 items only), [sitemap](https://www.sonarsource.com/sitemap.xml), [community announcements](https://community.sonarsource.com/c/announce/20), [SonarSource GitHub org](https://github.com/SonarSource), [Docker images](https://github.com/SonarSource/docker-sonarqube/releases).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). 35 ledger rows across all seven calendar segments.
- **Source coverage:** All 11 press releases with sitemap `lastmod` from 2026-04 on were read as raw HTML (one, dated 2026-10-13, was outside the window). The `datePublished` of all 379 English blog URLs with a 2026-04+ sitemap `lastmod` was harvested, giving 95 in-window posts, and 26 were read. The community "announce" category was read via the Discourse JSON API (108 topics created in the window; 19 opened). GitHub releases came from `gh api`. Other sources: the npm registry; NVD API (keywords `sonarqube`, `sonarsource`); the Jenkins security advisory; and the Hacker News Algolia API. Independent articles read: SiliconANGLE (2) and The Straits Times; EDB Singapore (a government partner) was read as context. The Statesman and The New Stack were **not fetched**, because their robots.txt disallows Claude agents. DevOps.com returned **HTTP 403**. WebSearch was not used, because the budget was exhausted. See the [search log](095-sonar.search-log.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | sonarsource.com sitemap + raw HTML | press releases, lastmod ≥ 2026-04 | 11 (10 in window) | 11 | 5 rows | Gartner MQ, AWS award, two event PRs (marketing), Open Weights letter (policy); Daybreak PR dated 2026-10-13 (out of window) | index pagination `?page=` disallowed by robots, so sitemap used |
| 2026-10-16 | sonarsource.com blog | 379 URLs, `datePublished` harvested | 95 in window | 26 read | 13 rows (+ checks) | model evaluations, opinion, explainers, case studies | many sitemap URLs are re-dated old posts; `datePublished` used |
| 2026-10-16 | community.sonarsource.com (Discourse JSON) | `announce` category, all pages | 108 in window | 19 opened | 11 rows (+ checks) | weekly roundups, course/video posts, rule-pack posts | staff announcements only; support threads not screened |
| 2026-10-16 | GitHub (`gh api`), npm, Docker releases | SonarSource repos and releases | 100 most recently pushed repos; 8 release feeds | 8 | 5 rows (+ date checks) | per-patch releases folded | patch-level notes only partially read |
| 2026-10-16 | HN Algolia, NVD, Jenkins | `sonarqube`, `sonarsource`, `sonar gitar`; CVE keyword | HN 5 Sonar-related stories; NVD 2 | 7 | 1 row | Flawfinder CVE unrelated | HN engagement minimal; no critical thread found |
| 2026-10-16 | independent press via Sonar's own coverage page | SiliconANGLE, Straits Times, DevOps.com, Statesman, The New Stack, startupticker | 60+ links listed | 6 attempted | 3 used as checks | robots disallow (Statesman, The New Stack), HTTP 403 (DevOps.com), syndication (startupticker) | discovery biased toward coverage Sonar chose to list |

## 2. Verified company/product identity and baseline

Sonar sells **code quality and code security** analysis. The main products are **SonarQube Server** (self-managed; in-window releases 2026.3, 2026.4 and 2026.5 LTA), **SonarQube Cloud**, **SonarQube for IDE**, the free **SonarQube Community Build** (LGPL-3.0, in [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube)) and the paid **SonarQube Advanced Security** (SCA, malicious-package detection). In the window, Sonar repositioned around "AI code verification" and its **Agent Centric Development Cycle (AC/DC: Guide, Verify, Solve)** and added agent-facing products: the SonarQube CLI, the MCP Server, agent plugins, Sonar Vortex, the Remediation Agent, the Hunter Agent and Gitar.

**Licensing boundary (observed 2026-10-16 via the GitHub licence endpoint):**

| Component | Licence |
|---|---|
| Community Build, scanners (`sonar-scanner-cargo`, `@sonar/scan`) and the IDE extensions | LGPL-3.0 |
| `sonarqube-cli` | LGPL-3.0 per its LICENSE text, although the GitHub API reports NOASSERTION |
| `sonarqube-mcp-server`, `sonarqube-agent-plugins`, and the analyzers `sonar-java` and `sonar-python` | **SONAR Source-Available License v1.0** (source-available, not OSI open source) |
| `sonar-migration-tool` | none detected |
| Cloud service, Vortex, the Remediation Agent, the Hunter Agent and Gitar | proprietary, hosted or add-on |

**Pre-window baseline (context only):**

- MCP Server announced 2025-10-07.
- SonarSweep announced 2025-10-21.
- SonarQube Server 2026.1 LTA (2026-01-29).
- Context Augmentation and AC/DC (2026-03-03).
- The [AWS award press release](https://www.sonarsource.com/company/press-releases/sonar-awarded-a-2026-regional-aws-partner-award/) appears in-window but was excluded as recognition rather than a capability.
- **Post-window, excluded:** OpenAI Daybreak partner programme (2026-10-13), vulnerability reachability (2026-10-14), new JS/TS engine (2026-10-14).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | CLI open beta (Apr 13); BYOK/CMK on Cloud Enterprise (Apr 14); Claude Code plugin (Apr 16); Claude Code trust-dialog research (Apr 30) | [community](https://community.sonarsource.com/t/sonarqube-cli-is-now-in-open-beta-and-its-available-to-everyone/181112), [blog](https://www.sonarsource.com/blog/now-available-sonarqube-plugin-for-claude-code/), [blog](https://www.sonarsource.com/blog/claude-arbitrary-code-execution/) | none found | Apr 15 "Gitar" seed-funding post carries a migrated date and was excluded (see log) |
| 2026-05 | Agent plugins 2.0.0 (May 7); Remediation backlog beta (May 13); Server 2026.3 with embedded MCP (May 20); Copilot CLI plugin (May 20); Remediation Agent launch (May 21); **Gitar acquisition** (May 21); Mini Shai-Hulud research (May 26); Hunter alpha (May 26) | [PR](https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/), [PR](https://www.sonarsource.com/company/press-releases/sonar-globally-launches-sonarqube-remediation-agent-at-atxsummit/), [blog](https://www.sonarsource.com/blog/announcing-sonarqube-server-2026-3/) | [SiliconANGLE May 21](https://siliconangle.com/2026/05/21/ai-code-quality-startup-sonar-buys-ai-code-review-startup-gitar/); [Straits Times May 21](https://www.straitstimes.com/tech/ai-debugging-tool-developed-tested-by-spore-engineers-rolled-out-to-tackle-rising-risks) | Gartner MQ PR (May 26) excluded |
| 2026-06 | CLI 1.0 (Jun 10); MCP Server 1.20 with breaking changes (Jun 23); Advanced Security on Team plan (Jun 24); Codex/Cursor plugins (Jun 25); Sonar way profile trimmed (Jun 26); **Vortex + Remediation GA, ARR > $430M** (Jun 30) | [release](https://github.com/SonarSource/sonarqube-cli/releases/tag/1.0.0.2628), [PR](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/) | startupticker.ch (syndicated copy, not independent) | GitHub Agent App post (Jun 2) noted, not ledgered |
| 2026-07 | Java < 21 scanner brownout (Jul 7); Hunter open beta (Jul 9–10); `@sonar/scan` 5.0 breaking change (notice Jul 14, npm Jul 20); Server 2026.4 (Jul 22); Antigravity plugin (Jul 27); Migration Tool (Jul 31); Open Weights letter (Jul 31) | [community](https://community.sonarsource.com/t/brownout-notice-phasing-out-java-21-as-a-scanner-runtime-on-sonarqube-cloud/185016), [blog](https://www.sonarsource.com/blog/introducing-sonarqube-server-2026-4/) | none found | The Open Weights letter is a policy statement and was not ledgered |
| 2026-08 | Open Secure AI Alliance (Aug 10); free Gitar for non-commercial OSS (Aug 17); Gitar ADO/Bitbucket GA (Aug 21); **Java AutoScan incompleteness advisory** (Aug 27); **Hunter Agent GA** (Aug 27) | [community](https://community.sonarsource.com/t/advisory-java-autoscan-analysis-update/187747), [PR](https://www.sonarsource.com/company/press-releases/sonar-launches-sonarqube-hunter-agent/) | [SiliconANGLE Aug 27](https://siliconangle.com/2026/08/27/sonar-launches-hunter-agent-to-find-flaws-code-scanners-cant-see/); DevOps.com (403) | "Return of Shai-Hulud" research (Aug 5) noted only |
| 2026-09 | Jenkins SonarQube Scanner plugin CVE-2026-84665 (Sep 2); Gitar BYO model (Sep 4); R support (Sep 9); four new Cloud languages (Sep 4); Cargo scanner 1.0 (Sep 11) and Rust on Cloud (Sep 22); **Server 2026.5 LTA** (Sep 29) | [Jenkins advisory](https://www.jenkins.io/security/advisory/2026-09-02/), [PR](https://www.sonarsource.com/company/press-releases/sonarqube-server-2026-5-lta-release/) | NVD record of the CVE | Model-evaluation posts (GPT-6, Opus 5.5) excluded |
| 2026-10-01..12 | Remediation Agent on Server (Oct 1); Vortex on Server, metered in tool calls (Oct 6); Community Build 26.10 (Oct 12) | [blog](https://www.sonarsource.com/blog/sonarqube-remediation-agent-is-now-available-on-sonarqube-server/), [blog](https://www.sonarsource.com/blog/sonar-vortex-is-now-available-on-sonarqube-server/) | none found | AI Engineer NY PR (Oct 8) is an event notice and was excluded |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](095-sonar.events.csv) (35 rows, IDs `CI2026-095-001`…`035`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-095-010 | 2026-05-21 | Sonar acquires Gitar (AI code review that fixes PRs until CI passes) | Terms undisclosed; Gitar stays standalone | [PR](https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/) | SiliconANGLE (Fortune 500 vs 100 conflict) | E2 (independent report of vendor event) |
| CI2026-095-009 | 2026-05-21 | Remediation Agent from AutoCodeRover; "3.2% false positive rate" | Paid; rolled out by end June | [PR](https://www.sonarsource.com/company/press-releases/sonar-globally-launches-sonarqube-remediation-agent-at-atxsummit/) | Straits Times repeats vendor/IMDA statements | E1 |
| CI2026-095-014 | 2026-06-23 | MCP Server 1.20: silent zero-issue bug fixed, CORS decoupled from bind address, breaking renames | Source-available licence | [release](https://github.com/SonarSource/sonarqube-mcp-server/releases/tag/1.20.0.2929) | `gh api` | E2 |
| CI2026-095-018 | 2026-06-30 | Vortex: "up to 36%" fewer tokens, "92%" fewer issues; ARR > $430M | Vendor benchmark only | [PR](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/) | none | E1 |
| CI2026-095-026 | 2026-08-27 | Java AutoScan analyses possibly incomplete since early May | Mitigated; scope undisclosed | [advisory](https://community.sonarsource.com/t/advisory-java-autoscan-analysis-update/187747) | none | E2 (vendor incident record) |
| CI2026-095-027 | 2026-08-27 | Hunter Agent GA on Cloud (logic/access-control flaws) | Server "coming soon" | [PR](https://www.sonarsource.com/company/press-releases/sonar-launches-sonarqube-hunter-agent/) | SiliconANGLE | E2 (independent report) |
| CI2026-095-028 | 2026-09-02 | CVE-2026-84665 stored XSS in Jenkins SonarQube Scanner plugin ≤ 2.18.3 | Fixed in 2.19.0 | [Jenkins advisory](https://www.jenkins.io/security/advisory/2026-09-02/) | NVD API | E2 (third-party advisory) |
| CI2026-095-032 | 2026-09-29 | Server 2026.5 LTA brings agentic add-ons to self-managed/air-gapped | Docker tag 2026-09-25 precedes PR | [PR](https://www.sonarsource.com/company/press-releases/sonarqube-server-2026-5-lta-release/) | docker-sonarqube release | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent tooling | SonarQube CLI beta→1.0→1.9 (`sonar integrate` for Claude Code, Copilot, Codex, Cursor, Antigravity; secrets hooks; git pre-commit SCA); agent plugins 2.0.0 skills; GitHub Agent App; MCP Server 1.16–1.28 and an embedded MCP in Server 2026.3 | shipped (vendor) |
| Agentic products | Vortex (pre-generation context plus in-loop verification), Remediation Agent (beta→GA→Server), Hunter Agent (alpha→beta→GA Cloud), Gitar (acquired) | shipped, plan-gated, paid |
| Supply chain / security | Advanced Security on the Team plan (SCA, malicious packages, licence visibility); CycloneDX 1.6 VEX export; BYOK; secrets blocking before LLM context; threat research on agent-config attacks | shipped (vendor) |
| Languages | R/R Markdown, Rust (Cargo scanner 1.0, 122 Clippy rules), DataWeave, Gosu, Groovy, PowerShell; C/C++ taint and CTU betas | shipped / beta |
| Governance | Architecture management on Server at no extra cost (2026.4); "Agentic AI" quality gate; centralized LLM governance (2026.5) | shipped (vendor) |
| Pricing/OSS | Free Gitar for non-commercial OSS (1 year, by application); Vortex metered in tool calls on Server | observed in posts |
| Breaking/maintenance | Java < 21 scanner runtime dropped on Cloud; `@sonar/scan` 5.0 (Node 22.12+, ESM, aliases removed); PySonar drops Python 3.9; MCP argument renames; Sonar way rule removals | observed |
| Quality incidents | Java AutoScan incomplete analysis (May–Aug); MCP `analyze_code_snippet` silently returned zero issues for tsx/jsx before 1.20 | vendor-disclosed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Hunter Agent "support for SonarQube Server coming soon" | [PR 2026-08-27](https://www.sonarsource.com/company/press-releases/sonar-launches-sonarqube-hunter-agent/) | none | planned; 2026.5 LTA PR (Sep 29) says Hunter is purchasable with Server | Delivery on Server not independently observed |
| LLM governance "with support for open-weight models coming soon" | [PR 2026-09-29](https://www.sonarsource.com/company/press-releases/sonarqube-server-2026-5-lta-release/) | none | planned | No date |
| Gitar to integrate with SonarQube "from the moment an agent starts writing code to the moment it lands" | [PR 2026-05-21](https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/) | none | partly delivered (Gitar bundled, BYO model, ADO/Bitbucket) | Integration depth not verified |
| R analysis "will release with 2026.5 for SonarQube Server" | [community 2026-09-09](https://community.sonarsource.com/t/sonarqube-adds-support-for-r/188084) | 2026.5 | stated; 2026.5 shipped Sep 29 | R presence in 2026.5 not checked |
| Remediation Agent "full roll-out to be complete by the end of June" | [PR 2026-05-21](https://www.sonarsource.com/company/press-releases/sonar-globally-launches-sonarqube-remediation-agent-at-atxsummit/) | end of June 2026 | Jun 30 PR calls it GA | Consistent |
| Vortex "Available as a separate subscription … metered in tool calls" | [blog 2026-10-06](https://www.sonarsource.com/blog/sonar-vortex-is-now-available-on-sonarqube-server/) | current | pricing model | Price levels not checked |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Deterministic static analysis will be repackaged as an **in-loop verifier for coding agents** (hooks, MCP, CLI) instead of a CI-only gate | CLI, MCP, plugins for 6+ agents, PostToolUse hooks, Vortex; same pattern across agent vendors | Marketing re-labelling of existing scanners; developers may disable noisy hooks | Agent-hook installs stay rare, or controlled tasks show no gain in accepted-task rate vs CI-only checks | moderate that the packaging persists; low on benefit |
| H2: Verification vendors will add **LLM reasoning layers** (Hunter, Remediation, Gitar) on top of rules, and false-positive/false-negative reporting will become the key differentiator | Hunter "confirms each candidate"; "3.2% false positive rate" claim; MCP silent zero-issue bug | LLM layers may add cost without precision gains | Independent benchmarks show LLM layers no better than rules on the same denominator | low; no public denominators |
| H3: Verification cost will become **usage-metered and coupled to agent activity** | Vortex metered in tool calls; token-reduction marketing (36%) | Seat pricing may persist for most buyers | Sonar or peers revert to seat or LOC pricing by 2028 | low–moderate |
| H4: The **open-core boundary** will keep shifting toward source-available and proprietary layers | Analyzers and MCP under SSALv1; agentic products proprietary; Community Build stays LGPL | Licence choices may stabilise; the free OSS programmes offset the shift | New agent tooling released under OSI licences, or SSALv1 relaxed | moderate for observation, unknown for trend |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Verification moves into the agent loop (hooks after each edit) | Compare repos with agent-hook configs vs CI-only analysis, opt-in only | Hooks installed but ignored or disabled | Consented repos and logs only |
| M2 accepted task quality | In-loop checks may cut rework; default-profile and AutoScan changes shift issue counts without code changes | Hidden-test acceptance with and without an in-loop analyzer; pin the quality profile version | Issue-count drops reflect rule removal, not quality | Pin analyzer/profile versions; all attempts in denominator |
| M3 discoverability | Press volume (acquisition, ARR) high; HN engagement minimal (5 stories, ≤ 4 points) | Separate press counts from use | Press ≠ use | Stars/press never used as outcome |
| M4 verified third-party reuse | LGPL scanners vs SSALv1 analyzers/MCP affect what downstream projects may embed | Licence audit at pinned commit before reuse | Users rely on hosted service, not code reuse | Licence files, not API summaries |
| M5 rights/security/provenance | Agent-config attack research; secrets-before-LLM blocking; plugin CVE in the CI chain | Planted-secret tests; dependency of CI on third-party plugins | Blocking may miss non-pattern secrets | Synthetic secrets only |
| M6 review/maintenance and lifecycle cost | Runtime deprecations, breaking scanner/MCP changes, tool-call metering | Count migration minutes per toolchain change | Changes small in practice | No kWh/CO2e inferred from tokens |
| M7 actionable interventions | A cheap pre-commit or agent-hook secrets/quality check | See §8 | Adds friction with no accepted-task gain | Synthetic tasks until approval |

Company adoption claims (7M+ developers, 75% of the Fortune 100, 750 billion lines a day, ARR > $430M) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), run on synthetic, network-free tasks only. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Run a local static-analysis and secrets check **after each agent edit**, before human review, instead of relying only on CI. Reuse comes first, and no new tooling is built. The comparison is between the tools the repo already runs (`python -m unittest` plus the existing artifact checks; Ruff if already configured) and adding the free LGPL-3.0 **SonarQube for IDE / Community Build** analysis, or the SonarQube CLI secrets hook, as a post-edit step. The SSALv1 MCP server and paid agentic add-ons are excluded unless a human approves their licence and cost.

**Treatment/control and frozen comparable task:** Freeze 12 small synthetic issues, such as validator edge cases, CSV-schema fixes and docstring fixes. Each issue gets **hidden acceptance tests written by someone other than the operator** and kept out of the agent's context. Each issue is done once in each arm, with the order randomized:

- **Arm A:** existing checks at commit time only.
- **Arm B:** Arm A plus the post-edit Sonar analysis at a pinned version (record the exact version and quality-profile name).

Both arms use the same agent, model version, prompt and time box. The accepted-task unit is one patch that passes the hidden tests and the existing suite and is accepted by the human reviewer without rework.

**Success and guardrails:**

- **Primary measure:** accepted tasks out of all 12 assigned. Refused, failed and timed-out tasks count in the denominator.
- **Secondary measures:** new analyzer findings on changed lines at review time, and reviewer minutes per task.
- **Secrets guardrail:** only a planted fake secret is used, and whether each arm blocks it is logged. No real credentials or personal data are used.
- **Dependency guardrail:** no new runtime dependency in the repo, and no network calls from tests.
- **Measured human work:** setup minutes, review minutes, and minutes spent triaging false positives.
- **Cost and authorship:** no paid API or SaaS spend without approval, and no energy or CO2e estimate unless metered. Commit authorship stays with the maintainer.

**Stop/reversal rule:** Keep Arm A and stop if any of these hold:

- Arm B does not raise the accepted-task rate.
- Arm B does not lower reviewer minutes.
- Arm B adds more than 5 minutes of false-positive triage per task.
- Its licence or data-handling terms cannot be confirmed for this repo.

Stop immediately if any tool transmits repository content off the machine without approval. **No trial has been executed and no effect has been estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):**
  - Release timestamps confirmed by `gh api` for the CLI (0.9.0 open beta 2026-04-13, 1.0.0 2026-06-10, up to 1.10.0 on 2026-10-14, which is post-window), MCP Server 1.16–1.28, agent plugins 2.0.0, Cargo scanner 1.0.0, Community Build 26.5–26.10, and Server Docker images 2026.3.0, 2026.4.0 and 2026.5.0.
  - `@sonar/scan` 5.0.0 on npm (2026-07-20).
  - CVE-2026-84665 fix in Jenkins plugin 2.19.0 (Jenkins advisory and NVD).
  - Licence texts for the CLI (LGPL-3.0), the MCP server, agent plugins and analyzers (SSALv1).
- **Claims/announcements only:**
  - Figures: 3.2% false-positive rate, "36%" token reduction, "92%" fewer issues, "44% less likely" outages, "up to 8%" token reduction, "up to 67%" fewer vulnerabilities (SonarSweep), 450 secret patterns, 200 Hunter zero-days, "up to 90%" faster scans, ARR > $430M.
  - Customer and scale numbers.
  - The SWE-bench Verified #1 claim (Sonar Foundation Agent).
- **Conjectures and unknowns:** H1–H4 in §6, and actual accepted-task effects of every agentic product.
- **Important contradictory or null evidence:**
  - (a) SiliconANGLE writes "75% of the Fortune 500" where Sonar writes Fortune 100.
  - (b) Remediation Agent "launch" on 2026-05-21 (paid, staged roll-out) and again on 2026-06-30 ("now generally available"). This is one product with two launch dates.
  - (c) The Server 2026.5.0 Docker release (2026-09-25) predates the GA press release (2026-09-29). The 2026.3.0 Docker image (05-19) predates the blog (05-20).
  - (d) CLI GA: GitHub release 2026-06-10, community post 2026-06-17.
  - (e) Sonar's own advisory says Java AutoScan analyses may have been incomplete from early May to late August.
  - (f) Before 1.20, the MCP server silently reported zero issues for tsx/jsx snippets.
  - (g) A migrated Gitar post dated 2026-04-15 announces a seed round "emerging from stealth". Its date is inconsistent with Gitar's 2024 posts on the same site, so it was not used.
  - (h) Hacker News shows no meaningful in-window discussion; no critical independent article was found.
- **#56 candidates (not minted):** SiliconANGLE 2026-05-21 (Gitar), Straits Times 2026-05-21 (Remediation Agent), SiliconANGLE 2026-08-27 (Hunter), Jenkins advisory 2026-09-02. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
