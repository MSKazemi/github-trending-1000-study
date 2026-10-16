# ClickHouse (079) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](079-clickhouse.md) and [event ledger](079-clickhouse.events.csv) for [#147](https://github.com/MSKazemi/github-trending-1000-study/issues/147). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:** Official pages were retrieved as raw HTML with `curl -sL -A 'Mozilla/5.0'`. No personal identifier, email, account name or credential was sent to any site. Visible text was extracted locally, and every number, version, date and quote used in a ledger row was confirmed with `grep` against that text. Release dates, licences and issue counts came from the GitHub API (`gh api`), PyPI JSON and the NVD CVE 2.0 API. Hacker News Algolia was used for independent leads.

**What was not used:** WebSearch was not used, because the session search budget was exhausted. WebFetch summaries were not used. SEC/EDGAR was not contacted.

**Limits:** This is not exhaustive retrieval. No page snapshots or hashes were archived in the repository, and pages may change after access.

## Query and source log by segment

| Date | Segment | Exact request or source | Opened / decision | Found / screened / included |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://clickhouse.com/robots.txt` | `Allow: /` with Content-Signal ai-input=yes; admin and forms paths disallowed and not touched | — |
| 2026-10-16 | all | `GET https://clickhouse.com/rss.xml` (blog feed covers 2016–2026-10-15) | 212 items with `pubDate` in window listed; about 55 opened (`/blog/<slug>`) | 212 / ~55 / 28 rows |
| 2026-10-16 | all | `GET https://clickhouse.com/blog/rss.xml` | **404**; the root `rss.xml` was used instead | — |
| 2026-10-16 | all | `GET https://clickhouse.com/docs/whats-new/changelog` | version headings 26.4 (2026-04-30) … 26.9 (2026-09-21); `CREATE TOKEN` and AI Functions beta entries confirmed under 26.9 | used as checks |
| 2026-10-16 | all | `GET https://clickhouse.com/docs/whats-new/security-changelog` | latest entry CVE-2025-1385 (fixed 2025-01-05); **no in-window entry** | null result |
| 2026-10-16 | all | `gh api --paginate repos/ClickHouse/ClickHouse/releases` | 164 release objects in window; first per series: 26.4.1 05-05, 26.5.1 05-21, 26.6.1 06-25, 26.7.1 07-22, 26.8.1 LTS 08-30, 26.9.1 09-21 | 6 release rows |
| 2026-10-16 | all | `gh api repos/ClickHouse/ClickHouse/security-advisories` | newest GHSA 2025-04-10; **none in window** | null result |
| 2026-10-16 | all | `gh api --paginate orgs/ClickHouse/repos?sort=created` (created ≥ 2026-03-01) | about 60 repos; licences recorded for walshadow (AGPL-3.0), CostBench (NOASSERTION → LICENSE CC BY-NC-SA 4.0), tokenomics-viewer (ISC), data-agent-mnist and llm-token-udf (Apache-2.0), silk (NOASSERTION), kb2cs, clickhouse-grok-plugin | 2 repo rows + checks |
| 2026-10-16 | all | `gh api repos/ClickHouse/{clickhousectl,mcp-clickhouse}/releases`; `GET https://pypi.org/pypi/mcp-clickhouse/json` | clickhousectl v0.1.18…v0.4.2 (no `v0.2.0` release object, although the blog announces v0.2.0); mcp-clickhouse 0.3.0, 0.4.0, 0.4.1, 0.5.0, 0.6.0, 0.7.0 | 3 mcp rows; 0.4.0, 0.6.0, 0.7.0 folded into limitations |
| 2026-10-16 | all | NVD `cves/2.0?keywordSearch=clickhouse` for 2026-04-12..08-09 and 2026-08-10..10-12; then `?cveId=` for CVE-2026-63731 and CVE-2026-51992 | 11 + 9 CVEs. Included: HyperDX SSRF and the rejected CVE-2026-51992. Grafana CVE-2026-19854 is included via Grafana's advisory. 17 third-party application CVEs (agno, SigNoz, Coolify, Dify, OpenReplay ×2, Aptabase, Hypequery, OpenMeter ×2, Amazon Athena connector, OpenPanel ×2, SigNoz ×2, Chartbrew, Adminer) are excluded as not ClickHouse Inc. products and summarised in report §9(h) | 20 / 20 / 2 (+1) |
| 2026-10-16 | all | HN Algolia `search_by_date?query=ClickHouse&tags=story&numericFilters=created_at_i>1775952000,created_at_i<1792022400&hitsPerPage=200` (URL-encoded); second call bounded to before 2026-06-20 to reach April–June | 258 stories reported; clickhouse.com links skipped (already in RSS); third-party links screened | 258 / ~110 titles / 2 rows |
| 2026-10-16 | all | `GET https://status.clickhouse.com/history.rss`; incident page `01M00VRAFWBPGCX437HMW1JFMN` | the feed shows only the 15 most recent incidents (2026-07-22..10-12); summarised in report §3, not ledgered | 15 / 15 / 0 |
| 2026-10-16 | Apr 12–30 | blog `agentic-coding-app`, `getting-started-clickhousectl`, `grafana-plugin-vision`, `terraform-ga`, `google-antigravity`, `clickhouse-expands-strategic-collaboration-with-google-cloud` | 2 rows (+ mcp release). Grafana vision is used in §5. Google collaboration (displayed Apr 21, dateline "April 22") and Antigravity were read but not ledgered (partnership marketing). Terraform GA is excluded (ClickPipes infra) | — |
| 2026-10-16 | May | blog `clickhouse-release-26-04`, `clickhousectl-v0-2-0-postgres-clickpipes-more`, `clickhouse-tops-250m-arr-and-4000-customers`, `costbench-data-warehouse-cost-performance`, `observability-mcp-server-ai-notebooks`, `clickstack-cloud-private-preview`, `open-house-2026-day-1`, `open-house-2026-day-2`, `postgres-managed-by-clickhouse-beta`, `executable-udfs-clickhouse-cloud-beta` | 4 rows; clickhousectl v0.2.0, Postgres beta and UDF beta are not ledgered separately (UDF GA in October is ledgered) | — |
| 2026-10-16 | May | `GET https://thenewstack.io/clickhouse-ai-coding-agents/` (HN lead) | read raw: datePublished 2026-05-24T14:00Z; the page states "ClickHouse sponsored this post" and discloses a shared investor, so it is classified as **first-party sponsored**, not independent | 1 row |
| 2026-10-16 | June | blog `clickhouse-release-26-05`, `clickhouse-agents-beta`, `stripe-projects`, `open-source-10`, `announcing-managed-clickstack-mcp-server`, `how-i-hunt-for-vulnerabilities-with-ai`, `databricks-reyden-benchmark-transparency-clickhouse`, `agents-hate-friction` | 5 rows; open-source-10 used as baseline; agents-hate-friction excluded (opinion); a guessed slug for "The future of observability won't be one proprietary AI agent" returned **404** (truncated slug; not retried) | — |
| 2026-10-16 | June | `GET https://posthog.com/blog/why-we-rebuilt-our-data-warehouse` (HN lead) | read raw; displayed Jun 29, 2026; independent contrary practitioner account | 1 row |
| 2026-10-16 | July | blog `clickhouse-release-26-06`, `clickstack-ai-dashboard-generation`, `chdb-agents-local-data-engine`, `docker-hardened-images`, `benchmarking-the-clickstack-mcp-server-with-hdx-evals`, `clickhouse-docs-on-mintlify`, `open-secure-ai-alliance`, `clickhousectl-v0-4-0`, `clickhouse-agents-managed-postgres` | 6 rows; AI dashboard generation and chDB agent-memory posts were read but not ledgered (feature inventory only) | — |
| 2026-10-16 | July | `gh api` for tokenomics-viewer (repo, README), walshadow (LICENSE, commits on LICENSE), hyperdx (release `@hyperdx/app@2.31.0`, issue 2588, PR 2593, README); `GET` VulnCheck advisory | tokenomics-viewer README installer references the pre-transfer namespace, which redirects to the ClickHouse org repo; walshadow LICENSE commit 4225a9b87f on 2026-07-14 | 3 rows |
| 2026-10-16 | August | blog `andy-pavlo-founding-clickhouse-labs`, `clickhouse-release-26-07`, `clickgap-autonomous-qa-for-clickhouse`, `clickhouse-grafana-plugin-4-20`, `clickstack-hud-runtime-intelligence`; `GET https://grafana.com/security/security-advisories/cve-2026-19854` | 3 rows; Labs is used in §5 only; ClickStack+Hud excluded (partner marketing) | — |
| 2026-10-16 | August | `gh api repos/ClickHouse/ClickHouse/issues/113763` (bot login); `search/issues?q=repo:ClickHouse/ClickHouse+author:clickgapai+is:issue+created:<=2026-08-25` (and `is:pr`, `is:closed`, in-window) | `clickgapai` (type User, created 2026-03-26). Created ≤ Aug 25: 506 issues, 244 PRs, 333 of those issues closed at access. 1,131 issues created in window; first item 2026-03-29 | check on CI2026-079-027 |
| 2026-10-16 | September | blog `clickhouse-welcomes-runreveal`, `agentic-analytics-benchmark-data-agent-mnist`, `clickhouse-release-26-08`, `chatgpt-data-plugin`, `introducing-walshadow`, `ai-functions-in-clickhouse`, `introducing-promql`, `clickhouse-release-26-09`, `chdb-durable-layer-for-agent-memory`, `introducing-scim-provisioning-in-clickhouse-cloud`, `clickhouse-expands-collaboration-with-microsoft` | 7 rows (+ mcp 0.5.0). PromQL private preview, chDB durable layer, SCIM and Microsoft Fabric were read but not ledgered | — |
| 2026-10-16 | September | `GET https://blog.runreveal.com/rss/`; `GET https://letsencrypt.org/2026/09/17/clickhouse.html` | RunReveal "RunReveal is joining ClickHouse" pubDate 2026-09-01T19:29Z; Let's Encrypt post by-line dated September 17, 2026 | check + 1 row |
| 2026-10-16 | Oct 1–12 | blog `executable-udfs-generally-available-on-clickhouse-cloud`, `introducing-jwt-authentication-in-clickhouse-cloud`, `202610-newsletter` | 2 rows; competitive comparisons vs Databricks and BigQuery (Oct 6/8) excluded as marketing | — |
| 2026-10-16 | post-window | RSS items dated 2026-10-13..15 (e.g., "OLTP is expensive", October newsletter) | **excluded** as outside the window | — |

