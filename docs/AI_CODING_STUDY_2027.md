# AI-assisted and vibe-coding sub-study (planned for 2027)

**Status:** prospective, independently consented sub-study; NOT measured by the Trending data alone. Its purpose is to evaluate net useful software delivery, not models' token throughput.

## Distinguish development modes
- **Manual/reference:** developer writes and reviews the code without generative AI for a specified task.
- **AI-assisted, verified:** AI tools may draft/modify code, but developer understands critical decisions and validates requirements, tests, security and behavior.
- **Vibe coding (operational definition):** developer drives implementation through natural-language iteration and evaluates primarily via execution/observation, with little systematic inspection of generated implementation. The latter label is a **workflow**, not an insult or a conclusion about quality.
- **Autonomous coding-agent workflow:** delegated repository tasks/PRs with configurable human review gates; this may overlap either AI-assisted or vibe coding.
**Never infer these modes from AGENTS.md, README mentions, a commit signature or claimed 'AI generated' code detection alone.** Public artifacts can support sensitivity analyses, not gold-standard individual author attribution. Prefer opt-in diaries with explicit data rights.

## Research hypotheses (unconfirmed)
- A1: AI helps more on **greenfield/bounded scaffolding** than on complex existing-code maintenance once review/rework are counted. May be false; design must permit disconfirmation.
- A2: task-specific context, explicit acceptance tests and review gates improve accepted outcomes per unit total engineering effort.
- A3: larger agent-generated patches impose disproportionate maintainer review cost compared to equivalently useful, bounded patches.
- A4: a 2027 project's independent user-task success and 90-day viability are poorly predicted by star count or total commit volume alone.
- A5: AI assistance may raise activity but have heterogeneous effects on security regressions, task quality and net engineering time.

## Design: two complementary methods
**Study A — observational:** enrich the 1,000 Trending + 1,000 controls with only observable AI-era markers (agent-instruction files, attributable PR labels where documented, explicit usage disclosures, AGENTS files over time). Assess sensitivity to under-detection and false classification; compare different repository types, creation years and before/after cohort. Do not claim causal impact of AI use from these observational markers.

**Study B — opt-in prospective evaluation:** recruit volunteer developers/projects using structured consent and minimal data collection. Pilot ~20 bounded tasks, conduct a power simulation and then preregister a realistically sized experiment (do NOT promise 60/100 tasks absent recruitment). Divide tasks by new/established code, bugfix/feature/docs/refactor/security, estimated complexity, developer familiarity, and project risk. Define a task's acceptance suite and definition of done **before** workflow assignment. Randomize permitted assistance where ethical and willing, block by developer/project/task type, analyze participant clustering. Consider crossover with counterbalancing and washout; identify carryover effects. If no-AI assignment would cause selective refusal, use **randomized encouragement** or a transparent observational design with limited causal claims instead.

**October 2026 pilot-planning addition:** [Synthetic cluster-factorial binary-acceptance sensitivity](CLUSTER_TRIAL_POWER_SENSITIVITY_2026_10.md) uses the existing four-arm allocation definitions but models **only secondary accepted-task probability**, not the study's proposed primary per-human-hour throughput. It is *not* a pilot-calibrated sample-size calculation; real pilot measurements and independent statistical approval are needed before confirmatory enrollment.

## Outcome hierarchy
**Primary proposed outcome:** independently accepted, correct task completions per *total developer-hour*, with severity-weighted nonconformances and explicit rework (not tasks completed by AI alone). Predefine whether 'incomplete' receives zero accepted task outcomes and preserve time-to-abandonment.

**Secondary:** time to independently accepted result; defect rate and severity; security-specific negative tests; independent review minutes and rounds; reopened bugs at 30/90d; feature revert rate; onboarding usability; tokens per *accepted* task; cost per accepted task; maintainers' attention displaced; developer experience reported separately as subjective.

Record human minutes (planning, prompt writing, context gathering, review, testing, debugging, redeployment, follow-up), AI wait/wall-clock minutes, concurrent sessions and overlap, input/output/cached tokens and model/version if usage permissions allow. Do not add overlapping concurrent intervals. Dollar cost, if reported, uses **prices paid for that period and plan**; $0 cash does not imply $0 time/opportunity cost.

## Experimental analysis
- Intention-to-treat by assigned workflow; also report compliant/per-protocol results, not as replacement.
- Mixed-effects models for bounded tasks, cluster by developer/project, task difficulty; survival analysis for time-to-acceptance with unfinished tasks censored **only as justified**. Abandonment is usually a separate failure outcome, not innocuous censoring.
- Predeclare noninferiority or superiority margin in *accepted correct outputs per human hour* and risk thresholds before pilot outcomes; report distribution, CIs and missingness.
- Adjudicators inspect final solution blinded to assistance condition where feasible; measure reviewer agreement.
- For 30/90-day maintenance, enforce same exposure period and record differing follow-up availability.
- Report heterogeneity (mature vs greenfield, experience, task risk, language) as exploratory unless powered for interaction.
- Include sensitivity to developer choice/participation, learning curves, multi-agent concurrency and quality vs speed tradeoffs.

## Key prior evidence and why transfer is limited
- METR 2025 RCT: experienced OSS developers using early-2025 AI on their own mature projects were slower on average **in that study** (19% longer completion); does NOT say all AI is slower.
- METR Feb 2026 update: later point estimates suggested some speedup, but the authors said task and participant self-selection made the updated estimates unreliable. Do NOT market an exact 2026 speedup.
- DORA 2025 report: AI can amplify strong and weak organizational practices and may increase throughput and instability simultaneously; largely survey/organization-level, not a task-level causal effect.
- Agentic Much? 2026: commits/PR markers support large-scale **adoption** measurement but underdetect uncredited agent use; adoption != effectiveness.
- AIDev and agentic PR work: large-scale outcomes and review traces, but PR acceptance is not equivalent to downstream usefulness or exploit-free correctness.

Sources and evidence notes: [references](REFERENCES_AI_2027.md).

## Ethical boundaries
No private prompt transcripts, tokens, work content, pricing, or developer identities are public by default. Use opt-in collection and aggregate publication, honor withdrawal where feasible, preserve consent metadata separately and never claim detection of undisclosed AI-assisted authors. Tasks on production systems must use safe test environments and human approval.

## Publication outputs
A frozen protocol, synthetic schema examples, opt-in task logs, acceptance rubric, anonymized aggregate results, subgroup uncertainty, and a research artifact replicable within documented privacy/platform constraints.
