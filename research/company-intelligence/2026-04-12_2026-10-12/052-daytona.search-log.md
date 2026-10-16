# Daytona (052) — provisional dated source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (2026-10-16):** this log, the [report](052-daytona.md) and the [event ledger](052-daytona.events.csv) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. This does not close [issue #119](https://github.com/MSKazemi/github-trending-1000-study/issues/119).

**Window:** 2026-04-12…2026-10-12 inclusive. **Research/source inspection:** 2026-10-16 (Europe/Rome date; the host UTC clock read 2026-10-15T22:23Z during the screen). Per-query UTC run times were not recorded individually.

**Provenance:** three kinds of public source were used:

- a public web search tool (US results);
- direct page fetches of Daytona's [changelog index](https://www.daytona.io/changelog), [DotFiles index](https://www.daytona.io/dotfiles) and individual dated entries;
- unauthenticated-equivalent read-only GitHub REST API calls (`gh api`) for the [daytonaio](https://github.com/daytonaio/daytona) and [daytona](https://github.com/daytona) organizations and the [Nightona](https://github.com/nightona-co/nightona) fork, plus SEC EDGAR full-text search and one Form D document.

Each included record is one row in [052-daytona.events.csv](052-daytona.events.csv). **This is not exhaustive discovery.** Search-tool result totals and full excluded-hit denominators are **unknown**, not zero. No snapshot hashes of third-party pages were taken.

**Material coverage limit:** the session's shared web-search budget ran out after the six searches listed below. The planned independent-press queries were therefore **not run**: TechCrunch, The Register, The New Stack, an NVIDIA Vera corroboration search, and `"Daytona" after:2026-04-11 before:2026-10-13`. Following the session rule, no workaround through other search engines, proxies or archives was used. Segments whose evidence is first-party only are flagged below.

## Query log

| Date screened | Segment | Exact recorded query or retrieval | Source pages opened/read and decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all (identity) | WebSearch `Daytona sandbox 2026 announcement` | Results were motorsport (Daytona Speedway/500, karting) only. **All excluded**: name collision. | 9 links returned / 9 screened / 9 excluded |
| 2026-10-16 | all (identity, rights) | `gh api repos/daytonaio/daytona`, `/releases?per_page=100`, `/tags`, `/commits`, `/readme`, `contents/LICENSE?ref=v0.190.0` | Repo `archived=true`. 26 releases in-window (v0.165.0 2026-04-14 … v0.190.0 2026-06-23). [Maintenance-notice commit b40f732a](https://github.com/daytonaio/daytona/commit/b40f732a38a9bdb5a124312bbe4b32712836c7dc) (2026-06-23) **included**. v0.190.0 LICENSE = AGPL-3.0. Releases v0.160–v0.164 (Apr 2–10) **excluded** as pre-window. | 100 releases listed; 26 in-window; 1 commit row included |
| 2026-10-16 | Jun–Oct (rights, releases) | `gh api orgs/daytona`, `orgs/daytona/repos`, `repos/daytona/clients/releases`, `contents/LICENSE`, `commits?path=CLA.md`, `commits?path=LICENSE` | [daytona/clients](https://github.com/daytona/clients) created 2026-06-23. 34 releases v0.191.0 (2026-06-25) … v0.224.0 (2026-10-12), incl. one prerelease. LICENSE: Apache-2.0 except `cli/` AGPL-3.0. [CLA commit](https://github.com/daytona/clients/commit/db054ed16f76f5533b1e85eefee4f5316291d66f) **included**. v0.224.1 (2026-10-14) **excluded** as post-window. | 35 releases listed; 34 in-window; 1 commit row included |
| 2026-10-16 | Apr 12–Oct 12 | Fetch [daytona.io/changelog](https://www.daytona.io/changelog) index | 60 entries Apr–Oct displayed; 55 dated Apr 14–Oct 12 in-window. Entries Apr 2, 3, 8, 9, 10 **excluded** as pre-window. Individually opened and **included**: Apr 14, Apr 23, May 29, Jun 10, Jun 23, Jun 25, Jul 9, Jul 14, Jul 17, Jul 29, Aug 18, Sep 26, Oct 5, Oct 12. Not opened, so not ledgered: the other 41 entries (e.g. May 11 GPU runners, Aug 11 outbound proxy). | 55 in-window / 14 opened / 14 included |
| 2026-10-16 | Apr 12–Oct 12 | Fetch [daytona.io/dotfiles](https://www.daytona.io/dotfiles) index | Dated updates included after opening: [Apr 13 credential advisory](https://www.daytona.io/dotfiles/updates/security-advisory-api-credential-exposure-in-sandboxes), [Apr 30 Copy Fail](https://www.daytona.io/dotfiles/updates/security-update-cve-2026-31431-copy-fail), [May 25 pagination](https://www.daytona.io/dotfiles/updates/daytona-is-moving-to-cursor-based-pagination), [Jun 11 closed source](https://www.daytona.io/dotfiles/updates/daytona-is-going-closed-source). Articles included after opening: [Jul 21 Devin](https://www.daytona.io/dotfiles/devin-outposts-on-daytona), [Aug 26 Yutori](https://www.daytona.io/dotfiles/real-computers-for-computer-use), [Sep 2 Cursor](https://www.daytona.io/dotfiles/cursor-self-hosted-machines-on-daytona), [Sep 18 snapshot search](https://www.daytona.io/dotfiles/snapshots-as-search-states-go-explore-with-daytona), [Oct 7 density](https://www.daytona.io/dotfiles/when-2000-agents-share-one-cpu). | See per-item decisions below |
| 2026-10-16 | Jun–Oct | WebSearch `Daytona closed source AGPL sandbox June 2026` | Opened: the Daytona Jun 11 post (dup of the included row), the [Nightona README](https://cdn.jsdelivr.net/gh/nightona-co/nightona@main/README.md) plus `gh api repos/nightona-co/nightona` (created 2026-07-02, AGPL-3.0) **included**, and [helix.ml comparison](https://helix.ml/blog/self-hosted-agent-sandboxes) (Aug 31, updated Sep 15; competitor) used as `independent_check_url` only. Not opened: devtoollab, stork.ai, agenticwire, sourcepulse, ai.engineer. | 9 returned / 3 opened / 1 row included |
| 2026-10-16 | Jul–Sep (corporate) | WebSearch `"Daytona" AI sandbox news 2026 funding OR acquisition OR "Series B"` | [Dealroom item](https://dealroom.co/news/145417-daytona-lands-48-3m-series-b-for-ai-agent-sandbox-platform/) returned **HTTP 404**, so it is unavailable and not cited as evidence. [AlleyWatch August-rounds list](https://alleywatch.com/?p=163430) opened; it lists USD 48.3M but shows no explicit date, so it is used as a check URL only. Feb 5 Series A press release **excluded** as pre-window. Profile-site traction claims (yespress) not opened and **excluded**. No acquisition found in the results. | 9 returned / 2 opened / 0 rows directly |
| 2026-10-16 | Aug (corporate) | EDGAR full-text `q="Daytona Platforms"&forms=D`; fetch Form D `primary_doc.xml` | Two Form D filings: 2026-02-05 (**excluded**, pre-window) and [2026-08-17](https://www.sec.gov/Archives/edgar/data/1977563/000197756326000002/primary_doc.xml) (**included**; first sale 2026-07-31; USD 48,274,000 sold of USD 60,000,000). | 2 found / 2 screened / 1 included |
| 2026-10-16 | Jun–Oct (reaction) | WebSearch `Daytona "going closed source" sandbox security AI scanning reaction` | [Agent37 comparison](https://www.agent37.com/blog/daytona-alternative), dated Oct 12 and written by a competitor, **included as E0 lead**. Its "archived 2026-10-03" claim and Reddit quote were **not verified** at origin. The search tool's summary mentioned an arXiv privileged-mode critique, but no arXiv URL was opened, so it is **excluded** as unverified. Not opened: towardsai (member-only/paywall, not bypassed), decryptiondigest, pytorch.kr, dev.to. | 9 returned / 1 opened / 1 included |
| 2026-10-16 | all (independent press) | WebSearch `Daytona sandboxes AI agents thenewstack OR techcrunch OR theregister 2026` | **Not performed**: search budget exhausted | unknown |
| 2026-10-16 | Oct | WebSearch `Daytona NVIDIA Vera sandboxes October 2026` | **Not performed**: search budget exhausted. The Oct 7 benchmark remains uncorroborated. | unknown |

## Per-segment result summary

| Segment | Ledger rows | Independent (non-Daytona) rows | Notes |
|---|---:|---:|---|
| Apr 12–30 | 4 (001–004) | 0 | First-party only. Advisory fix date (Apr 9) is pre-window; publication is in-window. |
| May | 2 (005–006) | 0 | First-party only. Other May changelog entries exist but were not opened. |
| June | 5 (007–011) | 0 | Closed-source event group spans 008/010, with commentary in 012 and 028 |
| July | 7 (012–018) | 1 (012 Nightona) | Nightona's date is repository creation |
| August | 3 (019–021) | 1 (019 SEC filing); 021 is a customer guest post on the vendor blog | No official funding announcement located |
| September | 3 (022–024) | 0 | Sep 18 includes vendor-reported negative results |
| Oct 1–12 | 4 (025–028) | 1 (028 competitor, E0) | v0.224.1 (Oct 14) excluded |

## Inclusion, exclusion and validity decisions

- **Included = 28 ledger rows.** Distinct source URLs are 28. **Rows are not independent confirmations**: 25 are Daytona-controlled channels (changelog, blog incl. one customer guest post, GitHub orgs); only 3 (Nightona fork, SEC Form D, Agent37 competitor article) are non-Daytona sources.
- **Deduplication:** the Jun 11 announcement, Jun 23 repo notice, Jul 2 Nightona fork and Oct 12 Agent37 commentary all share `duplicate_event_group = 052-closed-source`. The fork/snapshot rows share `052-fork-snapshot`. Auto-pause and TTL share `052-lifecycle`.
- **Availability classes:** fork/snapshot Apr 14 is **preview** (experimental) and became **stable** on Jul 29. The closed-source post is classed **announced_only**, with implementation evidenced by the Jun 23 commit (**reversed/cancelled** = public OSS maintenance ended). The Android sandbox class removal is **reversed/cancelled**. Integration, benchmark, funding and competitor rows are **reported_undetermined**.
- **Security classes:** the two Daytona advisories are vendor-issued and remediated per the vendor (**corrected**). No independent exploit reproduction or audit was found or attempted.
- **Exclusions:**
  - pre-window: changelog Apr 2–10, monorepo releases v0.160–v0.164, Series A (2026-02-05) and Form D 2026-02-05, and the Jan 30 2026 update;
  - post-window: client v0.224.1 (2026-10-14);
  - undated DotFiles items: Stripe Projects, Convex component, Brainbase;
  - unavailable: Dealroom (404);
  - unverified: the arXiv critique, the yespress traction figures and the Reddit quote.
- **Review access:** public pages and read-only API only. No login, paywall bypass (the towardsai member-only story was not read), network scan, exploitation, GitHub Trending access or participant data was used. Public pages may change; URLs and displayed dates were recorded, but byte hashes were not. **Independent human factual and scientific review is pending.**

A future reviewer should re-run these queries plus the unrun independent-press queries, record UTC timestamps and result totals, verify the archive date and the partner-side (Cognition, Cursor) availability, and spot-check the security entries before any issue closure.