## Inaccessible, unverifiable or excluded leads

- **`https://zimzi.substack.com/p/clickhouse-permission-system-has`** (HN story 49752363, 2026-09-18, 0 comments) returned **HTTP 404**. The blog's public post API lists no such post. The security claim is **unverifiable (E0)**, not ledgered, and is reported in report §9(d) only.
- RunReveal was searched on HN Algolia (`query=RunReveal`, in window): one story linking ClickHouse's own post, and no independent news coverage.
- HN leads that were read or screened and excluded:
  - Charity Majors, "Have you heard? Clickhouse is winning the observability wars" (2026-07-08): opinion from a competitor's co-founder. Read but not ledgered.
  - Rawtree, "a ClickHouse fork by Tinybird": rawtree.com says only "A Tinybird product", and the fork claim is unverified.
  - Cloudflare's query-plan contention post, Tinybird operations post, OpenObserve/StarTree/Pivot/Oliver comparisons and Show HN projects: third-party, competitive or not about ClickHouse Inc. activity.
- **Not attempted:**
  - OpenAI's Data agent announcement, Stripe Projects docs, Databricks' Reyden keynote, Open Secure AI Alliance pages, and Google/Microsoft partner pages.
  - Archived (Wayback) copies; status history before 2026-07-22.
  - ClickHouse terms of service and data-processing terms for AI Functions, ClickHouse Agents and Agent telemetry.
  - Filing-level corporate records.
