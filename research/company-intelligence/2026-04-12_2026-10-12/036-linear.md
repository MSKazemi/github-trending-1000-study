# Linear: provisional six-month technology intelligence screen (036)

> **PROVISIONAL, AI-ASSISTED FIRST-PASS SCREEN, NOT HUMAN-REVIEWED (prepared 2026-10-16).** An AI assistant prepared this report, its [event ledger](036-linear.events.csv) and its [search log](036-linear.search-log.md) from public web pages it read on 2026-10-16. **No qualified human has reviewed them.** Factual/link review, source-access/rights review and methods review are all **pending**. They are documentary source leads only. They are not a verified chronology, an accepted six-month study, a product test, an adoption measurement or a scientific finding. Issue [#103](https://github.com/MSKazemi/github-trending-1000-study/issues/103) was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates remain open. No `NEWS-YYYY-NNNN` item for [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) has been minted from this screen.

- **Company watchlist ID:** 036 (slug `linear`)
- **Research issue:** [#103](https://github.com/MSKazemi/github-trending-1000-study/issues/103); evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (candidate leads only, see section 9).
- **Ownership and product boundaries (as of 2026-10-12):** product **Linear**, operated by **Linear Orbit, Inc.** according to the [Linear terms](https://linear.app/terms) (effective date shown: 2026-06-09) and the [How teams build report](https://linear.app/data) author byline. The company is privately held. Its own [Aug 26 post](https://linear.app/now/sharing-growth-with-the-people-building-linear) describes a secondary employee tender, not an acquisition. No in-window rename, acquisition or parent company was found. This was **not** checked against corporate filings.
- **Product URL and company channels:** [linear.app](https://linear.app/), [changelog](https://linear.app/changelog), the [Now blog/newsroom](https://linear.app/now), the [public SDK monorepo linear/linear (MIT)](https://github.com/linear/linear) and the [status page](https://linearstatus.com/). No official public product roadmap was found (see search log).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. **Source access date:** 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional). **27 ledger rows**, with at least one dated source in every one of the seven calendar segments.
- **Method:** [company intelligence protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) and [template](../../../templates/company_six_month_intelligence.md). The E0–E4 grades below are company-watch working tiers, not the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

The exact queries, the pages opened and the exclusions are in the [search log](036-linear.search-log.md). Summary:

- **Primary sources** were read directly: all 19 dated changelog entries in the window (changelog index pages 1–3), 8 Now/blog/customer pages, the terms page and the GitHub release list of `linear/linear`.
- **Second-entity and independent sources:** [GitHub changelog, Jul 23](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available/) (partner), [DevOps.com, Jul 27](https://devops.com/github-gives-teams-more-control-over-copilots-cloud-agent-in-linear/), [LeadDev, Jun 25](https://leaddev.com/ai/ai-coding-agents-are-now-the-default-what-comes-next) (only partly readable because of the paywall), [Accel, Aug 26](https://accel.com/news/our-investment-in-linear-the-digital-connectivity-between-engineers-and-agents) (an investor, not independent) and a [third-party pricing-page tracker](https://pricingsaas.com/companies/linear/diffs/2026W25).
- **Found/screened/excluded hit counts are unknown, not zero.** The search tool did not expose totals or stable rankings. Pages were read through an AI summarising fetch tool. Some exact strings (model names, dates, the $0.25 price, the 30% claim) were re-checked against the raw HTML. No byte-hash snapshots were stored.
- **No month had zero findings.** Most in-window coverage is first-party. **No independent hands-on evaluation** of Linear Agent, Diffs, coding sessions or Loops was found. That is a gap in what the search surfaced. It does not show that no such evaluation exists.

## 2. Verified company/product identity and baseline

Linear is a hosted issue-tracking and product-planning SaaS. Its public code is limited to the MIT-licensed [linear/linear](https://github.com/linear/linear) repository (TypeScript `@linear/sdk`, `@linear/import` and tooling). The hosted service, Linear Agent, coding sessions and the hosted MCP server are **proprietary services**. The SDK licence does not grant any rights to them.

**Pre-window baseline (context only, not counted as in-window events):**

- **Mar 24, 2026.** Linear launched **Linear Agent** in beta ([changelog](https://linear.app/changelog/2026-03-24-introducing-linear-agent)), and the CEO published the essay "[Issue tracking is dead](https://linear.app/next)". [The Register](https://www.theregister.com/2026/03/26/linear_agent/) and [DevClass](https://www.devclass.com/development/2026/03/27/linear-moves-sideways-to-agentic-ai-as-ceo-declares-issue-tracking-dead/5211661) both reported that a coding agent, codebase Q&A and diffs were then **planned**. This screen only saw the search snippets for these two articles.
- **Mar 24, 2026.** A permission-filter bug exposed private-team data to other members of the same workspace for about an hour. The [post-mortem](https://linear.app/now/linear-incident-on-mar-24th-2026) was published **Apr 6**, which is before the window, so it is excluded from the ledger. Its remediation commitments are relevant context for the in-window security controls.
- **Feb 26 and earlier.** Deeplinks into AI coding tools, the Linear MCP server, and GitHub Copilot for Linear in public preview from 2025-10-28 ([GitHub changelog](https://github.blog/changelog/2025-10-28-github-copilot-for-linear-available-in-public-preview)).

So the planned features from March (coding agent, codebase Q&A, diffs) were all reported as **shipped** inside the window: Code Intelligence on May 14, Diffs on May 28 and coding sessions on Jun 11. That supports one dated "announced, then delivered" chain. It is still vendor documentation, not an independent test.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Microsoft Teams app and custom coding-tool launchers (Apr 16); Linear Agent as an **MCP client** with admin allowlists (Apr 23); **Releases**, tying issues to CI/CD deployments (Apr 30); SDK 82.0.0 (Apr 18) | [Apr 16](https://linear.app/changelog/2026-04-16-linear-for-microsoft-teams), [Apr 23](https://linear.app/changelog/2026-04-23-linear-agent-mcp-support), [Apr 30](https://linear.app/changelog/2026-04-30-releases) | none found | Apr 9 sub-teams and Apr 10 blog are pre-window and excluded |
| 2026-05 | **Code Intelligence** public beta (May 14); GitHub Enterprise Cloud support and Slack Asks (May 21); **Linear Diffs**, in-Linear PR review synced to GitHub (May 28) | [May 14](https://linear.app/changelog/2026-05-14-code-intelligence), [May 21](https://linear.app/changelog/2026-05-21-project-slack-channels), [May 28](https://linear.app/changelog/2026-05-27-linear-diffs) | none found (Product Hunt and aggregators only) | Diffs page shows May 28, but its URL slug says 05-27 |
| 2026-06 | **Coding sessions**, a cloud coding agent using Claude Code and Codex (Jun 11); vendor metric post (Jun 11); bug auto-fix post (Jun 12); agent project updates, Vercel Eve and OAuth app manifests (Jun 18); terms effective Jun 9 | [Jun 11 changelog](https://linear.app/changelog/2026-06-11-coding-sessions), [Jun 11 post](https://linear.app/now/coding-sessions-for-linear-agent), [Jun 18](https://linear.app/changelog/2026-06-18-agent-assisted-project-updates) | [LeadDev Jun 25](https://leaddev.com/ai/ai-coding-agents-are-now-the-default-what-comes-next) (relays Linear's own figures) | Pricing tracker recorded "Coding Sessions (Beta)" on the pricing page, but the changelog does not say beta |
| 2026-07 | Initiative properties and Okta-managed MCP authorisation (Jul 2); **Loops** (Jul 20); human-vs-agent text attribution (Jul 23); **Copilot cloud agent for Linear GA** from GitHub (Jul 23); mobile coding sessions and **signed commits** (Jul 30) | [Jul 2](https://linear.app/changelog/2026-07-02-initiative-properties), [Jul 20](https://linear.app/changelog/2026-07-20-introducing-loops), [Jul 23](https://linear.app/changelog/2026-07-23-agent-assisted-editing), [Jul 30](https://linear.app/changelog/2026-07-30-coding-sessions-on-mobile) | [GitHub changelog Jul 23](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available/) (partner); [DevOps.com Jul 27](https://devops.com/github-gives-teams-more-control-over-copilots-cloud-agent-in-linear/) | DevOps.com cites no primary source, so it is treated as a restatement |
| 2026-08 | Agent architecture post (Aug 10); team initiatives and an added coding model option (Aug 13); vendor telemetry report (Aug 17); environments, browser self-testing and **usage pricing** for coding sessions (Aug 20); **$99M employee tender at $2.5B** (Aug 26); Ramp customer story (Aug 31) | [Aug 10](https://linear.app/now/how-we-built-linear-agent), [Aug 13](https://linear.app/changelog/2026-08-13-team-initiatives), [Aug 17](https://linear.app/data), [Aug 20](https://linear.app/changelog/2026-08-20-coding-environments), [Aug 26](https://linear.app/now/sharing-growth-with-the-people-building-linear), [Aug 31](https://linear.app/customers/ramp) | [Accel Aug 26](https://accel.com/news/our-investment-in-linear-the-digital-connectivity-between-engineers-and-agents) (investor); [Magica commentary](https://magica.com/news/linear-instinct-same-valuation-different-tests) (search result only) | /data and /customers/ramp show no date; their dates come from the /now index |
| 2026-09 | Priority inbox and **third-party app approval** (Sep 3); Loops for product management (Sep 14); CI rework post (Sep 21); **adaptive routing, environment secrets and open-weight (GLM) models** (Sep 24); **SDK 97.0.0 ESM-only breaking change** (Sep 28) | [Sep 3](https://linear.app/changelog/2026-09-03-priority-inbox), [Sep 14](https://linear.app/changelog/2026-09-14-loops-for-product-management), [Sep 21](https://linear.app/now/ci-bottleneck-reworked), [Sep 24](https://linear.app/changelog/2026-09-24-new-controls-for-linear-coding-agent), [SDK 97.0.0](https://github.com/linear/linear/releases/tag/%40linear/sdk%4097.0.0) | none found | Loops-for-PM entry page shows **Sep 14**, but the /now index shows **Sep 10**, so the release day is unresolved |
| 2026-10-01..12 | **Stacked PRs** in Diffs, **OAuth PKCE S256 required**, GitLab token renewal, another coding model option (Oct 8); SDK 97.1.0 (Oct 7) | [Oct 8](https://linear.app/changelog/2026-10-08-stacked-pull-requests), [releases](https://github.com/linear/linear/releases) | none found | Oct 13 "Five principles for working with Loops" is out of window and excluded |

## 4. Dated event evidence and capabilities

The [CSV](036-linear.events.csv) holds all 27 rows: 18 Linear changelog entries, 6 other first-party articles or reports, 1 SDK release, 1 partner changelog (GitHub) and 1 trade-press article (LeadDev). The highlights:

| Event ID | Published / event date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Working grade |
|---|---|---|---|---|---|---|
| CI2026-036-002 | 2026-04-23 / — | Linear Agent calls external MCP servers; admin allowlists | plan/GA not stated; new prompt-injection and data-egress surface | [changelog](https://linear.app/changelog/2026-04-23-linear-agent-mcp-support) | none | E2 |
| CI2026-036-003 | 2026-04-30 / — | Releases: issue status follows CI/CD deployment | 15 pipelines on Business, unlimited on Enterprise | [changelog](https://linear.app/changelog/2026-04-30-releases) | none | E2 |
| CI2026-036-004 | 2026-05-14 / — | Code Intelligence reads selected GitHub repos | **public beta**, Business/Enterprise | [changelog](https://linear.app/changelog/2026-05-14-code-intelligence) | [CEO post](https://linear.app/now/code-intelligence-for-linear-agent) (same company) | E2 |
| CI2026-036-006 | 2026-05-28 / — | Diffs: PR review in Linear, synced to GitHub; GitHub code access **on by default** when connecting | all plans; guided reviews in beta | [changelog](https://linear.app/changelog/2026-05-27-linear-diffs) | none | E2 |
| CI2026-036-007/008 | 2026-06-11 / — | Cloud coding sessions with Claude Code and Codex; claims "roughly 30%" of internal bugs resolved and ~700 PRs merged in a month | AI credits; GitHub code access required; beta label disputed | [changelog](https://linear.app/changelog/2026-06-11-coding-sessions), [post](https://linear.app/now/coding-sessions-for-linear-agent) | [pricing tracker](https://pricingsaas.com/companies/linear/diffs/2026W25) | E2 (release) / E1 (metrics) |
| CI2026-036-013 | 2026-07-23 / — | Text attribution separates colleague, Loop and agent edits | plan not stated; applies to text, not code | [changelog](https://linear.app/changelog/2026-07-23-agent-assisted-editing) | none | E2 |
| CI2026-036-014 | 2026-07-23 / — | GitHub Copilot cloud agent for Linear is GA | Copilot paid plans; org owner + workspace admin required | [GitHub changelog](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available/) | [DevOps.com](https://devops.com/github-gives-teams-more-control-over-copilots-cloud-agent-in-linear/) | E2 (second entity) |
| CI2026-036-015 | 2026-07-30 / — | Coding sessions can sign commits with SSH or GPG keys; admins can require it | plan not stated | [changelog](https://linear.app/changelog/2026-07-30-coding-sessions-on-mobile) | none | E2 |
| CI2026-036-019 | 2026-08-20 / 2026-08-20 | Pinned environments; browser self-testing; tokens at provider rates with "no markup" plus **$0.25 per 20-minute sandbox block**; spend limits | effective the same day | [changelog](https://linear.app/changelog/2026-08-20-coding-environments) | none | E2 |
| CI2026-036-025 | 2026-09-24 / — | Adaptive model routing; **environment secrets** in sessions; open-weight GLM sessions; audit log for OAuth revocations | admins choose models | [changelog](https://linear.app/changelog/2026-09-24-new-controls-for-linear-coding-agent) | none | E2 |
| CI2026-036-026 | 2026-09-28 / 2026-09-28 | `@linear/sdk` 97.0.0 becomes ESM-only (a breaking change) | MIT; GitHub release | [release](https://github.com/linear/linear/releases/tag/%40linear/sdk%4097.0.0) | [release list](https://github.com/linear/linear/releases) | E2 |
| CI2026-036-027 | 2026-10-08 / — | Stacked PRs in Diffs; OAuth PKCE must use S256 | GitHub-native stacks only | [changelog](https://linear.app/changelog/2026-10-08-stacked-pull-requests) | [GitHub stacked-PR docs](https://docs.github.com/en/pull-requests/reference/stacked-pull-requests) (search result) | E2 |

**Feature inventory by theme:**

- **Agents and coding.** Code Intelligence → Diffs → coding sessions → environments and browser testing → model routing and open-weight models. Two coding-session model options named on the pages are "GPT-5.6 Luna" (Aug 13) and "Claude Sonnet 5.5" (Oct 8). Both were checked against the raw page text.
- **Recurring automation.** Loops (Jul 20), extended to product-management triggers on Sep 14.
- **Traceability.** Releases links issues to deployments. The changelogs also add a "Missing issue" PR filter (Jun 18), a "Linear issue" magic word (Jul 2), the `updates` magic word (Sep 24) and stacked PRs (Oct 8).
- **APIs, SDK and MCP.** Linear is an MCP client (Apr 23) and runs its own MCP server, which gained tool additions and fixes throughout. Okta-managed MCP authorisation shipped for Claude (Jul 2 and Aug 13). OAuth app manifests (Jun 18). `@linear/sdk` went through **16 major versions** in the window (82.0.0 on Apr 18 to 97.x on Oct 7, per the GitHub release list).
- **Security and governance.** Signed commits (Jul 30), third-party app approval and published outbound IPs (Sep 3), OAuth-revocation audit entries (Sep 24) and PKCE S256 (Oct 8).
- **Risk-increasing defaults.** GitHub code access is now enabled by default when connecting (May 28), and environment secrets are available to the agent sandbox (Sep 24).
- **Third-party agents.** GitHub Copilot cloud agent (GA Jul 23), Vercel Eve (Jun 18) and Ramp's in-house Inspect agent built on Linear's API ([customer story](https://linear.app/customers/ramp)).

**Vendor assertion vs verification.** Every capability above is **vendor-documented (E1/E2)**. None was exercised by this screen, and no neutral E3 test was found.

## 5. What the company says it intends to do

| Paraphrase of public direction (short quotes only) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Coding sessions are a step toward "Self-driving SaaS"; the understanding "stays with the team and deepens with every loop" | [Jun 11 post](https://linear.app/now/coding-sessions-for-linear-agent) | none stated | vision statement, uncommitted | No dated deliverables |
| Keep expanding the agent products (Coding Sessions, Linear Agent, Loops) and grow the team (>30 open roles) | [Aug 26 post](https://linear.app/now/sharing-growth-with-the-people-building-linear) | none stated | stated intention | Hiring and product intent are not delivery evidence |
| Agents will "soon" author more issues than people and integrations combined | [/data report](https://linear.app/data) (index date Aug 17) | "soon" | forecast from vendor telemetry | Paid-workspace data only; PR counts are opened, not merged |
| More capable models may coordinate the tools for more complex tasks; skills let capability grow without enlarging every prompt | [Aug 10 post](https://linear.app/now/how-we-built-linear-agent) | none | tentative engineering outlook | No evaluation data |
| Introductory Loops credits extended through Dec 31 | [Sep 14 changelog](https://linear.app/changelog/2026-09-14-loops-for-product-management) | 2026-12-31 | dated pricing commitment | Pricing after the promotion is not described in the entry |
| Webhook outbound IPs "going live in the next few weeks" | [Sep 14 changelog](https://linear.app/changelog/2026-09-14-loops-for-product-management) | weeks | announced_only | Not checked after Oct 12 |

Linear has no public roadmap, so these are the only attributable forward statements found. They are not a roadmap.

## 6. Independent interpretation: direction and alternative scenarios (conditional, 2027–2031)

These are the researcher's **hypotheses**, not Linear's strategy and not findings.

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| Issue trackers become agent control planes where code is written, reviewed and deployed (issue → session → diff → release) | Chain of Code Intelligence → Diffs → coding sessions → Releases; partner agents (Copilot, Eve, Ramp Inspect) | Bundling for revenue (AI credits) rather than better outcomes; code hosts (GitHub) and IDE agents may keep review and execution | Customers keep review in GitHub; the share of PRs reviewed in Diffs stays small; Linear spins coding back out to partners | low; no independent usage data |
| Agent-authored work items become the majority, raising review and CI cost per human | Vendor telemetry of ~50% agent-created issues; Linear's own CI rework after a ~4x test growth | Selection bias (AI-forward customers); issue counts inflated by automation; PRs counted when opened | Independent data show flat merged-PR or accepted-task rates per human; agent-issue share falls | low–medium; vendor data only |
| Usage-metered agent pricing makes lifecycle cost visible per task | Aug 20 token pass-through plus $0.25 per 20-minute sandbox block; spend limits | Promotional credits hide true cost; pricing may change | Flat-rate bundling returns; cost per accepted task cannot be computed from dashboards | medium for visibility, unknown for cost level |
| Frequent breaking SDK majors keep downstream integration upkeep high | 16 `@linear/sdk` majors in 6 months; ESM-only switch | Majors are mostly generated schema diffs with little practical break | Downstream projects pin old majors without failures; changelog shows mostly non-breaking items | medium (cadence is documented; impact not measured) |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Issue-assigned cloud agents (Linear, Copilot, Ramp Inspect) open PRs from tracker items | Opt-in comparison of issue-delegated agent PRs vs IDE-agent PRs on frozen tasks | Same accepted-task rate; only the entry point differs | Vendor claims (30%, ~700 PRs, 75%) are **not** study data |
| **M2** accepted task quality | Agent browser self-tests and PR review in Diffs | Hidden, independently authored acceptance tests; count refused, failed and abandoned sessions | Self-verification passes while hidden tests fail | Agent screenshots are not independent acceptance |
| **M3** discoverability | Issue/PR linkage (magic words, "Missing issue" filter) may make provenance easier to find | Measure how quickly an outside reader traces a commit to its rationale | No difference compared with GitHub-native linking | Linear workspaces are private; public projects rarely expose them |
| **M4** verified third-party reuse | MIT SDK and API reused by third parties (e.g. Ramp Inspect, per vendor) | Trace consented downstream integrations and their upgrade breaks | SDK reuse is confined to integrators, with many forced upgrades | Stars, downloads and customer logos are not verified reuse |
| **M5** rights/security | Code access on by default; secrets in sandboxes; MCP egress; signed commits; PKCE | Threat-model review of a sandbox workspace with dummy secrets | Controls work as described; or residual exfiltration paths remain | Proprietary service terms; no independent audit found |
| **M6** lifecycle human/energy cost | Metered sandbox minutes and tokens; CI load from agent-written tests | Record review minutes, CI minutes and credits per **accepted** task | Lower authoring time is offset by review and CI | Provider-side energy is unknown; **no token-to-CO2e conversion** |
| **M7** actionable interventions | Release traceability and agent guidance as maintainer practices | Section 8 experiment | No measurable benefit for a small repo | One maintainer, small N; not generalisable |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The task pool is its open documentation and test-only issues (no capture, network or source-access code). Live Trending `capture` stays disabled under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md), and no tool changes that.

**Candidate practice (not validated):** delegating small issues to an **issue-tracker-assigned cloud coding agent** that opens a PR, compared with the maintainer's existing local agent workflow. GitHub's own **Copilot cloud agent assigned from a GitHub issue** is the reuse-first option because it needs no new tracker. A Linear workspace with coding sessions is tested **only if** its terms, data-access scope and credit budget are approved first.

**Treatment/control and frozen task:**

- Pre-register **10 small issues**: docs fixes, test additions and validator messages.
- Write the acceptance criteria before any attempt. The **hidden acceptance tests** are authored by someone other than the agent and kept out of its context.
- Assign the issues alternately, by a sealed list, to:
  - (A) the existing local agent workflow plus a GitHub PR, or
  - (B) an issue-assigned cloud agent: GitHub Copilot cloud agent, or Linear coding sessions if approved.
- Pin models and harness versions where the product allows it, and record them when it does not.

**Accepted-task functional unit:** one issue whose PR passes the hidden tests and the existing CI (`python -m unittest discover -s tests -v`, `scripts/check_research_artifacts.py`), and that the maintainer merges without rewriting more than 20 lines. The denominator is **all 10 assigned issues**, including refused, timed-out and abandoned ones.

**Guardrails:**

- Use a throwaway fork or sandbox with **no** real secrets.
- Which arm produced each PR is logged in the private trial record. Commits follow the repository's existing authorship policy.
- Stop if the agent touches capture or network code, any dependency is added without review, or any secret or personal data appears in logs.

**Measured human work:** the maintainer's wall-clock minutes for issue writing, steering, review and rework, CI minutes and credits or tokens charged, each logged per issue. Energy is reported **only** if metered, with no token-to-CO2e conversion.

**Stop rule:** abandon (B) if its accepted-task rate is not higher than (A)'s, or if its review-plus-rework minutes per accepted task exceed (A)'s by more than 25%. Also stop on any guardrail breach. A null or negative result is kept and reported.

**Status:** **not executed. No effects are estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (vendor-documented, E2):** 19 dated changelog entries in the window, 18 of them in the ledger. Together they show Linear moving from tracker to agentic code workflow: Code Intelligence (beta), Diffs, coding sessions with metered pricing, Loops, Releases, stacked PRs and several governance controls. There were also 16 `@linear/sdk` major releases, and GitHub reports Copilot-for-Linear GA.
- **Claims and announcements only (E1):** usage and financial metrics (ARR, 40,000 paying companies, 177% NRR, agent share of issues, 30% of bugs, ~700 PRs, Ramp 60% → 75%), the $99M tender and "self-driving SaaS" direction statements.
- **Conjectures and unknowns:**
  - real adoption and accepted-task quality;
  - independent security review of code access, sandbox secrets and MCP egress;
  - coding-session beta vs GA status;
  - exact release days for two entries;
  - pricing after the promotions;
  - filing-level corporate structure.
- **Contradictory or null evidence:**
  - "Coding Sessions (Beta)" on the pricing page (third-party tracker) vs no beta label in the changelog;
  - Diffs slug 05-27 vs displayed May 28;
  - Loops for product management shown as Sep 14 vs Sep 10;
  - Ramp figure of "over 60%" (Jun 11) vs "75%" (Aug 31, undated page);
  - the vendor's own report says the coding-agent teams "were already higher-output before coding agents existed, so the levels aren't directly comparable" (quote corrected 2026-10-16);
  - no neutral evaluation was found.
- **#56 linkage:** candidate news leads for later human verification are CI2026-036-010 (LeadDev) and CI2026-036-014 (GitHub changelog, partner). **No NEWS ID minted.**
- **Reviewer links and audit date:** **pending.** A qualified human should:
  1. spot-check at least 5 rows against the live pages, including the two date conflicts;
  2. confirm the 16-major SDK count;
  3. re-run the search log queries with recorded result counts.

  Only then should #103 be considered for closure.

## Independent source spot-check (2026-10-16)

A second AI-assisted pass re-read 14 ledger rows plus the entity claim against the cited sources on 2026-10-16. Figures, dates and quotes were matched against raw page text (`curl` plus text grep) or the GitHub REST API. No page was archived or hashed. This also covers the reviewer tasks listed in section 9: both date conflicts and the 16-major SDK count.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (section 2) | confirmed | Terms page: "Effective date: June 09, 2026", service "PROVIDED BY LINEAR ORBIT, INC.". Filing-level structure is still not checked |
| 003 | confirmed | Changelog dated April 30, 2026: "up to 15 release pipelines on Business, or unlimited on Enterprise" |
| 006 | confirmed | Page displays May 28, 2026 while the slug says 05-27 (conflict stands as recorded); Diffs "available now on all plans"; guided reviews in beta for Business/Enterprise; "Connecting GitHub now defaults to enabling code access" |
| 007 | confirmed | Dated June 11, 2026; "roughly 30% of incoming bug reports"; Basic/Business/Enterprise; AI credits. No "beta" label on the changelog page. The PricingSaaS tracker does record "Coding Sessions (Beta)" between its Jun 8 and Jun 15 captures |
| 008 | confirmed | June 11, 2026: "almost 700 PRs were merged by the agent"; Ramp Inspect "more than 60% of the pull requests they merge" |
| 010 | confirmed | LeadDev, June 25, 2026: "30% more PRs, 33% more issues closed"; Tom Moor, head of engineering, "over 50% of PRs generated by the coding agent are mergeable" |
| 014 | confirmed | GitHub changelog July 23, 2026: GA; Copilot Pro, Pro+, Business and Enterprise; GitHub organisation owner plus Linear workspace admin required |
| 017 | confirmed | Changelog August 13, 2026: "Added GPT-5.6 Luna as a model option"; Okta-managed MCP authorisation for Enterprise with Okta SAML |
| 018 | corrected | Figures confirmed (Aug 3, 2026 week: 2,435 agent/MCP vs 2,481 people/integrations issues, i.e. just under half; PRs counted when opened). The report's quoted phrase "is not like-for-like" does not appear on the page. The actual wording is "the levels aren't directly comparable", so the quote is corrected in section 9 and the CSV limitation |
| 019 | confirmed | Changelog August 20, 2026: "Starting today"; tokens at provider rates "with no markup"; sandbox runtime "$0.25 per 20-minute block"; workspace and per-user spend limits |
| 020 | confirmed | August 26, 2026: $99 million tender at a $2.5 billion valuation; Accel and 01A plus Salesforce Ventures and S32; ARR passed $100M; more than 40,000 paying companies; NRR 177%; agents in 95% of paid workspaces; agent-created share 50% |
| 021 | confirmed | Customer page: "three of every four PRs Ramp merges". The `/now` index dates it "Aug 31, 2026" |
| 023 | confirmed | Entry page shows September 14, 2026 while the `/now` index lists "Loops for product management" under Sep 10, 2026 (conflict stands as recorded); credits extended "through December 31"; outbound webhook IPs "will go live in the next few weeks" |
| 026 | confirmed | GitHub API: `@linear/sdk@97.0.0` published 2026-09-28T13:43:54Z, ESM-only. In-window SDK releases: 24, with majors 82.0.0 (2026-04-18) through 97.0.0, i.e. **16 majors** (81.0.0 was 2026-04-07, before the window). Repo licence MIT |
| 027 | confirmed | Changelog October 8, 2026: "Required an explicit S256 method for PKCE"; "Added Claude Sonnet 5.5 as a coding session model"; GitLab token renewal |

**Outcome counts:** 15 checks (14 rows plus the entity claim): 14 confirmed, 1 corrected (a misquoted phrase; the underlying data were right), 0 unverifiable, 0 wrong. No fabricated URL or figure and no contamination from another company was found. Event IDs are unchanged.

*This is an AI-assisted source spot-check. It is not a qualified human factual, rights or methods review, and those reviews remain pending.*
