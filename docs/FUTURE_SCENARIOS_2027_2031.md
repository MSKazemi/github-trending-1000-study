# What could change in open source and coding agents, 2027–2031?

**Forecast vintage:** 2026-10-11. **Not a prediction of certain events.** Current evidence suggests fast uptake, task heterogeneity and possible delivery instability; it does not justify a single confident outcome for 2031. This register retains hypotheses and must be *versioned*, not overwritten after observing future data.

## Baseline signals we can actually cite as of October 2026
- 2026 Stack Overflow Developer Survey: named coding-agent/assistant question n=12,255; Claude Code 65.5%, GitHub Copilot 58.7%, Codex 29.5%, multiple choices; self-selected sample **not universal market share** [SO data](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) and [methods](https://survey.stackoverflow.co/2026/methodology).
- Stack Overflow, separate workplace-use question n=17,464: 65.9% respondents indicate AI coding assistants/agents, 26.2% agentic automated workflows; **different denominator and exposure** [SO AI](https://survey.stackoverflow.co/2026/ai/data).
- METR Feb 2026: experimental task/developer selection and multi-agent time measurement complicate simple productivity claims [METR](https://metr.org/blog/2026-02-24-uplift-update/).
- DORA 2025, explained March 2026: AI associated with increased throughput and instability; organization controls determine realized value [DORA](https://dora.dev/insights/balancing-ai-tensions/).
- [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/): 4.3m 'AI-related' repositories under its platform definition. An AI-related app is NOT proven to be agent-generated.
- GSF SCI for AI specification (ratified Dec 2025, published 2026) provides framework for provider/consumer emissions and functional boundaries [GSF](https://greensoftware.foundation/standards/sci-ai/).

## Six plausible shifts; each needs a trigger and possible falsification

| Shift / 2031 possibility | Leading indicators to monitor at least semiannually | Opportunity for our research | What would falsify or weaken it |
|---|---|---|---|
| **F1: Generated code supply greatly expands, while reliable maintenance stays scarce** | public agent-attributed PR volume, independent issue-to-fix rate, security incidents, maintainer review waiting, repo abandonment | measure verified task utility and support burden; avoid attention proxies | maintained outcomes and reviewer capacity improve proportionally to code volume |
| **F2: Agents become better at interpreting, integrating and patching existing software** | qualified reuse discovery@K, human review minutes, 30/90d defect burden, upgrade success across versions | task-to-component gold benchmark and cross-agent generalization | retrieval breadth improves but safely integrated adoption stagnates |
| **F3: Trusted provenance and machine-readable compatibility become key infrastructure** | registry attestation/SBOM coverage, OSV alerts, successful third-party install and version compatibility | provenance-aware ranking and reusable component contracts | trust signals have low predictive usefulness or verification cost outweighs benefits |
| **F4: Model inference cost falls per call while total task and societal energy may rise (rebound)** | measured kWh/accepted task, task demand, total service volume, region-specific carbon mix, agent retries | full lifecycle SCI, absolute vs intensity and counterfactual scenarios | both total and intensity footprints drop under equivalent measurement boundaries |
| **F5: Closed enterprise knowledge and public OSS diverge** | share of private versus public agent tasks, availability of open integration examples, portability/lock-in | consented partners, interoperable evidence formats, avoid GitHub-only population claims | open standards and portable artifacts remain widely adopted across orgs |
| **F6: Maintainer trust, security and human comprehension become binding constraints** | low-evidence AI issues/PRs, review time/accepted task, newcomers' independent fix success, release quality | verified bounded PRs, human comprehension audits, contribution guidelines | post-agent trust, comprehension and stability improve with little additional cost |

**Do not assign fabricated numerical probabilities.** Reassess per quarter with actual trends, explicit external source dates, and the conditional decision; a scenario may differ sharply across ecosystems/regions.

## No-regret versus contingent actions
**No-regret directions even if agent capability changes radically:** independent functional tests, versioned provenance, security/rights checks, responsible maintainer support, task-centered onboarding, reusable interfaces, measurement denominators and full-energy reporting.

**Contingent bets:** building an OSS-retrieval platform, training a bespoke ranking model, creating a real-time Trending dashboard, automating PR submission or making an environmental certification. Each requires prospective evidence of incremental value versus existing alternatives and credible legal/security/energy measurement before investment.

## Four axes of uncertainty for scenario analysis
1. Agent ability to plan/verify/maintain without high human oversight (low ↔ high).
2. Availability of audited and licensable existing components / public vs closed ecosystems (limited ↔ rich).
3. Transparency of energy/provider telemetry and pricing (opaque ↔ measurable).
4. Maintainer and legal/supply-chain capacity (stressed ↔ strong).

If agents become cheap and reliable, direct human coding-hours saved may be smaller in financial value, but **validation, upstream stewardship, environmental workload and rights** remain fundamental. If AI tools become more restricted/expensive, reusable open components and portable benchmark evidence may become more valuable.

## Research-plan changes by 2031 scenario
- In **high-agent capability** worlds, shift the science from generating implementations to provenance, auditability, correctness in complex contexts, energy under large task volume and long-horizon maintenance.
- In **high-dependency-risk** worlds, strengthen trust and small-vs-large dependency boundary decisions, allow fresh minimal implementations when safer.
- In **low-observability** worlds, narrow prevalence claims, expand opt-in consented data and replicate across platforms; maintain clear unknown categories.
- In **low-energy-transparency** worlds, report robust partial-boundary energy and conditional scenarios only, not absolute global 'carbon saved'.
- In **maintainer-overloaded** worlds, measure externalities and avoid unsolicited agent contributions; upstream collaboration before independent forks.

## Review cadence
Quarterly source freshness + scorecard update. Annual recorded assessment 'forecast / observed evidence / correction / next hypothesis' that preserves prior versions. The future is not a marketing slogan; it is a series of testable alternatives.

References: [advisory strategy](ADVISORY_BOARD_STRATEGY_2027_2031.md), [roadmap](FIVE_YEAR_ROADMAP_2027_2031.md), [claims and limits](CLAIM_LEDGER.md).
