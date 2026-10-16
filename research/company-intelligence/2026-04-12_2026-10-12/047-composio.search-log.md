# Composio (047) — provisional dated source-query and inclusion audit

> **Provisional source-lead screen (2026-10-16):** this search log, the [report](047-composio.md) and the [event ledger](047-composio.events.csv) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. This is not scientific or security sign-off and does not close [issue #114](https://github.com/MSKazemi/github-trending-1000-study/issues/114).

**Window:** 2026-04-12…2026-10-12 inclusive. **Research/source inspection:** 2026-10-16.

**Provenance:** sources were found and read in four ways:
- a general web-search tool (results returned as titles and URLs) and a page-fetch tool;
- `curl` of public documentation files;
- public GitHub REST API calls through `gh api` (read-only; no github.com/trending access);
- public PyPI JSON, the OSV and NVD APIs.

**This is not exhaustive internet discovery.** Search-tool result totals, query-run UTC times and complete denominators of excluded hits are **unknown, not zero**. No snapshot hashes of third-party pages were taken. No login, account creation, paywall, package installation or tool execution was used.

## Cross-window channel enumeration (performed once, then split by segment)

| Date screened | Channel / exact query or call | Result and decision |
|---|---|---|
| 2026-10-16 | Page fetch `https://composio.dev/blog` (blog index) | 10 in-window posts: May 4 (×2), May 21, Aug 28, Sep 9, Sep 14, Sep 17, Sep 22, Sep 30, Oct 8. Pre-window posts (e.g. Mar 27 Universal CLI, Oct 2025 Tool Router beta, Jul 2025 Series A) treated as baseline |
| 2026-10-16 | Page fetch `https://docs.composio.dev/docs/changelog` and `https://docs.composio.dev/changelog` | Both returned HTTP 404 to the fetch tool |
| 2026-10-16 | Web search `Composio changelog 2026` | No official changelog returned. Third-party trackers only (aitoolsatlas, pricingsaas). Not used as event sources (see exclusions) |
| 2026-10-16 | Web search `docs.composio.dev changelog 2026 link auth migration connected accounts` | Returned canonical dated changelog URLs (e.g. `/docs/changelog/2026/04/24`, `/04/28.md`, `/06/04.md`) and `migrating-initiate-to-link`. Preview-deployment mirror URLs (`*.preview.composio.dev`) were ignored |
| 2026-10-16 | `curl https://docs.composio.dev/llms.txt`, then `curl https://docs.composio.dev/docs/changelog.md` | The index lists **35** dated entries from 2026-04-17 to 2026-10-12 (plus Oct 14 and 15, out of window). 24 in-window entries were downloaded as `.md` and read. `curl` returned HTTP 200 for the HTML URLs cited in the ledger |
| 2026-10-16 | `gh api repos/ComposioHQ/composio` and `.../license` | MIT; created 2024-02-23; default branch `next`. The star count is recorded only as context and is not an adoption measure |
| 2026-10-16 | `gh api repos/ComposioHQ/composio/releases --paginate`, filtered to window | **662** releases (Apr 41, May 63, Jun 52, Jul 47, Aug 143, Sep 265, Oct 51), mostly CLI beta and per-package tags. Read the notes for core 0.9.0, 0.11.0, 0.12.0 and CLI 0.3.0. Used only as corroboration (`independent_check_url`), **not** counted as events |
| 2026-10-16 | `gh api repos/ComposioHQ/composio/security-advisories` | Empty result (repository-published advisories: none visible) |
| 2026-10-16 | `https://pypi.org/pypi/composio/json` | 22 versions uploaded in the window (0.11.6 Apr 23 → 0.26.0 Oct 12; `2.0.0b0` Aug 31). License field empty |
| 2026-10-16 | OSV API queries: `composio` (PyPI), `@composio/core` (npm), `composio-core` (PyPI) | Only 2024–2025 GHSAs, plus PyPA `PYSEC-2026-1262…1267` dated 2026-07-07. These are **re-indexings of older advisories** (e.g. PYSEC-2026-1262 = CVE-2025-56427, last affected 0.7.20), so they were excluded as new in-window events. `@composio/core`: none |

## Per-segment screen

| Segment | Queries / channels that produced leads | Source pages opened/read and decision | Search found/screened/excluded counts |
|---|---|---|---|
| Apr 12–30 | Changelog index; `curl` of `/2026/04/{17,22,23,24,27,28}.md` | Included Apr 22, 23, 24 and 27. Screened but not counted: Apr 17 observability APIs and Apr 28 `link()` guard / sandbox tier (lower lens relevance). **Excluded** as pre-window: Apr 7, 8, 9 entries | unknown |
| May | Blog index; changelog `/05/{07,12,13}.md`; web searches `Composio breach May 2026 GitHub tokens API keys` and `"Composio" security incident OAuth tokens revoked customers 2026 report` | Opened [Apr 28 incident report](https://composio.dev/blog/incident-report-april-28) (published May 4), [agents can sign up](https://composio.dev/blog/your-agents-can-signup-for-composio) (May 4; screened, not counted, because the post gives no scope or availability detail), [May 2026 security incident](https://composio.dev/blog/composio-may-2026-security-incident) (two fetches; version table May 21–27, updated Sep 16), [Mintlify status page](https://status.mintlify.com/incidents/01KSB1RZK85RJ71W4BYSDFGYH1). May 8 session-reuse entry was not counted separately. Search results not opened: `composio.dev/content/...` (mirror of the blog URL), Cursor forum thread, status.composio.dev, threatcluster.io | unknown |
| June | Changelog `/06/{04,17,19,27}.md` read in full; other June entries judged on their index titles only; Material Security result from the May incident searches | Included [Material Security analysis (Jun 3)](https://material.security/resources/the-composio-breach-one-token-10242-doors), Jun 4 roll-up and Jun 19 TS SDK 0.11.0. Screened, not counted: Jun 16 (Python equivalent of Jun 19; title only), Jun 17 PostHog region, Jun 27 Python sessions-first (read), Jun 25/26/28 SDK session releases (titles only) | unknown |
| July | Web search `composio CVE 2026 OR GHSA composio python package vulnerability`; NVD API `cveId=CVE-2026-59807`; `gh api` issue #3746, PR #3763, release `@composio/cli@0.2.32-beta.283`; `gh api /advisories/GHSA-hp3h-89pf-5q58`; changelog `/07/{15,30}.md` | Opened the [VulnCheck advisory](https://www.vulncheck.com/advisories/composio-sdk-beta-283-sensitive-file-upload-via-tool-file-uploads-ts) (Jul 8, CVSS 4.0 8.9) and the [thehackerwire mirror](https://www.thehackerwire.com/vulnerability/CVE-2026-59807/) (CVSS 3.1 6.8). The NVD API gives published 2026-07-08 and CNA `disclosure@vulncheck.com`. The NVD HTML page rendered no content in the fetch tool. Issue opened 2026-07-03; PR merged and prerelease shipped 2026-07-06. The GHSA cited in the PR title returned 404 from the global advisory API. Included Jul 15 and Jul 30 changelog entries | unknown |
| August | Changelog `/08/{07,19,28}.md`; blog index | Included Aug 7 (redaction defect fix) and Aug 28 (scoped session permissions). Screened, not counted: Aug 19 session-aware provider helpers (read); Aug 5/6 CLI installer and argument fixes (index titles only); [Aug 28 family-newspaper tutorial](https://composio.dev/blog/building-a-daily-family-newspaper) (tutorial, not an event); PyPI `2.0.0b0` (pre-release with no release note found) | unknown |
| September | Blog index; changelog `/09/{04,21,24,29}.md`; web search `Composio AI agent integration platform news 2026` | Included [Sep 9 security post](https://composio.dev/blog/two-questions-every-security-review-asks-us), [Sep 14 Shared Connections](https://composio.dev/blog/introducing-composio-shared-connections), Sep 21 read-scope fix, [Sep 22 Yang](https://composio.dev/blog/yang-software-factory). Screened, not counted: [Sep 17 webhook triggers for 14 providers](https://composio.dev/blog/build-reactive-integrations-with-webhook-triggers), Sep 24 experimental premium-usage policies (precursor of Instant), Sep 29 Instant session contract (used as `independent_check_url`), [Sep 30 CI runners](https://composio.dev/blog/cpumaxxing-our-ci-runners) (internal CI timings, vendor-reported). The news search returned only undated profiles and comparison pages | unknown |
| Oct 1–12 | Blog index; changelog `/10/12.md` | Included [Oct 8 Composio Instant](https://composio.dev/blog/composio-instant) (launch row plus a separate announced_only row for stated plans) and Oct 12 SDK 0.26.0/0.23.0. **Excluded** Oct 14 and Oct 15 changelog entries (out of window) | unknown |
| Identity / ownership / funding | Web search `Composio raises Series B 2026 OR acquisition Composio agents`; page fetch [terms](https://composio.dev/terms); [Entrackr funding article](https://entrackr.com/news/agentic-ai-startup-composio-raises-25-mn-led-by-lightspeed-9525112) | The Series B/acquisition search returned only unrelated companies (CompoSecure, Hexagon Composites, etc.): **no in-window corporate event found**. Terms page: "Sampark Inc, doing business as Composio", Delaware law, no date shown. The Series A article is dated 2025-07-22, so it is **pre-window baseline** | unknown |
| Negative/irrelevant query | Web search `Composio Rube MCP launch 2026` | All results unrelated (spaceflight). Nothing recorded | unknown |

## Inclusion, exclusion and data-validity decisions

- **Included = 25 ledger rows.** Several rows cite the same changelog site with distinct dated entries. Rows 009–011 are **one incident** told by three publishers (`047-may-incident`). Rows 002/014 are one control and its later bypass (`047-upload-denylist`). Rows are not independent confirmations of product success.
- **Not used as event sources:**
  - [pricingsaas Week 37 diff](https://pricingsaas.com/companies/composio/diffs/2026W37) (Aug 31 → Sep 7): it reports that the pricing page now advertises "1500+ toolkits", but the page contradicts itself on which plans this applies to, and a catalog count is a marketing claim.
  - pricingsaas Week 42 ("Premium tools" renamed "Instant Tools"): seen only as a search snippet, not opened.
  - aitoolsatlas changelog summary: an undated secondary aggregation.
  - cxodigitalpulse funding article: returned by search, not opened; the funding is pre-window.
  - truto.one "alternatives to Composio": competitor marketing.
  - Composer (PHP) CVE-2026-45793 results: a different product.
- **Availability classes:**
  - Webhook V2 and callback identity verification: opt-in.
  - Shared connections: experimental in May; dashboard feature in Sep, with the developer API still experimental.
  - Scoped keys: staged rollout from Jun 4.
  - CVE fix: CLI **prerelease**.
  - Instant: launched (no beta/GA label), with separate future plans.
  - No item has been promoted from announced to shipped.
- **Date handling:**
  - The May incident row uses the May 21 date shown on the blog index and in the page's own version table. The live page is "Updated September 16, 2026".
  - Mintlify's first update is displayed as "May 23, 2026, 06:32 PM" with no timezone, so the UTC day may be May 24.
  - The Apr 28 outage has published 2026-05-04 and event 2026-04-28.
  - The CVE row has published 2026-07-08 (VulnCheck/NVD) and event 2026-07-06 (fix merged).
- **Primary vs independent:** vendor changelogs support E2 claims about what was documented as released. They are not proof of behaviour. Independent evidence is limited to an affected customer, a commercial security vendor and a CNA record. **No E3 controlled test exists.**
- **Review access:** public pages and APIs only. Public pages may change after access. Factual, scientific and **independent human review is pending**.

A future reviewer should re-run these queries with UTC timestamps and result totals. They should also archive the changelog entries and the versioned incident page, and verify the July 3 auth cutover, scoped-key availability and the status of the GHSA cited in PR #3763 before any issue closure.
