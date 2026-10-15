# Issue #244 engineering audit — 2026-10-14

**Scope:** [Issue #244](https://github.com/MSKazemi/github-trending-1000-study/issues/244), [PR #291](https://github.com/MSKazemi/github-trending-1000-study/pull/291). This record is an engineering review of the offline Git-tracked Python/JSON gate, **not independent qualified human approval**, source authentication, security certification, empirical evidence or permission to scrape.

## Decisions and preserved work

- Reuse the existing `scripts/check_research_artifacts.py` and its strict JSON parser; do not install a second competing validator.
- Git-index enumeration checks NUL-delimited indexed paths in all directories, rejects nonregular/unmerged entries, symlinked parents, missing checkout paths, malformed Python and ambiguous/non-UTF-8 JSON; bounded counts and size limits.
- Preserve the existing research JSON/JSONL/CSV checks, CI matrix (3.10/3.12/3.13/3.14), SHA-pinned actions, read-only checkout, and main-only push plus PR triggers.
- Added regression cases for unresolved merge stages, symlinked ancestors and PEP 263-encoded Python source. These are synthetic offline tests, not live research observations.
- The operator guide, README, CONTRIBUTING and roadmap are updated in this PR. No hypothesis, raw observation, research denominator or protocol was intentionally modified.

## Validation and limitation

An earlier head `8c63b628bbd160057065489dd2ad325b81b87496` passed all five jobs in [run 38602382600](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38602382600). **That run does not validate later commits.** Recheck the exact final head and current `main` before merging, with all five jobs successful; local full-repo execution was unavailable because this session could not resolve github.com through its container. Review GitHub's exact-head Actions log and failing test cases, not historical success text.

The checker inspects **working-tree bytes for paths in the index**, not independently authenticated committed Git blob content. It does not inspect Git submodule internals, Markdown sources, legal provenance, dependency security, source truth, scientific validity, or independently approved consent. It is not a race-proof sandbox for adversarial filesystems. The separate `#248` server-enforced branch rules and independent reviewer check remain unfulfilled unless proven with real GitHub settings/evidence.

## Required merge gate

1. Read the final diff, confirm no loss of unique research files/tests and no unresolved conversations.
2. Require a qualified independent human review; none was present when this audit was prepared.
3. Confirm a successful pull_request run on the **actual final PR head**, and current-base alignment; check Python 3.10/3.12/3.13/3.14 and research-artifacts.
4. Merge only with expected-head SHA, then independently verify the push-triggered `main` workflow; close #244 only after this evidence is documented.

## Practical maintainer lesson

A green unit suite can miss an unimported broken Python or JSON file in an unexpected directory. Couple NUL-safe, index-based artifact enumeration to real failure-case tests and current-head CI, but never convert syntax checks into scientific claims or substitute automated checks for qualified review.


## Follow-up staged-blob safety correction (2026-10-14)

Code inspection found a bounded correctness gap relevant to local pre-commit reuse: `git ls-files` enumerated staged names but validated only working-copy contents. A bad staged `*.py`/`*.json` could thus escape the local checker if the working copy was repaired without restaging. The same canonical validator now reads each indexed regular Git blob with a validated hash, bounded blob type/size check, and validates both staged and checked-out contents. Added four synthetic negative/positive regression scenarios. This is complementary to CI checkout validation, not a new scanner.

**Review gates pending at time of editing:** final exact-head five-job CI, no unresolved human review, current-base merge safety and post-merge `main` CI. No independent qualified review or new field data is claimed by this written audit. Do not close the issue on the basis of this note alone.

## 2026-10-14 independent follow-up: ancestor-symlink swap and current-head CI

- At inspection, PR #291 head `8517506441312b9ea1594cf013b92ceeb2bc04e6` passed all five Actions jobs in [run 38621038703](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38621038703). This was verified from the GitHub workflow run and individual jobs, not a local clone. The working container could not resolve `github.com`.
- The former checked-file path performed `Path.is_symlink()` on ancestor components, then opened the entire pathname in a later operation. A concurrent directory-to-symlink replacement **after** the check could lead to scanning an unrelated outside file, even with `O_NOFOLLOW` on the leaf. This is a filesystem integrity defect, not a demonstrated real-world exploit or a research finding.
- Hardened the existing gate with `dir_fd`-relative opening of each ancestor, using `O_DIRECTORY|O_NOFOLLOW` on supported POSIX systems; the leaf remains opened with `O_NOFOLLOW|O_NONBLOCK`. Retained the best-effort platform fallback and a strict regular-file/fstat plus actual-byte-size check. Added an adversarial synthetic regression that replaces a parent *after* its precheck and expects refusal, not acceptance of outside content.
- The frozen diff compared against `main` `9dc35ea8784c909dcc397dee1dcfc1278793abcb` showed only five new company-intelligence/documentation files on the updated main since the PR base, with no overlapping paths; REST reported `mergeable_state=clean`. These facts are snapshot-specific and require rechecking before merge.
- **Validation pending for this new commit:** all five exact-head CI jobs must be green. An agent's review is not independent qualified human approval. Leave #244 open and PR #291 unmerged until that approval and post-merge main CI; #248 separately owns server-side protections.

**Practical reusable lesson:** a one-time symlink check plus a no-follow **leaf** open does not prevent a swapped **ancestor**. Where feasible, anchor traversals to open directory file descriptors, and test the deliberate check/open swap with a controlled synthetic fixture. This narrows one race but does not prove a fully race-proof sandbox.

## 2026-10-15 preservation-first integration with current main — pending final CI

A live compare showed that current `main` (commit `b6ece720220297e78f47720beadd8947638dfaac`) had advanced relative to PR #291, modifying `scripts/check_research_artifacts.py` with new company event-ledger checks and `trending_study/data_integrity.py` with bounded regular-file input. Blindly replacing the script with the PR version would have removed the newer event-ledger validator. Reconstructed the PR's target tree **from the current main tree**, then added the single canonical indexed Python/JSON scan, CI/test/docs changes and branch history. Kept `_validate_company_event_row` and its associated date/CSV logic, plus the strict stage/blob/checkout gate. Preserved current-main README content and added the tracked-gate pointer without deleting source assets.

Also corrected **both** public-CI duplicate-key diagnostic paths: `scripts/check_research_artifacts.py` and `trending_study/data_integrity.py` now raise stable duplicate-key error classes without printing any attacker-provided key string. Added a direct-cli regression for a synthetic contact-like duplicate key; the index/worktree validator already has a matching regression. This is narrow diagnostic containment, not a promise of complete log anonymization. **No qualified human review yet**; wait for all five new exact-head PR CI jobs and verify post-merge main CI only after the authorized review/merge.

**Practical lesson:** when two PRs touch a validator, reconcile unique functions against the latest main tree with explicit negative tests; neither a green older head nor an 'ours' overwrite is an acceptable no-loss merge.

## 2026-10-15 correction note (supersedes two earlier statements)

The "Validation and limitation" paragraph above says the checker inspects only **working-tree bytes** for indexed paths. That was accurate when written but is superseded by the 2026-10-14 staged-blob follow-up: the gate now validates **both** the checked-out file and the regular staged Git index blob (`git cat-file`) for every tracked `.py`/`.json`. It still does not authenticate blob content against any external trusted origin. The original text is retained as history.
