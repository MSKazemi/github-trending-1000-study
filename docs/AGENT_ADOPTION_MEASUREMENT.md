# Identifying coding-agent adoption without guessing (draft v0.2)

## Fundamental measurement problem
A release date proves only tool availability. GitHub code style, README marketing, topics, AGENTS.md and a generic 'generated with AI' phrase **cannot prove** which agent wrote code or what proportion was authored by a human. Robbes et al. (ACM TOSEM 2026) and Khosravani & Mockus (2026 preprint) warn that single-channel detection misses substantial adoption. **No detected trace ≠ confirmed manual coding.**

## Classification of repo-event provenance (rather than a binary vibe label)

| Class | Definition / minimum evidence | Use in study | Key caveat |
|---|---|---|---|
| D — directly confirmed | Consented first-party usage log recording agent, task and UTC with matched repo/PR; OR authorized official platform per-repo metrics covering actual agent activity | Prospective opt-in causal/observational substudy | Self-selection; provider semantics/privacy |
| H — high-confidence public trace | Recognized dedicated verified agent bot/PR actor (identity and deployment checked against current official list), or artifact with manually validated official provenance | High-precision **observed use** study | Silent CLI use goes undetected; impersonation possible |
| M — plausible attributable public evidence | Explicit tool-specific coauthor trailers, reproducible structured metadata, or verified PR description disclosing agent with matching date | Sensitivity analysis; manually audit before stronger claims | Co-authorship indicates assistance, not percentage AI-generated |
| L — readiness/context hint | AGENTS.md, CLAUDE.md, .github/copilot-instructions.md, model tool config, 'AI' topic or vague mention | Tooling-adoption/compatibility descriptive **only** | Not evidence of actual use |
| U — unobserved/unknown | No credible positive trace in permitted observation frame | Denominator category 'no observed trace' | **Not** verified human-only |

Only D/H can support a *high-confidence public-observable treatment indicator*; optionally M in separate sensitivity analysis. Keep full history of transitions, source URI/commit SHA, UTC detection, agent identity provenance and human adjudication.

## Detection algorithm and requirements
1. Obtain exact *allowed* public events and consented data: PR actors/labels, commit trailers, PR body disclosures, GitHub Actions/workflow metadata, bot identities, dated config presence; preserve only minimally needed provenance in public export.
2. Version signed patterns + allowlists, inspect bot impersonation and changes in GitHub agent identity; **no unvalidated regex alone** should assign high confidence. Include negative cases such as generic 'agent', marketing phrases and boilerplate.
3. Reconcile immutable repository ID and timestamp. An artifact dated before the agent's verified release is a **false positive / requires investigation**, not early adoption.
4. Store agent product (Claude Code/Codex/Copilot coding agent/Cursor/other/unknown), evidence class, event type, source ID, date, detector version, uncertainty and manual reviewer record.
5. Draw stratified gold set across high/medium/low/no-trace and project types/windows (pilot **>=200 reviewed artifacts** as a feasibility target, chosen independently of predicted certainty); two reviewers and adjudication. Report positive predictive value (precision), sensitivity *only with a gold set including actual use*, and Wilson CIs. Public trace-only gold labels cannot estimate recall for **silent** tool use.
6. Analyze observed adoption both as **first observable agent event** (D/H) and as a lagged dose (events attributed / all eligible qualifying events, with eligibility and missingness). Preserve zeros only for counts observed within complete windows.
7. Run sensitivity by agent product, evidence class, date/platform semantics, owner type, repository type and human-verified vs machine-only traces.
8. For non-user-accessible third-party data, do NOT request privileged enterprise metrics. A GitHub Copilot repository-level metric exists for authorized organizations [GitHub Jul 17 2026](https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available/), but is not a public census.

## Identification and evaluation
- **Main estimates** should be descriptive within probabilistically sampled observed-Trending and comparison frames; agent status is a *stratum/predictor*, not a filter on success.
- **Event-study/DiD** (exploratory until preregistered): compare a project before/after first D/H trace to **not-yet-detected** comparable projects, matching pre-period growth, project maturity and calendar time. Use staggered-adoption estimators with pre-trend tests and placebo dates. The adoption date may lag true use; comparison is not verified AI-free; **causal identification remains weak**.
- No binary causal 'vibe coding is better/worse' from public repos. True productivity requires opt-in logs, independently accepted tasks, developer hours/tokens and 30/90-day rework.
- Separately model *agent compatibility*, *agent-attributed contribution volume*, *verified individual adoption*, and *usefulness*. These are different constructs.

## False discovery and legal/ethical guardrails
- Never publicly accuse a named maintainer of undisclosed AI usage or low quality based on a model inference.
- Distinguish PR coauthorship from all code authored; a PR can include human changes. Repositories may contain more than one agent and human workflow.
- Do not redistribute consented usage logs or private prompts. Publish aggregates where feasible and comply with tool/platform policies.
- Report recall bounds and unknowns; if opt-in direct logs show many false negatives, update protocol **before** interpreting findings.
