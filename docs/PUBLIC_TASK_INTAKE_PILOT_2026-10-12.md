# Pilot intake of independent development-task candidates (2026-10-12)

**Research status:** exploratory candidate discovery only. Neither the five-year roadmap nor this intake sample is preregistered. No real task was assigned, independently accepted, or adjudicated. This does not prove reuse opportunity, climate savings, or agent productivity.

## Purpose and research lineage

Complements [issue #21](https://github.com/MSKazemi/github-trending-1000-study/issues/21) and [gold-standard protocol](REUSE_GOLD_STANDARD_2027.md). The independent task-first study must begin **before inspecting available reuse solutions, any agent outputs or eventual task outcomes**. This work makes a small GitHub issue candidate frame auditable; it does not convert GitHub issue reports into full experimental tasks.

The separate experimental allocator in [PR #34](https://github.com/MSKazemi/github-trending-1000-study/pull/34) remains **unmerged** as of the review. Its human/agent randomization must not receive the unreviewed issue leads here until the necessary ethics, consent, task/acceptance freeze and independent review gates are completed. Avoid mixing the observation and trial datasets.

## Selection source and scope

At approximately 2026-10-12 08:28:55 UTC we inspected public GitHub REST `issues` listings in newest-created-first order. The reduced metadata fixture commits **five actual returned rows per each of three deliberately selected repositories**: `pallets/click`, `Textualize/rich`, and `psf/requests`. The underlying source query requested the newest *15* open GitHub issue/PR entries per repository. The committed first-five subsets are **curated truncations for this bounded demonstration**, not complete API response snapshots and **not a probability sample of all GitHub issues**. GitHub's `issues` API includes pull requests; a PR does not enter task candidate selection but is preserved in the exclusion ledger.

The three repositories were chosen for convenient, varied Python OSS tasks, not at random. Their ages and established popularity do not imply any reuse verdict. Issue current status, body and comments can change after inspection. The SHA-256 output identifies the **reduced input JSON frame**, not a cryptographic snapshot of GitHub's full server responses. Store no usernames, individual profile details, issue bodies, tokens or confidential patches in this public intake.

This explicit truncation is an **exploratory feasibility limitation**; a future confirmatory sampling protocol must define full frames, query pagination/cutoffs, selection probabilities and all failure/coverage records before any recruitment or discovery measurements. We must not replace omitted source rows with positive-looking tasks.

## Reproduce the public-issue screening ledger

Python 3.10+ and standard library only:

```bash
python -m trending_study.task_intake --input examples/task_intake.public_2026-10-12.json --output /tmp/intake-screening-2026-10-12.json
python -m unittest discover -s tests -v
```

The `--output` path must be new; overwriting an existing snapshot fails closed. The script does **not** make network calls, run issue code, scrape, contact maintainers or send PRs. It checks URLs, schema, UTC dates, page order, stable issue IDs and privacy-minimized fields. It calculates a fixed-seed SHA-256 priority on `seed | repository | issue ID`, selects at most **two** open non-PR issue leads per source and preserves every input row. An issue not selected remains in the ledger. No filtering uses whether an implementation or package exists.

Every selected entry carries:
- `task_spec_status=not_frozen`;
- `independent_acceptance_status=not_frozen`;
- `reuse_opportunity=unknown`;
- `experiment_enrollment_status=not_eligible_unreviewed`.

Those values are restrictions, not evidence that no reuse exists.

## Expected bounded intake only

| Stage | Count | Meaning |
|---|---:|---|
| Reduced public issue+PR rows in three sources | 15 | Five manually truncated records for each chosen repository |
| Pull requests preserved/excluded | 3 | All three come from the selected Click slice |
| Public issue leads eligible for the intake lottery | 12 | Candidate descriptions, **not** screened/verified tasks |
| Issue leads selected for *future independent screening* | 6 | Two per repo; deterministic from seed |
| Frozen task specifications / hidden acceptance suites | 0 | Unavailable |
| Independent human judgments / verified reuse opportunities | 0 | Not undertaken |
| Randomized task attempts or environmental measurements | 0 | Not undertaken |

Counts in this table describe the fixed fixture, not the global repository population and not verified task quality.

## Required human/engineering gates before real evaluation

1. Review source-frame definitions, potential bot/spam/security/private-data issues and independently timestamp a candidate-source lock; include unopened and unsolved tasks, not only issues thought to be reusable.
2. Independently screen every candidate against a public, preregistered feasibility rubric; record **all** exclusions and reasons. Tasks without known reuse opportunities must remain eligible whenever safe and independently specifiable.
3. Independently author and freeze complete functional and negative acceptance tests, OS/runtime versions, repository commit SHAs, deadline, legal/security boundaries and allowed tool access *before any implementation/retrieval intervention*. Keep held-out tests secret from agents in the active trial.
4. Record issue edits/closures and linked PRs/patch solutions as leakage/confounding flags. Do not treat an already known historical fix as an uncontaminated challenge.
5. Obtain ethics/consent and participant permissions, and a versioned reviewed assignment/ITT analysis plan, then use the separately reviewed trial allocator. External maintainers must not be contacted or spammed to satisfy a dataset quota.
6. After the task freeze, build an **independent** candidate pool from multiple retrieval channels plus a deep/random audit. Assess license, availability at baseline, supply-chain safety, and clean-task pass with two blinded human raters. Mark unresolved candidate pairs unknown, never false.
7. Only a later properly instrumented trial may estimate full human time, provider token use, local/CI electricity, opaque cloud-energy uncertainty, 30/90d maintenance, and downstream maintainer burden. No carbon-from-token conversion.

## Reuse-first decision and external implementation comparison

This intake tool was intentionally implemented using Python's standard-library `json`, `hashlib`, `datetime`, `pathlib` and `argparse`; it extends the repository's existing offline methodological gates rather than adding a new search platform or clone detector. Existing GitHub REST issues listing is reused instead of inventing a crawler. The cost of this local validation is not characterized as measured energy, and the selected candidates are not a reusable-software benchmark.

**Related:** [protocol](PROTOCOL.md) · [ethics](ETHICS.md) · [pilot gates](INCEPTION_CHECKLIST_2026_2027.md) · [task-to-code gold protocol](REUSE_GOLD_STANDARD_2027.md).

## Secondary GitHub REST metadata spot-check — 2026-10-12

As an additional **limited consistency check**, three of the 15 reduced-frame issue identifiers were re-queried through the public GitHub REST issue endpoint on 2026-10-12, after this fixture was prepared:

| Named API issue | Rechecked identifier | Rechecked created timestamp | Comparison |
|---|---:|---|---|
| [pallets/click #3847](https://api.github.com/repos/pallets/click/issues/3847) | 5361921880 | 2026-09-06T00:43:13Z | ID, link, open status and timestamps matched fixture at recheck |
| [Textualize/rich #4235](https://api.github.com/repos/Textualize/rich/issues/4235) | 5753377703 | 2026-10-07T23:31:37Z | ID, link, open status and timestamps matched fixture at recheck |
| [psf/requests #7634](https://api.github.com/repos/psf/requests/issues/7634) | 5806823841 | 2026-10-12T00:55:23Z | ID, link, open status and timestamps matched fixture at recheck |

This is **only three public metadata re-queries**, not an authentication of the original capture timestamp, not a full audit of the other 12 records, and not a completeness audit of the original `per_page=15` GitHub responses. It cannot transform the convenience/truncated slice into a probability-sampled or accepted task benchmark. Future real task frames require full retrieval provenance and human screening. The validator now explicitly rejects future-labeled captures, blank source-panel/seed identifiers, and dot/dotdot repository path components.
