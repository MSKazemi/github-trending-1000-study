# Baseten (067) — search, enumeration and inclusion log

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16), not reviewed by a qualified human.** Companion to the [report](067-baseten.md) and [event ledger](067-baseten.events.csv). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Issue:** [#135](https://github.com/MSKazemi/github-trending-1000-study/issues/135) · **Window:** 2026-04-12 … 2026-10-12 inclusive (UTC dates) · **All access:** 2026-10-16 · **Method:** [company-intelligence protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). **Not exhaustive.** Search engines exposed no reliable hit totals. "unknown" means not available, not zero. The requests used a generic browser User-Agent only. No personal identifier, login, paywall or account was used. No page snapshot hashes were stored in the repository.

## A. Public web-search queries (executed)

| ID | Segment | Exact query | Found | Opened / decision |
|---|---|---|---|---|
| Q01 | all | `Baseten 2026 announcement` | unknown | 0 relevant results (music, BASF, unrelated). Recorded as a null query. |
| Q02 | all (funding) | `Baseten funding 2026 valuation` | unknown | Leads only: multiples.vc, noqta.tn, techleap, techpartner.news, kucoin, letsdatascience, shopifreaks. Only techpartner.news was opened (see Q03). |
| Q03 | June | `Baseten Series F $1.5 billion $13 billion valuation June 2026` | unknown | **Opened:** [Baseten Series F post](https://www.baseten.co/blog/announcing-our-series-f/), [Dealroom 2026-06-23](https://dealroom.co/news/135561-baseten-raises-1-5b-series-f-at-13b-valuation-as-ai-inference-demand-sur/), [Reuters via techpartner.news 2026-06-24](https://www.techpartner.news/news/ai-startup-baseten-hits-13-billion-valuation-as-australias-blackbird-makes-record-bet-626878). Excluded: kucoin, ai2.work, caproasia, stockanalysis (aggregators/crypto news). |
| Q04 | September | `Baseten acquires Blaxel September 2026` | unknown | **Opened:** [Tekedia (Blaxel investor) 2026-09-10](https://www.tekedia.com/baseten-acquires-tekedia-capital-portfolio-company-blaxel/). **Inaccessible:** [Wilson Sonsini page](https://www.wsgr.com/en/insights/wilson-sonsini-advises-blaxel-on-its-acquisition-by-baseten.html) returned HTTP 403, so it was skipped. **E0 lead, not included:** a deal-tracker snippet claiming Baseten also acquired "Fully Parsed" the same day; it was not opened or verified. |
| Q05 | September | `Baseten OpenAI partnership Codex open models September 2026` | unknown | **Opened:** [Digital Today 2026-09-30](https://www.digitaltoday.co.kr/en/view/109278/baseten-joins-openai-marketplace-open-models-available-directly-in-codex). It restates Baseten's statement. **E0, not opened:** a startupresearcher.com snippet about Kimi K3 in Codex (dated Oct 1, attributing a "first Chinese open model" claim to Sina Finance). No OpenAI-hosted page surfaced. |
| Q06 | all (incidents) | `Baseten outage incident 2026` | unknown | Pointed to the third-party monitor [statusfield](https://statusfield.com/services/baseten/incidents). It was fetched but not used because it duplicates the official feed (section B3). Other hits were unrelated power outages. |
| Q07 | June | `TechCrunch Baseten two-tier valuation $11 billion $13 billion` | unknown | Only snippets of secondary sites (kucoin, valuethemarkets, texxr, mezha.net, a mirrored TechCrunch/WSJ-attributed item) were returned. **None were opened**, so the $11B/$13B split is graded **E0** and kept out of the ledger. |

**Planned but not executed (session web-search budget exhausted):** `Microsoft AI MAI-Thinking-1 Baseten`; `OpenAI B2B marketplace open models Codex Baseten openai.com`; `Goodfire Project Beacon Baseten inference safety October 2026`. Further planned critical and contrary searches were also not run: security advisories/CVE for Truss, Hacker News or Register criticism, customer-side incident reports, and NVIDIA OpenShell partner lists. **Partner-side confirmation and independent critical coverage are therefore a known gap**, not a finding of absence.

## B. Direct source enumeration (no search engine)

1. **Blog index:** `https://www.baseten.co/blog/?page=1` … `?page=11`, plus the category pages `news`, `product` and `community`. The embedded CMS records (slug, title, short description, `_publishedAt`) were parsed. This gave 104 distinct posts, 80 of them with CMS time in window. Nineteen posts were then fetched in full and their **displayed** "Published" dates read from page text.
2. **Changelog:** the index page shows only the 10 latest entries, so the 237 changelog URLs were taken from `https://www.baseten.co/sitemap.xml`. The 72 most recent were fetched individually. Each page's displayed date was cross-checked against its CMS `_firstPublishedAt`, and they agreed within the US-Pacific/UTC offset. **53 entries have displayed dates in the window.**
3. **Status page:** `https://status.baseten.co/api/v2/incidents.json`, plus 3 incident pages opened. The feed returns only the latest 50 incidents, oldest created 2026-06-03. Counts by impact and month (Pacific-time created date) are below. **Apr 12–Jun 2 is unscreened.**

   | Month | major | minor |
   |---|---:|---:|
   | 2026-06 (from 06-03) | 2 | 10 |
   | 2026-07 | 4 | 11 |
   | 2026-08 | 1 | 10 |
   | 2026-09 | 4 | 6 |
   | 2026-10-01..12 | 1 | 1 |

4. **GitHub API (`gh api`):** I listed repos in the `basetenlabs` org created since 2026-03 (36 repos). For Truss, baseten-cli, baseten-switch, basetenkenizer, terraform-provider-baseten, baseten-skills, baseten-bdn and sandbox I recorded licence, fork flag, creation date and in-window release timestamps. Truss has 42 non-prerelease and 37 prerelease releases in the window. `v0.16.2rc0` and `v0.18.31.dev101` are not flagged as prerelease despite their names.
5. **Entity:** [Terms and Conditions](https://www.baseten.co/terms-and-conditions/) (Baseten Labs, Inc.; updated 2026-09-15), the [archived January 30, 2026 terms](https://www.baseten.co/terms-and-conditions-january-30-2026/) (fetched, not diffed), and [about-us](https://www.baseten.co/about-us/).

## C. Segment coverage

| Segment | Sources inspected | Included rows | Gaps |
|---|---|---:|---|
| Apr 12–30 | blog, changelog, Truss releases | 4 | no independent coverage; no status data |
| May | blog, changelog, CLI releases | 4 | no independent coverage; no status data |
| June | blog, changelog, status, Reuters, Dealroom | 7 | MAI partner side not checked |
| July | blog, changelog, status, Switch releases | 4 | no independent coverage |
| August | blog, changelog, status | 2 | thinnest platform month; model-catalog posts excluded |
| September | blog, changelog, status, CLI and Terraform releases, Tekedia, Digital Today | 10 | OpenAI and NVIDIA confirmations missing; law-firm page 403 |
| Oct 1–12 | blog, changelog, status, CLI releases | 6 | Goodfire side not checked |

No segment was empty of first-party evidence. Every segment except June and September lacks independent reporting in what was retrieved.

## D. Inclusion, exclusion and data-validity decisions

- **Included: 37 ledger rows.** Each is one dated source record. Shared `duplicate_event_group` values join the records of one event: Series F (blog + Reuters), the DeepSeek v3.1/MiniMax deprecation (notice + execution), the MCP/skill launch (changelog + blog) and rolling deployments (explainer + default change).
- **Dates:** `published_utc` is the source's **displayed** date. GitHub uses the API `published_at`, and the status page uses the UTC creation date. Baseten's displayed dates appear to follow US Pacific time. The CMS `_publishedAt` in the blog index is **not** used because it records republishes (Loops shows May 8 but its CMS time is Jul 13; Frontier Gateway shows May 6 vs Aug 29; the agentic-optimization post shows Oct 2 vs Oct 6; the NemoClaw post shows Mar 19 vs Apr 16).
- **Excluded as out of window:** the NemoClaw/secure-harness post (displayed 2026-03-19), the Inferless acquihire (2026-02-14), the rolling deployments changelog (2026-03-30), the BDN launch (2026-03-19), and posts dated 2026-10-13 to 10-15 (Gradium TTS, Runway video models, Nemotron 3.5 Super VL, Muse Spark Open).
- **Excluded as low study relevance (context only):** in-window model-availability and tutorial posts, including GLM 5.1/5.2/5.3, Kimi K3, DeepSeek V4 Pro 0813 and V4.1 Flash, Inkling, Nemotron family, TTS/ASR, GPU comparison guides, hiring posts and the CMO appointment. Their changelog dates were still used to compute model-endpoint lifetimes cited in rows 016 and 024.
- **Figures checked against raw page text** (downloaded HTML converted to text and searched, not model summaries): $1.5B/$13B and the lead investors (both sources); 20x/40x growth; 131K+ sequence length; 280+ TPS; 50–60% deploy frequency; 7.5%/57%/"roughly 50%"/89%→97%/320 runs/16 tasks; 25 ms and "up to 5x"; vLLM 0.25.1, "up to 90%" and 2.33x; deprecation dates (May 1, June 17, June 24, July 24, September 25); `b10_` and Oct 1 15:00 UTC; the 5-minute OIDC refresh; the April 17 cache pricing date; incident times and texts; the terms entity name and update date. GitHub dates and licences come from the API.
- **Untrusted instructions observed:** the [connect-coding-agents changelog](https://www.baseten.co/resources/changelog/connect-coding-agents-to-baseten/) contains an install prompt to paste into a coding agent. It was logged and not followed. No other page directives aimed at automated agents were observed.
- **Independence:** Reuters and Dealroom restate the company's funding statement. Digital Today restates Baseten's OpenAI statement. Tekedia is a Blaxel investor. None is an independent test (E3). No row is graded above E2.

A future human reviewer should re-run the planned-but-unexecuted queries, record result totals, fetch partner-side confirmations and screen status incidents before 2026-06-03 (for example through the status page history), and only then upgrade or downgrade confidence.
