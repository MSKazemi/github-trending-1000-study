# Vercel — provisional six-month technology intelligence screen (027)

> **PROVISIONAL INITIAL EVIDENCE SCREEN (2026-10-16). AI-assisted, NOT reviewed by a qualified human.** This report, its [event ledger](027-vercel.events.csv) (26 rows) and its [search log](027-vercel.search-log.md) are a first-pass **documentary source-lead screen**. They are not an accepted six-month study, verified chronology, license determination, security assessment, product test or empirical reuse result. Factual/link review, source-access/rights review and methods review are all **pending**. Issue [#94](https://github.com/MSKazemi/github-trending-1000-study/issues/94) stays open. No item here has been minted as a [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) news-corpus ID; candidates are listed in section 9 for a human to verify before minting.

- **Company watchlist ID:** 027
- **Research issue:** [#94](https://github.com/MSKazemi/github-trending-1000-study/issues/94); linked corpus initiative [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see section 2. Only partly verified.
- **Product URL and company newsroom:** [vercel.com](https://vercel.com/), [blog](https://vercel.com/blog), [changelog](https://vercel.com/changelog), [Next.js blog](https://nextjs.org/blog), [vercel GitHub org](https://github.com/vercel), [Next.js security advisories](https://github.com/vercel/next.js/security/advisories).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were read on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass for the maintainer; factual reviewer **pending**; methods reviewer **pending**.
- **Status:** screened (first pass). Not independently checked and not published as a finding.
- **Source coverage:** all seven calendar segments contain at least one dated row. The exact queries, the pages opened and the exclusions are in the [search log](027-vercel.search-log.md). Search-engine hit counts, run times in UTC and archived page snapshots were **not captured**, so they are **unknown**, not zero. **Claim grading** uses the company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 (time not recorded) | vercel.com/blog index, read directly | Full blog index (619 posts reported; first 317 rendered) | unknown | about 80 in-window titles read | 19 (plus 2 nextjs.org and 1 KB bulletin) | Customer stories, recaps and hiring/intern posts were excluded as non-events or duplicates | Index text was truncated at the 2024-08 posts. All in-window posts were visible |
| 2026-10-16 | vercel.com/changelog, pages 1–2 | Direct read | 16 | 16 | 0 | All entries were dated Oct 13–15, after the window | The changelog needs deeper pagination. In-window entries were reached through linked pages and community weeklies |
| 2026-10-16 | GitHub REST API (`gh api`) | `repos/vercel/next.js/security-advisories`, `releases`, repo license metadata | 39 advisories / 15 releases listed | all | 4 rows | Advisories before Apr 12 or after Oct 12 were excluded | API data reflects the state at access time |
| 2026-10-16 | Web search (see the log for exact strings) | Incident, acquisition, funding, Ship 2026, Agent Plugins, Next.js security | unknown | about 40 results | 3 independent sources | Aggregator, SEO and mirror pages were excluded | No paywalled outlets were read. No Reuters, Bloomberg or FT item was found |

The included rows are a **purposive, material-event screen**. They are not a census of Vercel releases. The changelog lists dozens of entries per week, many of them AI Gateway model additions, and those were not ledgered individually.

## 2. Verified company/product identity and baseline

- **Entity:** Vercel Inc., a privately held US cloud and developer-platform company. Guillermo Rauch is CEO ([TechCrunch, 2026-04-13](https://techcrunch.com/2026/04/13/vercel-ceo-guillermo-rauch-signals-ipo-readiness-as-ai-agents-fuel-revenue-surge/)). Its last reported primary round was a $300M Series F at $9.3B, led by Accel in September 2025. That is pre-window baseline, as reported by TechCrunch, and has **not** been checked against filings. The founding history (formerly ZEIT) and the cap table were **not verified** at filing level in this pass. **No parent company** was found. No acquisition *of* Vercel was found in the window.
- **Acquisitions by Vercel:** [Better Auth, 2026-07-07](https://vercel.com/blog/vercel-acquires-better-auth) is in the window. Pre-window baseline seen on the blog index includes NuxtLabs (2025-07), Tremor (2025-01), Grep (2024-11) and "new.website joins forces with v0" (2026-03-23). None of these was re-verified here.
- **Offering verification (issue prompt: "v0, deployment and AI SDK"):** confirmed and broader. It covers the hosting/CDN platform, the Fluid compute functions, v0 (an AI app builder plus API), the AI SDK (Apache-2.0, `vercel/ai`), AI Gateway, Vercel Sandbox, the Workflow SDK (Apache-2.0), Next.js (MIT, `vercel/next.js`), the new eve framework (Apache-2.0), Vercel Connect, Vercel Agent and the skills.sh registry. **Open versus proprietary:** the frameworks and SDKs are public repositories (licenses read through the GitHub API or LICENSE files on 2026-10-16). The hosted platform, v0, AI Gateway, Sandbox, Connect and Agent are **proprietary managed services**. An open SDK license gives no rights to, and no portability guarantee for, the hosted service.
- **IPO:** TechCrunch (Apr 13) reports only that the CEO says the company is "getting more ready". One search-result aggregator claimed an S-1 filing in May 2026. That claim was **not verified** and is **excluded**.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | 001 IPO/revenue press; 002 Workflows GA; 003 security incident | [Workflows](https://vercel.com/blog/a-new-programming-model-for-durable-execution), [incident bulletin](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) | [TechCrunch](https://techcrunch.com/2026/04/13/vercel-ceo-guillermo-rauch-signals-ipo-readiness-as-ai-agents-fuel-revenue-surge/), [CyberInsider](https://cyberinsider.com/vercel-confirms-security-incident-as-hackers-claim-to-sell-internal-access/), customer [Trunk](https://trunk.io/blog/vercel-april-2026-incident) | The incident root cause is a compromised third-party AI tool (Context.ai), per Vercel. Threat-actor sale claims are unverified |
| 2026-05 | 004 deepsec OSS; 005 Next.js advisory batch (May 6–7); 006 AI Gateway index; 007 token-theft/BotID | [deepsec](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base), [advisories](https://github.com/vercel/next.js/security/advisories) | [Netlify changelog](https://www.netlify.com/changelog/2026-05-08-react-nextjs-security-vulnerabilities.md) (a competitor's corroboration of the patch set) | Sources disagree on the May advisory count (12 or 13); the GitHub API lists 12 on May 6 plus 1 on May 7 (13 total) |
| 2026-06 | 008 Enterprise Apps & Agents; 009 Connect beta; 010 eve preview; 011 AI SDK 7; 012 Services beta | [Ship 2026 recap](https://vercel.com/blog/vercel-ship-2026-recap) | None found in TechCrunch, The Register or The New Stack | The Ship recap and the Services post give different Services availability (section 4) |
| 2026-07 | 013 Better Auth acquisition; 014 new Vercel Agent; 015 Next.js advisory batch (9) | [Better Auth](https://vercel.com/blog/vercel-acquires-better-auth), [Vercel Agent](https://vercel.com/blog/vercel-agent) | [Dealroom, Jul 9](https://dealroom.co/news/137900-vercel-acquires-better-auth-a-year-after-ethiopian-founders-5m-seed/) (seen only as a search result) | Deal terms are undisclosed |
| 2026-08 | 016 Next.js 16.3; 017 v0 API GA; 018 Agent Plugins 1.0.0; 019 $1M Sandbox challenge; 020 Connect GA; 021 Run SDK; 022 critical Next.js RCE advisories | [Next.js 16.3](https://nextjs.org/blog/next-16-3), [v0 API](https://vercel.com/blog/introducing-the-new-v0-api), [Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) | [Netlify Aug 25](https://www.netlify.com/changelog/2026-08-25-nextjs-security-vulnerabilities.md) | Densest month |
| 2026-09 | 023 libheif disclosure write-up; 024 public bug bounty; 025 State of agent skills | [libheif](https://vercel.com/blog/reproducing-disclosing-and-fixing-the-libheif-vulnerability-with-hacktron-and-the-maintainers), [bug bounty](https://vercel.com/blog/the-vercel-bug-bounty-program-is-now-publicly-available) | Upstream [libheif advisory](https://github.com/strukturag/libheif/security/advisories/GHSA-g89c-p67h-r497) | Next.js advisories on Sep 22 and Sep 30 (one critical `next/og` RCE plus seven others) were seen through the API but **not ledgered**. Flat Rate CDN (Sep 8) was excluded as pricing-only |
| 2026-10-01..12 | 026 Next.js 16.4 | [Next.js 16.4](https://nextjs.org/blog/next-16-4) | none | A Rogo customer story (Oct 2) and a Rillet customer story (Oct 9) were excluded as vendor-authored testimonials. Vercel Sandbox Secure Compute ([Sep 30 changelog](https://vercel.com/changelog/vercel-sandbox-now-supports-secure-compute)) was seen but not ledgered |

## 4. Dated event evidence and capabilities

The full detail is in the [CSV](027-vercel.events.csv). The table below is a summary. The **E grade** is the company-watch tier: E1 means vendor document only; E2 means a dated official record plus a readable artifact (repository, release or advisory) or a second-entity document. **No row reaches E3**, because no independent controlled test or neutral audit was found.

| Event ID | Published / underlying event | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| 001 | 04-13 | CEO says 30% of apps on the platform come from agents; revenue figures come from The Information and Forbes | Not a product event; the share has no stated method | TechCrunch (press) | — | E2 (second entity) |
| 002 | 04-16 / 04-16 | Workflows GA; open-source Workflow SDK; Python SDK beta | GA for TypeScript. Usage figures are vendor-reported | blog | [repo](https://github.com/vercel/workflow) Apache-2.0 | E2 |
| 003 | 04-19 / 04-19 | Compromised third-party AI tool, then Google Workspace, then the Vercel account; non-sensitive environment variables decrypted for some customers | Customer count undisclosed; npm packages reported clean | KB bulletin | [CyberInsider](https://cyberinsider.com/vercel-confirms-security-incident-as-hackers-claim-to-sell-internal-access/); [Trunk](https://trunk.io/blog/vercel-april-2026-incident) | E2 |
| 004 | 05-04 | deepsec: a harness that runs claude/codex agents to find vulnerabilities | Self-reported false positives of about 10–20% | blog | [repo](https://github.com/vercel-labs/deepsec) Apache-2.0 | E2 |
| 005 | 05-06 | 13 Next.js advisories, May 6–7 (bypass, SSRF, XSS, DoS) | Patched; check affected and fixed ranges per advisory | GitHub advisories | Netlify May 8 | E2 |
| 006 | 05-12 | Tool-call share of gateway tokens rose to 58.9% (from 31.6% in Oct 2025) | Single-vendor traffic sample | blog | — | E1 |
| 007 | 05-29 / 04-12 | Inference-theft surge; BotID blocked more than 10k requests | One self-reported case | blog | — | E1 |
| 008 | 06-16 | Passport, Enterprise Managed Users and BYOC-on-AWS for agent governance | Beta and private beta | blog | Ship recap (same vendor) | E1 |
| 009 | 06-17 | Connect: OIDC exchanged for short-lived scoped provider tokens | Public beta; the page was later edited to say GA | blog | — | E1 |
| 010 | 06-17 | eve open-source agent framework | Public preview; other deploy targets are "on the way" | blog | [repo](https://github.com/vercel/eve) Apache-2.0 | E2 |
| 011 | 06-25 | AI SDK 7: tool approvals, WorkflowAgent, experimental HarnessAgent | Breaking changes not enumerated in the post | blog | [repo](https://github.com/vercel/ai) Apache-2.0 | E2 |
| 012 | 06-30 | Services: multi-framework project with internal bindings | Post says **public beta**; the same-day recap says "available July 1" | blog | — | E1 |
| 013 | 07-07 | Better Auth acquired; vendor says it stays MIT | Terms undisclosed | blog | [repo](https://github.com/better-auth/better-auth) MIT; Dealroom | E2 |
| 014 | 07-21 | Vercel Agent: read-only by default, with plan-scoped escalation | Pro/Enterprise; maturity label not stated | blog | — | E1 |
| 015 | 07-21 | 9 Next.js advisories | Patched | GitHub advisories | — | E2 |
| 016 | 08-03 | Next.js 16.3: version-matched `AGENTS.md` docs for coding agents; memory and build-cache gains | Benchmarks run by the vendor on its own apps | nextjs.org | [v16.3.0 release](https://github.com/vercel/next.js/releases/tag/v16.3.0) | E2 |
| 017 | 08-05 | v0 API GA: prompt to sandboxed app, repo/ZIP import, one-call deploy | Old-API chats must be migrated | blog | — | E1 |
| 018 | 08-06 | Agent Plugins 1.0.0, a multi-vendor plugin manifest | No signing or provenance layer in v1 | blog + changelog | [spec repo](https://github.com/agentplugins/agent-plugins-spec): CC-BY-4.0 for text, Apache-2.0 for code | E2 |
| 019 | 08-18 | $1M Sandbox isolation bug-bounty challenge | Results post is dated Oct 14 (outside the window) | blog | — | E1 |
| 020 | 08-25 | Connect GA, adding RBAC and audit logs | Pricing figures conflict with the June page | blog | — | E1 |
| 021 | 08-25 | Run SDK: QuickJS isolation for agent code mode | No escape testing reported | blog | [repo](https://github.com/vercel-labs/run) Apache-2.0 | E2 |
| 022 | 08-25 | Critical AVIF and Windows RCE advisories; fixed in 15.5.24 and 16.3.3 | Exposure depends on the deployment | GitHub advisory | Netlify Aug 25 | E2 |
| 023 | 09-18 / 08-11 | libheif heap overflow reached through sharp/libvips; coordinated fix | Fixed upstream in v1.23.2 | blog | [GHSA-g89c-p67h-r497](https://github.com/strukturag/libheif/security/advisories/GHSA-g89c-p67h-r497) | E2 |
| 024 | 09-24 | HackerOne bug bounty made public | No statistics given | blog | — | E1 |
| 025 | 09-25 | skills.sh: about 1M skills; 0.04% of skills account for 62% of installs | Installs are not unique users | blog | — | E1 |
| 026 | 10-06 | Next.js 16.4: `next upgrade --agent`, `agentUpgrade` and `agentFeedback` (experimental) | Blog dated Oct 6; GitHub release Oct 7 UTC | nextjs.org | [v16.4.0 release](https://github.com/vercel/next.js/releases/tag/v16.4.0) | E2 |

**Feature inventory, grouped by theme:**

- **Agent runtime and SDKs:** AI SDK 7, Workflow SDK GA, eve, Run SDK, Sandbox (challenge and Secure Compute), Vercel Agent.
- **Agent identity and credentials:** Connect (beta, then GA), Better Auth plus the planned Agent Auth, Passport, and Vercel Agent's own identity.
- **Agent-generated UI and delivery:** v0 API GA and Services beta.
- **Discoverability and reuse surfaces:** Agent Plugins 1.0.0, skills.sh, and Next.js version-matched `AGENTS.md` docs plus agent-driven upgrades.
- **Security:** the April incident, 32 Next.js advisories published in the window according to the GitHub API (May 6–7: 13, Jul 21: 9, Aug 25: 2, Sep 22: 1, Sep 30: 7), the libheif coordination, deepsec, and the bug bounty.

**Every item is a vendor assertion.** The only exceptions are that the repository, license and release metadata were read directly from GitHub, and that external parties (Netlify, the libheif maintainers, Trunk and CyberInsider) corroborate the existence and timing of the security events. **None of the functionality was exercised in this screen.**

## 5. What the company says it intends to do

| Close paraphrase of public direction | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Workflows 5 will add concurrency controls, global infrastructure and a snapshot-based runtime | [2026-04-16](https://vercel.com/blog/a-new-programming-model-for-durable-execution) | unstated (beta tag available) | tentative | No date given |
| Agent identity from Better Auth (Agent Auth) to be brought to Connect and eve | [2026-07-07](https://vercel.com/blog/vercel-acquires-better-auth) | unstated | planned | No delivery evidence found by Oct 12 |
| eve deployment to platforms other than Vercel is "on the way" | [2026-06-17](https://vercel.com/blog/introducing-eve) | unstated | uncommitted | A portability claim that cannot be tested yet |
| Vercel Agent will delegate to specialists (security review, design/UX review) "soon" | [2026-07-21](https://vercel.com/blog/vercel-agent) | "soon" | tentative | — |
| Cache Components to become the default in Next.js 17; a future `agentUpgrade` policy will help agents adopt new programming models | [2026-10-06](https://nextjs.org/blog/next-16-4) | next major version | planned | A major-version breaking change implies migration cost for downstream apps |
| Better Auth stays MIT with the same governance | [2026-07-07](https://vercel.com/blog/vercel-acquires-better-auth) | ongoing | commitment (unenforceable) | License verified as MIT on 2026-10-16 only; future relicensing is not excluded by any binding instrument we have seen |

A stated intention does not schedule a delivery, and none of these statements is independent evidence about the future.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 hypotheses)

These are **analyst hypotheses, not Vercel strategy and not forecasts.**

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Framework vendors will ship agent-facing upgrade and documentation channels (version-matched `AGENTS.md`, `upgrade --agent`), and these will reduce the maintenance cost of agent-assisted dependency upgrades | 016, 026; skills.sh scale (025) | Gains may come from model improvement rather than from docs channels; vendors may push upgrades to sell hosting | Independent paired tasks show no higher accepted-upgrade rate or no fewer reviewer minutes with version-matched docs; or the feature is deprecated | Low. No independent task data |
| H2: Short-lived, scoped, OIDC-derived credentials will become the default for agents that call third-party APIs, replacing stored tokens | 003 (incident through stored, decryptable variables), 009/020, 013, 014 | GitHub/cloud OIDC and workload identity already provide this without a vendor broker; the broker itself becomes a new trust concentration | Incident reports keep naming long-lived secrets on these platforms; Connect adoption stalls; provider revocation stays inconsistent | Medium for the direction, low for vendor-specific uptake |
| H3: Agent extension packaging (skills/plugins) will consolidate on a multi-vendor manifest, but reuse will be extremely concentrated and weakly vetted | 018 (TSC from AWS/Cursor/Microsoft/OpenAI/Vercel), 025 (0.04% of skills account for 62% of installs; about half installed once) | Install counters may be inflated by automation; clients may fork the spec | Major clients drop the spec; a signing/provenance layer arrives and changes the reuse distribution | Medium/low |
| H4: The attack surface of the frameworks and the agent toolchain will keep growing faster than vendor hardening programs | 005, 015, 022, 023 (more than 30 Next.js advisories in six months, several critical RCEs); 004/019/024 | More advisories may reflect better disclosure (paid bounties, AI-assisted research) rather than worse code | Advisory counts fall while independent fuzzing and audit finds fewer issues | Low. Counts are not normalized for code size or scrutiny |

## 7. Implications for the GitHub 1000 study (M1–M7)

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Vendor claims that agents produce 30% of apps (001) and 58.9% of gateway tokens are tool-call traffic (006) | Use only opt-in task logs; never infer agent authorship from vendor share figures | Platform-specific self-selection | Vendor aggregates are E1 and are not repository-level data |
| **M2** accepted task quality | Agent-generated apps deployed through the v0 API (017), plus Vercel Agent fixes (014) | Hidden, independently authored acceptance tests on frozen tasks; count every attempt | Sandbox "verification" ≠ user acceptance | No vendor accuracy denominators |
| **M3** discoverability | skills.sh / Agent Plugins as a new discovery channel (018, 025) | Compare the discovery path (registry versus GitHub search) for the same component | Install counters are not human discovery | Registry data is vendor-hosted |
| **M4** independently verified useful reuse | Better Auth stewardship (013); Apache-2.0 SDKs (002, 010, 011, 021) | Trace a consented downstream integration to an accepted task; use license and commit pins | npm downloads and contributor counts are not reuse | No downstream verification performed here |
| **M5** reuse-first / package rights and security | More than 30 framework advisories; the libheif transitive chain (022/023); third-party AI tool compromise (003) | Dependency-pin audit plus advisory-to-patch latency in sample repositories | Advisory volume can reflect disclosure effort | Repository metadata was read; code was not audited |
| **M6** lifecycle human and energy cost | Major-version migrations (AI SDK 7, Next.js 17 default change), secret rotation after 003 | Measure upgrade and rotation minutes on real tasks; meter energy only where it is instrumented | Vendor memory and build claims (016, 026) are not measured here | **No token-to-CO2e conversion; no carbon figures** |
| **M7** actionable interventions | Agent-readable version-matched docs; short-lived credentials | The experiment in section 8 | It may show no improvement | Single maintainer; small N |

Stars, funding, revenue, npm downloads, registry installs and customer stories are **not** verified adoption or task outcomes.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) (Python, `unittest`, offline fixtures). No Vercel product is required: the treatment reuses a **pattern** (version-matched agent guidance, from 016/026), not a vendor service. The live Trending `capture` stays **disabled** under the source-access decision. Nothing here changes that.

**Candidate practice (not yet validated):** add a short, version-pinned "upgrade guidance" block to the repository's agent instructions. The block names the exact supported Python versions, the pinned dependencies, the commands that run the gates, and the location of the changelog for each pinned dependency. A coding agent reads it before attempting a dependency or security-upgrade task.

**Treatment/control and frozen comparable task:**

- **Control A:** the current `AGENTS.md`, unchanged.
- **Treatment B:** `AGENTS.md` plus the version-pinned upgrade block.
- **Frozen inputs:** the same agent, model version, effort setting and token/time budget in both arms. Before any run, freeze 10 synthetic upgrade or maintenance tasks, created on throwaway branches. Each task is one functional unit, for example "bump dependency X to version Y and keep all gates green", or "replace a deprecated stdlib call flagged by Python 3.14".
- **Assignment:** tasks are assigned to A/B in a randomized, counterbalanced order. Hidden acceptance checks are written by a person other than the agent and are not shown to it.

**Functional unit and primary endpoint:** independently accepted upgrade PRs divided by **all** assigned tasks. Refused, abandoned and timed-out attempts stay in the denominator.

**Guardrails (any breach fails the task):**

- the full `python -m unittest discover -s tests -v` passes on Python 3.10 and 3.12;
- `scripts/check_research_artifacts.py` and `trending_study.data_integrity` pass;
- no new unreviewed dependency;
- no secrets or credentials in the diff;
- no edits to write-once evidence files;
- no AI-attribution trailers.

**Measured human work:** reviewer minutes per task, measured with a stopwatch log; the number of review/rework rounds; and the minutes needed to write and maintain the guidance block itself, which is charged to B. Energy is **not** estimated, because there is no metering.

**Stop/reversal rule:** stop after 10 paired tasks, or earlier on any guardrail breach. **Reject B** unless it (a) raises the accepted-task proportion by at least 2 of 10 **and** (b) does not raise median reviewer minutes. Report a null or negative result as is. With N=10 this is a feasibility pilot, not a causal estimate. **No trial has been executed and no effects are estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (vendor-dated, with readable artifacts):**
  - releases: Next.js 16.3 and 16.4;
  - Apache-2.0 repositories: eve, deepsec, Run SDK, Workflow SDK and AI SDK;
  - Better Auth remains MIT;
  - Agent Plugins spec licensing: CC-BY-4.0 for text, Apache-2.0 for code;
  - Next.js security advisories, with dates from the GitHub API;
  - the upstream libheif fix.
- **Claims/announcements only:**
  - GA, beta and preview labels and pricing for Workflows, Connect, v0 API, Services, Passport and Vercel Agent;
  - all usage, revenue, customer and performance figures;
  - all roadmap statements in section 5.
- **Conjectures and unknowns:**
  - H1–H4;
  - affected-customer count of the April incident;
  - deal terms;
  - actual IPO status;
  - whether the agent-facing features improve task outcomes.
- **Important contradictory or null evidence:**
  - April incident: Vercel's own platform was breached through a third-party AI tool (003), which is a counterweight to its agent-security positioning.
  - Services availability: post (public beta) and recap ("available July 1") disagree.
  - Connect pricing: the June and August pages disagree.
  - Next.js 16.4 date: the blog (Oct 6) and the GitHub release (Oct 7 UTC) disagree.
  - Sandbox challenge: the Oct 14 results post (out of window) reports a kernel zero-day and cross-tenant flaws found **in** Vercel Sandbox, and its valid-report counts do not reconcile.
  - Netlify reported that its platform was unaffected by the August RCEs, which shows that exposure depends on the deployment.
- **Candidate #56 news items (not minted):** 001 (TechCrunch), 003 with CyberInsider as the independent report of one incident, and 013 Better Auth (Dealroom). A human must read each one and verify it before minting an ID. Syndicated copies are **one** event.
- **Doubts about specific sources:**
  - The Vercel blog index renders many model and product names that cannot be checked here. Only items whose pages were fetched are ledgered.
  - The New Stack Better Auth page returned no readable body or date. It is listed in the log but not used.
  - The Dealroom page was seen only as a search result and was not fetched.
  - The Context.ai attribution comes from Vercel's bulletin as read on 2026-10-16. The page carries an update log, but no immutable snapshot was kept.
  - Several pages (Connect, Ship recap) have been edited since publication.
- **Reviewer links and audit date:** AI-assisted first pass, 2026-10-16. **Human factual/link spot check, source-access/rights review and methods review are pending.** Do not close #94 on the basis of this file.
