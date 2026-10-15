# Branch consolidation checkpoint — 2026-10-13

Related: [#273](https://github.com/MSKazemi/github-trending-1000-study/issues/273), [#277](https://github.com/MSKazemi/github-trending-1000-study/issues/277). AI-assisted engineering inspection; no scientific findings or human security signoff.

## Current decision

The [read-only inventory](../research-notes/branch-consolidation-checkpoint-2026-10-13.json) records **69 branches, 40 open PRs**, and main `35928569d1f6c2f8593a41b2d8e6b140ee6edf11`. Of these, 40 heads belong to open PRs, five match a merged PR head exactly, 23 require further content/history review, and one is main. This is a dated snapshot; concurrent work changes refs. Historical PR mapping uses the latest 100 updated PRs only and deliberately holds unmapped branches. A closed PR or a squash merge does not establish content equivalence.

The existing historical archive was read through GitHub: 59 recovery tag refs were returned. This checkpoint does not execute deletion, alter the original 124-row inventory, or assert immutable tag protections. PR #281 merged concurrently during this inspection; its recovery namespace correction and consistency test are on main. The literal newline escape in its supplemental Markdown is corrected in this follow-up.

## Newly merged heads to revalidate

| Branch | Merged PR | Original head SHA |
|---|---:|---|
| `chore/safe-merged-branch-retirement-20261013` | #274 | `4f959715913d817d605c0706c95bb3d9e8e90471` |
| `chore/276-branch-lifecycle-audit` | #278 | `0a573825c1a100964f2ee653609c48fcd80e5f02` |
| `ci/enterprise-pr-qa-gates-issue-240` | #272 | `0add541d0e66b6f54e6370fa31ca686d53cb60bd` |
| `fix/retirement-snapshot-archive-prefix-20261013` | #281 | `4950dd8052ac3395ff5051e85121fcf7140d1cf8` |
| `maintenance/retire-verified-merged-branches-20261013` | #275 | `c36e51965a1b0f9a356dd43af0ee92d900b581d0` |

Do not append these blindly to the old 60-head manifest. In particular, #272 now merged with a newer head than #253; that does **not** authorize replacing the old expected SHA. Review a separately dated allowlist, verify merged-commit ancestry in current main, protection, all open PRs, and an exact recovery tag before a SHA-leased retirement. This follow-up reuses the #281 branch, so that branch must remain held while this PR is open and must be reclassified at its new head after merge.

## Remaining blockers

- **#280 security review:** zero submitted reviews were returned during this checkpoint. Its description and the canonical merge gate require a qualified security/administration reviewer for the privileged workflow and token policy. Passing CI alone does not satisfy that gate.
- **Research drafts:** source dates, source rights, contradictory claims and independent factual review remain separate acceptance requirements. Retain both versions of overlapping company reports until unique material is present in a reviewed replacement.
- **Retirement execution:** this connection exposes no branch-delete or workflow-dispatch operation; a Git push dry run failed because no GitHub credentials were available. No deletion was attempted, no token was requested, and no cleanup outcome is claimed.
- **Server enforcement:** main was reported unprotected. Main/tag rulesets and independent human approval enforcement remain repository-owner administration tasks.

## Verification and bounded next steps

On main after #281, **483 offline unit tests passed**. Source compilation and both existing artifact-integrity CLIs also passed, checking 36 files / 234 logical records. These are engineering integrity checks, not authentication of sources, reviewers, collection permission, adoption or energy outcomes. The push CI for #281 was queued when first checked and must be verified separately.

Reuse this existing branch for this documentation follow-up rather than create another task branch. Check final-head PR CI on Python 3.10/3.12/3.13/3.14 plus research-artifacts before merge, then check push CI on resulting main. Retire reviewed merged heads only through the reviewed SHA-lease procedure after the security gate; retain exact original histories in recovery tags and publish actual per-ref outcomes.

Practical maintainer lessons: keep a budget of at most 5–10 genuinely active implementation branches; store pending research work as issues and versioned provisional ledgers; reuse a suitable existing branch for bounded follow-ups; preserve exact original commits before pruning; measure success by accepted functionality and useful evidence, not branch or merge counts. Fewer branches alone demonstrates no carbon or productivity benefit.
