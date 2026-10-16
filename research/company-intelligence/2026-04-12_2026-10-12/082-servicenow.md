# ServiceNow: provisional six-month technology intelligence screen (082)

> **PROVISIONAL, AI-assisted, not human-reviewed (2026-10-16).** This report, its [event ledger](082-servicenow.events.csv) and its [search log](082-servicenow.search-log.md) are an AI-assisted documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a validated task outcome, an exhaustive search, an endorsement, or a security or scientific sign-off.

- **Company watchlist ID:** 082, ServiceNow (slug `servicenow`).
- **Research issue:** [#150](https://github.com/MSKazemi/github-trending-1000-study/issues/150). Corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). The ledger rows are candidate leads for #56. No `NEWS-YYYY-NNNN` items were created.
- **Ownership and product boundaries (as of 2026-10-12):** ServiceNow, Inc. (NYSE: NOW), a publicly listed company headquartered in Santa Clara, California (per its press-release datelines). No parent company. In-scope acquired brands that now ship inside ServiceNow products: **Moveworks** (added to the platform per a 2026-02-26 release, pre-window), **Veza** (closed 2026-03-02, pre-window), **Armis** (closed 2026-04-20, in window) and **Traceloop** (described as "recently completed" on 2026-05-05; closing date not stated in the sources read). Filing-level verification was **not** performed. EDGAR was not contacted.
- **Product URL and channels:** [servicenow.com](https://www.servicenow.com/) (timed out or returned HTTP 403 to every request in this screen), [newsroom](https://newsroom.servicenow.com/press-releases/default.aspx) (HTML behind a Cloudflare challenge; the site's public JSON press-release feed and the official PDF copies on its q4cdn CDN could be read), [ServiceNowDocs](https://github.com/ServiceNow/ServiceNowDocs) (official release notes as markdown), [ServiceNow SDK releases](https://github.com/ServiceNow/sdk/releases), [npm `@servicenow/sdk`](https://www.npmjs.com/package/@servicenow/sdk), the [ServiceNow GitHub organisation](https://github.com/ServiceNow), the [ServiceNow-AI Hugging Face organisation](https://huggingface.co/ServiceNow-AI), and NVD records where ServiceNow PSIRT is the CNA.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were read on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass. Factual reviewer and review date are **pending**.
- **Status:** screened (provisional). The ledger has 35 dated rows that cover all seven calendar segments.
- **Scope:** As a large company, ServiceNow was screened against the issue's study angle: governed enterprise agents, developer tooling (Build Agent, the SDK, MCP), open-source repos and models, and security advisories. Customer wins, regional surveys, executive hires and most partner announcements were logged and excluded (see the search log).

## 1. Search and inclusion audit

Summary only. Exact requests, decisions and exclusions are in the [search log](082-servicenow.search-log.md). Search-engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | newsroom JSON feed (`/feed/PressRelease.svc/GetPressReleaseList`, year=2026) | all 2026 items, filtered to 2026-04-12..10-12 | 143 in-window items (press releases plus vendor-curated "in the news" links) | ~60 titles; 28 PDFs read | 18 rows | customer stories, surveys, hires, regional offices, German duplicates | Detail HTML pages blocked (Cloudflare); PDFs read instead |
| 2026-10-16 | GitHub API (`ServiceNow/sdk`, `ServiceNow/ServiceNowDocs`, org repo list) and npm registry | releases, repos and versions created or published in window | 10 SDK releases; ~17 new org repos | all | 9 rows | small or workshop repos, internal decks | Stars and forks are not adoption |
| 2026-10-16 | NVD CVE API 2.0 (`sourceIdentifier` = ServiceNow PSIRT CNA identifier) | pubStartDate 2026-04-12 to 2026-10-12 (two ranges) | 10 CVEs | 10 | 3 rows (grouped by KB bulletin) | none | KB bulletins require a support login |
| 2026-10-16 | HN Algolia API + one web search | `ServiceNow` and 12 variants | 16 stories for the main query | ~25 linked pages | 8 rows | Reddit, Ask HN, paywalled Fortune/Bloomberg | BleepingComputer, CPO Magazine and Security Boulevard returned 403 |

## 2. Verified company/product identity and baseline

ServiceNow sells a hosted workflow platform (the "ServiceNow AI Platform") with release families named after places. In-window evidence:

- **Australia** family: feature Early Availability on 2026-03-12 (pre-window). Patches 2 to 7 shipped in window.
- **Brazil** family: Early Availability on 2026-09-24. Patch 1 followed on 2026-10-08 ([available-versions, Brazil](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/brazil/markdown/release-notes/available-versions.md)).

The platform runtime is proprietary. The public developer surfaces are:

- **ServiceNow SDK ("Fluent")**: npm metadata says MIT, but the GitHub API detects **no licence** on `ServiceNow/sdk`. The conflict is recorded, not resolved.
- **ServiceNowDocs**: product documentation as markdown for LLM use. Its LICENSE file is Apache-2.0, while the GitHub API reports NOASSERTION.
- **Research repos** under the ServiceNow organisation, with mixed licences: EnterpriseOps-Gym Apache-2.0, eva MIT, StarHarness MIT; NOWAI-Bench and Dark-Agent have no detected licence.
- **Apriel open-weight models** on Hugging Face (MIT). **No new ServiceNow-AI model repo was created in the window.** SuperApriel-15B was created on 2026-04-07, five days before the window opened.

Pre-window baseline (context only, not counted):

- the 2026-04-09 release "moves beyond the sidecar AI era" (AI in every package, Build Agent SDK);
- the Anthropic (2026-01-28) and OpenAI (2026-01-20) partnerships;
- the Moveworks FedRAMP Moderate release (2026-02-25);
- the Veza close (2026-03-02).

Post-window items are excluded: the "Statement on M&A Misinformation" (2026-10-13) and the AI Passport / third-generation harness releases (2026-10-15).

The company's self-description changed during the window. Press releases from April to July used "the AI control tower for business reinvention". The 2026-10-01 and 2026-10-06 releases use "the Super Intelligence Control Tower for business reinvention" (observed in the PDF boilerplate).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes (ledger rows) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | AI-in-every-package and Build Agent SDK coverage (001; unverifiable: robots.txt-disallowed source, see spot-check); SDK 4.6.0 "AI Skills" for Claude Code/Kiro (002); Armis close (003); Q1 results (004); Google Cloud preview (005); ServiceNowDocs LLM-docs repo (007) | [SDK v4.6.0](https://github.com/ServiceNow/sdk/releases/tag/v4.6.0), [Armis PDF](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-completes-Armis-acquisition-closing-the-gap-between-asset-visibility-and-cyber-risk-2026.pdf), [ServiceNowDocs](https://github.com/ServiceNow/ServiceNowDocs) | [The Register 04-13](https://www.theregister.com/2026/04/13/servicenow_ai_everywhere/); [CNBC 04-23](https://www.cnbc.com/2026/04/23/software-stocks-plunge-on-servicenow-ibm-results-ai-fears-escalate.html) (shares about -18%) (006) | Register article of 04-11 (Salesforce vs ServiceNow) is pre-window |
| 2026-05 | Knowledge 2026 (May 5–6): Action Fabric + GA MCP Server (008); AI Control Tower expansion incl. kill switch and AI Gateway (009, TechTarget 010); Project Arc preview + NOWAI-Bench (011); AI specialists (012); Otto + 2030 targets (013); Build Agent in Cursor/Windsurf/Claude Code/Copilot (014); AWS AgentCore + SDK for Kiro (015); MCP Registry + A2A plan (016); SDK 4.7.0 (017) | official PDFs (see CSV) | [TechTarget](https://www.techtarget.com/searchitoperations/news/366642774/ServiceNow-reintroduces-itself-as-an-AI-security-company), [SiliconANGLE](https://siliconangle.com/2026/05/05/servicenow-bids-become-control-tower-enterprise-ai/), [The New Stack](https://thenewstack.io/servicenow-ai-governance-agents/) | Microsoft Agent 365 preview, Lenovo, FedEx, HR and University releases logged, not ledgered |
| 2026-06 | **Security incident**: unauthenticated API access; hosted fix 06-05 (018, 019); SDK 4.8.0 `now-sdk query` for agents (020); MosaicLeaks agent-privacy research (021) | [HF blog](https://huggingface.co/blog/ServiceNow/mosaicleaks), [SDK v4.8.0](https://github.com/ServiceNow/sdk/releases/tag/v4.8.0) | [Triskele Labs 06-10](https://www.triskelelabs.com/resources/servicenow-security-incident-unauthenticated-api-access-exposing-customer-data), [TechInformed 06-15](https://techinformed.com/?p=38679); BleepingComputer 06-09 inaccessible (403) | Vendor bulletin KB3067321 is login-only. IBM (06-11) and Accenture (06-29) partnership releases logged, not ledgered |
| 2026-07 | CVE-2026-6875 unauthenticated RCE, CVSS v4 9.5 (022); Q2 results and "ninefold" agentic deployments (023); CEO "kill switch" claim (024) | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-6875), [Q2 PDF](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-Reports-Second-Quarter-2026-Financial-Results-2026.pdf) | [SiliconANGLE 07-22](https://siliconangle.com/2026/07/22/servicenow-beats-estimates-raises-outlook-ai-passes-1b-bookings/), [CNBC 07-22](https://www.cnbc.com/2026/07/22/servicenow-ceo-kill-switch-rogue-ai.html) | SDK 4.9.0 (07-17) and Australia Patch 4 (07-09) not ledgered separately |
| 2026-08 | Autonomous Security GA claims (025); Reco "City-Forum" guest-portal campaign (026); Dark-Agent C2 repo (027); SDK 4.11.0 secure-by-default GraphQL API fields (028); StarHarness (029); four CVSS 10.0 CVEs (030) | [Reco](https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow), [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-18885) | Reco (security vendor) | SDK 4.10.0 (08-06) and Australia Patch 5 (08-07) not ledgered separately |
| 2026-09 | Five more CVEs, KB3159623 (031); Brazil EA: Build Agent (Trial) on by default, Autonomous Engineer, agent containment (032) | [Brazil Build Agent notes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/brazil/markdown/release-notes/build-agent-rn.md), [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-13016) | none found beyond vendor | SDK 4.12.0 (09-10), 4.13.0 (09-23), Australia Patch 6 and 5a not ledgered separately |
| 2026-10-01..12 | Flow by ServiceNow, standalone, controlled availability (033); AI Workflow Factory GA + Autonomous Engineer Early Access (034); Australia Patch 7 / Brazil Patch 1 (035) | official PDFs; [available versions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/australia/release-notes/available-versions.md) | none found in window | 10-13 and 10-15 items excluded as post-window |

## 4. Dated event evidence and capabilities

All rows are in the [CSV](082-servicenow.events.csv) (35 rows, IDs `CI2026-082-001`…`035`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-082-002 | 2026-04-15 | SDK "AI Skills" let Claude Code or Kiro build and deploy Fluent apps; auto-generated ACLs for AI agents | npm + GitHub release; licence conflict (npm MIT vs none detected on GitHub) | [release](https://github.com/ServiceNow/sdk/releases/tag/v4.6.0) | [npm registry](https://registry.npmjs.org/@servicenow/sdk) | E2 |
| CI2026-082-008 | 2026-05-05 | Action Fabric: governed workflows exposed to any agent via GA MCP Server; Anthropic first design partner | SKU-gated (Now Assist / AI Native) | vendor blog PDF | Brazil MCP Server Console notes | E1 |
| CI2026-082-014 | 2026-05-06 | Build Agent GA in Studio; skills in Cursor, Windsurf, Claude Code, Copilot; MCP client; AEMC free | some parts dated Q2/Q3 2026 | press PDF | [The New Stack](https://thenewstack.io/servicenow-ai-governance-agents/) (reports Claude Opus 4.6 inside Studio) | E1 |
| CI2026-082-018/019 | 2026-06-10 / 06-15; activity from 06-02, fix 06-05 | Unauthenticated API flaw used to query a subset of hosted instances; vendor attributes activity to researchers / bug bounty | fixed on hosted instances; no CVE at the time | [Triskele Labs](https://www.triskelelabs.com/resources/servicenow-security-incident-unauthenticated-api-access-exposing-customer-data), [TechInformed](https://techinformed.com/?p=38679) | two outlets; vendor KB unreadable | E1 / E2 |
| CI2026-082-022/030/031 | 07-13, 08-27, 09-24 | 10 PSIRT CVEs: four at CNA CVSS v4 10.0, all but one exploitable without authentication (RCE, sandbox escape, SQLi, access control) | hosted instances patched; vendor "not aware of" malicious exploitation | NVD API | CNA-scored; NVD "Awaiting Analysis" | E2 |
| CI2026-082-026 | 2026-08-12 | Attacker queries Service Portal search as guest across organizations; "not a platform vulnerability" | customer configuration exposure | [Reco](https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow) | security vendor, not neutral | E2 (documentary) |
| CI2026-082-032 | 2026-09-24 | Brazil EA: Build Agent (Trial) active by default; Autonomous Engineer spec-to-implementation with test generation; manual agent containment | EA customers only | official release notes (GitHub mirror) | available-versions table | E2 |
| CI2026-082-033 | 2026-10-01 | Flow: standalone chat-based service desk with no platform prerequisite | controlled availability; GA expected Q4 2026 | press PDF | none | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Coding agents and SDK | SDK 4.6.0–4.13.0. Changes include AI Skills and `now-sdk explain` (4.6.0); OAuth client-credentials CI install (4.7.0); `now-sdk query` with live instance data for agents (4.8.0); dependency fixes (4.8.1); ATF `TestSuite()` and secure-by-default GraphQL fields (4.11.0); and MFA plus an OAuth cookie fix (4.13.0). Build Agent GA in Studio (May); Build Agent (Trial) on by default from Brazil (Sep); Autonomous Engineer (Sep EA, Oct Early Access) | shipped / EA |
| Agent interoperability | GA MCP Server and MCP Server Console; MCP Registry (Innovation Lab); A2A Agent Cards "expected by year end"; Build Agent as MCP client (Figma, Miro, GitHub, Box) | mixed; A2A planned |
| Governance and security | AI Control Tower discovery, observability (Traceloop), risk frameworks, AI Gateway, agent containment ("kill switch"); Autonomous Security and Risk (Armis, Veza); AI Agent Access Security | preview → documented in Brazil EA notes |
| Hyperscaler and tool integrations | Google Cloud (preview), Microsoft Agent 365 (preview), AWS Bedrock AgentCore (available), Kiro, NVIDIA OpenShell for Project Arc (early preview) | vendor-stated |
| Open source and research | ServiceNowDocs (Apache-2.0 file); NOWAI-Bench umbrella (no licence detected) with EnterpriseOps-Gym (Apache-2.0) and eva (MIT); StarHarness (MIT); MosaicLeaks research; Dark-Agent (no licence) | observed via GitHub API |
| Security record | June unauthenticated-access incident; 10 CVEs (07-13, 08-27, 09-24); Australia security patch 5a (09-25) | observed (documentary) |
| Pricing / packaging | AI in every package with three AI tiers (pre-window announcement, covered 04-13); AEMC free; Flow sold standalone | vendor-stated |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "By 2030, ServiceNow is targeting $30 billion-plus in subscription revenues, with ServiceNow AI expected to represent over 30%" of ACV | [platform release, 2026-05-05](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-turns-enterprise-AI-chaos-into-control-with-the-platform-for-governed-autonomous-work-2026.pdf) | 2030 | target (uncommitted) | forward-looking disclaimer; April share drop shows market doubt |
| "ServiceNow moves beyond the platform of platforms to become the AI agent of agents" (McDermott) | same | none | positioning | not a product commitment |
| MCP Server "additional features available 2H 2026" | [Action Fabric, 2026-05-05](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise-2026.pdf) | 2H 2026 | planned | features unspecified |
| "A2A Agent Card support expected by year end" | [data foundation, 2026-05-06](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-launches-the-real-time-data-foundation-that-puts-autonomous-AI-to-work-across-the-enterprise-2026.pdf) | end 2026 | planned | not verified as delivered by 2026-10-12 |
| AI Control Tower enhancements: "general availability expected in August 2026" | [AICT release, 2026-05-05](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-expands-AI-Control-Tower-to-discover-observe-govern-secure-and-measure-AI-deployed-across-any-system-in-the-enterprise-2026.pdf) | Aug 2026 | partly evidenced: containment documented in Brazil EA notes (Sep) | GA in August not independently confirmed |
| Tier 2 SOC and Vulnerability Resolution AI specialists "expected to be available in December 2026" | [Autonomous Security, 2026-08-04](https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-delivers-Autonomous-Security-the-industrys-most-complete-security-offering-2026.pdf) | Dec 2026 | planned | — |
| Flow "general availability expected for North America and EMEA in Q4 2026" | [Flow, 2026-10-01](https://s205.q4cdn.com/537566246/files/doc_news/Introducing-Flow-by-ServiceNow-a-new-AI-service-desk-that-deploys-instantly-2026.pdf) | Q4 2026 | planned | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Incumbent workflow platforms will route external coding and assistant agents through governed MCP endpoints instead of competing on the agent itself | GA MCP Server for third-party agents; Build Agent skills shipped into Cursor, Claude Code and Copilot; SDK for Kiro; AWS/Google/Microsoft integrations | Partner announcements are marketing that may not reflect usage; MCP may be superseded | Major customers keep agent actions outside vendor governance; MCP access stays SKU-gated with little third-party use | low–moderate; no usage denominator |
| H2: Pushing developer agents onto platforms raises the cost of platform security defects | In-window: one exploited unauthenticated access issue (June), 10 CVEs incl. four CVSS 10.0 unauthenticated, plus a guest-portal campaign. Meanwhile the SDK gives agents live instance query access | The CVE rate may reflect better disclosure or more bug-bounty activity, not more defects; CVSS is CNA-assigned | Independent audits show no rise in exploitable defects per release as agent features grow | low; n=1 vendor, 6 months |
| H3: "Governed by default" agentic app generation will reduce, not remove, the need for human review | Self-healing test loop, AEMC approvals and Autonomous Engineer test generation are vendor claims; no accepted-task data | Governance features may shift work to approvers rather than reduce it | Controlled tasks show agent-generated platform apps pass hidden acceptance tests at human-equivalent rates with lower review time | unknown |
| H4: Vendors will publish machine-readable docs and agent skills as a discovery channel for developers | ServiceNowDocs (llms.txt, monthly refresh); `now-sdk explain`; Build Agent skills | Docs repos may mainly serve the vendor's own agents | Controlled tasks show no accepted-task gain from LLM-oriented docs vs ordinary docs | low; untested |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Vendors ship "skills" and MCP servers so general coding agents can target their platforms | Count consented repos that use vendor agent skills, and record whether the tasks were accepted | Skills unused outside vendor demos | Only opt-in workflow logs |
| M2 accepted task quality | Vendor test loops and test generation claim quality gates | Hidden acceptance tests on platform-app tasks, with and without vendor skills | No difference in accepted-task rate | All attempts in the denominator |
| M3 discoverability | Heavy press volume (≥13 releases on May 5–6) and 536 stars on ServiceNowDocs | Separate press and star counts from verified use | Press and stars are not reuse | Stars never used as an outcome |
| M4 verified third-party reuse | Open benchmarks (EnterpriseOps-Gym, eva) said to be integrated into NeMo Gym | Trace actual imports at pinned commits | Mentions without execution | Executed tests only |
| M5 rights/security/provenance | Licence conflicts (SDK npm MIT vs repo none; docs Apache file vs NOASSERTION); unlicensed repos; 10 CVEs; incident; agent-provenance field is self-declared | Licence check at a pinned commit before reuse; security review of agent data access | A self-declared `created_by_build_agent` tag is not attestation | Licence files and advisories only |
| M6 review/maintenance and lifecycle cost | Ten SDK releases in six months; a monthly patch train; security patches needing customer action on self-hosted instances | Measure upgrade and migration minutes per SDK minor version | Agents absorb the churn cheaply | No energy inferred from tokens or revenue |
| M7 actionable interventions | Secure-by-default API flags and agent containment as low-cost guardrails | See §8 | Guardrails add friction without reducing exposure | Synthetic tasks only until approval |

Company adoption claims (for example "ninefold" agentic deployments, $1 billion in AWS Marketplace transactions, 66% cost reduction in a customer story) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline CLI and unit-test suite, run as **synthetic, network-free** tasks. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Give coding agents a small, versioned, machine-readable "how to work in this repo" bundle. The bundle would hold an `llms.txt`-style index of `docs/` plus a skill file listing the exact gates (`python -m unittest discover -s tests -v` and the gate CLIs). This mirrors ServiceNowDocs and `now-sdk explain`. Reuse first: assemble it from existing `AGENTS.md` and `docs/` text, with no new tooling and no new dependency.

**Treatment/control and frozen comparable task:** Freeze 10 small synthetic issues (validator edge cases, CSV schema checks, doc-link fixes). The **hidden acceptance tests are written by a person other than the agent operator** and kept out of agent context.
- **Arm A (control):** the current `AGENTS.md` and `docs/` only.
- **Arm B (treatment):** A plus the index/skill bundle.

Both arms use the same agent, model version, prompt template and time budget, with task order randomized. The accepted-task unit is one patch that passes the hidden tests and the full suite and is accepted by the maintainer without rework.

**Success and guardrails:**
- **Primary measure:** accepted tasks out of all 10 assigned. Refused, failed and timed-out tasks stay in the denominator.
- **Guardrails:**
  - no network access during runs and no secrets in the environment;
  - no new dependency added;
  - no change to protocol or capture code;
  - full unit suite green;
  - licence and provenance of any reused snippet recorded.
- **Measured human work:** bundle-authoring minutes and per-task review minutes.
- **Cost:** only actual billed costs. No paid API spend without the maintainer's explicit approval. No energy or CO2e estimate unless metered.

Commit authorship stays with the maintainer.

**Stop/reversal rule:** Drop the bundle if Arm B does not raise the accepted-task count by at least 2 of 10, or if it adds more than 5 review minutes per task on average. Also drop it if keeping the bundle in sync with `AGENTS.md` takes more than 15 minutes per month, since that is drift-maintenance cost. Stop immediately if any run reaches the network or modifies protocol files. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

**Observed/shipped (documentary):**
- ten SDK releases, 4.6.0–4.13.0 (GitHub release and npm times recorded);
- ServiceNowDocs repo and its Brazil EA refresh;
- Australia patches 2–7 and Brazil Patch 1 dates;
- Brazil EA release notes for Build Agent (Trial default) and Autonomous Engineer;
- 10 PSIRT CVEs;
- new public repos (StarHarness MIT, Dark-Agent unlicensed);
- the MosaicLeaks research post.

**Claims/announcements only:**
- MCP Server GA;
- Build Agent in third-party IDEs;
- AI Control Tower kill switch and GA timing;
- Project Arc;
- Autonomous Security availability;
- Flow;
- AI Workflow Factory;
- A2A support;
- 2030 targets;
- "ninefold" deployments;
- customer outcome figures.

**Conjectures and unknowns:** H1–H4 in §6. Also unknown: whether any CVE corresponds to the June incident (none was found in NVD under ServiceNow PSIRT for June), the number of affected customers, and actual agent task outcomes.

**Important contradictory or null evidence:**
- (a) Licence conflicts: SDK npm metadata says MIT while the GitHub API detects no licence; ServiceNowDocs has an Apache-2.0 LICENSE file but the API reports NOASSERTION.
- (b) Date conflicts:
  - ServiceNowDocs README says the repo was created 23 April 2026, but the GitHub API `created_at` is 2026-04-29.
  - Brazil release-note `last_updated` dates (09-10, 09-23) precede the 09-24 EA date.
  - npm publish times precede the GitHub release times by hours for every SDK release checked.
- (c) The June incident: ServiceNow attributes the activity to researchers or bug bounty. An AppOmni CISO, quoted by TechInformed, urged caution, saying anyone who knew the endpoint could access data without authenticating.
- (d) Market skepticism: shares fell about 18% on 2026-04-23 (CNBC) and stayed down more than 30% year to date on 2026-07-22 (CNBC), even though Q2 beat guidance.
- (e) SiliconANGLE's "AI passed $1 billion in ACV" was not found in the Q2 press-release text.
- (f) No new open-weight model was released under ServiceNow-AI in the window (null finding).
- (g) The Reco campaign concerns customer guest-user configuration, not a ServiceNow platform flaw, per Reco.

**#56 candidates (not minted):** The Register 2026-04-13 (robots.txt disallows generic user agents; not re-checkable); CNBC 2026-04-23; TechTarget 2026-05-05; The New Stack 2026-05-06; Triskele Labs 2026-06-10; TechInformed 2026-06-15; CNBC 2026-07-22; SiliconANGLE 2026-07-22; Reco 2026-08-12. Each needs human reading before an ID is assigned.

**Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

An independent reviewer re-fetched the cited sources on 2026-10-16. Pages and PDFs were retrieved with a generic browser User-Agent after checking each host's robots.txt, and PDFs were converted with `pdftotext`. GitHub, npm and NVD were queried through their APIs. No personal identifier was sent to any site.

| Row | Outcome | Note |
|---|---|---|
| CI2026-082-001 | **unverifiable** | theregister.com robots.txt ends with `User-agent: *` / `Disallow: /`, a default-deny for generic user agents. The article was therefore **not** re-fetched. The original screen fetched it with a generic User-Agent against that rule. The row rests on this one source, so its quotes and the "three levels" pricing detail are unconfirmed. Confidence was set to `E0_UNVERIFIABLE_ROBOTS_DISALLOWED_SOURCE`, and the limitation, report §3 and §9 and the search log were annotated. |
| CI2026-082-002 | confirmed | Release notes name Claude Code or Kiro and the `now-sdk-explain` skill, and say `AiAgent`/`AiAgenticWorkflow` auto-generate ACLs. npm 4.6.0 was published 2026-04-15T04:56:53Z and the GitHub release 2026-04-15T21:57:42Z. npm is MIT; GitHub reports no licence. |
| CI2026-082-003 | confirmed | Raw text has "nearly 7 billion devices" and "completion of the Veza acquisition in March 2026". |
| CI2026-082-004 | confirmed | Raw text has $3,671M (+22%), EmployeeWorks, "closed its acquisition of Armis on April 20, 2026", Veza "on March 2, 2026" and ~125 bp from Armis. |
| CI2026-082-006 | confirmed | `datePublished` 2026-04-23T17:04Z. Raw text has "sank about 18% Thursday, its worst day on record", the Middle East "headwind" and AI tools "from companies like Anthropic and OpenAI". |
| CI2026-082-008 | confirmed | "The MCP Server is generally available today and included in every Now Assist and AI Native SKU, with additional features available 2H 2026." |
| CI2026-082-009 | confirmed | Raw text has 30 new enterprise integrations, Traceloop, "Five new risk frameworks aligned to NIST and EU AI Act" and "kill switch". AI Agent Advisor GA is May 2026; Control Tower enters Innovation Lab in May with GA expected August 2026. |
| CI2026-082-010 | confirmed | `datePublished` 2026-05-05T13:00Z. Raw text has the April 28 press-briefing demo (Veza access graph, prompt injection), "enter preview this month and ship in August" and the Forrester analyst's view that autonomy "remains an aspiration for most". |
| CI2026-082-011 | confirmed | Project Arc "is available as an early preview". NOWAI-Bench (EnterpriseOps-Gym, EVA-Bench) is "available now as an open-source release", and NVIDIA is integrating both into NeMo Gym. |
| CI2026-082-013 | confirmed | Raw text has "$30 billionplus in subscription revenues" by 2030, with ServiceNow AI "over 30%" of ACV. |
| CI2026-082-014 | confirmed | Build Agent GA in Studio, "powered by Anthropic models", Cursor/Windsurf/Claude Code/GitHub Copilot, MCP client to Figma/Miro/GitHub. The availability list dates the skills April 2026 and the MCP client Q2 2026. |
| CI2026-082-018 | confirmed | Published Wed 10 June 2026. Raw text has KB3067321 (support portal only), "5 June 2026", "2-3 June 2026", no CVE assigned at time of writing, the Australia-release scope, and the community-reported endpoint as unconfirmed. |
| CI2026-082-019 | confirmed | `datePublished` 2026-06-15T15:16Z. Raw text has the ServiceNow statement ("gain greater access … than intended"), April 22, June 2, "no data was used or retained", KB3067372 and the AppOmni CISO's caution. |
| CI2026-082-022 | confirmed | NVD: published 2026-07-13, CWE-94, CNA CVSS v4 9.5, Awaiting Analysis, "not currently aware of exploitation". |
| CI2026-082-023 | confirmed | Raw text has $3,877M (+24.5%), "increased ninefold in just nine months", 123 transactions and 658 customers. |
| CI2026-082-024 | confirmed | `datePublished` 2026-07-22T22:56Z. The kill-switch quote is verbatim; OpenAI disclosed its agent escape "one day" earlier; the stock is "down more than 30% this year". |
| CI2026-082-027 | confirmed | GitHub API: repo created 2026-08-12T19:50Z, no licence. Description: "Mythic C2 agent with a full in-memory BOF loader for macOS and Linux". |
| CI2026-082-029 | confirmed | GitHub API: repo created 2026-08-25, MIT. |
| CI2026-082-030 | confirmed | NVD: CVE-2026-18885, -18886, -6876 and -74820 were published 2026-08-27, each CNA CVSS v4 10.0, all referencing KB3152242. Their CWEs are 94; 284; 94/693/1284; and 89. All are unauthenticated and "not currently aware of malicious exploitation". |
| CI2026-082-031 | confirmed | NVD: CVE-2026-13016 and -86857 to -86860 were published 2026-09-24, with CNA CVSS v4 from 8.4 to 9.3, all referencing KB3159623. CVE-2026-86857 is the authenticated one, and CVE-2026-86858 says "In August 2026" for the hosted update. |
| CI2026-082-017 / 020 / 028 (timestamps) | confirmed | npm 4.7.0 2026-05-21T17:16Z / GitHub 22:42Z; npm 4.8.0 2026-06-16T09:54Z / GitHub 19:29Z; npm 4.11.0 2026-08-19T14:19Z / GitHub 23:54Z. |

**Counts:** 23 rows checked: 22 confirmed, 0 corrected, 0 wrong, 1 unverifiable (001, robots.txt-disallowed source).

**Robots.txt audit:** theregister.com is the only robots-disallowed source the search log fetched, handled as above. These allow the paths used: newsroom.servicenow.com (including the Q4 feed API), s205.q4cdn.com, cnbc.com, techtarget.com, triskelelabs.com, techinformed.com, huggingface.co, reco.ai, siliconangle.com, thenewstack.io and raw.githubusercontent.com. BleepingComputer, CPO Magazine and Security Boulevard returned HTTP 403 and were not used as row sources.

**Process note:** the search log records one web search and one WebFetch summary (BleepingComputer). No ledger row depends on either; the June incident rows were confirmed from Triskele Labs and TechInformed raw text.

**Qualification:** the search log's "Figures confirmed against raw text" list includes the Register "three levels" figure, which came from a robots-disallowed fetch and cannot be re-confirmed. Every other figure re-checked here matched its source.

*This is an AI-assisted spot-check, not qualified human review.*
