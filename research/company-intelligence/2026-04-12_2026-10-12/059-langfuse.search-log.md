# Langfuse (059): provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (2026-10-16).** This log belongs to the [report](059-langfuse.md) and [event ledger](059-langfuse.events.csv) for [issue #127](https://github.com/MSKazemi/github-trending-1000-study/issues/127). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Source access:** 2026-10-16. Exact UTC run times per query were not logged. **Access method:**
- `curl` with a generic `Mozilla/5.0` User-Agent. No personal identifier or contact address was sent in any header, URL or payload.
- GitHub REST API through `gh api`.
- NVD REST API.
- One web-search tool. Its result counts are **not available**, which means unknown rather than zero.

No accounts, paywalls, private endpoints or scans were used. Pages were not archived or hashed, so later edits cannot be detected.

**Number verification:** every figure, price, version and date in the ledger was matched against raw page text (HTML stripped locally) or against GitHub/NVD API JSON. Web-search summaries were used only as leads.

## A. Primary-source enumeration

| Source | Exact access | Result | Decision |
|---|---|---|---|
| Sitemap | `https://langfuse.com/sitemap.xml` → `sitemap-0.xml` (859 URLs); filtered for `/changelog/2026-04..10-12` and `/blog/2026-04..10` | 48 in-window URLs | All fetched. **The sitemap is incomplete**: 26 more changelog slugs were found only through links on monthly updates and the changelog index. 22 of those were fetched; 4 returned 404: `2026-04-13-experiments-beta`, `2026-06-19-monitors-list`, `2026-08-22-evaluation-experience` and `2026-10-12-session-view`. These are probably renamed slugs; none was itemised |
| Changelog index | `https://langfuse.com/changelog` | Shows only the latest 50 entries (from 2026-06-18) | Used for Jun–Oct slugs |
| Monthly updates | `/blog/2026-04-30-langfuse-april-update`, `-05-31-…-may-update`, `-07-31-…-july-update`, `-08-31-…-august-update`, `-09-30-…-september-update` | Read | Used for corroboration and to detect date conflicts. **No June update post was found** in the sitemap |
| Roadmap | `https://langfuse.com/roadmap` (current), plus `gh api repos/langfuse/langfuse-docs/commits?path=content/docs/roadmap.mdx` → raw files at commits `456989f59a` (2026-05-18) and `3e3c531d82` (2026-08-04) | 12 commits in history | Two dated versions used as attributable intent. The Oct 2–8 commits were noted but not itemised |
| Releases | `gh api repos/langfuse/langfuse/releases` (paginated) | 161 releases published 2026-04-17…2026-10-12 (v3.168.0…v4.57.0; v4.0.0 on 2026-07-29; v3.225.x security-backport line continues) | Only v4.0.0 was itemised |
| Advisories | `gh api repos/langfuse/langfuse/security-advisories` | 4 total; 1 in window (GHSA-2524-j966-gfgh, 2026-04-17) | Included. Advisory lists for langfuse-python and langfuse-js were empty. The global advisory DB search `affects=langfuse` returned nothing |
| NVD | API `cveId=CVE-2026-41487`; `keywordSearch=langfuse` for 2026-04-01→07-30 and 2026-07-30→10-13 | 1 and 0 | Included as the severity-conflict row. The NVD HTML detail page is a JS shell, so the API JSON was cited instead |
| License | `gh api repos/langfuse/langfuse/commits?path=LICENSE` and the diffs of `907194fdfe` and `88f7b0a829`; current `LICENSE`; `/open-source`; `/self-hosting/license-key` | Copyright holder changed on 2026-08-18; MIT terms unchanged | Included (CI2026-059-024) |
| Related repos | `gh search repos --owner langfuse`; experiment-action, skills, claude/codex/cursor observability plugins | In-window repo creations and releases | Claude plugin v1.0.0 included. The others are cited as context |
| Status page | `https://status.langfuse.com/` (incident.io; embedded JSON) and detail pages `incidents/h3t8vhtd` and `incidents/trdzkge0` | 14 resolved incidents published 2026-08-03…2026-09-30 | 2 included. The status page exposes no earlier in-window history, so **Apr–Jul incident coverage is unknown** |

## B. Web-search queries (exact strings)

