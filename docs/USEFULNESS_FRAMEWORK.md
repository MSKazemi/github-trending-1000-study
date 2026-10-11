# What makes an open-source project useful? A measurable framework

**Status: construct proposal; no empirical validation yet.** This framework separates actual user benefit from GitHub visibility or activity. It is inspired by multidimensional developer-productivity measurement (SPACE) and the community-health emphasis of CHAOSS; its rubrics and thresholds are **our proposed heuristics**, not externally validated scales.

## Four separate constructs (do not collapse them into one quality score)
1. **Demand & relevance:** a real target user/job-to-be-done, observed frequency/pain of the task, current alternatives, willingness to switch; anecdotal maintainer enthusiasm is not independent evidence.
2. **Task-level effectiveness:** verified success on predefined representative tasks and users; accessibility, reproducibility, error rate and safety; evaluate against **existing alternative** and a **do-nothing** baseline.
3. **Adoption & repeat value:** external non-maintainer adoption, task completion over time, retention at 30/90 days where consent/measurement allows, documented independent integration, reduction in time/errors/costs. Stars and forks are attention signals only.
4. **Lifecycle economics & sustainability:** **total** developer effort, token/tool consumption, infrastructure cost, verification/rework burden, onboarding friction, maintenance hours, defect/rework rate, maintainer concentration and dependencies.

Use dashboard **profiles**, not one arbitrary rank. A validated small utility with few stars may be extremely valuable in a specialized niche.

## Construct-to-metric operationalization
| Construct | Metric (exact numerator/denominator) | Collection method | Common false inference | Validation method |
|---|---|---|---|---|
| Problem evidence | independent users identifying same recurring pain / people approached | consented short interviews or support tickets | friends agreeing = demand | distinct organizations, non-leading questions |
| First-run success | independent users completing specified task unaided / users attempting | timed install+task test | README exists = usable | standardized clean-environment test |
| Task quality | passing required tests, functional acceptance, security controls | fixed acceptance suite + code review | tests passed = safe/useful | negative/edge tests and third-party audit |
| Time saved | median elapsed task time baseline − tool time | repeated paired tasks with counterbalancing | self-reported speed = observed speed | independent clocks, task stratification |
| Net user benefit | difference in completed outcomes or cost between tool and best alternative | preregistered external-user task study | total users = impact | baseline, CIs, attrition |
| Repeat adoption | users who complete >=2 meaningful workflows in follow-up / active eligible users at baseline | opt-in product telemetry or structured check-ins | downloads = retention | data rights, independent confirmation |
| OSS reuse | independent downstream integrations **verified** / eligible known adopters | package/dependency/issue evidence | forks = deployed use | inspect cited dependency/import |
| Time cost | specification + prompts + waiting + review + repairs + deployment + follow-up effort | structured maintainer work log | AI typing speed = productivity | record whole cycle |
| Token cost | input + output + cached tokens per accepted task | provider/agent usage logs where accessible | provider tokens reflect all costs | mark unobservable components unknown |
| Maintenance debt | regression/reopen severity, repair hours, dependency upkeep | issue + incident + time log | no issues = no defects | active user context and observation window |
| Community health | first substantive human response and newcomer contribution path | CHAOSS-aligned event logs | bot reply = supportive maintainer | bot filtering, censored response times |
| Stability | reproducible install/build and successful task at 30/90d | pinned clean environment | one demo = sustainable | repeated versioned checks |
| Security/privacy | critical unresolved findings, exposed secrets, misuse impact | SAST, dependency audit, independent review | green CI badge = secure | threat-model-specific assessment |
| Reach | GitHub stars, Trending, mentions | GitHub + independent channels | reach = users or durable value | explicitly secondary |

**Missing, not applicable and zero are distinct.** Only include measures that apply to the type of project (library, CLI, dataset, curated list, developer framework, research prototype, deployed service).

## Operational definitions for independent evidence
- **Independent user:** person not a maintainer or the developer's recruited agent; declare relationship and incentives. Respect consent and privacy; never expose identities.
- **Verified use:** independently repeats a declared task or documents integration with an auditable, permission-respecting source. Do not rely solely on flattering comments.
- **Sustained value:** recurring use plus nontrivial completed outcomes during a prespecified 30/90-day period. If not observable, mark `unknown`.
- **External evidence:** published integration, user-task protocol, consented interviews, dependency evidence with provenance. Positive anecdotes are lower confidence.

## No single 'usefulness score'
A 95-star specialized research tool with 3 repeat institutional adopters can be more useful than a 50,000-star tutorial repository in a different context. Comparisons must be **within objective, project type and intended audience**.

Optional decision gates (provisional, not validated): (A) clearly defined problem + target; (B) comparative task works; (C) safe enough for intended context; (D) total value exceeds cost of maintenance; (E) independent use or a research-specific replication artifact exists. The exact quantitative threshold and required evidence depend on risk and project type. Do not treat no reported independent users as proof of zero value.

## Critical validity threats
- **Goodhart's law:** optimizing stars, commit count or benchmark passes can produce the metric without real benefit.
- **Survivorship/selection:** trending excludes invisible but useful niche tools and may overrepresent novelty or publicity.
- **Measurement access:** GitHub APIs rarely show unique actual end users; opt-in telemetry and external evidence have selection biases.
- **Post-treatment leakage:** projects may improve READMEs after Trending attention.
- **Automation:** bot commits, AI PRs, downloads, installs and CI may increase activity without solving user problems.
- **Project archetype:** datasets, libraries, infrastructure and personal art projects need different impact measures.
- **Risk-weighting:** production software requiring authentication, financial or clinical correctness needs stronger independent review than a personal prototype.

## Reporting template
Report each construct with raw numerator, denominator, timeframe, comparison/baseline, missing rate, an estimate + uncertainty (where feasible), evidence source, applicability and confidence; never convert an absent measurement to a ranking loss.
