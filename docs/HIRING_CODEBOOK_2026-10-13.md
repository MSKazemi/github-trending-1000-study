# Hiring signals annotation codebook — proposal v0.1 (#223)

**Status:** proposed, **not frozen**; no real double coding or inter-rater reliability measurement completed. The row-level evidence lives in [the pilot audit](../references/ai_hiring_job_leads_source_audit_2026-10-13.csv).

## Units, eligibility, blinding
Code a verified individual job-description *body*, not a title or search snippet alone. A text indexed externally may be marked `indexed_content_only` and must not be treated as a live source. Before coding, strip company identifiers where feasible but keep exact source record separately. If the job body identifies a different corporate employer from the page URL, place the role on **identity hold**. Preserve all missing and excluded rows in the denominator.

## Multi-label taxonomy
| Label | Include if responsibilities explicitly mention | Exclude unless explicit |
|---|---|---|
| `agent_runtime` | Agent execution, tool loops, scheduling or orchestration | Generic chatbots |
| `sandbox_security` | Isolated code execution, privileged access boundaries, containment | Generic security slogans |
| `evaluation_quality` | Measured agent evals, regression/failure analysis, benchmark construction | Product quality without tests |
| `rl_training` | Reinforcement learning, training environments, post-training pipelines | General model development |
| `context_memory` | Agent persistence, context construction, durable memory | LLM context window marketing |
| `developer_reuse` | Code search, dependency discovery, verified existing-component reuse | Merely generating new code |
| `enterprise_integrations` | Identity, governance, tool connectors, deployment enterprise workflows | Enterprise audience only |
| `inference_efficiency` | Serving, model routing, latency, runtime cost or efficiency | Unquantified fast claims |
| `agent_operations` | Deployment, observability, incident handling, recovery | Generic backend software |
| `other` | Clear relevant function outside taxonomy | Silent guessed category |

Tags describe **advertised responsibilities**, not delivered products or employer priority ranking.

## Coding procedure
1. Freeze a registered random or stratified set of eligible descriptions *before* interpreting likely products. Keep the original selection and exclusions.
2. Two **distinct human reviewers** independently inspect the same source and mark each theme as `present`, `absent`, `uncertain`, `not_reviewable`, with a short source-backed rationale. No generated synthetic reviewer votes presented as humans.
3. Compute exact agreement per binary label and Cohen's kappa where data supports it; include prevalence, uncertainty and missingness. If rare positive labels cause degenerate kappa, disclose prevalence and percent agreement; do not force a numeric kappa. For multiple labels, report per-label metrics rather than a misleading single accuracy. Aggregate agreement only with its defined denominator.
4. Report disagreement, independently adjudicate and keep pre-adjudication labels immutable. Resolve identification disputes before aggregating company comparisons.
5. Report observations and exceptions (company sample, selection, missingness) independently from forecast hypotheses. Avoid confident predictions from small or hand-picked samples.

## Validation examples (illustrative, NOT study observations)
- Example A: Role describes isolated execution of untrusted code and permission scopes. Label `sandbox_security=present`, `agent_runtime=present` only if execution loop is explicitly described.
- Example B: Role describes tracking API token cost only. Label `inference_efficiency=present` if serving/runtime engineering is explicitly required; otherwise `uncertain`.
- Example C: Careers index says “RL Environments” without responsibilities. Mark `not_reviewable` rather than assuming RL experiments.

**Review gate:** independent reviewer identities/consent and evidence access, frozen codebook, per-label agreement calculations and adjudication log are **not done**.
