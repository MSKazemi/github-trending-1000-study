# PR #291 review and integration record — 2026-10-14

**Scope:** [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244), an engineering-only Git-tracked Python/JSON syntax and ambiguity gate. **Target:** `main`. **PR:** [#291](https://github.com/MSKazemi/github-trending-1000-study/pull/291).

## Actual review

- Inspected all seven original changed paths: `.github/workflows/ci.yml`, `CONTRIBUTING.md`, `README.md`, `docs/RESEARCH_JSON_INTEGRITY_GATE.md`, `docs/ROADMAP.md`, `scripts/check_research_artifacts.py`, and `tests/test_tracked_code_json_gate.py`.
- Reviewed fail-closed Git-index NUL-delimited inventory, top-level requirement, stage/mode checking, path/symlink avoidance, UTF-8 and strict JSON checks, compile-without-execute Python validation, cardinality and byte limits. This is read-only validation of checkout bytes, **not** a race-proof sandbox, security audit or source authentication.
- Inspected positive and negative tests for nested/hidden files, contextual Python syntax, bad UTF-8, duplicate keys, nonfinite numeric values, symlinks, missing files, size limits, newline filenames, untracked exclusions and empty index. No substantive implementation defect identified.
- Verified [pre-documentation-fix CI run 38602382600](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38602382600) succeeded with `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts` on commit `8c63b628bbd160057065489dd2ad325b81b87496`. **That run does not validate subsequent documentation-only commits; require a new exact-head run before merge.**
- Checked review submissions/threads at the time of review: none reported; GitHub reported mergeable. The separate PR #290 overlaps README/roadmap, not the new scanner. Re-check current base, mergeability, reviews and CI immediately before merge.
- Corrected a stale operator-guide introduction: it incorrectly described three steps in the matrix and omitted the standalone research-artifacts job; now documents current matrix and both research validators. This is a documentation-only correction, not evidence of a new validated result.

## Explicit non-claims and required gates

No empirical GitHub Trending collection, source-rights/robots approval, scientific preregistration, independent source or human methods review, real-world reuse/adoption result or environmental effect is implied. A repository owner should establish server-enforced required checks and independent review where needed ([#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248)). This record is an engineering-agent review and **not an independent qualified human signoff**.

**Merge condition:** completed all-five-job GitHub Actions `pull_request` workflow with success on **final** SHA; no new review objections, merge conflicts or unexpected base changes; merge with expected head SHA and verify post-merge main separately. If any condition fails, keep open and correct it.

## Practical maintainer lessons

1. Check *tracked* inputs as well as conventional code directories, including hidden or unimported paths.
2. Combine negative fixtures and per-file/aggregate bounds with an explicit fail-closed parser; never execute inputs to merely check syntax.
3. Run exact-head CI for documentation fixes too; a prior passing commit does not certify subsequent changes.
4. Treat structural engineering checks and scientifically authenticated evidence as separate gates.


## 2026-10-14 current-branch reassessment and repository-owner handoff

**Actual inspected state before this record update:** PR #291 was open, non-draft and reported mergeable against `main` at `2efbf2fbf7dabc9199945bc366baaaf7a2148b17`. Its reviewed head `9306281018d2c7624e7ceb3f5fedc9e63dd76a39` was **8 commits ahead and 0 behind**. The full current diff changed **9 paths** (no file-level deletions), including two review records. The tracked-gate test module contains **18 `test_*` methods**, not the older 15-method count in PR text. Other PR #290 overlaps only README and roadmap; independently review overlapping content if merge order changes.

**Independently verified *workflow metadata* for that exact pre-record head:** [GitHub Actions run 38619400106](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38619400106) is a completed successful `pull_request` run with `head_sha=9306281018d2c7624e7ceb3f5fedc9e63dd76a39`. All five jobs succeeded: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts`. The four test jobs include the tracked-code gate *before* unit tests. An independent local clone/test was not available: this environment could not resolve `github.com`. Do not imply a local execution happened.

**Security and scientific boundary:** The additive validator inspects Git-indexed Python/JSON **working-tree bytes** using NUL-safe staged file entries. It compiles Python without executing it and applies strict JSON syntax/ambiguity checks. It does not cryptographically bind checkout bytes to Git blobs, guarantee no filesystem race, scan submodule internals, authenticate research sources or resolve platform-access, privacy, licensing, security, preregistration or empirical validity issues. No code defect was established by this review, but green checks are not proof that every conceivable malformed input or attack is handled.

**Actual review/branch-rule state:** GitHub reported **no review submissions and no unresolved review threads**. A qualified **independent human reviewer has not approved this PR**. The `main` branch metadata reported `protected=false` and the repository ruleset listing was empty. The branch-protection detail endpoint returned HTTP 403 to this integration; an authorized owner must verify and establish enforceable controls under [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248). Past attempts to squash merge this PR reported HTTP 409 on older heads; do not infer a current conflict merely from that historical error.

**Decision:** Preserve a **merge hold** pending real independent approval. The owner should appoint a qualified reviewer, resolve any substantive comments, verify `main` remains aligned and reconfirm five passing `pull_request` jobs on the **new final head**, then use `expected_head_sha` to squash merge and inspect the post-merge `main` push CI before closing [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244). This very documentation update changes the branch SHA, so run 38619400106 is historical evidence after this commit—not proof for the new head. Record its fresh successful run in the PR conversation without another unnecessary commit.

**Practical maintainer lessons:** (1) Keep PR descriptions in sync with actual test and file counts; (2) prove an important negative-path gate runs under every target interpreter, not only that a workflow displays green; (3) distinguish workflow completion on an exact Git SHA from earlier CI; (4) make reviewer independence and server-enforced branch rules real controls, not checked-in assertions; (5) publish explicit security/scientific non-claims alongside artifact gates.

## 2026-10-14 additional bounded-read hardening and merge checkpoint

- Re-reviewed all nine changed files, current `main`, the G0-G8 repository merge policy, review threads and exact-head GitHub Actions job list.
- Corrected a check-then-read weakness: open the target once with no-follow/nonblocking flags where supported, reject nonregular opened descriptors, and cap actual read bytes (`max_file_bytes + 1`) instead of trusting only the pre-read file size. This improves local CI robustness; it is **not** a hostile-filesystem race-proof sandbox, especially for maliciously replaced ancestors.
- Added FIFO substitution, excessive-size and aggregate-limit regression tests in `tests/test_tracked_code_json_gate.py`. Earlier passing five-job Actions run `38619400106` applies only to the previous head `9306281018d2c7624e7ceb3f5fedc9e63dd76a39`, **not** these new commits.
- This engineering review is not independent qualified human review. At the checkpoint, review submissions and unresolved review threads were both empty. Do not represent an AI's own review as an independent review, and do not merge unless all final-head checks and appropriate independent maintainer approval are established.
- Practical lesson: verify the properties of the *opened file descriptor*, enforce limits on *actually read bytes*, and always rerun exact-head CI after a fix. Distinguish parser robustness from proof of provenance, scientific validity, or consent.
