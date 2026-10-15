# From job descriptions to testable engineering futures — draft (#224)

**Status:** exploratory research design, **not** a causal result or validated prediction. Jobs signal *advertised skill demands*, while releases signal *provider claims* and independently tested task outcomes signal observed usefulness. No longitudinal hiring/product outcome matching has yet been completed.

## Triangulation matrix
| Candidate signal | Hiring source examples | Independent test required | Competing explanation / failure signal |
|---|---|---|---|
| Reliable agent execution and isolation | [OpenAI Codex Systems](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/); [Anthropic Product Sandboxing](https://job-boards.greenhouse.io/anthropic/jobs/5394943008) | Dated release with sandbox behavior, external permission-boundary test | Hiring to fix faults, canceled initiative, no externally accessible interface |
| Better agent evaluations and code review | [Anthropic Claude Code performance](https://job-boards.greenhouse.io/anthropic/jobs/5098025008); [Cursor quality](https://cursor.com/careers/software-engineer-agent-evaluation-and-quality) | Pre-registered cross-repo task tests, failed-task denominator | Internal-only benchmarks, narrow tasks, outcome regressions |
| Durable memory / coordination | [OpenAI Core Agents](https://openai.com/careers/software-engineer-codex-core-agents-san-francisco/); [AWS AgentCore](https://amazon.jobs/en/jobs/10544938/sr-software-development-engineer-agentcore-aws-agentic-ai) | Inspect dated public API docs, test resumability/context corruption and cost | Research role does not ship; increased runtime maintenance |
| Operational agents | [AWS Agentic DevOps](https://www.amazon.jobs/en/jobs/10552775/software-development-engineer-agentic-ai-devops) | Review shipped incident workflows with explicit human approvals, false-remediation tests | Automation scope remains assisted and is not safe for autonomous remediation |
| Reusable software discovery | **No explicit direct positive hire in this selected seed** | Independently sample code-search/reuse roles, compare against agent-generated duplicate work | Agent growth instead increases duplicated packages and maintenance |

## Linked established evidence tracks
- Existing vendor news/company issues [OpenAI #67](https://github.com/MSKazemi/github-trending-1000-study/issues/67) and [Anthropic #68](https://github.com/MSKazemi/github-trending-1000-study/issues/68) contain claims that must be dated and source checked; **not independent performance verification**. The [100-company protocol](COMPANY_INTELLIGENCE_METHOD_2026_10.md) has a separate news-time window.
- Evaluate planned experiments under [reuse-first trials](REUSE_FIRST_EXPERIMENT.md), [task-cost accounting](TASK_COST_LEDGER_2026-10-12.md), [green metrics](REUSE_SUSTAINABILITY_METRICS.md), [supply-chain constraints](SUPPLY_CHAIN_PROVENANCE_2027.md), and [evidence-to-lesson thresholds](EVIDENCE_TO_LESSON_PROTOCOL.md).
- A company launch page, associated job posting and its own benchmark are **correlated first-party statements**, not three independent confirmations.

## Four falsifiable repository experiments
1. **Reuse-first search:** fixed accepted task and independently prepared tests; matched agent/human assignment to explicit existing-code search versus ordinary coding; endpoints functional success, distinct verified dependencies reused, licenses, vulnerabilities, human review, tokens, reproducible energy boundary where possible.
2. **Safe agent runtime:** compare least-privilege isolated tasks and unrestricted baseline only in a safe synthetic/test environment; record unauthorized actions, regressions, accepted completions and maintenance time.
3. **Eval-first pull requests:** independently specified regression/safety gates versus business-as-usual for eligible consented projects; include PR rejection, failed/unfinished tasks and 30/90-day repair overhead.
4. **Task-context portability:** compare versioned machine-readable instructions with ordinary context across unseen, held-out repositories; measure verified cross-project task completion and dependency reuse rather than generated lines.

**Primary challenge:** do improvements persist under independent testing after total search, review, maintenance and inference costs, *including failed tasks*, are included? Lower token counts are not automatically lower kWh or CO2e.

## Forecast accounting and validation
For each candidate theme create a future evidence pair `(hire_snapshot_utc,release_event_utc)` with explicit original company identity and unit. Test whether temporally *prior* recruitment signals predict specified public capabilities better than a preregistered release-only baseline and a shuffled-company negative control, accounting for censoring and source coverage. Do not backdate first-seen employment ads or use present roles to predict earlier launches. A proposed 2027–2031 transition to agent-governed development remains a **conditional scenario** until prospectively tested.

## Repo maintainer application (hypotheses, not measured benefits)
Make code discoverable by search/repository metadata, keep component interfaces and license clear, provide agent-safe sandbox and approval rules, independently executable quickstarts/tests and a repair-cost ledger. If the new scaffolding harms first-task success or raises total cost, roll it back. Prefer contributing verified fixes upstream rather than copying functionality into new repositories.

**Pending:** primary-source release/event ledger, contradictory product evidence audit, independent held-out task trial, and human methodological review.

## 2026-10-15: dated observed job–release source-pair review

The [bounded primary-source and counterevidence screen](reviews/2026-10-15-hiring-release-triangulation-source-pairs.md) adds six candidate themes, dated April–September official events, inaccessible/missing pair controls and falsifiable task experiments. **Jobs first observed in October cannot be retrospective predictors of earlier releases.** No independent user test, authenticated first posting date, actual hire, personnel census, causal forecast or carbon result has been produced. The earlier “pending release/event ledger” note above refers to the historical 2026-10-13 draft; the new pair screen remains exploratory until authentic prospective enrollment and rights/methods approval.
