# Zed Industries (024) — provisional dated source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (upgraded 2026-10-16):** this search log, the [report](024-zed-industries.md), the [event ledger](024-zed-industries.events.csv) and the [source-QC note](024-zed-industries.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads** for [issue #91](https://github.com/MSKazemi/github-trending-1000-study/issues/91). They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #91 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Window:** 2026-04-12…2026-10-12 inclusive. **Research/source inspection:** 2026-10-16 (single session; exact UTC times per query not recorded). **Provenance:** direct reading of the official [Zed blog index](https://zed.dev/blog) and individual posts; read-only GitHub REST API calls (`gh api`) for `zed-industries/zed` releases, security advisories, root contents, README licensing text, the commit history of `LICENSE-AGPL` and PR #57948, plus `agentclientprotocol/agent-client-protocol` releases and licence; three general web searches (provider-ranked; result totals not exposed). **This is not exhaustive internet discovery.** Result totals and complete excluded-hit denominators are **unknown**, not zero. No page snapshots or hashes were stored. The earlier first pass recorded only one targeted query (`site:zed.dev/blog 2026 "parallel agents" "sandboxing" "Delta public beta"`); it is preserved in the [report's earlier-screen section](024-zed-industries.md#earlier-screen-preserved). No older separate search-log file existed for 024.

## Official index screens (one fetch each on 2026-10-16)

