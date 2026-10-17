# Expedited five-PR integration: user-directed technical decision — 2026-10-17

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study)

**Status of this record:** Four source PRs were merged and fully verified on `main` at this checkpoint. The fifth, documentation PR #427 (which contains this record), remains **pending** until its exact-head checks and GitHub merge response complete. Consult its PR discussion and GitHub push-run readback for the final fifth outcome. This file supersedes the earlier pre-merge checkpoint's `zero merges` status **only after** those four specifically verified GitHub transactions; the older review remains a true dated snapshot.

## Explicit deviation from the pre-existing review policy

The user directly instructed the assistant to **not wait for a human reviewer, check readiness and merge**. The merge operator therefore proceeded with a documented, user-requested expedited exception to the [canonical PR merge policy](../PR_MERGE_QUALITY_GATE_2026_10_13.md) after examining each affected module/diff and validating exact-head CI, no direct path overlap, open non-draft status, and expected-head SHA on every GitHub merge request.

**No independent human review occurred or is claimed.** This user-directed exception does **not** satisfy the usual independent human security, methods, scientific or privacy signoff. Neither the user request nor automated testing is an approved source-rights determination, qualified ethics review, empirical assessment or permission to deploy the research programs. The current `main` branch reported `protected=false`; repository rulesets were `[]` at preflight. Proper [issue #248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) server-enforced rules and qualified future reviews remain strongly recommended. This single execution is **not** a blanket change to policy for later PRs.

## Exact, sequential merge evidence

All four source PRs passed five required **pull_request** CI checks on their exact source head before merging. Merges used GitHub's `merge` method (preserving original commits) with the exact `expected_head_sha`, followed by verification of `main` at the returned merge commit and all five required **push** checks (Python 3.10, 3.12, 3.13, 3.14, and `research-artifacts`) before starting the next merge.

| Sequence | PR / original issue | Expected source head | Actual main merge SHA | Successful post-merge push run | Outcome |
| --- | --- | --- | --- | --- | --- |
| 1 | [#425](https://github.com/MSKazemi/github-trending-1000-study/pull/425) / [#19](https://github.com/MSKazemi/github-trending-1000-study/issues/19) | `fc21f35a9d51e9ad2f8d9362f26cd9d89a388ecf` | `a4cd1d6af3a15c0fcd4f44c5e63023d1c983ae39` | [39057056803](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39057056803): **5/5 success** | Merged; original research issue remains open |
| 2 | [#426](https://github.com/MSKazemi/github-trending-1000-study/pull/426) / [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) | `b137d301805418c15d335f30b4eb22bcaf00bc7a` | `fd067e96c2146e23cec4517363baa2d7ea89d87e` | [39057105730](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39057105730): **5/5 success** | Merged; original research issue remains open |
| 3 | [#428](https://github.com/MSKazemi/github-trending-1000-study/pull/428) / [#222](https://github.com/MSKazemi/github-trending-1000-study/issues/222) | `43246acd6dc63b8550f1927d07ad0374a6c2ebcb` | `430cc622a13ff0e0b13c7fde45a595b35fb9b715` | [39057162240](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39057162240): **5/5 success** | Merged; original research issue remains open |
| 4 | [#429](https://github.com/MSKazemi/github-trending-1000-study/pull/429) / [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22) | `db8db8077560f8c90a5ddcdd38569999735af5a6` | `685e9e75a3f4403dd6c05575af2a27d42435133e` | [39057230108](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39057230108): **5/5 success** | Merged; original research issue remains open |
| 5 | [#427](https://github.com/MSKazemi/github-trending-1000-study/pull/427) documentation audit | **Exact final head to be verified after this record's commit** | **Pending** | **Pending** | Merge only if final-head and integrated CI pass |

No PRs were merged in parallel. Original source branches were not force-pushed or deleted. The PR comment history for each of the four source PRs explicitly records this review waiver.

## Byte-preservation verification

After all four source merges, the following source files on `main` had the **exact same Git blob SHA** as the corresponding final source PR branches, so there was no silent code-file replacement in sequential integration:

| Source file on main | Expected and observed Git blob SHA |
| --- | --- |
| `trending_study/goldset.py` | `2a6a9aac51df1e538f08b2181bbd9eb0319359c9` |
| `trending_study/news_corpus.py` | `852971828822b9a1568fd254c3f41b73be449ea6` |
| `trending_study/hiring_observations.py` | `312878731001014bbe0bd6f167edde482d4c79c9` |
| `trending_study/package_review.py` | `fb98707cc69bdeae1fed15f5aa19df03ad149af4` |

**Scientific boundaries:** these are offline syntactic validation/privacy changes, not independently verified sources, a real 1,000-item news corpus, public hiring signals, a validated reuse benchmark, measured safety, real package license approval, or a confirmed algorithmic visibility effect. The linked scientific issues #19, #56, #222 and #22 must remain open until their original empirical/human acceptance criteria are met.

## Practical maintainer lessons

1. When expedited integration is explicitly requested, **record the exception** rather than misrepresent an automated check as independent human approval.
2. Use GitHub **expected-head leases and serial merges**; a passing PR check on an earlier base cannot substitute for the integrated push run after the preceding merge.
3. Verify both **five-job integrated CI** and exact per-module Git blob identity to detect accidental code replacement even when filenames do not overlap.
4. Treat backend permission to merge an **unprotected main** as a security gap to fix, not an endorsement that every PR is safe.
5. Prefer authentic task/source evidence and reproducible scientific results over raw PR or issue closure counts. A bounded engineering fix can be merged while its research issue remains open.
