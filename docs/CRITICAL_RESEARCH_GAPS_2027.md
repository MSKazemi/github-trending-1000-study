# Critical gaps and failure-mode audit — 2027 useful/green software study

**Recorded:** 2026-10-11. **Status:** an audit of our proposed protocol, not study findings. **Question:** What is still missing before claims about reusable software or carbon savings become publishable?

Prior documentation *mentions* some of these topics, but mentioning is not equivalent to a reproducible operational plan. The entries below distinguish gaps in **implementation**, **scientific identification**, and **construct measurement**.

## Ranked gaps and what closes them
Priority P0 = could invalidate a primary conclusion; P1 = materially restricts correctness/generalizability; P2 = important to translation/maintenance. This priority scale is **a project-management judgment**, not an empirical weighted score.

| ID | Priority | Gap / failure mode | Previously covered? | Required safeguard and deliverable | Metric or audit |
|---|---|---|---|---|---|
| X01 | P0 | **Independent task-to-code relevance ground truth:** syntactically similar packages may not solve the same problem | Partial in reuse metrics, no gold protocol | [Gold-set protocol](REUSE_GOLD_STANDARD_2027.md), double raters, functional tests, task/spec and candidate versions | adjudicated viable@K, reviewed unknowns, inter-rater agreement |
| X02 | P0 | **Choosing tasks only because a reusable solution exists** makes reuse-first look artificially good | Partial; stated inclusion both types but estimand conditional | Primary ITT over **all preregistered sampled tasks**, independent 'reuse-eligible' subgroup analysis | opportunity rate among all eligible task specs, sensitivity to ascertainment |
| X03 | P0 | **Discovered set != possible solutions:** GitHub, registries, local code, archive ecosystems differ | Partial in cohort C | Diverse retrieval runs, TREC-style judged candidate pool + independent deeper/random audit; report unjudged | pooled relative recall, top-K judged coverage, withheld/unseen solutions |
| X04 | P0 | **Dependency-supply-chain trust:** malicious packages, typosquatting, generated fake packages, unsafe builds | Partial license/security mention, no versioned controls | [Trust gate](SUPPLY_CHAIN_PROVENANCE_2027.md), exact package+version+source provenance; OSV/Scorecard/OSPS/SLSA checks + human review | unverified package recommendations, severe unresolved risk, provenance completeness |
| X05 | P0 | **False green savings:** lower development tokens may increase deployment/runtime/water/embodied hardware | SCI discussed, break-even not operationalized | [Lifecycle model](FULL_LIFECYCLE_BREAK_EVEN_2027.md) with equivalent workload, break-even curve, measured vs estimated boundaries | per-accepted-task lifecycle kWh, gCO2e, optional water and break-even workload |
| X06 | P1 | **Upstream maintainer externality:** reusable dependencies can move work rather than eliminate it | Some community metrics, not upstream burden | [Community and knowledge transfer](MAINTAINER_EXTERNALITIES_2027.md) | upstream support/review minutes per successful integration, response strain |
| X07 | P1 | **Benchmark leakage, weak tests, retrospective cherry picking** | Partial | task freeze, temporal cutoffs, blind tests/adjudicators, held-out private variants where permitted; [benchmark](REUSE_GOLD_STANDARD_2027.md) | leakage flags, independent-pass vs public-test-pass, audit |
| X08 | P1 | **New, educational and public-good outcomes** get mislabeled 'waste' | Mentioned, not an explicit utility rubric | type-specific objective/novelty/human-learning evidence; no universal value score | independent intended-outcome pass, research replication / learning goals |
| X09 | P1 | **People, tooling and time shift in 2027:** agents, prices, model versions and repo metadata evolve | Mentioned, no version lock policy | versions, dates, access policies, rolling replication and planned source updates | temporal robustness, version-and-cost coverage, drift |
| X10 | P1 | **Interference and selection bias:** reuse can affect shared maintainers; agent adoption is hidden; Trending is selected | Mentioned, needs formal analysis plan | two-stage cohort + opt-in randomized study, cluster effects, partial-identification sensitivity | exposure misclassification bounds, spillover analysis |
| X11 | P2 | **Searching too long is its own waste:** discovery/index/verification costs and stop rules | Mentioned, not economically optimized | [Break-even and stopping](FULL_LIFECYCLE_BREAK_EVEN_2027.md); randomize bounded search budgets in feasibility pilot | incremental qualified discovery per minute/token, time to decision |
| X12 | P2 | **Sharing existing useful code:** no common compatibility examples, SBOM, interfaces, governance or long-term support | Mentioned in playbook | copyable reuse manifest and minimal reproducible example; provenance, terms, contact | independent clean integration, reproducibility, documentation task success |