| Source | What was read | In-window items | Notes |
|---|---|---:|---|
| [Zed blog index](https://zed.dev/blog) | titles, displayed dates, slugs | 19 posts dated Apr 12–Oct 12 (Apr 12–30: 3; May: 7; Jun: 5; Jul: **0**; Aug: 2; Sep: 2; Oct 1–12: **0**) | Apr 9 "Agent Metrics" and Apr 7 "How We Developed Zeta2" **excluded** (pre-window). No July or early-October blog post was listed — those segments rely on release notes. |
| GitHub API `repos/zed-industries/zed/releases` (paginated, 1,311 releases returned) | tag, `published_at`, prerelease flag | 57 stable (non-prerelease) releases and 67 prereleases with `published_at` in window | Stable tags run v0.232.2 (Apr 15) → v1.0.0 (Apr 29) → v1.23.3 (Oct 12). Release bodies read for v1.9.0, v1.10.0, v1.12.0, v1.14.2, v1.18.0, v1.22.0, v1.23.2 only. |
| GitHub API `repos/zed-industries/zed/security-advisories` | GHSA id, CVE, severity, `published_at`, patched range | 5 advisories published 2026-05-08; 0 others in window | 7 earlier advisories (Aug 2025–Feb 2026) **excluded** as pre-window baseline. |
| GitHub API `repos/agentclientprotocol/agent-client-protocol` (+ releases) | licence, tags, `published_at` | 53 release objects in window (library and schema tags; v0.11.6 Apr 14 → v1.11.0 Oct 9) | Only v1.0.0 (Jun 24) used as a row; the rest counted, not individually screened. |

## Per-segment log of fetches/queries actually run

| Segment | Exact query or fetch | Pages opened and decision | Found/screened/excluded |
|---|---|---|---|
| Apr 12–30 | fetch [parallel-agents](https://zed.dev/blog/parallel-agents) | QC of existing row -001: ok | n/a |
| Apr 12–30 | fetch [zed-1-0](https://zed.dev/blog/zed-1-0); `gh api` release v1.0.0 date | Included **-006** | n/a |
| Apr 12–30 | web search `"Zed 1.0" editor release April 2026` | Results (search-result leads only): [Phoronix](https://phoronix.com/news/Zed-1.0-Released) — opened, **HTTP 403**, not usable; [zed.dev/releases/stable/1.0.0](https://zed.dev/releases/stable/1.0.0) listed in results (not opened; GitHub API date used instead); dealroom/blog/aggregator pages **excluded** (secondary or unverifiable). Some aggregators gave Apr 30/May 1 dates — contradicted by the vendor and GitHub release date (Apr 29). | unknown |
| Apr 12–30 | blog index | Apr 27 "Community Champion Spotlight" **excluded** (community profile, not a product event) | n/a |
| May | fetch [releases/stable/1.3.5](https://zed.dev/releases/stable/1.3.5) | QC of existing row -002: ok | n/a |
| May | fetch [zed-for-business](https://zed.dev/blog/zed-for-business), [zeta2-1](https://zed.dev/blog/zeta2-1), [terminal-threads](https://zed.dev/blog/terminal-threads), [anthropic-subscription-changes](https://zed.dev/blog/anthropic-subscription-changes) | Included **-008, -007, -012** (deduplicated with -002), **-014** | n/a |
| May | `gh api repos/zed-industries/zed/security-advisories` + per-advisory detail for GHSA-63qj, GHSA-fj2r and list detail for GHSA-c3g6/-rqq3/-c99f | Included **-009, -010** (groups three terminal-allowlist advisories), **-011** | 5 in window / 5 screened / 0 excluded |
| May | `gh api repos/zed-industries/zed/contents/`, README licensing text, `commits?path=LICENSE-AGPL`, `pulls/57948` | Included **-013** (AGPL→GPL relicensing merged May 28) | n/a |
| May | blog index | May 5 "We're Not Building AI Features for the Money", May 15 "Use Your ChatGPT Subscription in Zed", May 19 "Why and How to Run Local Models in Zed" **not opened** (titles only; lower priority) | 3 not opened |
| June | fetch [introducing-deltadb](https://zed.dev/blog/introducing-deltadb), [github-copilot-usage-based-billing](https://zed.dev/blog/github-copilot-usage-based-billing) | Included **-016**, **-015** | n/a |
| June | `gh api` ACP repo licence and releases; v1.0.0 body | Included **-018** (low confidence; org stewardship unverified) | 53 release objects in window; 1 used |
| June | blog index | Jun 2 Community Champions, Jun 16 Zed Guild retrospective, Jun 23 Hidden Gems Part 4 **not opened** (community/tips posts) | 3 not opened |
| July | `gh api` release bodies v1.9.0, v1.10.0, v1.12.0 | Included **-019, -017, -020**. No July blog post exists on the index. | 9 stable releases in July; 3 read |
| August | fetch [sandboxing](https://zed.dev/blog/sandboxing), [introducing-delta](https://zed.dev/blog/introducing-delta) | QC of existing rows -005 and -003: ok | n/a |
| August | `gh api` release body v1.14.2 | Included **-022** (same group as -005) | 8 stable releases in Aug; 1 read |
| September | fetch [delta-public-beta](https://zed.dev/blog/delta-public-beta), [agentic-xanadu](https://zed.dev/blog/agentic-xanadu) | QC of existing row -004: ok; included **-021** | n/a |
| September | `gh api` release bodies v1.18.0, v1.22.0 | Included **-023** (v1.22.0); v1.18.0 read but **not included** (model-list and UI changes; lower relevance) | 7 stable releases in Sep; 2 read |
| September | web search `Zed Delta DeltaDB "pull requests" review 2026` | Opened [The New Stack](https://thenewstack.io/zed-delta-github-alternative/) — page body truncated, no date/author shown; recorded as **search-result lead only**, not a row. Other results (zeli.app, runtimewire, labmemo, plushcap) are summaries of Zed's posts; **not opened/excluded**. A search-summary claim that Zed engineers merged 570 changes without PRs was **not verified** on a primary page and is not used. | unknown |
| Oct 1–12 | `gh api` release body v1.23.2 | Included **-024**. No in-window October blog post on the index. | 2 stable releases Oct 1–12 (v1.23.2, v1.23.3); 1 read |
| identity | web search `Zed Industries funding OR acquisition 2026` | No 2026 funding/acquisition result for Zed Industries; one Aug 2025 Business Wire result (Series B, Sequoia-led) is **pre-window** and was not opened. Other "Zed" companies **excluded**. | unknown |

### Not executed (logged to respect the shared search budget)

- `"Zed" CVE-2026-44465 OR CVE-2026-44463 independent analysis` — not executed; advisory facts taken from the vendor's GitHub advisories.
- `"Agent Client Protocol" JetBrains OR Neovim adoption 2026` — not executed; third-party ACP adoption remains **unknown**.
- `Zed editor outage OR incident 2026` — not executed; incidents **unknown**, not zero.
- `site:zed.dev/blog "July" 2026` — not needed: the official index lists no July post.
- Company registry / ownership filing lookup — not executed (would need registry access); ownership stays **unverified**.

### Inclusion, exclusion and data validity decisions

- **Ledger: 5 → 24 rows.** Per segment (by `published_utc`): Apr 12–30: 2; May: 9; Jun: 3; Jul: 3; Aug: 3; Sep: 3; Oct 1–12: 1. Every segment has at least one verifiable dated official record. The ledger is a purposive selection, not a census: 57 stable releases appeared in the window.
- **Deduplicated:** -002 and -012 (same Terminal Threads feature: release note and blog post) share `024-2026-05-20-zedstable`; -005 and -022 (sandboxing blog and v1.14.2 release note) share `024-reconciled-5`; the three May 8 terminal-allowlist advisories are one row (-010). DeltaDB (-016) → Delta private beta (-003) → Delta public beta (-004) → stated direction essay (-021) are separate stages, not repeats.
- **Availability classes:** Delta private/public beta = `preview`; DeltaDB Jun 11 and the Sep 1 essay = `announced_only`; third-party billing notices = `reported_undetermined`; advisories = `corrected` (fixes in versions released before the window; disclosure in window).
- **Primary vs independent:** all rows are first-party (Zed blog, Zed release notes, Zed GitHub advisories/PRs) except -018 (ACP organization; relationship to Zed unverified). No independent test, audit or neutral report was successfully opened; **no E3 evidence**.
- **Exclusions (out of window):** Apr 7 and Apr 9 blog posts; advisories published Aug 2025–Feb 2026; Aug 2025 Series B; versions listed after Oct 12 (e.g. the 1.24.x series seen on the release page).
- **Untrusted content:** advisory texts include reporter messages addressed to the Zed team; nothing addressed to AI agents was found in fetched pages.
- **Review access:** public pages and public API metadata only; no login, paywall, private dashboard, exploit testing, participant data or github.com/trending access. No email or personal identifier was sent in any request.
