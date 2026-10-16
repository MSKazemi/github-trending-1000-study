# StackBlitz / Bolt.new (026): source-query and inclusion log (provisional)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log goes with the [report](026-stackblitz.md) (see its "Standardisation upgrade (2026-10-16)" section) and the [event ledger](026-stackblitz.events.csv) for [#93](https://github.com/MSKazemi/github-trending-1000-study/issues/93). The original [`026-stackblitz.events.json`](026-stackblitz.events.json) is unchanged. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Method:** raw-HTML retrieval with `curl` (generic `Mozilla/5.0` User-Agent; no personal identifier, email or credential sent to any site), text extraction, and a scripted exact-string check of every number, date, price and quote used in a ledger row. Release dates and licences came from the npm registry JSON and `gh api`. Three web searches were run, and the Hacker News Algolia API was used for independent discussion. **This is not exhaustive retrieval.** Search-engine result totals were not exposed, so they are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## robots.txt checks (before any fetch)

| Host | Result | Used? |
|---|---|---|
| bolt.new | `User-agent: *` Allow `/`; Disallow `/~`, `/hosting` | yes (`/blog/*`, `/blog?page=N`, `/pricing`, `/`) |
| support.bolt.new | Disallow `/cdn-cgi/`, `/_next/` only | yes (sitemap and three doc pages) |
| blog.stackblitz.com | Allow `/` | yes (sitemap, RSS) |
| stackblitz.com, webcontainers.io, status.bolt.new, hn.algolia.com | robots.txt returns 404, so no rules | yes. On status.bolt.new (incident.io) only the HTML pages `/`, `/history` and two `/incidents/<id>` pages were fetched, with no `/api/` or `/proxy/` paths |
| registry.npmjs.org | the `/robots.txt` path resolves to an npm package document, with no crawler rules | yes (package JSON) |
| alphasignal.ai | Allow `/` for `*` and explicitly for Claude-User/ClaudeBot; Disallow `/api/` | yes (one article) |
| evilmartians.com | Disallow `/careers/`, `/privacy`, `/cookies` | sitemap only |
| thenewstack.io | **Disallows `anthropic-ai`, `ClaudeBot`, `Claude-Web`** | **not fetched** (a Forge article surfaced in search) |
| pypi.org, sec.gov | not contacted | — |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://bolt.new/sitemap.xml`, `/cms/sitemap.xml` | only homepage, pricing and `use-cases/*` SEO pages, with no blog URLs and no lastmod dates | — |
| 2026-10-16 | all | `GET https://bolt.new/blog` and `/blog?page=2` … `?page=16` (the "Load More" pagination) | 120 unique posts parsed (listing ends at 2025-04-08; pages 14–16 add nothing). 75 dated 2026-04-12…2026-10-14, of which 72 are in the window | 120 / 75 / see below |
| 2026-10-16 | all | `GET /blog/tag/announcements`, `/blog/tag/changelog`, `/blog/tag/security`, `/blog/category/product` | used to separate product announcements from marketing/SEO posts | — |
| 2026-10-16 | all | `GET https://bolt.new/blog/rss.xml` | **HTTP 404**, no feed | — |
| 2026-10-16 | all | `GET https://blog.stackblitz.com/sitemap-index.xml`, `sitemap-0.xml`, `rss.xml` | newest post is dated 2025-06-04, **so there are no in-window posts**. The StackBlitz blog appears dormant and Bolt.new/blog is the active channel | 133 URLs / 0 in window |
| 2026-10-16 | all | `GET https://stackblitz.com/` | links only to the enterprise page and the old blog. No changelog found | — |
| 2026-10-16 | all | `GET https://support.bolt.new/sitemap.xml`; `/account/bolt-forge`, `/building/skills`, `/building/security` | docs carry no publication dates (dateModified 2026-10-14). Used only as corroboration, and no release-notes page exists in the sitemap | 107 URLs / 3 / — |
| 2026-10-16 | all | `gh api orgs/stackblitz/repos`, `orgs/stackblitz-labs/repos` (sorted by push) | new in-window repos: `bolt-slides` (MIT, created 2026-07-14), `bifrost` (Apache-2.0 **fork** of maximhq/bifrost with no release, excluded), `kev-conor-hackathon` (no licence, excluded) | 44 / 12 / 9 |
| 2026-10-16 | all | `gh api repos/<r>/releases` for bolt.diy, pkg.pr.new, alien-signals, sdk, bolt-slides, bifrost, webcontainer-core, stackblitz.zip, use-stick-to-bottom, starters | in-window GitHub releases: bolt.diy v1.0.1 (2026-10-12) and alien-signals v3.2.0 (2026-05-12) only | 2 included |
| 2026-10-16 | all | `gh api repos/stackblitz-labs/bolt.diy/security-advisories`; `gh api advisories?affects=@webcontainer/api` and `?affects=pkg-pr-new` | **none published** | 0 |
| 2026-10-16 | all | `GET https://registry.npmjs.org/@webcontainer/api`, `/alien-signals`, `/pkg-pr-new`, `/@stackblitz/sdk` | version publish times and licence fields | 4 rows |
| 2026-10-16 | all | `GET https://webcontainers.io/enterprise` | commercial-licence condition for production for-profit use (used as the rights cross-check) | — |
| 2026-10-16 | Apr 12–30 | blog `claude-opus-4-7-vs-4-6` (Apr 15) | included as a vendor benchmark claim | 1 |
| 2026-10-16 | May | blog `bolt-microsoft-partnership` (May 5), `bolt-stitch-integration` (May 20) | both included. `save-20k-build-your-business-website-with-ai`, `how-to-create-stunning-websites-with-bolt` excluded as marketing | 4 / 2 / 2 |
| 2026-10-16 | June | 7 blog posts (real-estate series, `is-saas-dying`, `ai-for-small-business`, `ai-built-elearning-platform`) | **all excluded** as marketing/SEO/opinion with no dated product change. No npm or GitHub release in June (pkg-pr-new gap from 0.0.75 on May 19 to 0.0.78 on July 13). **June has no ledger row. This is a finding of this bounded screen, not a zero-activity claim** | 7 / 7 / 7 |
| 2026-10-16 | July | blog `forrester-agentic-development-platforms-landscape`, `introducing-bolt-slides`, `introducing-bolt-new-skills`, `security-audit-on-publish`; `build-custom-software-small-business-ai` excluded | 4 included, plus SDK npm and status record | 5 / 4 / 1 |
| 2026-10-16 | Aug | blog `dictation-bolt-new`, `bolt-open-source-fund-2026`, `prompt-queueing`; 15 other August posts (customer stories `tradeweave`, `netdoctor`, `photos-by-nathan`; SEO explainers such as `what-is-vibe-coding`, `webflow-alternative`) excluded | 3 included, plus 1 status incident | 18 / 3 / 15 |
| 2026-10-16 | Sep | blog `visual-edits`, `what-is-bolt-forge`, `bolt-acquires-dokai`. 23 others excluded (customer stories, `prompting-guide` usage guide, agency/SEO explainers such as `5-best-ai-website-builders-in-2026-ranked-by-capability`) | 3 included, plus 1 secondary report | 26 / 3 / 23 |
| 2026-10-16 | Oct 1–12 | blog `bolt-new-plan-mode` (Oct 1) read: it is a **how-to guide** for an existing mode ("Some Bolt.new help pages also call it Discussion mode"), not a launch, so it was excluded. `test-ai-built-app-before-launch` was read and excluded as a guide. The `*-alternatives` SEO posts (Oct 8–9) and the `ginger-pulse` customer story (Oct 12) were excluded | 0 blog rows. bolt.diy v1.0.1 and the status-history row are included | 11 / 2 / 11 |
| 2026-10-16 | post-window | blog posts dated Oct 13–14 (`5-bubble-alternatives…`, `5-retool-alternatives…`, `how-to-build-app-prototype`); status incidents of Oct 13 and Oct 16 | **excluded** as out of window | — |
| 2026-10-16 | Jul–Oct | `GET https://status.bolt.new/history`, then `/incidents/01KYRYVYTRDBZC39F0EWZNGWSC` and `/incidents/01KZBZVFERM6MHQ80AJT3SK9FM` | history parsed from page-embedded JSON: it starts at 2026-07-15. **April to mid-July status history is not shown (missing, not zero)** | 170 in-window entries / 2 opened. *Spot-check 2026-10-16: an independent re-parse split these 143 dependency mirrors / 27 own entries (first pass: 144/26); CI2026-026-021 corrected* |
| 2026-10-16 | cross-window | HN Algolia `search_by_date` for `stackblitz`, `bolt.new`, `bolt.diy`, `webcontainers`, `bolt forge` (created_at between 1775952000 and 1792022400) | 2 + 3 + 0 + 5 + 8 hits, all with ≤ 10 points. Considered but not ledgered: 2026-05-06 item 48040677 linking an Evil Martians tweet ("Bolt.new's 'AI magic' runs on a Rails app we've been maintaining for 4 years"), because the tweet was not read (x.com not fetched) and stays **E0**. 2026-09-15 item 49706644 is a re-post of a 2024 StackBlitz blog post and was excluded. Show HN "open-source alternative to WebContainers" items (2026-07-28, 2026-08-06) are noted as competitive context only | 18 / 18 / 18 |
| 2026-10-16 | cross-window | web search `Bolt.new StackBlitz 2026 news Forge OR Dokai OR Microsoft OR layoffs OR funding` | only directories, reviews and aggregators (ai.engineer, nevercodealone, superdesign, traeai, neuronfeed). **E0, not used.** The snippet funding figures (Series B $105M, Jan 2025) are pre-window and unverified | unknown / 10 / 10 |
| 2026-10-16 | Sep | web search `"Bolt Forge" Arcee training data opt-in Bolt.new September 2026` | AlphaSignal article fetched raw and **included** as a secondary report. thenewstack.io was **not fetched** (robots disallows Claude agents). producthunt, chatgate, createwith, aitoolly, completeaitraining, productcool and huntscreens were excluded as directories/aggregators | unknown / 10 / 9 |
| 2026-10-16 | May | web search `Google Stitch "Export to Bolt" DESIGN.md May 2026 blog.google OR developers.googleblog.com` | only Bolt pages, Bolt-hosted copies (`*.bolt.host`) and Bolt docs were returned. **No Google-side primary source was found**, so none was used | unknown / 9 / 9 |