## Most serious scientific traps

### Hidden outcome-selected cohorts
The unit for randomized task intervention is the **task assignment**, and failures/abandoned tasks belong in intent-to-treat. Do not restrict the *primary* outcome denominator to tasks with verified reusable solutions because those tasks will favor the reuse arm by construction. A candidate-eligible subgroup is useful only when defined by auditors **before** arm assignment and assessed independently of the treatment result.

### No-retrieval is not no-solution
An agent may fail to find a mature package because of search ranking, outdated model knowledge, local context, non-English metadata or incomplete indexing. We must report **unknown opportunity** where the pool is unjudged and evaluate search separately from implementation quality.

### Similarity, license, security and functional fit are distinct
A code-clone detector, GitHub Trending position or embedding similarity cannot establish that adapting a candidate yields a correct, legal, maintained result. For license checks, absence of a LICENSE is **unknown/unlicensed**, never permissive by default. A missing advisory is not a proof of security.

### Lower energy is not automatically lower environmental impact
Carbon, water, hardware manufacture, local power draw, cloud inference, deployment and runtime can move in different directions. Quantify operational vs embodied and observe functional-equivalent tasks; use signed ranges, not 'tokens saved × fixed CO2 factor'.

### No assumptions of poor value based on small audience
A one-person scientific replication, public teaching artifact, accessibility tool, archival software or standardized interface may satisfy a real objective despite low stars. Require a project-type-specific outcome and resource boundary, not a universal popularity threshold.

## Immediate action order
1. Freeze unit of analysis, eligibility, primary ITT and gold judgments **before** task results are available.
2. Create a stratified task sample independent of the candidate systems' outputs, including no-known-solution cases; pilot test feasible judgments and agreement.
3. Integrate supply-chain provenance and legal/safety gates into candidate adjudication.
4. Design matched functional workload for reuse/build plus lifecycle break-even sensitivity.
5. Pilot blinded independent tasks, with logs for model version, human work, upstream maintenance and energy boundaries.
6. Preserve null/failed results and report genuine uncertainty and data not collected.

**Next phase status:** design only. This file does not validate source-code candidates, carbon savings, developers' behaviour or 2027 outcomes.

## External methodological anchors
- [2024 systematic review of real-world reuse benefits/costs](https://doi.org/10.1016/j.infsof.2024.107451)
- [NIST TREC: pooling and qrels](https://trec.nist.gov/howto.html) and [NIST bias in pooled judgments](https://www.nist.gov/publications/comparison-pooled-and-sampled-relevance-judgments)
- [Revisiting SWE-bench: dataset weakness/leakage](https://doi.org/10.1109/ICSE-Companion66252.2025.00075)
- [Census III: production library usage](https://www.linuxfoundation.org/press/open-source-usage-trends-and-security-challenges-revealed-in-new-study)
- [OpenSSF OSPS Baseline](https://baseline.openssf.org/) and [SLSA](https://slsa.dev/spec/v1.2/)
- [Green Software Foundation: beyond carbon](https://greensoftware.foundation/articles/revisiting-green-software-from-silicon-to-screen/)
