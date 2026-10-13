# Replit — company intelligence, preliminary six-month source screen

- **Watchlist entry:** 014
- **Research issue:** [#80](https://github.com/MSKazemi/github-trending-1000-study/issues/80)
- **Retrospective publication interval:** 2026-04-12 to 2026-10-12 inclusive.
- **Prepared/source-reviewed:** 2026-10-12.
- **Status:** INITIAL screened research DRAFT (not fully systematically collected or independently reviewed).
- **Coverage:** vendor/official notices for agentic hosted IDEs, prompt-to-app workflows and developer deployment; [official index](https://replit.com/blog). Each event has canonical source URL in [CSV evidence ledger](014-replit.events.csv).
- **Methods:** [company methodology](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) and [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

## 1. Discovery and inclusion audit (incomplete)

This is a **bounded primary-document evidence shortlist**, not a systematic seven-month search. Source discovery/review occurred on 2026-10-12; **search-engine result counts, complete query clickstream, number screened, excluded URLs and full independent source screening were not preserved**, therefore they are **unknown**, not zero. Reproducibility queries below are **next-pass suggestions, not claims that each exact expression was executed**:

- `"Replit" after:2026-04-11 before:2026-10-13 coding agent releases security`
- `site:replit.com 2026 model tool changelog license agent`
- `"Replit" 2026 API roadmap change security acquisition`
- `"Replit" Reuters OR TechCrunch OR The Register 2026 criticism independent audit`

For final issue acceptance, search each full/partial month separately in primary/independent outlets, log exact run UTC/timezone, immutable query/results and reason for inclusion/exclusion; inspect releases, product docs, public source licenses and pricing; preserve zero-result screens as **search results missing/not found**, not proof of corporate inactivity. Vendor news can change after initial publication and lacks immutable full-text snapshot here. Don't deduplicate separate feature announcements into mere publicity count or count syndications as independent product confirmations.

## 2. Entity, products, availability and baseline

Replit Inc. provides hosted development software, including Replit Agent and project hosting. Replit Agent, package firewall and design tools have different implementation/hosting boundaries; published self-reports are not evidence of independently verified downstream use.

**Rights/safety boundary:** The Package Firewall's '8,000 packages daily' is a vendor-reported screening number with unknown denominator/false-positive rate; blocked packages are neither verified security incidents nor accepted-task outcomes.

**Specific correction/ambiguity to preserve:** Replit's self-evaluation claims on model routing and subagent economics are not independently reproduced; hardware/cloud energy unknown.

## 3. Month-by-month dated candidate ledger

| 2026 month segment | Included candidate event/source(s) | Coverage notes |
|---|---|---|
| Apr 12–30 | Not documented in this limited screen | Missing source coverage; not a finding of no releases |
| May | Not documented in this limited screen | Missing source coverage; not a finding of no releases |
| June | [Package Firewall](https://replit.com/blog/package-firewall); [Custom skills for Replit Agent](https://replit.com/blog/custom-skills); [Evaluating and improving Agent at scale](https://replit.com/blog/evaluating-and-improving-agent-at-scale) | First-party sources screened |
| July | [Replit Design](https://replit.com/blog/introducing-replit-design) | First-party sources screened |
| August | [Replit Free Mode](https://replit.com/blog/replit-introduces-free-mode) | First-party sources screened |
| September | [Agent harness subagent selection](https://replit.com/blog/free-the-models) | First-party sources screened |
| Oct 1–12 | Not documented in this limited screen | Missing source coverage; not a finding of no releases |

All dates are **as displayed by the source** and rendered as calendar dates; UTC publication timezone has not been independently established. Underlying launch/deployment date is **not assumed identical** to article date. If page describes a different earlier event, document discrepancy separately; follow-up source audit needed.

## 4. Event and capability map with source-level confidence

| Event ID | Published / underlying event date | Source | Claim or documented change | Reported status and restrictions | Evidence/construct |
|---|---|---|---|---|---|
| CI-014-01 | 2026-06-09; event date not separately verified | [Package Firewall](https://replit.com/blog/package-firewall) | Replit says it defaults a Socket-supported malicious dependency installation firewall on. | shipped; Vendor's 8k blocked/day not independent breach/vulnerability count; updated June 10. | E1; M2;M5 |
| CI-014-02 | 2026-06-10; event date not separately verified | [Custom skills for Replit Agent](https://replit.com/blog/custom-skills) | Replit describes reusable custom instructions/skills for its hosted agent. | shipped; Tier/access and reproducibility of skill interpretation not tested. | E1; M1;M5 |
| CI-014-03 | 2026-06-23; event date not separately verified | [Evaluating and improving Agent at scale](https://replit.com/blog/evaluating-and-improving-agent-at-scale) | Replit describes internal agent evaluation practices and benchmark process. | reported_undetermined; Methodology is vendor-reported, not independent replication. | E1; M2 |
| CI-014-04 | 2026-07-29; event date not separately verified | [Replit Design](https://replit.com/blog/introducing-replit-design) | Replit announces integrated design-related development interface. | shipped; Service availability and external project benefits not verified. | E1; M1 |
| CI-014-05 | 2026-08-18; event date not separately verified | [Replit Free Mode](https://replit.com/blog/replit-introduces-free-mode) | Replit announces a new access mode for building with AI. | shipped; No verified adoption or user task count; pricing/limits must be rechecked. | E1; M1;M4 |
| CI-014-06 | 2026-09-29; event date not separately verified | [Agent harness subagent selection](https://replit.com/blog/free-the-models) | Replit describes dynamic use of specialists and resource allocation; reports own task benchmark comparisons. | shipped; Vendor performance claims lack independent replication and do not prove environmental benefit. | E1; M1;M2;M6 |

**Grade E1 for ALL 6 entries:** vendor/publication statements only. 'Shipped' means provider **reports** availability, not a tested implementation or independent adoption. The separate CSV has source type, first-seen review date, status and missingness fields. An independent assessment is needed for E3 validation; page popularity, benchmarks, stars, press coverage, merger announcements and provider security assertions do not qualify.

### Product impact distinctions

- **Product direction:** Replit is emphasizing workflow-level safety controls, portable/agent-readable skills, hosted design, and agent self-allocated specialist subagent effort.
- **Integration:** pin exact dependency, API, model/version, source commit/weight checksum, task context, deployment and subscription restrictions, instead of comparing names or marketing scores.
- **Security/licensing:** The Package Firewall's '8,000 packages daily' is a vendor-reported screening number with unknown denominator/false-positive rate; blocked packages are neither verified security incidents nor accepted-task outcomes.
- **Economics:** compare matched **independently accepted task** output including human/review minutes, CI/runtime, hosted inference and 30/90-day upkeep. Tokens do not imply kWh or carbon savings.

## 5. Attributed roadmap versus realized release

**Direction is inferred from the vendor publications**, not an independently established plan: Replit is emphasizing workflow-level safety controls, portable/agent-readable skills, hosted design, and agent self-allocated specialist subagent effort.

Any `preview` and `announced_only` record stays distinct from vendor-described general availability. A direction statement or claimed open-source license requires checking the exact artifact. Future intent has no guaranteed release date unless the cited official source explicitly guarantees it; the event table is not a promise calendar.

## 6. Analyst 2027–2031 conditional interpretation

| Hypothesis (not company commitment) | Rival explanation | Observable disconfirmation |
|---|---|---|
| Standard agent instruction files and on-by-default supply-chain checks may improve repeated task acceptance without each maintainer writing a custom harness. | A hosted integrated experience may cause lock-in and change cost distribution rather than reduce software creation waste. | Equivalent offline-first open CLI onboarding yields equal task correctness and fewer hosted/review costs. |

**Confidence:** low/exploratory until independent outcome tests and representative recruitment. Research design must not treat this editorial ten-company screen as a random sample of companies, repositories or model users.

## 7. Study implications (M1–M7)

| Objective | Operational observation and validity safeguard |
|---|---|
| M1 workflow evolution | Pinned dated exposure to working agent workflow; release != actual user adoption |
| M2 quality/review | Preregistered task correctness, human review minutes and failures under independent evaluation |
| M3 discovery | Prospective cohort and comparisons controlling baseline popularity, language and publicity |
| M4 meaningful third-party reuse | External real working downstream integration, not stars, impressions, downloads or trial signups |
| M5 reuse-first vs rebuild | License/provenance/security checked candidate pool, matched task and no-solution cases |
| M6 lifecycle sustainability | Complete human + inference + CI + upkeep + upstream costs, environmental meter/model boundaries and uncertainty; no carbon/token coefficient invented |
| M7 ethical maintainer growth | Fixed low-risk intervention for organic onboarding, downstream verified use, prospective controls |

None of these effects were measured in this source review. External ecosystem product announcements are **hypothesis generators only**.

## 8. Concrete experiment for the maintainer's own repository

**Repository:** [the existing GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study), using offline synthetic [parser fixture](../../../tests/fixtures/trending.html) and existing CLI. Avoid unauthorized GitHub Trending collection.

**Candidate intervention:** Use existing Trending parser fixtures in a timed newcomer onboarding A/B test of AGENTS.md plus a tested task recipe, not a new Replit-hosted copy of the parser.

**Control/treatment with frozen task:** A: current README & CLI instructions; B: revised task card/agent instructions pointing explicitly to existing reusable CLI; same frozen input, clean environment and reviewer.

**Independent acceptance and actual reuse signal:** Independent first-use pass of offline parse and summarize with exact schema; verify downstream script imports accepted JSONL; include all failures and support/rework minutes.

**Pre-register** all assigned tasks (including failures/no-solution), acceptance hash/schema and evaluator before any agent runs. Record exact repo commit, agent/model/versions, candidate license/security provenance, human review, token/billing if available, build/CI, attempts, 30-day support and downstream external adoption. Consent for any human participant logs and minimize personal telemetry.

**Stop rule:** Do not deploy hosted workflow if it requires code/data exposure, duplicate components, or adds maintainer costs without verified accepted tasks.

**Applicability:** a small offline CLI task, not evidence of representative OSS growth or positive environmental impact. The purpose is to *verify reuse of existing work*, not to maximize generated code, repo count or GitHub stars.

## 9. Review status, discrepancies and limits

- **Documentary output:** 6 attributed source records. Scope is source discovery, not independent validation of announced product quality or commercial uptake.
- **Special conflicting/qualified statement:** Replit's self-evaluation claims on model routing and subagent economics are not independently reproduced; hardware/cloud energy unknown.
- **Not established:** systematic full recall, company-wide corporate ownership auditing, third-party task acceptance, API reproducibility, real external users, long-run cost, maintenance load or kWh/CO2e.
- **Independence:** no external researcher fact-checked this file; no E3/E4 assignment, no original observations, no actual task trial.
- **Acceptance work outstanding:** rerun all seven monthly searches with screen logs; independent link/date/article-version check; verify artifact rights and product access/version; look for negative independent coverage, regulatory/security history and corrections; inspect exact legal parent after any merger; run tests/CSV validation in repo checkout; approve human review.
- **Merge gate:** **draft PR only**; do not close issue, merge to `main`, treat as final evidence or create false [#56 news](https://github.com/MSKazemi/github-trending-1000-study/issues/56) IDs until reviewers sign off.

**Actionable but UNTESTED lesson:** provide a single verified first-use task and reusable, permissioned interface to the component you already maintain; measure *outsider accepted reuse and total lifecycle burden* before adding an agent or duplicating a repository.

## 10. Provisional source lead preserved from overlapping first-pass PR #196 (not counted)

[PR #196](https://github.com/MSKazemi/github-trending-1000-study/pull/196) supplied a differently structured JSON event-lead inventory. Its overlapping Replit evaluation and free-mode links are already represented in this report; **do not count them again as independent events**. One distinct candidate remains:

- [Intelligent Model Routing on Replit](https://replit.com/blog/intelligent-model-routing) — preliminary lead `014-E03` in PR #196, with a **draft-attributed, not independently verified** publication date of 2026-08-26. The earlier draft reports a vendor-internal relative cost claim, not an independently reproduced result. Independently inspect the original article and revisions, the baseline definition, model/task mix, feature availability and actual cost measurements **before** adding an event row to `014-replit.events.csv`.

This is a **source-discovery handoff, not an accepted source/event, empirical measurement, human-reviewed statement or extra count**. The original JSON draft and reasoning remain accessible in PR #196's preserved branch; any future inclusion needs URL/date verification, event deduplication and a reviewer-linked commit.
