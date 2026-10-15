# Railway (032) — provisional source-query and inclusion log, 2026-10-16

> **PROVISIONAL, AI-assisted first-pass screen — not reviewed by a qualified human.** Companion to the [report](032-railway.md) and [event ledger](032-railway.events.csv) for issue [#99](https://github.com/MSKazemi/github-trending-1000-study/issues/99). Factual/link, source-access/rights and methods review are **pending**.

**Window:** 2026-04-12…2026-10-12 inclusive. **Screening date:** 2026-10-16 (all `accessed_utc` values). **Tools:** a public web-search tool, a page-fetch tool that returns a model-generated summary of each page (not raw HTML), and the authenticated public GitHub REST API via `gh api`. **Consequence:** page details in the ledger come from tool summaries of the fetched pages; a human reviewer should spot-check wording, numbers and dates against the live pages. No page snapshots or hashes were archived. Search-result totals and per-query UTC run times are **unavailable, not zero**. **This is not exhaustive internet discovery.**

## Query and source log

| Segment | Exact query / direct source | Opened and decision |
|---|---|---|
| all | direct read `https://railway.com/changelog` | Index lists 26 entries dated 2026-04-17…2026-10-09 (previous entry 2026-04-10 is out of window; none after Oct 9 in window). Opened 18 (see below); 8 unopened entries (Jun 12, Jun 19, Jul 16, Jul 24, Aug 28, May 1, May 15, May 29) are title-only and **not ledgered**. |
| all | web search `Railway railway.com 2026 announcement` | Returned mostly rail-transport homonyms; surfaced [Compute Week 2026](https://railway.com/compute-week) (Jun 1–5) and a Jan 2 pre-window changelog (excluded). |
| all | web search `Railway cloud platform Jake Cooper 2026 funding OR acquisition OR outage` (extended mode) | Funding coverage is **pre-window** (Jan 22 Series B: [SiliconANGLE](https://siliconangle.com/2026/01/22/intelligent-cloud-infrastructure-startup-railway-gets-100m-simplify-application-deployment/), [Axios Pro](https://www.axios.com/pro/enterprise-software-deals/2026/01/22/software-deployment-railway-100-million)) — baseline only. A May 21 aggregator piece (aiforautomation.io, "3M users") and startuphub.ai/webpronews/techbuddies pieces were **excluded** as low-provenance relays of company-stated metrics. No acquisition found. |
| all | web search `site:railway.com/blog 2026` | No railway.com hits (homonyms only); `railway.com/blog` returned **HTTP 404**; blog actually lives at `blog.railway.com`. |
| all | direct read `https://blog.railway.com/` | Index shows 10 in-window dated posts (Jun 26–Oct 8) plus many undated posts; in-window posts dated on their own pages found via Compute Week and incident titles. |
| all | web search `Railway incident report outage postmortem 2026 railway.com` | Third-party status aggregators (pingoru.io, isdown.app, uptimerobot.com, plushcap.com) used **only as leads**; official postmortems then read on blog.railway.com. plushcap.com July summary page used to locate the Jul 3 incident URL. |
| May | web search `Railway Google Cloud suspended account outage May 2026` (extended) | Read [The Register, May 20](https://www.theregister.com/off-prem/2026/05/20/google-cloud-suspended-major-customer-railwaycom-without-cause-causing-outage/5243111) → row 005 (same event as row 004; **not** independent confirmation of cause). [DCD](https://www.datacenterdynamics.com/en/news/google-unexpectedly-suspends-railwaycoms-cloud-account/) returned **HTTP 403** (not read). Not opened: Northflank (competitor marketing), ilert/GIGAZINE/bex.co/upnorthmedia (secondary commentary), HN thread, Central Station forum thread. |
| all | web search `"Railway" deployment platform Gilfoyle ad OR sandboxes OR "dev.new" 2026 news` | No dated independent news article. morphllm.com states Sandboxes GA on Jun 26 — **contradicted** by primary Sep 17 changelog; excluded. basenor.com Grok/Railway dates unreconciled; excluded. |
| all | web search `Railway railway.app security vulnerability OR breach OR CVE 2026` | No CVE/breach of Railway's own product found (results were rail-transport CVEs). Recorded as **not found**, not as "no vulnerabilities". |
| identity | direct read `https://railway.com/legal/terms` (plain HTTPS GET) | Legal name **Railway Corporation**, Delaware law, ToS effective date 2026-04-20. Report section 2 only. |
| OSS | `gh api repos/railwayapp/cli/releases?per_page=100 --paginate` filtered to window | 207 releases (v4.37.3 2026-04-15 … v5.66.0 2026-10-12), 0 prereleases; v5.0.0 2026-06-04, v5.2.0 2026-06-05, v5.23.3 2026-06-30, v5.63.1 2026-09-28. Read v5.0.0 notes → row 010. |
| OSS | `gh api repos/railwayapp/{cli,railway-skills,railway-ts-sdk}` | All three report SPDX `MIT`; skills created 2026-01-04, ts-sdk created 2026-05-22. |

## Per-segment coverage

| Segment | Sources opened | Rows | Notes |
|---|---|---|---|
| Apr 12–30 | changelog Apr 17, Apr 24; ToS | 001–002 | No independent coverage found |
| May | changelog May 8, May 22; blog May 19 incident (published May 20), Summer 2026 update (May 27); The Register | 003–007 | DCD 403 |
| June | Compute Week page; blog Metal Gen 2 (Jun 2), Railway for Agents (Jun 3); CLI v5.0.0 release; changelog Jun 5, Jun 26 | 008–012 | Jun 12 and Jun 19 changelog entries unopened |
| July | blog Jul 2 incident (published Jul 3); changelog Jul 3 (opened, not ledgered), Jul 10, Jul 31 | 013–015 | Jul 16/24 unopened |
| August | changelog Aug 7 (3 rows), Aug 14, Aug 21 (2 rows); blog dev.new (Aug 13), deploy without account (Aug 17) | 016–023 | Aug 28 unopened |
| September | changelog Sep 4, Sep 11, Sep 17, Sep 25; blog Sep 30 incident | 024–028 | Third-party trackers mention a second Sep 30 dashboard/auth slowdown; not verified |
| Oct 1–12 | changelog Oct 1, Oct 9; blog Oct 5, Oct 8 | 029–032 | Nothing after Oct 12 included |

**Months with no findings:** none. **Months with no independent (non-vendor) reporting found:** April, June, July, August, September, October.

## Inclusion, exclusion and validity decisions

- **Included = 32 rows**, one per distinct dated claim cluster. Three source pages produce multiple rows (Aug 7 changelog ×3, Aug 21 changelog ×2) because they record separable events (beta launch vs security default vs defect fix; release vs deprecation). Shared URLs are not independent corroboration.
- **Deduplication:** rows 004/005 = one incident (two sources); rows 014/030 = one feature line (beta → GA); rows 015/019 = dev.new; rows 021/022/027 share the anonymous-access group. `duplicate_event_group` records these.
- **Dates:** `published_utc` = displayed page/index date. Slug/display mismatches recorded (Jul 16/17, Aug 20/21, Sep 17/18, Oct 1/2). `event_date_utc` filled only for incidents and the GitHub release timestamp.
- **Status vocabulary:** Priority Boarding / beta / early access / experimental → `preview`; vendor "live/available/GA" → `shipped`; roadmap and deprecation end-dates → `announced_only`; incidents → `reported_undetermined`; fixed defect → `corrected`.
- **Excluded:** pre-window Series B and Feb/Mar incident reports; undated "Best X in 2026" marketing posts; aggregator and competitor pages; the CDN post's headline metric (title says 30M RPS on the blog index but 100M RPS on the Compute Week page).
- **Doubtful details to spot-check:** model names quoted for the ChatGPT-subscription feature (row 026) were deliberately **not** recorded because they could not be cross-checked; numeric details (e.g. 20,000 blackholed links, 13%/40% workload shares, $5,000/mo tier) come from tool summaries of vendor pages.
- **Access:** public pages only; no login, paywall, private status data, scraping of GitHub Trending, or personal data.

A future reviewer should re-run these queries with recorded result totals and UTC times, open the 8 unopened changelog entries, and attempt the DCD article through an authorised route before issue closure.
