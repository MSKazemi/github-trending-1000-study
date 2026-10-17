# Cross-ecosystem GitHub issue-candidate intake (2026-10-12)

**Status: real public REST metadata observed; exploratory, convenience-selected candidate frame; zero accepted tasks, zero independent human reviews, zero randomized assignments and zero measured reuse/energy outcomes.** This is an operational continuation of the [faculty-style scientific priorities](https://github.com/MSKazemi/github-trending-1000-study/pull/61) and the [initial three-Python-repository intake](PUBLIC_TASK_INTAKE_PILOT_2026-10-12.md), *not* a confirmatory study.

## Why this limited exercise matters

The reuse-first experiment needs a **task-first list that is selected without asking whether reusable code already exists**. We therefore selected source repositories before inspecting issue bodies, implementation options or agent-generated solutions, and used the same SHA-256 selection procedure already implemented in `trending_study/task_intake.py`. Do **not** retroactively filter to tasks with discoverable packages or easier acceptance tests.

The selected six repositories were deliberately chosen for **feasibility and diverse ecosystems**, not randomly drawn from all open source. Language/category labels were chosen a priori by familiar repository focus, *not measured or validated project-level strata*. Real upstream issue reports are not necessarily bounded, reproducible, suitable, safe or consented experimental tasks.

## Source and provenance (minimal public metadata)

At **2026-10-12T20:11:31.062Z UTC**, after six public GitHub REST queries had completed, their first page of `per_page=15` newest-created-first open issue/PR records was reduced to the [immutable checked-in input frame](../examples/task_intake.cross_ecosystem_2026-10-12.json).

- All six requests used `GET https://api.github.com/repos/{owner}/{repo}/issues?state=open&sort=created&direction=desc&per_page=15&page=1`, via the connected GitHub app. Each returned exactly 15 records, so **none of the first-page source rows was manually omitted in this reduced frame**.
- A GitHub REST `issues` listing also contains pull requests. They remain recorded as exclusions; they cannot be silently counted as development-task candidates.
- Only issue numeric ID, issue number, canonical URL, UTC created/updated time, open-state and PR flag are stored. No username, issue body, private prompt, profile or token was stored.
- The timestamp above represents the **end of this bounded retrieval sequence**, **not a cryptographically attested API response timestamp**. Individual HTTP headers, raw complete API responses, etags, page-2 coverage and full repository issue universes were **not retained or verified**. Source rows may change; this reduced Git-committed frame supports re-running the *offline selection* only, not reproducing the live API's historical state.
- This **is not GitHub Trending data**, does not encounter the unresolved Trending URL permissions, and must not be merged into Study A's prospective Trending cohort.

| Source repo (convenience selected before querying) | Open REST page rows | Issue leads (non-PR) | PRs excluded | Hash-selected leads for later screening |
|---|---:|---:|---:|---:|
| [pallets/click](https://github.com/pallets/click) (Python CLI) | 15 | 10 | 5 | 3 |
| [Textualize/rich](https://github.com/Textualize/rich) (Python output) | 15 | 15 | 0 | 3 |
| [psf/requests](https://github.com/psf/requests) (Python HTTP) | 15 | 12 | 3 | 3 |
| [vitejs/vite](https://github.com/vitejs/vite) (JavaScript/TypeScript tooling) | 15 | 3 | 12 | 3 |
| [tokio-rs/axum](https://github.com/tokio-rs/axum) (Rust services) | 15 | 2 | 13 | 2 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) (Go monitoring) | 15 | 2 | 13 | 2 |
| **Total** | **90** | **44** | **46** | **16** |

These are counts of an **observed page-limited convenience frame**, not a census of issues, projects or available reusable code. A high PR fraction in the latest 15 rows of a source constrains the candidate yield; it does **not** imply the repository has few open issues overall. The older 15-row/6-selected fixture remains a distinct, earlier exploratory sample and is not pooled.

## Reproduce and inspect the 16 selected leads offline

From repository root with Python 3.10+:

```bash
python -m trending_study.task_intake \
  --input examples/task_intake.cross_ecosystem_2026-10-12.json \
  --output /tmp/task-intake-cross-ecosystem-2026-10-12.json
python -m unittest discover -s tests -v
```

Inspect `ledger` and filter `selection_status == "selected_for_independent_task_screen"` to retrieve the 16 exact issue links. Every link points to a mutable external public issue, *not* an approved task. The source frame retains all 90 rows, including 46 excluded PRs and 28 non-selected issue candidates. The deterministic selector uses no issue titles/bodies, package matching or reuse opportunity. Its checksum covers the **reduced frame JSON**, not the original GitHub API response.

All 90 records and all 16 selected records explicitly retain:

- `reuse_opportunity: unknown` — **unknown is not no solution**;
- `task_spec_status: not_frozen` and `independent_acceptance_status: not_frozen`;
- `experiment_enrollment_status: not_eligible_unreviewed`.

Source data are read-only; output publication uses a new path and must not overwrite earlier runs.

## Human screening and scientific decision gates

1. **Source/ethics gate:** appoint a qualified methods reviewer and privacy steward; check allowed public metadata use and internal requirements for contacting contributors. This exercise has **not obtained human experimental consent**.
2. **Blind task screen:** give *all 16* hash-selected issue links to **two independent human screeners** before any code-reuse search. Record clarity, scope, reproducibility, legitimacy, safety, accessibility and confounding/leakage flags; independently adjudicate disagreements. Use [feasibility review card](../templates/feasibility_task_review_card.md) and preserve all exclusions.
3. **Frozen independent specs/tests:** create separate neutral task specifications and functional, negative and security acceptance tests plus reproducible versioned target environments. Verify task legality, right to use data/code, task-version feasibility and issue patch leakage before trial admission.
4. **No solution selection bias:** include *no known existing solution* tasks wherever safely specifiable. Do not silently swap rejected candidates for attractive tasks; preregister any supplementary frame or attrition treatment.
5. **Only after frozen tasks:** have at least two independent candidate-discovery channels and blinded judges assess actual available versions, license, provenance, security, integration and task success. Label not viable/viable/unknown with evidence, not guessing from stars or text similarity.
6. **Only after approval and power review:** decide whether a randomized, consented 2-arm agent-only contrast is feasible, or a sufficiently powered 2x2 study. Check allocation leakage and whole-task human time, security/no-harm, maintainer costs and unknown inference energy. Reuse-existing GitHub issue tasks may be **contaminated by known historical fixes** and should not automatically be used in a blinded agent benchmark.

**2027 practical lesson to test:** An agent-friendly README and AGENTS.md should teach a *search -> verify -> reuse/upstream or justify new build -> test -> document decision* workflow. Its benefit must be established with independently accepted outcomes and full human/maintenance costs, **not** inferred from 16 open issue leads, PR counts or star growth.

## Source follow-up, not task acceptance

An additional [bounded independent REST-identity and issue-status recheck](TASK_SCREENING_SOURCE_RECHECK_2026-10-12.md) recorded that all 16 selected public issues were open at **2026-10-12 20:25:45.446Z UTC**, with matching GitHub numeric issue IDs, links and original `updated_at` metadata timestamps. The new `trending_study.task_screen` module binds a **pre-search human-review packet** to both the frozen convenience frame and this later metadata snapshot. No external human raters or frozen acceptance tests have yet been provided, and source-status matches alone cannot establish benchmark validity. See [PR #170](https://github.com/MSKazemi/github-trending-1000-study/pull/170).

## Publication status and issue mapping

- Issue [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2): independently audited **actual Trending** capture remains blocked by source-access review and field human QA; this REST task frame does not satisfy it.
- Issues [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21) and [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25) may have been closed for **tooling implementation**; this frame does not complete their real human task, consent or randomized-study acceptance criteria.
- [Gold-standard method](REUSE_GOLD_STANDARD_2027.md), [task experiment draft](PREREGISTRATION_DRAFT_2027.md) and [protocol freeze status](PROTOCOL_FREEZE_STATUS_2026_10_12.md) remain authoritative until a reviewed prospective amendment is formally approved.

## 2026-10-18 input integrity correction (engineering issue #446)

The offline issue-intake CLI now reads reduced frames with the repository's **shared bounded and descriptor-checked strict JSON loader**. It refuses ambiguous duplicate keys (including repeated `is_pull_request` values that could falsely admit excluded PR rows), nonstandard and unrepresentable numbers, symlinks, directories and oversized files **before** selecting candidates. A safe generic CLI diagnostic does not disclose the input filename or object-key contents. The previously frozen 90-row/16-selected exploratory fixture and SHA-256 selection algorithm are **unchanged**. No network calls or real human screening are introduced.

The synthetic regression checks include a duplicate PR key, nonfinite/overflow/underflow numerics, a source symlink, a directory, and an oversized input. These verify software integrity only; they **do not verify** the original GitHub REST source history, independent task acceptability, permissions, consent or actual downstream reuse. Keep [#65](https://github.com/MSKazemi/github-trending-1000-study/issues/65) open for those genuine scientific gates.

**Practical lesson:** reject duplicate raw keys and unsafe file types *before* assigning research eligibility. Checking the validated Python dictionary alone cannot recover a silently overwritten key.

**2026-10-18 read/write privacy follow-up (#446):** In addition to strict **input** decoding, the offline CLI now uses path-neutral **output** exception messages while preserving the exclusive-create no-overwrite guarantee. An actual subprocess smoke regression runs the original reduced six-source frame through the CLI, confirms the unchanged **90 rows, 46 excluded PRs, 16 selected unreviewed leads**, original reduced-frame digest, and verifies no task is falsely marked independently accepted. Negative cases prove a missing input and an already-existing private output filename cannot appear in stderr. These are offline software checks only, not source authentication, human task screening, consent or study preregistration.
