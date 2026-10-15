# Atlassian: provisional six-month technology intelligence screen (035)

> **PROVISIONAL first-pass screen (2026-10-16), AI-assisted and not reviewed by a human.** This report, its [event ledger](035-atlassian.events.csv) and its [search log](035-atlassian.search-log.md) are **documentary source leads**. No qualified human has checked them. Factual/link review, source-access/rights review and methods review are all **pending**. Nothing here is a validated finding, an adoption measurement or a scientific conclusion. Do not close issue [#102](https://github.com/MSKazemi/github-trending-1000-study/issues/102) on the basis of this file. Verified, deduplicated news items may later feed the evidence corpus in [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56), but only after human review.

- **Company watchlist ID:** 035. **Research issue:** [#102](https://github.com/MSKazemi/github-trending-1000-study/issues/102). **Linked corpus:** [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Analysis window:** 2026-04-12 through 2026-10-12 inclusive. **Source inspection:** 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** collecting. This is a provisional screen of 30 dated source leads covering all seven month segments. It is not independently checked and not exhaustive.
- **Method and template:** [screening protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [report template](../../../templates/company_six_month_intelligence.md). Evidence grades use the company-watch E0–E4 scale. They are **not** the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).
- **Official channels checked:** [atlassian.com](https://www.atlassian.com/), the [company-news blog](https://www.atlassian.com/blog/announcements), the [Bitbucket blog](https://www.atlassian.com/blog/bitbucket), the [developer blog](https://www.atlassian.com/blog/developer), [Jira release announcements](https://jirareleases.atlassian.com/), the [developer changelog](https://developer.atlassian.com/changelog/) (only partly accessible), [security advisories](https://confluence.atlassian.com/security/), [Statuspage incidents](https://jira-software.status.atlassian.com/), SEC EDGAR filings (via the public submissions API for CIK 0001650372) and [github.com/atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server).

## 1. Search and inclusion audit (summary)

The full query-by-query log is in the [search log](035-atlassian.search-log.md): 26 recorded web queries plus direct listings of the official channels above. The search tool gives no hit totals, so found, screened and excluded **counts are unknown, not zero**. Some sources could not be reached:

- Business Wire returned 403 and the Nasdaq copy of the press release timed out.
- The investor press-release page returned 404.
- DevOps.com was blocked by a Cloudflare check.
- Developer-changelog entries before Oct 6 are rendered by JavaScript and were not visible.

Thirty rows were included. Two duplicate groups merge the Team '26 posts and the CVE-2026-21589 advisory with its independent exploitation report. Every segment has at least one dated row. Developer-changelog coverage for Apr–Sep is a documented gap.

## 2. Verified company/product identity and baseline

- **Entity.** The registrant is **Atlassian Corporation**, incorporated in Delaware, with Class A shares listed on Nasdaq as **TEAM**. Its principal office is in San Francisco and its fiscal year ends on June 30. Source: the [FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/0001650372/000165037226000036/team-20260630.htm), filed 2026-08-14 and read for its cover page and business section. The company's earlier history of domicile changes was **not re-verified** in this screen.
- **Acquisitions (baseline, before the window).** The 10-K's XBRL tags give acquisition dates of 2025-10-20 for The Browser Company (Arc/Dia) and 2025-11-10 for DX (engineering intelligence). This screen found **no acquisition announced inside the window**. A 2025 Secoda acquisition appeared only as an aggregator snippet and is unverified.
- **Products relevant to this study.** Jira (including the Jira Coding Agent, Agents in Jira, Planner and Automation), Confluence, Bitbucket Cloud and Data Center (Pipelines, Agentic Pipelines, Merge Queues, code search), Loom, Rovo (chat, agents, Studio, the Rovo/Atlassian MCP server, the Teamwork Graph and its CLI), Rovo Dev (CLI and Code Reviewer), Forge (the app platform), DX, Compass, Bamboo, Crowd, and Fisheye/Crucible.
- **Pre-window baseline.** Rovo Dev became generally available around 2025-10-09 ([DevOps.com](https://devops.com/atlassian-makes-ai-coding-agent-generally-available/)). Data Center end-of-life plans were announced in September 2025, according to the 10-K risk factors. Atlassian announced about 10% layoffs in March 2026 (search result only; outside the window).
- **Undated context, read 2026-10-16 and not used as ledger rows.**
  - The [Rovo Dev licensing FAQ](https://www.atlassian.com/licensing/rovo-dev) says standalone Rovo Dev "will reach end of life" with the final date "TBA". It says Code Reviewer moves into Jira/Teamwork Collection subscriptions with Rovo Credits metering from **2026-12-03**, and that this is "not the Rovo Dev end-of-life date".
  - The [Jira Coding Agent setup doc](https://support.atlassian.com/jira-software-cloud/docs/set-up-jira-coding-agent-in-your-organization/) says the agent is not yet available on Enterprise plans or to organizations requiring HIPAA, BYOK or data residency.
- **Open-source versus proprietary.** The [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) repository is Apache-2.0 and was created 2025-08-01. It contains client plugins, configs, skills and MCP Registry metadata. The hosted MCP service is Atlassian-operated and proprietary. No public specification, repository or license was found for AMP (the Agentic Multiplayer Protocol).

## 3. Month-by-month discoveries

| Month | Announcements and changes (ledger IDs) | Independent reporting | Notes and limitations |
|---|---|---|---|
| 2026-04-12..30 | 001 Apr 21 security bulletin; 002 Apr 22 Google Cloud partnership; 003 Apr 27 Agents in Jira **open beta** | [Futurum, Apr 28](https://futurumgroup.com/insights/atlassian-and-google-cloud-expand-agentic-ai-partnership/) (analysis, not a test) | The undated weekly cloud-changes page was excluded |
| 2026-05 | 004/005 May 6 Team '26 posts; 006 May 14 us-east identity outage; 007 May 19 Agentic Pipelines + Claude Code; 008 May 20 Cursor in Jira | [heise, May 8](https://heise.de/-11287380); [SiliconANGLE, May 6](https://siliconangle.com/2026/05/06/atlassian-opens-teamwork-graph-pushes-rovo-agentic-execution-team-26) | Agents in Jira was beta on Apr 27 and **GA on May 6**: one staged rollout |
| 2026-06 | 009 Jun 16 "Open in coding tool"; 010 Jun 18 Claude Agent for Jira; 011 Jun 25 Agentic Pipelines + Codex; 012 Jun 30 Merge Queues GA | none found | Claude Agent for Jira requires the customer's Anthropic key and a GitHub PAT |
| 2026-07 | 013 Jul 6 EU identity incident; 014 Jul 8 MCP SSE endpoint removed from registry entry (GitHub PR #197); 015 Jul 15/16 AI-native SDLC in Jira; 016 Jul 31 coding-agent automation actions | [IT Brief, Jul 16](https://itbrief.co.uk/story/atlassian-adds-jira-tools-for-ai-native-software-teams) (press-release-based) | The "agent sessions GA on 8 July" claim on dev.to is **unverified** |
| 2026-08 | 017 Aug 5 Forge Container Services **Preview**; 018 Aug 6 Q4 FY26 results; 019 Aug 18 Code Context **open beta**; 020 Aug 30 internal vulnerability-fix case study | [Futurum Q4 note](https://futurumgroup.com/insights/atlassian-q4-fy-2026-can-rovo-turn-ai-usage-into-durable-growth/) (seen in search, not fetched) | "1M MAU" for MCP and CLI is a company metric |
| 2026-09 | 021 Sep 1 MCP v2 endpoint in public client configs; 022 Sep 4 Jira Planner **EAP**; 023 Sep 14 Bitbucket code search **open beta**; 024 Sep 23 public-sector roadmap and Data Center EOL date | none found | Semantic code search is listed as "what's next" |
| 2026-10-01..12 | 025 Oct 5 CVE-2026-21589 (critical); 026 Oct 6 rebuilt MCP server **GA**; 027 Oct 6 OpenAI partnership; 028 Oct 6 AMP; 029 Oct 7 AI-native SDLC; 030 Oct 8 exploitation attempts | [BleepingComputer, Oct 6](https://www.bleepingcomputer.com/news/security/atlassian-warns-of-critical-file-access-flaw-in-jira-confluence/); [SecurityWeek, Oct 8](https://www.securityweek.com/attackers-target-critical-atlassian-vulnerability-within-hours-of-poc-publication/); [Techzine, Oct 7](https://www.techzine.eu/blogs/devops/144826/atlassian-amp-how-can-enterprises-run-and-govern-agentic-ai-teams/) | Team '26 Europe (Amsterdam). Developer-changelog items from Oct 13 onward are **excluded** |

## 4. Dated event evidence and capability inventory

Row-level fields, including product, availability, limitation and confidence, are in the [CSV](035-atlassian.events.csv). The table below groups the rows by capability cluster.

| Cluster (ledger IDs) | What the dated documents support | Availability and limits | Working grade |
|---|---|---|---|
| **Issue-to-agent assignment in Jira** (003, 004, 005, 008, 010, 015, 016) | Work items can be assigned to Rovo, Cursor, GitHub Copilot, Claude and the native Jira Coding Agent. Agents work in a sandbox or cloud and open draft PRs linked back to the work item. Automation rules can dispatch work to agents. Agent actions are logged in Jira's audit trail (vendor statement). | Beta (Apr 27), then GA (May 6) for Agents in Jira. Integrations are "available now" for paid plans with Rovo. Codex is "coming soon". The Coding Agent is excluded for Enterprise and HIPAA/BYOK/residency organizations (undated doc). | E1–E2 |
| **Issue context to local agents** (009) | "Open in coding tool" opens Claude Code, Cursor, Copilot, Codex, Rovo Dev CLI or VS Code with work-item context packaged through Atlassian MCP. | Available now (vendor). The quality of the packaged context has not been tested. | E1 |
| **Agents in CI** (007, 011, 020) | Agentic Pipelines steps run Rovo Dev (the default), Claude Code or Codex from `bitbucket-pipelines.yml`. In an internal case study, one Atlassian team reports more than 55 agent PRs merged and a 95% first-run merge rate. | Open beta. Code, prompts and logs go to the third-party provider, and Atlassian disclaims responsibility for privacy, security and cost. The case study is self-reported, has no comparator and gives no denominator of attempted runs. | E1 |
| **Context and search for agents** (004, 019, 023, 029) | The Teamwork Graph CLI and the graph tools in the MCP server are in open beta (May). Code Context indexes Bitbucket and GitHub repositories with permission-aware retrieval (Aug, open beta). Bitbucket code search is in open beta (Sep). | Beta or EAP. The "44% more accurate, 48% fewer tokens" figures are **internal benchmarks**. GitLab is not mentioned. | E1–E2 |
| **MCP surface** (014, 021, 026) | The rebuilt hosted MCP server is GA (Oct 6) with more than 220 tools, OAuth 2.1 with PKCE, separation of read, write and destructive actions, admin allowlists and audit logs. Public repository history shows the SSE transport removed from the registry entry (Jul 8) and clients pointed at the v2 endpoint (commit Sep 1, merged to main Sep 2 via PR #231). | GA claim. Jira Service Management support is "coming soon". The repository is client configuration only, so server internals cannot be inspected. | E1 (claims); E2 (repo records) |
| **Agent identity and governance** (028, 029) | AMP gives agents identity, scoped authority and reviewable results. Agent Sessions are in closed EAP. Agent accounts and a non-human identity inventory are "soon". DX AI Measurement is GA. | Techzine reports AMP is "not a formal specification", and no public specification was found. | E1 |
| **Merge safety and CI** (012) | Bitbucket Merge Queues are GA for Standard and Premium. | Uses Pipelines build minutes. | E1 |
| **Ecosystem runtime** (017) | Forge Container Services entered Preview, is billable and can be deployed to production and Marketplace. | Not GA; Government Cloud support is targeted for "next year". | E1 |
| **Security** (001, 025, 030) | The monthly Data Center bulletin is dominated by third-party-dependency CVEs. CVE-2026-21589 is critical (vendor CVSS 4.0 9.3; NVD's own CVSS 3.1 score is 7.5 High): unauthenticated file read across eight Data Center products. Cloud was patched. After the watchTowr proof-of-concept on Oct 6, Previdian's honeypots logged 190 attempts by Oct 8. | Attempts are not confirmed compromises. The vendor initially reported no evidence of exploitation. | E2 (advisory); E2 (independent documentary) |
| **Reliability** (006, 013) | Two identity-service incidents with postmortems: May 14 (us-east, 56 minutes) and Jul 6 (EU; automation rules also failed permission checks). | Vendor postmortems; customer impact counts not disclosed. An Aug 27 global incident was seen in a snippet only and is not included. | E2 |
| **Business and usage claims** (018) | The CEO says the MCP server and Teamwork Graph CLI "surpassed one million monthly active users". Q4 revenue was $1,766M (+28%). | MAU is undefined and is not verified reuse or task success. | E2 (that the statement was filed); E0 (as an adoption measure) |

**Vendor assertion versus observation.** Every capability above is **vendor-described**. This screen did not install, configure or exercise any Atlassian product. Two items are directly readable public artifacts: the GitHub repository records (014, 021) and the SEC filing (018). Only the CVE-2026-21589 exploitation reporting (030) comes from parties independent of Atlassian, and even that is honeypot telemetry, not a controlled study.

## 5. What the company says it intends to do

Quotes are under 25 words each. "Status" is this researcher's classification.

| Public direction | Link / date | Horizon | Status | Missing or contradictory context |
|---|---|---|---|---|
| "we're building and shipping in public, every day, alongside our customers" | [Founder post, 2026-05-06](https://www.atlassian.com/blog/company-news/founder-update-team-26) | ongoing | stated intention | Many announced items are beta or EAP, so the cadence claim is not a quality claim |
| Codex is part of a roadmap to orchestrate "all major coding agents" in Pipelines (paraphrase) | [Bitbucket blog, 2026-06-25](https://www.atlassian.com/blog/bitbucket/agentic-pipelines-now-supports-openai-codex) | undated | planned | Still open beta; provider terms shift risk to the customer |
| Codex assignment in Jira "coming soon" | [DEVOPSdigest relay, 2026-07-16](https://devopsdigest.com/atlassian-announces-system-for-ai-native-software-development-in-jira); [SDLC post, 2026-10-07](https://www.atlassian.com/blog/company-news/team26-europe-ai-sdlc) | undated | tentative | Still "coming soon" three months later |
| Government Cloud support for Forge containers targeted "next year"; Bitbucket modules planned | [Forge blog, 2026-08-05](https://www.atlassian.com/blog/development/forge-container-services-preview) | 2027 | planned | Preview only, with no pricing listed |
| Semantic code search listed under "What's next" | [Bitbucket blog, 2026-09-14](https://www.atlassian.com/blog/bitbucket/find-code-faster-improved-search-experience) | undated | uncommitted | Code Context (Aug/Oct) separately claims semantic search in beta |
| IL5 submission "July 2028"; FedRAMP High submission January 2029; Data Center end-of-life March 28, 2029 | [Public-sector post, 2026-09-23](https://www.atlassian.com/blog/company-news/next-chapter-public-sector) | 2028–2029 | planned | A submission is not an authorization. The EOL date affects self-managed users and their security patching |
| "actively exploring" deeper Codex integration; autonomous agents with "built-in human checkpoints" | [OpenAI partnership post, 2026-10-06](https://www.atlassian.com/blog/company-news/atlassian-openai-strategic-partnership) | undated | exploratory | No dates or deliverables |
| Agent accounts and a non-human identity inventory: "Soon, we're adding controls around what is visible to AI" | [AMP post, 2026-10-06](https://www.atlassian.com/blog/company-news/team26-europe-ai-platform) | undated | tentative | AMP has no published specification |
| Jira Service Management support in the MCP server "coming soon" | [MCP post, 2026-10-06](https://www.atlassian.com/blog/company-news/team26-europe-atlassian-mcp) | undated | tentative | n/a |

None of these statements is a guarantee of delivery. They describe Atlassian's stated plans, not independent forecasts.

## 6. Independent interpretation: conditional 2027–2031 scenarios

These are **researcher hypotheses**, not Atlassian strategy and not established fact.

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence and unknowns |
|---|---|---|---|---|
| **H1.** Issue trackers become the dispatch and audit layer for coding agents ("work item to agent to draft PR" as the default path) | Rows 003–005, 008, 010, 015, 016, 029: several third-party agents are wired into Jira assignment, automation and session views within six months | Repository hosts (GitHub/GitLab issues plus native agents) absorb the same role. Assignment may be a marketing surface rather than the workflow developers actually use | Agent Sessions still in EAP through 2027. Third-party integrations deprecated. Independent studies show no accepted-task or review-time difference versus repo-native issues | Low. No independent usage or outcome data. The MAU figure is undefined |
| **H2.** Vendor-hosted MCP servers replace bespoke REST integrations as the main way agents read and write enterprise work data | Row 026 (GA, 220+ tools); row 018 (1M MAU claim); rows 014/021 (transport and endpoint churn) | MCP may be one of several transient standards. REST and SDKs stay dominant for deterministic automation | Further breaking endpoint changes. MCP usage no longer reported. Clients revert to REST | Medium-low. Churn (SSE removal, v1 to v2) suggests a maintenance cost for downstream users |
| **H3.** Organization context ("Teamwork Graph") measurably improves agent task acceptance | Repeated internal claim of 44% higher accuracy and 48% fewer tokens (rows 004, 015, 019) | Gains may come from model upgrades, task selection or benchmark design | An independent replication with frozen tasks finds no difference, or finds higher review rework | Low. The benchmark tasks, denominators and models are undisclosed |
| **H4.** Ending self-managed Data Center moves security burden to the vendor, while legacy self-managed risk peaks before 2029 | Rows 001, 025, 030 (critical Data Center CVE exploited within hours of a proof-of-concept); row 024 (EOL 2029-03-28) | Exploitation pressure on self-managed software is industry-wide, not Atlassian-specific. Cloud carries its own risks (rows 006, 013 identity outages) | The EOL is extended. Cloud incidents with data exposure rise. No further critical Data Center CVEs | Medium for "self-managed risk persists". The share of customers on Data Center is unknown |

## 7. Implications for the GitHub 1000 study

Mapped to the canonical M1–M7 questions in the [research mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding-workflow change | Agent-authored PRs that link back to tracker items (Jira keys, Cursor/Claude PR links) | Repo-month markers (linked issue keys, agent bot authors) with an accuracy audit | Availability is not adoption. Private Jira usage is invisible from public repos | Public repositories only; detector error |
| **M2** accepted quality and review cost | Draft-PR acceptance rate and reviewer minutes per agent PR | Prospective, preregistered frozen-task comparison (section 8) | The vendor's 95% first-run merge figure is self-selected | Count every attempt, including abandoned and refused runs |
| **M3** discovery | Code-search and MCP-registry discoverability of reusable components | Not directly testable from vendor claims. Repository-registry listings could be observed over time | Registry presence is not usage | MCP Registry entries only |
| **M4** verified external reuse | Downstream use of the public MCP client plugins and skills | Audit consented downstream configs that reference `atlassian/atlassian-mcp-server` | Stars and forks are not users. The hosted server cannot be inspected | Apache-2.0 client repo only |
| **M5** reuse-first versus generate | Using an existing tracker-to-agent integration versus writing glue code | A reuse-first arm in section 8 (existing GitHub issue forms versus Jira+MCP) | Licensing, credentials and third-party data terms may outweigh the benefit | Includes license, provider and data-handling review |
| **M6** lifecycle human and energy cost | Setup and administration minutes, Rovo Credits (metered from 2026-12-03 for Code Reviewer per the undated FAQ), Pipelines build minutes | Measure human minutes and billed units. Energy only if actually instrumented | Fewer tokens does not mean less energy. No kWh or CO2e are derived from tokens | Explicitly no carbon numbers |
| **M7** maintainer interventions | Structured issue specs with acceptance criteria handed to agents | Section 8 experiment | The effect may come from the spec quality, not from the tool | Opt-in; maintainer's own repositories only |

**Adoption claims versus outcomes.** Statements such as "Rovo is used by over 90% of enterprise cloud customers" (relayed by SiliconANGLE) and "1M MAU" (row 018) are company adoption claims. They are **not** independent task outcomes, verified reuse or lifecycle-cost evidence.

## 8. One small, falsifiable experiment for the maintainer's repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), restricted to offline tasks such as validators, docs and synthetic-fixture tests. **Live Trending `capture` stays disabled** under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md), and no Atlassian feature changes that.

**Candidate practice (not yet validated):** hand a coding agent a *structured issue specification* (problem, frozen acceptance criteria, files in scope, out-of-scope list) and require a draft PR that traces back to the issue.

**Treatment, comparator and frozen task.** Use 12 bounded tasks drawn from the existing backlog. Freeze them before any run. Include at least two deliberately no-solution or "should refuse" tasks, all of which stay in the denominator. Hidden acceptance tests are authored by a human who is not the agent and are kept out of the agent's context.

- **Arm A (reuse-first comparator):** a GitHub Issue Form with the structured spec, using the maintainer's existing coding agent, a pinned model and a draft PR. No new vendor.
- **Arm B:** the same spec as a Jira work item, handed to the *same* agent and model through "Open in coding tool" or Atlassian MCP context (rows 009 and 026). This arm runs only if the maintainer has approved the Atlassian plan, the Rovo Credits terms and the OAuth scopes. Use read-only MCP scopes where possible.
- Randomize task order. One attempt per task per arm.

**Functional unit:** one task that **passes the hidden acceptance tests and is accepted by an independent human reviewer** without behavioural rework. The denominator is all assigned tasks.

**Guardrails:**
- The full `python -m unittest discover -s tests -v` suite and `scripts/check_research_artifacts.py` stay green.
- Zero credentials, tokens or personal data appear in prompts or logs.
- The agent has no merge rights and no scope outside its branch.
- No network capture.
- No AI attribution trailers. The repository hooks enforce this and are never bypassed.

**Measured human work:** minutes to write each spec, reviewer minutes, rework rounds, and administrative setup minutes for Arm B (Jira site, OAuth app, allowlist). Provider-reported token and billing units are recorded as reported, with **no conversion to energy or CO2e**.

**Stop or reversal rule.** Stop Arm B immediately if any of these happens:

- a credential or secret is exposed;
- an agent acts outside its granted scope;
- the data-handling or provider terms are unclear;
- Arm B setup exceeds a pre-set budget (for example, 4 human-hours).

After 12 tasks, adopt nothing unless Arm B shows **at least 2 more independently accepted tasks than Arm A** with no guardrail breach. Otherwise keep the simpler GitHub-native Arm A. A null result is a valid outcome and must be recorded.

**Status: not run, and no effects estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (vendor-documented, E1–E2):**
  - Agents in Jira GA (May 6, after an Apr 27 beta).
  - Cursor (May 20), Claude (Jun 18) and deeplink handoff (Jun 16) integrations.
  - Jira coding-agent assignment and automation actions (Jul 15/31).
  - Merge Queues GA (Jun 30).
  - Rebuilt MCP server GA (Oct 6).
  - Public MCP client-repo changes (Jul 8, Sep 1).
  - CVE-2026-21589 patches (Oct 5).
- **Preview, beta or EAP:** Agentic Pipelines (Claude, Codex), Teamwork Graph CLI and MCP graph tools, Code Context, Bitbucket code search, Jira Planner, Forge Container Services, Agent Sessions, AI Review, and AMP's identity controls.
- **Claims and announcements only:** Codex in Jira, deeper OpenAI integration, semantic code search, the IL5 and FedRAMP High submission dates, agent accounts and non-human identity inventory, and JSM support in MCP.
- **Conjectures and unknowns:**
  - All productivity, accuracy, token and adoption figures are company-reported (44%/48%, 95% first-run merges, 1M MAU, 90% of enterprise customers).
  - The Rovo Dev standalone end-of-life date is "TBA".
  - The "agent sessions GA 8 July" claim is unverified.
  - Apr–Sep developer-changelog coverage is missing.
- **Contradictory or null evidence:**
  - Agents in Jira was labelled **beta** on Apr 27 and **GA** on May 6, which is consistent with a staged rollout.
  - The Bitbucket blog index image-path month (2026/04) for Merge Queues conflicts with the displayed date (Jun 30); the displayed date is used.
  - Atlassian initially said it had found no evidence of CVE-2026-21589 exploitation, but Previdian logged exploitation attempts within hours of the watchTowr PoC (attempts, not confirmed compromises).
  - Two identity-service outages (May 14, Jul 6) show a shared dependency for permissions and automation, which also gates agent actions.
  - Independent trade coverage (heise, SiliconANGLE, IT Brief, Techzine) relays vendor claims without testing them.
- **Doubtful or weak sources:**
  - Row 015 cites a trade-press relay because the Business Wire original returned 403.
  - The dev.to keynote write-up comes from an Atlassian consultant (a conflict of interest).
  - Futurum discloses vendor engagements.
- **Reviewer links and audit date:** none yet. **Pending:** a human factual/link spot-check of a sample of rows, a source-access/rights review, a methods review, and the PR linked back to [#102](https://github.com/MSKazemi/github-trending-1000-study/issues/102).

## Independent source spot-check (2026-10-16)

A second AI-assisted pass re-read 16 ledger rows plus the entity claim against the cited sources on 2026-10-16. Figures and dates were matched against raw page text (`curl` plus text grep) or the GitHub REST API (repository records); NVD's CVE API was used for the CVE score. No page was archived or hashed. SEC EDGAR refuses automated requests that do not declare a contact identity. This review does not supply one, so the SEC-sourced checks are recorded as unverifiable.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (section 2) | unverifiable | The 10-K is on SEC EDGAR, which refuses undeclared automated access (403). It was not re-checked under this review's no-contact-identity rule. The entity claim stays as the first pass recorded it |
| 001 | confirmed | Bulletin page shows "April 21 2026" and fixed versions "current as of April 21, 2026 (date of publication)". CVE-2022-1471 (9.8) and CVE-2022-25927 (7.5, Bitbucket DC) are listed as stated |
| 003 | confirmed | Dated April 27, 2026; "now in open beta"; GitHub Copilot coding agent and Figma agent named |
| 006 | confirmed | May 14, 2026, 04:30 to 05:26 UTC; us-east race condition during rollback; "mitigated in 56 minutes"; postmortem posted May 19, 2026 19:04 UTC |
| 010 | confirmed | Blog dated June 18, 2026; Standard/Premium/Enterprise with Rovo. The PAT detail is in the Jira release note (dated June 24, 2026), not in the blog |
| 012 | confirmed | Dated June 30, 2026; GA for Standard and Premium; uses existing Pipelines build minutes |
| 013 | confirmed | Jul 6, 2026, 06:51 to 20:17 UTC; cache-lifetime change; an emergency mitigation blocked automation rules from the identity endpoint; postmortem posted Jul 17, 2026 |
| 014 | confirmed | GitHub API: PR #197 merged 2026-07-08T00:03:22Z; head commit f4d9804 (2026-07-07T23:54:55Z) removes the `v1/sse` remote and bumps 1.1.2 to 1.1.3. Repo licence Apache-2.0, created 2025-08-01 |
| 015 | corrected | DEVOPSdigest (July 16, 2026) carries the 44%/48% internal-benchmark figures and "Codex coming soon". The 65% and ~10% figures appear only in IT Brief (16 Jul 2026), so the limitation now attributes them there. Business Wire still returned 403, so the Jul 15 event date stays unconfirmed |
| 018 | unverifiable | SEC EDGAR exhibit; access refused without a declared contact identity, so it was not re-checked. Figures stay as first-pass values awaiting human check |
| 020 | confirmed | Dated August 30, 2026; ">120 vulnerabilities", ">55 agent-created pull requests merged", "Ninety-five percent ... merged on the first run" |
| 021 | corrected | Commit 9956814 was authored 2026-09-01 but reached `main` on 2026-09-02 via PR #231 (merge commit d390144). The Gemini CLI (Sep 3) and MCP Registry v2 (Sep 8 to 9) follow-ups are confirmed |
| 024 | confirmed | Dated September 23, 2026; IL5 submission "July 2028", FedRAMP High "January 2029", Data Center end-of-life "March 28, 2029" |
| 025 | confirmed (note added) | Advisory lists the eight products and vendor CVSS 4.0 9.3 Critical, and says no evidence of exploitation was found; page "Last modified on Oct 5, 2026". NVD (published 2026-10-05) also carries NVD's own CVSS 3.1 score of 7.5 High, which is now noted |
| 026 | confirmed | Dated October 6, 2026; "220+ tools", OAuth 2.1 and PKCE, "up to 25% tokens" on Claude models, JSM "coming soon", "generally available now" |
| 028 | confirmed | Dated October 6, 2026; "It's live across the Atlassian platform today"; agent-account controls "Soon"; local EU AI inference announced |
| 030 | confirmed | SecurityWeek, October 8, 2026: watchTowr PoC on October 6; 190 attempts from 32 IP addresses in 10 countries; not yet in CISA KEV |

**Outcome counts:** 17 checks (16 rows plus the entity claim): 13 confirmed (one with an added note), 2 corrected, 2 unverifiable (SEC EDGAR access policy), 0 wrong. No fabricated URL or figure and no contamination from another company was found. Event IDs are unchanged.

*This is an AI-assisted source spot-check. It is not a qualified human factual, rights or methods review, and those reviews remain pending.*
