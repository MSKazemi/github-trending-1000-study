# Braintrust: provisional six-month technology intelligence screen (055)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](055-braintrust.events.csv) and [search log](055-braintrust.search-log.md) are **provisional, AI-assisted documentary source leads** prepared for [issue #122](https://github.com/MSKazemi/github-trending-1000-study/issues/122). **No qualified human has reviewed them.** Factual/link review, source-access/rights review and methods review are all still **pending**. This screen is not scientific or security sign-off; issue #122 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 055; [issue #122](https://github.com/MSKazemi/github-trending-1000-study/issues/122). Study lens: *structured datasets, evals and failure analysis* (AI evaluation and observability).
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16**. The following are unavailable:
  - exact UTC search-run times;
  - full search-result counts;
  - immutable page snapshots;
  - an independent reviewer.
- **Status:** **provisional dated documentary screen.** It holds 23 traceable source leads covering all seven calendar segments. No qualified human has reviewed it, and factual/link, source-access/rights and methods review are pending. It is **not** verified task outcomes, exhaustive retrieval or human-approved scientific completion. See the [event ledger](055-braintrust.events.csv), the [month-segment queries and inclusion/exclusion log](055-braintrust.search-log.md) and the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:**
  - [Braintrust](https://www.braintrust.dev/)
  - [changelog](https://www.braintrust.dev/docs/changelog), which has month-level headings only
  - [blog](https://www.braintrust.dev/blog)
  - [Trust Center updates](https://trust.braintrust.dev/updates), which did **not render** for this screen
  - the [braintrustdata GitHub organization](https://github.com/braintrustdata), via read-only public API for releases and licence metadata
- **Claim grading:** uses the company-watch E0–E4 tiers, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](055-braintrust.search-log.md) records every query and fetch actually run, together with the include/exclude decisions. Three planned web queries were **not executed** because the session's search budget ran out. They are listed in the log and remain open.

**Main source-shape limitation.** Braintrust's official changelog groups entries by **month without day dates**. Changelog items are therefore used only as corroboration and narrative context. Ledger rows come from day-dated blog posts, GitHub releases or press articles. As a result, many changelog-only features are **not** ledger rows, including:

- workload identity federation for Anthropic, Vertex, Azure and OpenAI;
- audit logging;
- gateway failover;
- API key expiry controls;
- span customizers.

The April changelog block cannot be split at April 12, so the in-window status of April items is **unresolved**. One example is the public preview of "Sandboxes for agent evals".

This is **not** exhaustive internet search. When a month has no surfaced article, that is not evidence of inactivity. Search result counts are unknown, not zero.

## 2. Corporate/product identity and rights baseline

**Entity and products.** Braintrust ([braintrust.dev](https://www.braintrust.dev/)) sells an AI evaluation and observability platform. Its main parts are:

- experiments, datasets and scorers;
- tracing and logs;
- Topics clustering;
- the Loop assistant;
- the Brainstore trace store;
- an AI gateway;
- SaaS, BYOC and self-hosted data-plane deployment options.

**Ownership and funding.** Corporate parent, beneficial ownership and any acquisitions were **not verified** to filing level as of 2026-10-12. No in-window rename or acquisition was surfaced. As **pre-window baseline only**, [SiliconANGLE (2026-02-17)](https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai/) reported an $80M Series B led by Iconiq at an $800M valuation. Funding is not adoption evidence.

**Name ambiguity.** The name "Braintrust" is also used by unrelated organizations. All sources here were checked to refer to braintrust.dev.

**Open-source licences.** Licence data comes from GitHub SPDX metadata read on 2026-10-16. It is **not** a commit-pinned legal review.

| Component | Licence (GitHub metadata) | Note |
|---|---|---|
| [autoevals](https://github.com/braintrustdata/autoevals) scorer library | MIT | Most reusable standalone component for evals |
| [braintrust-sdk-python](https://github.com/braintrustdata/braintrust-sdk-python), [braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript), Go/Ruby/.NET/Rust SDKs, [bt CLI](https://github.com/braintrustdata/bt) | Apache-2.0 | SDK and CLI are client code; the hosted service is proprietary |
| [braintrust-sdk-java](https://github.com/braintrustdata/braintrust-sdk-java), [braintrust-proxy](https://github.com/braintrustdata/braintrust-proxy) | MIT | |
| [agentbehavior](https://github.com/braintrustdata/agentbehavior) (behavior specs) | Apache-2.0 | The [agentbehavior.dev](https://www.agentbehavior.dev/) site states no licence, version or date |
| [braintrust-coding-agent-plugins](https://github.com/braintrustdata/braintrust-coding-agent-plugins) | NOASSERTION | The LICENSE file reads as an Apache-2.0 **placeholder** ("TODO"). Treat its rights as **unresolved** before reuse |

An open-source SDK does **not** make the platform's components open-source or self-hostable without a licence. Brainstore, Topics, Loop, Patterns and the control plane are all hosted platform components. Self-hosted data-plane availability depends on the vendor's data-plane version and plan.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 14 Python SDK 0.15.0](https://github.com/braintrustdata/braintrust-sdk-python/releases/tag/py-sdk-v0.15.0) and [Apr 20 JS SDK 3.9.0](https://github.com/braintrustdata/braintrust-sdk-javascript/releases/tag/braintrust%403.9.0), both adding per-input eval trial counts; [Apr 15 bt CLI 0.5.0](https://github.com/braintrustdata/bt/releases/tag/v0.5.0) | The trial-count feature is one capability shipped in two SDKs. The bt release notes list only binaries. Apr 13 and Apr 28 blog posts are guidance and were excluded. The Apr 3–8 CLI/MCP and Brainstore posts are **pre-window** |
| May | [May 6 TechCrunch](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/) and [May 8 SecurityWeek](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/) report unauthorized access to a Braintrust AWS account that held customer-stored AI provider keys. Per the vendor notice relayed by SecurityWeek, it was detected May 4 | This is **one incident**. The vendor's notice did not render for this screen. The spokesperson said there was "no evidence of a breach" while confirming a "security incident". No root cause was found. The May changelog (month-level) lists secret previews, rotation timestamps and API-only key creation removed. We **do not assert** these were caused by the incident |
| June | [Jun 1 Topics GA](https://www.braintrust.dev/blog/topics-ga); [Jun 4 Topics architecture](https://www.braintrust.dev/blog/topics-architecture); [Jun 9 autoevals 0.3.0](https://github.com/braintrustdata/autoevals/releases/tag/py-0.3.0); [Jun 30 startups program](https://www.braintrust.dev/blog/braintrust-for-startups) | GA is the vendor's label. Pricing for Topics changed in May per the changelog. A Jun 12 outage lead is **unverified** (the status page returned 404) and excluded |
| July | [Jul 7 Brainstore shingled phrase search](https://www.braintrust.dev/blog/brainstore-phrase-search); [Jul 29 behavior specs open standard](https://www.braintrust.dev/blog/behavior-specs) (with Basis) | The ">25x" figure is a vendor benchmark on undisclosed customer data. The behavior-spec licence comes only from the repository metadata |
| August | [Aug 5 Cloudflare Agents tracing](https://www.braintrust.dev/blog/cloudflare-agents); [Aug 24 Harbor plugin](https://www.braintrust.dev/blog/harbor-agent-evals); [Aug 26 MCP server](https://www.braintrust.dev/blog/braintrust-mcp); [Aug 28 @braintrust/otel 1.0.0](https://github.com/braintrustdata/braintrust-sdk-javascript/releases/tag/%40braintrust/otel%401.0.0) | No stage label is given for the Harbor plugin or MCP. The Cloudflare and Harbor sides were not checked on their own primary sources |
| September | [Sep 3 Patterns/Debugger/enhanced Loop](https://www.braintrust.dev/blog/active-observability-loop-patterns-debugger) (**public preview**); [Sep 18 Jev judge](https://www.braintrust.dev/blog/evaluate-agent-responses-with-jev) (access-gated); [Sep 23 FAQ with stated plans](https://www.braintrust.dev/blog/patterns-topics-loop-faq); [Sep 24 Nitro query engine](https://www.braintrust.dev/blog/nitro) | Preview is not GA, and pricing is to follow "before general availability". Nitro speedups are vendor-run benchmarks with anonymized competitors |
| Oct 1–12 | [Oct 5 JS SDK 3.37.0](https://github.com/braintrustdata/braintrust-sdk-javascript/releases/tag/braintrust%403.37.0) (eval cancellation, batch workflow evals); [Oct 7 coding agent insights](https://www.braintrust.dev/blog/coding-agent-insights) (preview); [Oct 7 autoevals 0.4.0](https://github.com/braintrustdata/autoevals/releases/tag/py-0.4.0) (default scoring model changed); [Oct 8 application logs](https://www.braintrust.dev/blog/application-logs) (preview) | The [Oct 15 workflow-evals post](https://www.braintrust.dev/blog/workflow-evals) is **excluded** as out-of-window. Independent October coverage is unknown because that query was not executed |

See the [CSV](055-braintrust.events.csv) for the **23 dated source records**. This is a purposive list of material events, not a census. For comparison, the GitHub API shows 36 Python SDK, 32 JS core-SDK and 34 stable `bt` releases in the window.

Blog and changelog dates are the dates displayed on the pages, not archive timestamps. `event_date_utc` is filled only when a release is timestamped by GitHub or when the incident detection date is stated by a source.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited documents support | Important non-equivalence or counterexample |
|---|---|---|
| **Structured datasets:** eval trial counts (Apr), [Harbor sync into managed datasets](https://www.braintrust.dev/blog/harbor-agent-evals) (Aug), plus changelog-only dataset snapshots, environments, filters and versioning (Apr/May) | Vendor-described dataset lifecycle tooling: versioned snapshots, filtered runs, and sandboxed task results converted to dataset rows and scores | Harbor verifier rewards are **task-author defined**, not independent acceptance. Dataset features on the hosted service are not portable open formats unless exported |
| **Failure analysis:** [Topics GA](https://www.braintrust.dev/blog/topics-ga) → [Patterns/Debugger preview](https://www.braintrust.dev/blog/active-observability-loop-patterns-debugger) → [coding agent insights](https://www.braintrust.dev/blog/coding-agent-insights) | LLM-summarized facets are clustered with HDBSCAN/UMAP ([architecture](https://www.braintrust.dev/blog/topics-architecture)). Patterns then runs scheduled LLM investigations that output findings with trace evidence | The [Patterns docs](https://www.braintrust.dev/docs/observe/patterns/index) state that findings separate confirmed causes from hypotheses when code or MCP context is missing. No independent precision/recall or false-finding rate was found. Topics needs at least 400 traces |
| **Evaluation reproducibility:** [autoevals 0.3.0](https://github.com/braintrustdata/autoevals/releases/tag/py-0.3.0) moved to the gateway; [0.4.0](https://github.com/braintrustdata/autoevals/releases/tag/py-0.4.0) changed the default scoring model; [JS 3.37.0](https://github.com/braintrustdata/braintrust-sdk-javascript/releases/tag/braintrust%403.37.0) changed timeout semantics | The MIT scorer library is actively maintained and accepted first-time external contributions | **A default judge-model change makes LLM-judge scores non-comparable across library versions** unless the model is pinned. This is a concrete reproducibility hazard for this study's own evals |
| **Open interoperability:** [@braintrust/otel 1.0.0](https://github.com/braintrustdata/braintrust-sdk-javascript/releases/tag/%40braintrust/otel%401.0.0), [Cloudflare OTLP](https://www.braintrust.dev/blog/cloudflare-agents), [application logs over OTLP](https://www.braintrust.dev/blog/application-logs), [behavior specs](https://www.braintrust.dev/blog/behavior-specs) | Vendor-stated OpenTelemetry ingest paths and an Apache-2.0 Markdown spec format for trajectory behaviour | No independent adopter of behavior specs was surfaced. OTLP ingest does not make Braintrust-specific SQL, Topics or Patterns portable |
| **Coding-agent integration:** [MCP server](https://www.braintrust.dev/blog/braintrust-mcp) (Aug 26), coding-agent tracing plugins, [coding agent insights](https://www.braintrust.dev/blog/coding-agent-insights) | Agents (Claude Code, Codex, Cursor and others) can query traces and run or modify evals through MCP. Coding sessions can be traced per developer, model or branch | Write tools inherit account permissions, and dataset deletion is permanent. **Per-developer telemetry raises consent and privacy questions** that the post does not address. The plugin repository licence is a placeholder |
| **Security incident:** [TechCrunch](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/), [SecurityWeek](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/), [Security Affairs](https://securityaffairs.com/191888/data-breach/braintrust-security-incident-raises-concerns-over-ai-supply-chain-risks.html) | Unauthorized access to one AWS account holding org-level AI provider secrets. One customer was confirmed affected, three reported suspicious usage spikes, and all customers were asked to rotate keys | All three articles relay **vendor** statements, and none is a forensic audit. The initial access vector was not disclosed in sources found. Customer names in some coverage are third-party speculation and are **not** recorded |
| **Performance:** [phrase search](https://www.braintrust.dev/blog/brainstore-phrase-search), [Nitro](https://www.braintrust.dev/blog/nitro) | Vendor A/B and benchmark numbers with stated hardware and method | These benchmarks are vendor-run with anonymized competitors. Energy was not measured, and speed is not lower lifecycle cost |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated near-term intention | Current research classification |
|---|---|---|
| [Sep 3 Patterns/Debugger post](https://www.braintrust.dev/blog/active-observability-loop-patterns-debugger) | "Pricing details will follow before general availability." | **Announced only**: a GA date and price are not given |
| [Sep 23 FAQ](https://www.braintrust.dev/blog/patterns-topics-loop-faq) | "We plan to let you connect external systems in the near future"; an "agents abstraction" below project level is being worked on | **Announced only**, undated and uncommitted |
| [Sep 3](https://www.braintrust.dev/blog/active-observability-loop-patterns-debugger) / [Oct 7](https://www.braintrust.dev/blog/coding-agent-insights) / [Oct 8](https://www.braintrust.dev/blog/application-logs) posts | Expand active observability (Loop editing project objects, coding-agent telemetry, application logs) | **Public preview**, so not GA. Self-hosted access is gated by data-plane version |
| [Security Affairs](https://securityaffairs.com/191888/data-breach/braintrust-security-incident-raises-concerns-over-ai-supply-chain-risks.html) relay of the vendor notice (May 9) | Add timestamps and user attribution for API key changes | **Reported intention.** The May changelog lists "secret previews and rotation tracking", which is partial documentary corroboration. Vendor completion is not independently verified |

A stated intention does not guarantee delivery. These statements describe Braintrust's near-term product direction only. They are not a 2027–2031 company strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| LLM-driven trace clustering and failure-finding (Topics/Patterns) shortens time from production failure to a regression-test dataset row | Teams with good structured logging and manual triage reach the same rows equally fast | A blinded comparison shows no reduction in time-to-regression-test, or a high false-finding rate |
| Open trajectory specs (behavior specs) become a portable eval interchange format | Proprietary eval DSLs or OTel GenAI conventions dominate instead | No independent tool or organization adopts the spec by 2027, or the spec is abandoned or forked |
| Hosted eval platforms that store provider keys concentrate supply-chain risk | Workload identity federation (shipped per the changelog) removes stored long-lived keys | No further key-exposure incidents across vendors, and federation becomes the default |

## 7. M1–M7 study relevance

| Construct | Prospective measurement, not an inferred conclusion |
|---|---|
| **M1** coding practice | Coding agent insights and MCP show vendors instrumenting agent sessions. Only an **opt-in, consented** session log could measure workflow change; product availability is not adoption |
| **M2** accepted task quality | Eval tooling can *record* acceptance, but LLM-judge scores are not independent acceptance. Use hidden, human-authored tests and count **all** attempts |
| **M3** discovery | Blog cadence and startup programs are promotion, not discoverability evidence for third-party repositories |
| **M4** verified third-party reuse | The autoevals MIT library has external first-time contributors. Verified **downstream** reuse would need traced, consented integrations; stars (about 1k on autoevals) are not usage |
| **M5** reuse-first | Compare reusing autoevals or OTel-based tracing against writing bespoke scorers and logging for the same eval task |
| **M6** lifecycle human and energy cost | Judge-model calls, Topics inference and stored-trace volume cost money and energy. Measure reviewer minutes and metered compute where instrumented. **Do not convert tokens to CO2e** |
| **M7** actionable interventions | "Golden dataset from production failures" is a candidate maintainer practice. It needs a controlled, independently graded trial |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** the [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) repository's own offline synthetic evaluation fixtures, for example parser or gate outputs. **No live Trending capture** is involved; the study's `capture` command remains disabled under the source-access decision.

**Question:** does reusing an existing MIT scorer library with a **pinned** judge model give a reproducible, independently checkable failure-triage dataset at lower maintainer effort than bespoke scoring?

**Frozen task (functional unit):** classify 40 frozen, synthetic, pre-labelled outputs (20 correct and 20 seeded failures in 4 failure types) and emit a structured dataset of failures with type labels. Hidden reference labels are authored by a human other than the person running the arms, before any run.

**Arms:**

- **A (comparator):** existing in-repo deterministic checks plus a hand-written rubric applied by the maintainer.
- **B (reuse-first):** [autoevals](https://github.com/braintrustdata/autoevals) at an exact pinned version and commit, with the **judge model and temperature explicitly pinned**. The default is *not* used, because 0.4.0 changed it. Run locally with output written to a JSONL file. No hosted Braintrust account is required.
- **C (optional):** the same as B, but run through a hosted eval platform with stored provider keys. Run C only after a rights, terms and secret-handling review, and only with keys scoped and rotated for the trial.

**Acceptance test:**

- **Primary:** failure-detection agreement with the hidden labels across **all 40 items**. Abstentions and errors count as failures.
- **Reproducibility:** re-running B with identical pins on two separate days must give identical or near-identical labels, with a tolerance set before the trial.

**Measured costs:**

- maintainer setup and review minutes;
- number of judge calls and provider invoice amount;
- wall-clock time;
- dependency count added.

Energy is reported only if actually metered. **There will be no token-to-CO2e conversion.**

**Stop rule:** abandon B and keep A if any of the following holds:

- B's agreement with the hidden labels is not at least as good as A's;
- re-runs disagree beyond the preset tolerance;
- licence or dependency review finds an unresolved issue;
- any provider key would need to be stored outside the maintainer's own environment;
- setup plus review time exceeds A's by more than a preset margin.

A null or negative result is a valid outcome and must be preserved. **Nothing has been executed and no effect is estimated.**

## 9. Findings, uncertainties and limitations (2026-10-16)

- **Observed/shipped (documentary E1–E2):**
  - frequent SDK and CLI releases;
  - Topics GA;
  - OTel 1.0 package;
  - MCP server;
  - Cloudflare and Harbor integrations;
  - the behavior-spec repository (Apache-2.0);
  - the Nitro engine as stated by the vendor;
  - autoevals releases.
- **Preview or announced only:**
  - Patterns, Debugger and enhanced Loop;
  - coding agent insights;
  - application logs;
  - Jev (access-gated);
  - future external-system connections and the agents abstraction;
  - GA pricing.
- **Independent evidence:** limited to press reports of the May 2026 AWS-account key-exposure incident, which relay vendor statements. No independent product evaluation, benchmark replication or verified adopter outcome was found.
- **Missingness and unknowns:**
  - day-level dates for month-only changelog items;
  - in-window status of April changelog items such as the sandbox preview;
  - the vendor Trust Center notice text (did not render);
  - the incident root cause;
  - the unverified Jun 12 outage;
  - independent October coverage (query not run);
  - Harbor's and Jev's licences;
  - the coding-agent-plugins licence (placeholder);
  - filing-level ownership;
  - complete search hit counts;
  - archived snapshots.
- **Rights and privacy:** SDK licences do not cover the hosted service. Per-developer coding-agent telemetry needs consent review before any use in this study's trial instruments.
- **Pending:**
  - human factual/link spot-check of the ledger URLs and dates;
  - source-access and rights review;
  - methods review;
  - running the three unexecuted queries.

  **Issue #122 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.** on the basis of this screen.
