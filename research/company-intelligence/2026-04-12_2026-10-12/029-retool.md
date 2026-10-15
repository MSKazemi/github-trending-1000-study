# Retool — provisional six-month technology intelligence screen (029)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16), not human-reviewed.** This report, its [event ledger](029-retool.events.csv) and [search log](029-retool.search-log.md) were produced by an AI research assistant as **documentary source leads**. A qualified human has **not** reviewed them. Factual/link review, source-access/rights review and methods review are **pending**. This is not scientific sign-off and does not close [issue #96](https://github.com/MSKazemi/github-trending-1000-study/issues/96).

- **Company watchlist ID:** 029; research issue [#96](https://github.com/MSKazemi/github-trending-1000-study/issues/96); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see §2; legal entity and ownership **not verified to filing level**.
- **Product URL and channels:** [retool.com](https://retool.com/), [changelog](https://docs.retool.com/changelog), [blog](https://retool.com/blog), [community announcements](https://community.retool.com/), [GitHub org tryretool](https://github.com/tryretool). `retool.com/press` returned 404 on 2026-10-16. *Correction (2026-10-16 spot-check):* a first-party [newsroom](https://retool.com/newsroom) does exist and carries the 2026-06-17 press release.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; sources inspected 2026-10-16.
- **Researcher / factual reviewer / review date:** AI research assistant (single pass) / **pending** / **pending**.
- **Status:** screened (provisional). **25 dated ledger rows across all seven calendar segments, all first-party or vendor-issued.** No independent (non-vendor, non-syndicated) reporting was found for any month. Not an exhaustive search, not verified task outcomes.
- **Evidence grading:** company-watch E0–E4 from the [screening protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

The exact queries, surfaces and decisions are in the [search log](029-retool.search-log.md). In summary, the dated [docs changelog](https://docs.retool.com/changelog) was walked back across 14 index pages (to 2026-03-31). The [blog index](https://retool.com/blog) was screened, with 12 in-window posts. Web searches covered news, funding/security, partner and interview queries. The public `tryretool` GitHub org and the npm registry were queried directly. Search engines did not expose result totals, so found and excluded counts are **unknown, not zero**. Business Wire pages returned HTTP 403 and were not bypassed. Paywalled business press was not searched.

| Search run (date) | Site/engine | Query focus | Included | Coverage limitation |
|---|---|---|---:|---|
| 2026-10-16 | docs.retool.com changelog (direct) | full window, 14 index pages | 19 rows + cross-checks | Routine version and model notices excluded; summaries read via a fetch tool |
| 2026-10-16 | retool.com/blog (direct) | first index page | 4 rows | Older posts on later index pages not opened |
| 2026-10-16 | web search (11 queries) | news, funding, security, partners, interviews | 1 row (wire release, 403) | No result totals; name collisions (Roctool) |
| 2026-10-16 | GitHub API, npm registry | repos, releases, package metadata | 1 row + 1 cross-check + rights note | Repo contents not audited |

## 2. Verified company/product identity and baseline

- **Entity.** Retool sells a hosted and self-hosted platform for building internal applications, workflows (automations) and AI agents on top of a company's existing databases and APIs. Its [About page](https://retool.com/about) names **David Hsu as CEO** and claims "tens of thousands of companies" use Retool. That figure is a vendor claim, not adoption evidence. The fetched pages state **no legal entity name, headquarters, investors or parent company**. The site footer reads only "© Retool". No in-window acquisition, merger, rename, layoff or funding event was found (search-log Q06). **Ownership remains unverified to filing level.** Secondary aggregators describe it as privately held, but they are low quality and were not used.
- **Baseline (pre-window, context only).** Retool Agents were announced on 2025-05-28 ([Business Wire, 2025](https://www.businesswire.com/news/home/20250528644298/en/Retool-Automates-Over-100-Million-Hours-of-Work-Announces-Agents-to-Drive-More-Return-on-AI)). An AWS strategic collaboration agreement dates from 2025-12-01, and a "Build vs. Buy" survey release from 2026-02-17. None of these count as in-window events.
- **Brand change in window.** The drag-and-drop IDE is renamed **"classic apps"**. A new **AI app builder generates React apps** ([community post, 2026-06-17](https://community.retool.com/t/the-new-retool-app-builder-is-here/66848)). In a reply on that thread, a product-team member says classic apps will be supported for "at least two years" after the new builder reaches GA.
- **Open vs proprietary scope.** The platform is proprietary SaaS or licensed self-hosted software. Public GitHub repos are deployment tooling ([retool-helm](https://github.com/tryretool/retool-helm), MIT; Terraform modules) and agent-facing helpers ([skills](https://github.com/tryretool/skills), Apache-2.0). The new npm package `@tryretool/cli` declares **no license** in its registry metadata (checked 2026-10-16), so reuse rights are unclear.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes |
|---|---|---|---|---|
| 2026-04-12..30 | Agent skills repo (001); MCP server public beta for org/resource management (002); Workflows Python 3.10 EOL set for 2026-10-31 (003) | [skills](https://github.com/tryretool/skills), [mcp](https://docs.retool.com/changelog/mcp), [py3.10 EOL](https://docs.retool.com/changelog/python-3-10-end-of-life) | none found | ClickHouse beta and model additions screened and excluded as lower relevance |
| 2026-05 | **New AI app builder (React 19) beta** and **build apps via MCP** (004, 005; both 05-28) | [app-builder](https://docs.retool.com/changelog/app-builder), [mcp-app-building](https://docs.retool.com/changelog/mcp-app-building) | none found | Workflows analytics beta (05-13) excluded for brevity |
| 2026-06 | Source control for new apps (006); React app import from Replit/Lovable/Claude Code zips (007); self-hosted 4.0 requires Kubernetes+Helm (008); public launch press release (009) and vendor governance survey (010), both 06-17 | [source-control-apps](https://docs.retool.com/changelog/source-control-apps), [react-app-import](https://docs.retool.com/changelog/react-app-import), [4.0 stable](https://docs.retool.com/changelog/self-hosted-retool-40-stable), [Business Wire](https://www.businesswire.com/news/home/20260617017651/en/As-Vibe-Coding-Tops-C-suites-List-of-Concerns-Retool-Unveils-First-Platform-to-Extend-Enterprise-Governance-to-All-AI-Coded-Apps), [survey](https://retool.com/blog/ai-governance-report-2026) | none found (01net.it copy is syndication) | **Date conflict:** builder beta 05-28 vs public launch 06-17 |
| 2026-07 | MSSQL ODBC allowlist breaking security change (011); object permissions (012); AI model registry engineering post (013) | [odbc](https://docs.retool.com/changelog/mssql-windows-auth-odbc-allowlist), [object-permissions](https://docs.retool.com/changelog/object-permissions), [registry](https://retool.com/blog/ai-model-registry) | none found | — |
| 2026-08 | Org-wide agent context in Markdown (014); Postgres row/column access policies (015); plan mode (016); debug console (017); "up to 50% fewer credits" claim (018); Assist removal notice (08-18, cross-check of 023) | [building-context](https://docs.retool.com/changelog/building-context), [access-policies](https://docs.retool.com/changelog/access-policies), [plan-mode](https://docs.retool.com/changelog/plan-mode), [debug-console](https://docs.retool.com/changelog/debug-console), [app-agent-efficiency](https://docs.retool.com/changelog/app-agent-efficiency) | none found | — |
| 2026-09 | Retool CLI public beta (019); external MCP servers in the builder (020); MongoDB partnership plus scoped Atlas credentials (021); hardened images (022 group); Assist removed (023) | [CLI blog](https://retool.com/blog/retool-cli), [mcp-in-app-builder](https://docs.retool.com/changelog/mcp-in-app-builder), [MongoDB](https://retool.com/blog/retool-mongodb-partnership-atlas-security), [hardening](https://docs.retool.com/changelog/continued-hardening), [assist-removal](https://docs.retool.com/changelog/assist-removal) | none found; no MongoDB-side announcement found | The same day (09-30) also brought deprecations: Free-plan Retool Email from 2027-01-01, and custom-auth JS libraries and MSSQL Windows auth |
| 2026-10-01..12 | Agent creates Postgres/REST resources from a prompt (024); **centralized agent harness, early access** (025) | [nl-resources](https://docs.retool.com/changelog/natural-language-postgres-rest), [harness](https://retool.com/blog/introducing-agent-harness) | none found | Entries dated Oct 13–14 were excluded as out of window |

*Ledger IDs above are the last three digits of `CI2026-029-NNN`, in row order of the [CSV](029-retool.events.csv).*

## 4. Dated event evidence and capabilities (selected)

| Event ID | Published / event date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| CI2026-029-004 | 2026-05-28 / — | AI builder generates React 19 apps; Chat/Data/Code tabs; approval gates on writes; npm packages | beta; plan limits not stated | changelog (first-party) | [community post 06-17](https://community.retool.com/t/the-new-retool-app-builder-is-here/66848) (first-party) | E2 |
| CI2026-029-007 | 2026-06-03 / — | Import of React apps from other AI builders as .zip | public beta; backend handling not documented | changelog | none | E2 |
| CI2026-029-008 | 2026-06-11 / — | Self-hosted 4.0: Kubernetes+Helm is the only supported path; Compose is non-production only | stable | changelog | [retool-helm v6.11.0](https://github.com/tryretool/retool-helm/releases/tag/v6.11.0) (first-party repo) | E2 |
| CI2026-029-009 | 2026-06-17 / — | "First platform to extend enterprise governance to all AI-coded apps" | vendor says available; product team calls it beta | wire press release (403 on Business Wire; full text read from the [Retool newsroom copy](https://retool.com/newsroom/retool-extends-enterprise-governance-to-vibe-coded-apps) in the spot-check) | none | E1 |
| CI2026-029-010 | 2026-06-17 / fielded May 2026 | Survey of 307 tech/security leaders: 93% at least somewhat concerned; 19% report an incident from an AI-generated internal tool per the blog (the press release says 22%; see spot-check) | vendor-commissioned, non-probability; bases inconsistent | vendor survey | none | E1 |
| CI2026-029-011 | 2026-07-07 / — | ODBC parameter allowlist blocks connection-string attribute injection | self-hosted only; no CVE cited | changelog | none | E2 |
| CI2026-029-013 | 2026-07-30 / — | Versioned hosted model/pricing registry with fallback snapshot; append-only rate history | design write-up | engineering blog | none | E1 |
| CI2026-029-018 | 2026-08-25 / — | "Up to 50% fewer credits consumed" | no baseline or sample | changelog | none | E1 |
| CI2026-029-019 | 2026-09-24 / — | `@tryretool/cli`: local React app dev, offline `retool check`, push/preview/publish | public beta; paid cloud plans; **no license field on npm** | blog + changelog | [npm registry](https://registry.npmjs.org/@tryretool%2Fcli) metadata | E2 |
| CI2026-029-023 | 2026-09-30 / 2026-09-30 | Assist (classic-builder AI) beta ended and removed; limited access to 2026-12-31 | removed | changelog | [notice 08-18](https://docs.retool.com/changelog/upcoming-assist-removal) | E2 |
| CI2026-029-025 | 2026-10-06 / — | Per-employee agents in Slack/Teams/Google Chat behind a policy gateway; per-agent service accounts; audit; hosted sandbox; VPC option | early access via waitlist | CEO blog | [community post](https://community.retool.com/t/early-access-introducing-retool-s-centralized-agent-harness/67572) (first-party) | E1 |

See the CSV for all 25 rows. **No row reaches E3.** Every `independent_check_url` is either another first-party page or registry metadata. Such links give documentary corroboration, not independent behavioural verification.

**Feature inventory by theme (vendor-asserted unless noted):**
- **AI app generation and reuse paths:** app builder (004), MCP building (005), React import (007), CLI (019), agent-created resources (024). Several code paths now converge on one governed runtime.
- **Agent context and workflow:** org-wide Markdown instructions (014), plan mode (016), debug console with agent repair (017), message queueing and threads (screened, not in ledger).
- **Governance and security:** object permissions (012), Postgres access policies (015), ODBC allowlist (011), custom CSP (06-24, screened, not in ledger), hardened images (022), scoped MongoDB credentials (021), agent harness gateway (025).
- **Maintenance and churn signals (observed in the changelog):** Python 3.10 EOL (003); self-hosted move to Kubernetes-only (008); Assist removal (023); several Sep 30 deprecations; MSSQL integration v1/v2 retirement (07-28, excluded). These are documented costs that fall on adopters.
- **Licensing:** platform proprietary; helper repos MIT/Apache-2.0; CLI package license undeclared.

## 5. What the company says it intends to do

| Close paraphrase or short quote (≤25 words) | Link/date | Horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| MCP server: "actively adding additional tools", including app building | [changelog, 2026-04-23](https://docs.retool.com/changelog/mcp) | unspecified | **Delivered in part** on 05-28 (MCP app building) | Shows that a stated plan later shipped as beta |
| Classic apps supported "at least two years" after the new builder reaches GA | [community thread, from 2026-06-17](https://community.retool.com/t/the-new-retool-app-builder-is-here/66848) | GA + 2 years | planned (reply by product-team member) | GA date not announced; reply not separately dated in fetch |
| "Eventually, all images used by Retool will be hardened"; some libraries/features will lose support | [changelog, 2026-09-30](https://docs.retool.com/changelog/continued-hardening) | unspecified | tentative | No list of affected libraries or dates |
| CLI access for self-hosted customers in upcoming edge and stable releases | [blog, 2026-09-24](https://retool.com/blog/retool-cli) | "upcoming" | planned | — |
| Agent harness: "beginning to roll out access to the next hundred customers over the next few weeks" | [blog, 2026-10-06](https://retool.com/blog/introducing-agent-harness) | weeks | planned | Waitlist; no GA date |
| Model registry `tiers` field to be wired up "in v1.1 without a schema-version bump" | [blog, 2026-07-30](https://retool.com/blog/ai-model-registry) | unspecified | planned | Internal engineering intent |
| Free-plan Retool Email removed from 2027-01-01; Python 3.10 Workflows EOL 2026-10-31 | [email](https://docs.retool.com/changelog/retool-email-free-plan-deprecation), [py](https://docs.retool.com/changelog/python-3-10-end-of-life) | dated | announced | Effective after the window |

Executive commentary in the [WSJ Tech Council panel write-up (2026-09-29)](https://retool.com/blog/ai-roi-wsj-technology-summit) contains CEO estimates, for example that about 90% of tokens are "net negative". These are **unsourced personal estimates** and are not treated as evidence or as company commitments.

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher hypotheses, not company strategy)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Low-code vendors become **governed runtimes for code written elsewhere**, by AI builders, coding agents or humans, rather than visual editors | React import (007), MCP building (005), CLI (019); classic IDE renamed and its AI assistant retired (023) | Marketing repositioning around "vibe coding" with unchanged usage; import may be rarely used | Classic apps remain the dominant creation path in vendor or independent data; import/CLI stay beta or are withdrawn by 2028 | Low; no usage data |
| H2. **Central policy gateways for agents** (identity, tool-argument checks, audit) become a standard enterprise layer, separate from model choice | Agent harness (025), object permissions (012), access policies (015), the vendor survey's stated preference for centralized controls (010) | Identity providers, cloud IAM or model vendors absorb the layer; vendor survey framing biases the result | Independent audits show that gateway policies are bypassed or add no reduction in incidents; harness does not leave early access | Low–medium; one vendor, no independent tests |
| H3. AI-driven platforms **raise adopters' maintenance churn** through frequent deprecations, runtime moves and feature retirements | 003, 008, 023, Sep 30 deprecations, MSSQL v1/v2 retirement | Normal SaaS hygiene that reduces security debt (hardening 022, ODBC 011) | Measured migration hours per customer stay flat or fall; deprecation notices become less frequent | Medium for "churn exists" (documented); unknown for net cost |
| H4. Exportable plain React plus git **reduces lock-in** compared with the classic builder | React 19 apps, source control (006), local CLI (019) | Runtime-bound resources, permissions and functions keep apps non-portable; CLI license undeclared | An exported app cannot run outside Retool without substantial rewrite (testable) | Unknown |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Agent workflows move between in-product chat, MCP and CLI against a shared governed backend | Log opt-in task attempts by surface (chat/MCP/CLI) on frozen tasks | Surface choice has no effect on accepted outcomes | Vendor docs only; no traces |
| **M2** accepted task quality | Plan mode, debug console and approval gates may change first-pass acceptance | Hidden, independently authored acceptance tests; count all attempts | Gains reflect easier task selection | Credits ≠ quality |
| **M3** discoverability | Agent skills repo and CLI `skill install` make the product legible to coding agents | Compare agent success with and without skill files on the same task | Agents succeed equally from public docs | Repo stars not used |
| **M4** verified reuse | Import and export paths could enable reuse of externally generated apps | Trace one consented import→publish→export round trip | Imported apps get rewritten, so there is no real reuse | No customer data |
| **M5** reuse-first and rights/security | Reuses existing data connectors and permissions instead of re-implementing auth | Compare against a minimal self-built React app plus existing IdP/DB roles | Generic stack equally safe with less lock-in | CLI license undeclared; proprietary runtime |
| **M6** lifecycle human/energy cost | Deprecations and runtime migrations impose recurring work | Count adopter-facing breaking/deprecation notices per quarter; time actual migrations | Notices are rarely relevant to a given user | **No energy or CO2e inferred**; credits are billing units |
| **M7** actionable interventions | Org-wide agent instruction files (014) are analogous to `AGENTS.md` | See §8 | — | — |

Company adoption claims ("tens of thousands of companies", "millions of MongoDB queries weekly", "3x–5x token return") are **vendor assertions** and are not treated as verified adoption or outcomes.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The target is its offline validation CLIs (`python -m trending_study.value_gate`, `reuse_gate`, `scripts/check_research_artifacts.py`). This is **not** a proposal to adopt Retool. The idea transferred from Retool's August–September changes is **plan-before-edit plus a local, offline `check` command that agents must pass before submitting** (cf. plan mode, `retool check`, and org-wide agent context).

**Candidate practice (not yet validated):** a short, versioned "agent preflight" section in `AGENTS.md`. It would require (a) a written plan listing the files to be touched before editing, and (b) one documented offline command that runs the existing validators and the unit suite. The command is a thin wrapper that reuses the existing validators; nothing new is reimplemented.

**Treatment/control and frozen task:** Freeze 8 small synthetic tasks, for example "add one company ledger row with a deliberately out-of-window date" or "add a field to a synthetic fixture and update docs". Half of the tasks must include a planted violation that the existing validators should catch. **Control:** current `AGENTS.md`. **Treatment:** the same file plus the preflight section. Use the same agent and model version pinned per run, the same base commit and a fixed token/time budget. Assign task order randomly. Hidden acceptance checks are written by a human who does not author the treatment text.

**Accepted-task functional unit:** one task whose resulting diff (i) passes the hidden acceptance checks, (ii) passes `python -m unittest discover -s tests -v` and both research validators, and (iii) is accepted by a human reviewer without rework. Refused, timed-out and abandoned attempts stay in the denominator.

**Guardrails:** no network capture (the `capture` hard stop stays in force); no new dependencies; no secrets; no edits outside the task scope (diff path check). Any planted violation that reaches an accepted diff counts as a failure.

**Measured human work:** reviewer minutes per task (timed), rework rounds, and maintainer minutes to write and maintain the preflight section. Agent tokens and wall-clock are logged as reported by the tool and are **not converted to energy or CO2e**.

**Stop/reversal rule:** stop and keep the control if, after 8 paired tasks, the treatment shows no reduction in planted-violation escapes **and** no reduction in reviewer minutes. Also stop if the treatment raises refusal/timeout rate by 2 or more tasks, or if maintaining the section takes more than 30 minutes per month. A null result is recorded as such. **No trial has been run and no effect is estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (first-party documentary, E2):** the changelog documents a stream of features. These include a beta React app builder, MCP/CLI/import build paths, object and row-level permissions, an ODBC injection allowlist, and Kubernetes-only self-hosting from 4.0. They also include several deprecations and the removal of the Assist AI beta.
- **Claims/announcements only (E1):** the governance-platform "first" claim, the agent harness (early access), the "up to 50% fewer credits" claim, the MongoDB partnership (no MongoDB-side source found) and the vendor survey statistics.
- **Conjectures and unknowns:** ownership and legal entity; actual usage of any new path; portability of exported apps; CLI license; meaning of "RetoolOS" in [retool-helm v6.12.0](https://github.com/tryretool/retool-helm/releases/tag/v6.12.0); the role Snowflake's 2026-06-02 CoCo release gives Retool (not verified).
- **Contradictory or null evidence:** builder beta date 05-28 versus launch messaging 06-17; changelog pages edited after publication (they mention 4.0.21 stable from 10-08); internal inconsistency in survey bases (n=307 versus bases of 387–397; 51% versus 59% "unknown" figures, which both appear on the blog page itself, and 19% versus 22% reporting an incident between blog and press release). **No independent news coverage was found in any month.** This is a coverage gap, not evidence of absence.
- **Reviewer links and audit date:** none yet. Required before closure: a human factual/link spot check of at least the 9 directly opened changelog entries and all blog rows; a direct reading of the Business Wire release; a search of paywalled business press; a methods review of §8.

## Independent source spot-check (2026-10-16)

A second agent, who did not write this screen, re-fetched the cited sources on 2026-10-16. Pages were read as raw text: `curl -sL` for docs.retool.com, retool.com and the newsroom; the Discourse `/t/<id>.json` endpoint for the community thread; the npm registry JSON; and `gh api`. A model summary was not used for any figure. Pages were not archived.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (section 2) | confirmed, with one correction | The About page names "our CEO, David Hsu" and says "Tens of thousands of companies use Retool". The docs JSON-LD `Organization` record gives founding date 2017 and 1550 Bryant Street, San Francisco; this is vendor metadata, not a filing. **Correction:** `retool.com/newsroom` exists and lists the 2026-06-17 press release, so "no separate newsroom was found" was wrong and is annotated in the header |
| 001 | confirmed | `gh api repos/tryretool/skills`: created 2026-04-21T00:01Z, Apache-2.0, "Teaching agents how to use Retool" |
| 002 | confirmed | Apr 23 entry: MCP server in public beta; tools manage the org and users, write queries and inspect resource config. App building is listed as a future addition. The 4.0.21 Stable badge is present, consistent with a later edit |
| 003 | confirmed | "Python 3.10 will reach end of life on October 31, 2026"; workflows "will not be automatically migrated" |
| 004 | corrected | The May 28 entry says the builder "is now available", lists React 19 and the Chat/Data/Code tabs with "optional approval gates on writes", and does **not** say beta. The beta label comes from a Retool Team reply on 2026-06-23 ("currently a beta product"), and the same thread confirms the classic-app support of "at least two years after ... GA". The CSV availability was re-attributed |
| 008 | confirmed, detail added | "Kubernetes with Helm is the only supported deployment path for Retool 4.0"; "does not support Docker Compose for production". The entry requires Helm chart **6.11.4 or later** (v6.11.4 was published 2026-06-15). The cited v6.11.0 (2026-06-11) corroborates timing only; this was noted in the CSV |
| 009 | corrected (upgraded from snippet-only) | Business Wire still returns 403. The full release was read on the [Retool newsroom](https://retool.com/newsroom/retool-extends-enterprise-governance-to-vibe-coded-apps) (06.17.2026, `publishDate` 2026-06-17). The named tools and the "first platform" headline are confirmed. The confidence label changed from `E1_SEARCH_SNIPPET_ONLY` to `E1_VENDOR_PRESS_RELEASE`; the evidence is still vendor-only |
| 010 | corrected | The blog (`datePublished` 2026-06-17) confirms 307 respondents, Wynter, May 2026, 93%, "Cross-tabs are directional", and chart bases of 397 and 387. The 51% versus 59% conflict is **within the blog itself** ("almost half of respondents (59%)" and "51% ... can't say for certain"), not between press and blog as the CSV said. The press release gives **22%** with at least one incident, where the blog gives 19%; it uses 19% for those who "could definitively say they haven't had an incident"; and it describes "300 C-suite executives". Limitation rewritten; the section 4 and section 9 text was annotated |
| 018 | confirmed | "These improvements can result in up to 50% fewer credits consumed" (2026-08-25) |
| 019 | confirmed, detail added | `datePublished` 2026-09-24; "public beta for cloud customers on team, business, and enterprise plans"; `retool check` validates offline. npm `@tryretool/cli`: latest 0.1.10, with no `license` or `repository` field. The package was created 2026-07-28, which was added to the CSV |
| 021 | confirmed | `datePublished` 2026-09-30: "millions of MongoDB queries every week", read-only or read-write scoped users, "No human ever sees the password"; cloud-hosted only |
| 023 | confirmed | Sep 30: Assist public beta concluded; "Certain customers retained access until December 31, 2026" |
| 025 | confirmed | David Hsu, `datePublished` 2026-10-06; "running this internally at Retool for the last 4 months"; waitlist / early access. The headline says "first centralized agent harness". The article body does not mention MCP; the only "mcp" string is in site navigation |

**Totals:** 12 ledger rows (001, 002, 003, 004, 008, 009, 010, 018, 019, 021, 023, 025) and the entity claim were checked. Outcome: 7 confirmed (001, 002, 003, 018, 021, 023, 025), 2 confirmed with detail added (008, 019), 3 corrected (004, 009, 010), and 1 correction to the identity/newsroom statement. No fabricated URL or figure was found and no row was removed. The survey-figure conflict (row 010) is a vendor inconsistency, not an extraction error. It should be read by a human before any figure is reused.

*This is an AI-assisted source spot-check, not qualified human factual, rights or methods review. Every pending gate above still applies.*