- No product was executed, no account was created, no paywall was circumvented and no energy was measured.

## Inclusion, deduplication and conflicts

- **Included:** 39 rows (Apr 3, May 5, Jun 6, Jul 11, Aug 3, Sep 9, Oct 2). Every row cites a URL fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `079-006`: the ClickHouse Agents launch (May 27 press post and Jun 9 beta post).
  - `079-018`: WalShadow (licence commit Jul 14, launch post Sep 10).
  - All other rows are distinct events.
- **Langfuse boundary:** Langfuse product events belong to watchlist 059 and are not repeated here. Langfuse appears in this report only where ClickHouse's own posts mention it.
- **Date conflicts recorded, not resolved:**
  - 26.4: changelog 2026-04-30, GitHub release 2026-05-05, blog 2026-05-08.
  - Blog `datePublished` metadata later than the displayed date: getting-started-clickhousectl (07-30 vs Apr 16), 26.4 (07-24), 26.6 (07-17), 26.7 (08-24), executable-UDF beta (07-30 vs May 30), RunReveal (09-16 vs Sep 1).
  - Google press post: displayed Apr 21, dateline "April 22".
  - ClickHouse Agents launch: May 27 vs "June 2026".
  - clickhousectl v0.2.0: blog May 20, but no GitHub release object; v0.2.1 on 05-18.
