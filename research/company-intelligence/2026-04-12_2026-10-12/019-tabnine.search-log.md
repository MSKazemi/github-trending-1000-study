# Tabnine (019) — dated source-query and inclusion log (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this search log, the [report](019-tabnine.md), [event ledger](019-tabnine.events.csv) and [source-QC note](019-tabnine.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**, unreviewed by a qualified human; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#86](https://github.com/MSKazemi/github-trending-1000-study/issues/86) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Window:** 2026-04-12…2026-10-12 inclusive. **Run date:** 2026-10-16 (UTC calendar date; exact per-query UTC times not recorded). **Tools:** a general web-search tool (5 queries), direct HTTPS fetches of official pages, Internet Archive Wayback Machine availability API and raw (`id_`) captures, and read-only `gh api` calls. No logins, paywalls, github.com/trending access or bulk crawling. **Result counts** from the web-search tool are not exposed and are recorded as **unknown**, not zero. No earlier search log existed for 019 (the 2026-10-12/13 screens stated that their queries were "next-pass suggestions" and were not preserved).

## Access condition discovered first

On 2026-10-16 every tested `www.tabnine.com` path (`/`, `/blog/`, `/blog/category/product-news/`, `/pricing`, and all blog article URLs below) returned **HTTP 301** to a generic `www.tricentis.com` page. Tabnine-domain blog content was therefore read only through Wayback captures. `docs.tabnine.com` (release notes, product docs) remained reachable (HTTP 200).

## Primary-channel fetches (not web searches)

| # | Fetch | Result | Use |
|---|---|---|---|
| F1 | `curl -I`-style status checks of tabnine.com URLs | all 301 → tricentis.com | access finding; recorded in QC |
| F2 | Wayback availability API for the three ledger URLs, `/blog/`, `/blog/category/product-news/`, Context-Readiness and Gartner posts | captures exist for April recap (20260512), shared-memory (20260621), new-chapter (20260804, 20260909), `/blog/` (20260607, 20260909); none for Context-Readiness article, Gartner post, May-2026 product-update article or product-news category | QC + index listings |
| F3 | Raw Wayback capture `/blog/` 20260607023936 | lists posts dated Apr 6, Apr 9, **Apr 29** (May 2026 Product Update), **May 6** (April recap) and a Gartner post displayed as **"May 28, 2025"** | CI2026-019-005; Gartner date conflict (excluded) |
| F4 | Raw Wayback capture `/blog/` 20260909050654 | lists posts Jun 17, Jun 18, Jun 22, Jun 24, Jun 25, **Jun 26**, Jul 6, Jul 10, **Jul 30**; **no post after Jul 30** as of 2026-09-09 | CI2026-019-008; August blog silence noted (not an event) |
| F5 | `https://docs.tabnine.com/main/administering-tabnine/release-notes` (+ `.md` export) | dated entries v6.0.4 (Apr 12) … v6.6.11 (Oct 14) | CI2026-019-003/006/007/009/013/015/017/018 |
| F6 | `https://www.tricentis.com/news/tricentis-acquires-tabnine` | HTTP 200, dateline "AUSTIN, Texas – July 30, 2026" | CI2026-019-010 |
| F7 | `gh api orgs/codota/repos` (pushed after 2026-04-01) and per-repo releases | `tabnine-pr-agent` v2 (2026-04-29); `tabnine-opencode-public` (created 2026-07-23) tags v0.4.1 (2026-08-05) … v1.0.5 (2026-10-08); `tabnine-vscode` and `tabnine-nvim` **archived** (archive date not exposed by API) | CI2026-019-004/014/016 |
| F8 | `gh api /advisories?cve_id=CVE-2026-64642` | GHSA-6gpp-xcg3-4w24, Next.js, high, published 2026-07-22 | independent check for CI2026-019-015 |
| F9 | `gh api repos/sst/opencode` | redirects to `anomalyco/opencode`, MIT | rights baseline |
| F10 | `https://docs.tabnine.com/main/getting-started/tabnine-plugin-for-opencode` | no beta/GA label, names OpenCode, no licence statement; page contains an "Agent Instructions" block addressed to AI agents (ignored) | feature map |

## Per-segment log

