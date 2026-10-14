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
