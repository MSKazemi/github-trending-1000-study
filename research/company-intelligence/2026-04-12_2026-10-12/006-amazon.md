# Amazon / AWS — six-month AI/software company intelligence (initial source screen)
 
- **Watchlist ID:** 006
- **Issue:** [#72](https://github.com/MSKazemi/github-trending-1000-study/issues/72)
- **Period:** 2026-04-12 to 2026-10-12 inclusive, calendar publication dates.
- **As-of source review:** 2026-10-12.
- **Research status:** **INITIAL source-screened draft only**. Not a complete six-month systematic search, independently adjudicated result, formal peer review, real product deployment test, or study finding.
- **Company sector:** AWS developer tooling, cloud agents and Bedrock.
- **Official publication entry:** https://aws.amazon.com/blogs/devops/
- **Individual machine-readable events:** [006-amazon.events.csv](006-amazon.events.csv).
- **Methods:** [company-source protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md); [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

## 1. Search and coverage audit

Source screening consulted the linked first-party publication/archive pages, product announcement text and relevant source discovery for this organization as of 2026-10-12. The following are **reproduction search suggestions**, not a log claiming these literal exact queries were all executed. They should be run independently for every month, in official and high-quality secondary sources, before final issue completion:

1. `"Amazon / AWS" after:2026-04-11 before:2026-10-13 agent coding open weights`
2. `site:aws.amazon.com 2026 model launch agents`
3. `"Amazon / AWS" 2026 developer API security pricing`
4. `"Amazon / AWS" 2026 independent benchmark and criticism`

**Audit limitations:** Search-hit totals, all screened/excluded URL counts, frozen web snapshots, completeness/recall and an independently audited secondary corpus were **not measured**. The included events below are a bounded purposive screen, not an enumeration of every release. The seven partial/full month segments are displayed even when an event was not found. **An unfilled month is missing evidence, not a zero-activity finding.** Verify link accessibility, page update history, publication timezone, actual release date vs article date and region/plan availability before declaring the report done. No web scraping or private-user data collection.

## 2. Identity and product boundary

Amazon.com, Inc. operates Amazon Web Services (AWS). Amazon Q Developer, Kiro, and Amazon Bedrock are distinct products, not interchangeable brand names; each has a different support, data and billing boundary.

Public first-party landing/news channels identify product offerings, but this report does not independently verify corporate cap tables or product rights. Amazon's 2026-04-30 post dates IDE-plugin support end to 2027-04-30, while preserving AWS Console Q; do not misreport this as a 2026 product shutdown.

## 3. Month-by-month candidate events

| Period | Source-linked discovered candidate(s) | Coverage characterization |
|---|---|---|
| 2026-04-12..30 | [Amazon Q Developer support transition](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) | First-party pages; see events |
| 2026-05 | [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/) | First-party pages; see events |
| 2026-06 | [Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/) | First-party pages; see events |
| 2026-07 | [Control framework for AI coding agents](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/) | First-party pages; see events |
| 2026-08 | [AWS Continuum developer workflow](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/) | First-party pages; see events |
| 2026-09 | No event documented in this bounded source subset | Unresolved coverage; not evidence of inactivity |
| 2026-10-01..12 | No event documented in this bounded source subset | Unresolved coverage; not evidence of inactivity |

## 4. Dated evidence and feature map

| Event | Published / underlying event | Source-linked provider claim or dated documentary event | Availability / constraint | Evidence grade and independent check | Relevant objectives |
|---|---|---|---|---|---|
| CI-006-01 | 2026-04-30 / event day not independently timed | [Amazon Q Developer support transition](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) — AWS announces April 30 2027 end-of-support for Q Developer IDE plugins/subscriptions; encourages Kiro migration. | announced_only; Future 2027 sunset; AWS Console and some first-party Q surfaces explicitly unaffected. | Provider E1; independent efficacy **not** verified | M1;M4 |
| CI-006-02 | 2026-05-18 / event day not independently timed | [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/) — Kiro announces web workflow for delegated development tasks. | preview; Preview status and region/plan scope may vary. | Provider E1; independent efficacy **not** verified | M1;M2 |
| CI-006-03 | 2026-06-19 / event day not independently timed | [Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/) — AWS presents Kiro integration with AWS DevOps Agent. | shipped; Availability is vendor-described; task cost and reliability unmeasured. | Provider E1; independent efficacy **not** verified | M1 |
| CI-006-04 | 2026-07-30 / event day not independently timed | [Control framework for AI coding agents](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/) — AWS publishes author/build-time controls and governance guidance. | reported_undetermined; Security guidance is not empirical evidence of effectiveness. | Provider E1; independent efficacy **not** verified | M2;M5 |
| CI-006-05 | 2026-08-05 / event day not independently timed | [AWS Continuum developer workflow](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/) — AWS announces partner-integrated code-security workflow. | preview; Preview; performance and measured vulnerability reduction unverified. | Provider E1; independent efficacy **not** verified | M2 |

**Grading:** **E1** = provider-described release or policy. It supports attribution and reported availability, **not** reproducible behavior, quality, adoption or effectiveness. API version/docs and actual package licenses remain to be independently inspected; **E3/E4 is not awarded** to vendor metrics. The event CSV separately records class, observed limitations and link provenance. `shipped` means the **provider described availability** on the date, not independently validated access. **No claims about measured carbon impact or representative adoption.**

### Feature, integration, licensing and security boundaries

- **Current/new capabilities reported by provider:** AWS publicly shifts coding workflow focus from Q Developer IDE plugins toward Kiro's specification-led agent environment while extending hosted/cloud agent operations.
- **Availability:** check every event's status (including preview and future-only); descriptions of features are not interchangeable with externally accepted user tasks.
- **Open-source/API/license:** A Q Developer IDE **future** sunset is not a completed 2026 shutdown. AWS explicitly keeps Q Developer in AWS Console and first-party surfaces outside the scheduled plugin sunset.
- **Security and provenance:** do not execute untrusted build instructions, model install scripts or agent-recommended dependencies; record exact artifact identities, license, origin, signing/release tag, vulnerability results and permissions.
- **Economic context:** model/API prices, tokens, human review, CI and ongoing support must be measured per functional task. Vendor throughput claims are not metered kWh or emissions.

## 5. Public roadmap / intention (not independently guaranteed)

**Direction attributable to the company's publications:** AWS publicly shifts coding workflow focus from Q Developer IDE plugins toward Kiro's specification-led agent environment while extending hosted/cloud agent operations.

A roadmap statement, planned support sunset, future model release or planned deployment **must not** be counted as generally available in the window. See specific `announced_only` and `preview` items in the dated table. Commitments are scope- and time-specific, and product marketing is a weaker evidence class than a pinned artifact and repeated independent task result.

## 6. Analyst interpretation, alternatives and disconfirmation (2027–2031)

| Conditional inference — NOT company commitment | Motivation | Rival explanation | Disconfirming observation |
|---|---|---|---|
| Agent orchestration via spec-driven workflows could improve maintainable integrations when tests and approvals travel with tasks. | Above source-linked product directions (E1) | Migrating from Q to Kiro can impose license, workflow and retraining costs without user-outcome gains. | Stable legacy CLI+tests achieve equal accepted tasks with lower total burden. |

**Confidence:** exploratory/low until independent task comparisons and lifecycle measurement. Some genuinely useful reusable components predate this six-month interval; they remain eligible as controls/candidates, not excluded as old technology.

## 7. Mapping to the study's M1–M7 objectives

| Question | Needed observation rather than a product popularity proxy |
|---|---|
| M1 agent/workflow change | Timestamped, consented and version-pinned task use; feature availability is **not adoption** |
| M2 accepted quality and review load | Frozen external acceptance suite; failures, review minutes, defects and follow-up counted for **all assigned tasks** |
| M3 discoverability | Prospective matched repo controls and pre/post visibility measures with exposure/selection confounding |
| M4 independent reuse | Audited outsider import, deployment or working repeat-use; stars and installs alone insufficient |
| M5 reuse vs rebuilding | Pre-screened OSS candidates, provenance/license/security, missing/no-solution cases and same objective task |
| M6 whole lifecycle | Same functional unit; human time, provider costs, CI/hosting, runtime, upgrades and upstream burden; kWh only if metered or transparently modeled |
| M7 maintainer intervention | Ethics-reviewed opt-in onboarding/API/docs intervention; independent first-use success and no artificial star boosting |

These are study **measurement targets**, **not observations** of M1–M7 effects in this report.

## 8. Practical, falsifiable pilot for the maintainer's own repository

**Repository:** [GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study) (existing offline CLI and synthetic fixture; do not scrape live Trending).

**Practice to test:** Use the current offline synthetic Trending fixture to compare the existing documented CLI workflow with a frozen requirements/spec card for a delegated change to the *existing* parser.

**Treatment/comparator:** A: baseline agent or human prompt with current docs; B: the same task with a reusable spec, review gate and preselected existing CLI; pin versions and independent tests.

**Freeze before treatment:** same repository SHA, dependency/model versions, synthetic inputs, objective expected outputs, task/time cap and evaluator; record failures and no-solution tasks. A second person creates or freezes acceptance tests before any agent-generated change.

**Primary outcome and verifiable reuse:** Outside evaluator accepts no-regression parser output and rejects malformed input as expected; record attempts, reviewer minutes, cost, and 30-day issues.

**Costs / constraints:** record active human time, reviewer minutes, task-level billed/model tokens where known, CI runtime, 30-day defects, code provenance, package-license/security checks and any upstream support work. Tokens/LOC/stars are **not kWh or CO2e**. Prospective experiment **not run**; sample size/power and human consent not secured.

**Stop/reversal:** Do not adopt the spec-agent layer if it increases review time without better accepted work, creates uncontrolled AWS use, or violates source-access policy.

**Transferable maintainer lesson:** prefer a reusable, versioned interface with an independently testable first-use task over a flashy new repository; test whether verified outside use improves without shifting hidden maintenance/security costs.

## 9. Evidence quality, counterclaims and pending QA

- **Observed in documentation:** 5 directly linked dated source events, primarily first-party. Only the publication/product claims and their reported availability are supported.
- **Not demonstrated:** independent feature efficacy, benchmark validity, customer/OSS adoption, earned GitHub attention, per-task cost savings, kWh/CO2e, or causal environmental benefit.
- **Counterclaim / specific uncertainty:** Amazon's 2026-04-30 post dates IDE-plugin support end to 2027-04-30, while preserving AWS Console Q; do not misreport this as a 2026 product shutdown. Migrating from Q to Kiro can impose license, workflow and retraining costs without user-outcome gains.
- **Required next verification:** (1) independent second-reviewer date/link/identity pass; (2) seven-segment systematic queries with preserved screen counts and exclusion rationale; (3) inspect exact weights/code license, APIs, prices, status and data policies; (4) seek credible independent adverse/critical reporting; (5) duplicate/correction and secondary coverage audit; (6) independent task trial and tests before recommending broad adoption.
- **Review state:** analyst-drafted with source URLs, independent human factual QA **pending**, no full Python test suite run for this documentation-only proposal. Keep the issue and PR open/draft; **do not merge** or close until criteria satisfied.
- **Cross-link:** distinct validated articles may enter [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) after its own verification; no `NEWS-` ID minted by this screen.

**Validity conclusion:** The only defensible output here is a **testable engineering hypothesis** and a documented source shortlist; not a conclusive company ranking or a green-coding result.

### Documentary recheck — 2026-10-13 (analyst pass, not independent reviewer)

- [Amazon Q Developer transition, dated April 30](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/): IDE plugins and paid Q Developer subscriptions are scheduled for **end of support April 30, 2027**, not shutdown in the 2026 collection window. New signups were scheduled to stop **May 15, 2026**; existing customers retain relevant access through the transition. **Q Developer in AWS Management Console and specified first-party AWS surfaces is explicitly excluded from this sunset**. Preserve product/channel-specific denominators when counting retirements.
- [Kiro Web announcement](https://kiro.dev/blog/introducing-kiro-web/) describes **preview** for paid subscribers. The referenced trial/rollout should not be counted as fully available or supported in all environments.
- [June 19 AWS blog](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/) documents a Kiro Power connecting the IDE to AWS DevOps Agent. A provider how-to supports the integration description, **not** independent improvement in incident resolution, accepted code or energy use.

**Practical reuse gate:** Record provider, product, host surface and announced support-end date in dependency decisions. Run a migration acceptance test using the current pinned project CLI before replacing a working path with an agent platform.


## Evidence-preserving reconciliation of competing drafts (2026-10-13)

This source-screened working report retains the full **original PR #192 report** and its factual limitations. Later [draft PR #229](https://github.com/MSKazemi/github-trending-1000-study/pull/229) was separately prepared and includes unique source observations, caveats and a proposed experiment. Its exact original Markdown is preserved in [the dated source archive](source-archives/006-amazon.2026-10-13-first-screen.md); the initial 22-column CSV (including the original evidence tiers and statuses) is preserved unchanged as [the earlier event ledger](source-archives/006-amazon.2026-10-12-source-ledger.csv). Both are **provenance archives, not independent corroboration**.

**Canonical working event index:** [006-amazon.events.csv](006-amazon.events.csv) contains 8 deduplicated *publisher URL leads*: 4 retained from the newer screening plus 4 unique older URLs. Older-only candidates are conservatively marked `E0_ARCHIVED_UNREVIEWED_VENDOR_LEAD` until independent URL/date/content QA, while the archived older labels remain unchanged. Event IDs and original unreviewed claims are preserved, not reset or silently backdated.

| URL in both screens | Original status | Newer status | Required disposition |
|---|---|---|---|
| No differing categorical labels identified | — | — | Source assertions still require human verification |

### Unique source material from each branch

**Earlier screen source leads retained in the canonical CSV (archived E0 until checked):**
- 2026-05-18: [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/), prior status `preview`, prior tier `E1` (author's working label; not independent product proof)
- 2026-06-19: [Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/), prior status `shipped`, prior tier `E1` (author's working label; not independent product proof)
- 2026-07-30: [Control framework for AI coding agents](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/), prior status `reported_undetermined`, prior tier `E1` (author's working label; not independent product proof)
- 2026-08-05: [AWS Continuum developer workflow](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/), prior status `preview`, prior tier `E1` (author's working label; not independent product proof)

**Later screen unique links (publisher working records):**
- 2026-05-12: [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/) — `shipped`; source-bound, not an independent effectiveness test
- 2026-10-09: [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) — `preview`; source-bound, not an independent effectiveness test
- 2026-10-12: [CLI changelog: version 2.30.0](https://kiro.dev/changelog/cli/) — `shipped`; source-bound, not an independent effectiveness test

**Scientific and release gate:** source QA is incomplete: query-result denominators, revisions, contradictory/independent journalism, verified first availability, exact rights/licenses and genuine independent human factual review are outstanding. The two PRs must not be represented as completed company investigations. No participant task, provider workload, environmental footprint or software adoption result was measured. Leave issue #72 open until study acceptance is satisfied.


## Dated public-source desk check — 2026-10-14 (AI-assisted; not independent human review)

**Limited evidence action:** On 2026-10-14 an AI-assisted desk check read one *public publisher-controlled page* for this issue. This is a dated source-text cross-check, **not** an authenticated archived capture, complete seven-segment search, independent source corroboration, signed reviewer approval, executed installation or empirical task outcome. The event ledger's evidence tier is **not** upgraded by this check.

- **Publisher page and source publication date:** [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) — 2026-10-09 (publisher-stated date; access check 2026-10-14).
- **Source-attributed observation:** The Kiro publisher distinguishes June opt-in V3 from startup prompts gradually beginning 12 October and a planned general default by the end of October. The latter is future intent relative to the study's 12 October cutoff.
- **Correction / uncertainty to retain:** Do not label CLI V3 universally default or the late-October change completed as of 12 October. Page text is a first-party rollout claim, not an install-verified release population or independent performance outcome.
- **Falsifiable maintainer experiment (not performed):** Freeze a small spec-driven code-change task and compare documented spec/review-first flow with a baseline. Require clean-room acceptance and source/security checks; record task refusals and actual reviewer effort rather than promotional speed.
- **Remaining research gate:** Verify a versioned/retrievable first-use source record, all seven period segments with exact query/result/exclusion logs, independent critical/contrary evidence, licenses and rights, and a qualified human reviewer before considering the research issue complete. No user-adoption, carbon, causal or real-task benefit claim is made here.