## Inclusion, deduplication and conflicts

- **Included:** 22 rows (Apr 12–30: **3**, May: **3**, Jun: **0**, Jul: **6**, Aug: **4**, Sep: **4**, Oct 1–12: **2**). Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Carried forward from `026-stackblitz.events.json`** (byte-identical, not edited): 026-E01 → CI2026-026-006, 026-E02 → CI2026-026-010, 026-E03 → CI2026-026-018 (plus the secondary report CI2026-026-019), and 026-E04 → CI2026-026-020. The `duplicate_event_group` column carries the JSON ID.
- **Duplicate groups:** `026-E03` covers the Forge launch (Bolt blog plus AlphaSignal, which is one event in two documents). `026-status` covers the status records (two single incidents plus the history summary row; the summary's counts include both incidents).
- **Conflicts recorded, not resolved:**
  - (a) The `@webcontainer/api` npm `license` field reads `MIT`, while webcontainers.io/enterprise says production for-profit use needs a commercial licence. The bolt.diy README also points to those commercial terms.
  - (b) AlphaSignal says Bolt "promises" to release the resulting model weights openly. That claim does not appear in the Bolt Forge blog post or the support doc read on 2026-10-16.
  - (c) The Stitch post's title in the earlier report ("Export Google Stitch designs to Bolt in one click") does not appear on the page now. The page shows H1 "Design in Stitch, build in Bolt", og:title "Google Stitch to Bolt: one-click design export", and dateModified 2026-08-17.
- **Figures confirmed against raw text** with a scripted exact-string check of the extracted page text:
  - Opus 4.7: "up to 10%", "7.5 hours".
  - Microsoft: "will be available for direct procurement", "75% of the Fortune 500", "12 months to three to four months", "50 to nearly 70".
  - Security audit: "45 percent", "20 percent"/"57 percent", "74 confirmed vulnerabilities", "two to three minutes", "never touches your tokens".
  - Dictation: "2.93 times".
  - OSS fund: "$1,700/month", "$11,333/month", "27 developers"/"22 developers".
  - Prompt queue: "next five prompts".
  - Visual Edits: "As of September 3, 2026", "free and paid plans".
  - Forge: "September 14, 2026 as a research preview", 92.2/101.0/91%, 50X, October 14, Arcee AI, "StackBlitz may be paid", EEA/UK/Switzerland exclusion, model names, "Claude Opus 5", "$25 a month", "September 21, 2026", "$9/month", "trillion-parameter-class".
  - Dokai: "Terms were not disclosed", "34 days", "roughly half", "late fall".
  - WebContainers enterprise licence sentences.
  - npm/GitHub dates and licences come from API JSON. bolt.diy change and new-contributor counts (118, 12) come from our count of bullets in the release body.
  - All of these remain **vendor or press statements**, not verified measurements.
- **Third-party statistics inside vendor posts** (Veracode, Endor Labs, Georgia Tech, Stanford HAI, ACM 2018) were **not** checked at their origin.
- **Untrusted-content note:** fetched pages were treated as data. No page contained instructions directed at an AI agent or researcher. The incident page asks users to contact support, which is ordinary customer text. Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

- The New Stack Forge article (robots disallows Claude agents, so it was not fetched). The Evil Martians tweet (x.com, not fetched). The Forrester report (gated). Google-side Stitch announcement (not found). Microsoft Marketplace or other Microsoft pages for the Bolt listing (deliberately not accessed). Dokai's own site or any filing confirming the acquisition. Status history before 2026-07-15. Bolt.new terms of service and the Forge data-licence agreement text. GitHub Sponsors records for the OSS fund. Changelogs for `@webcontainer/api` 1.6.4.
- No product was executed, no account created, no paid plan used, no paywall circumvented, no energy measurement.
- **Reproduction:** re-run the requests above with UTC timestamps, save raw HTML hashes, and have an independent human spot-check at least the Forge rows (CI2026-026-018/019), the licence conflict (001, 022), the Microsoft row (004) and the status rows (012, 013, 021) before any evidence is promoted beyond provisional status.
