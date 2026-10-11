# GitHub, coding agents and genuinely useful software: scenarios for 2027

**Forecast status:** scenarios, **not forecasts or observed 2027 outcomes**. Baseline literature reviewed 2026-10-11. Every scenario can be falsified.

## Starting point
GitHub's 2025 reporting describes sharply increasing activity (R01). Empirical evidence shows high adoption of coding agents (R08–R10), but outcomes vary with tasks and measurement designs (R03/R04/R11). DORA argues AI can amplify strengths and weaknesses (R05/R06). These do not identify a universal trajectory for 2027.

## Three plausible scenarios
| Scenario | If this happens | Leading indicators to track | Practical robust response |
|---|---|---|---|
| **S1: Abundance of generated repos, scarce maintainer attention** | Creating code is cheap; trustworthy maintenance, onboarding and review become bottlenecks | median unreviewed age, failed installs, reopened defects, bot/agentic PR share, external successful usage | small reproducible tasks, verified tests, responsible maintenance, evidence before outreach |
| **S2: Agents improve net delivery on many task classes** | Tool capability + context + verifiers reduce end-to-end accepted-task effort | accepted tasks/human-hour, reviewer-minutes/task, 30/90-day defect burden, tool-specific task effects | invest in clear contracts, reliable harnesses and automated tests, update experimental baselines quarterly |
| **S3: Visible output accelerates but trust/maintenance lags** | code/PR counts rise faster than user value, vulnerabilities and project abandonment may rise | gap between PR volume and independent task success, sustained adoption, security reviews and post-release rework | reduce scope, human approvals for risky changes, validation gates, archive unproven ideas |

All three may occur simultaneously in different languages, project types or organizations. Do not collapse to a single certainty narrative.

## What to monitor each quarter in 2027
1. Share of independently **verified** user-task successes in audited repo-type strata.
2. Repeated external adoption and satisfaction where consent allows, rather than GitHub stars alone.
3. Time to accepted and safe deliverable, split into human work, agent waiting and rework.
4. Reviewer attention burden and unresolved high-severity security issues.
5. Agent usage attribution coverage (declared vs unobserved), with false negative sensitivity analysis.
6. Longitudinal survival of repo usability, release and maintainer capacity.
7. Whether Trending ranking proxies and cohort language/age distributions have drifted.
8. The cheapest credible reusable alternative for each evaluated project idea.

## Decision-ready output format
For each quarter, publish:
- evidence and N per cohort; deviations and attrition;
- supported new lessons, contradictions and 'unknown' results;
- a repo-type-specific **do / trial / defer / avoid** matrix with costs;
- a short changelog of platform/API, model and study-design revisions;
- assumptions that would change recommended action next quarter.

## Falsifiability examples
- If verified newcomer task success is no better for a documentation intervention, downgrade that recommendation.
- If AI-assisted accepted-task throughput improves **after** factoring review/security/maintenance, upgrade guidance for that task class.
- If small niche tools show repeated independent integration, do not penalize them for weak Trending attention.
- If 2027 data contradicts any scenario, record the contradiction and revise the scenario rather than rationalizing.

For actual practice see [developer decision playbook](DEVELOPER_DECISION_PLAYBOOK.md); for science see [AI substudy](AI_CODING_STUDY_2027.md) and [lesson derivation](EVIDENCE_TO_LESSON_PROTOCOL.md).
