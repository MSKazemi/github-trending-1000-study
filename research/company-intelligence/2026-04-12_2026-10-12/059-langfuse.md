# Langfuse: provisional six-month technology intelligence screen (059)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](059-langfuse.events.csv) and [search log](059-langfuse.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. It is not a verified chronology, a license determination, a product test or an empirical reuse result. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

- **Company watchlist ID:** 059 ([watchlist row](../../../docs/AI_SOFTWARE_COMPANIES_100_WATCHLIST_2026-10-12.md))
- **Research issue:** [#127](https://github.com/MSKazemi/github-trending-1000-study/issues/127). Linked corpus initiative: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` corpus IDs were minted here. Candidate nonduplicate items for #56 are listed in section 9.
- **Ownership and product boundaries (as of 2026-10-12):** Langfuse (product) is owned by **ClickHouse, Inc.** since January 2026. ClickHouse (#079) is a separate watchlist row with the **same parent**. Do not count the two as independent ownership groups. Details in section 2.
- **Product URL and newsroom:** [langfuse.com](https://langfuse.com/), [changelog](https://langfuse.com/changelog), [blog](https://langfuse.com/blog), [roadmap](https://langfuse.com/roadmap), [status](https://status.langfuse.com/), [langfuse/langfuse on GitHub](https://github.com/langfuse/langfuse), [repository security advisories](https://github.com/langfuse/langfuse/security/advisories).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / pending.
- **Status:** screened (provisional). It has not been independently checked.
- **Source coverage:** 33 ledger rows that cover all seven month segments: Apr 12–30: 4, May: 9, Jun: 3, Jul: 5, Aug: 7, Sep: 3, Oct 1–12: 2. The search covered the vendor sitemap, the changelog and blog, the GitHub REST API (releases, advisories, commits, licenses), NVD, the incident.io status page and web searches. One aggregator was inaccessible (isdown.app returned 403). Search-engine hit counts are **unknown, not zero**. See the [search log](059-langfuse.search-log.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 (time not logged) | langfuse.com sitemap + changelog index | `sitemap-0.xml` filtered to `/changelog/2026-04..10` and `/blog/2026-04..10`; changelog index; links harvested from monthly updates | 75 in-window changelog slugs + 16 blog posts | 70 pages fetched (4 linked slugs returned 404) | 27 | many minor UI changelog entries were deliberately not itemised | The sitemap is incomplete: some entries were found only through monthly-update links |
| 2026-10-16 | GitHub REST API (`gh api`) | releases, security-advisories and LICENSE commits for langfuse/langfuse; SDK and plugin repos | 161 server releases in window; 1 in-window advisory | all | 4 | Individual minor releases not itemised; SDK v5/v6 (Oct 14) are out of window | Git author dates are unauthenticated metadata |
| 2026-10-16 | NVD API | `cveId=CVE-2026-41487`; `keywordSearch=langfuse` for 2026-04-01..2026-07-30 and 2026-07-30..2026-10-13 | 1 | 1 | 1 | none | NVD caps the date range at 120 days, so the search was split |
| 2026-10-16 | status.langfuse.com (incident.io) | embedded incident list | 14 incidents (2026-08-03..09-30) | 2 detail pages | 2 | 12 summarised only | Shows only the history the page exposes; displayed times have no stated timezone |
| 2026-10-16 | Web search (WebSearch tool) | 11 queries (see log) | unknown | ~40 result titles | 2 independent (Thoughtworks, jacar.es) | vendor-SEO comparisons, aggregators, out-of-window acquisition coverage | No paywalled press; no exhaustive news sweep |

## 2. Verified company/product identity and baseline

- **Baseline (outside the window):** on 2026-01-16 ClickHouse announced that it was acquiring Langfuse GmbH, together with a $400M Series D ([SiliconANGLE, Jan 16 2026](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/); [Langfuse "joins ClickHouse" post](https://langfuse.com/blog/joining-clickhouse), front-matter date 2026/01/16). Langfuse said then that there were "no planned changes to licensing". This is **baseline context, not an in-window event**.
- **In-window evidence of the parent link:** "Sign in with ClickHouse Cloud" (CI2026-059-007). On 2026-08-18 the repository LICENSE copyright holder changed from "Langfuse GmbH" to "ClickHouse, Inc." (CI2026-059-024). The Japanese launch blog says ClickHouse acquired Langfuse in January.
- **Unresolved entity detail:** the website footer read on 2026-10-16 still says "© 2022–2026 Langfuse GmbH / Finto Technologies Inc.", while a sibling commit on 2026-08-18 ([5621699bd7](https://github.com/langfuse/langfuse/commit/5621699bd7)) changed the `ee/LICENSE` copyright to "ClickHouse, Inc" and now refers to an agreement "as agreed by you and Langfuse GmbH or ClickHouse, Inc." (corrected by the 2026-10-16 spot-check; the original screen said `ee/LICENSE` was untouched). The legal contracting entity for Cloud and Enterprise customers was **not verified**.
- **Offering (verified from vendor docs):** an open-source LLM/agent observability platform covering tracing, prompt management, evaluations (LLM-as-a-judge, code and decision-model evaluators), datasets/experiments, dashboards and monitors. It is offered as Langfuse Cloud (EU, US, HIPAA and, from Apr 27, JP regions) and as a self-hosted deployment.
- **License (repository read 2026-10-16):** MIT ("MIT Expat") for everything outside the `ee/`, `web/src/ee/` and `worker/src/ee/` directories. Those directories are under a commercial Enterprise license. GitHub reports `NOASSERTION` because the license is mixed. The current [license-key page](https://langfuse.com/self-hosting/license-key) (undated) lists the key-gated features: project-level RBAC roles, protected prompt labels, data retention, audit logs, server-side masking, UI customisation, organisation creators, the Org Management API with SCIM, and the Instance Management API. That list should be compared with the vendor's "all core features MIT" framing on [/open-source](https://langfuse.com/open-source). The difference is a matter of definition, not necessarily a contradiction. SDKs: langfuse-python is MIT. langfuse-js reports NOASSERTION; its license was **not read**.

## 3. Month-by-month discoveries

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Experiments become a first-class feature (Apr 13); CVE-2026-41487 advisory (Apr 17; patched Apr 9); Cloud Japan region (Apr 27) | [changelog Apr 13](https://langfuse.com/changelog/2026-04-13-experiments-rebuild), [GHSA-2524-j966-gfgh](https://github.com/langfuse/langfuse/security/advisories/GHSA-2524-j966-gfgh), [Japan](https://langfuse.com/changelog/2026-04-27-langfuse-cloud-japan) | [Thoughtworks Radar, Trial header but "remains in Assess" in text, Apr 15](https://www.thoughtworks.com/radar/platforms/langfuse) | The Apr 30 update already names the Experiments GitHub Action and the Academy (beta), before their changelog "launch" dates |
| 2026-05 | NVD rates the CVE MEDIUM (May 8); Academy (May 14); ClickHouse Cloud login (May 18); roadmap rewrite (May 18); Launch Week 5, May 25–29: CI action, agent skill, full-text search beta, code evaluators, MCP expansion | [May update](https://langfuse.com/blog/2026-05-31-langfuse-may-update), changelog entries in CSV | NVD record (government registry) | Launch Week was held at the ClickHouse OpenHouse event (vendor statement) |
| 2026-06 | Monitors and alerts (Jun 19); Assistant public beta (Jun 19); code-evaluator runtime post with a researcher credential-extraction episode (Jun 22) | [monitors](https://langfuse.com/changelog/2026-06-19-monitors), [Assistant](https://langfuse.com/changelog/2026-06-19-langfuse-assistant-public-beta), [runtime post](https://langfuse.com/blog/2026-06-22-code-evaluators-execution-model) | none found | Several smaller June entries were screened and not itemised (scores API v3, SDK export masking, browser scores, multi-modal datasets) |
| 2026-07 | Claude Code observability plugin v1.0.0 (Jul 3); finance deployment-gate case (Jul 15); "copy our eval setup" (Jul 22); signed remote experiment triggers (Jul 28); **v4.0.0 GitHub release (Jul 29)** | [plugin release](https://github.com/langfuse/claude-observability-plugin/releases/tag/v1.0.0), [v4.0.0](https://github.com/langfuse/langfuse/releases/tag/v4.0.0) | none found | Jul 31 update announces a Q3 roadmap Town Hall (Aug 12) |
| 2026-08 | Roadmap refresh: Gateway (Aug 4); **v4 GA announcement and Cloud v3 cutover date 2026-11-16 (Aug 17)**; LICENSE holder changed to ClickHouse, Inc. (Aug 18); OpenAI fast-mode cost tracking (Aug 18); status incident during the v3/v4 transition (Aug 19); CLI 1.0 (Aug 21); stable evaluator API (Aug 27) | [v4 changelog](https://langfuse.com/changelog/2026-08-17-langfuse-v4), [LICENSE commit](https://github.com/langfuse/langfuse/commit/907194fdfe), [status](https://status.langfuse.com/incidents/h3t8vhtd) | none found | The status page lists 8 resolved incidents published in August (6 in September) |
| 2026-09 | Old-SDK ingestion delayed about 3 h by the v4 batch migration (Sep 14); Jev decision-model judge (Sep 22) | [incident](https://status.langfuse.com/incidents/trdzkge0), [Jev](https://langfuse.com/changelog/2026-09-22-jev-as-a-judge) | [jacar.es hands-on v3 to v4 migration, Sep 25](https://jacar.es/?p=7395) | Sep 3 Assistant sandbox and Sep 7 evaluator backfills were screened and not itemised |
| 2026-10-01..12 | Organisation usage breakdown (Oct 6); API-key expiration (Oct 7) | [usage](https://langfuse.com/changelog/2026-10-06-organization-usage-breakdown), [API keys](https://langfuse.com/changelog/2026-10-07-api-key-expirations) | none found | Excluded as out of window: Oct 13 session view and decision models; Oct 14 Python SDK v5 / JS SDK v6 (GitHub releases 2026-10-14) and org-level LLM connections |

## 4. Dated event evidence and capabilities

Grades follow the company-watch E0–E4 scale. No row reaches E3. "E2" means a dated, reproducible documentary record. It does not mean that the functionality was tested.

| Event ID | Published / event date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| CI2026-059-001 | 2026-04-13 | Experiments become a top-level concept | shipped (vendor) | changelog | none | E2 |
| CI2026-059-002 | 2026-04-15 | Radar header "Trial" (blip text also says "remains in Assess"; source-internal conflict); v3 is more scalable but more complex to self-host | opinion, not a test | Thoughtworks Radar (independent) | n/a | E1 independent opinion |
| CI2026-059-003 | 2026-04-17 / 2026-04-09 | Member role could exfiltrate stored LLM provider keys through a redirected baseUrl test; fixed in v3.167.0 and on Cloud | corrected; advisory self-labelled "low" | GHSA | NVD API | E2 |
| CI2026-059-004 | 2026-04-27 | Tokyo Cloud region; vendor claims "well over a hundred customers in Japan" | shipped; customer count is a vendor claim | changelog + blog | none | E2 |
| CI2026-059-005 | 2026-05-08 | NVD: CVSS v4.0 5.3 (GitHub CNA) / v3.1 5.4 (NVD) MEDIUM | **conflicts with the GHSA "low" label** | NVD API | GHSA | E2 |
| CI2026-059-006 | 2026-05-14 | Langfuse Academy launch | **launch-date conflict** with the Apr 30 "beta is live" statement | changelog | Apr 30 update | E2 |
| CI2026-059-007 | 2026-05-18 | ClickHouse Cloud as login provider | shipped | changelog | none | E2 |
| CI2026-059-008 | 2026-05-18 | Roadmap and vision ("auto-optimizing agents", neutral execution layer) | announced only | docs-repo commit | none | E1 |
| CI2026-059-009 | 2026-05-25 | GitHub Action experiment gate that can block PRs | shipped; v1.0.0 was released 2026-05-05 | changelog | GitHub release | E2 |
| CI2026-059-010 | 2026-05-26 | Agent skill for coding agents | shipped; compatibility is a vendor claim | changelog | none | E2 |
| CI2026-059-011 | 2026-05-27 | ClickHouse full-text search; claimed 18 s / 494 GB down to <0.5 s / <1 GB | **beta rollout** on the Cloud v4 preview | changelog + May update | none | E1 |
| CI2026-059-012 | 2026-05-28 | Deterministic Python/TS code evaluators | shipped | changelog | none | E2 |
| CI2026-059-013 | 2026-05-29 | MCP server covers most project data | shipped; MCP OAuth is still on the roadmap | changelog | none | E2 |
| CI2026-059-014 | 2026-06-19 | Cost/quality/latency monitors → Slack/webhook/GitHub Actions | shipped | changelog | none | E2 |
| CI2026-059-015 | 2026-06-19 | In-product Assistant | **public beta** | changelog | v4.0.0 notes | E2 |
| CI2026-059-016 | 2026-06-22 | Lambda tenant-isolated evaluator runtime; researcher extracted Lambda role credentials; vendor says probing was fully denied | vendor self-report | engineering blog | none | E1 |
| CI2026-059-017 | 2026-07-03 | Claude Code session-telemetry plugin (prompts, tool calls, tokens, cost) | released, MIT | GitHub release | none | E2 |
| CI2026-059-018 | 2026-07-15 | 150-item FinanceBench run at 81.3% failed an 85% gate | vendor case study; unnamed bank | blog | none | E1 |
| CI2026-059-019 | 2026-07-22 | Public copyable eval setup + open-source chatbot | **slug date 07-16 differs from displayed 07-22** | blog | none | E1 |
| CI2026-059-020 | 2026-07-28 | HMAC-signed remote experiment triggers | shipped, opt-in | changelog | none | E2 |
| CI2026-059-021 | 2026-07-29 | v4.0.0 self-host release; in-app agent moved out of EE | released | GitHub release | v4 changelog | E2 |
| CI2026-059-022 | 2026-08-04 | Roadmap: Gateway, issue detection, trajectory evals | announced only, "directional" | docs-repo commit | none | E1 |
| CI2026-059-023 | 2026-08-17 | v4 GA; "at least 10x" dashboards; Cloud v3 removal 2026-11-16 | GA; speed is a vendor claim | changelog | jacar.es (did not measure speed) | E2 |
| CI2026-059-024 | 2026-08-18 | LICENSE holder → ClickHouse, Inc.; MIT terms unchanged | in repo | commit | current LICENSE | E2 |
| CI2026-059-025 | 2026-08-18 | OpenAI Fast/priority tier cost tracking | shipped | changelog | none | E2 |
| CI2026-059-026 | 2026-08-19 | EU v3→v4 propagation delay incident | resolved | status page | status index | E2 |
| CI2026-059-027 | 2026-08-21 | CLI 1.0; "10x+" faster start; agent-readable exit codes | shipped | changelog | none | E2 |
| CI2026-059-028 | 2026-08-27 | Stable evaluator API (evaluation-as-code) | shipped | changelog | none | E2 |
| CI2026-059-029 | 2026-09-14 / 2026-09-13 | Old-SDK ingestion delayed ~3 h by the v4 batch job | resolved | status page | none | E2 |
| CI2026-059-030 | 2026-09-22 | TypeSafe Jev judge; $0.042/M input tokens | shipped; third-party speed/cost claims | changelog | Sep 30 update | E2 |
| CI2026-059-031 | 2026-09-25 | Independent migration test reports upgrade pitfalls | one author, one environment | independent blog | upgrade guide | E2 independent single report |
| CI2026-059-032 | 2026-10-06 | Organisation usage breakdown with CSV export | shipped | changelog | none | E2 |
| CI2026-059-033 | 2026-10-07 | API-key expiration dates | shipped, optional | changelog | none | E2 |

### Feature inventory (vendor assertion vs observed)

| Area | What the dated sources support | What remains unverified |
|---|---|---|
| Agent-facing interfaces (M1) | MCP server expansion (May 29), agent skill (May 26), CLI 1.0 with exit codes for agents (Aug 21), coding-agent telemetry plugins (Claude Code v1.0.0 Jul 3; Codex and Cursor plugin repos created Jun 3 and Sep 14) | Whether agents complete accepted tasks better with these interfaces. No one has measured this |
| Evaluation / accepted-task gates (M2) | Code evaluators, CI experiment gate, stable evaluator API, decision-model judges, finance gate case | Gate validity, judge calibration and false-pass rates. The finance figures come from a single vendor-run case |
| Cost tracking (study angle, M6) | Fast/priority-tier OpenAI pricing (Aug 18), organisation usage breakdown (Oct 6), monitors on cost (Jun 19) | Whether reported costs reconcile with provider invoices. Usage "units" are billing units, not energy |
| Security | One in-window CVE (RBAC; credential exposure), API-key expiry, HMAC triggers, vendor-reported credential extraction from the evaluator runtime | No independent audit. The severity label conflicts with NVD. MCP OAuth and granular key scopes are still roadmap items |
| Licensing/rights (M5) | MIT core plus a commercial `ee/` tree; copyright holder changed to ClickHouse, Inc. (Aug 18); a v4.0.0 PR title says the in-app agent moved out of EE | Whether any EE boundary moved in the other direction (code moved into EE). The legal Cloud contracting entity |
| Reliability/maintenance (M6) | The v4 transition caused documented status incidents and a forced Cloud migration date. An independent migration test found procedural pitfalls | Overall uptime trend. The full cost of migration for users |

## 5. What the company says it intends to do

| Public direction (paraphrase; short quotes ≤25 words) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Langfuse should "own the improvement loop around agentic software" and stay neutral in the execution layer. Long-term "auto-optimizing agents", with humans kept for the highest-leverage judgments | [roadmap source, commit 456989f59a, 2026-05-18](https://raw.githubusercontent.com/langfuse/langfuse-docs/456989f59a/content/docs/roadmap.mdx) | none stated | tentative vision | The Aug 4 refresh (commit 3e3c531d82) no longer contains the vision or "auto-optimizing" text |
| Langfuse Gateway: bring-your-own-key gateway with virtual keys and cost tracking; proactive issue detection; trajectory evals; AI-generated code evaluators | [roadmap source, commit 3e3c531d82, 2026-08-04](https://raw.githubusercontent.com/langfuse/langfuse-docs/3e3c531d82/content/docs/roadmap.mdx) | none; "directional, not a commitment" | planned (uncommitted) | Oct 2–8 edits (outside the scope of the dated rows) add org-level API keys and usage controls |
| Langfuse Cloud becomes v4-only and removes legacy APIs on **2026-11-16** | [v4 changelog, 2026-08-17](https://langfuse.com/changelog/2026-08-17-langfuse-v4) | 2026-11-16 | committed date (future) | Not yet verified as executed |
| Self-hosted v3 receives security patches "until end of January 2027" | [upgrade guide](https://langfuse.com/self-hosting/upgrade/upgrade-guides/upgrade-v3-to-v4) (undated living page, read 2026-10-16) | 2027-01 | stated support window | The page is undated, so the date it was first stated is unknown |
| Post-acquisition: stays open source and self-hostable, "no planned changes to licensing" | [joining-clickhouse, 2026-01-16](https://langfuse.com/blog/joining-clickhouse) | none | **baseline (pre-window)** | In window: MIT terms are unchanged and the copyright holder changed (CI2026-059-024) |

## 6. Independent interpretation: direction and alternative scenarios (2027–2031, conditional)

These are researcher hypotheses. They are not company strategy and not forecasts.

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Observability platforms become the evaluation/acceptance layer for agent-written changes (CI gates, code evaluators, MCP access) | CI action, stable evaluator API, code evaluators, agent skill/plugins, roadmap "improvement loop" | Ordinary unit/integration tests plus CI already serve as the acceptance layer. LLM-eval gates may stay niche for LLM-app teams | Independent studies show no change in accepted-task rate or review minutes when the gates are added. Vendors pivot back to pure tracing | Low; no outcome data |
| H2: Parent-company consolidation will tie Langfuse more closely to ClickHouse infrastructure and identity | ClickHouse Cloud login, ClickHouse FTS, v4 requires ClickHouse ≥25.12, LICENSE holder change | ClickHouse was already Langfuse's datastore since v3. The integration may be purely technical | MIT terms are narrowed, features move into `ee/`, or self-hosting is deprioritised. Conversely, an independent ClickHouse-free backend appears | Medium for the technical coupling; unknown for licensing |
| H3: Cheap non-generative "decision models" will make full-population scoring of agent traces economical | Jev and decision-model evaluators; vendor price $0.042/M input tokens | Price and accuracy claims are unverified. LLM judges may keep getting cheaper | Calibration studies show poor agreement with human labels. Pricing rises | Low |
| H4: Frequent major data-model migrations impose real lifecycle cost on self-hosters | v4 cutover, status incidents, independent migration pitfalls, deprecated APIs returning 404 | A one-off re-architecture, not a recurring pattern | No further breaking major release by 2028. Migration tooling removes the manual steps | Medium for 2026; unknown beyond that |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 coding workflows | Coding-agent session telemetry (plugins, MCP, CLI exit codes) makes agent use observable in opt-in records | Opt-in, consented session traces compared against self-report diaries for the same tasks | Telemetry captures tool calls, not workflow intent. Availability is not adoption | Only consented local traces. No inference from stars or plugin installs |
| M2 accepted task quality | CI experiment gates may catch regressions before merge | Frozen tasks with hidden human-authored acceptance tests; count every attempt | Gates may only re-measure what unit tests already catch | The independent acceptance tests decide the outcome, not Langfuse scores |
| M3 discovery | Academy, region launch and Radar listing are discovery signals | Not testable from this screen | Discovery ≠ use | Do not use stars (35.9k displayed) as a measure of adoption |
| M4 verified reuse | "Copy our eval setup" and MIT plugins are reuse invitations | Trace one consented downstream adoption of a published evaluator | Copying is unobserved. Downloads are not distinct users | Requires an independent downstream audit |
| M5 reuse-first | Reusing an MIT observability stack vs building ad-hoc logging | Compare the existing repository ledger (`trending_study.task_costs`) against Langfuse capture on the same tasks (section 8) | Hidden costs: ClickHouse/Redis/S3 operations, EE gating, migrations | Pin the exact version and record the license for each component |
| M6 lifecycle cost | Cost/usage dashboards could improve token and cost accounting. Migrations add human hours | Measure setup, upgrade and incident minutes along with invoice reconciliation | Billing units are not energy. Tokens are not kWh | **No CO2e or energy claims**; measured minutes and invoice amounts only |
| M7 interventions | Credential hygiene (key expiry, least privilege) as a maintainer practice | Lab test of key expiry and rotation drills | The vendor CVE shows a configuration risk, not a prevalence | Use synthetic credentials only |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), specifically the offline task-cost ledger (`trending_study.task_costs`, see [task cost ledger contract](../../../docs/TASK_COST_LEDGER_2026-10-12.md)). No real provider or human traces may be collected without the maintainer's explicit consent and recorded scientific approval. The first run uses **synthetic** tasks only.

**Candidate practice (not yet validated):** reuse an existing MIT tracing stack (self-hosted Langfuse server pinned to one v4.x tag, Python SDK pinned, Claude Code observability plugin pinned) instead of hand-entered cost and time records. The goal is to capture token usage, cost and wall-clock time for agent-assisted maintenance tasks more completely and with less human effort.

**Treatment/control and frozen comparable task:**
- **Control A:** the current workflow. Hand-entered ledger rows per task (tokens from provider console export, wall-clock from shell timestamps, human minutes self-timed).
- **Treatment B:** the same workflow plus local self-hosted Langfuse capture, exported to the same ledger schema by a small script.
- **Functional unit:** one **independently accepted** maintenance task. Freeze 8 small synthetic tasks, for example "add a validator for field X with tests". Each task has hidden acceptance tests written by a human, not by the agent. Use a crossover design, so each task runs once per arm, with the order randomised and logged before the run. Abandoned, refused and failed tasks stay in the denominator.

**Primary endpoint:** the share of all 8 assigned tasks per arm whose ledger record is **complete** (tokens, provider cost, wall-clock, human minutes all present) and whose cost total matches the provider's own usage export within a tolerance fixed before the trial.

**Secondary endpoints:** human minutes spent recording each task; one-time setup and 30-day maintenance minutes for B (including upgrades, for example the 2026-11-16 Cloud cutover pattern, which is relevant only if Cloud is used); task acceptance rate, which must not differ, as a guardrail.

**Quality, security and rights guardrails:**
- Self-host on localhost only, so that no prompt content leaves the machine. Use synthetic repositories and synthetic credentials.
- Enable SDK masking and run a secret-scan over exported traces. Any secret or personal datum found in a trace means immediate stop.
- Record the license of every component: MIT core, no `ee/` features, no license key.
- Run the repository gates (`python -m unittest discover -s tests -v`) unchanged.
- Telemetry stays private research data and is not used in commits or PR text.

**Measured human work:** setup minutes, per-task recording minutes, review minutes, and upgrade/incident minutes over 30 days, each timed by the maintainer. **No energy or carbon figures** unless they are metered separately.

**Stop/reversal rule:** abandon B if any of the following occurs:
1. Its completeness rate does not exceed A's by a margin fixed before the trial.
2. Setup plus 30-day maintenance minutes exceed the recording minutes it saves.
3. Any secret or prompt content leaks outside the local host.
4. A license or EE boundary blocks a required function.

In those cases keep the simpler hand-entered ledger. **No trial has been executed and no effect has been estimated.** A null result is a valid outcome and must be preserved.

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary E2):**
  - v4 data model: released on GitHub Jul 29 and announced GA on Aug 17. **These are two dated sources for one major-version event, not two releases.**
  - Evaluation tooling: CI gate, code evaluators, stable evaluator API.
  - Agent interfaces: MCP, skill, CLI, coding-agent plugins.
  - Cost/usage features, the Japan region, API-key expiry.
  - The copyright-holder change to ClickHouse, Inc.
- **Claims/announcements only:**
  - Performance multiples ("at least 10x", "up to 165×", FTS 18 s → <0.5 s).
  - Customer counts in Japan.
  - Jev speed and cost multiples (TypeSafe claims relayed by Langfuse).
  - Roadmap items (Gateway, issue detection, trajectory evals, auto-optimizing agents).
  - The 2026-11-16 Cloud cutover, which is still a future date.
- **Conjectures and unknowns:**
  - Adoption.
  - Accuracy of the judges.
  - Whether `ee/` boundaries moved in both directions.
  - The legal Cloud contracting entity.
  - Full search-hit denominators.
  - Behaviour of pages that may have been edited after publication. No archived snapshots were taken.
- **Contradictory or null evidence (preserved):**
  - (a) GHSA severity "low" vs NVD MEDIUM 5.3/5.4. The advisory timeline also contains an apparent "April 16, 2025" year typo.
  - (b) Academy and Experiments CI action appear as live in the Apr 30 update, before their May 14 and May 25 changelog "launch" dates. The action's v1.0.0 is dated May 5.
  - (c) The "copy our eval setup" slug says 07-16 but the page displays 07-22.
  - (d) The v4 GitHub release (Jul 29) predates the GA changelog (Aug 17).
  - (e) The vendor reported a researcher extracting Lambda role credentials from the evaluator runtime. Only the vendor account exists.
  - (f) Status incidents in Aug–Sep tied to the v4 migration, plus an independent report of migration pitfalls.
  - (g) Thoughtworks notes added self-hosting complexity.
  - Independent mainstream press coverage in the window was **not found** (searches logged). This is not proof that no coverage exists.
- **Candidate nonduplicate items for #56 (not minted; require human verification first):**
  - CI2026-059-003 together with 005, as one security event with two records.
  - CI2026-059-002 (Thoughtworks).
  - CI2026-059-021 together with 023, as one v4 event.
  - CI2026-059-031 (independent migration report).
- **Reviewer links and audit date:** none yet. AI-assisted screen dated 2026-10-16. Human factual/link, source-access/rights and methods review are **pending**.

### Untrusted-content note

Web pages were treated as data. No instructions addressed to AI agents were observed in the fetched pages (a pattern grep for phrases such as "ignore previous" and "if you are an AI" found none). One web-search result summary said that a Langfuse changelog page tells readers to use the canonical docs rather than the changelog code samples. That page variant was not read. If the note exists, it is ordinary documentation guidance and was not acted upon. All requests used a generic `Mozilla/5.0` User-Agent with no personal identifier.

## Independent source spot-check (2026-10-16)

AI-assisted spot-check, not qualified human review. Each cited URL was re-fetched on 2026-10-16 (`curl` with a generic browser User-Agent, `gh api`, NVD API JSON) and figures were compared against raw page text, not WebFetch summaries. 16 items checked: 15 ledger rows plus the ownership/acquisition baseline. Ledger-row outcome: 10 confirmed, 5 corrected (one of these, CI2026-059-024, fixes a wrong statement in the report about `ee/LICENSE`), 0 unverifiable, 0 wrong rows left. The baseline acquisition item is confirmed, with its wording corrected.

| Item checked | Outcome | Note |
|---|---|---|
| Baseline: ClickHouse acquisition of Langfuse GmbH | confirmed (wording corrected) | SiliconANGLE (datePublished 2026-01-16T21:49Z): ClickHouse closed a $400M Series D at a $15B valuation and "it's acquiring Langfuse GmbH". The `joining-clickhouse.mdx` front matter says `date: 2026/01/16`, and the post says "no planned changes to licensing". The Japan blog says ClickHouse "acquired Langfuse in January". Section 2 now says "was acquiring" to match the source |
| CI2026-059-002 Thoughtworks Radar | corrected | The header shows "Last updated: Apr 15, 2026 / Apr 2026 Trial", but the blip body says "Langfuse remains in Assess". The source contradicts itself, and the row now records this. The v3 ClickHouse/Redis/S3 complexity and OTel-native SDK text is confirmed |
| CI2026-059-003 GHSA-2524-j966-gfgh | confirmed | `gh api`: CVE-2026-41487, severity low, published 2026-04-17T07:23Z. Affected range >=3.68.0 <3.167.0; Cloud patched April 9, 2026 1PM UTC. The timeline includes the Mar 31 mis-triage and the "April 16, 2025" year typo |
| CI2026-059-005 NVD record | corrected (clarified) | NVD API: published 2026-05-08T15:16Z, status Analyzed. The GitHub CNA score is **CVSS v4.0** 5.3 MEDIUM and the NVD score is **CVSS v3.1** 5.4 MEDIUM. CVSS versions were added |
| CI2026-059-004 Cloud Japan | confirmed | ap-northeast-1, jp.cloud.langfuse.com and "Full platform parity" appear in the changelog. "well over a hundred customers in Japan" appears in the blog |
| CI2026-059-006 Academy date conflict | confirmed | The May 14 changelog says "Today we're launching". The Apr 30 update says "Langfuse Academy (beta) is live" |
| CI2026-059-009 experiment-action | confirmed | `gh api`: repo created 2026-04-20T11:38Z, MIT. The v1.0.0 release was published 2026-05-05T12:06Z. The Apr 30 update already links the Experiments GitHub Action |
| CI2026-059-011 full-text search | confirmed | "beginning to roll out ... v4 preview". Indexes cover Mar 31–May 27, 2026. The May update gives 18 seconds / 494 GB, now "under half a second" and "less than a gigabyte" |
| CI2026-059-018 finance gate case | confirmed | 81.3%, a 150-item FinanceBench run (with Claude Sonnet), an 85% numerical-accuracy gate and "one of the five largest banks in the world". Displayed date July 15, 2026 |
| CI2026-059-019 eval-setup post date | confirmed | Slug 2026-07-16; displayed date "July 22, 2026" |
| CI2026-059-023 v4 GA | confirmed | "seconds to milliseconds", "at least 10x faster" dashboards, site banner "up to 165x faster", "Langfuse Cloud becomes v4-only on November 16, 2026"; dated August 17, 2026 |
| CI2026-059-024 LICENSE commit 907194fdfe | corrected | `gh api`: author date 2026-08-18T08:06Z; this commit changed only `LICENSE` ("Langfuse GmbH" became "ClickHouse, Inc."). **But** the report said `ee/LICENSE` was untouched, and that was wrong: the sibling commit `5621699bd7` (2026-08-18T08:07Z, same message "docs: update license") changed the `ee/LICENSE` copyright to "ClickHouse, Inc" and replaced the Langfuse Terms of Service reference with an agreement "as agreed by you and Langfuse GmbH or ClickHouse, Inc.". The row and section 2 were corrected. The site footer still reads "Langfuse GmbH / Finto Technologies Inc." |
| CI2026-059-026 status incident h3t8vhtd + index count | corrected (limitation) | Confirmed: EU Ingestion API degraded, "scaled our database infrastructure", latest major SDKs not impacted. The status index lists 14 resolved incidents (8 in Aug, 6 in Sep, 2026-08-03 to 2026-09-30). The embedded JSON *does* carry UTC timestamps (10:30Z–15:10Z), so the "no stated timezone" limitation was narrowed |
| CI2026-059-029 status incident trdzkge0 | corrected (event date) | Confirmed: "ingestion delay of old SDKs by 3 hours", then "about 60 minutes", then resolved. The embedded JSON gives the impact start as 2026-09-13T23:51Z and resolution as 2026-09-14T06:10Z, so `event_date_utc` was set to 2026-09-13 |
| CI2026-059-030 Jev judge | confirmed | "$0.042 per million" input tokens appears in both the Sep 22 changelog and the Sep 30 update. The 20–200x / 40–400x multiples were not re-checked |
| CI2026-059-031 jacar.es migration | confirmed | datePublished 2026-09-25. Migration from v3.225.8 to v4.37.0. The new compose "can lower ClickHouse's version". On a fresh install the worker started before web and ten background migrations were left failed until `restart langfuse-worker`. The author did not measure the "at least 10x" claim. Canonical URL confirmed |

No personal identifier was sent in any request. Pages were treated as untrusted data.