| # | Query | Segment focus | Notable results opened | Decision |
|---|---|---|---|---|
| 1 | `Langfuse 2026 news ClickHouse` | baseline/identity | SiliconANGLE 2026-01-16 (fetched) | Baseline only, outside the window |
| 2 | `"Langfuse" vulnerability OR outage OR incident 2026` | Aug–Sep incidents | isdown.app incident pages: **HTTP 403, inaccessible** | Replaced by the first-party status page |
| 3 | `"Langfuse" v4 review OR criticism OR migration problems 2026` | Aug–Sep | jacar.es migration post (fetched; datePublished 2026-09-25); compatibility docs; upgrade guide | jacar.es included as independent evidence. promptquorum and releases.sh were not opened (aggregator/SEO) |
| 4 | `ClickHouse Langfuse OpenHouse May 2026 announcement` | May | launch-week-5 page, releases.sh | Launch Week covered through changelog entries. The ClickHouse corporate ARR post was excluded: ClickHouse is the parent (#079), the post was not retrieved, and it is not Langfuse product evidence |
| 5 | `Langfuse LLM observability comparison 2026 open source license enterprise edition criticism` | licensing | openobserve, inference.net, mastra, futureagi, datacamp, pydantic comparison | **Excluded**: competitor or vendor SEO comparisons. Their claim of 9 EE-gated features was instead checked against the first-party license-key page |
| 6 | `"Langfuse" September 2026 OR August 2026 OR July 2026 news` | Jul–Sep | Unrelated "fuse" results; one ClickHouse event listing (Sep 1 training) | No in-window news found |
| 7 | `ClickHouse tops $250M ARR 4,000 customers Open House 2026 press release Langfuse` | May | digg repost, job postings, BusinessWire (Jan) | Excluded (parent-company metrics, not a primary source) |
| 8 | `news.ycombinator.com Langfuse 2026` | community | plushcap tracker only | Excluded (aggregator; HN itself not retrieved) |
| 9 | `Langfuse Cloud Japan region launch April 2026 press` | Apr | First-party pages only; plushcap summaries | No independent Japanese press found |
| 10 | `Langfuse site:theregister.com OR site:techcrunch.com OR site:infoq.com 2026` | all | Thoughtworks Radar (fetched; "Last updated: Apr 15, 2026") | Thoughtworks included. **No Register/TechCrunch/InfoQ coverage surfaced** |
| 11 | `"Langfuse" Jev TypeSafe decision model September 2026` | Sep | Changelog/blog (fetched); datacamp, hackernoon, letsdatascience, OpenRouter (not opened) | Only the first-party Langfuse pages were used. Third-party Jev coverage concerns TypeSafe, not Langfuse |

## C. Month-segment coverage

| Segment | Included rows | Notes |
|---|---:|---|
| Apr 12–30 | 4 | Apr 13 Bedrock API keys and Apr 15 LLM-as-a-judge unstable API were screened and not itemised. The `experiments-beta` slug returned 404 |
| May | 9 | Launch Week 5 (May 25–29). May 15 and May 20 export changes were screened and not itemised |
| Jun | 3 | Many UI and SDK entries screened and not itemised. No monthly update post found |
| Jul | 5 | Jul 7 experiments API, Jul 8 Parquet exports, Jul 17 dashboards API and similar entries were screened and not itemised |
| Aug | 7 | |
| Sep | 3 | Sep 1–7 evaluator and Assistant entries were screened and not itemised |
| Oct 1–12 | 2 | Oct 13–14 entries are **out of window** and excluded (redesigned session view, System One decision models, org LLM connections, Python SDK v5 / JS SDK v6). The Oct 7 "OpenAI decision model" entry was screened and not itemised, because the model name could not be checked independently |

## D. Conflicts recorded rather than resolved

1. GHSA severity "low" vs NVD CVSS 5.3/5.4 MEDIUM. The advisory timeline says "April 16, 2025", which is probably a year typo.
2. The Academy is "(beta) live" in the Apr 30 update but has a "Today we're launching" changelog entry dated May 14.
3. The Experiments GitHub Action is mentioned in the Apr 30 update and has a v1.0.0 release on May 5, yet its Launch Week changelog entry is dated May 25.
4. The blog slug `2026-07-16-steal-our-eval-setup` displays the date July 22, 2026.
5. The v4.0.0 GitHub release (Jul 29) comes before the v4 GA changelog (Aug 17). These are treated as one event.
6. The repository LICENSE names ClickHouse, Inc. from Aug 18, while the website footer still names Langfuse GmbH / Finto Technologies Inc.

## E. Untrusted-content log

No instructions directed at AI agents were observed in the fetched content. A grep of all fetched pages for "ignore previous", "if you are an AI" and similar phrases returned no matches.
