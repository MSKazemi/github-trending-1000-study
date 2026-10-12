# Next steps — execution plan after whole-repository audit (2026-10-12)

**Status:** proposed and not preregistered. Maintainer approval required; no enrollment, independent reviewers, measurements or third-party permissions are implied. **Audit:** [repository-wide review](REPOSITORY_AUDIT_2026-10-12.md); [audit PR #45](https://github.com/MSKazemi/github-trending-1000-study/pull/45); [tracking issue #44](https://github.com/MSKazemi/github-trending-1000-study/issues/44).

## One decision that controls all priorities

The primary research mission is **modern AI-era software development and evidence-backed code reuse**, including useful, trustworthy, sustainable software and lessons for 2027 maintainers. **GitHub Trending is the observational discovery/attention track, not a proxy for reuse or quality.** Run two separate designs:

- **Study A (observational):** dated, permitted, independently quality-audited Trending appearances and comparator repositories; investigate *associations* with future attention and externally verified adoption, never treat stars as impact.
- **Study B (task experiment):** eligible real development tasks chosen before search, independently frozen acceptance tests, and a consented reuse-first vs usual workflow comparison; track all assigned attempts, real human burden and verified outcomes. This supplies the **main causal test of reuse-first coding** if randomization and prerequisites are satisfied.
- Connect studies at the later interpretation stage using evidence-provenance tables; **do not merge different units, populations or causal estimands into one score**.

## Priority work queue — every step has an evidence gate

| Order / urgency | Bounded action and existing issue | Implementer / necessary human decision | Definition of done; not just 'CI green' |
|---|---|---|---|
| **0 / immediately** | **Review and merge the [audit PR #45](https://github.com/MSKazemi/github-trending-1000-study/pull/45)** after confirming evidence, or request corrections. | Maintainer + AI drafting support | Dated report visible from `main`, issue #44 tracked/closed only when genuinely complete; no auto-merge assumed. |
| **1 / first code change, P0** | **Fix source overwrite and collision paths** in `capture`, `parse-trending`, `pilot-parse`, `enrich`; [issue #4](https://github.com/MSKazemi/github-trending-1000-study/issues/4). | AI/engineering contributor; maintainer code review | New files created exclusively; raw source and manifest are not silently replaced. Re-running same names and input=output fail *before changing bytes*. A partial/crash/retry test verifies a recoverable state. Atomic/staged writing where appropriate; all Python 3.10/3.12 CI tests pass. |
| **2 / P0** | **Repair reviewer→gold-set availability-only failure**, [PR #43](https://github.com/MSKazemi/github-trending-1000-study/pull/43), then revalidate source pool and human judgment schema. | AI contributor; independent methods reviewer + maintainer | Synthetic round-trip demonstrates a task-baseline-later release can be classified temporal-not-viable **without inventing a failed functional gate**. Unknown evidence remains unknown; `goldset.evaluate` can consume the documented output. No claim raters were real or code was tested. |
| **3 / P0** | **Review and integrate selected existing PRs**: [#42 mission](https://github.com/MSKazemi/github-trending-1000-study/pull/42), [#38 task-intake](https://github.com/MSKazemi/github-trending-1000-study/pull/38), [#43 reviewer](https://github.com/MSKazemi/github-trending-1000-study/pull/43) after fix, [#34 assignment](https://github.com/MSKazemi/github-trending-1000-study/pull/34); consider [#35 evidence watch](https://github.com/MSKazemi/github-trending-1000-study/pull/35) separately after checking references. | Maintainer decides; AI rebases/resolves conflicts and tests | PR branch rebased against latest `main`; reviewed methodology; targeted cross-module integration tests, consistent IDs/timestamp/schema and full CI. Preserve synthetic/not-reviewed labels. Do not merge a PR because CI alone passed; #34 and #38 reported conflicts in the audit. |
| **4 / P0 source validity** | **Conduct permitted real-page parser QA**, [issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2), and stable-ID capture follow-ups [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4). | Maintainer confirms GitHub access terms; AI captures only as permitted; independent human checks raw/visible sample | Dated immutable raw+manifest captures; **at least 30 independently hand-checked visible rows** across allowed supported surfaces; extraction precision *and completeness* with skips/rank audit; numeric repo IDs and missingness ledger. Flag failure; no inferential cohort enrollment. |
| **5 / P0 study decisions** | **Consolidate and freeze draft protocol** [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27), [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13). | Independent methods/statistical reviewer, data/privacy steward and maintainer; AI can assemble draft | Explicit Study A/B units, estimands, priority endpoints and missingness; predeclared sampling, exclusions, leakage handling, multiplicity, minimum important effect, power simulation; source rights and consent approval; true external time-stamped registration *before* confirmatory data/outcomes. Draft signoff without named consent/approval is not sufficient. |
| **6 / P0 gold standard** | **Build real, task-first, permission-respecting task set**, [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21) and [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22). | AI supports structured intake/search; independent humans write acceptance tests and judge; maintainer checks risk | Versioned source-frame ledger with inclusion/exclusion, tasks selected **without knowing reuse opportunity**; baseline repo commit & UTC, frozen independently authored requirements/tests; candidate pool from >=2 independent discovery channels plus deep/random audit; two blinded independent judgments, documented disagreement, version/license/provenance/security/maintenance gates. Unknown is never silently negative; no untrusted third-party code run on credentialed CI. |
| **7 / next feasibility stage** | **Run a small, consented, permission-safe experiment pilot** [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), [#17](https://github.com/MSKazemi/github-trending-1000-study/issues/17). | Actual consenting developers and independent adjudicators; statistician reviews study design | Illustrative **12–20 diverse tasks** *only to debug feasibility*, not a power claim. Preassign conditions, freeze agent/model/tool versions and independent tests, retain failures/refusals/missing costs and non-reuse opportunities, log actual active human minutes, provider token/accounting when accessible, CI workload, rights/security flags. Pilot variance/attrition informs **future** N. No confirmatory p-values from this convenience pilot. |
| **8 / parallel, after valid source capture** | **Develop the prospective Trending cohort and comparison frame**, [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4), [#15](https://github.com/MSKazemi/github-trending-1000-study/issues/15). | AI can build collectors under approved source rules; statistician/maintainer approve | Explicit frame, permitted schedule, failure log, stable repo IDs, baseline and 30/90/180d snapshots; controls sampled from independent documented frame, distinguish not-observed from never-trended; uncertainty and attrition. **1,000 is a feasibility target, not current N.** Unsupported six language surfaces cannot be counted as captured. |
| **9 / after a credible pilot** | **Lifecycle and social-cost measurement**, [#10](https://github.com/MSKazemi/github-trending-1000-study/issues/10), [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18), [#23](https://github.com/MSKazemi/github-trending-1000-study/issues/23), [#24](https://github.com/MSKazemi/github-trending-1000-study/issues/24). | AI can build logging/analysis; humans supply permission and meter data | Equivalent accepted functionality and defined horizon; separate measured energy from modeled/unknown model-provider inference; report carbon intensity, CI, runtime, updates, maintainer burden, rebound and uncertainty. Never compute verified kWh/CO2 solely from token counts. |
| **10 / evidence output** | **Produce publishable figures and reusable developer lessons**, [#7](https://github.com/MSKazemi/github-trending-1000-study/issues/7), [#11](https://github.com/MSKazemi/github-trending-1000-study/issues/11), [#12](https://github.com/MSKazemi/github-trending-1000-study/issues/12), [figure plan](FIGURE_TABLE_PLAN_2027_2031.md). | Researchers + technical maintainers | Reproducible input hashes/scripts and traceable claims; sample-flow, uncertainty, negative results and applicability; separately validated recommendations for actual repositories; release only licensed, rights-permitted and privacy-safe artifacts. |

## Suggested near-term sequence (illustrative, not a research schedule commitment)

### First 3 working days — engineering safety

1. Human: review PR #45 and accept/correct this priority plan.
2. AI/engineering: tackle *only* [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4) in a focused PR: refuse overwrites, prevent every input/output collision, add deterministic offline tests, update collector SOP and README.
3. AI/engineering: submit a focused follow-up on PR #43 proving the availability-only negative case; maintainers verify compatibility. Keep this separate from source-capture work.
4. Triage the outstanding PR dependency/conflict matrix; do **not** close #21 or #25 for synthetic instrumentation alone.

### Following 1–2 weeks — prepare validated pilot inputs

1. Human: approve/decline permitted GitHub access and collection cadence. If approved, create a small, **explicitly observational pilot** with actual raw and date/HTTP manifests and independent >=30-row manual QA.
2. AI + reviewers: convert independently screened public task *leads* into fully frozen task specs/tests. Store task hashes/UTC, baseline commits, version and rights information; mark unreviewed as unknown.
3. Statistician/qualified reviewer: reconcile the primary protocol with separate Study A/Study B outcomes; decide whether four arms are feasible and simulate study power/precision.
4. Merge only reviewed, mutually compatible tooling changes into `main`.

### After prerequisites — small experimental pilot then go/no-go

1. Recruit consenting developers/reviewers and run a **small feasibility pilot** with all-task denominator. `12–20` is a planning illustration, not statistically sufficient N.
2. Publish attrition, independent task acceptance, retrieval coverage, full human effort and provider-data missingness.
3. Decide whether the design can produce interpretable causal results. If not, revise and re-register **before confirmatory recruitment**; preserve negative feasibility findings.

**Date safeguard:** the existing proposed **2026-10-15–31** collection pilot and **2026-11-01** confirmatory start are *conditional drafts*. If access, quality, task-frame, power, registration or review gates are unmet, record a **dated future-start amendment**; never backdate present-day metadata as historical Trending.

## What we can implement directly vs cannot claim to do

| Can be prepared/implemented with repo access | Requires actual human/authorized resource |
|---|---|
| Data-safe file writes, CLI guards, schemas, tests, CI and documentation | Human scientific/ethics/statistics approval; external preregistration when necessary |
| Deterministic offline candidate intake/review packets, records and screening interfaces | Actual independent test authors and blind reviewers; their identities/permission cannot be invented |
| Synthetic integration tests and auditable figure/table pipelines | Real consented participants, actual measured resource costs and true task outcomes |
| Dated evidence register, issue/PR review workflow and developer lesson templates | Source access permissions, dataset rights, maintainer review/merge decisions |

## Do **not** spend time on these before the pilot

- Ranking "top 1,000 high-quality repos" as if Trending is an objective quality index.
- Building a new reusable-code registry, clone engine or dashboard before testing whether the existing GitHub/package/semantic tools miss meaningful opportunities.
- Creating full 2027–2031 forecast graphs without real observed denominators.
- Treating more code, agents, tokens, commits, stars or new repositories as intrinsic scientific success.
- Making broad green/energy/marketing claims from proxies.

## Short practical playbook for the maintainer's own repositories

Before adding a substantial feature to any repository, record the **real external user's task**, search local/upstream/registry prior work with a fixed time budget, compare reuse/extension/upstream patch/minimal implementation, lock acceptance/security/license criteria, execute a fresh-install task test, publish small stable releases with examples, and seek one independently reproducible downstream use. Report maintenance/review burden and 30/90-day outcome where feasible. This is **a testable engineering guideline, not an established star-growth or carbon-savings result**.

**Next implementation target:** the **#4 no-overwrite/provenance integrity change**, then **#43 availability compatibility**, with the **#2 permitted real-page audit** being the first indispensable external-data gate.