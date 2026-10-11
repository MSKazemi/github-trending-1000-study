# Metric register and 2027 evaluations — draft v0.2

Each metric has an **object, unit, denominator, source, observation window and bias correction**. “Missing” and “not applicable” are not zero. Proposed primary outcomes must be frozen before enrollment and a pilot-based power analysis.

## Four research targets — deliberately separate
1. **Github discovery/selection:** probability of observation on scheduled Trending pages, displayed rank and recurrence.
2. **Agent adoption:** independently evidenced coding-agent use or attributed contributions, recognizing silent use and tool changes.
3. **Engineering health:** functionality, response/review burden, reliability, defects and maintainability.
4. **Useful impact vs effort:** actual independent user outcomes, adoption, maintenance and **total cost per accepted task** (requires an opt-in sub-study).

## Candidate measurement matrix
| Key | Exact measure / time | Data and denominator | Main pitfall | Validation / handling | Use |
|---|---|---|---|---|---|
| SEL01 | Eligible dated Trending appearances | raw captured row by page/window | pages overlap; missing captures | preserve page SHA/time, failed fetches, page length | Sampling frame |
| SEL02 | Unique listed repos | immutable GitHub ID first seen during 2026-11..2027-04 | renames/duplicates | ID reconciliation, unresolved queue | Sample target |
| SEL03 | Displayed ranking percentile | (rank-1)/(page_length-1), only if list_len>1 | rank not a quality signal; pages differ | within identical filters/windows only | Descriptive |
| SEL04 | Baseline age days | t0-created_at; exact UTC | old repos inherently more popular | covariate + bins | Matching covariate |
| SEL05 | Baseline stars | official point-in-time stargazers_count | age, bots, bookmarks | covariate; log1p; audit | Matching covariate |
| SEL06 | Repo type / language / owner | fixed classifier + human audit | Github language not true functionality | inter-rater coding + unknown | Strata/covariate |
| AI01 | High-confidence observed adoption | >=1 D/H agent provenance action by t; repo-by-month | silent agent use; bot spoofing; lag | manual gold set, provider traces | Exposure |
| AI02 | Attributed agent share of events | attributed qualifying events / all qualified publicly visible events in complete month | != share of generated code; denominator mixing | provide counts and unknown channel | Exploratory |
| AI03 | First detected agent use | earliest D/H attributable event UTC | not earliest actual adoption; may lag | sensitivity with M and opt-in D | Event time |
| AI04 | Agent readiness marker | configuration docs and date | AGENTS.md != agent use | report separately from AI01 | Descriptive |
| VIS01 | 30/90/180-day **net** stars | S(t+n)-S(t), can be negative | attention != user value | true prospective counts, same UTC lag | Popularity secondary |
| VIS02 | Growth log-difference | log1p(S(t+30))-log1p(S(t)) | denominator/baseline skew | also report absolute, CI | Popularity secondary |
| COM01 | Human first response distribution | time from new PR/issue to 1st substantive non-self human response | answered-only median is biased | survival curves + censored unresolved, bot audit | Community |
| COM02 | New external contributors | distinct eligible actors with first accepted PR in window / repo | user renames, squash, contribution definition | opt-in/pseudonymization and multiple definitions | Community |
| COM03 | Contributor continuity | returning qualifying contributor IDs by 90/180d / baseline contributors eligible | lurking/non-PR users invisible | attrition/exposure denominators | Sustainability |
| ENG01 | Verified clean install + task success | independent task successes / *all* attempted with fixed task | README length does not prove first-run utility | human testers blinded to hypothesis; N, CI | **User value primary in sub-study** |
| ENG02 | Functional accepted work | independently accepted tasks / started tasks, including abandoned | merged PR != delivered functionality | preregistered tests + independent adjudicator | **Primary in opt-in experiment** |
| ENG03 | Defect/rework burden | severity-weighted failures + repair minutes per accepted task at 30/90d | no issues != no defects | same follow-up availability, negative tests | Quality |
| ENG04 | Code review bottleneck | human review minutes & requests-for-change per *accepted* task | GitHub review timestamps miss offline effort | consented time log, PR traces; distinguish approval vs correctness | Cost |
| ENG05 | Security risk | validated high-severity findings unresolved / eligible audited issues | CI pass != no vulnerabilities | threat model, independent security triage | Safety gate |
| ENG06 | Documentation usability | task-completion first try, help requests, elapsed minutes | README length / screenshots confounded | fixed rubric and dual audit | Value |
| COST01 | Total human-active task minutes | sum nonoverlapping plan+prompt+review+repair+ship+followup | overlapping work / multi-agent waiting | time diary; concurrency accounting | **Cost primary in opt-in experiment** |
| COST02 | Tokens per accepted task | all observed input+output+cached-equivalent tokens across *all attempts* / accepted tasks | providers count cache differently, 0 successes undefined | missing as unknown, versioned provider | Cost |
| COST03 | Cash + opportunity cost | API/CI/cloud spend + human hours valued at declared rate + maintenance forecast | voluntary no salary != zero time cost | report separate components and range | Decision support |
| USE01 | Independently validated repeat use | users completing >=2 relevant workflows across 30/90d / *eligible enrolled users* | downloads/stars != users, survivorship | opt-in repeated task logs and churn | Long-term usefulness |
| USE02 | Verified integrations | independently confirmed downstream deployments/uses / eligible known integrations | fork/dependency download could be automation | artifact audit; selection caveat | Useful adoption |

