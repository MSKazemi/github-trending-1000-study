# ServiceNow (082): provisional source-query and inclusion log

> **PROVISIONAL, AI-assisted, not human-reviewed (2026-10-16).** This log accompanies the [report](082-servicenow.md) and [event ledger](082-servicenow.events.csv) for [#150](https://github.com/MSKazemi/github-trending-1000-study/issues/150). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates).

**Accessed:** 2026-10-16.

**Method:**
- Official pages and PDFs were retrieved with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site. No access gate was bypassed.
- Text was extracted locally with `pdftotext` or HTML stripping, and confirmed with `grep`.
- GitHub data came from `gh api`. The npm registry, Hugging Face API, HN Algolia API and NVD CVE API 2.0 were queried without keys.
- One web search was used for the June incident. One WebFetch summary was used for the inaccessible BleepingComputer article; its figures were not used unless they were confirmed in other raw text.
- EDGAR / sec.gov was **not** contacted.

**This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown. No page snapshots or hashes were archived in the repository.

## Query and source log

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://newsroom.servicenow.com/`, `/press-releases/default.aspx`, `/rss`, `/sitemap.xml` | **HTTP 403 Cloudflare "Just a moment..." challenge**; inaccessible to curl. WebFetch of the press-release page returned only navigation (JS-rendered list) | 0 |
| 2026-10-16 | all | `GET https://www.servicenow.com/`, `/company/media/press-room.html`, `/sitemap.xml` | curl timed out (HTTP/2 stream error, then HTTP/1.1 timeouts); WebFetch HTTP 403. **Inaccessible**; product docs site not read directly | 0 |
| 2026-10-16 | all | `GET https://newsroom.servicenow.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=3&pressReleaseDateFilter=3&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=2026&excludeSelection=1` (public Q4 JSON feed; an earlier variant carried an extra `categoryId` parameter, which only narrowed the list) | 236 items for 2026; 143 dated in window. These include press releases and vendor-curated "in the news" links to third-party coverage. Body field empty; `DocumentPath` links to official PDFs on `s205.q4cdn.com` | 143 / ~60 titles screened |
| 2026-10-16 | all | 28 official press-release PDFs from `s205.q4cdn.com` (IDs 3511, 3523, 3525, 3620, 3621, 3624, 3626, 3628, 3632, 3637, 3639, 3640, 3641, 3642, 3643, 3748, 3761, 3786, 3790, 3829, 3830, 3840, 3860, 3863, 3878, 3925, 3941, 3952) | read with `pdftotext`; availability sections grepped | 28 / 28 / 10 not ledgered (3626 Autonomous Security & Risk folded into 009/025 context; 3621 Microsoft preview, 3643 Accenture FDE, 3748 IBM (2H 2026 solutions), 3761 Accenture security services, 3786 TeamViewer, 3829 CMO hire, 3840 Brazil office, 3860 Tech Mahindra, 3863 Aramco, 3878 T-Systems sovereign cloud (German), 3952 Raleigh customer story: partner, customer or corporate items outside the study angle) |
| 2026-10-16 | all | `gh api orgs/ServiceNow/repos?sort=created` | ~17 repos created in window. Included: ServiceNowDocs, Dark-Agent, StarHarness. Excluded: workshop decks (`servicenowbadeck`, `servicenowsdlc`), small research repos (PiSAs, PrivacyAlign, Dr-CiK, behavior-grounding, budget-constrained-web-agents, enhanced-rag-pipeline, agenthorizon, dcvexplainer, xcc-custom-connector-reference), `drflow_old`, and the archived `cube-standard` | 17 / 17 / 14 |
| 2026-10-16 | all | `gh api repos/ServiceNow/sdk` and `/releases` (60); `GET https://registry.npmjs.org/@servicenow/sdk`; release HTML pages v4.6.0, v4.7.0, v4.8.0, v4.11.0 | GitHub releases 4.6.0–4.13.0 (10 in window). npm shows more versions in window (through 4.13.6 on 2026-10-05). npm licence MIT; GitHub licence null | 10 / 10 / 6 folded into report text |
| 2026-10-16 | all | `gh api repos/ServiceNow/ServiceNowDocs` (+ branches, README on `brazil` and `australia`, LICENSE, legal/README); raw markdown `release-notes/` files: available-versions (australia, brazil), build-agent-rn, mcp-server-console-rn, ai-control-tower-rn, agentic-desktop-rn, servicenow-ai-experience-lab-for-vs-code-rn, servicenow-sdk-rn, security-notables (australia, brazil) | Official release notes mirrored as markdown. Used for patch dates, the Brazil EA date and Build Agent / AI Control Tower notes. Security-notable files list hundreds of problem fixes; detailed security patch notes are login-only | 12 files read |
| 2026-10-16 | all | Hugging Face API `models?author=ServiceNow-AI`, `datasets?author=ServiceNow-AI` | **No model created in window** (latest SuperApriel-15B, 2026-04-07, pre-window). Datasets `eva-bench`, `cascade_bench` (06-04), `AgentJudgeBench`, `asr_codeswitched` (04-27) logged and not ledgered | null finding recorded |
| 2026-10-16 | Apr–Oct | NVD CVE API 2.0 `keywordSearch=ServiceNow` (Apr 12–Aug 9 range; the second range returned **HTTP 429**), then `sourceIdentifier` set to the ServiceNow PSIRT CNA identifier (an address-form ID, omitted here) for Apr 12–Aug 9 and Aug 10–Oct 12; `cveId=` for CVE-2026-6875, -18885 and -13016 | 1 + 9 CVEs, grouped by bulletin: KB3137947 (07-13), KB3152242 (08-27), KB3159623 (09-24). NVD detail HTML pages are JS shells, so the API URLs are cited | 10 / 10 / 0 |
| 2026-10-16 | all | HN Algolia `search_by_date` stories: `ServiceNow`, `Apriel`, `Moveworks`, `Armis ServiceNow`, `Now Assist`, `ServiceNow AI`, `ServiceNow vulnerability`, `ServiceNow breach`; stories and comments: `ServiceNow security incident`, `ServiceNow customer data`, `ServiceNow layoffs`, `ServiceNow Knowledge 2026`, `Build Agent ServiceNow`, `ServiceNow MCP` | Main query 16 stories. `Apriel` and `Now Assist` returned fuzzy, irrelevant matches. Leads opened below | — |
| 2026-10-16 | Apr | The Register 04-13 (`servicenow_ai_everywhere`); CNBC 04-23 (`software-stocks-plunge...`) | both read raw and included (**2026-10-16 spot-check: theregister.com robots.txt disallows all paths for generic user agents, so that fetch was against the rule; row 001 is marked unverifiable**). The Register 04-11 Salesforce-vs-ServiceNow piece is **pre-window** (excluded) | 2 / 2 / 0 |
| 2026-10-16 | May | TechTarget 05-05; SiliconANGLE 05-05; The New Stack 05-06; Fortune 05-06 | TechTarget included as a row; SiliconANGLE and The New Stack used as independent check URLs. Fortune is paywalled (`isAccessibleForFree:false`), not used. Fortune 05-05 and the vendor-curated list (CRN, Constellation, Diginomica, Futurum, No Jitter, CIO, etc.) were not opened | ~25 / 4 / 1 |
| 2026-10-16 | Jun | BleepingComputer 06-09 (`servicenow-discloses-security-incident-exposing-customer-data`, and `/amp/`) | **HTTP 403** to curl; WebFetch returned a model summary (published June 9, 2026). It was **not** used as a row source; its figures were cross-checked in raw text below | inaccessible |
| 2026-10-16 | Jun | CPO Magazine 06-17 | **HTTP 403**; inaccessible | 0 |
| 2026-10-16 | Jun | web search `ServiceNow unauthenticated API flaw June 2026 Australia release security update customer instances` | Results: bleepingcomputer, rankiteo, techinformed, triskelelabs, rescana, threatcluster, aviatrix, anavem. Read raw: [Triskele Labs](https://www.triskelelabs.com/resources/servicenow-security-incident-unauthenticated-api-access-exposing-customer-data) (Published Wed 10 June 2026) and [TechInformed](https://techinformed.com/?p=38679) (datePublished 2026-06-15T15:16Z). Aggregators rankiteo, rescana, threatcluster, aviatrix and anavem were snippet-only, **E0**, and not used (including anavem's "variant fix on June 10" claim) | unknown / 9 / 7 |
| 2026-10-16 | Jun | Hugging Face blog `ServiceNow/mosaicleaks` (HN 06-20) | read raw. Published June 18, 2026; included. The arXiv paper it cites was not read | 1 / 1 / 0 |
| 2026-10-16 | Jun | HN "ServiceNow Mass Layoffs [Reddit Thread]" 06-11 | Reddit thread: not a reputable source, **E0**, not opened, not used. The Q2 release shows severance costs in non-GAAP reconciliations but gives no headcount figure | excluded |
| 2026-10-16 | Jul | SiliconANGLE 07-22; CNBC 07-22 (`servicenow-ceo-kill-switch-rogue-ai`) | both read raw; CNBC included as a row, SiliconANGLE as the check URL for Q2 | 2 / 2 / 0 |
| 2026-10-16 | Aug | Reco `city-forum-campaign-salesforce-servicenow` (HN 08-12, 08-14, 09-06) | read raw. datePublished Aug 12, 2026, dateModified Sep 22, 2026; included | 1 / 1 / 0 |
| 2026-10-16 | Aug | Bloomberg 08-21 (buybacks and bluster); HN "pushing customers off SaaS" (Ask HN, 08-19); Ars Technica 08-13 supply-chain story (an HN comment mentioned ServiceNow) | Bloomberg paywalled, not read. Ask HN is not a reputable source. Ars was not opened (only a comment-level lead) | excluded |
| 2026-10-16 | Sep | Security Boulevard 09-07 (OpenAI cyber-defense signatories including ServiceNow) | **HTTP 403**; inaccessible, not used | 0 |
| 2026-10-16 | Sep–Oct | no independent in-window coverage found for Brazil EA, Flow or AI Workflow Factory beyond vendor-curated links (YourStory 09-15, Yahoo Finance 09-11 not opened) | — | — |
| 2026-10-16 | post-window | feed items dated 10-13 (Statement on M&A Misinformation), 10-15 (AI Passport; third-generation employee AI harness); GitHub repos created 10-14/10-15 (`drflow`, `gemma-triton-flash-attn`) | **excluded** as out of window | — |

## Months with thin or no findings

No month was empty.
- **June:** official press output was thin (IBM 06-11, Inspira 06-17, Accenture 06-29), but the security incident, SDK 4.8.0 and MosaicLeaks fill the month.
- **September:** two rows only. The CVE batch and Brazil EA are included; SDK 4.12/4.13 and the Australia patches appear in report text.
- **October 1–12:** three rows.

## Inclusion, deduplication and conflicts

**Included.** 35 rows: Apr 7, May 10, Jun 4, Jul 3, Aug 6, Sep 2, Oct 3. Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.

**Duplicate groups.**
- `082-009`: AI Control Tower vendor release (009) and the TechTarget report of the April 28 demo (010).
- `082-018`: the June incident as reported by Triskele Labs (018) and TechInformed (019). These are two documents about one incident.
- The vendor-curated "in the news" items in the newsroom feed are pointers to third-party coverage of the same announcements. They were not counted as separate events.

**Figures confirmed against raw text** (grep of saved PDF/HTML/JSON):
- Q1 and Q2 results: $3,671M and +22%; $3,877M and +24.5%; ninefold; 123 transactions; 658 customers.
- Armis: "nearly 7 billion devices"; Veza closed March 2.
- Control Tower: "30 new enterprise integrations"; five risk frameworks; GA expected August 2026.
- Build Agent availability lines (GA; April 2026; Q2; Q2; Q3).
- MCP Server "included in every Now Assist and AI Native SKU"; "additional features available 2H 2026".
- Project Arc "early preview"; NOWAI-Bench "available now as an open-source release".
- 2030 target "$30 billion-plus", ">30% of ACV".
- A2A "expected by year end".
- Autonomous Security December 2026 items.
- Flow GA "Q4 2026"; AI Workflow Factory "globally available today".
- CNBC "about 18%" and "more than 30%".
- Register "three levels" of AI pricing (from a robots.txt-disallowed fetch; not re-confirmable, see the report's spot-check).
- TechTarget "preview this month and ship in August".
- Triskele "5 June 2026", "2-3 June 2026", KB3067321.
- TechInformed "April 22", "June 2", KB3067372.
- Reco IP infrastructure "since March 2025", `/api/now/sp/search`, "That is not a platform vulnerability".
- SiliconANGLE "$1 billion in annual contract value".
- NVD CVSS v4 scores, CWE IDs and KB references.
- npm and GitHub release timestamps.
- ServiceNowDocs changelog and available-versions dates.

These remain vendor or press statements, not verified measurements.

**Not confirmed / not used.**
- Figures appearing only in the BleepingComputer WebFetch summary: none beyond what Triskele and TechInformed state in raw text.
- Anavem's "variant fix June 10" (E0).

**Date conflicts recorded, not resolved.**
- ServiceNowDocs: README says created 23 April 2026; GitHub API says 2026-04-29.
- Brazil release-note `last_updated` precedes the EA date.
- npm publish precedes the GitHub release by hours for every SDK version checked.
- The TechTarget demo date (04-28) is earlier than the Knowledge announcement (05-05).

**Licence conflicts.**
- `ServiceNow/sdk`: GitHub null vs npm MIT.
- ServiceNowDocs: Apache-2.0 file vs API NOASSERTION.
- NOWAI-Bench and Dark-Agent have no detected licence.

## Untrusted-content note

Fetched pages were treated as data. ServiceNowDocs' README contains usage tips addressed to readers' AI agents, e.g. "Point your AI at `llms.txt`" and a suggested prompt. One tip also tells Windows readers to run a git configuration command. These were recorded as content; nothing was followed or executed. No fetched page contained instructions directed at this researcher. Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

**Inaccessible:**
- newsroom HTML and RSS (Cloudflare);
- www.servicenow.com, including the docs site and blogs (timeouts / 403);
- ServiceNow support KB bulletins KB3067321, KB3067372, KB3137947, KB3152242 and KB3159623 (login);
- BleepingComputer, CPO Magazine and Security Boulevard (403);
- Fortune and Bloomberg (paywall).

**Not attempted:**
- Reuters;
- Wayback copies;
- filings (EDGAR deliberately not contacted);
- ServiceNow Store listings;
- the developer portal (developer.servicenow.com);
- community forums.

No product was executed, no account was created, no scanning was done and no paywall was circumvented.

**Reproduction:** re-run the requests above, save raw hashes, and have an independent human spot-check at least the incident rows (018, 019), the CVE rows (022, 030, 031), the Build Agent/SDK rows (002, 014, 032) and the licence findings before any evidence is promoted beyond provisional status.
