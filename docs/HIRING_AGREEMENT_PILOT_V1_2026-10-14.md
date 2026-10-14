# HIRING-INTEL #223 — proposed codebook v1.0.0 and blind double-coding pilot

**Proposed version:** `hiring-223-codebook-v1.0.0` (documentary proposal, not a frozen or implemented instrument; substantive revisions should receive a new version). **Status:** proposal only; **software, machine-readable frame, human protocol/rights approval and independent human ratings are absent**. **Date of proposal:** 2026-10-14. **Evidence status:** no computed agreement results or employer investment claim has been established.

[Issue #223](https://github.com/MSKazemi/github-trending-1000-study/issues/223) depends on [#220](https://github.com/MSKazemi/github-trending-1000-study/issues/220). The original 18-row source audit and six-lead expansion are retained without rewriting. The [canonical v0.1 proposal](HIRING_CODEBOOK_2026-10-13.md) remains unchanged; this proposed revision has not been approved to replace it; do not treat its exploratory `theme_codes` or `theme_hypotheses` as independently coded votes.

## 1. Proposed sampling frame, unit and exclusions (not frozen or preregistered)

The analysis unit is an **official individual requisition with a readable description body**, coded once per distinct source role. We start from **24 purposively collected leads** observed in the source registers on 2026-10-13: [18-row audit](../references/ai_hiring_job_leads_source_audit_2026-10-13.csv) plus [six-row expansion](../references/ai_hiring_expansion_leads_2026-10-13.csv). A future machine-readable candidate frame is proposed at `references/hiring_agreement/pilot_frame_v1.json`; **that file does not exist in this branch**. It would need to enumerate all 24 without dropping unsuccessful or disputed leads. The S01–S18 and E01–E06 IDs below are proposed aliases for the source-audit seed rows and expansion CSV row order, respectively, not existing machine-readable identifiers.

| Proposed frame status | N | Policy |
|---|---:|---|
| `selected_pending_recheck` | **9** | Original audit items S01–S06, S09, S10 and S12, recorded as directly read on 2026-10-13. Every item must be independently rechecked for access and retention rights *by each coder*; unavailable bodies receive `not_reviewable`, never `absent`. |
| `index_text_only` | **13** | Eight source-audit and five expansion leads with indexed text but no authenticated direct description. Excluded, not negative theme observations. |
| `identity_hold` | **1** | S11 has unresolved Cursor URL versus SpaceXAI body identity, quarantined from employer comparisons. |
| `direct_access_unconfirmed` | **1** | E02 is classified as `official_individual_page` in the expansion ledger, but current direct access is unverified; proposed deferral pending renewed verification. No timestamped 2026-10-14 spot-check artifact is supplied here. |
| **Total frame** | **24** | Retain original source rows and exact reason for all 15 excluded/deferred items. |

**Sampling caveat:** the nine were selected *after* an exploratory source screen; the selection is not random, preregistered, representative or predictive of a company's hiring investment. The nine are **candidates** only, not nine authenticated live ads as of 2026-10-14. Current source availability, original posting dates, rights, employers' hiring decisions and independent reviewers are unknown. No proxy, bypass, repeated unattended crawling, or redistribution of full job descriptions is authorized.

## 2. Controlled evidence layers and decision rules

- **Direct-description claim:** what responsibilities and skills *an individual employer/ATS job description body explicitly advertised* when the coder accessed it (include actual UTC access time and a short original-word evidence note). A direct job description is still a company's claim, not a delivered product or investment amount.
- **Index/title-only lead:** search index, careers list, or inaccessible/identity-conflicted page; it **cannot** supply a positive or negative theme vote in this pilot.
- **Analyst interpretation:** hypotheses about product roadmap, research trends, reuse effects or 2027–2031 outcomes; kept **out** of the blind coding packet and out of ground-truth counts.

For each directly read body and each theme: `present` only for an explicit responsibility or required capability; `absent` when the sufficiently readable body lacks such a claim; `uncertain` when the text cannot resolve the decision; `not_reviewable` **only** when the direct body was not accessible. A title, paraphrased prior analyst note, indexed snippet, or predicted company product is **never** enough. Multiple `present` labels are allowed. Record short paraphrased evidence for every positive/uncertain and access failure. Negatives require an actual body review, not an unsuccessful fetch.

### Proposed multilabel themes

| Key | Positive evidence required | Do **not** infer from |
|---|---|---|
| `agent_runtime` | Agent/tool execution loop, scheduling, orchestration, controlled action execution | Generic assistant/chat/UI labels |
| `context_memory` | Persistent agent state, context assembly/retrieval, long-lived memory mechanisms | Large context window or generic database alone |
| `evaluation_quality` | Agent-specific tests, regressions, benchmarking, error analysis or quality measurement | Unqualified "high quality" marketing |
| `rl_training` | Reinforcement learning, post-training pipelines, training environments/feedback optimization | General model use, fine-tuning without relevant detail |
| `sandbox_security` | Isolated code execution, secrets/permissions boundaries, threat containment or privilege control | A bare claim of being secure or SOC2-compliant |
| `enterprise_integrations` | Enterprise identity/governance, SSO, connectors, access policies or business-system integration | Enterprise customers mentioned without an engineering task |
| `inference_efficiency` | Serving throughput/latency, model routing, inference optimization or runtime unit cost | Faster developer workflow or generic performance promise |
| `developer_reuse` | Explicit existing-code search/discovery, dependency or component reuse, reusable maintained agent libraries | Code generation, generic tooling or ordinary SDK alone |
| `platform_infrastructure` | Shared agent APIs/SDK/runtime substrate, distributed platform services or foundational developer infrastructure | A one-off feature or interface alone |
| `agent_operations` | Deployment, monitoring/observability, incidents, rollback/recovery, operations of agents | Generic backend maintenance without agents |
| `other` | Explicit relevant role task not captured above; justify why none fit | Ambiguous or absent evidence |

Labels can overlap **only** when separate evidence supports each: e.g., a security sandbox plus an enterprise SSO connector may earn both `sandbox_security` and `enterprise_integrations`; a generic word "platform" alone earns neither `platform_infrastructure` nor `agent_runtime`. If the text is insufficient, use `uncertain` rather than resolving by intuition.

### Independent primary advertised task (nominal taxonomy)

Assign **exactly one** task representing the clearest central advertised deliverable: `agent_harness`, `context_memory`, `evaluations`, `rl_post_training`, `security`, `enterprise_integration`, `inference_efficiency`, `reuse_discovery`, `platform`, `operations`, `other`, `uncertain`, `not_reviewable`. The first eleven categories map to their same-domain theme; a chosen category requires that theme marked `present`. Use `uncertain` for equally prominent/tied/insufficient tasks (do **not** use a hidden tie-break order), `not_reviewable` if the body was not available. Do not make "primary" into a prediction of the employer's budget or roadmap.

## 3. Blind independent workflow and audit trail

1. **Custodian/rights gate:** Record source and employer identity, access rules and any retention restrictions outside the rater packet. From the 24-lead frame, confirm the nine designated individual descriptions by direct employer/authorized ATS body access; do not use cached snippets as stand-ins. If rights/access fails, keep the item with access=`unavailable`. Preserve the original source ledgers; the proposed manifest is not yet created or frozen. Any later approved sampling revision should be a new version.
2. **Separate coders:** Obtain two genuinely distinct, consented human reviewers. Give each the v1.0.0 rubric and a separate blank packet. Hide original analyst `theme_codes`, `theme_hypotheses`, company predictions, each other's markings and any release forecasts. The source body may itself identify the employer: **company masking cannot be guaranteed**. The public manifest is not cryptographic blinding. Human independence, blinding and rights still require an external custodian's verification.
3. **Record votes independently:** Each reviewer must record all nine item IDs (including failed access), UTC `source_checked_at_utc`, source access, all 11 theme decisions, a primary task, concise evidence/uncertainty and a counterinterpretation. `human` and independence flags are **self-attestations, not software-verified identities**. Preserve unmodified raw ratings and SHA-256 checksums; do not copy the other's answers.
4. **Compute pre-adjudication agreement:** Compare both inputs only after both are sealed. A future implementation must reject mismatched samples, duplicated IDs, missing decisions, false negative inaccessible sources, incompatible primary codes, malformed UTC times and unacknowledged nonhuman ratings; these guards have not been implemented or tested here. Report source-frame N, selected N, per-label jointly binary-rated N, `uncertain`/`not_reviewable` counts, full 2×2 confusion, raw observed agreement, positive/negative agreement, and **per-label Cohen's kappa**, plus separate **nominal primary-task kappa**. Retain every disagreement, including abstention differences.
5. **Third-party adjudication:** A different human may receive disputed item/code pairs after sealing the two original forms, still without product forecasts. Give decisions with short source-backed reasons. A separate adjudication file records `complete` or `partial`. **Never overwrite pre-adjudication ratings or replace reliability coefficients with consensus.** Log disagreements that remain unresolved.
6. **Human research signoff:** Only after consent/access/source audit, genuine independent reviewers, source permissions, denominator review and third-party methodological approval should #223 be described as having a completed independent pilot. There is **no such pilot result in this change**.

## 4. Planned offline interface and schema (not executable)

**The module, its tests and the proposed JSON frame are absent. Do not run the following commands as a current repository workflow.** This block specifies a proposed interface for a separately reviewed implementation; it has not been validated as runnable or standard-library-only:

```bash
python -m trending_study.hiring_agreement verify-frame --frame references/hiring_agreement/pilot_frame_v1.json --root .
python -m trending_study.hiring_agreement pack --frame references/hiring_agreement/pilot_frame_v1.json --output /tmp/hiring_coder_A.json
python -m trending_study.hiring_agreement pack --frame references/hiring_agreement/pilot_frame_v1.json --output /tmp/hiring_coder_B.json
# Planned only: humans would independently fill the two templates and verify direct source access.
python -m trending_study.hiring_agreement analyze --frame references/hiring_agreement/pilot_frame_v1.json --coder-a /tmp/hiring_coder_A.json --coder-b /tmp/hiring_coder_B.json --output /tmp/hiring_pre_adjudication.json
# Planned optional interface, after a third independent human resolves disagreements:
python -m trending_study.hiring_agreement analyze --frame references/hiring_agreement/pilot_frame_v1.json --coder-a /tmp/hiring_coder_A.json --coder-b /tmp/hiring_coder_B.json --adjudication /tmp/hiring_adjudication.json --output /tmp/hiring_with_adjudication.json
```

Any future implementation must create output files **exclusively** (never overwrite existing ratings/results). Keep private files outside the repo until ethics/provenance review. Proposed implementation paths are `trending_study/hiring_agreement.py` and `tests/test_hiring_agreement.py`; **neither exists in this branch**. The original source ledgers, sample and disagreement records must remain separately available to authorized reviewers. A future valid analysis result must include SHA-256 digests of submitted files and explicitly report `human_independence_verified: false` because software cannot establish the human/consent/blinding facts.

**Proposed adjudication file shape (not a validated schema):** `{"schema_version":"hiring-223-v1", "sample_id":"hiring-223-direct-read-candidates-2026-10-14", "adjudicator_id":"third_reviewer", "predictions_unseen_attested":true, "decisions":[{"item_id":"S01", "code":"agent_runtime", "decision":"present", "rationale":"Short source-backed rationale"}]}`. A future implementation must accept only actually disputed item/code pairs, reject every extra, duplicate or invalid decision, and report outstanding disputes as pending. None of these checks is implemented here.

## 5. Proposed agreement mathematics and limitations (no computed results)

For each binary theme, among roles on which *both* rated `present` or `absent`, construct cells `PP`, `PA`, `AP`, `AA` and `n=PP+PA+AP+AA`. Then observed agreement `P_o=(PP+AA)/n`, chance agreement `P_e=(A_present×B_present + A_absent×B_absent)/n²`, and unweighted nominal **κ = (P_o−P_e)/(1−P_e)**. If `n<2` or `P_e=1`, a future report must leave κ **null with a reason**, even with 100% apparent agreement. Positive agreement is `2PP/(2PP+PA+AP)` and negative agreement `2AA/(2AA+PA+AP)`, each null if its denominator is zero. For primary tasks, the same nominal κ formula sums marginal products across the mutually exclusive task categories; `uncertain` and `not_reviewable` are excluded but separately counted. **No pooling of all multilabel decisions into one misleading κ.**

Interpretation is deliberately descriptive: the source selection is retrospective, small and employer-clustered, the full 24-lead frame was purposive, missingness can be nonrandom, and κ is sensitive to prevalence and marginal imbalance. Do not compute job-opening rates, company rankings, confidence in hiring forecasts, causal effects or inter-rater reliability until the separate real human ratings exist. See [Cohen (1960), original nominal agreement definition](https://doi.org/10.1177/001316446002000104), [Feinstein & Cicchetti (1990), prevalence paradoxes](https://pubmed.ncbi.nlm.nih.gov/2348207/) and [Cicchetti & Feinstein (1990), positive/negative agreement](https://pubmed.ncbi.nlm.nih.gov/2189948/).

## 6. Validation and remaining completion gates

**Current engineering checks:** run the existing offline suite with `python -m unittest discover -s tests -v` and compile with `python -m compileall -q trending_study tests`. These checks do **not** validate an absent hiring-agreement implementation or compute agreement. **Still required for software readiness:** a separately reviewed module, machine-readable frame, independent acceptance criteria, and regression tests using exclusively **synthetic, explicitly fictional reviewer records**, including invalid inputs and write-once outputs. The planned `verify-frame` command above is unavailable; future passing tests would establish computation and schema safety, not observed agreement.

**Still required for completed scientific #223:** human ethics/rights permission; two real independent human coder packets with source access; external identity/blinding signoff; actual per-theme disagreement + coefficients and suitable sparse-cell interpretation; third-person adjudication and retained pre-adjudication audit; acceptance by the owner of #220's source-screening method. **Do not close #223 solely on a green CI run.**

### Lessons for this and other repositories

- Freeze *definitions, inputs and exclusions* rather than publishing only headline percentages; ambiguous sources should produce missingness, not success or failure counts.
- Maintain immutable first-pass evidence, corrections, human ratings, adjudications and codebook versions independently so reviewers can trace changes and avoid data leakage.
- Use separate outcome tests for **verified code reuse, real task acceptance, maintainability, license/security and total operator time** before turning hiring-language trends into recommended development investments.
- Publish null/negative outcomes as carefully as positive cases, and keep a reproducible offline fixture-based gate without claiming the fixtures are study evidence.