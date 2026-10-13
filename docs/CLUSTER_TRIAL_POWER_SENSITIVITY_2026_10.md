# Synthetic sensitivity analysis for 2x2 cluster task acceptance (#9)

**Prepared 2026-10-13. Status: uncalibrated design aid only.** This tool does **not** register a trial, collect human data, establish a valid sample size, simulate actual trial randomization, or power the proposed primary endpoint (**independently accepted tasks per total human-active hour**). It is a deliberately narrow *analytic normal approximation* for a **secondary binary all-assigned task acceptance** contrast.

## Reuse, not reinvention

The repository already implements deterministic four-arm cluster allocation and an all-task intention-to-treat ledger in [the trial instrument](TRIAL_PILOT_INSTRUMENT.md). This helper imports those existing four arm names, reads no participant/outcome files and does not duplicate allocation or create a new observational cohort. Python standard-library NormalDist avoids statistical dependencies. The exact accepted-task/time ratio requires pilot evidence for the joint outcome-and-time variance; no invented "20 pilot tasks gives X power" is justified.

## Reproduce synthetic arithmetic only

    python -m trending_study.power_sensitivity --input examples/power_sensitivity.synthetic.json
    python -m unittest discover -s tests -v

The fixture contains **three invented scenarios**, not pilot estimates: baseline ICC=0, increased within-cluster correlation, and then twice as many clusters. All probabilities and ICC values are assumptions. Output is explicitly not a power result for the primary throughput endpoint, nor a validated sample-size requirement.

## Model, interpretation and assumptions

Four arms: human_usual (HU), human_reuse_first (HR), agent_usual (AU), agent_reuse_first (AR). The *hypothetical* binary all-assigned ITT outcome is an independently accepted correct task; known failures/refusals/abandonment contribute no acceptance. Genuinely **unknown** outcomes must not silently be assigned failure. This illustrative model assumes every assigned task's eventual acceptance status is observed; real missingness needs prespecified bounds/sensitivity.

For hypothetical arm-specific probabilities p_a, C independently randomized clusters per arm, m tasks per cluster, and common ICC rho:

    delta = [(p_HR - p_HU) + (p_AR - p_AU)] / 2
    DE = 1 + (m-1)*rho
    n_eff_per_arm = C*m / DE
    Var(delta_hat) ~= [sum over all four arms of p_a*(1-p_a)] / [4*n_eff_per_arm]
    se = sqrt(Var(delta_hat))
    z_effect = abs(delta) / se
    two_sided_normal_rejection_prob ~= Phi(z_effect - z_(1-alpha/2))
                                      + Phi(-z_effect - z_(1-alpha/2))

The signed delta is the **balanced marginal reuse-first effect**, positive when assumed reuse-first acceptance is better. A high two-sided rejection probability for a *negative* delta would detect assumed harm, **not** benefit. The model assumes enough independent clusters, equal cluster sizes, common ICC, no cross-arm interference or shared-solution leakage, stable case mix, no missingness, and no additional clustering/block imbalance. The code requires at least **30 clusters per arm** for its asymptotic calculation; this is an operational guard, **not** a guarantee of valid nominal type-I error.

The tool does not estimate the primary accepted-tasks-per-human-hour ratio; factorial interactions, unequal clusters, developer/project clustering beyond the declared unit, allocation concealment, crossover, carryover, missingness, refused recruitment, reviewer disagreements, time/acceptance covariance, cost, maintenance and security effects remain outside the model. More tasks in correlated clusters are less informative than the same number in independent clusters.

## Input contract and fail-closed limits

Bounded JSON: schema_version 1.0; dataset_kind synthetic; exact outcome independently_accepted_binary_all_assigned; exact estimand reuse_first_minus_usual_marginal_acceptance_probability; a *string* two_sided_alpha in (0,1); 1–25 scenarios. Each scenario declares a unique opaque ID, clusters_per_arm integer 30–10,000, tasks_per_cluster integer 1–1,000, decimal-string intracluster_correlation in [0,1), and exactly the four arm probability strings in (0,1). Decimal strings permit at most six places and no exponent or NaN/Infinity; duplicate JSON keys are rejected. Input maximum 512 KiB. These are safety/validation bounds, **not** scientific recruitment advice.

## Independent research steps before genuine enrollment

1. Independently freeze task-frame source, acceptance/security/rights criteria, consent, and all-task ITT comparison (including tasks without viable solutions).
2. Complete a lawful opt-in pilot with independent reviewers, real balanced/blocked assignment, all refused/failed/abandoned outcomes, active human time, and missing-data reasons.
3. From authorized pilot evidence estimate joint binary success and time variability, cluster ICC, participation/missingness, block imbalances, practically worthwhile effect, budget and leakage.
4. Ask an independent statistician to power **the actual primary throughput ratio** using an appropriate joint bootstrap, model or Monte Carlo simulation with realistic clustering and follow-up, and publish sensitivity to assumptions, neutral and negative results.
5. Freeze the approved protocol and sample-size reasoning *before* confirmatory recruitment. If 2026-11-01 is infeasible, openly date a schedule amendment; never backdate captures.

## Methodological references

- Hemming et al., *Methods for sample size determination in cluster randomized trials* (2015): [open manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC4521133/). Describes standard DE = 1+(m-1)ICC, equal-size limitations and small-cluster concerns.
- *Optimal design of cluster randomized trials allowing unequal allocation of clusters and unequal cluster size between arms*: [open manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC7614658/). Highlights effective sample size and arm differences.
- [Trial design](TRIAL_PILOT_INSTRUMENT.md), [research governance](SCIENTIFIC_GOVERNANCE_2027.md), [inception gates](INCEPTION_CHECKLIST_2026_2027.md).

**Practical lesson:** Freeze independent task acceptance and record all randomized attempts, genuine failure/review minutes and maintenance instead of treating generated code volume or accepted PR count as the developer outcome.
