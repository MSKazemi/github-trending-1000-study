# PR #290 — independent engineering pre-merge checkpoint

**Recorded 2026-10-14. Status: engineering reviewed; scientific sign-off pending.**

Related: [PR #290](https://github.com/MSKazemi/github-trending-1000-study/pull/290), [issue #6](https://github.com/MSKazemi/github-trending-1000-study/issues/6), [merge policy](../PR_MERGE_QUALITY_GATE_2026_10_13.md), [instrument specification](../TRENDING_COVERAGE_AND_RANK_PROXY_2026_10_14.md).

## Review boundary

This is a code, test and documentation review of a **synthetic, offline** instrument. It is **not** a qualified, independent human methodology review, a security certification or evidence of source permission. Inspectors reviewed the 10-file changed-file inventory, both new contracts, their shared overlap/JSON validators, related roadmap, regression tests, PR discussion and GitHub Actions jobs. The PR remains a contribution toward issue #6, not a completed empirical study.

The observed base-branch reference during the review was `main@2efbf2fbf7dabc9199945bc366baaaf7a2148b17`; it can advance. The baseline changed-file comparison was mergeable without declared conflicts, but the feature branch had diverged from main. Reconfirm the exact merge head and final combined CI immediately before any authorized merge.

## Correctness, privacy and safety findings

| Finding | Resolution | Evidence / remaining limitation |
| --- | --- | --- |
| Original JSON loader tested a path with `stat()` before a separate open/read, allowing replacement with a symlink or non-regular input in between | Fixed with descriptor-based `O_NOFOLLOW` opening, `O_NONBLOCK`, `fstat()` on the opened descriptor, and a cap on bytes actually read | Regressions exercise symlink substitution just before open, FIFO rejection and growth between size inspection and read; platforms without `O_NOFOLLOW` now fail closed |
| Unknown JSON field names were included in error messages, potentially exposing a sensitive key name | Fixed by reporting missing *known* field names and an unsupported-field count, not the untrusted names | Test inserts a private-looking key and verifies it does not appear in the exception |
| Large, malformed or ambiguous input | Kept existing strict duplicate-key, NaN/Infinity, UTF-8, field-shape and byte-limit checks | Structural parsing is not source authentication; a knowingly false but syntactically valid artifact can still pass |
| Frame denominator and rank-proxy leakage | Retained per-declared-frame fractions and train-only predictor selection with chronological, source-digest and stable-ID restrictions | No known GitHub-wide candidate denominator, independent time/provenance attestation, heldout preregistration, or real observed association |
| Output interpretation | Report is explicitly descriptive; no hidden Trending algorithm weights, causal effect, population fairness, or real empirical outcome claimed | Heldout within-page pairs are dependent. Source rights and methods review are outside the programmatic tests |

## CI evidence and precise boundaries

- The [GitHub Actions run #1474](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38602193822) finished successfully for **commit `ac0e369b39c594c150ba9213e197bf4c9d6cb274`** after the code/test corrections: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)` and `research-artifacts` all reported `success`.
- This record is written in a later documentation commit. **The run above is not a claim that the final documentation-inclusive head passed.** Check the GitHub Actions run tied to the actual final PR head.
- A workflow green check proves the checked software's tests passed. It does **not** verify GitHub data access authorization, prospective preregistration, source contents/hashes, research independence, license, publication validity or that a sample represents the platform.
- No independent human methods review or requested reviewer approval was visible during this checkpoint. The [merge policy](../PR_MERGE_QUALITY_GATE_2026_10_13.md) requires such review for a new study frame/proxy. Do not mark that gate complete on the basis of agent review or user-delegated engineering maintenance.
- `main` was observed to have branch-protection enforcement disabled at review time. That makes self-enforced merge discipline more important, not less; configure required status checks and qualified review before future empirical work.

## Merge decision and remaining work

**Not yet cleared for final merge under the repository's scientific-review policy.** Keep the PR available for independent, qualified methodological sign-off on the explicit frame denominator, page-conditioned target, chronology, predictor and holdout logic. Before merge, re-read the current PR head and main, ensure all five CI jobs succeeded on the **exact final head** with no unresolved review threads or conflicts, then use an expected-head SHA. After merge, verify the integrated `main` workflow. Do not close issue #6 until the separately listed authorized real-data audit and empirical gates have been satisfied.

## Lessons applicable to other repositories

1. Guard file **descriptors** as well as paths: schema validation cannot compensate for a symlink/file-swap race, blocking FIFO, or reads that exceed a pre-open size check.
2. Error logs are a privacy surface: do not echo unknown user-controlled field names or data even when rejecting input.
3. Separate reproducible **synthetic software checks** from reproducible research evidence and independent scientific validity.
4. Freeze sampling denominators and feature availability *before* target observations. Report unknown populations and missing measurements as unknown.
5. Require fresh exact-head CI, human approval when the study protocol changes, and post-merge main CI; do not substitute an unprotected branch or old workflow green check.