| Segment | Queries / fetches actually run | Pages opened | Included rows | Excluded / notes | Search counts |
|---|---|---|---|---|---|
| Apr 12–30 | F3, F5, F7 | release notes v6.1.0; PR-agent v2 release; `/blog/` 20260607 capture | CI2026-019-003 (Apr 15), -004 (Apr 29), -005 (Apr 29) | "Governance You Can Trust: What's New in Tabnine 6.1" displayed **Apr 9** → **outside window**; v6.0.4–v6.0.10 and v6.1.2–v6.1.5 patch notes not separately logged (bug-fix only) | unknown |
| May | F2/F3, F5 | April-recap capture 20260512; release notes v6.2.0 | CI2026-019-001 (existing, May 6), -006 (May 12) | Gartner "Visionary 2026 MQ" post: displayed date "May 28, 2025" on a 2026 capture conflicts with the 2026 title → **excluded** pending a dated primary copy; no third-party Gartner page opened | unknown |
| June | F2, F4, F5 | shared-memory capture 20260621; release notes v6.3.0; `/blog/` 20260909 capture | CI-019-02 (existing, Jun 18), CI2026-019-007 (Jun 7), -008 (Jun 26) | Thought-leadership posts Jun 17/22/24/25 listed but not counted (commentary, no release); v6.3.x patches excluded | unknown |
| July | Q1, F4, F5, F6 | release notes v6.4.0; new-chapter capture 20260804; Tricentis release; Calcalist | CI2026-019-009 (Jul 7), CI2026-019-002 (existing, Jul 30), -010 (Jul 30), -011 (Jul 31) | Business Wire, SD Times ("SD Times Newswire"), GovConWire, Intelligent CIO, 01net, Pulse2, IT Brief = **syndications of one release**, not opened beyond SD Times byline check / deduplicated. Futurum Group page opened: **AI-generated byline ("FuturumAI"), header Jul 31 vs body Aug 6** → excluded as low-reliability. Jul 6/Jul 10 blog essays not counted. | unknown |
| August | Q2, F5, F7 | beri.net analysis; release notes v6.5.0; opencode releases | CI2026-019-012 (Aug 2), -013 (Aug 5), -014 (Aug 5) | No Tabnine blog post Aug 1–Sep 9 per F4 (observation of silence, not an event row). briefglance.com "$500M" headline seen **only as a search-result title, not opened**, conflicts with Calcalist → not used. | unknown |
| September | Q3, Q4, F5, F7, F8 | release notes v6.6.0–v6.6.6; opencode v1.0.0 | CI2026-019-015 (Sep 15), -016 (Sep 24) | v6.6.1/6.6.2/6.6.3/6.6.6 patches folded into feature map; no Sept roadmap statement found from Tabnine or Tricentis | unknown |
| Oct 1–12 | F5, F7 | release notes v6.6.8, v6.6.9 | CI2026-019-017 (Oct 4), -018 (Oct 8) | v6.6.11 (Oct 14) and the 2026-10-16 site-redirect observation are **outside the window** (context only); opencode v1.0.4/1.0.5 not separately counted | unknown |

## Web-search queries executed (5)

| ID | Exact query | Useful results opened | Decision |
|---|---|---|---|
| Q1 | `Tricentis acquires Tabnine July 2026` | Futurum (excluded), SD Times (syndication) | buyer release + independent leads |
| Q2 | `Tabnine 2026 news coding agent OR "Context Engine" OR CLI announcement May June September` | none opened (aggregators yespress.io, pricingsaas.com, tooliverse.ai, similarlabs.com) | used only to locate the Gartner and pricing leads; aggregator summaries not cited as evidence |
| Q3 | `Tabnine CLI "OpenCode" 2026` | docs.tabnine.com OpenCode plugin page (F10) | feature map |
| Q4 | `Tabnine after Tricentis acquisition customers product roadmap September 2026` | Calcalist, beri.net | CI2026-019-011, -012 |
| Q5 | `Tabnine vulnerability OR security advisory OR outage 2026` | none (third-party status aggregators only) | excluded; no Tabnine CVE found by search; status.tabnine.com not opened |

## Planned but not executed

- `site:tabnine.com after:2026-04-11 before:2026-10-13` per month — **not executed** (site redirects; replaced by Wayback index captures F3/F4).
- Gartner Magic Quadrant 2026 Enterprise AI Coding Agents publication date (gartner.com) — **not executed** (budget; likely paywalled).
- pricingsaas.com Tabnine Week-20 packaging diff (Context Engine bundling, mid-May) — **not executed/opened**; seen only as a search-result summary, not cited.
- Corporate filing for the Tricentis–Tabnine closing (e.g. Israeli registrar) — **not executed** (no public filing located; would require registry access).
- status.tabnine.com incident history — **not executed**.
- Reuters/TechCrunch/The Register targeted queries — **not executed** (shared search budget); absence of such coverage is unknown, not zero.

## Validity notes

- Release-notes rows share one living URL; each row is pinned by version and displayed date, but the page has no per-entry archive hash and has self-corrected at least twice (v6.2.0 hint, CLI version 0.20.3→0.20.2).
- Wayback captures are third-party copies, not vendor-signed snapshots.
- Rows are a purposive selection of feature releases and material corporate events, not a census of Tabnine changes.
