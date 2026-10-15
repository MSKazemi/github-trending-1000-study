# Bubble — provisional six-month technology intelligence screen (028)

> **PROVISIONAL INITIAL EVIDENCE SCREEN (2026-10-16), AI-assisted and not reviewed by a qualified human.** This report, its [event ledger](028-bubble.events.csv) and its [search log](028-bubble.search-log.md) are **documentary source leads**. They are not a verified chronology, product test, license determination or empirical reuse result. Factual/link review, source-access/rights review and methods review are all **pending**. The report does not close [issue #95](https://github.com/MSKazemi/github-trending-1000-study/issues/95), and no `NEWS-YYYY-NNNN` items for [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) should be minted from it until a human reads and verifies each source.

- **Company watchlist ID:** 028 ([watchlist](../../../docs/AI_SOFTWARE_COMPANIES_100_WATCHLIST_2026-10-12.md)).
- **Research issue:** [#95](https://github.com/MSKazemi/github-trending-1000-study/issues/95). Linked corpus initiative: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see section 2. The entity is Bubble Group, Inc.; no in-window ownership change was found, but this was not checked at filing level.
- **Product URL and company channels:** [bubble.io](https://bubble.io/), [release notes](https://bubble.io/release-notes), [blog](https://bubble.io/blog/), [forum announcements](https://forum.bubble.io/c/announcements/9), [status page](https://status.bubble.io/) (no history rendered), [terms](https://bubble.io/terms), [GitHub org bubblegroup](https://github.com/bubblegroup).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were read on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional). **34 dated source rows** cover all seven calendar segments. The rows are a purposive sample, not a census of Bubble releases. Methods: [screening protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [template](../../../templates/company_six_month_intelligence.md).
- **Claim grading:** company-watch E0–E4 tiers, which are distinct from the [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

The full query table, inaccessible sources and exclusions are in the [search log](028-bubble.search-log.md). In summary:

- **What was searched:** one web-search tool plus direct fetches of the release notes, the forum Announcements category, the blog index, the terms page and the GitHub API. Search-engine result counts and run timestamps were not exposed or recorded, so they are **unknown**.
- **What was inaccessible:**
  - isdown.app incident pages (HTTP 403).
  - nocode.tech (HTTP 429).
  - The official status-page history (404, and no history rendered on the root page).
  - Part of the release-notes page: the fetched rendering was truncated inside the 2026-04-22 section.
- **How pages were read:** the fetcher returns model-summarized page text. A human must therefore re-check exact wording, numbers and dates.
- **Independent press:** no in-window coverage of Bubble from major technology or business outlets was found. This is a search result, not proof that none exists.

## 2. Verified company/product identity and baseline

| Item | Evidence | Limits |
|---|---|---|
| Legal entity | The [Terms of Service](https://bubble.io/terms) name **Bubble Group, Inc.**, 22 W 21st Street, New York, under New York law. The terms were last revised 2026-09-28 and took effect 2026-10-03. | No corporate filing was checked. A search snippet showed an older 2025 revision, but the fetched page is used. |
| Offering | A proprietary hosted visual no-code platform for web apps and native mobile apps. It includes a visual editor, a built-in database, workflows, an API Connector, a plugin marketplace, and the AI Agent / app generation. | Proprietary and hosted. The terms describe **no app code-export process**, which is consistent with the "no code export" criticism in third-party reviews. Those reviews are undated or conflicted, so the point is not verified further. |
| Content rights | The terms say users keep rights in "Direct User Content" (site content, design, workflows, data), and Bubble gets a license only to operate the platform. | Keeping rights is not the same as portability: apps run only on Bubble's runtime. |
| Open source | [github.com/bubblegroup](https://github.com/bubblegroup) holds 26 public repos, mostly MIT/ISC forks of build tooling. [bubble-for-agents](https://github.com/bubblegroup/bubble-for-agents) (agent/MCP client configuration) was created **2026-10-13**, after the window, and has **no LICENSE file**. | The platform itself is not open source. |
| Leadership | Co-founders Emmanuel Straschnov and Josh Haas sign the monthly community updates. The Feb 2026 AMA recap describes Emmanuel as co-CEO. | Baseline only. |
| Funding (baseline) | A US$100M Series A from 2021 was reported in third-party coverage, e.g. [Venture Capital Journal](https://www.venturecapitaljournal.com/no-code-platform-bubble-attracts-100m-series-a/). | Outside the window. Funding is not adoption. |
| AI model supplier | The Anthropic [customer story](https://claude.com/customers/bubble) and Bubble's release notes name Claude models. | Supplier relationships can change, and a model swap can change agent behaviour. |

**Pre-window context:** forum critiques before April 2026 (e.g. the topic "Nine Months Later, Bubble's AI Gap Is Compounding") argued that Bubble's AI lagged AI-first builders. These are baseline only and are not counted.

## 3. Month-by-month discoveries

| Month | Announcements and changes (row IDs) | Primary URLs | Independent reporting | Notes and limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Property-editor redesign opt-in beta (001). App generation partly on Claude 4.7, and Agent access expanded to agencies/BAMs (002). Anthropic case study (003). Agent image upload (004). | [forum 395213](https://forum.bubble.io/t/redesigned-property-editor-beta-now-available-to-everyone/395213), [release notes](https://bubble.io/release-notes), [forum 395311](https://forum.bubble.io/t/new-in-the-ai-agent-image-upload-smarter-expressions-clearer-responses/395311) | Supplier case study only | Agent access was **limited to cohorts** at this point. The case study's date comes from search metadata. |
| 2026-05 | The May 5 update recaps April and sets roadmap targets: compound edits in June, JSON parsing in May (005). The May 20 release notes list compound edits, improvements to mobile app generation and to AI-generated privacy rules, and a 4.5-minute API Connector timeout (006). | [May update](https://forum.bubble.io/t/monthly-community-update-may-2026/395768) | none found | No May blog posts on the index page. |
| 2026-06 | Native JSON parsing (007). June update: Opus 4.8 and compound edits live (008). Mobile plugin editor alpha (009). Agent secret redaction (010). | [forum 396794](https://forum.bubble.io/t/new-feature-native-json-parsing-is-now-available-in-the-api-connector/396794), [June update](https://forum.bubble.io/t/monthly-community-update-june-2026/396817), [forum 396919](https://forum.bubble.io/t/mobile-plugin-editor-alpha-is-now-available-to-everyone/396919) | none found | A late-June series of outages began (see July). |
| 2026-07 | Agent creates API calls (011). Property editor on by default (012). Agent reusable elements and read-only data access (013). **Reliability post-mortem** for Jun 26–Jul 15 (014). Reverse pilot (015). Global expressions GA (016). | [July update](https://forum.bubble.io/t/monthly-community-update-july-2026/397817), [post-mortem](https://forum.bubble.io/t/reliability-post-mortem-late-june-to-mid-july-2026/398590), [forum 398755](https://forum.bubble.io/t/feature-update-global-expressions-are-out-of-beta/398755) | Status aggregators only (snippets) | The post-mortem's table and text disagree on several durations. |
| 2026-08 | The balancer was replaced with Cloudflare-based routing (017). The Agent gains full native-mobile editing, still in beta (018). An HTTP 520 outage on Aug 4 lasted 1h14m per a third-party mirror (019). Merges ~30% faster, read replicas in private beta (020). App planning sessions (021). | [Aug update](https://forum.bubble.io/t/monthly-community-update-august-2026/399015), [blog](https://bubble.io/blog/bubble-ai-agent-mobile/), [Pulsetic](https://pulsetic.com/status/bubble/incidents/6165/) | Pulsetic mirror of the vendor status page | The outage came one day after the stability claim. |
| 2026-09 | Agent dev-database read/write when explicitly granted, approval modes, plugin auto-install (022). Business of Building telemetry report (023). Sonnet 5 as the default model and an experimental server-side issue checker (024). Mobile plugin editor public beta with any npm library (025). **BubbleGo deprecated** (026). AMA: MCP expected in 2–3 weeks (027). Terms revised (028). Reverse for teams (029). | [Sep update](https://forum.bubble.io/t/monthly-community-update-september-2026/400039), [forum 400849](https://forum.bubble.io/t/now-in-public-beta-mobile-plugin-editor-plus-important-bubblego-update/400849), [AMA](https://bubble.io/blog/september-2026-founder-ama/), [terms](https://bubble.io/terms), [forum 401106](https://forum.bubble.io/t/introducing-reverse-dev-for-teams/401106) | [Create With](https://createwith.com/tool/bubble/updates/bubble-launches-reversedev-to-map-codebases-visually), an AI-drafted trade note | Several items are previews or private betas. |
| 2026-10-01..12 | **Agent 2 GA** (030). **Bubble MCP beta** (031). AI credits and a Starter price rise effective Oct 20 (032). MCP limitations thread (033). Community critique of the Agent versus MCP (034). | [Agent 2 blog](https://bubble.io/blog/agent-2/), [Oct update](https://forum.bubble.io/t/monthly-community-update-october-2026/401306), [forum 401313](https://forum.bubble.io/t/bubble-mcp-is-here-whats-next/401313), [forum 401538](https://forum.bubble.io/t/the-good-the-bad-and-the-amazing-mcp-agent-feedback/401538) | Community forum only | The `bubble-for-agents` repo (Oct 13) is out of window. |

## 4. Dated event evidence and capabilities

All 34 rows are in the [CSV](028-bubble.events.csv) (`CI2026-028-001` to `-034`). The clusters that matter most for this study:

| Cluster (rows) | What the cited documents support | Availability and limitations | Working grade |
|---|---|---|---|
| **Built-in AI Agent: limited cohort → beta for all → Agent 2 GA** (002, 004, 008, 011, 013, 018, 022, 024, 030) | Bubble describes an in-editor agent that edits UI, workflows, data types, privacy rules, API calls, plugins, reusable elements, custom states and mobile apps. Edits are proposed then approved, with auto-approve or always-ask modes. Dev-database access requires an explicit grant. | Rollout was staged (agencies and BAMs in April, "rolling out to everyone" in August, GA on Oct 6). The improvement claims ("1.5x / 2x") come from **internal, unpublished evals**. The default model changed several times in six months (Opus 4.7 → Opus 4.8 → Sonnet 5), which threatens reproducibility. | E1–E2 |
| **External-agent access via the Bubble MCP** (027, 031, 033) | Users connect their own agent (Claude Code, Codex) to edit existing apps. Bubble says this consumes no Bubble AI credits. | **Beta.** It cannot read logs, merge branches or deploy. Cursor fails to connect because of CIMD authentication. Users report truncated workflow visibility. A post-window GitHub repo holds the client configuration and has no license. | E1 |
| **Reuse primitives inside Bubble** (013, 016, 007) | Global expressions are GA as reusable parameterized expressions. The Agent can create and modify reusable elements. Native JSON parsing reduces workaround API calls. | All of this reuse is **within one proprietary app**. It is not portable code and not cross-project package reuse. | E1–E2 |
| **Third-party dependency surface** (009, 022, 025) | Mobile plugins went from alpha (React Native libraries only) to public beta allowing **any npm library**. The Agent now recommends and **installs** marketplace plugins. | The supply-chain and maintainer-retirement risk grows. A June reply names plugin maintainer retirement as a risk. Users asked what drives the Agent's plugin choice and got no answer. | E1 |
| **Security and privacy features** (006, 010, 013, 022) | AI-generated privacy rules. Secret redaction in Agent chat. Agent data access that is read-only or explicitly granted. | No independent test was found. In the October thread, one user reports AI data-access toggles were on by default on an existing app; another says they are opt-in. That conflict is **unresolved**. | E1 |
| **Production reliability** (014, 017, 019) | The vendor post-mortem lists about ten incidents from Jun 26 to Jul 15, including recurring full-platform outages and a component dropping about 10% of requests. A mirrored status entry records a 1h14m HTTP 520 outage on Aug 4. | Durations are internally inconsistent in the vendor's own post. The official status page did not render its history. | E2 (vendor post-mortem) / E1 (mirror) |
| **Lifecycle and platform changes** (001, 012, 026, 032) | The property editor went from opt-in beta to default, with the old editor to be phased out later. BubbleGo was deprecated, so on-device dev builds now require paid plans. AI credit metering and a Starter price rise were announced. | These are the forced-migration and cost changes a maintainer would face. Their actual burden was not measured. | E1 |
| **Coded-app tooling: Reverse** (015, 029) | An Innovation Lab product that syncs with a GitHub repo, visualizes a coded or vibe-coded app, and allows branch-based edits. It is pitched at Replit and Lovable apps as well as Bubble. | A pilot. No pricing, data-handling or license terms were found in the posts. | E1 |

## 5. What the company says it intends to do

| Paraphrase (short quotes only) | Link/date | Horizon | Status | Missing or contradictory context |
|---|---|---|---|---|
| Workflow engine revamp with branching, looping and try/catch; beta "toward the end of the year" | [Oct update](https://forum.bubble.io/t/monthly-community-update-october-2026/401306), 2026-10-06; earlier "early stage" (Jul 1) and "alpha very soon" (Aug 3) | end of 2026 (beta) | planned | The target slipped across updates. An alpha was promised "later this month" on Sep 3. |
| MCP is "just the beginning"; more per-app permission settings | [Agent 2 blog](https://bubble.io/blog/agent-2/), [Oct update](https://forum.bubble.io/t/monthly-community-update-october-2026/401306), 2026-10-06 | none given | tentative | Missing features (logs, merge, deploy) have no dates. |
| A second MCP so that an app's **end users** can interact with it through their own AI tools, after the new workflow engine | [Sep AMA](https://bubble.io/blog/september-2026-founder-ama/), 2026-09-25 | none given | uncommitted | Depends on the workflow engine slipping no further. |
| Server-side pre-rendering "is something the team wants" | [Sep AMA](https://bubble.io/blog/september-2026-founder-ama/), 2026-09-25 | none given | uncommitted | Relevant to SEO and discoverability. |
| Old property editor to be phased out "down the line" with "plenty of notice" | [forum 398077](https://forum.bubble.io/t/redesigned-property-editor-now-on-by-default/398077), 2026-07-09 | none given | planned | No date. |
| App data tab redesign with inline editing | [Oct update](https://forum.bubble.io/t/monthly-community-update-october-2026/401306) | November 2026 | planned | It was shown at the June AMA and users asked repeatedly when it would ship. |

These are company statements, **not** forecasts or delivered features.

## 6. Independent interpretation: conditional 2027–2031 scenarios

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence / unknowns |
|---|---|---|---|---|
| H1: Visual no-code platforms will become **agent-operable back ends**, edited mainly by external agents over MCP rather than through the visual editor. | MCP beta; credit-free MCP access; user report that MCP "automate[s] weeks" of work; `bubble-for-agents` config repo (post-window) | MCP may stay a niche power-user feature while most users keep the built-in agent; vendor pricing may later meter MCP | MCP stays beta past 2027 without deploy/merge; MCP becomes credit-metered; no independent task study shows MCP edits are accepted at least as often as editor edits | Low; based only on vendor posts and anecdote |
| H2: The maintainability gap between proprietary visual apps and code shifts from "can't read the code" to "**can't audit or diff agent changes**". | Users say MCP changes are hard to audit; a user asked for a PR-style review workflow (row 020); Bubble's Reverse goes the other way, visualizing coded apps for non-coders | Bubble may add PR review, diffs and test gates; branch merges were already improved | A first-party PR/diff review plus test-on-deploy for agent edits ships and is independently exercised | Low–medium |
| H3: Agent-installed marketplace and npm dependencies will make **third-party dependency risk** a main lifecycle cost for no-code apps. | The Agent installs plugins; npm libraries are allowed in mobile plugins; community concern about plugin abandonment | Bubble may curate or vet plugins, or pin versions | A published plugin vetting/pinning policy plus low observed breakage in an independent sample | Low |
| H4: Fast changes to the default model make AI-built results on hosted platforms hard to reproduce. | Three model changes in about five months, each with vendor-claimed improvements | Changes may raise quality monotonically; users may not need reproducibility | Bubble publishes pinned-model options or eval sets; replayed tasks give stable results across model changes | Medium on the observation, low on its consequence |

These are researcher hypotheses, not Bubble's strategy. Funding, user counts and "6 million users" claims are not evidence of adoption.

## 7. Implications for the GitHub 1000 study

| Construct | Possible observable effect | Study design to test it | Negative or null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding-practice change | External coding agents (Claude Code, Codex) operating a no-code platform via MCP | Opt-in logged comparison of the same tasks done via the built-in Agent, via MCP and manually | Users may simply prefer manual editing | Only on consented, synthetic or own apps |
| **M2** accepted task quality | The vendor claims "2x fully functional" results | Frozen tasks with independent hidden acceptance tests; count every attempt, including failures | The vendor evals may not transfer to real tasks | No vendor eval data available |
| **M3** discoverability | Telemetry links frequent deploys with monetization; SSR "wanted" | None feasible from public data; vendor telemetry is not accessible | Correlation, with selection bias | Do not reuse the vendor's numbers as study evidence |
| **M4** verified third-party reuse | Marketplace plugins and reusable elements are reused across apps | Trace one consented plugin through to real use in a downstream app | Installs are not useful reuse | Marketplace install counts are not verified reuse |
| **M5** reuse-first and rights | Bubble-internal reuse (global expressions) does not port; open-source footprint limited to forks; new config repo unlicensed | License check at a pinned commit before any reuse | The proprietary scope is by design | Terms are not a portability guarantee |
| **M6** lifecycle human and energy cost | Forced editor migration, BubbleGo deprecation, outages, AI credit metering, price rise | Log review, migration and support minutes on one pilot app over 30 days | Costs may be small for small apps | **No token-to-CO2e conversion**; energy only if actually metered |
| **M7** actionable interventions | Planning sessions (clarify before generating), approval modes | Compare generation with and without planning on the same task specification, with blinded acceptance | Planning may only add time | Synthetic tasks only |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). This is a *process* experiment and does not adopt Bubble. The transferable idea from Bubble's in-window changes is the "app planning session" (row 021): the agent asks clarifying questions before generating, under an approve-before-apply mode (row 022). Live Trending `capture` remains **disabled** under the source-access policy, and nothing here changes that.

**Candidate practice (not validated):** before a coding agent writes code for a bounded issue, it must produce a short clarification-and-plan note. The note lists its assumptions, open questions and the existing code or packages it intends to reuse, and a human must approve it before any edits.

**Treatment and comparator:**
- **Comparator:** the current workflow, in which the agent edits directly from the issue text.
- **Treatment:** the same agent and model, pinned to an exact model ID that is recorded, plus the mandatory plan-and-approve step.
- **Tasks:** 10 frozen small tasks of the kind seen in this repo (for example a validator rule, a CLI flag, a docs/schema update), randomly assigned 5/5 or crossed over.
- **Acceptance:** acceptance tests are written beforehand **by someone other than the agent**, are hidden from the agent's context, and are frozen before the trial.

**Accepted-task functional unit:** one task whose hidden acceptance tests and full `python -m unittest discover -s tests -v` suite pass, and which a human reviewer accepts with no more than one revision round.

**Primary endpoint:** accepted tasks divided by **all** assigned tasks, counting refused, abandoned and timed-out tasks as failures.

**Measured human work:**
- Minutes spent approving plans.
- Minutes spent reviewing and reworking.
- Number of review rounds.
- Wall-clock time to acceptance.
- Agent token counts as logged (tokens are **not** converted to energy or CO2e).

**Guardrails:**
- No new dependency without a license and maintenance check.
- No secret or credential appears in a prompt or log.
- `scripts/check_research_artifacts.py` and `trending_study.data_integrity` both pass.
- No change to frozen research protocols.

**Stop rule:**
- Stop and keep the simpler workflow if, after 10 tasks, the treatment's acceptance rate is not higher, **or** median human minutes per accepted task rise by more than 25%.
- Stop at once on any guardrail breach.
- Record a null or negative result as such.

**Status:** not executed; no effects estimated.

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (per vendor documents, not independently exercised):**
  - Agent 2 GA (Oct 6).
  - Global expressions GA (Jul 27).
  - The property editor became the default (Jul 9).
  - Native JSON parsing (Jun 2).
  - Agent secret redaction (Jun 17).
  - App planning sessions (Aug 31).
  - Merge improvements (Aug 28).
  - BubbleGo deprecated (Sep 22).
  - Terms revised (Sep 28 / Oct 3).
- **Previews and announcements only:**
  - Bubble MCP (beta).
  - Mobile plugin editor (public beta).
  - Read replicas (private beta).
  - Reverse (pilot).
  - Workflow engine (alpha/beta targets).
  - Second MCP and SSR (uncommitted).
  - Starter price rise (effective after the window).
- **Conjectures and unknowns:**
  - Actual Agent and MCP task-acceptance rates.
  - Data-access defaults.
  - The real migration burden.
  - Uptime over the full window.
  - Corporate structure at filing level.
  - The license for `bubble-for-agents`.
  - Exact release-note wording (the page was truncated in the fetched rendering).
- **Contrary or null evidence:**
  - The vendor's own reliability post-mortem.
  - The Aug 4 outage, the day after the stability claim.
  - The community report that the built-in Agent degrades over turns and is costly.
  - MCP client-compatibility failures.
  - Pushback on the forced editor migration and the price rise.
  - No in-window independent press coverage found.
- **Reviewer links and audit date:** none. The human factual/link spot-check, the source-access/rights review and the methods review are all pending. Raise them on the PR for [#95](https://github.com/MSKazemi/github-trending-1000-study/issues/95). **Do not close #95 on the basis of this screen.**

## Independent source spot-check (2026-10-16)

A second agent, who did not write this screen, re-fetched the cited sources on 2026-10-16. Pages were read as raw text: `curl -sL` for blog, Pulsetic and Anthropic pages; the Discourse `/t/<id>.json` endpoint for forum threads, which gives `created_at` and the staff flag; and `gh api`. `bubble.io/terms` and `bubble.io/release-notes` render client-side, so their DOM was dumped with headless Chrome (`--dump-dom`) and searched. With this method the **full** release-notes page rendered, which removes the truncation limitation in section 1 for the dates checked. A model summary was not used for any figure. Pages were not archived.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (section 2) | confirmed | Rendered terms: "Bubble Group, Inc.", "22 W 21st Street, 2nd Floor, New York"; "Last revised: September 28, 2026 / Effective date: October 3, 2026". No app code-export clause was found. `gh api orgs/bubblegroup`: 26 public repos, created 2015-05-31. `bubblegroup/bubble-for-agents` was created 2026-10-13T21:21Z and has license `null`. Filing-level ownership is still unchecked |
| 002 | corrected | Apr 22 release notes: "Claude 4.7", and access expanded "to a broader group of agencies and BAMs". The CSV had expanded BAMs to "Bubble Ambassadors", which the page does not do; the acronym is now kept as written |
| 003 | confirmed | "2x first-week user activation rate", "~30% increase in user satisfaction" (~70% to ~90% positive feedback), and an approve-before-apply flow. No publication date was found in the raw page, so the date stays search-metadata only (E0) |
| 006 | corrected | May 20 entries exist, but mobile app generation and AI-generated privacy rules are **improvements** to existing features ("more reliable", "now automatically restrict filtering on hidden fields"). The timeout change is 2.5 to **4.5** minutes. The CSV and the section 3 sentence were fixed |
| 008 | confirmed, conflict added | June 2 (Discourse `created_at` 2026-06-02T16:48Z, by josh): "Claude Opus 4.8", "up to 20% faster", "doubled the cap ... from 2.5 minutes to 5 minutes", Prompt AI aimed at "the end of the month". The 5-minute figure conflicts with the 4.5 minutes in the May 20 notes; this was added to the limitation |
| 010, 013, 024 | confirmed | Rendered release notes: Jun 17 "Secret redaction" for "API keys and tokens you share in the Agent chat"; Jul 15 reusable elements and read-only data access; Sep 9 "Bubble's AI now runs on Claude's latest model (Sonnet 5)" plus app planning sessions |
| 014 | confirmed | Post-mortem dated 2026-07-22T20:58Z (fede.bubble). Its table has 11 rows, one of them "June 30, July 9, July 13 / Full platform down, recurring"; "about 10% of requests" were dropped. The internal duration conflicts are real: domain reassignment is "a few days" in the text but "~2 hrs" in the table, and mobile preview is "a few hours" in the text but "14 hrs" in the table. A staff reply says "about 80% of it has been retired" (Balancer) |
| 015 | corrected | Thread created 2026-07-24T11:50Z by a user. Staff post 7 says "It literally just launched yesterday", so the 07-23 event date stands. The GitHub sync, workflow views, docs and branch-based edits are described in post 12 by a **non-staff-flagged** account writing as "we", not by staff. Attribution fixed |
| 019 | confirmed | Pulsetic incident #6165: "Brief Outage - HTTP 520", Major, started "Aug 4, 2026 · 4:40 PM", resolved 5:55 PM, duration "1h 14m". The page states no timezone |
| 020 | confirmed | 2026-08-28: "cutting merge time by ~30% in testing"; "Read replicas (private beta)"; a user asks for a "formal Pull Request (PR) workflow" |
| 023 | corrected | `datePublished` 2026-09-08. The page says "studied more than 250,000 Bubble apps". The "over six months" in the CSV is the apps' **first six months** of deploys ("about 45 updates" versus "two"), not the study window, and "live" was not stated. Wording fixed |
| 025, 026 | confirmed | 2026-09-22 (amy.zhong): "any third-party npm library"; "As of today, September 22, we're officially deprecating BubbleGo", citing Apple App Store policy; "dev builds are only available on paid plans" |
| 027 | corrected | `datePublished` 2026-09-25T20:10Z; MCP beta "within the next two to three weeks"; end-user MCP to follow the new workflow engine; pre-rendering "something the team wants". The page gives **no AMA session date**, so the event date 2026-09-24 was removed (left blank) |
| 030, 031, 032 | confirmed | Agent 2 blog `datePublished` 2026-10-06T15:15Z: "1.5X better at building exactly what the user asked and 2X better at ensuring the result is fully functional"; "out of beta"; MCP "can't read logs, merge branches or deploy" and does not draw on AI credits; Starter Web rises to "$39/month ($32/month billed annually)" on October 20 |
| 034 | confirmed | 2026-10-12, a "Regular" community user: MCP "can automate weeks of Bubbling in hours"; the built-in Agent output "gets worse and worse" over turns; monthly allowance compared to "5-hour usage of a $20 AI plan" |

**Totals:** 19 ledger rows (002, 003, 006, 008, 010, 013, 014, 015, 019, 020, 023, 024, 025, 026, 027, 030, 031, 032, 034) and the entity claim were checked. Outcome: 13 confirmed, 1 confirmed with a vendor-internal conflict added (008), 5 corrected (002, 006, 015, 023, 027). No fabricated URL or figure was found and no row was removed. No evidence grade was changed. No contamination from another company was found.

*This is an AI-assisted source spot-check, not qualified human factual, rights or methods review. Every pending gate above still applies.*
