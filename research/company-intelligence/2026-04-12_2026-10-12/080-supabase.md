# Supabase — provisional six-month technology intelligence screen (080)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](080-supabase.events.csv) and [search log](080-supabase.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 080
- **Research issue:** [#148](https://github.com/MSKazemi/github-trending-1000-study/issues/148); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Supabase Inc. (CNBC caption "Courtesy: Supabase Inc."), co-founded by CEO Paul Copplestone and CTO Ant Wilson; privately held and venture-funded (Series F, June 2026). No parent company was found. Supabase announced it **is acquiring Turso** on 2026-10-02 (confirmed by Turso the same day); closing was not reported in the window. Pre-window acquisitions named in the blog feed (Hydra, BKND, Feb 2026) are baseline only. Filing-level corporate verification was **not** performed.
- **Offering:** hosted Postgres "backend" platform (Database, Auth, Storage, Realtime, Edge Functions, Data API via PostgREST/pg_graphql), CLI, client SDKs, an official MCP server, and self-hosting via Docker Compose.
- **Product URL and source channels:** [supabase.com](https://supabase.com/), [blog](https://supabase.com/blog) ([RSS](https://supabase.com/rss.xml)), [changelog](https://supabase.com/changelog) ([RSS](https://supabase.com/changelog-rss.xml)), [status page](https://status.supabase.com/) (moved to incident.io on 2026-10-08), [GitHub org `supabase`](https://github.com/supabase) and [`supabase-community/supabase-mcp`](https://github.com/supabase-community/supabase-mcp), npm `@supabase/*` and `supabase`, PyPI `supabase`, GitHub security advisories per repository.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 44 ledger rows across all seven calendar segments.
- **Source coverage:** 28 in-window blog posts (all read as raw HTML), 47 in-window changelog entries (all 47 fetched; 13 ledgered, others used as context or listed), status RSS (covers 2026-07-18 onward) plus three incident pages, GitHub API (repos, releases, security advisories for 33 repositories, one commit), npm and PyPI registry JSON, Hacker News Algolia (167 in-window stories), and independent pages from CNBC, TechCrunch (two), UpGuard, Turso and an independent security researcher. WebSearch was not used. See the [search log](080-supabase.search-log.md).

## 1. Search and inclusion audit

Summary only; exact requests, opened URLs and exclusions are in the [search log](080-supabase.search-log.md).

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | supabase.com blog RSS + raw HTML | all items 2026-04-12..10-12 | 28 in-window posts | 28 | 18 rows | 10 posts not ledgered as own rows (explainers, minor features, partner/connector posts; two Select posts used as supporting sources; see log) | RSS gives date only; posts can be edited later (e.g. Pipelines Oct 2 note) |
| 2026-10-16 | changelog RSS + entry pages | entries 2026-04-12..10-12 | 47 | 47 opened | 13 rows | dev-update digests, minor fixes, items folded into blog rows | changelog date = posting date, not always effective date |
| 2026-10-16 | GitHub API | org repos created ≥2026-04-01; releases; `security-advisories` for 33 repos | 26 new repos; 4+1 in-window advisories | all | 5 rows (+ checks) | supabase/postgres Nix advisory (low, docs) not ledgered; storage advisories dated 2026-10-14 out of window | private/unpublished advisories invisible |
| 2026-10-16 | status.supabase.com RSS + pages | incidents | 55 RSS items (Jul 18–Oct 14) | 55 titles, 5 pages | 3 rows | many short regional incidents (log) | RSS does not reach April–mid-July; two older incident pages reached via HN links |
| 2026-10-16 | HN Algolia `query=supabase`, stories, window bounds | 2026-04-12..10-12 | 167 | 167 titles; 9 linked pages fetched | 5 rows | Show HN projects, blogs without in-window Supabase events | HN is a lead source, not a census of coverage |

## 2. Verified company/product identity and baseline

Supabase packages open-source components around Postgres. In the window the main platform repo [supabase/supabase](https://github.com/supabase/supabase) reports Apache-2.0 and 111,611 stars (GitHub API, 2026-10-16; stars are context, not adoption). Client SDKs and new packages (`@supabase/server`, `@supabase/middleware`, `@supabase/pg-delta`, `supabase-go`, `supabase/sdk`) are MIT; `supabase/evals`, `supabase/realtime`, `supabase/etl`, `multigres/multigres` and `orioledb/orioledb` are Apache-2.0 (GitHub API). The hosted control plane, billing and multi-tenant operations are proprietary services; an open-source component does not confer any right to the hosted platform.

Pre-window baseline (context only, not counted): agent skills post (2026-04-09), custom OIDC providers (2026-04-08), 100,000 GitHub stars post (2026-04-02), Hydra and BKND joining (Feb 2026), and a $100M round at a $5B valuation in October 2025 as reported by [TechCrunch](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/). **Post-window, excluded:** blog posts dated 2026-10-13 to 10-15 (Declarative Schemas 2.0 deep-dive, local project per agent, branch config), .NET OpenTelemetry (2026-10-14), and two **critical** supabase/storage advisories published 2026-10-14 (GHSA-8rrf-w776-x75g, GHSA-67rp-h2mf-ph72), which a follow-up screen should pick up.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Stripe Sync Engine moved to Stripe (Apr 14); pg-delta declarative schema alpha (Apr 16); ISO 27001 (Apr 22); RLS tester preview (Apr 24); OSSCAR Index (Apr 28); Data API stops auto-exposing new tables (Apr 28) | [blog](https://supabase.com/blog/stripe-sync-engine-transfer), [changelog](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically), [blog](https://supabase.com/blog/introducing-osscar-index) | GitHub API shows `stripe/sync-engine` (Apache-2.0) and `commitvc/osscar` (MIT) | client retry change (Apr 20) and tax notice (Apr 17) not ledgered |
| 2026-05 | Git-free branching default (May 4); `@supabase/server` (May 6); CLI LICENSE moved in monorepo (May 6); ChatGPT app (May 8); pg_graphql introspection off (May 25); npm supply-chain post naming a typosquat (May 26) | [blog](https://supabase.com/blog/introducing-supabase-server), [commit](https://github.com/supabase/cli/commit/cad09571874a22db60da5ecbfcc047bf35cf6e0a), [blog](https://supabase.com/blog/protecting-your-supabase-projects-from-npm-supply-chain-attacks) | npm registry record of `supabase-javascript` (created May 12, unpublished May 13) | Postgres 14 end-of-support, OAuth 201→200, self-hosted PG17, passkeys beta, temporary DB tokens: listed, not ledgered |
| 2026-06 | Free-tier email-template lock after phishing abuse (Jun 3); Series F (Jun 4); Multigres v0.1 alpha (Jun 4; GitHub release May 30); two Realtime advisories (Jun 16, Jun 25); OpenCode integration and multi-region capacity incident (Jun 30) | [changelog](https://supabase.com/changelog/46599-changes-to-email-template-customisation-on-free-tier), [blog](https://supabase.com/blog/supabase-series-f), [status](https://status.supabase.com/incidents/3tx3nnmbwyh9) | [CNBC Jun 4](https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html); [TechCrunch Jun 5](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/) | Realtime binary payloads, log_connections default change not ledgered |
| 2026-07 | Realtime schema lockdown (Jul 14; release Jul 7); self-hosted Envoy replaces Kong (Jul 17); Pipelines public alpha (Jul 21); extension version pinning ignored (Jul 22); Sign in with ChatGPT beta (Jul 29); Supabase Evals open-sourced (Jul 31) | [changelog](https://supabase.com/changelog/48048-self-hosted-supabase-envoy-becomes-the-default-api-gateway-b), [blog](https://supabase.com/blog/introducing-supabase-evals) | none found beyond HN reposts | CipherStash (Jul 9), Grafana (Jul 23), Unified Logs beta (Jul 16) not ledgered |
| 2026-08 | Agent-friendly docs eval (dated Aug 1); independent PostGIS/managed-Postgres research naming Supabase (Aug 14); Realtime log-injection advisory (Aug 17); MCP enterprise-managed auth GA (Aug 24); supautils/GLIBC incident (Aug 28) | [blog](https://supabase.com/blog/are-supabase-docs-agent-friendly), [researcher](https://mehmetince.net/part-1-6-systemic-risks-in-the-managed-postgresql-industry-extension-risks-are-real-exploiting-postgis-memory-corruption-bug-at-neondb-supabase-and-many-more/) | researcher blog (independent, single source) | Perplexity connector (Aug 7), Postgres Changes filters (Aug 5), client trace propagation (Aug 18) not ledgered |
| 2026-09 | Auth outage (Sep 16); high Realtime advisory and UpGuard exposure research (Sep 24); TechCrunch report, Postgres 15.19/17.11 rollout, logs usage pricing (Sep 25) | [advisory](https://github.com/supabase/realtime/security/advisories/GHSA-9vjf-j9f7-j42c), [UpGuard](https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps) | [TechCrunch Sep 25](https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/) | Gemini Enterprise connector (Sep 9), Health Check Advisors (Sep 18), Middleware 1.0 (Sep 30) folded or listed |
| 2026-10-01..12 | OrioleDB public beta (Oct 1); Turso acquisition (Oct 2); Supabase Select launches and recap (Oct 2); `@supabase/server` adapters deprecated (Oct 5); TLS CBC cipher deprecation notice (Oct 12) | [blog](https://supabase.com/blog/supabase-is-acquiring-turso), [blog](https://supabase.com/blog/supabase-select-2026-recap), [changelog](https://supabase.com/changelog/cbc-tls-ciphers-deprecated) | [Turso](https://turso.tech/blog/turso-is-joining-supabase) (second entity) | scoped PATs GA (Oct 6), Go SDK alpha (Oct 5), .NET official (Oct 9), status page move (Oct 8) listed in log |

No calendar segment was empty.

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](080-supabase.events.csv) (44 rows, IDs `CI2026-080-001`…`044`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-080-005 | 2026-04-28 | OSSCAR Index: growth ranking of OSS orgs from stars, contributors, downloads | live; MIT code | [blog](https://supabase.com/blog/introducing-osscar-index) | [commitvc/osscar](https://github.com/commitvc/osscar) | E2 (documentary) |
| CI2026-080-006 | 2026-04-28 (staged to 2026-10-30) | New tables not exposed to Data/GraphQL API without explicit grants | existing-project step after window | [changelog](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically) | none | E1 |
| CI2026-080-009 | 2026-05-06 | CLI MIT LICENSE moved to `apps/cli-go/`; GitHub API now reports no repo licence | observed | [commit](https://github.com/supabase/cli/commit/cad09571874a22db60da5ecbfcc047bf35cf6e0a) | npm `supabase` declares MIT | E2 |
| CI2026-080-012 | 2026-05-26 / typosquat 2026-05-12 | `supabase-javascript` typosquat; supply-chain hardening | guidance | [blog](https://supabase.com/blog/protecting-your-supabase-projects-from-npm-supply-chain-attacks) | [npm record](https://registry.npmjs.org/supabase-javascript) | E2 |
| CI2026-080-014/015 | 2026-06-04 | $500M Series F, $10B pre-money; usage claims | not product | [blog](https://supabase.com/blog/supabase-series-f) | [CNBC](https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html) | E1 / E2 |
| CI2026-080-026 | 2026-07-31 | Supabase Evals: open agent benchmark; skills and docs-usage findings | Apache-2.0 repo | [blog](https://supabase.com/blog/introducing-supabase-evals) | [supabase/evals](https://github.com/supabase/evals) | E2 (documentary; self-evaluation) |
| CI2026-080-017/018/029/033 | 2026-06-16 … 09-24 | Four Realtime security advisories (low, medium, low, high) | three with patched versions; the high one lists none | GitHub advisories | GitHub API | E2 |
| CI2026-080-034/035 | 2026-09-24 / 09-25 | 16,326 Supabase databases exposing readable tables (customer misconfiguration) | research | [UpGuard](https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps) | [TechCrunch](https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/) | E2 (independent documentary), not E3 |
| CI2026-080-039/040 | 2026-10-02 | Turso acquisition announced | closing unknown | [Supabase](https://supabase.com/blog/supabase-is-acquiring-turso) | [Turso](https://turso.tech/blog/turso-is-joining-supabase) | E1 / E2 |
| CI2026-080-041 | 2026-10-02 | Docker-free local stack, declarative schemas, Compute (private alpha), app MCP server | mixed alpha | [blog](https://supabase.com/blog/select-2026-build-anything) | none | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent surfaces | ChatGPT app (29 tools), OpenCode plugin with bundled skills, MCP server 0.8.0→0.13.0 on npm, enterprise-managed MCP auth (Okta), MCP Elicitations, `query_logs` MCP tool, Sign in with ChatGPT beta, app-level MCP server block | shipped / beta (vendor) |
| Schema-as-code | pg-delta diff engine (alpha), Git-free branching default, Declarative Schemas 2.0, `supabase config pull` | alpha → default for some flows |
| Server SDKs | `@supabase/server` (May), `@supabase/middleware` 1.0 (Sep), adapters deprecated (Oct), Go SDK public alpha, .NET SDK made official | shipped, fast churn |
| Security defaults | explicit Data API grants, pg_graphql introspection off, extension version pinning ignored, Realtime schema lockdown, free-tier email template lock, scoped PATs GA, TLS CBC removal notice, ISO 27001 claim | staged; several breaking |
| Data infrastructure | Multigres (OSS alpha; platform private alpha), OrioleDB public beta, Pipelines / supabase ETL public alpha, Turso acquisition | alpha/beta |
| Evaluation and discovery | Supabase Evals (Apache-2.0), docs evaluated with agents, OSSCAR Index (MIT), dbarena benchmark site | shipped (vendor) |
| Licensing/stewardship | Stripe Sync Engine transferred to Stripe (Apache-2.0); Kong replaced by Envoy in self-hosting citing Kong 3.10 removing free mode; CLI LICENSE file relocated | observed / vendor-stated |
| Breaking changes | Data API grants, OAuth token status 201→200, pg_graphql 1.6.0, self-hosted PG15→17 and Studio role, Envoy gateway, Postgres 15.19/17.11 (pgcrypto legacy ciphers), TS 5.0 floor from 2027-01-31, adapter removal 2026-12-01 | observed in changelog |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Round funds "development of open source / Postgres tools", growth and employee liquidity; Multigres "will provide Vitess-grade horizontal scaling" | [Series F, 2026-06-04](https://supabase.com/blog/supabase-series-f) | "a few months" (Multigres production) | partly delivered (platform private alpha Oct 1) | Sharding "later"; not production-ready in window |
| OrioleDB "targeting production-readiness this year" | same | 2026 | tentative | Public beta Oct 1 says not for production, no SLA |
| Data API grant change applied "to all existing projects" on 2026-10-30 | [changelog, 2026-04-28](https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically) | 2026-10-30 | planned | UpGuard describes related RLS defaults as still weak |
| "Supabase now works code first … You decide what gets fixed and merged." | [Select recap, 2026-10-02](https://supabase.com/blog/supabase-select-2026-recap) | none | uncommitted direction | Compute private alpha only |
| Bring "the Supabase experience to every agent"; Turso keeps SQLite work, Supabase keeps Postgres | [Turso post, 2026-10-02](https://supabase.com/blog/supabase-is-acquiring-turso) | "coming months" (Turso post) | announced | Deal closing and terms not disclosed |
| SCIM provisioning "on the roadmap"; log drains to Grafana "in progress"; agent feedback CLI/MCP tool planned | [MCP auth](https://supabase.com/blog/enterprise-managed-auth-for-the-supabase-mcp-server), [Grafana](https://supabase.com/blog/observability-for-every-supabase-project-with-grafana-cloud), [Evals](https://supabase.com/blog/introducing-supabase-evals) | none | planned, undated | — |
| Logs usage-based pricing enforced after a grace period "through early 2027"; TS 5.0 floor from 2027-01-31; CBC ciphers removed no earlier than 2026-11-10 | [logs](https://supabase.com/changelog/logs-usage-based-pricing), [TS](https://supabase.com/changelog/47812-deprecation-notice-supabase-supabase-js-will-require-typescript-5-0), [TLS](https://supabase.com/changelog/cbc-tls-ciphers-deprecated) | dated | planned | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Backend platforms will be chosen and configured mainly by coding agents, making agent-facing defaults (grants, RLS, elicitations) the main security lever | Vendor: >60% of new databases launched by AI tools; CNBC: Claude Code largest contributor; UpGuard: 16,326 exposing DBs; docs eval found agents granting anon writes | Vendor and press numbers are unaudited; exposure may be driven by inexperienced humans regardless of agents | Independent scans show exposure rates in agent-built apps no higher than in hand-built apps; or default changes do not reduce exposure counts | low–moderate; no denominators |
| H2: Vendors will publish their own agent benchmarks and tune docs/skills to them | Supabase Evals; agent-friendly docs work; skill activation tuning (1 in 10 → 60%) | Marketing; self-evaluation bias; small scenario sets | Independent replication shows no accepted-task gain from vendor skills | low; vendor-only data |
| H3: Fast secure-default and API churn transfers maintenance cost to reusers | ≥8 breaking/deprecation notices in window; `@supabase/server` adapters deprecated five months after launch | Changes are small and mostly opt-in; agents may absorb migrations | Pinned example repos need near-zero migration minutes across the window | moderate for churn, unknown for cost |
| H4: "Per-agent databases" (SQLite-class) will become a distinct product layer beneath Postgres platforms | Turso acquisition; "over one million databases per week" claim; Docker-free per-directory local stacks | Consolidation/financial motives; usage claims unverified | The acquisition is never completed, or per-agent DB usage stays niche by 2028 | low |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents invoke backends through MCP/plugins; vendor reports agents rarely read docs (Claude Code <40% of scenarios) | Record, with consent, which interface an agent uses per task | Vendor harness differs from real use | Only consented logs; vendor percentages not reused as data |
| M2 accepted task quality | RLS/grant mistakes are silent failures; docs edits changed eval outcomes | Hidden acceptance tests that probe anon access, not only functional behaviour | Agents already pass most tasks (vendor) | All attempts in denominator |
| M3 discoverability | OSSCAR ranks growth by stars/contributors/downloads; Supabase is "most recommended by Claude Code" (UpGuard) | Treat such rankings as exposure signals only; compare with verified reuse | Stars and rankings are not use | No star or ranking metric as outcome |
| M4 verified third-party reuse | Stripe adopted the sync engine repo; Turso/OSS components; OpenAI Agents-style integrations | Trace pinned downstream repos that import and execute components | Code transfer is not usage | Pinned commits, executed tests |
| M5 rights/security/provenance | Repo-level licence no longer detected for supabase/cli; typosquat; four Realtime advisories; 16k exposed customer DBs | Licence check at pinned commit (file path aware); package-name verification; grant/RLS scanner in CI | Detection tooling false negatives | Licence files and advisories at fixed dates |
| M6 review/maintenance and lifecycle cost | Breaking notices and deprecations; logs usage pricing; capacity incident Jun 30–Jul 13 | Migration minutes per notice on a pinned sample app | Notices may not affect small apps | No energy inferred from pricing, tokens or DB counts |
| M7 actionable interventions | Explicit grants, scoped tokens, MCP confirmation prompts as low-cost guardrails | See §8 | Guardrail friction without exposure reduction | Synthetic, local-only until approval |

Company adoption claims (e.g., "nearly 10 million developers", "over one million databases per week") are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) has no Supabase dependency and the disabled Trending `capture` command stays disabled. The experiment therefore uses a **throwaway, local-only, synthetic** Supabase stack (open-source CLI, no hosted project, no real data) in a separate scratch repository, testing a **reusable guardrail** rather than adopting the platform.

**Candidate practice (not yet validated):** Before accepting an agent-proposed database schema change, run an automated "default-deny" access check (an anon-role query script asserting no unintended SELECT/INSERT/UPDATE/DELETE grants and RLS enabled on every exposed table). Reuse first: compare (A) the plain SQL checks the maintainer writes from Postgres catalog views, with (B) an existing open-source checker found in the window, such as the single-file SQL audit linked on HN on 2026-09-20 as `Concepto505/supabase-audit` (the GitHub API now resolves it to [EstasDespedido/supabase-audit](https://github.com/EstasDespedido/supabase-audit), MIT, created 2026-09-20; code not yet reviewed), after licence and code review. Build nothing new if (B) passes review.

**Treatment/control and frozen comparable task:** Freeze 10 small synthetic schema tasks (e.g., "a public read-only dashboard table", "a per-user to-do list with sharing"). A person other than the agent operator writes hidden acceptance tests covering function **and** anon/authenticated access, kept out of agent context. Control: agent change reviewed by the maintainer without the access check. Treatment: same agent, model version, prompt and time budget, with the access check run before review. Accepted-task unit: one migration that passes the hidden tests and is accepted without rework.

**Success and guardrails:** Primary: accepted tasks / all 10 assigned (failed, refused, timed-out included) and count of over-permissive grants reaching "accepted". Guardrails: local stack only; no hosted Supabase project, no real credentials or personal data; no paid API spend without explicit approval; no new dependency in this study repository; full unit suite green. Measured human work: setup minutes, per-task review minutes, false-positive triage minutes. No energy or CO2e estimate unless metered. Commit authorship stays with the maintainer.

**Stop/reversal rule:** Stop and drop the check if it catches no over-permissive grant that the control review missed across the 10 tasks, or adds more than 5 review minutes per task on average, or (B) fails licence/security review. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** repository transfer to `stripe/sync-engine`; npm releases of `@supabase/server` (1.0.0 2026-05-06T09:27Z → 1.9.2 2026-10-12), `@supabase/middleware` 1.0.0 (2026-09-30T09:40Z), 48 `@supabase/pg-delta` alphas; `multigres/multigres` v0.1.0 (2026-05-30T00:08Z); Realtime v2.112.7 (2026-07-07); four in-window Realtime advisories; CLI LICENSE relocation; `supabase-javascript` typosquat record on npm; three status-page incidents.
- **Claims/announcements only:** usage numbers (600% database-launch growth, >60% by AI tools, ~10 million developers, >1 million databases/week, 250,000 customers via CNBC), ISO 27001, OrioleDB 1.8x, eval percentages, docs pageview statistics, 44 CVEs closed, staged default changes, Turso deal, all §5 items.
- **Conjectures and unknowns:** H1–H4; whether default changes reduce real exposure; Supabase's remediation of the PostGIS research; status history April–mid-July (only via two HN-linked pages).
- **Important contradictory or null evidence:** (a) Series F dated Thursday 2026-06-04 by Supabase and CNBC vs "announced Friday" by TechCrunch (2026-06-05); CNBC and Supabase name different subsets of investors; (b) `@supabase/server` called "public beta" while npm published 1.0.0 the same day; (c) Multigres GitHub release 2026-05-30 vs blog 2026-06-04; (d) agent-friendly docs post `datePublished` 2026-08-01 but cites data "through August 16"; (e) UpGuard JSON-LD date 2026-09-24 vs displayed "Publish date October 14, 2026"; (f) typosquat removal "a few hours later" (Supabase) vs ~17 h between npm creation and unpublish; (g) UpGuard says programmatically created tables lack RLS by default while Supabase's grant change (a different control) is staged to existing projects only on 2026-10-30; (h) Realtime advisory GHSA-pfwq metadata "low" vs body "Medium, CVSS 5.3"; GHSA-9vjf lists no patched version; (i) Supabase CISO: projects are "secure by default" (TechCrunch) vs UpGuard's 16,326 exposing databases — both can be true under shared responsibility; not resolved here.
- **#56 candidates (not minted):** CNBC 2026-06-04; TechCrunch 2026-06-05; UpGuard 2026-09-24; TechCrunch 2026-09-25 (same finding as UpGuard; count once); Turso 2026-10-02; Mehmet Ince 2026-08-14. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

An independent reviewer re-fetched the cited sources on 2026-10-16. Pages were retrieved as raw HTML with a generic browser User-Agent after checking each host's robots.txt. GitHub and npm were queried through their APIs. No personal identifier was sent to any site.

| Row | Outcome | Note |
|---|---|---|
| CI2026-080-008 | confirmed | The raw text has "public beta" and "25,000 deployed Edge Functions". npm `@supabase/server` is MIT; 1.0.0 was published 2026-05-06T09:27:37Z and 1.9.2 on 2026-10-12. |
| CI2026-080-009 | confirmed | Commit cad0957187 renames `LICENSE` to `apps/cli-go/LICENSE`. Its committer date is 2026-05-06T08:38:33Z and its author date 2026-05-05T09:43:31Z. The GitHub API reports no repository licence, and npm `supabase` declares MIT. |
| CI2026-080-012 | confirmed | `datePublished` 2026-05-26. The page has "supabase-javascript", "a few hours later", pnpm 11 `minimumReleaseAge` and `pull_request_target`. The npm registry shows the package created 2026-05-12T17:49:45Z and unpublished 2026-05-13T10:50:54Z, so the ~17 h conflict the log records is confirmed. |
| CI2026-080-014 | confirmed | Raw text has $500M Series F, $10B pre-money, GIC, Stripe second investment, Georgian and Salesforce Ventures, 600%, "More than 60%", "Nearly 10 million" and OrioleDB production-readiness "this year". `datePublished` 2026-06-04. |
| CI2026-080-015 | confirmed | `datePublished` 2026-06-04T16:09Z. Raw text has "$10.5 billion, including the fresh capital", "roughly doubled since … October", over 250,000 customers, 350 employees and the Claude Code / Codex attribution to Copplestone. |
| CI2026-080-017 | confirmed | GHSA API: CVE-2026-54238, low (CVSS 3.1 score 3.1), published 2026-06-16, affected <= 2.102.2, patched >= 2.103.1. |
| CI2026-080-018 | confirmed | GHSA API: CVE-2026-62247, medium (6.5), published 2026-06-25, affected <= 2.111.1, patched >= 2.111.2. The description matches (presence.write vs presence.read). |
| CI2026-080-020 | confirmed | Incident timestamps run from 2026-06-30T02:38:13Z to resolution at 2026-07-13T16:00:12Z. The page states capacity was "still … limited" in ap-northeast-2, ap-south-1 and eu-north-1. |
| CI2026-080-026 | confirmed | `datePublished` 2026-07-31. The page has Sonnet 5 78%→100%, GPT-5.6 Sol 89%→100% and "under 40% of scenarios". |
| CI2026-080-027 | confirmed | 56,974 pageviews / 90 days, 31% unhelpful, 26% of support tickets, and the finding that anon write grants remained. |
| CI2026-080-029 | confirmed | GHSA API: severity low, no CVE, published 2026-08-17, affected <= 2.128.2, patched 2.128.3. The body says "Severity: Medium, CVSS: 5.3", which confirms the recorded label conflict. |
| CI2026-080-032 | confirmed | Incident timestamps are 2026-09-16T07:17:12Z to 09:33:34Z, Auth partial outage. |
| CI2026-080-033 | confirmed | GHSA API: high (8.2), published 2026-09-24, affected <= 2.137.14, patched field empty. The reporter reproduced it on `supabase/realtime:v2.137.14`. |
| CI2026-080-034 | confirmed | `datePublished` 2026-09-24T14:47 -07:00. The displayed "Publish date October 14, 2026" matches `dateModified`. Raw text has ~300,000 domains, 16,326 databases, "Over half … PII" and the observation that programmatically created tables do not enable RLS by default. |
| CI2026-080-035 | confirmed | `datePublished` 2026-09-25T17:29Z. Raw text has "around 16,000", Bil Harmer, "secure by default" and shared responsibility. TechCrunch describes the ~16,000 as databases with "some degree of personal data" exposed, whereas UpGuard says over half had PII indicators. This is a framing difference between the sources, not a ledger error. |
| CI2026-080-036 | confirmed | Raw text has 15.19/17.11 from 15.14/17.6, five security cycles, 44 CVEs, CVE-2026-14663 and CVE-2026-2004. |
| CI2026-080-038 | confirmed | The changelog has beta18 on Postgres 17.11, no SLA, no PITR and "about 1.8x". The "up to 1.8x … dbarena.com" wording comes from the Select "scale without limits" post, as the row attributes. orioledb beta19 GitHub release is dated 2026-10-01T04:58Z. |
| CI2026-080-039 | confirmed | `datePublished` 2026-10-02. Raw text has "over one million databases per week" and "Glauber will lead this agentic infrastructure effort". |

**Counts:** 18 rows checked: 18 confirmed, 0 corrected, 0 wrong, 0 unverifiable.

**Robots.txt audit:** the search log fetched no path that robots.txt disallows for a generic User-Agent. supabase.com, cnbc.com, techcrunch.com (article path), upguard.com, mehmetince.net, turso.tech, blog.val.town and blog.simbastack.com are all allowed for the paths used. status.supabase.com, HN Algolia and the npm registry serve no robots.txt that restricts them.

The search log's statement that every number was string-confirmed held for every figure re-checked here.

*This is an AI-assisted spot-check, not qualified human review.*
