# Claim ledger — evidence and uncertainty (2026-10-11)

This file is the citation backbone for public findings and future advice. **No original results have yet been collected.** 'Source-backed' means the cited author/platform reports the claim **within its context**, not that the conclusion generalizes to every GitHub project. 'Proposed' means not a result. Consult [reference register](REFERENCES_AI_2027.md).

| ID | Claim / research proposition | Status | Evidence | Validity boundary / test needed |
|---|---|---|---|---|
| C001 | GitHub stars alone cannot measure software usefulness | supported as measurement caution | R02, R15; [USEFULNESS_FRAMEWORK](USEFULNESS_FRAMEWORK.md) | Need independent outcome measures; does not imply stars contain zero useful signal |
| C002 | GitHub repository and contribution activity has grown markedly | platform-reported descriptive | R01 | Not causal effect of AI; definitions/platform mix shift |
| C003 | Early-2025 AI assistance slowed skilled OSS developers on the studied tasks | supported, narrow | R03 | 16 developers, 246 mature-project tasks, model/tools in 2025 |
| C004 | Late-2025 AI task-speed effects were estimated reliably at a universal rate | **not supported** | R04 | Selection/concurrency problems; do not cite a universal 2026 rate |
| C005 | Agentic AI leaves some observable GitHub contribution traces | supported, incomplete detection | R08–R10 | Hidden/misattributed assisted work; no confident label from code appearance |
| C006 | A larger number of AI-generated PRs proves better software | **not supported** | R02, R10–R12 | Need task outcomes, accepted correctness, maintenance and user evidence |
| C007 | AI may improve throughput while worsening instability | DORA-reported association | R05, R06 | Organizational observational research, not universal causal law |
| C008 | Short first human response can help assess project community health | standards-backed proxy | R07 | Exclude bots; censor unanswered PRs; not definitive user satisfaction |
| C009 | README installation test-success matters more than README word count for actual onboarding | **proposed hypothesis** | [EVIDENCE_TO_LESSON_PROTOCOL](EVIDENCE_TO_LESSON_PROTOCOL.md) | Needs randomized/documentation intervention or credible user-task study |
| C010 | AI developer speedup differs between greenfield and mature projects | **proposed hypothesis** | R03, R13 | No result here; predefine interaction/adequate sample |
| C011 | A high-star repo may be niche-irrelevant or unusable for a user's job | **possible counterexample**, not prevalence estimate | [USEFULNESS_FRAMEWORK](USEFULNESS_FRAMEWORK.md) | Collect task-level and user evidence |
| C012 | A small specialized repo can be useful despite limited stars | **plausible premise** | [USEFULNESS_FRAMEWORK](USEFULNESS_FRAMEWORK.md) | Demonstrate verified user outcomes and limitations |
| C013 | Publishing AGENTS.md means most of a repository's code was AI-generated | **unsupported inference** | R08–R10 | Require provenance or opted-in workflow logs |
| C014 | Buying stars or engagement exchanges are good ways to demonstrate value | **rejected research recommendation** | ethical policy and construct mismatch | No manipulation, artificial activity or purchased marketing |
| C015 | We can derive GitHub's exact Trending ranking weights from visible pages | **unsupported** | R16; [TRENDING_ALGORITHM_AUDIT](TRENDING_ALGORITHM_AUDIT.md) | Only infer proxies in a black-box audit |
| C016 | 'Build less, verify usefulness early' is cost-effective for all projects | **candidate practical heuristic** | [DEVELOPER_DECISION_PLAYBOOK](DEVELOPER_DECISION_PLAYBOOK.md) | Quantify by project risk/type and real-world experiments |

## State transitions
Proposed → observed → analyzed → independently reviewed → context-validated → replicated. Each move needs an actual dataset ID/snapshot, code commit, effect size/CIs, comparison, limitations and reviewer approval. Do not put unsourced '2027 findings' into this ledger.

## Correction policy
Keep negative/null results, update links when new versions supersede old ones, and preserve the earlier version with a dated explanation. Never silently delete contradictory studies.