### What NOT to use as a scientific primary selection criterion
- “More than N stars,” trending position, commits, PR volume, followers, README length, days since last PR, AGENTS.md presence, product hype.
- Percent of code created by AI guessed from a classifier, downloads mistakenly labeled users, positive interview anecdotes without recruitment denominator.
- Historical star counts derived by subtracting WatchEvents from current stars without archival completeness validation.

## Prespecified main estimands (subject to pilot)
**Observational cohort:** signed log 30-day star growth vs baseline documentation and evidenced agent activity, adjusting for baseline age/stars, type, language, owner, pre-baseline activity and calendar week. This is **association within a selected frame**, not the causal benefit of Trending or agent use.

**2027 user-value substudy:** (a) independent task success and (b) independently accepted task outcomes per *all human-active hours* by workflow, with defect/severity guardrails; analyze randomized assignment when feasible and stratify by task type/developer experience/project maturity. Do not post-hoc reweight winners. User value is **not observable from generic GitHub metadata** alone.

## Statistical estimators and model testing
- **Descriptive:** cohort flow, capture completeness, exact denominators, distributions (median/IQR, skew), Wilson CIs for relevant rates, stratification by type/language.
- **Growth:** signed robust regression on log changes (net can be negative); zero-inflated/negative binomial only for genuinely nonnegative count outcomes with adequate diagnostics; robust intervals clustered by repo.
- **Agent adoption:** event-study and modern staggered DiD with not-yet-adopters; baseline/pre-trends, exposure-date lag, calendar shocks, placebo dates and sensitivity for undetected use. Never present observational associations as randomization.
- **Issue/PR response:** survival analysis with right censoring; if abandoned/closed without answer, record competing risks separately.
- **Ranking black box:** within-page Kendall tau-b, Jaccard and rank-biased overlap for same filters; chronological held-out rank prediction and PR-AUC for selection only with defined candidate frame. No proprietary-algorithm claim.
- **Independent usefulness:** fixed tasks, independent human adjudication, mixed models or paired experiments, attrition checks, effect sizes and 95% CIs; group by project and tester to avoid pseudo-replication.
- **Exploratory hypothesis multiplicity:** report BH-FDR with exact preregistered family. Distinguish corrected significance from practical importance.

## Misleading comparisons checklist
1. **Conditioning on Trending** introduces collider bias; compare to independent controls and explicitly limit generalization.
2. **Comparing old vs new directly** confounds project maturity and ecosystem conditions; compare repo histories around measured agent-use events with contemporaneous controls.
3. **Calling no trace 'human-only'** yields contaminated controls; obtain direct opt-in confirmation or sensitivity bounds.
4. **Reconstructing before-period metrics from today's API** creates survivorship and time-travel bias; use dated sources or unknown.
5. **More merged PRs / generated lines** can represent greater review load rather than more delivered software; use accepted task/user outcomes.
6. **Shorter review** can be rubber-stamping; measure defect/security and independent correctness, not speed alone.
7. **Percentages without denominator** (Stack Overflow survey n=12,255 vs total n=30,903; product WAU; agent-attributed PRs) are not comparable.
8. **Token optimization without quality** incentivizes false economy; report accepted value with human effort, risk and maintenance.

## Periods and reporting cadence
- 2026-10 pilot (capture reliability, provenance, gold labels, precision/power).
- 2026-11 to 2027-04 inclusive: main observation window (capture at declared UTC time, every permitted surface/day).
- Baseline, +7, +30, +90, +180 days per repository (optional +14, +60 explicitly exploratory); last nominal follow-up 2027-10.
- Interim 2027 Q1/Q2 reports clearly labeled *pilot/interim*; full 180-day comparative findings no sooner than late 2027. For 2027 actionable lessons, grade evidence and constrain scope.

## References
[Reading list](READING_LIST_2027.md), [selection](SELECTION_PROTOCOL_2027.md), [agent adoption](AGENT_ADOPTION_MEASUREMENT.md), [source register](../references/study_sources_2026.json), [evidence-to-lesson protocol](EVIDENCE_TO_LESSON_PROTOCOL.md).
