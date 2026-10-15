# Linear (036): search and inclusion log (provisional first pass)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (2026-10-16).** This log belongs to the [036 report](036-linear.md) and [event ledger](036-linear.events.csv) for issue [#103](https://github.com/MSKazemi/github-trending-1000-study/issues/103). An AI assistant ran these searches and fetches on **2026-10-16** (exact UTC run times not recorded) using a public web-search tool and a page-fetch tool that summarises pages with a small model. Selected exact strings were re-checked against raw HTML downloaded with `curl`. **This is not exhaustive internet discovery.** The search tool exposes no total hit counts, stable rankings or per-query result exports, so the found, screened and excluded counts below are **unknown, not zero**. No archived snapshots or byte hashes were stored. Pages may have changed after the window.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Accessed:** 2026-10-16.

## A. Direct primary-source inspection (not search-engine dependent)

| ID | Surface | What was read | Outcome |
|---|---|---|---|
| P01 | [linear.app/changelog](https://linear.app/changelog), [page 2](https://linear.app/changelog/page/2), [page 3](https://linear.app/changelog/page/3) | Index of all entries Dec 2025 to Oct 8, 2026 | 19 in-window entries found (Apr 16 to Oct 8). All 19 opened individually; 18 are ledger rows (Jun 4 "Team documents" was read but not given a row; see section D) |
| P02 | Individual changelog entries | Main feature plus "fixes and improvements" for GitHub, GitLab, API, MCP, agents and security | Model names (GPT-5.6 Luna, Claude Sonnet 5.5, GLM), the $0.25 per 20-minute price, the "roughly 30%" claim and displayed dates for the Diffs and Loops-for-PM entries were re-checked in raw HTML |
| P03 | [linear.app/now](https://linear.app/now) index | Posts and customer stories Apr to Oct 2026 | Used to date the undated pages /data (Aug 17) and /customers/ramp (Aug 31). The index shows **Sep 10** for "Loops for product management", while the entry page shows **Sep 14** |
| P04 | Now posts | [Code Intelligence May 14](https://linear.app/now/code-intelligence-for-linear-agent), [coding sessions Jun 11](https://linear.app/now/coding-sessions-for-linear-agent), [bug auto-fix Jun 12](https://linear.app/now/linear-agent-bug-fix), [How we built Linear Agent Aug 10](https://linear.app/now/how-we-built-linear-agent), [tender Aug 26](https://linear.app/now/sharing-growth-with-the-people-building-linear), [CI rework Sep 21](https://linear.app/now/ci-bottleneck-reworked), [Ramp story](https://linear.app/customers/ramp), [/data report](https://linear.app/data) | Six are E1 ledger rows (Jun 11, Aug 10, Aug 17, Aug 26, Aug 31, Sep 21). The May 14 post is used only as an `independent_check_url` (same company). The Jun 12 post was read but not given a row (see D) |
| P05 | GitHub API `repos/linear/linear/releases` (via `gh api`) | All releases with `published_at` in the window | 48 releases: `@linear/sdk` 82.0.0 (2026-04-18) to 97.1.0 (2026-10-07), with matching `@linear/import` releases. Release bodies read for 82.0.0 and 97.0.0. The repo licence reported by the API is MIT. One ledger row (97.0.0 ESM-only); cadence summarised in the report |
| P06 | [linear.app/terms](https://linear.app/terms) | Legal entity | "Linear Orbit, Inc."; effective date shown 2026-06-09. Not given a row: an effective date is not a publication date |
| P07 | [linearstatus.com](https://linearstatus.com/) | Incident history | Only current status and Jul to Oct uptime were visible. `/history` returned 404. No dated incident list was available from the official page |
| P08 | [linear.app/now/linear-incident-on-mar-24th-2026](https://linear.app/now/linear-incident-on-mar-24th-2026) | Security post-mortem | Published **Apr 6, 2026** (pre-window). Used as baseline context only |

## B. Web search queries (exact strings as issued)

| ID | Segment | Exact query | Pages opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| Q01 | all / funding | `Linear app 2026 news coding agent funding` | [Accel Aug 26](https://accel.com/news/our-investment-in-linear-the-digital-connectivity-between-engineers-and-agents) opened (investor statement, used as `independent_check_url` with caveat). Aggregators (stockanalysis, multiples.vc, pitchbook, vcbacked) excluded as unsourced | unknown |
| Q02 | identity | `"Linear" issue tracker "Linear Orbit" company` | Directory sites (craft.co, yourstory and others) excluded. Entity confirmed instead from [terms](https://linear.app/terms) | unknown |
| Q03 | Aug | `Linear employee tender offer $2.5 billion valuation Accel 2026` | [Linear post](https://linear.app/now/sharing-growth-with-the-people-building-linear) opened and included. pulse2.com, dealroom and seedtable seen but not opened (they restate the post) | unknown |
| Q04 | Jun | `Linear coding sessions Claude Code Codex launch June 2026` | No Linear-specific independent result. Generic Claude Code vs Codex comparison blogs excluded | unknown |
| Q05 | May | `Linear Diffs code review TechCrunch OR "The Verge" OR "The New Stack" 2026` | No coverage from the named outlets. Product Hunt mirrors, releases.sh and chatgate translations excluded as aggregators | unknown |
| Q06 | baseline | `Linear Karri Saarinen interview 2026 agents "issue tracking is dead"` | The Register (Mar 26) and DevClass (Mar 27) are pre-window baseline, seen as search results only. mindstudio blog posts excluded (commentary) | unknown |
| Q07 | Aug | `Linear app tender offer $2.5 billion news report August 2026` | Only [Magica commentary](https://magica.com/news/linear-instinct-same-valuation-different-tests) was relevant (search result only). Results about unrelated "Linear" companies (IEI merger, Linear Technology SEC filing) excluded as an entity collision | unknown |
| Q08 | Jun–Oct | `theregister.com Linear agent coding 2026 Loops OR Diffs OR "coding sessions"` | No in-window Register article found. [LeadDev](https://leaddev.com/?p=34114) and the [pricing tracker](https://pricingsaas.com/companies/linear/diffs/2026W25) opened. aiagentrank comparison pages excluded (SEO listicles) | unknown |
| Q09 | Jun | `devclass Linear 2026 coding agent Claude Code Codex Linear writes code` | No in-window DevClass article surfaced | unknown |
| Q10 | Jun | `leaddev "AI-coding agents are now the default. What comes next?" Linear` | Canonical [LeadDev URL](https://leaddev.com/ai/ai-coding-agents-are-now-the-default-what-comes-next) confirmed (dated Jun 25; partly paywalled). Found [DevOps.com Jul 27](https://devops.com/github-gives-teams-more-control-over-copilots-cloud-agent-in-linear/) (opened) | unknown |
| Q11 | Jul | `github.blog changelog 2026 Copilot coding agent Linear` | [GitHub changelog Jul 23](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available/) opened and included. The 2025-10-28 preview entry is baseline. A kingy.ai tracker gives Jul 24, a one-day discrepancy; the GitHub page date was used | unknown |
| Q12 | all / security | `Linear.app security incident OR outage OR vulnerability May June July August September 2026` | Pingoru status mirror lists operational incidents (snippets mention May 18, Jun 3, Jun 9, Jun 15). **Not included**: a third-party mirror, individual pages not opened, and not linked to official incident records. No in-window security disclosure found | unknown |
| Q13 | Jul–Sep | `Linear "Loops" agent recurring work July 2026 review` | Only Linear pages and aggregators. A "Mean CEO" newsletter (Aug) gives commentary, not an evaluation, and was excluded. No independent hands-on review found | unknown |
| Q14 | Apr / Oct | `"Linear" stacked pull requests October 2026 OR "Linear Releases" CI/CD April 2026 news` | Only the Linear changelog plus GitHub stacked-PR docs (used as context). DevOps.com "GitHub brings stacked pull requests…" concerns GitHub, not Linear, and was excluded | unknown |
| Q15 | roadmap | `linear.app public product roadmap 2026 Linear upcoming features` | **No official public roadmap found.** Third-party reviews (automationatlas, capterra, pikvue) excluded as low-quality or unsourced. One newsletter gives Code Intelligence as May 13 vs the changelog's May 14 | unknown |

## C. Month-segment coverage

| Segment | Dated in-window sources found? | Ledger rows | Independent or second-entity sources |
|---|---|---|---|
| Apr 12–30 | yes | 001–003 | none found |
| May | yes | 004–006 | none found (aggregators only) |
| Jun | yes | 007–010 | LeadDev Jun 25 (relays company claims) |
| Jul | yes | 011–015 | GitHub changelog Jul 23 (partner); DevOps.com Jul 27 (restatement) |
| Aug | yes | 016–021 | Accel Aug 26 (investor, not independent) |
| Sep | yes | 022–026 | none found |
| Oct 1–12 | yes | 027 (plus SDK 97.1.0 on Oct 7, summarised but not a row) | none found |

**No month segment had zero findings.** "None found" for independent reporting is a search limitation, not evidence of absence.

## D. Inclusion, exclusion and deduplication decisions

- **Included: 27 rows.** 18 Linear changelog entries (19 in-window entries minus Jun 4), 6 other Linear pages (Jun 11 CEO post, Aug 10, Aug 17, Aug 26, Aug 31, Sep 21), 1 GitHub SDK release, 1 GitHub partner changelog and 1 trade-press article (LeadDev). 18 + 6 + 3 = 27. The CSV is authoritative.
- **Shared `duplicate_event_group`:**
  - `036-coding-sessions`: the Jun 11 changelog and the Jun 11 CEO post describe one launch.
  - `036-loops`: the Jul 20 launch and the Sep 14 extension.
  - `036-mcp-managed-auth`: the Jul 2 and Aug 13 enterprise-managed MCP authorisation items.

  Rows in a shared group are not independent confirmations.
- **Read but not given a row (to stay within a bounded ledger):**
  - Jun 4 "Team documents" and shared agent skills ([changelog](https://linear.app/changelog/2026-06-04-team-documents));
  - Jun 12 "[Teaching an agent to auto-fix bugs](https://linear.app/now/linear-agent-bug-fix)", which claims the agent lands the correct fix for failing background tasks "about a third of the time" with no denominator;
  - the other 47 SDK and import releases (cadence summarised in the report);
  - SDK 82.0.0 (Apr 18), whose schema descriptions were rewritten "for AI agents".
- **Seen in the index only (not read):** May 28 "Code review should be fast", Jun 10 "Reviewing code in the agent era", Jul 15 Boom and May 13 Cars24 customer stories, Aug 11 Coinbase story, Aug 18 delta-sync post, Aug 26 StyleX post, Apr 17 and Apr 28 posts, and the two YouTube press items (Aug 12, Sep 29).
- **Out-of-window exclusions:**
  - Apr 9 multi-level sub-teams;
  - Apr 6 security post-mortem and Apr 10 blog;
  - Mar 24 Linear Agent launch, essay and press;
  - Oct 13 "Five principles for working with Loops".
- **Date conflicts kept, not resolved:**
  - Diffs is shown as May 28 but its slug says 05-27. Recorded: May 28.
  - Loops for PM is shown as Sep 14 on the entry page and Sep 10 on the /now index. Recorded: Sep 14.
  - Code Intelligence is May 14 per Linear, May 13 per a third-party newsletter. Recorded: May 14.
  - Copilot-for-Linear GA is Jul 23 per GitHub, Jul 24 per a tracker. Recorded: Jul 23.
- **Availability conflict:** the changelog gives coding sessions with no beta label, while the third-party pricing tracker recorded "Coding Sessions (Beta)" on the pricing page in the week ending Jun 15. Status is `shipped` with the conflict noted in the row.
- **Metric conflict:** Ramp Inspect's share of merged PRs is "over 60%" in the Jun 11 Linear post and "75%" in the undated customer story indexed Aug 31. Both are vendor-relayed customer claims with no method given.
- **Access:** public pages only. No login, paywall bypass, private workspace, personal data or scraping beyond single page fetches. LeadDev was partly paywalled; only the visible portion was used.

## E. Inaccessible or unresolved

- The official incident history at linearstatus.com/history returned 404.
- The LeadDev full text is paywalled.
- Linear's pricing page was not fetched directly; the beta label rests on the third-party tracker.
- Corporate structure was not checked at filing level.
- The Register and DevClass March articles were not fetched (search snippets only).

A human reviewer should re-run sections A and B with recorded result counts and UTC times, and spot-check the date conflicts, before any closure of #103.
