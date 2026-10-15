# Braintrust (055): dated source queries and inclusion log, 2026-10-16

> **Provisional source-lead screen (2026-10-16):** this search log, the [report](055-braintrust.md) and the [event ledger](055-braintrust.events.csv) are **provisional, AI-assisted documentary source leads** for [issue #122](https://github.com/MSKazemi/github-trending-1000-study/issues/122). **No qualified human has reviewed them.** Factual/link review, source-access/rights review and methods review are all still **pending**. This log is not scientific or security sign-off and does not close issue #122.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Research/source inspection:** 2026-10-16 (UTC calendar day). **Provenance:** an AI web-search tool, direct fetches of public Braintrust pages, and the public GitHub REST API (`gh api`, read-only, unauthenticated-equivalent public data) for `braintrustdata` organization releases, repository creation dates and licence metadata. Each dated event is one row in [055-braintrust.events.csv](055-braintrust.events.csv).

**This is not exhaustive internet discovery.** We did not obtain search-tool result totals, exact query-run UTC times or complete excluded-hit denominators, so they are recorded as **unknown**, not zero. We did not obtain snapshot hashes of third-party pages. The search tool's **session budget ran out** partway through the screen. The last three planned queries (marked below) were **not executed**, and no workaround was used.

## Query log

| Date screened | Segment | Exact query or request | Pages opened/read and decision | Found/screened/excluded counts |
|---|---|---|---|---|
| 2026-10-16 | all segments (official) | WebFetch `https://www.braintrust.dev/docs/changelog` (read in four 100k-character offsets) | Read the official changelog. It uses **month headings only**, with no day dates, covering Feb 2026 to Oct 2026 in detail. Its items cannot satisfy the ledger's day-level `published_utc` without inventing a day, so they are used as **corroboration** (`independent_check_url`) and narrative context and are **not** ledger rows. The April 2026 month block cannot be split at Apr 12, so April changelog items such as "Sandboxes for agent evals (public preview)" are **unresolved** as to in-window status. | unknown (one page) |
| 2026-10-16 | all segments (official) | WebFetch `https://www.braintrust.dev/blog` | Blog index with displayed dates from 2026-04-03 to 2026-10-15. 27 posts are listed. Dated product posts were opened individually (below). Posts dated Apr 3, Apr 6 and Apr 8 are **pre-window**. The Oct 15 "workflow evals" post is **post-window**. | 27 listed / 20 opened / see decisions |
| 2026-10-16 | all segments (official OSS) | `gh api orgs/braintrustdata/repos?per_page=100&sort=pushed`; `gh api orgs/braintrustdata/repos?per_page=100` filtered `created_at >= 2026-03-01` | Repository licences (SPDX metadata), archive state and creation dates. Used for the rights baseline. Repository creation is **not** treated as a publication event. | first page of 100 repositories only; further pages not listed |
| 2026-10-16 | Apr 12–30 | `gh api repos/braintrustdata/braintrust-sdk-python/releases` (window filter); `.../braintrust-sdk-javascript/releases`; `.../bt/releases` (pages 1–4, stable only) | Included py-sdk-v0.15.0 (Apr 14), bt v0.5.0 (Apr 15) and braintrust@3.9.0 (Apr 20). Other April releases (py 0.16–0.18, bt 0.6–0.8) were **screened, not itemized**. | Python 36 / JS core (`braintrust@`) 32 / bt stable 34 GitHub releases in window by `published_at` UTC; most not itemized |
| 2026-10-16 | Apr 12–30 | WebFetch blog posts `/blog/ai-compliance-governance` (Apr 13), `/blog/stakeholder-trust-evals-observability` (Apr 28) | Both are **guidance/educational** with no product release. **Excluded** from the ledger and noted in the report. | 2 opened / 0 included |
| 2026-10-16 | May | `Braintrust AI evaluation observability 2026 funding OR launch OR acquisition` | Returned Series B coverage (SiliconANGLE 2026-02-17, opened). It is **pre-window baseline**, not a ledger row. Aggregators (pulse2, texxr, parsers.vc, neuronfeed, simplify) were **not opened** because they duplicate the same news. | unknown |
| 2026-10-16 | May | `"Braintrust" AI evals news May 2026 OR June 2026 OR July 2026` | Returned a competitor comparison page (atlan.com) that mentions a May 2026 AWS incident. It was **not used as evidence** because it comes from a competitor; it served as a lead. A Voiceflow review was not opened. | unknown |
| 2026-10-16 | May | `braintrust.dev security incident OR vulnerability OR advisory 2026` | Leads to the May 2026 AWS-account incident. The aggregator, French and Spanish reposts were **not used**. | unknown |
| 2026-10-16 | May | `"Braintrust confirms breach" rotate keys TechCrunch` | Opened the [TechCrunch 2026-05-06 article](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/). **Included** as row 004. | unknown |
| 2026-10-16 | May | `site:braintrust.dev security incident May 2026 API keys AWS` | Returned no braintrust.dev page. Opened [SecurityWeek 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/) (**included**, row 005, same duplicate group) and [Security Affairs 2026-05-09](https://securityaffairs.com/191888/data-breach/braintrust-security-incident-raises-concerns-over-ai-supply-chain-risks.html) (used as `independent_check_url`). Both cite the vendor notice `trust.braintrust.dev/updates`. | unknown |
| 2026-10-16 | May | WebFetch `https://trust.braintrust.dev/` and `https://trust.braintrust.dev/updates` | **Inaccessible content.** Only the page title rendered (a client-side app), so the primary vendor incident notice is **not directly verified** in this screen. | 2 attempted / 0 readable |
| 2026-10-16 | May | `Braintrust AWS incident root cause update postmortem 2026` | No root-cause postmortem was found. A status-aggregator lead mentions a 2026-06-12 US data-plane outage, but `status.braintrust.dev/history` returned HTTP 404, so the outage is **unverified and excluded**. | unknown |
| 2026-10-16 | May | WebFetch `/blog/multi-turn-scoring` (May 14), `/blog/human-review-golden-datasets` (May 21), `/blog/six-generations-ai-agents` (May 21) | All three are **guidance**. **Excluded** as events. The May 11 post "traces and evals same place" was **not opened**. | 3 opened / 0 included |
| 2026-10-16 | June | WebFetch `/blog/topics-ga` (Jun 1), `/blog/topics-architecture` (Jun 4), `/blog/any-framework-any-provider` (Jun 16), `/blog/braintrust-for-startups` (Jun 30) | Included Topics GA, Topics architecture disclosure and the startups program. The Jun 16 post is **guidance** and was excluded. The Jun 1 "active observability" and Jun 26 "stateful agent evals" posts were **not opened**. | 4 opened / 3 included |
| 2026-10-16 | June | `gh api repos/braintrustdata/autoevals/releases` (window filter) | Included autoevals py-0.3.0 (Jun 9). js-0.3.0 from the same day is a duplicate, used as `independent_check_url`. | 4 releases in window / 2 included |
| 2026-10-16 | July | WebFetch `/blog/brainstore-phrase-search` (Jul 7), `/blog/behavior-specs` (Jul 29); `gh api repos/braintrustdata/agentbehavior`; WebFetch `https://www.agentbehavior.dev/` | Both posts were included. The agentbehavior repository reports Apache-2.0 and was created 2026-06-08. The site itself states no licence, version or date. | 2 opened / 2 included |
| 2026-10-16 | August | WebFetch `/blog/cloudflare-agents` (Aug 5), `/blog/harbor-agent-evals` (Aug 24), `/blog/braintrust-mcp` (Aug 26); `gh api .../braintrust-sdk-javascript/releases/tags/@braintrust/otel@1.0.0` | All four were included. | 4 opened / 4 included |
| 2026-10-16 | September | WebFetch `/blog/active-observability-loop-patterns-debugger` (Sep 3), `/blog/evaluate-agent-responses-with-jev` (Sep 18), `/blog/patterns-topics-loop-faq` (Sep 23), `/blog/nitro` (Sep 24), `/docs/observe/patterns/index` | Four rows were included, and the Patterns docs page serves as the preview-label check. | 5 opened / 4 included |
| 2026-10-16 | September | `Braintrust Loop Patterns Debugger public preview September 2026 agent observability` | Returned only Braintrust's own blog and docs pages. **No independent coverage** was surfaced. | unknown |
| 2026-10-16 | Aug–Oct | `"Braintrust" eval platform partnership OR integration announcement August 2026 OR September 2026 OR October 2026` | No in-window partnership announcement was surfaced. The results were the seed-round post (pre-window), CrewAI docs (undated integration), Azure Marketplace listing and review sites, none of which was included. | unknown |
| 2026-10-16 | Oct 1–12 | WebFetch `/blog/coding-agent-insights` (Oct 7), `/blog/application-logs` (Oct 8); `gh api` JS braintrust@3.37.0 (Oct 5) and autoevals py-0.4.0 (Oct 7) | All four were included. The [Oct 15 workflow-evals post](https://www.braintrust.dev/blog/workflow-evals) is **excluded as out-of-window**. | 4 opened / 4 included |
| 2026-10-16 | cross-window | `"Braintrust" "behavior specs" Basis agentbehavior.dev` | **NOT EXECUTED**: the search budget was exhausted. | not run |
| 2026-10-16 | Oct 1–12 | `Braintrust AI observability news October 2026` | **NOT EXECUTED**: the search budget was exhausted. Independent October coverage is unknown. | not run |
| 2026-10-16 | Apr 12–30 | `Braintrust sandboxes agent evals public preview April 2026 Modal Lambda` | **NOT EXECUTED**: the search budget was exhausted. The in-window status of the April sandbox preview is unresolved. | not run |

### Inclusion, exclusion and validity decisions

- **23 ledger rows are included.** Each is one dated publication: a vendor blog post, an official GitHub release or an independent press article. Several rows share a `duplicate_event_group`, so rows are **not** independent confirmations:
  - TechCrunch and SecurityWeek report **one** incident.
  - Topics GA and Topics architecture describe one feature.
  - The Brainstore phrase-search and Nitro rows cover one storage engine.
  - The two autoevals rows are one library.
  - The Python and JS trial-count rows are one capability.
- **Per-segment counts:** Apr 12–30: 3; May: 2; Jun: 4; Jul: 2; Aug: 4; Sep: 4; Oct 1–12: 4. These are a **purposive selection** of material events, not a release census. For example, 36 Python SDK, 32 JS core-SDK and 34 stable `bt` CLI GitHub releases fall in the window, and most were not itemized. Thin months reflect selection and the source shape (the changelog is month-only), so they should **not** be read as lower activity.
- **Excluded:**
  - Pre-window: blog posts dated Apr 3, 6 and 8, and the Feb 17 Series B.
  - Post-window: the Oct 15 workflow-evals post.
  - Guidance-only posts: Apr 13, Apr 28, May 14, May 21 ×2 and Jun 16.
  - Unverified leads: the Jun 12 status-page outage (only aggregator evidence; the status page returned 404) and third-party lists of allegedly affected customers.
  - Competitor and aggregator pages, including Atlan, Rescana, threat-feed clusters and foreign-language reposts.
- **Primary vs independent:**
  - Vendor blogs and release notes support E1/E2 claims about what Braintrust **published**.
  - TechCrunch and SecurityWeek are independent reports of a vendor-confirmed incident, relaying vendor statements. They are not a forensic audit.
  - No independent product benchmark, adopter study or neutral evaluation of Topics or Patterns accuracy was found.
- **Access:** only public pages and the public GitHub API were used. There was no login, paywall bypass, scraping of github.com/trending or access to personal data. Individual contributor handles in release notes are **not** recorded.

A future independent reviewer should:

- re-run these queries with UTC timestamps and result counts;
- run the three unexecuted queries;
- retrieve the Trust Center notice through a browser;
- resolve the April changelog items at day level;
- spot-check every ledger URL before issue #122 is closed.
