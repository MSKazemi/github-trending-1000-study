# Blinded review of reusable software candidates — offline pilot instrument

**Written:** 2026-10-12. **Status:** methodology/tooling proposal for [issue #21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), **not** a completed real-world study, not a registered protocol, and not evidence of software reuse or environmental savings. All examples are intentionally **synthetic**. Human raters, independent functional tests and a real candidate audit are not claimed.

## Why an independent judgment layer is essential

A search engine or agent can correctly retrieve similar code that is nevertheless unusable because of function, license, security, environment, or maintenance. The [existing pooled gold-set validator](GOLDSET_VALIDATION_CLI.md) checks declared labels but cannot establish that those labels came from independent blinded reviewers. A *new review packet and audit layer* separates discovery rankings from the two reviewers, records their disagreements and exports conservatively labeled inputs to the existing validator. No new search platform or classifier is needed.

**Research question:** Does a component already available at the task's frozen baseline meet a real user's *independently fixed* requirements safely, legally and at acceptable total effort? This requires actual human and technical investigation; these scripts only validate its record structure.

## Workflow and ownership

```text
Prospective task source (independent of whether reuse exists)
  -> Human task eligibility review + consent/rights check
  -> Freeze task specification, independent acceptance suite and baseline UTC
  -> Pool candidates from >=2 independent discovery channels + deep/random audit
  -> Freeze pool (SHA-256) and redact retrieval system names/order
  -> Reviewer A ----------\
                             -> audit labels, agreement, missingness
     Reviewer B ----------/  -> unresolved disagreements => unknown
                             -> Reviewer C adjudication only when reviewers disagree
                             -> provisional goldset input (existing goldset.py)
                             -> evidence audit + clean sandbox functional verification
                             -> interpreted *pilot* evidence; not population/global recall
```

The blinded packet includes artifact links, candidate version and historical availability because these are necessary for feasibility judgment, but omits retrieval channels, rankings, system names and previously assigned labels. Candidate IDs should be opaque. Package reputation, references, or a public issue with an existing answer may still partially unblind assessors; a script cannot guarantee effective or independent blinding.

## Run the synthetic demonstration (stdlib only)

From the repository root with Python >=3.10:

```bash
python -m trending_study.blind_review prepare \
  --pool examples/review_pool.synthetic.json \
  --output /tmp/blinded-packet.json

# These next files illustrate two hypothetical independent reviews and a third
# hypothetical adjudicator. No people performed these ratings.
python -m trending_study.blind_review audit \
  --pool examples/review_pool.synthetic.json \
  --review-a examples/review_rater_a.synthetic.json \
  --review-b examples/review_rater_b.synthetic.json \
  --adjudication examples/review_adjudication.synthetic.json \
  --output /tmp/blinded-audit.json

# Feed the conservative export to the EXISTING gold-set analysis tool:
python -c 'import json; d=json.load(open("/tmp/blinded-audit.json")); json.dump(d["goldset_input"], open("/tmp/goldset-from-review.json","w"), indent=2)'
python -m trending_study.goldset --input /tmp/goldset-from-review.json --k 2

python -m unittest discover -s tests -v
```

The output file must not already exist. `prepare` and `audit` never access the network, install dependencies, fetch source files, execute packages or read hidden tests. They check only **submitted assertions and metadata**.

## Input schemas and evidence boundary

| Artifact | Fields | Purpose / scientific restriction |
|---|---|---|
| Frozen pool | `schema_version`, `dataset_kind`, `pool_id`, `tasks` | `dataset_kind` is `synthetic`, `pilot` or `observational` and is retained in output |
| Task | `task_id`, `task_ref`, `baseline_utc`, `spec_sha256`, `acceptance_sha256`, `candidates`, `retrieval_runs` | Acceptance SHA is a commitment, not proof the tests are genuinely independent or strong |
| Candidate | `candidate_id`, `artifact_ref`, `version_ref`, `available_since_utc` | Use exact official artifact and immutable revision where possible; missing date/version cannot pass a viable judgment |
| Retrieval run | `name`, `channel`, `searched_at_utc`, `ranked_candidate_ids` | Allowed channels: local, registry, code_host, lexical, semantic, expert, deep_audit; *every candidate must occur in a recorded run* |
| Independent review A/B | `schema_version`, `pool_sha256`, `reviewer_slot`, `reviewed_at_utc`, `judgments` | Pseudonymous slots `A` and `B`, separately submitted; real reviewer independence is verified outside this script |
| Judgment | `task_id`, `candidate_id`, `label`, `gates`, `evidence_refs`, `decision_ref` | A dimension's declared pass/fail needs a nonempty traceable evidence reference; file existence and truth are **not** verified here |
| Adjudication | `schema_version`, `pool_sha256`, `adjudicator_slot`, `adjudicated_at_utc`, `decisions` | Pseudonymous third slot `C`, permitted **only** when both raters supplied disagreeing labels |

Gates are `functional`, `license`, `security`, `maintenance`, `availability`, each `pass|fail|unknown`. Labels are `viable|not_viable|unknown`. The tool refuses a *viable* assertion when any gate is unknown or failed, a candidate has no exact version/availability date, or its claimed availability is after the task baseline. A *not_viable* assertion requires at least one failed dimension. Human reviewers must substantiate evidence with exact source revision, tested OS/dependency version, locked acceptance tests, SPDX compatibility and obligations, dated advisory/provenance findings, integration burden and independent reviewer notes where appropriate. A link or `pass` string does **not** guarantee any of those conditions were actually met.

## What the synthetic output demonstrates (NOT research findings)

The example has two **fictional tasks**, four candidate pairs in one of them, retrieval records from registry/lexical/deep-audit, and hypothetical A/B/C judgments. Three pairs are double-reviewed; one lacks a second review; one has conflicting assessments resolved by a fictional third assessor. The emitted *provisional* labels include one `viable`, one `not_viable`, and two `unknown`. With a complete absence of candidates for the second task, the correct conclusion is **none found in this limited pool**, *not* that no reusable code exists on GitHub or anywhere else.

Raw agreement and unweighted Cohen's kappa are provided only for pairs that **both** reviewers labeled; `unknown` is retained as a category. Kappa can be unstable/undefined with small samples or extreme prevalence. Do not interpret these toy calculations as reviewer reliability measurements. The original pooled validator reports top-K bounds and pooled-relative recall, **never true global recall**.

## Guards before a real pilot is scientifically usable

1. **Source frame:** Freeze actual sampled user problems *without checking whether a reusable candidate exists*. Include no-opportunity, abandoned and failed tasks; predefine exclusions, selection probabilities and project-type strata. Public GitHub issues can be initial leads, not assumed equivalent to participant tasks.
2. **Independent criteria:** Human reviewers must fix task requirements, accessibility/privacy boundaries, environmental constraints and tests before treatment. Keep hidden tests outside public outputs and outside agent-visible code.
3. **Time and leakage:** Freeze GitHub repository SHA and candidate's precise version/digest; show candidate existed at task baseline. Mark previously public patches/solutions and retrospective retrieval contamination. A timestamp field is *self-reported* unless its source log is independently archived.
4. **Candidate pool coverage:** Combine local, registry, code host and/or expert channels, plus a deeper/random audit; preserve negatives and candidates nobody judged. This tool flags tasks with fewer than two channels but cannot certify diversity, sampling probability or completeness.
5. **Real human independence:** Store separate, consented, access-controlled A/B submissions until sealed; disclose affiliations/conflicts; third adjudicator should be an independent person. Slot strings A/B/C and date strings are **not** identity authentication.
6. **Supply-chain and safety:** Do not automatically install or run untrusted dependencies on credentialed machines. Require isolated bounded sandboxes and manual legal/security review. A missing known CVE is not a security certification; a popular package is not automatically trustworthy.
7. **Reporting:** Carry missingness and unresolved labels forward. Report human-active review/search time, integration cost, failure cases and follow-up. No ranking from stars, no causal productivity claims from observational GitHub traces, and no CO2/token conversion.
8. **Approvals:** Preregistration, ethics/privacy permissions, human signoff and power feasibility remain open work; merging the tool does not close issue #21 or authorize enrolling participants.

## Practical lessons to test in your own repositories

Before adding a novel subsystem to a project such as **NovaFabric** or **idkmesh**, make a short immutable task card: user goal, executable acceptance tests, existing local code, vetted official library alternatives, required exact versions/licensing, integration time budget and expected maintenance burden. Ask a second developer to assess candidates **without seeing the original agent's rankings**. If all viable candidates fail requirements, a smaller original implementation may be preferable. If reuse works, publish a runnable integration example, pinned constraints, and attribution so others can actually reuse your work. These are **proposed development practices**, not conclusions already proven by this study.

**Related:** [2027 gold standard](REUSE_GOLD_STANDARD_2027.md) · [supply-chain controls](SUPPLY_CHAIN_PROVENANCE_2027.md) · [all-task ITT](SCIENTIFIC_GOVERNANCE_2027.md) · [reuse metrics](REUSE_SUSTAINABILITY_METRICS.md) · [issue #21](https://github.com/MSKazemi/github-trending-1000-study/issues/21).

## Temporal availability must survive the entire review pipeline (2026-10-12 integration fix)

An important cross-tool validity failure was identified before this instrument was merged: a candidate released **after** the task's frozen baseline can pass the four functional/license/security/maintenance gates but still be unusable *at that historical point*. The original `goldset.py` schema only recognized the four gates, so a reviewer-declared `not_viable` due to `availability=fail` could be rejected downstream. This could cause selective loss of real historical negative candidates.

The converter now preserves a **fifth gate, `availability`**, and `goldset.py` accepts that gate when present. Historical four-gate inputs remain backward-compatible. A `not_viable` candidate is valid only with traceable failure evidence, including an availability-only failure. Conversely, `viable` cannot coexist with unknown/failed availability, and a declared `availability=pass` conflicts with an availability timestamp later than baseline. These are *consistency checks of supplied metadata*, not independent verification of package release history.

The synthetic integration regressions include a candidate with all four other gates passing and a release between task baseline and human judgment. The expected downstream label is **not viable at task baseline**, not a false functional or security failure. An incomplete search remains an incomplete pool; absent verified candidates do **not** prove a globally unavailable solution.
