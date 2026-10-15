# Make — provisional six-month technology intelligence screen (050)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](050-make.events.csv) and [search log](050-make.search-log.md) are **provisional, AI-assisted documentary source leads** for [issue #117](https://github.com/MSKazemi/github-trending-1000-study/issues/117). They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Nothing here is scientific or security sign-off; issue #117 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 050; [issue #117](https://github.com/MSKazemi/github-trending-1000-study/issues/117). **Study lens:** reuse of workflow templates and integration patterns.
- **Window:** 2026-04-12 through 2026-10-12 inclusive. **Source-screened on 2026-10-16.** Exact UTC search-run times, full search result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen.** It has 26 source leads covering all seven calendar segments and has not been reviewed by a qualified human. It is not independently verified, not an exhaustive retrieval, and not a human-approved scientific result. The shared web-search quota ran out during the screen, so independent-press coverage is thin (see the [search log](050-make.search-log.md)). Method: [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [make.com](https://www.make.com/), [2026 release-notes index](https://help.make.com/2026), [What's New](https://www.make.com/whats-new), [blog](https://www.make.com/en/blog), [status page history feed](https://status.make.com/history.rss), [developer docs](https://developers.make.com/make-cli), and public code under the [`integromat` GitHub organization](https://github.com/integromat). **Claim grading** uses the company-watch E0–E4 tiers, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](050-make.search-log.md) lists the queries actually run and the official pages read directly, with include/exclude decisions for each segment. The dated backbone is the vendor's [2026 help-center release index](https://help.make.com/2026). It is supplemented by individual release notes, the official status-page RSS (which covers only **2026-06-21 to 2026-10-12**), two vendor blog posts, and GitHub/npm metadata.

Model-catalog additions (new Claude, GPT, Gemini and Grok versions inside Make connectors) are frequent. They were logged but **not ledgered** as Make capabilities. Make security advisories and CVEs for the window were **not found**. Because no dedicated advisory index was located, this is "unknown", not "zero". Pre-Jun 21 outages appear only on third-party aggregators and are **excluded as unverified**.

## 2. Corporate/product identity and rights baseline

**Make** (make.com) is the visual workflow-automation platform formerly called **Integromat**. A 2021-01-28 Make blog post states it "was officially acquired by Celonis … on October 14, 2020" ([source](https://www.make.com/en/blog/integromat-2020-in-review)). Two in-window artifacts support continued Celonis ownership as of the window:

- The make.com terms page footer reads "© 2026 Celonis, Inc." ([terms](https://www.make.com/en/terms-and-conditions)).
- The status page operates `eu1.make.celonis.com` and `us1.make.celonis.com` zones ([status feed](https://status.make.com/history.rss)).

The contracting entity, Make's internal structure within Celonis, and filing-level ownership were **not verified**. The rename from Integromat is pre-window baseline, and the public GitHub organization still uses the name `integromat`.

**Rights scope:**

- **Hosted platform:** the scenario platform, Maia, Make Grid and the Make AI Provider are proprietary hosted services under Make terms.
- **Public repositories:** the repos examined ([make-cli](https://github.com/integromat/make-cli), [make-skills](https://github.com/integromat/make-skills), [make-endpoints-sdk](https://github.com/integromat/make-endpoints-sdk), [make-blueprints](https://github.com/integromat/make-blueprints)) declare **MIT** licenses in GitHub metadata. They are clients, skills and SDKs for the proprietary service, not source for the platform.
- **Templates:** template and blueprint reuse rights inside Make's own template gallery were **not examined**.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed/index publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | Apr 15 [Module Migrator](https://help.make.com/introducing-module-migrator); Apr 17 [Make CLI GA note](https://help.make.com/the-make-cli-is-now-live); Apr 24 [make-cli v1.4.0](https://github.com/integromat/make-cli/releases/tag/v1.4.0) | The CLI's first release (v1.0.0, Apr 2) is **pre-window**. The What's New page dates the CLI Apr 20. The CLI repo had no push after Apr 24 through Oct 12. |
| May | May 11 [Make Functions app](https://help.make.com/new-make-functions-app); May 25 [Make Skills open beta](https://help.make.com/introducing-make-skills) | Skills are **open beta**. Help-page `createdAt` metadata (Mar 24, May 18) precedes the index dates. The May 13 and May 22 outages are aggregator-only and **excluded**. |
| June | Jun 1 Claude 4 deprecation notice ([index](https://help.make.com/2026)); Jun 3 [MCP tools in AI Agents (New)](https://help.make.com/make-ai-agents-new-mcp-tools-are-now-available); Jun 29–30 [field-clearing blueprint bug](https://status.make.com/incidents/07pn8l856njv) | The deprecation's execution on Jun 15 was not observed. The incident is vendor-reported and its scope was still under analysis when it was marked resolved. |
| July | Jul 8 [Make Grid maps n8n / Claude Managed Agents / Relevance AI](https://help.make.com/connect-your-third-party-automation-and-ai-agents); Jul 8 [Grid content search](https://help.make.com/content-search-in-make-grid); Jul 27 [sub-agents and tool-output filtering](https://help.make.com/sub-agents-and-tool-output-filtering-are-now-available-in-the-make-ai-agent-new-app) | Grid gives read-only mapping and search, not cross-platform execution. Sub-agents allow one nesting level. Private spaces (Jul 17) is noted but not ledgered. |
| August | Aug 3 [make-blueprints repo](https://github.com/integromat/make-blueprints) (empty); Aug 4–10 [model unavailability](https://status.make.com/incidents/klbdpdcxl01s); Aug 12 [Maia launch blog](https://www.make.com/en/blog/maia-conversational-ai-coworker-for-ai-agents-and-automation); Aug 12 [connection/key usage notifications](https://help.make.com/introducing-connection-and-key-usage-notifications); Aug 13 [cycles removal notice](https://help.make.com/cycles-removal-on-october-1-2026); Aug 14 [deployment rollback](https://status.make.com/incidents/q9vl12qn8wc1); Aug 24 [AI Provider token pricing](https://help.make.com/more-value-for-your-credits-updated-makes-ai-provider-token-pricing-model) | Maia status **conflicts**: the blog says "live today for all Make users", while the [help note](https://help.make.com/meet-maia-your-ai-and-automation-co-worker) says "public beta for all paid plans". Maia was first announced in Oct 2025 (pre-window). |
| September | Sep 9 [Make plugin for ChatGPT](https://help.make.com/official-make-plugin-for-chatgpt-is-now-available); Sep 16 [plugin blog with temporary-disablement notice](https://www.make.com/en/blog/make-plugin-chatgpt) | At access (2026-10-16) the blog states that OpenAI temporarily disabled the plugin. When the disablement started is **unknown**. |
| Oct 1–12 | Oct 7 [make-skills MCP Registry commit](https://github.com/integromat/make-skills/commit/0abffba9158bc616fed8eea75fb6e24ab482c769); Oct 7 [version control](https://help.make.com/improved-scenario-toolbar-and-version-control); Oct 7 [make-endpoints-sdk v0.1.0](https://github.com/integromat/make-endpoints-sdk/releases/tag/v0.1.0); Oct 8 [event subscriptions](https://help.make.com/introducing-event-subscriptions); Oct 9 [AI Agent fallback/caching/MCP audit logs](https://help.make.com/make-ai-agent-improvements-new-ai-models-sso-login-routing-and-mcp-tools-for-audit-logs); Oct 12 [Scenario-app (subscenario) failures](https://status.make.com/incidents/kmfmzcvvcwpp) | The Endpoints SDK is **closed beta**. Its v0.5.0/v0.6.0 releases (Oct 14–15) and Make Waves '26 (Oct 19–20) are **outside the window and excluded**. |

The [CSV](050-make.events.csv) holds the **26 dated source records**. The segment counts (3/2/3/3/7/2/6) reflect where official dated sources were found. They are **not** a measure of release cadence. A purposive selection centred on the reuse/interoperability lens is not a census of all Make releases.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited document supports | Important non-equivalence or counterexample |
|---|---|---|
| Agent-facing access: [CLI](https://help.make.com/the-make-cli-is-now-live) → [Skills](https://help.make.com/introducing-make-skills) → [ChatGPT plugin](https://help.make.com/official-make-plugin-for-chatgpt-is-now-available) → [MCP Registry commit](https://github.com/integromat/make-skills/commit/0abffba9158bc616fed8eea75fb6e24ab482c769) → [Endpoints SDK](https://github.com/integromat/make-endpoints-sdk) | Make is publishing several machine-facing ways for coding agents and chat assistants to create, run and inspect scenarios. The repos are MIT-licensed. | Several are beta. The vendor warns that the CLI and Skills can modify or delete live resources. The plugin was disabled by a third party at access. Registry publication itself was not verified. |
| Template/integration reuse: [Module Migrator](https://help.make.com/introducing-module-migrator), [Make Functions](https://help.make.com/new-make-functions-app), [Grid content search](https://help.make.com/content-search-in-make-grid), [version control](https://help.make.com/improved-scenario-toolbar-and-version-control), Maia adapts pre-built templates ([help note](https://help.make.com/meet-maia-your-ai-and-automation-co-worker)), Skills commit "add popular templates as example files" ([repo](https://github.com/integromat/make-skills)) | Tooling to find where a module or webhook is reused, migrate deprecated modules, restore prior scenario versions and seed agents with templates | The public [make-blueprints](https://github.com/integromat/make-blueprints) repo was **empty** at access. Version control is restore-based, with no documented diff. No downstream-reuse or template-success measurements were found. |
| Interoperability: [MCP tools in agents](https://help.make.com/make-ai-agents-new-mcp-tools-are-now-available), [Grid third-party mapping](https://help.make.com/connect-your-third-party-automation-and-ai-agents), [event subscriptions](https://help.make.com/introducing-event-subscriptions) | Agents can call external MCP servers. Grid can map n8n workflows, Claude Managed Agents and Relevance AI agents. Signed outbound platform events have delivery logs. | Grid mapping is visibility, not portable execution. Exporting a Make scenario to another runtime is **not** documented here. The full event-type list is not on the page. |
| Failure handling: [Jun 29–30 blueprint bug](https://status.make.com/incidents/07pn8l856njv), [Aug 14 rollback](https://status.make.com/incidents/q9vl12qn8wc1), [Aug 4–10 model outage](https://status.make.com/incidents/klbdpdcxl01s), [Oct 12 Scenario-app failures](https://status.make.com/incidents/kmfmzcvvcwpp), [agent fallback connection](https://help.make.com/make-ai-agent-improvements-new-ai-models-sso-login-routing-and-mcp-tools-for-audit-logs) | Vendor-disclosed defects affected saved scenario blueprints, shared subscenario modules and third-party model availability. A single-retry fallback connection shipped Oct 9. | Status pages describe vendor-stated impact. They give no affected-customer counts or independent post-mortem. One retry is limited resilience. |
| Governance: [connection/key notifications](https://help.make.com/introducing-connection-and-key-usage-notifications), [custom roles](https://help.make.com/custom-roles-for-precise-access-control) (Enterprise), [private spaces](https://help.make.com/introducing-private-spaces), [MCP audit-log tools](https://help.make.com/make-ai-agent-improvements-new-ai-models-sso-login-routing-and-mcp-tools-for-audit-logs) | Shared credentials are visible and audited, roles are configurable, and members have isolated workspaces | Notifications do not block misuse. Audit-log entries and admin visibility are Enterprise-only. No independent security testing was found. |
| Breaking changes: [Claude 4 deprecation](https://help.make.com/2026), [cycles removal](https://help.make.com/cycles-removal-on-october-1-2026), [token pricing split](https://help.make.com/more-value-for-your-credits-updated-makes-ai-provider-token-pricing-model) | Upstream model churn and platform semantic changes impose maintenance on existing (including reused) scenarios | Execution of the scheduled changes and their real billing or behavioural effect were not observed. Credits are not energy. |

**Counterevidence and rights:** MIT-licensed client repos do **not** license the hosted platform, templates in Make's gallery, or connector behaviour. The `[AI code generation]` label in one make-skills commit is a repository's own label. It is **not** an authorship audit, and nothing here identifies individual developers. The make-skills CHANGELOG repeats the same feature list across 0.1.5–0.1.7, so it is a weak change record. Commit history is the better trace.

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source (≤25-word quotes) | Company-stated intention | Research classification |
|---|---|---|
| [Aug 12 Maia blog](https://www.make.com/en/blog/maia-conversational-ai-coworker-for-ai-agents-and-automation): more expert capabilities "coming soon"; aiming for Maia "present everywhere you go in Make" | Wider Maia presence, more knowledge of the team's automation estate, proactive suggestions | **Announced only**; no dates. The Oct 9 note adds a run-improvement suggestion feature, which is partial delivery of unknown scope. |
| [Sep 16 plugin blog](https://www.make.com/en/blog/make-plugin-chatgpt): "We'll update this article as soon as plugin access is restored." | Plugin restoration, which depends on OpenAI | **Unavailable/unknown** at access |
| [make-endpoints-sdk README](https://github.com/integromat/make-endpoints-sdk) (closed beta): "Beta feedback shapes 1.0." | A 1.0 SDK | **Preview**; the 0.x API may change between versions |
| Create With [Aug 28](https://www.createwith.com/tool/make/updates/make-puts-maia-at-the-center-of-a-broader-workspace-overhaul) paraphrasing a LinkedIn post by Make's CPTO: Make now ships in one or two quarters what previously took a year | Faster delivery cadence | **Secondary, AI-drafted paraphrase** of a post not read here; E0 lead only |

A public intention is not a scheduled delivery. None of these establish Make's 2027–2031 strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Workflow platforms become agent-addressable back-ends (CLI/MCP/skills), so coding agents assemble automations from existing connectors instead of writing integration code | Agents may write direct API glue just as cheaply. MCP-native SaaS may bypass automation platforms entirely. | Matched tasks show equal or better accepted outcomes, with lower lock-in, from direct code than from platform-mediated builds |
| Cross-platform inventories (Grid) make reuse safer by exposing dependencies before change | Teams may standardise on one platform, making mapping unnecessary | Impact-search recall is poor, or incidents caused by shared-component changes do not decline |
| Shared, reused components concentrate failure, as when the Oct 12 Scenario-app failure hit every subscenario user | The same blast radius exists for any shared library | Reused-component incidents are not more frequent or severe than per-scenario duplication |

## 7. M1–M7 study relevance

| Construct | Prospective measurement, not an inferred conclusion |
|---|---|
| **M1** coding practice | Opt-in records of whether coding agents use the Make CLI/MCP/Skills or write direct API code for the same integration task. Self-applied "AI code generation" labels are not detection. |
| **M2** accepted task quality | Independently authored acceptance tests for integration tasks, counting failed, refused and timed-out attempts. Platform incidents (Jun 29–30, Oct 12) are a threat to validity for any trial window. |
| **M3** discovery | Whether agent-facing listings (MCP Registry, plugin directories) change discoverability. This is not measured by stars or plugin installs. |
| **M4** verified third-party reuse | Trace consented downstream use of public Make templates or SDKs. The empty make-blueprints repo is **not** reuse evidence. |
| **M5** reuse-first | Compare reusing an existing connector or template against generating new integration code, under matched specifications that include no-solution tasks |
| **M6** lifecycle human and energy cost | Maintenance minutes caused by deprecations, cycle removal and model churn, plus credit or invoice cost. **No token-to-CO2e conversion**: credits and tokens are not energy. |
| **M7** actionable interventions | Whether a published, versioned, tested template (with a migration note) improves first-use success compared with a prose how-to |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** a separate, *authorized* sandbox outside [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The study's live Trending `capture` stays **disabled under the source-access decision**. No automation platform makes unapproved scraping permissible, and none of the tasks below touch GitHub Trending.

**Frozen task (functional unit = one independently accepted integration task):** "When a GitHub issue in a synthetic test repo gets label `X`, post a formatted notice to a test chat webhook and append one row to a test spreadsheet; retries must not duplicate rows." Freeze 10 task variants before the trial, including 2 deliberately unsatisfiable (no-solution) variants. All of them stay in the denominator. Hidden acceptance assertions (row count, idempotency on retry, payload fields, no secret in logs) are authored by someone other than the person or agent doing the work.

**Arms:**

- **A (reuse-first):** start from an existing Make template or connector, built via the Make UI or the [Make CLI](https://developers.make.com/make-cli) at a pinned version.
- **B (comparator):** the maintainer's usual practice, a small GitHub Actions workflow plus direct API calls written with or without a coding agent.

Both arms use the same test accounts, the same least-privilege credentials and the same time box.

**Primary endpoint:** independently accepted tasks divided by all assigned tasks.

**Secondary endpoints:**

- Human minutes (build, review, debugging)
- 30-day maintenance minutes, logging any deprecation or platform change that forces edits
- Credits or CI minutes as billed
- Credential exposure, which must be zero
- Portability: minutes to move the accepted solution to the other arm

**Measurement boundary:** energy is reported only if actually metered. Nothing is converted from tokens or credits.

**Stop rule:** stop and favour B if any of these occur:

- any secret appears in logs or exports
- A requires a paid tier or terms that permit the vendor to reuse the test data
- A fails ≥3 of 8 satisfiable variants
- a platform incident invalidates the run window

Favour the simpler arm whenever acceptance is equal. **No trial has been executed and no effects are estimated.** A null or negative result for A is a valid result and must be preserved.

## 9. Findings, uncertainties and review status (2026-10-16)

- **Observed/shipped (vendor-documented, E1–E2):** CLI GA; Module Migrator; Make Functions; MCP tools in agents; Grid third-party mapping and content search; sub-agents; connection/key notifications; version control; event subscriptions; agent fallback and prompt caching. Public MIT code artifacts were checked via the GitHub and npm APIs.
- **Preview / beta:** Make Skills (open beta), Maia (public beta per help page, which conflicts with the blog), Make Endpoints SDK (closed beta).
- **Announced only / undetermined:** Claude 4 deprecation, Oct 1 cycles removal, token-pricing effect, MCP Registry listing, ChatGPT-plugin restoration.
- **Contrary or null evidence:** four vendor-disclosed incidents (blueprint field-clearing, deployment rollback, model unavailability, subscenario failures); an empty public blueprints repo; the CLI repo was inactive after Apr 24; the plugin was disabled by a third party.
- **Unknowns:** the contracting entity and filing-level ownership; any Make security advisories; pre-Jun 21 official incident history; independent press coverage (the search quota ran out); the reasons for the index vs `createdAt` vs What's New date disagreements; template-gallery licensing; actual adoption or task outcomes.
- **Pending:** human factual/link spot-check, source-access/rights review, methods review, re-running the two unexecuted queries, and confirming the plugin status. **Issue #117 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.** on the strength of this screen.
