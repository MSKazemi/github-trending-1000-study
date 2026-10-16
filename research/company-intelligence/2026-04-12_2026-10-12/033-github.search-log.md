# GitHub (033): source-screen search and inclusion log

> **PROVISIONAL — AI-assisted documentary screening on 2026-10-16 UTC. No qualified human factual, rights or methods review.** Companion to [033-github.md](033-github.md), [19-row event ledger](033-github.events.csv), [issue #100](https://github.com/MSKazemi/github-trending-1000-study/issues/100) and [methods](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). This is source attribution, not independent verification of functionality, user benefit or adoption.

## Scope, method and sources

- **Predefined historical date window:** publication on 2026-04-12 through 2026-10-12 inclusive (UTC calendar day).
- **Access date:** 2026-10-16. The web-search interface returned relevant GitHub Changelog articles and monthly archives. Selected first-party URLs were read as attributed announcements or release notes, with publication dates and observed availability statements distinguished from effective dates. No login, credentials, API writes, source scraping, code downloads or instrumented product trials.
- **Sources screened:** GitHub Changelog month archives for Apr, Jun, Jul, Aug, Sep and Oct where found; specific dated release and policy pages; the existing in-repository first-pass [report](033-github.md); and a relevant peer-reviewed/security-research abstract as external *context*, not a corroboration of any product-performance claim.
- **Exact search phrases used in this pass:** `site:github.blog/changelog/2026 GitHub Copilot 2026 April May June July August September October code review agent API`; `site:github.blog/changelog/2026-07- "GitHub Copilot" "public preview"`; `site:github.blog/changelog/2026-04- OR site:github.blog/changelog/2026-06- "GitHub" "Copilot"`; `GitHub 2026 6 months changelog Copilot agents security supply chain 2026 April October`; queries targeted at the May 13 agent API, May 14 app preview, July 30 stacked PRs, Aug 28 policy notice, Sep 1 approvals, Sep 24 future-default policy and Oct 8 billing controls.
- **Review limits:** Search engine hit totals, excluded-URL lists and first-seen timestamps for each result were **not preserved**; the selected 19 rows are **not** a denominator for all GitHub announcements. The web-indexed documents could be revised after publication. No independently archived raw source HTML, hashes or source rights clearance. A source's public availability is not a republishing license.

## Seven calendar segments: selected first-party row counts (not event rates)

| Segment | Selected rows | Examples | Missing or unresolved |
|---|---:|---|---|
| 2026-04-12…30 | 2 | web debugging; June 1 review-billing announcement | Full April changelog pagination; permissions/security counterevidence |
| 2026-05 | 3 | VS Code April/May release summary; REST agent tasks public preview; desktop technical preview | Independently tested endpoint behavior, authentication compatibility, denied cases |
| 2026-06 | 5 | credit billing starts; sandbox preview; review runner settings; app GA; AGENTS.md support | Direct availability/tenant tests and realized charges |
| 2026-07 | 3 | in-app security preview; skills/MCP review GA; stacked PR preview | Review-failure negatives, vendor-independent security replication |
| 2026-08 | 2 | phased model policy; future policy and billing announcement | Actual effective date by organization and independent adoption |
| 2026-09 | 3 | AI reviewer approval preview; self-resolving review comments; Oct 22 defaults notice | Whether approvals were permitted in any audited repository |
| 2026-10-01…12 | 1 | Oct 8 organization review-cost controls | Other Oct releases, independent operational verification, Oct 13+ intentionally excluded |

Selected total: **19** GitHub first-party release/announcement documents (one source document per ledger row). This is neither a census of GitHub's product changes nor 19 measured software improvements. Dates use the displayed publication date; the July 29 skills/MCP page has a URL slug beginning `2026-07-31`, so do **not** infer publication date solely from a URL slug. The May 6 VS Code report covers some earlier April releases; it is **not** an assertion that every feature shipped May 6.

## Reconciliation and negative checks

- May 14 **technical preview** and June 17 **GA announcement** refer to the same Copilot desktop product, but are *different dated lifecycle events*, not two independent products or proven quality improvements.
- April 27 **future billing announcement** and June 1 **billing-in-effect** are different temporal states. The latter still does not prove what any maintainer was charged.
- Aug 28 future-policy notice, Aug 26 model-policy rollout and Sep 24 default-feature policy refer to distinct controls and effective dates. The Sep 24 article explicitly says **Oct 22, 2026** for default-feature enforcement, outside the historical window; do not backdate that change.
- Sep 1 Copilot **approval assessment** is **not** by itself a required status approval; admin-enabled AI approving reviews **may** count in GitHub's technical rule evaluation. This repository's scientific rule still requires qualified **human** review. A system may accept AI approval mechanically without meeting independent scientific review.
- GitHub (033) is part of **Microsoft**, and the Microsoft corporate report must not be used as a second independent company observation; de-duplicate shared announcements by canonical URL and underlying event date.
- Independent evidence context: [Siddiq et al. (2026), *Security in the Age of AI Teammates*](https://doi.org/10.1016/j.infsof.2026.108333) addresses security-relevant agent-authored PRs, but does **not** reproduce this vendor's Copilot features or establish their effectiveness. Peer-review/version and selection details warrant separate extraction under #7.
- A safety counterexample to automatic trust is a reported [OpenHands review-bot prompt-injection case](https://github.com/OpenHands/software-agent-sdk/issues/2026); this is an issue report, not a measurement of GitHub Copilot prevalence.

## Explicitly deferred scientific and factual checks

The 19 selected source pages have not been independently line-by-line reviewed against permanent captures by a qualified second reviewer; no source-rights assessment, complete per-segment retrieval log, paid-product installation, matched user-task evaluation, causal comparison or energy metering was performed. Publication dates and claims must be independently checked before upgrading from E1 vendor statements. Unseen or omitted results and inaccessible archives are *unknown*, not zero.

**Practical owner lesson (hypothesis to test):** keep AI coding/review permissions narrow; require a non-agent human for research/security signoff; compare parallel agents vs a sequential workflow on the **same frozen tasks**, including failed attempts and all human review minutes. Configure explicit branch protections before relying on AI-generated approvals. See [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248).
