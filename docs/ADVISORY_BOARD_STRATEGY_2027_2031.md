# Five-year advisory-board strategy for trustworthy, reusable and green software

**Prepared:** 2026-10-11. **Horizon:** 2027–2031. **Status:** proposed multi-disciplinary strategy, NOT advice actually issued or endorsed by named professors, corporations, CEOs or CTOs. No user/energy research outcomes are claimed.

## One-sentence vision
Enable developers and coding agents to **discover and independently validate the best suitable existing software first**, then reuse, extend, contribute upstream, or implement something new only when justified by functionality, legal/security requirements, human effort, lifecycle energy and long-term stewardship.

**Ultimate societal objective:** minimize **unnecessary repeated development** while maximizing verified public/private benefit. We must not confuse 'fewer lines, prompts or tokens' with environmental savings, and we must not punish legitimate innovative, educational, research, compatibility or accessibility projects that require new code.

## Hypothetical advisory-board viewpoints — NOT external endorsements

| Chair/perspective | Would demand before recommending scale | Will veto misleading behavior |
|---|---|---|
| Full professor — empirical software engineering | frozen questions, sampling frames, provenance, functional gold set, code/data release where lawful, reproducibility and null results | correlations described as causal, Trending stars described as software quality |
| Full professor — causal inference/statistics | prospective independently sampled tasks, randomized workflow comparison, intention-to-treat, DAG, missingness/power, sensitivity, pre-registration | selectively studying tasks that already have reusable code, agent-label contamination |
| Full professor — information retrieval/software reuse | time-stamped task-to-component judgments, independent assessors, multiple retrieval channels, gold set coverage and pooled-relative recall caveat | claiming an unavailable result means no prior implementation exists |
| Full professor — climate informatics/LCA | ISO SCI/SCI-for-AI boundaries, independent accepted-task functional unit, energy measurement tiers, long-run runtime and rebound | converting token count to fixed gCO2e, claiming whole-life savings from partial instrumentation |
| CEO — product and platform strategy | externally validated recurring problems, existing substitutes, willingness to adopt, organizational incentive to maintain/upstream, impact versus operating cost | building a complex product to chase stars before a reproducible user outcome |
| CTO — software architecture/SRE/security | repeatable install/integration, API compatibility, versioned provenance/SBOM, OpenSSF/OSPS, least-privilege agent execution, upgrade/rollback path | installing agent-recommended packages blindly; one score/badge as a safety guarantee |
| OSS ecosystem/maintainer chair | attribution, licenses, upstream reciprocity, review/support burden and user education, inclusion of small/old projects | mass AI PR spam or shifting unmeasured costs to volunteer maintainers |
| Research ethics/privacy advisor | consent for human/AI usage logs, data minimization/retention, explicit source permission, conflict-of-interest policy | raw private prompts, identifying developers by speculative AI detectors, covert instrumentation |

## Proposed scientific objectives (prioritize, do NOT conflate)
- **O1 (primary science):** For externally specified tasks sampled independently of search results, how often can existing software be verified to solve them? How do reuse-first vs regular development differ on independently accepted task outcomes per total human-active hour, with safety and maintenance guardrails?
- **O2:** Does an independent, repo-type-aware search/verification pipeline find viable candidate components more reliably than Trending, top-star search, keyword search and default coding-agent retrieval, at a bounded *search plus verification cost*?
- **O3:** How does agent use alter adoption, retrieval, patch size, review burden, security and rework, with source-confidence tiers and controlled task studies?
- **O4:** Under what workload/environment/maintenance conditions does reuse result in net measured lifecycle energy/carbon reduction? When might fresh code be greener or safer?
- **O5:** What practices make an artifact *reusable by other humans and agents*, while compensating or supporting the people who maintain it?

The public Github Trending sample (target 1,000 unique) and other observational cohorts address **visibility/association**. Real value and causation require prospective tasks, human adjudication and opt-in experiments. Do not allow Trending to define the eligible universe.

## Strategic choices and explicit non-goals
| Choice | Rationale |
|---|---|
| **Research before product** | Build evidence, gold tasks, measure missingness and stabilize eligibility before investing in an agent search platform |
| **Reuse-first, not reuse-always** | A poor/malicious package increases maintenance, exposure, runtime cost and user harm |
| **Portable evaluation core** | Models/agents/platforms evolve: task specs, acceptance, protocol and provenance must remain valid across products |
| **Human and ecological cost together** | Less downstream coding may simply move work to upstream maintainers or runtime GPUs |
| **Include historical, quiet and niche software** | Valuable old/low-star components often do not surface on Trending |
| **Accept negative/neutral results** | Scientific findings that refute the reuse hypothesis can still prevent wasted effort |
| **Do not create a paid-rank marketplace during science phase** | Commercial incentives would bias discovery and conflict with objective reproducibility |
| **Avoid unsupported private/enterprise access** | Proprietary traffic, model telemetry and full code provenance are unavailable for arbitrary public repositories |

## Product and scientific outputs are different artifacts
**Scientific outputs:** frozen registered protocols; observation cohort datasets where permitted; task–candidate gold labels; effect estimates/uncertainty; selection-bias audit; reproducible evaluation code; publishable negative results.

**Optional engineering output (only when validated):** an interoperable *task-to-component evidence registry* with candidate IDs, task compatibility/acceptance examples, SPDX license data, package URLs, version hashes, security/provenance signals, scope/unknowns, upstream contact, time-cost and independent success evidence. Its interface must be inspectable, portable and non-lock-in. Never conflate a simple registry with an already validated recommender.

## 2026 evidence that informs (not determines) strategy
- [2026 Stack Overflow survey, named agent use](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent): among **12,255 named-tool question respondents**, 65.5% report Claude Code and 29.5% Codex usage; multiple answers allowed, not worldwide market share.
- [2026 Stack Overflow methodology](https://survey.stackoverflow.co/2026/methodology): 30,903 valid responses through a community recruitment frame; not a probability sample.
- [DORA 2025 / 2026](https://dora.dev/insights/balancing-ai-tensions/): throughput and instability associations, time shifted toward verification; observational organization-level evidence.
- [METR February 2026](https://metr.org/blog/2026-02-24-uplift-update/): task/developer selection, concurrent agents and weak measured uplift demonstrate why adaptive study methods are necessary.
- [GitHub 2025 Octoverse](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/): agentic/AI-related activity scaling, **not** demonstrated downstream value.
- [Green Software Foundation SCI for AI](https://greensoftware.foundation/standards/sci-ai/): provider and consumer environmental measurement scopes.

See [five-year roadmap](FIVE_YEAR_ROADMAP_2027_2031.md), [future scenarios](FUTURE_SCENARIOS_2027_2031.md), [quarterly scorecard](LEADERSHIP_SCORECARD_2027_2031.md), and [leadership governance](RESEARCH_PROGRAM_GOVERNANCE_2027_2031.md).
