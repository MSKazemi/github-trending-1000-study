# Railway — provisional six-month technology intelligence screen (032)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16) — not reviewed by a qualified human.** This report, its [event ledger](032-railway.events.csv) and [search log](032-railway.search-log.md) were drafted by an AI coding assistant from public web pages and the public GitHub API. Factual/link review, source-access/rights review and scientific methods review are all **pending**. Nothing here is independently verified product behaviour, adoption, task outcome or environmental effect. Issue [#99](https://github.com/MSKazemi/github-trending-1000-study/issues/99) was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates above remain open.

- **Company watchlist ID:** 032 (Railway; sector: AI app builders, deployment and frontend).
- **Research issue:** [#99](https://github.com/MSKazemi/github-trending-1000-study/issues/99); evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see section 2; legal entity name from first-party terms, no filing-level ownership check.
- **Product URL and company newsroom:** [railway.com](https://railway.com/), [changelog](https://railway.com/changelog), [blog](https://blog.railway.com/), [Compute Week 2026](https://railway.com/compute-week), [railwayapp GitHub org](https://github.com/railwayapp).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Screened:** 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted draft / **pending** / **pending**.
- **Status:** screened (provisional documentary source leads; **32 ledger rows covering all seven calendar segments**). Not independently checked, not exhaustive, not published as a finding.
- **Method:** [company-intelligence protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [report template](../../../templates/company_six_month_intelligence.md), [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). Claim grades are company-watch E0–E4 working tiers, not the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

Exact queries, opened pages, exclusions and inaccessible sources are in the [search log](032-railway.search-log.md). Summary:

| Search run (date only) | Site/engine | Scope | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | railway.com/changelog (direct read) | weekly changelog index, Apr 17–Oct 9 entries | 26 in-window entries listed | 18 entries opened | 20 rows (from 17 entries; Aug 7 and Aug 21 entries split into separate rows) | 8 unopened entries (titles only) and the opened Jul 3 entry not ledgered | index titles only for unopened weeks |
| 2026-10-16 | blog.railway.com (direct read) + [Compute Week page](https://railway.com/compute-week) | blog index (10 posts dated in-window on the index; others undated there) | 10 index-dated + Compute Week/roadmap/incident posts dated on their own pages | 10 opened | 10 rows | marketing/comparison posts not used | many "Best X in 2026" posts are undated on the index; not screened |
| 2026-10-16 | GitHub REST API (`gh api`) | `railwayapp/cli` releases, repo licenses | 207 CLI releases in window | 3 release records read | 1 row | per-release notes not reviewed | API counts at query time only |
| 2026-10-16 | public web search | funding, outage, security, independent press | unknown | ~25 result titles | 1 independent press row | rail-transport homonyms, SEO aggregators, pre-window funding | search tool result totals unavailable |

Search result totals and run timestamps are unavailable, **not zero**. No paywall, login, private status data or personal data was accessed.

## 2. Verified company/product identity and baseline

- **Entity:** Railway's [Terms of Service](https://railway.com/legal/terms) (displayed effective date **2026-04-20**, i.e. updated inside the window; content diff versus the prior version **not** compared) name **Railway Corporation**, San Francisco DMCA address, Delaware governing law; page footer reads "Railway Corp." No parent company, acquisition or rename of the company was found in the window. The only rename found is the **iOS app listing** name (Oct 9, pending App Store approval; row 032). Filing-level ownership was **not** checked.
- **Offering:** a usage-billed developer cloud/PaaS (services, managed Postgres/MySQL/Redis/MongoDB, buckets, networking, templates marketplace) running on its own "Metal" datacenter hardware plus cloud burst capacity, with a growing agent layer (Railway Agent, MCP server, sandboxes, Cloud Agents, dev.new app builder).
- **Open-source surface (checked via GitHub API on 2026-10-16):** [railwayapp/cli](https://github.com/railwayapp/cli) — MIT; [railwayapp/railway-skills](https://github.com/railwayapp/railway-skills) — MIT (created 2026-01-04); [railwayapp/railway-ts-sdk](https://github.com/railwayapp/railway-ts-sdk) — MIT (created 2026-05-22). The hosted platform, control plane, Railway Agent and hosted MCP server are **proprietary services**; the MIT client tooling does not grant rights to the service.
- **Pre-window baseline (context only, not counted):** $100M Series B announced 2026-01-22 led by TQ Ventures ([SiliconANGLE](https://siliconangle.com/2026/01/22/intelligent-cloud-infrastructure-startup-railway-gets-100m-simplify-application-deployment/), [Axios Pro](https://www.axios.com/pro/enterprise-software-deals/2026/01/22/software-deployment-railway-100-million)); company-stated user and Fortune-500 figures in that coverage are **not adoption evidence**. Pre-window incident reports (Feb 11, Feb 18–21, Mar 30) are listed on the blog index and excluded.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger rows) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Remote MCP server, `railway agent` CLI, skills installer (001); Railway Agent live for every workspace, outbound IPv6 (002) | [Apr 17](https://railway.com/changelog/2026-04-17-remote-mcp), [Apr 24](https://railway.com/changelog/2026-04-24-railway-agent) | none found | ToS effective date Apr 20 noted in section 2, not ledgered |
| 2026-05 | one-shot agent setup and template search (003); **GCP account suspension outage** (004, 005); agent sandbox early access, GitHub-org deploy guardrail (006); Summer 2026 roadmap (007) | [May 8](https://railway.com/changelog/2026-05-08-easy-agent-setup), [May 20 postmortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage), [May 22](https://railway.com/changelog/2026-05-22-chat-agent-sandbox), [May 27 roadmap](https://blog.railway.com/p/railway-summer-update-2026) | [The Register, May 20](https://www.theregister.com/off-prem/2026/05/20/google-cloud-suspended-major-customer-railwaycom-without-cause-causing-outage/5243111) (relays Railway's account; Google did not comment at publication) | DCD article returned HTTP 403 (not read) |
| 2026-06 | Compute Week: Metal Gen 2 (008), Railway for Agents direction (009), CLI v5.0.0 (010), Sandboxes + experimental TypeScript IaC (011); Railway over SSH and six coding agents preinstalled in sandboxes (012) | [Jun 2](https://blog.railway.com/p/railway-metal-gen-2), [Jun 3](https://blog.railway.com/p/railway-for-agents), [v5.0.0](https://github.com/railwayapp/cli/releases/tag/v5.0.0), [Jun 5](https://railway.com/changelog/2026-06-05-sandboxes), [Jun 26](https://railway.com/changelog/2026-06-26-railway-over-ssh) | none found | CDN post title differs between blog index ("30M RPS") and Compute Week page ("100M RPS"); metric not used |
| 2026-07 | **US East outage** postmortem (013); feature flags, Slack/Discord agent beta, CLI spend caps (014); ChatGPT plugin, dev.new preview, private-by-default DB templates (015) | [Jul 3 postmortem](https://blog.railway.com/p/incident-report-july-2-2026-us-east-services-outage), [Jul 10](https://railway.com/changelog/2026-07-10-feature-flags), [Jul 31](https://railway.com/changelog/2026-07-31-railway-plugin-for-chatgpt) | none found | Grok plugin (Jul 16), DNS logs (Jul 24) and Gilfoyle ad campaign (Jul 3) seen in index only, not ledgered |
| 2026-08 | Cloud Agents beta (016); default Postgres CVE patching (017); ~10 h invalid-certificate defect fixed (018); dev.new blog (019); Access Groups, staged template changes, Agent Connectors (020); anonymous no-account deploys (021); Edge Rules, Redis HA (022); **Config-as-Code deprecation** (023) | [Aug 7](https://railway.com/changelog/agents-android-autopatch), [Aug 13](https://blog.railway.com/p/dev-new), [Aug 14](https://railway.com/changelog/2026-08-14-access-groups), [Aug 17](https://blog.railway.com/p/deploy-without-account), [Aug 21](https://railway.com/changelog/2026-08-20-railway-anon) | none found | Aug 28 (Grok Bot plugin, MySQL HA) index-only |
| 2026-09 | CLI MCP proxy + Postgres ops (024); one-click Postgres major upgrades (025); **Sandboxes GA** (026); free anonymous VMs, tracing preview (027); **Sep 30 routing outage** postmortem (028) | [Sep 4](https://railway.com/changelog/2026-09-04-postgres-in-the-railway-cli), [Sep 11](https://railway.com/changelog/2026-09-11-one-click-postgres-major-version-upgrades), [Sep 17](https://railway.com/changelog/2026-09-18-railway-sandboxes), [Sep 25](https://railway.com/changelog/2026-09-25-free-vms-without-an-account), [Sep 30](https://blog.railway.com/p/incident-report-sept-30-2026-routing-disruption) | none found (only third-party status aggregators) | secondary morphllm.com page dates Sandboxes GA to Jun 26 — contradicted by primary Sep 17 entry |
| 2026-10-01..12 | MongoDB HA early access, MySQL PITR GA (029); Slack/Discord agent GA (030); Railway Authentication identity-aware proxy, enterprise only (031); OpenRouter BYO-key beta (032) | [Oct 1](https://railway.com/changelog/2026-10-02-mongodb-high-availability), [Oct 5](https://blog.railway.com/p/railway-agent-slack-discord), [Oct 8](https://blog.railway.com/p/railway-authentication-identity-aware-proxy), [Oct 9](https://railway.com/changelog/railway-ios-auth-openrouter) | none found | — |

**No month lacked findings.** Independent reporting was found only for the May 19–20 GCP suspension outage.

**Date caveats:** several changelog URL slugs differ by one day from the displayed index date (Jul 16/17, Aug 20/21, Sep 17/18, Oct 1/2). `published_utc` uses the displayed changelog date; the discrepancy is recorded in the row limitation. Displayed dates are not archived byte-level timestamps.

## 4. Dated event evidence and capabilities

All 32 rows are in the [CSV](032-railway.events.csv). Grouped by capability cluster (row numbers = `CI2026-032-NNN`):

| Cluster (rows) | What the cited documents support | Availability and limitations | Working grade |
|---|---|---|---|
| **Agent interface to the platform** (001, 002, 003, 009, 014, 024, 030, 032) | Hosted OAuth-scoped MCP server; in-product Railway Agent (dashboard/CLI/Slack/Discord) acting with the user's own permissions; per-workspace Agent spend hard limits; skills installer for Claude Code/Cursor/Codex/OpenCode; `railway mcp` later defaults to a local proxy of the hosted MCP; BYO OpenRouter key | Mix of live, beta and GA labels; diagnosis/PR quality and permission enforcement not independently tested | E2 (documentary) |
| **Sandboxes and Cloud Agents** (006, 010, 011, 012, 016, 026, 027) | Per-conversation agent sandbox → flag-gated Sandboxes (Jun 5) → six third-party coding agents preinstalled (Jun 26) → **GA on every plan (Sep 17)**; Cloud Agents beta (Aug 7) with VM promotion to production; free anonymous 2 vCPU/2 GB VMs (Sep 25) | Isolation never independently audited; VM-to-production promotion bypasses git/CI by design | E2 |
| **App builder / onboarding** (015, 019, 021, 027) | dev.new prompt-to-deployed-app preview; code lives on a persistent volume in a normal Railway project; deploy without an account (60 min build, 24 h claim, $3 LLM cap) | Preview only; source export to GitHub **not described**; abuse and conversion data absent | E2 |
| **Data services and maintenance** (017, 022, 025, 029) | Default Postgres CVE patching; Redis/MySQL/MongoDB HA; one-click Postgres major upgrades; MySQL PITR GA | CVEs and patch latency unspecified; HA conversions drop connections; rollback window unstated | E2 |
| **Governance and security** (006, 017, 020, 022, 031) | GitHub-org deploy allowlist; Access Groups; staged reviewable template change sets; Edge Rules; identity-aware proxy (enterprise, $5,000/mo commitment) | Many controls plan-gated to committed spend; no independent security review | E2 |
| **Reliability incidents** (004, 005, 013, 018, 028) | Three vendor postmortems: GCP account suspension (~8 h, platform-wide), US East carrier/routing (~4 h of degraded cross-US connectivity 07:44–12:01 UTC, incl. ~2 h disk/private-network degradation and ~20 min without a default route in one zone), routing deploy-ordering bug (~5 min global 404s); ~10 h invalid certificates for some US users | Vendor-authored except The Register, which relays Railway's account; remediation completion unverified | E2 (vendor) / E1 (press) |
| **Infrastructure** (008) | Metal Gen 2 live in 3 of 4 regions, ~13% of containers on Gen 2 at Jun 1, ~40% workloads on cloud burst | Throughput/capacity multipliers vendor-stated; no energy data | E2 |
| **Deprecation** (023) | Config as Code (railway.json/railway.toml) stops for new services Aug 28 and ends Dec 1, replaced by TypeScript IaC SDK (experimental since Jun 5) | Real migration burden for existing repos; end date outside window | E2 |

**CLI release cadence (GitHub API, queried 2026-10-16):** 207 non-prerelease `railwayapp/cli` releases published in the window, from v4.37.3 (2026-04-15) to v5.66.0 (2026-10-12), with v5.0.0 on 2026-06-04. A release count is a maintenance-activity signal, **not** a quality or adoption measure.

## 5. What the company says it intends to do

| Close paraphrase / short quote | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Reliability problems "cost us customer trust"; Q2 reliability foundation (Metal Gen 2, four new datacenter sites, exploring ISO 27001) | [Summer 2026 update](https://blog.railway.com/p/railway-summer-update-2026), 2026-05-27 | Q2 2026 | planned (partly delivered: Metal Gen 2 3/4 regions, row 008) | ISO 27001 only "exploring"; four new sites not verified |
| Q3: sandbox primitive, SDK, better IaC, feature flags, mobile GA, templates "renaissance"; "the production agent-native cloud becomes the default" in Q4 2026 into 2027 | same | Q3 2026; Q4 2026–2027 | planned; several Q3 items later shipped (rows 011, 014, 026) | "default" is a positioning goal, not a measurable commitment |
| CLI being reworked for agents; NPM-hosted MCP being deprecated; CLI sign-up "Soon" | [Railway for Agents](https://blog.railway.com/p/railway-for-agents), 2026-06-03 | unspecified | tentative | partially realised by Sep 4 MCP proxy change (row 024) |
| Config as Code ends Dec 1; move to IaC SDK | [Aug 21 changelog](https://railway.com/changelog/2026-08-20-railway-anon) | 2026-12-01 | announced deprecation | IaC labelled experimental on Jun 5 |
| "This is just the start for us trying to make Railway as free as possible" | [Deploy without account](https://blog.railway.com/p/deploy-without-account), 2026-08-17 | unspecified | uncommitted | free trial was earlier removed over abuse (vendor statement) |
| dev.new workflow to move "inside the Railway dashboard itself" | [dev.new post](https://blog.railway.com/p/dev-new), 2026-08-13 | "over time" | uncommitted | — |
| GCP to leave the data-plane hot path; HA DB shards across AWS and Metal | [May 19 postmortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage), 2026-05-20 | unspecified | stated remediation | completion not verified in window |
| Multiple SAML providers "coming soon"; "big stuff coming this quarter" | [Oct 9 changelog](https://railway.com/changelog/railway-ios-auth-openrouter) | Q4 2026 | uncommitted | content unspecified |

These are company statements, not forecasts or verified delivery.

## 6. Independent interpretation: conditional 2027–2031 scenarios

| Hypothesis (researcher's, conditional) | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Deployment platforms become agent-operated: the MCP/CLI/agent surface, not the dashboard, becomes the primary way small teams deploy | Rows 001–003, 009, 024, 030; vendor says querying tools dominate agent CLI/MCP use | Agent features are marketing-led; humans still drive most deploys; equivalent tooling exists from rivals | Opt-in usage records show agent-initiated deploys remain a small share; agent-made changes show higher rollback/incident rates than human-made ones | low; no usage denominator available |
| H2. "Cloud = sandbox + production in one network" shortens prototype-to-production but weakens review/provenance | Rows 012, 016, 026 (VM promotion bypasses git/CI; sandboxes on private network) | Teams keep git/CI gates regardless; promotion is optional | Controlled tasks show equal review coverage and no extra defects with VM promotion vs git+CI | low; no independent test exists |
| H3. Concentrated platform dependencies remain the main reliability risk even with owned hardware | Rows 004, 013, 028; 40% workloads on cloud burst (row 008) | Incident rate is typical for PaaS of this scale; remediations may work | Post-remediation 2027 incident history shows no multi-region control-plane outage | medium for 2026 evidence, unknown going forward |
| H4. Free/anonymous agent onboarding increases discoverability but not durable reuse | Rows 021, 027 | Conversion may be high; abuse may force rollback (as with the earlier free trial) | Free anonymous access withdrawn, or independent data show retained, working downstream deployments | low |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** workflow change | Repos add `railway.ts`, agent skills or MCP config files after Apr 2026 | Dated, audited repo-month markers for Railway agent artefacts in an opt-in cohort | Files present ≠ agent actually used | availability ≠ adoption |
| **M2** accepted quality / review / maintenance | Config-as-Code → IaC migration creates maintenance churn; staged template diffs may help review | Count migration PRs and review minutes in consented repos; compare template edits with/without staged diffs | Migration may be trivial or automated | only consented repos |
| **M3** discovery | No-account deploys and unified template search may raise template visibility | Prospective template-page observation; no star/traffic inference | Exposure without use | no third-party traffic data |
| **M4** first-use success / verified reuse | One-command templates and dev.new could raise first-deploy success | Independently graded first-deploy tasks on a template, all attempts counted | Platform-specific success does not transfer elsewhere | deploy success ≠ downstream reuse |
| **M5** reuse vs generate | dev.new generates whole apps instead of reusing templates/packages | Matched tasks: template reuse vs dev.new generation vs hand-written, hidden acceptance tests | Generation may win on small tasks | synthetic tasks only until authorised |
| **M6** lifecycle cost | Agent spend caps, sandbox minutes and per-token billing are measurable; three outages impose recovery time | Record metered spend, human minutes and incident downtime per accepted task | Outage cost depends on workload, not platform choice | **no token-to-kWh/CO2e conversion**; no energy data published by vendor |
| **M7** interventions | "Deploy on Railway" buttons or skill files as onboarding interventions | Staggered, registered README intervention with independent first-use tasks | Promotion confounding | no causal claim from this screen |

Company adoption claims (millions of users, 50M+ builds/month, 80M deployments/month) are **vendor-reported** and are not independently verified usage, task outcomes or reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline CLI (`python -m trending_study ...`) — specifically a **read-only demo of the synthetic validators** (e.g. `value_gate`, `reuse_gate`, `goldset` on the committed synthetic examples). Live Trending `capture` stays **disabled** under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md); no hosting platform changes that.

**Candidate practice (not validated):** a reproducible "first successful run" path for newcomers. **Treatment A:** a pinned container recipe deployed as a one-command template on a hosted PaaS (Railway template + Sandbox, pinned CLI version, no secrets, no network calls from the app). **Comparator B (reuse-first, default):** the existing repo with a pinned `devcontainer`/local `python -m unittest` path and README instructions only. **Comparator C (optional):** a generic container on any equivalent host, to separate "container" from "Railway".

**Accepted-task functional unit:** one newcomer task = "run the three synthetic CLI smoke commands and obtain the documented `not_ready`/expected outputs", graded by an **independently authored hidden checklist** frozen before the trial. Denominator = **all assigned attempts**, including abandoned, failed, timed-out and refused.

**Guardrails:** no credentials or personal data in the template; no live GitHub access; dependency versions and licenses pinned and reviewed (CLI and SDK are MIT, the hosted service is proprietary); zero tolerance for any secret in logs; Railway spend hard limit set before start; template must not rely on Config-as-Code (deprecated Dec 1) — use whatever is current at freeze time and record it.

**Measured human work:** newcomer minutes to first accepted run; maintainer minutes for setup, review and 30-day upkeep (template breakage, CLI/IaC changes); metered platform spend. Energy only if actually metered; **no modelled carbon numbers**.

**Stop/reversal rule:** stop and keep Comparator B if (a) A does not beat B on accepted-first-run rate by a preregistered margin with ≥ the preregistered number of participants, (b) any secret exposure or license/terms ambiguity appears, (c) 30-day maintainer upkeep for A exceeds B, or (d) a platform outage or deprecation forces unplanned rework during the trial. A null or negative result is a valid outcome and must be preserved. **No trial has been run; no effect is estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-stated):** agent tooling (remote MCP, Railway Agent, skills, Slack/Discord GA); Sandboxes GA (Sep 17); Metal Gen 2 partial rollout; data-service HA/PITR/upgrades; Edge Rules; identity-aware proxy (enterprise); anonymous deploys; 207 CLI releases.
- **Claims/announcements only:** roadmap quarters (row 007), CLI agent rework and sign-up (009), Config-as-Code end Dec 1 (023), GCP hot-path removal (004), SAML providers, "big stuff this quarter" (032).
- **Conjectures and unknowns:** all section 6 hypotheses; isolation/security of sandboxes and Cloud Agents; dev.new code portability; real adoption, task quality and lifecycle cost; filing-level ownership.
- **Important contradictory or null evidence:** three vendor-documented outages plus a ~10 h certificate defect in the window; vendor's own admission that reliability "cost us customer trust"; The Register could not obtain Google's account of the suspension; secondary source misdates Sandboxes GA; changelog slug/display date mismatches; CDN headline metric inconsistent across two first-party pages.
- **Reviewer links and audit date:** none yet. Pending: human factual/link spot-check of sampled rows, rights/source-access review, methods review, PR review linked to [#99](https://github.com/MSKazemi/github-trending-1000-study/issues/99). No `NEWS-YYYY-NNNN` corpus items were created for [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56); The Register article (row 005) is the one independent candidate, subject to human verification.

## Independent source spot-check (2026-10-16)

An independent reviewer agent (not the author of this screen) re-fetched every cited URL on 2026-10-16 (all returned HTTP 200) and compared dates and specific figures against raw page text (`curl` + grep) or the GitHub REST API (`gh api`). Classification: confirmed / corrected / unverifiable / wrong.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (§2) | confirmed | ToS: "Effective date: 2026-04-20", "Railway Corporation", 548 Market St … San Francisco address, Delaware law; "Railway Corp." in page footers. No filing-level check. |
| Pre-window Series B (§2) | confirmed | SiliconANGLE: $100 million Series B led by TQ Ventures (Jan 22, 2026). Axios not re-read. |
| 032-001 | confirmed | Page 2026-04-17; OAuth workspace/project scoping, "7 tools today", destructive tool prompt, llms.txt. |
| 032-002 | confirmed | Page 2026-04-24; "live for every workspace", per-token rates, mix of Anthropic models, default Agent hard limit "$5 on Hobby, $20 on Pro", outbound IPv6. |
| 032-004 | confirmed | Postmortem dated May 20, 2026; "between 22:20 UTC and approximately 06:14 UTC on May 20 (~8 hours)", Google Cloud suspended the production account. |
| 032-005 | confirmed | The Register, "wed 20 May 2026 // 05:37 UTC"; relays Railway (Angelo Saraceno); "has contacted Google"; no Google response at writing. Article was written mid-incident. |
| 032-008 | confirmed | Jun 2, 2026; "live in three of four regions today: US West, US East, and Amsterdam", "40 percent of our workloads are on cloud burst", "About 13% of the containers … as of June 1". |
| 032-009 | confirmed | Jun 3, 2026; NPM-hosted MCP deprecation, sign-up "Soon", 48-hour soft delete, destructiveHint; "exceeded 80 million deployments" last month. |
| 032-010 / CLI count (§4, §9) | confirmed | `gh api`: v5.0.0 published 2026-06-04T15:57:44Z (PR #933); **207** releases (all non-prerelease) published 2026-04-12..10-12, first v4.37.3 (2026-04-15), last v5.66.0 (2026-10-12). cli/railway-skills/railway-ts-sdk all MIT; created dates match. |
| 032-013 | **corrected** | Postmortem (Jul 3, 2026) says increased latency/intermittent cross-US connectivity **07:44–12:01 UTC** (~4 h 17 min); disk and private-network degradation in one US East zone lasted **roughly two hours**; ~20 min without default route; ~20,000 links blackholed. The row had attached the 07:44–12:01 window to the "~2 h" figure; CSV row and §4 text fixed. |
| 032-012 / 016 | confirmed | Jun 26 entry: six coding agents preinstalled incl. Claude Code, Droid, Pi; Aug 7 entry: "Cloud Agents Beta", "we promote the VM to prod", Android app. |
| 032-014 / 030 | confirmed | Jul 10 entry: Slack/Discord agent "in beta", percentage rollout; Oct 5 blog: shipped to Priority Boarding in July, now GA. |
| 032-017 / 018 | confirmed | Aug 7 entry: CVE patching on notification + known mitigation, no public internet provisioning, not yet "fully managed"; fixes list "invalid cert for 10 hours". |
| 032-021 / 023 | confirmed | Aug 17 blog: 60 minutes build, 24 hours to claim, "Max of $3 of LLM credit", free trial rolled back over fraud/abuse. Aug 21 entry (slug 2026-08-20): Config as Code stops for new projects Aug 28, ends December 1. |
| 032-026 / 027 / 029 | confirmed | Sep 17 (slug 09-18) Sandboxes GA "on every plan", MySQL PITR 7 days in Priority Boarding; Sep 25: 2 vCPU / 2 GB, 60 min + 24 h; Oct 1 (slug 10-02) MongoDB 7/8 HA, MySQL PITR GA; CLI v5.63.1 (2026-09-28) PITR/Patroni fix. |
| 032-028 | confirmed | Sep 30, 2026; "between roughly 07:35 and 07:40 UTC … HTTP 404 in all regions"; serial migration ordering, schema-gated rollout, shard-based regional rollouts. |
| 032-031 / 032 | confirmed | Oct 8 blog: enterprise, admin-only, "$5,000/mo"; Oct 9 entry: OpenRouter beta, App Store rename pending, SAML "coming soon", "big stuff coming this quarter". |
| 032-007 | confirmed (paraphrase note) | May 27, 2026; "cost us customer trust", Q2/Q3/Q4 framing, "50M+ builds a month". ISO wording on the page is "angling to work on ISO27001" / "serious push toward ISO27001"; "exploring" is the screen's paraphrase. |
| CDN headline discrepancy (§3) | confirmed | Blog index "30M RPS" vs Compute Week page "100M RPS". |

Outcome: 23 of 32 ledger rows (001, 002, 004, 005, 007–010, 012–014, 016–018, 021, 023, 026–032) plus 4 report-level items (entity, Series B baseline, CLI count, CDN discrepancy) checked → 22 rows confirmed, 1 row corrected (013 duration), 4 report items confirmed; 0 unverifiable, 0 wrong. No fabricated URL, date or figure found; no cross-company contamination found. Not re-checked: rows 003, 006, 011, 015, 019, 020, 022, 024, 025 (URLs resolve, figures not compared), the Axios article and the unopened changelog weeks.

*This is an AI-assisted spot-check, not qualified human review; the human factual/link, rights and methods reviews remain pending.*
