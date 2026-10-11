# How an academic and industry advisory program should operate

**Draft, 2026-10-11.** The board described here is a **proposed governance model**, not an appointed group. No institution, university, corporation or individual has endorsed this research unless independently recorded.

## Roles and separation of authority
| Role (recommended capability; can be shared in a lean project) | Accountability | Independence safeguard |
|---|---|---|
| Scientific PI / chair | RQ scope, preregistration, publication, negative findings | cannot retrospectively relabel primary outcome after data |
| Statistical method reviewer | sampling frame, power, randomization, missingness, DAG, uncertainty | review protocol before outcomes visible |
| Software-reuse and retrieval lead | task–candidate pools, adjudicators, gold labels, search baselines | labels blinded to retriever/system when possible |
| Security/licensing reviewer | package identity, supply chain, exact source rights | no provider/maintainer self-attestation as sole proof |
| Sustainability/lifecycle expert | carbon/energy/water/hardware boundaries and calibration | veto unsupported CO2 savings claims |
| Industry user/product lead | recruit real task needs, compare alternatives, usability + retention | cannot cherry-pick favorable tasks or pay for ranking |
| OSS maintainer representative | upstream costs, contribution reciprocity, practical release/compatibility | no unsolicited participant PR spam |
| Ethics/data steward | consent, data access, protected human logs, withdrawal/corrections | no release of private developer/prompt data |
| Reproducibility lead | CI, independent re-runs, versioning, source checksums and reproducibility package | independent review of code/results before strong claims |

## Minimum practicable governance with limited resources
One lead can coordinate methods + experiments, one independent scientific reviewer can audit sampling/statistics, two blinded code judges can label a pilot, and a consenting external user can try a task. Do **not** claim a multinational professor/CEO/CTO board or enterprise data unless those partnerships actually exist. High-risk production trial and full LCA require specialist capacity.

## Leadership meetings and conflict process
**Monthly working group:** study status, blockers, source permissions, task eligibility, data quality, security/ethics incidents and resources. **Quarterly board review:** follow the scorecard; publish dated methodological deviations and contrasting stakeholder judgments. **Annual independent audit:** attempt replication and verify bibliography, dataset license and data-retention policy.

Conflict examples:
- CEO asks for spectacular growth figures, professor observes biased task selection → **publication standards win**; label exploratory or withdraw conclusion.
- CTO wants fastest time-to-ship, security reviewer finds a critical supply-chain risk → **do not reuse/deploy** until resolved, record true cost.
- Environmental chair observes lower device energy but opaque cloud/provider energy → present **partial boundary**, not total saving.
- OSS maintainer says agent PRs impose work → stop unsolicited contributions and measure upstream burden; require permission for experimental intervention.
- A potential product sponsor wants preferred ranking → separate funding from ranking labels and report conflicts; do not modify gold judgments for payment.

## Data rights and publication
All dated public GitHub capture use must comply with platform permissions. Opt-in developer logs need appropriate consent and privacy/security review. Publish scripts, annotated synthetic fixtures and aggregate results first; publishing individual raw tasks/identifiable prompts may not be permissible. Do not assign authorship/copyright of third-party OSS merely because a model generated an adaptation.

## Financial and commercial boundaries
Document source of funding/credits/paid annotators and in-kind resources. Track opportunity cost and token/CI/hosting spend; purchased or traded stars are not a research intervention. During research, independent candidate rankings should not monetize placement. If a software product becomes justified, create separate decision rights and disclose any product owner conflicts in every evaluation.

## Research integrity / stop powers
Independent statistical reviewer can block confirmatory causal interpretations; security and data steward can stop unsafe or unauthorized activity; sustainability lead can block unsupported full-lifecycle environmental claims. All can record dissent with rationale. Executive or sponsor preference should not erase null or negative results.

## Stage gates and five-year renewal
- 2027: source rights, pilot judges/accuracy, preregistration and initial task-value evidence.
- 2028: task-level replicated uplift and security equivalence.
- 2029: retriever/product only with incremental validated benefit and cost.
- 2030: field maintainability and environmental boundary audit.
- 2031: independent replication, transferability and sustainable governance/ownership.

No gate completion should be asserted without a linked paper/data/experiment registry ID, measured outcomes and sign-off records.