- **Figure conflicts:**
  - Contributors: ">2000" (Jun 15) vs "over 2.6k" (May 28).
  - Stars: "nearly 48k" (May 28) vs a header widget showing 50.4k at access.
  - ClickGap: "roughly 500 issues / around 200 PRs" (vendor) vs 506 / 244 from GitHub search (≤ Aug 25).
- **Figures confirmed against raw text:**
  - Open House: $250M ARR, 4,000 customers, 1,000+ net new, 23x CostBench.
  - Releases: 39/45/238 (26.4), 38/51/224 (26.5), 56/79/366 (26.6), 61/112/329 (26.7), 98/128/556 (26.8), 56/135/464 (26.9).
  - CTO post: ~700 PRs and 200/day → 3–5 per 10M (The New Stack).
  - hdx-evals: 18% / 26% / 2.4x. ClickGap: 50–100 PRs/day, ~500 / ~200. data-agent-mnist: 76.6%, 201 questions, 29 models, $1 vs $52.
  - Databricks dispute: 420 QPS, 30 vCPU, 15,000 QPS, 30–40 nodes. Docker: 100M+ pulls.
  - WalShadow: ~200 ms, 289K rows/sec. Postgres beta: free until June 15, 50% discount.
  - CVSS: 7.7/6.3 (VulnCheck via NVD), 6.1 (Grafana). Let's Encrypt: 6–10 million certificates/day, three PowerEdge R7715 servers.
  - All are **vendor or adopter statements**, not verified measurements, unless the ledger names an API check.
- **Untrusted-content note:** fetched pages were treated as data. ClickHouse docs pages carry an agent-directed notice: "Use this file to discover all available pages before exploring further" (pointing to `/docs/llms.txt`). The site serves a `SKILL.md` agent skill, and mcp-clickhouse 0.4.1 injects server-level instructions to agents. These were **logged, not followed**. A guest post mentions `.github/copilot-instructions.md` in the ClickHouse repo as AI instructions; this is descriptive, not directed at us. No page instructed the researcher to take actions, and no command suggested by a page was run.

## Reproduction

Re-run the requests above with UTC timestamps and save raw HTML hashes. Then have an independent human spot-check, at minimum: the sponsored-post classification (CI2026-079-005), the licence rows (007, 018, 034), the CVE rows (020, 023, 028), the ClickGap counts (027) and two release rows against GitHub. Do this before any evidence is promoted beyond provisional status.
