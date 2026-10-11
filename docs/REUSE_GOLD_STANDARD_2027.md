# Task-to-existing-software gold-standard protocol

**Status:** prospective, no audited benchmark exists yet. **Primary role:** determine whether a task had a *safe, legally usable and functionally adequate* existing implementation before anyone writes new code.

## Units and timing
- **Task** = independent, time-stamped real user problem, environment, nonfunctional requirements and frozen acceptance suite. The tasks must be selected from a documented issue/task frame **before** looking at candidate rankings or experiment outputs.
- **Candidate** = exact version/source commit of a specific prior component available **as of the task's timestamp**. Do not compare against software first released later. Store package URLs/identifiers and canonical project lineage, not just a mutable GitHub slug.
- **Task–candidate pair** = evaluator unit, with per-dimension annotations and uncertainty.
- **Solution outcome** = installed/integrated result meeting frozen functional and security requirements. Similar README text is insufficient.
- **Task opportunity label** = whether the independently audited candidate pool contains >=1 **verified feasible** candidate. When pool incompleteness prevents that judgment, mark **unknown**; do not label all negative.

## Construct a sample independent of any model
1. Predeclare ecosystems/tasks and sources (real issues, consented developer needs, approved standard tasks). Stratify by project type, language, user experience, old/new repos, complexity and whether a *known* solution exists, without conditioning the primary analysis solely on known-solution tasks.
2. Fix exact task timestamp; freeze functional and nonfunctional acceptance tests, environment, license/security constraints and independent reviewer instructions **before** running any retrieval system.
3. Candidate generation from mutually distinct channels: (i) existing local/dependency graph, (ii) registry/package search, (iii) GitHub/other code-host search, (iv) lexical/BM25 code/docs, (v) semantic/embedding retrieval, (vi) human domain specialists. Document query time, index date, search budget, hit rank and **eligible source frame**.
4. Merge/deduplicate canonical components by package URL and stable repository ID, preserving forks, mirrors and versions separately when technically relevant. Save hashes and licenses. Search should never directly execute arbitrary downloaded code.
5. Follow a TREC-style **pooling** plan: each system supplies top-K candidates; supplement with a **random/deep pool audit** to discover what all systems missed. Document the sample scheme and unjudged coverage. TREC pooling can favor systems contributing to the pool, so avoid evaluation exclusively on one proposed agent's candidates.
6. Two assessors who do not know which retriever proposed the candidate independently annotate a balanced stratified sample. Resolve disagreements with a third adjudicator, and report raw agreement plus kappa only where meaningful; do not replace unresolved with 'bad'.
7. Feasibility test candidate within secured, resource-limited isolated environment against fixed tests. Never run untrusted third-party code on the developer's machine. Record errors, exceptions, human assists and environment fingerprints.
8. Preserve original assessor labels as well as final adjudication and confidence. A gold set contains **actual provenance and test evidence**, not only someone's "verified" checkbox.

## Required pair labels (independent, not one 'score')
| Dimension | Values / required evidence |
|---|---|
| Relevance to task | direct / needs adapter / no fit / unknown, with tests and code/API references |
| Functional task | pass / fail / not run / not applicable (each acceptance criterion result) |
| API/OS compatibility | pass / fail / unknown, platform and version |
| License & rights | compatible / incompatible / unknown; SPDX license expression plus reviewed obligations |
| Security/provenance | acceptable / unacceptable / unknown, date and specific advisory/build evidence |
| Maintenance | active enough for specified risk / risky / unknown; recent policy/release and owner capacity (not commits alone) |
| Integration effort | developer human-active minutes and documented dependency footprint, incl. failed attempts |
| Candidate availability | available at task baseline / not available / unknown with timestamp evidence |
| Duplicate/lineage status | same upstream, fork, mirror, independently derived, unknown |
| Decision | reuse / upstream extension / compose / build new / defer, with rationale and what would change it |

**Viable:** available before baseline + functional acceptance + applicable license + required security requirements + acceptable integration cost. A missing signal must be explicitly unknown. For high-risk software, unknown security/rights blocks a reuse recommendation until resolved.

## Evaluation with incomplete candidate judgments
- **Precision@K**: proportion of top-K candidates adjudicated relevant/viable, but report alongside **judgment coverage@K**. If some unjudged, give optimistic/pessimistic bounds or mark the point estimate undefined rather than coding them false.
- **Relative recall@K**: recovered adjudicated viable candidates divided by all *known* viable candidates in the combined pool. Label *pooled relative recall*, NOT true recall over all open source.
- **Task opportunity detection**: at least one verified viable candidate in top-K vs independent adjudicated pool; report recall wrt audited opportunity-positive tasks and the number with unknown opportunity.
- **Clean install success** and **total integration effort** require independently observed attempts, including failures.
- **Rank calibration**: do higher model relevance scores predict passing verification? Hold out tasks chronologically, not random near-duplicates.
- **Inter-rater reliability**: calculate kappa for categorical relevance/feasibility in double-coded subset; class imbalance can distort kappa, so also report per-label agreement and prevalence.
- **Test strength**: adversarial/negative and compatibility tests, independent tests not disclosed to coding agents before submission. Record if public test accidentally leaks solutions.
- **Data contamination**: exact duplicate tasks, upstream PR patches, repository included in agent training or accessible public solution pages may bias capability evaluation. Undisclosed pretraining cannot be ruled out: report cutoffs and use withheld newly-authored task variations where feasible.

## Quantitative reporting minimum
Date and source frame; task count and categories; N candidate pairs per channel; how many candidates/versions were unique, adjudicated, viable, unknown, rejected for license or security; rater agreement; candidate pool coverage; retrieval runtime/tokens and energy costs; independently passed tasks; failure causes; confidence intervals clustered by task. Do not invent 'ground-truth total available software' from an incomplete crawl.

## Explicit non-goals
- Declaring that a clone is 'garbage' solely because of textual overlap.
- Claiming to inventory every usable GitHub/registry package.
- Having agents write the test assertions for the same solution they are being evaluated on.
- Publishing unlicensed copied code or raw security-sensitive package details.
- Inferring project quality from Trending status or total stars.

References: [NIST TREC collection methodology](https://trec.nist.gov/howto.html), [NIST pooled vs sampled judgments](https://www.nist.gov/publications/comparison-pooled-and-sampled-relevance-judgments), [ICSE 2025 SWE-bench leakage analysis](https://doi.org/10.1109/ICSE-Companion66252.2025.00075).
