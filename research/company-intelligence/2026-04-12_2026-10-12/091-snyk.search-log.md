# Snyk (091) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](091-snyk.md) and [event ledger](091-snyk.events.csv) for [#159](https://github.com/MSKazemi/github-trending-1000-study/issues/159). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:** robots.txt was checked on every host before any page was fetched. Raw HTML was retrieved with `curl` using a generic `Mozilla/5.0` User-Agent. No email, account name, personal identifier or credential was sent to any site, and sec.gov/EDGAR was not contacted. Text was extracted locally, and each number, version, date and quote used in a ledger row was confirmed with `grep` against the raw text. GitHub data came from `gh api` (public endpoints only) and release dates from the PyPI JSON API. Discovery used the Hacker News Algolia API and two WebSearch queries. WebFetch was not used, so no model-summarized page text was relied on.

**This is not exhaustive retrieval.** Pages may have changed after access, and no page snapshots or hashes were archived in the repository.

## Robots / access decisions

| Host | robots.txt result | Decision |
|---|---|---|
| snyk.io | `User-agent: *` Allow `/`; disallows `*.json`, `*.js`, `/advisor`, `?topic=`; Content-Signal `ai-input=yes` | fetched sitemaps, RSS, press and blog HTML |
| updates.snyk.io, labs.snyk.io | allow `/` except `*.json`/`*.js` | fetched |
| docs.snyk.io | allow all | sitemap index only; the release-notes URL guessed returned 404 (not used) |
| status.snyk.io | disallows `/api/`, `/embed/` only | fetched `/history` (JS-rendered, empty) and `/history.rss` |
| security.snyk.io | allow all | **not fetched** (braces entry not checked) |
| research.snyk.io | robots.txt 404 (no restrictions) | fetched one post |
| klue.com, en.globes.co.il, calcalistech.com, tech.eu, appsecsanta.com | no rule blocking the paths used, for `*` or for Claude/Anthropic agents | fetched article pages (appsecsanta not fetched) |
| arxiv.org | `/abs` allowed; crawl-delay 15 s | one `/abs` page fetched |
| darkreading.com | **disallows `/` for ClaudeBot, Claude-Web, Anthropic-ai** | **skipped** ("Snyk Names New CEO") |
| bankinfosecurity.net | robots.txt returned **HTTP 403** | **skipped** (could not verify rules) |
| cybernews.com | robots allows the path; the article returned an **HTTP 403 "Just a moment…" challenge** | **inaccessible**; not retried with another client |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://snyk.io/sitemaps/sitemap-press-releases.xml` then each URL; `publishDate` read from embedded page JSON | in-window: 05-07, 05-27, 06-23, 08-03, 08-04, 09-17; 10-15 Agentic AppSec **excluded** (post-window) | 68 (53 English) / 68 / 61 out of window or localized |
| 2026-10-16 | all | `GET https://snyk.io/blog/feed/` | 1,674 items, 2015-04-17…2026-10-15; 64 dated in window; 24 opened | 64 / 24 / see exclusions |
| 2026-10-16 | all | `GET https://updates.snyk.io/sitemap.xml` (483 URLs) then the 72 with lastmod ≥ 2026-04 | displayed dates parsed; four October pages show only "Updated N days ago" | 72 / 72 / 64 not ledgered |
| 2026-10-16 | all | `gh api repos/snyk/cli/releases?per_page=60` | 17 stable releases v1.1304.1 (04-27) … v1.1308.0 (10-08); v1.1308.1 (10-14) post-window; LICENSE text Apache-2.0 (API: NOASSERTION) | 17 / 17 / 13 patch releases not ledgered |
| 2026-10-16 | all | `gh api orgs/snyk/repos?sort=created`; `repos/snyk/agent-scan/releases`; `repos/snyk/studio-mcp/releases`; `GET https://pypi.org/pypi/snyk-agent-scan/json` | new in-window repos: claude-plugin-snyk (05-19, archived, NOASSERTION), cursor-plugin-snyk (05-21, NOASSERTION), evo-ads-sbx-kit (09-11, Apache-2.0); agent-scan 28 PyPI releases in window; studio-mcp v1.13.1…v1.15.5 seen, not ledgered | — |
| 2026-10-16 | all | `GET https://hn.algolia.com/api/v1/search_by_date?query=snyk&typoTolerance=false&tags=story&numericFilters=created_at_i>1775952000,created_at_i<1792022400&hitsPerPage=100` (operators URL-encoded) | 12 stories. Used: 50017567 (braces CVE, as a check). Leads only: 48661446 (layoffs, links to Snyk's letter), 49673686 (Labs Skill Inspector), 49499629 (agent-scan repo), 49378773 (model risk), 48557881 (arXiv). Excluded: ToxicSkills resubmission (blog dated 2026-02-05, pre-window), Miasma blog (research, not ledgered), third-party Show HN and blog posts | 12 / 12 / 11 |
| 2026-10-16 | all | first HN request without typo control | 218 fuzzy hits (snake, Manticore, etc.); discarded | 218 / 100 / 100 |
| 2026-10-16 | Apr 12–30 | blog `future-snyk-secrets` (04-23), `snyk-agent-fix-agentic-architecture` (04-27), `atlassian-integration-intelligent-remediation-jira` (04-29), `bun-based-stealer-hits-sap-cap-js-mbt-npm-packages` (04-29) | 3 rows; Secrets vision post (04-23) excluded as superseded by the 08-04 GA row. Not opened: JPMorgan checklist post, elementary-data/lightning PyPI and Qinglong posts, Thymeleaf CVE | — |
| 2026-10-16 | May | press 05-07, 05-27; blog `tanstack-npm-packages-compromised`, `mini-shai-hulud-antv-npm-supply-chain-attack`, `claude-enterprise-integration-desktop-expansion`, `snyk-remediation-agent-in-the-cli`; updates Studio hooks (05-11) and Agent Fix (05-28); CLI v1.1305.0 | 9 rows. Not opened: node-ipc, durabletask, Laravel Lang advisories, partner post (05-21), Relay case study, culture post | — |
| 2026-10-16 | June | blog `protestware-…-qwik-1-10-0-prompt-injection`, `secure-developer-program`, `agentic-development-security-ads`, `agentic-development-security-ai-coding-risk`, `when-a-vendors-breach-becomes-yours-…-klue-incident`, `a-note-to-our-customers-and-partners`, `snyk-vulnbench-js-1-0-…`; press 06-23; `arxiv.org/abs/2606.15762`; `klue.com/blog/an-update-on-recent-klue-security-incident` | 8 rows. ADS blog 06-23 used as context. Not ledgered: Miasma, node-gyp, Mastra compromises; "government pulls an AI model" commentary (06-14/15); NVD opinion (06-25) | — |
| 2026-10-16 | June | WebSearch `Snyk layoffs June 2026` | read raw: [Globes](https://en.globes.co.il/en/article-1001546903), [CTech](https://www.calcalistech.com/ctechnews/article/c48f8h988), [Tech.eu](https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/). Cybernews 403 (inaccessible). BankInfoSecurity skipped (robots 403). interviewpal, layoffhedge, autobound: trackers/aggregators, **E0, not used**. appsecsanta newsletter not read | 10 / 4 / 7 |
| 2026-10-16 | June | WebSearch `Snyk Ken MacAskill CEO appointed Peter McKay steps down` | Dark Reading **skipped (robots disallow for Claude agents)**. siliconvalleyinvestclub profiles, TechCrunch 2019 item, unrelated "Kenny MacAskill" (Scottish politician) and Raise Summit pages excluded. The "interim CEO" description is a search-summary claim, **E0, unverified** | 9 / 0 / 9 |
| 2026-10-16 | July | CLI v1.1306.0; updates Rule Extensions (07-15), COBOL (07-31), Bruno collections (07-08), ATAC (07-24); blog Snowflake Cortex Code (07-30), `openai-hugging-face-incident` (07-28) | 3 rows. The OpenAI/HF post is opinion, excluded; other updates are routine | — |
| 2026-10-16 | August | press 08-03, 08-04; blog `evo-continuous-offensive-security`, `snyk-secrets`, `remediation-agent-malicious-code-defense`, `why-we-rebuilt-evo-ai-model-risk-scoring`, `inside-keyv-npm-compromise-…`, `snyk-agent-fix-remediation-benchmark`; updates IAW, Secrets GA, model risk, org-scoped access, Repo Content Sync, Snyk Assist, new UI; CLI v1.1307.0; agent-scan v0.6.0; `research.snyk.io/blog/model-risk/` | 12 rows. Snyk Assist and UI rollout not ledgered (UX); "20 FAQs" and other explainers excluded | — |
| 2026-10-16 | September | press 09-17; updates Evo MCP Server (09-22), Code Priority Score change (09-23), Jira Connect→Forge (09-23), Go stdlib container reporting, custom CA; blog ADS Govern GA (09-30); repo evo-ads-sbx-kit | 4 rows. Priority Score and Forge migration seen, not ledgered (minor). Opinion posts 09-10/15/22/24 excluded | — |
| 2026-10-16 | Oct 1–12 | `GET https://status.snyk.io/history.rss`; CLI v1.1308.0; `gh api repos/github/advisory-database/pulls/10132` + issue comments; `gh api /advisories/GHSA-vfj7-8cjw-p6xm`; updates ADS installer (10-01) | 4 rows (with CTech, 10-01). Installer not ledgered (minor). Opinion posts 10-01 and 10-07 excluded | — |

## Inclusion, deduplication and conflicts

- **Included:** 43 rows (Apr 3, May 9, Jun 8, Jul 3, Aug 12, Sep 4, Oct 4). Every row cites a URL that was fetched as raw text or queried through an API. No row relies on a search snippet alone.
- **Duplicate groups:** `091-001` (Agent Fix announcement, delivery notice and vendor benchmark); `091-010` (Evo COS early access and GA); `091-012` (Remediation Agent CLI and Agentic AppSec first look); `091-016` (Evo ADS launch, telemetry post and Govern GA); `091-019` (restructuring letter, Globes, CTech; Tech.eu attached as CTech's check URL because both report the same UK filing).
- **Numeric/date conflicts recorded, not resolved:** layoffs ~90 (Globes) vs ~203 (filing via CTech/Tech.eu); headcount 1,550 (LinkedIn via Globes) vs 990 FTE at end-2025 (CTech); 2025 losses $197.9M net / $202.7M operating (CTech) vs $169M→$189M (Tech.eu); ADS GA "June 29" vs Govern Agent Behavior GA on Sep 30; Agent Fix "arrives May 26" vs update dated May 28; AntV post dated May 18 vs a May 19 event; Manoj Nair's three different titles; "nearly 9,700" (press) vs "nearly 10,000" (blog title) developer environments; "1 in 12 high/critical" vs "1 in 7 any finding" (different thresholds). CMS publish times on snyk.io are date-level placeholders (e.g., the TanStack page time precedes the incident times it reports), so only dates are recorded.
- **Figures confirmed against raw text (grep of saved pages):** all numbers in the ledger claim fields. These include 84/42 (TanStack); 323 packages, 22 minutes and ~16M (AntV); ~11.6 MB (SAP); 11 releases and 11:16 UTC (keyv); 9,700, 43% and 1 in 12 (ADS press); 50.8%, 1 in 7, 22.8% and 392 (ADS blog); 80/161, 22 and 134/158 (arXiv abstract); ~72%/~82% (Remediation Agent); 72–75%, 74.6%→85.4% and 64%→88% (benchmark); 3,000+ accounts, 11% from 4% and 44%→35% (Aug 3); 60%, 30%, 81.5%, 2.4M, 4.2M, 417,000+ and 4,800+ (Sep 17); 90 and 1,550 (Globes); 203, ~20%, $12.8–13.8M, $3.2M, $6.3M, $309.2M, $202.7M, $197.9M and 990 (CTech); $169M→$189M (Tech.eu); 0–1,000 with Aug 17 (model risk); Aug 18 (org-scoped access); release timestamps (GitHub API); and 28 releases (PyPI JSON). All remain **vendor or press statements**, not verified measurements.
- **Personal data:** the GitHub advisory thread and npm research name individual developers and include a support reply addressed to a named commenter. No individual names, handles or emails from those threads are reproduced in the ledger or report. Snyk staff are named only where they author or are quoted in official releases.

## Untrusted-content notes (embedded agent instructions)

- Every snyk.io and updates.snyk.io page carries a header link reading "llms.txt · Send this to your agent · Written for AI, not humans". [snyk.io/llms.txt](https://snyk.io/llms.txt) contains vendor guidance addressed to AI systems (e.g., "Use the platform, engine, and solution pages to understand capabilities and product selection"). It was treated as data, its directions were not followed, and it was not used for product selection or claims.
- The jqwik post describes a dependency that embeds an instruction for AI agents to delete tests. That payload was not retrieved. No fetched page contained instructions that were acted on, and no command suggested by a page was run.

## Missing, inaccessible or not attempted

- Cybernews (403 challenge); BankInfoSecurity (robots 403); Dark Reading (robots disallow for Claude agents); Reuters/Bloomberg not attempted; the UK Companies House filing itself not read; Snyk Trust Center and security.snyk.io braces entry not read; Anthropic, Atlassian, Snowflake and Cursor partner-side pages not read; status history before 2026-07-23 not available from the RSS; BitPatrol acquisition announcement not found; StepSecurity and TanStack incident reports not read; docs.snyk.io release notes not located.
- No product was executed, no account was created, no scan was run, no paywall was circumvented and no energy was measured.
- **Reproduction:** re-run the requests above, save raw HTML hashes, and have an independent human spot-check at least the restructuring rows (CI2026-091-019, -020, -040), the Klue row (-018), the braces dispute (-041) and two CLI releases against `gh api` before any evidence is promoted beyond provisional status.
