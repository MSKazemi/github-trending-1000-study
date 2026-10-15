# Retool (029) — provisional dated source-query and inclusion audit, 2026-10-16

> **PROVISIONAL, AI-assisted first-pass source screen (2026-10-16).** This log, the [report](029-retool.md) and the [event ledger](029-retool.events.csv) were produced by an AI research assistant and have **not been reviewed by a qualified human**. Factual/link review, source-access/rights review and methods review are **pending**. Nothing here closes [issue #96](https://github.com/MSKazemi/github-trending-1000-study/issues/96).

**Window:** 2026-04-12…2026-10-12 inclusive. **Research/source inspection:** 2026-10-16 (single session). **Tools:** a public web-search tool (provider ranking and result totals not exposed), a page-fetch tool that returns model-summarised page text (not raw bytes), `curl` HTTP status checks, the GitHub REST API (`gh api`) for the public `tryretool` org, and the public npm registry JSON for `@tryretool/cli`. **Search result totals, query-run UTC times, ranks and complete excluded-hit denominators are unavailable, not zero.** No page snapshots or byte hashes were archived.

**Important provenance caveat.** Page contents were read through a fetch tool that summarises pages with a small language model. Titles, dates and labels were cross-checked between the changelog index pages and individual entry pages for the items listed under "spot-checked" below, and every cited URL returned HTTP 200 on 2026-10-16 (a deliberately bogus slug returned 404 on both `docs.retool.com/changelog/` and `retool.com/blog/`, so 200 is not a soft-404). Wording-level accuracy of summaries still needs a human spot check.

## Query log

| # | Date screened | Segment | Exact query / surface | Pages opened and decision | Found / screened / excluded |
|---|---|---|---|---|---|
| Q01 | 2026-10-16 | all | web search: `Retool 2026 announcement AI agents` | Only 2025 Agents launch and an undated sponsor blurb surfaced; **excluded** (pre-window / undated) | unknown |
| Q02 | 2026-10-16 | all | direct: `https://docs.retool.com/changelog` and `/changelog/page/2` … `/page/14` (14 index pages walked back to 2026-03-31) | Primary chronology source. ~130 entries screened; routine "Self-hosted … stable updates", per-version Edge releases and model-availability notices were **excluded as routine** (counted below). 22 changelog entries became ledger rows or cross-check URLs | about 130 in-window entries listed (13 full index pages of 10 plus 3 entries on page 14) / all titles screened / exclusions not exactly counted |
| Q03 | 2026-10-16 | May–Jun | web search: `Retool new app builder React AI launch 2026` | [Changelog app-builder](https://docs.retool.com/changelog/app-builder) (included), [community launch post, Jun 17](https://community.retool.com/t/the-new-retool-app-builder-is-here/66848) (cross-check), Retool video/event pages (undated; excluded), Product Hunt pages (not opened; excluded) | unknown |
| Q04 | 2026-10-16 | all | web search: `Retool TechCrunch 2026` | No TechCrunch article about Retool found; low-quality aggregator profile excluded | unknown |
| Q05 | 2026-10-16 | all | direct: `https://retool.com/blog` (first index page, 12 posts, all in window) | Included: agent harness (Oct 6), MongoDB (Sep 30), CLI (Sep 24), model registry (Jul 30), governance report (Jun 17). Read but used only as narrative/context: WSJ summit post (Sep 29), "prompt to production" (Jun 17). Not opened: Sep 24 MCP-vs-CLI, Sep 2 multi-agent governance, Aug 20 AI-cost survey, Aug 11 governance questions, Jun 24 "building safely" (opinion/marketing; not new capabilities) | 12 / 12 / 5 included |
| Q06 | 2026-10-16 | all | web search: `"Retool" funding OR acquisition OR layoffs OR security incident 2026` | No in-window funding, acquisition, layoff or breach report found. A third-party status tracker (pingoru.io) reported a ~3h40m page-not-found incident on 2026-05-20; **excluded** (third-party aggregator, not opened) | unknown |
| Q07 | 2026-10-16 | Oct | web search: `Retool agent harness Slack Teams enterprise agents October 2026` | [Community early-access post, Oct 6](https://community.retool.com/t/early-access-introducing-retool-s-centralized-agent-harness/67572) used as cross-check; Slack/MindStudio/Runbear results unrelated to Retool's launch, excluded | unknown |
| Q08 | 2026-10-16 | Sep | web search: `MongoDB Retool partnership Atlas credentials September 2026` | **No MongoDB-side announcement found**; only third-party integration guides. Partnership therefore rests on Retool's own post | unknown |
| Q09 | 2026-10-16 | Jun | web search: `Retool "State of AI Governance" 2026 report survey` | Returned similarly named Schellman and AvePoint reports (different publishers; **excluded**, do not conflate) | unknown |
| Q10 | 2026-10-16 | all | web search: `Retool David Hsu interview 2026 AI apps enterprise` | ceointerviews.ai summaries (AI-assisted third-party summaries; date 2026-04-01 is pre-window) **excluded**; Retool event page undated, excluded | unknown |
| Q11 | 2026-10-16 | Jun | web search: `"Retool" new app builder review vibe coding enterprise governance news` | Surfaced the [Business Wire release, Jun 17](https://www.businesswire.com/news/home/20260617017651/en/As-Vibe-Coding-Tops-C-suites-List-of-Concerns-Retool-Unveils-First-Platform-to-Extend-Enterprise-Governance-to-All-AI-Coded-Apps) (included as E1 search-snippet-only, **fetch returned HTTP 403**) and an 01net.it copy (syndication; not independent). No hands-on independent review found | unknown |
| Q12 | 2026-10-16 | Jun | web search: `Retool June 2026 launch governance AI-coded apps Lovable Replit import SiliconANGLE OR VentureBeat OR InfoWorld OR "The New Stack"` | No coverage from named outlets; competitor/comparison blogs excluded | unknown |
| Q13 | 2026-10-16 | Jul–Sep | web search: `Retool news September 2026 OR August 2026 OR July 2026` | Only name collisions (Roctool, unrelated). **No independent Retool news found for Jul–Sep** | unknown |
| Q14 | 2026-10-16 | all | web search: `"Retool" announces 2026` | Name collisions only; excluded | unknown |
| Q15 | 2026-10-16 | all | web search restricted to businesswire.com: `businesswire Retool 2026` | In-window: Jun 17 governance launch (included), **Jun 8 "Retool Achieves AWS Consumer Goods Competency"** (search result only; not fetched; excluded as partner-program badge, not capability), **Jun 2 Snowflake CoCo release naming Retool as an integration partner** (fetch 403; see Q16). Pre-window: Feb 17 Build-vs-Buy report, Dec 1 2025 AWS SCA, May 28 2025 Agents — excluded | unknown |
| Q16 | 2026-10-16 | Jun | web search: `Snowflake CoCo coding agent Retool integration June 2026`; opened The New Stack, Snowflake (DE) blog, IT Brief | None of the opened pages mentioned Retool (The New Stack body truncated). Retool's role in the Snowflake announcement is **unverified; excluded from ledger** | unknown |
| Q17 | 2026-10-16 | Apr–Oct | GitHub API: `orgs/tryretool/repos` (sorted by push) and `repos/tryretool/{retool-helm,retool-cli,skills,agent-plugins}` releases/metadata | Included: [tryretool/skills](https://github.com/tryretool/skills) created 2026-04-21 (Apache-2.0). Cross-check: [retool-helm v6.11.0](https://github.com/tryretool/retool-helm/releases/tag/v6.11.0) (2026-06-11, "R² (React Retool) self-hosted support"). Noted not included: retool-helm v6.12.0 (2026-09-30, "Helm chart changes for RetoolOS" — meaning of RetoolOS not established), agent-plugins repo created 2026-07-31 (no description/license). `tryretool/retool-cli` was created 2023 and has no releases — it is **not** the new `@tryretool/cli` | n/a |
| Q18 | 2026-10-16 | Sep | npm registry: `https://registry.npmjs.org/@tryretool%2Fcli` | Package created 2026-07-28; latest 0.1.10 (2026-09-24); **no `license` or `repository` field**. Recorded as a rights limitation on the CLI row | n/a |
| Q19 | 2026-10-16 | identity | direct: `retool.com/about`, `retool.com/press` (404), `retool.com/legal` (404), homepage footer | About page names David Hsu as CEO and claims "Tens of thousands of companies"; legal entity name, HQ, ownership and funding **not stated** on fetched pages. Footer shows "© Retool" only | n/a |

### Spot-checked individual entries (opened directly, not only via index)

`app-builder`, `mcp`, `natural-language-postgres-rest`, `self-hosted-retool-40-stable`, `assist-removal`, `react-app-import`, `mssql-windows-auth-odbc-allowlist`, `app-agent-efficiency`, `continued-hardening` (all under `https://docs.retool.com/changelog/`). The remaining ledger changelog rows rely on the index-page summaries plus a 200 status check.

## Month-segment outcome

| Segment | First-party dated events found | Independent reporting found |
|---|---|---|
| Apr 12–30 | Yes (3 ledger rows: skills repo, MCP server beta, Python 3.10 EOL notice); also ClickHouse beta, Gemini/GPT model additions (excluded as routine) | **None found** |
| May | Yes (2 rows: new app builder beta, MCP app building, both May 28); also Workflows analytics beta May 13 (excluded for brevity) | **None found** |
| June | Yes (5 rows) | **None found** (Business Wire is a vendor-issued wire release; 01net.it is syndication) |
| July | Yes (3 rows) | **None found** |
| August | Yes (6 rows) | **None found** |
| September | Yes (4 rows) | **None found** |
| Oct 1–12 | Yes (2 rows) | **None found** |

No calendar segment lacked first-party findings. **Every segment lacked independent (non-vendor, non-syndicated) reporting in the searches run.** That absence is a search-coverage observation, not evidence that no independent coverage exists (paywalled outlets such as The Information, Bloomberg and WSJ were not searched directly).

## Inclusion, exclusion and data validity decisions

- **Included = 25 ledger rows.** Each row is one dated vendor record; some share a `duplicate_event_group` (`029-mcp` spans three rows: MCP server, MCP app building, external MCPs in builder; `029-launch` joins the Jun 17 wire release and the Jun 17 survey report).
- **Date conflict recorded, not resolved:** the new app builder appears in the changelog on **2026-05-28** (beta) while the community launch post and the Business Wire release are dated **2026-06-17**. Treated as a staged beta → public launch, with two separate rows.
- **Post-publication edits detected:** the Apr 23 `mcp` and Jun 3 `react-app-import` entries reference self-hosted Stable 4.0.21, which the changelog dates to 2026-10-08. The pages were therefore edited after first publication; no original snapshot is available.
- **Excluded as routine:** self-hosted Stable/Edge version notices (roughly half of all in-window entries; not exactly counted) and "model X available in Retool" notices. They show release cadence but not new reusable capability; model-name strings were not independently verified.
- **Excluded as out-of-window:** 2025 Retool Agents launch, Feb 2026 Build-vs-Buy report, Dec 2025 AWS agreement, Oct 13–14 changelog entries.
- **Survey inconsistency flagged:** the fetched blog summary reports n=307 but chart bases of 387–397, and an "unknown incident" share of 51% versus 59% in a search-result summary of the press release. Needs human reading of the original pages.
- **Access:** public pages only; no account, paywall, private forum, product trial, or customer data accessed. Business Wire pages returned 403 to the fetch tool and were not bypassed.

A future independent reviewer should re-run these queries, record result totals and UTC timestamps, open each changelog row directly, archive snapshots, and search paywalled business press before any issue closure.
