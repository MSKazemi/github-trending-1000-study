# Browser Use (054) — provisional dated source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (2026-10-16):** this search log, the [report](054-browser-use.md) and the [event ledger](054-browser-use.events.csv) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**. Factual/link review, source-access/rights review and methods review remain **pending**. They do not close issue #121.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Research and source inspection:** 2026-10-16.

**Provenance:** this log draws on three source types:
- a public web-search tool;
- direct reading of official dated pages ([changelog](https://browser-use.com/changelog), [blog index](https://browser-use.com/posts) and individual posts);
- read-only GitHub REST API calls via `gh api`, for repository metadata, releases, commits, repository security advisories and the global advisory database.

The GitHub API calls are listed in the table because they are reproducible.

**Limits:**
- This is **not exhaustive internet discovery**.
- Search-tool result totals, query-run UTC times and full excluded-hit denominators are unavailable. They are recorded as **unknown, not zero**.
- No page snapshots or hashes were captured.
- **The session's web-search budget was exhausted** before the planned independent-evaluation query, so independent coverage is under-searched.

## Query log

| Date screened | Segment | Exact recorded query or API call | Source pages opened/read and decision | Found/screened/excluded counts |
|---|---|---|---|---|
| 2026-10-16 | all (identity) | Direct read: `https://browser-use.com/` | Homepage: offerings, "© 2026 Browser Use", undated "SUPERFAST mode" waitlist. Identity baseline only; no ledger row | n/a |
| 2026-10-16 | all (identity/rights) | `gh api repos/browser-use/browser-use` | MIT, created 2024-10-31, not archived. Used for the rights baseline | n/a |
| 2026-10-16 | all | `gh api "repos/browser-use/browser-use/releases?per_page=100" --paginate` (filtered to `published_at` ≥ 2026-03-25) | 15 in-window releases, 0.12.7 to 0.13.11. **Included:** 0.12.7, 0.12.8, 0.13.0, 0.13.3, 0.13.8, 0.13.10, 0.13.11. **Used as corroboration:** 0.13.5, 0.13.9. **Not itemised:** 0.12.9, 0.13.1, 0.13.2, 0.13.4, 0.13.6, 0.13.7. 0.12.6 (2026-04-02) excluded as pre-window | 17 listed since 2026-03-25 / 15 in window / 7 rows |
| 2026-10-16 | all (security) | `gh api repos/browser-use/browser-use/security-advisories`; `gh api "advisories?ecosystem=pip&affects=browser-use"` | Only GHSA-x39x-9qw5-ghrf / CVE-2025-47241 (2025-05) and its duplicate. **Excluded as out-of-window.** No in-window reviewed advisory found | 2 found / 0 in window |
| 2026-10-16 | all (OSS footprint) | `gh api "orgs/browser-use/repos?per_page=100&sort=created"` (created ≥ 2026-03-01) | New in-window repos include browser-harness (04-17, MIT), bux (04-26, MIT), benchmark updates, browser-use-pi (09-05, MIT), browser-worlds-tinker-rl (08-08, Apache-2.0). Only the harness, bux and benchmark are cited. Repo creation alone is not a product event | first page of 100 only; unknown beyond |
| 2026-10-16 | all | `gh api "repos/browser-use/browser-harness/releases"` | First tags v0.1.1rc1/v0.1.1 on 2026-06-21, v0.1.4 on 2026-07-01. Used in the availability note for CI2026-054-002 | n/a |
| 2026-10-16 | Apr 12–Oct 12 | `gh api "repos/browser-use/benchmark/commits?since=2026-04-12…&until=2026-10-12…"`; `gh api repos/browser-use/benchmark` | V2 added 08-26, task encryption docs 09-09, seven-case correction 09-24, V2.1 metadata 09-25. **No LICENSE file** (`license: none`). Two commit rows included | ~45 commits listed / 2 rows |
| 2026-10-16 | Apr 12–30 | Direct read: `https://browser-use.com/changelog`, `https://browser-use.com/posts` | Changelog 2026-04-12 entry **included**. 04-03 entry and Apr 9 free-tier post **excluded** (pre-window). Posts opened: Apr 13 reverse-CAPTCHA (excluded, retired non-product experiment), Apr 19 harness (included), Apr 25 BUX (included) | 50 posts on index / 3 in segment / 2 rows (+1 changelog) |
| 2026-10-16 | Apr 12–30 | `"Browser Use" browser agent 2026 announcement` | Results were mostly aggregator/tweet mirrors (traeai.com, thursdai.news, aitoolsatlas.ai). **Excluded** as unverifiable secondary relays; they pointed back to official channels | unknown |
| 2026-10-16 | Apr 12–30 | `news.ycombinator.com Browser Harness "browser-use" 2026` | Opened the [hn.svelte.dev mirror](https://hn.svelte.dev/item/47890841), the canonical [HN item](https://news.ycombinator.com/item?id=47890841) and the official HN API `https://hacker-news.firebaseio.com/v0/item/47890841.json` (time → 2026-04-24T14:31:38Z, 134 points, 66 descendants). **Included** as an E0 community lead. Commenter identity is deliberately not recorded | unknown |
| 2026-10-16 | May | Blog index; opened May 5 "Everything I got wrong" and May 9 production architecture | May 9 **included**. May 5 **excluded**: internal engineering retrospective with no product, OSS or direction statement | 2 posts in segment / 1 row |
| 2026-10-16 | May | GitHub releases (above) | 0.12.7 (security hardening) and 0.12.8 (in-release reverts) **included**. 0.12.9 not itemised | see releases |
| 2026-10-16 | June | Blog index; opened Jun 10 BU Bench and Jun 15 Firecracker | Both **included**. Jun 10 "fetch-use" scraping-program post not opened (not screened) | 3 posts in segment / 2 rows |
| 2026-10-16 | June | `BrowserArena leaderboard cloud browser providers Browser Use Browserbase reliability`; direct read `https://notte.cc/arena` | Notte-operated page, **undated**: Browser Use rank 6, 99.0%, 4,538 ms, $0.06/hr. Used as **contrary evidence** in the limitation of CI2026-054-010, not as its own row (no in-window date) | unknown |
| 2026-10-16 | July | Changelog (07-01, 07-17, 07-20); blog: Jul 1 QA, Jul 12 AgentCore | 07-01 changelog merged with the v0.13.3 release (one event). 07-17 **included**. 07-20 read but **not itemised** (recording default/OAuth scope). QA and AgentCore posts **included** | 3 changelog + 2 posts / 4 rows |
| 2026-10-16 | August | Changelog (08-10, 08-17, 08-24); blog: Aug 5, Aug 6, Aug 26 | 08-17 and 08-24 **included**, 08-10 read but not itemised. Aug 5 judge-variance, Aug 6 x402 and Aug 26 RL-environment posts **included**. v0.13.8 included | 3 changelog + 3 posts / 7 rows |
| 2026-10-16 | September | Blog: Sep 3 Link, Sep 15 bitter lesson, Sep 21 Composio, Sep 21 Vesta | Sep 3 and Sep 15 **included**. Composio and Vesta read but **excluded from the ledger** as vendor-hosted customer testimonials with no verifiable metrics. Sep 7/14/21/25 explainer/comparison posts not opened (SEO content). Changelog: no September entry shown | 8 posts in segment / 2 rows (+ v0.13.10 and the benchmark correction) |
| 2026-10-16 | Oct 1–12 | `"Browser Use" October 2026 browser agent Claude toolset OR "anthropic.tools.browser"`; direct reads of `https://docs.browser-use.com/open-source/customize/integrations/toolsets-for-claude` and `https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool`; The New Stack result opened but truncated (no date or body) | v0.13.11 (Oct 7) **included**. Anthropic's "Browser use tool" recorded as a **name collision**, not a Browser Use event. Oct 1/6/7/12 posts **excluded** (listicle/how-to/glossary). Oct 15 post **excluded** (out of window). The docs page contained agent-directed instructions, treated as data and not followed | unknown |
| 2026-10-16 | cross-window (funding/ownership) | `Browser Use startup Magnus Müller Gregor Zunic 2026 funding OR raises OR acquisition` | Only March 2025 seed-round coverage surfaced. **Excluded** as pre-window baseline. No in-window ownership event found (not proof of absence) | unknown |
| 2026-10-16 | cross-window (security) | `"browser-use" vulnerability OR CVE OR "prompt injection" 2026` | No browser-use-specific in-window CVE surfaced. Results concerned other AI browsers. **Excluded** | unknown |
| 2026-10-16 | cross-window (independent press) | `"Browser Use" techcrunch OR "the register" OR venturebeat OR theverge 2026 web agent` | Only 2025 TechCrunch items and 2026 vendor/listicle pages. **No in-window independent press found** | unknown |
| 2026-10-16 | cross-window | `site:browser-use.com/posts 2026` | Site operator returned no official pages. Superseded by the direct blog-index read | unknown |
| 2026-10-16 | cross-window | `"Browser Harness" Browser Use open source CDP coding agents` | Third-party directory/aggregator listings (jimmysong.io, sourcepulse, PyPI mirrors). Used only to locate the Show HN thread. **Not cited** | unknown |
| 2026-10-16 | baseline | `"bu-30b-a3b-preview" Browser Use model Hugging Face` | Model originates from a 2025-12-16 changelog. **Excluded** as out-of-window | unknown |
| 2026-10-16 | cross-window (independent evaluation) | `arxiv 2026 evaluation "browser-use" agent framework benchmark comparison WebVoyager Online-Mind2Web` | **Not executed**: the web-search budget for the session was exhausted. Recorded as a coverage gap | not run |

### Inclusion, exclusion and data-validity decisions

- **Included:** 26 ledger rows. Segment counts: Apr 12–30 = 4, May = 3, Jun = 3, Jul = 4, Aug = 7, Sep = 4, Oct 1–12 = 1. No segment is empty, but **October has only one verifiable product event**, and the vendor changelog shows no entries after 2026-08-24.
- **Duplicates:**
  - CI2026-054-002 and -003 share group 054-002 (the harness launch and its community discussion).
  - The three benchmark rows (-020, -021, -025) share group 054-020; the Jun 10 BU Bench V1 post (-009) is kept separate.
  - The Jul 1 changelog and the v0.13.3 release are recorded as one row.
- **Status classes:**
  - shipped 14;
  - reported_undetermined 7 (self-benchmarks, methods/direction posts, community lead, externally blocked integration);
  - preview 1 (Rust beta);
  - reversed/cancelled 2 (v0.12.8 in-release revert; v0.13.8 default model);
  - corrected 2 (BYOK billing; benchmark task contracts).
- **Primary vs independent:**
  - All rows except the Show HN thread are first-party.
  - GitHub releases and commits are E2 reproducible documents of *what was published*, not evidence of functional quality.
  - No E3/E4 independent evaluation was found within the budget.
- **Out-of-window exclusions:**
  - 2026-04-03 changelog (free tier/pricing);
  - 2026-04-02 release 0.12.6;
  - 2026-04-09 free-tier post;
  - 2025-05 GHSA-x39x-9qw5-ghrf;
  - 2025-12 bu-30b-a3b-preview;
  - 2026-10-15 Firecrawl comparison.
- **Access and ethics:**
  - Only public pages and unauthenticated or read-only GitHub API calls were used.
  - No login, paywall, private advisory, network scan, product signup or participant data was involved.
  - github.com/trending was not accessed.
  - HN commenter handles are not recorded, apart from the public submitter handle shown on the item.
- **Next steps for review:** a future independent reviewer should:
  - re-run these queries with recorded result totals and UTC times;
  - spot-check the paraphrased release notes and blog figures;
  - complete the missing independent-evaluation search before any issue closure.
