# Branch reconciliation checkpoint — 14 October 2026

**Review-only historical inventory; NO branch deletion authorized.** Captured via GitHub branches and paginated open/closed PRs, main commit `1a9464f030572968d1590c268dc60c3e9b57e6a7`. GitHub can change concurrently. [Machine-readable full snapshot](../ops/branch-retirement/review-only-2026-10-14.json) retains all 70 branch SHAs and PR references and is deliberately **not** in the executable retirement-plan schema.

| Type | Count | Quality / no-loss decision |
|---|---:|---|
| `main` | 1 | Never delete |
| Open PR heads | 13 | Retain (12 drafts; #280 ready but security reviewer not approved) |
| Exact original merged PR heads | 23 | Prospective archive candidates **only** after fresh branch/PR check and immutable recovery-tag approval |
| Merged PR head advanced since merge | 6 | Hold: audit unique commits and test/source provenance |
| Closed but unmerged | 27 | Hold: compare source/negative tests with canonical successor |
| **Total** | **70** | No automated retirement from this snapshot |

## Unchanged merged heads (23) — candidates, not authorization

- `chore/276-branch-lifecycle-audit` — [PR #278](https://github.com/MSKazemi/github-trending-1000-study/pull/278); `0a573825c1a100964f2ee653609c48fcd80e5f02`
- `chore/safe-merged-branch-retirement-20261013` — [PR #274](https://github.com/MSKazemi/github-trending-1000-study/pull/274); `4f959715913d817d605c0706c95bb3d9e8e90471`
- `feat/news-corpus-schema-56` — [PR #285](https://github.com/MSKazemi/github-trending-1000-study/pull/285); `003b5c52da27e6e95de06b82dd95d8f67f317c5f`
- `fix/canonical-nested-symlink-audit-20261013` — [PR #283](https://github.com/MSKazemi/github-trending-1000-study/pull/283); `2bed9ec8e8172cb47282933c011e3a8c9bd15033`
- `maintenance/retire-verified-merged-branches-20261013` — [PR #275](https://github.com/MSKazemi/github-trending-1000-study/pull/275); `c36e51965a1b0f9a356dd43af0ee92d900b581d0`
- `research/ai-era-news-corpus-2026-10-12` — [PR #59](https://github.com/MSKazemi/github-trending-1000-study/pull/59); `7f2b5cb9ddf3f6a266fe8b19411a847489c6fd01`
- `research/company-intel-2026-002-anthropic` — [PR #172](https://github.com/MSKazemi/github-trending-1000-study/pull/172); `465f60ef9e9189d6dd4081aaa49ff43eae24fc13`
- `research/company-intel-2026-003-google-deepmind` — [PR #173](https://github.com/MSKazemi/github-trending-1000-study/pull/173); `60b42d7ffbdb1604c0accc22dc5e0bea398e9697`
- `research/company-intel-2026-004-microsoft` — [PR #174](https://github.com/MSKazemi/github-trending-1000-study/pull/174); `23f1eefabfe12c7b158f364a0140d47d169cec1f`
- `research/company-intel-2026-012-cursor-anysphere` — [PR #176](https://github.com/MSKazemi/github-trending-1000-study/pull/176); `ba797cc73a407c1b33bccbf50ffb4ea5b021611a`
- `research/company-intel-2026-019-tabnine-first-screen` — [PR #233](https://github.com/MSKazemi/github-trending-1000-study/pull/233); `b90ceccad65528279a549d7a82fead5006b516dd`
- `research/company-intel-2026-020-augment-code-first-screen` — [PR #234](https://github.com/MSKazemi/github-trending-1000-study/pull/234); `f047ac2442f222192c564c03d8e0890bff16a331`
- `research/company-intel-2026-021-factory-first-screen` — [PR #236](https://github.com/MSKazemi/github-trending-1000-study/pull/236); `67443a2afeb064af2057c9ce937962b0e0f77b3a`
- `research/company-intel-2026-023-cline-first-screen` — [PR #237](https://github.com/MSKazemi/github-trending-1000-study/pull/237); `c94cd95741b2612c7fb4323182f53342fc71bb5c`
- `research/company-intel-2026-024-zed-industries-first-screen` — [PR #238](https://github.com/MSKazemi/github-trending-1000-study/pull/238); `85a44ddcc66ee415ed3ce0252745a7a16519d79c`
- `research/company-intel-2026-025-lovable-batch2` — [PR #204](https://github.com/MSKazemi/github-trending-1000-study/pull/204); `8b1b7142b245cb8eb1abaa8e6ab8575876813a3a`
- `research/company-intel-2026-026-stackblitz-batch2` — [PR #205](https://github.com/MSKazemi/github-trending-1000-study/pull/205); `ce968190327e180d1a7067159ec2d04a427bb862`
- `research/issue-67-openai-six-month-intelligence` — [PR #175](https://github.com/MSKazemi/github-trending-1000-study/pull/175); `a16098011b55724073a0634187efca318095b96d`
- `research/issue-73-007-mistral-ai-screen` — [PR #193](https://github.com/MSKazemi/github-trending-1000-study/pull/193); `5be40e0060d34c26e01617b2395cca23434bd373`
- `research/issue-74-008-cohere-screen` — [PR #194](https://github.com/MSKazemi/github-trending-1000-study/pull/194); `63109a2416417d43d0ed10fbd295f9379d623369`
- `research/issue-75-009-deepseek-screen` — [PR #195](https://github.com/MSKazemi/github-trending-1000-study/pull/195); `46b498a2a7ba6123a2ae459633047c37501a1685`
- `research/issue-76-010-alibaba-cloud-screen` — [PR #207](https://github.com/MSKazemi/github-trending-1000-study/pull/207); `f443d7d3394ccec8fdb5f8e77ac774db48af2644`
- `research/issue-77-011-xai-screen` — [PR #209](https://github.com/MSKazemi/github-trending-1000-study/pull/209); `d1f890ce2ae9a9289d56fcc5260e223a2dc3cf2a`

Squash merging does **not** retain the original branch-tip commit as an ancestor of main. Only retire after the candidate is independently reverified, the original commit is preserved under a protected exact-SHA tag, and an explicit, atomic expected-SHA deletion is approved.

## Merged-PR heads that changed afterward (six)

- `ci/research-json-integrity-247` — [PR #250](https://github.com/MSKazemi/github-trending-1000-study/pull/250); merged head `9bfcf534f72201163359ae6bb2c44f94ff7f11f5`; now `e98d19fcb58c7833900e9f3a2a79941269b72861`
- `ci/restore-canonical-integrity-gate-20261013` — [PR #266](https://github.com/MSKazemi/github-trending-1000-study/pull/266); merged head `a933e06dce1062356867de8e8f80e91214d08873`; now `e19087a17263ea1b4aeb9f96d3401c83b2757749`
- `fix/retirement-snapshot-archive-prefix-20261013` — [PR #281](https://github.com/MSKazemi/github-trending-1000-study/pull/281); merged head `4950dd8052ac3395ff5051e85121fcf7140d1cf8`; now `0c5138a6041a85aea027755e6dc6f6ed3e3f2bbf`
- `research/issue-22-supply-chain-gate-oct2026` — [PR #216](https://github.com/MSKazemi/github-trending-1000-study/pull/216); merged head `52e05f039236ce3d183b29f81fd51e13639b51dc`; now `9e0ea7654defaf196202739a11e95a349bef0fd1`
- `research/issue-7-literature-ledger-oct2026` — [PR #189](https://github.com/MSKazemi/github-trending-1000-study/pull/189); merged head `d80afb2ea0c0ccabb5073f56d113ee20001a63d4`; now `4172d37e77415ca6eff49266e27a2073b750cee4`
- `research/issue6-trending-overlap-audit-20261012` — [PR #182](https://github.com/MSKazemi/github-trending-1000-study/pull/182); merged head `ac4cf1679741434a4268cd117dd438c96be1c875`; now `cc37e2014dd0cac3610d287574e2c9c56b82a14f`

Do not remove or reset these: compare individual post-merge commits, tests, docs, data references and chronology with the canonical implementation. Unique contributions must be integrated in a reviewed PR or preserved as separately justified research.

## 27 closed-unmerged branches

- `audit/pr-merge-gate-log-20261013` — former [PR #256](https://github.com/MSKazemi/github-trending-1000-study/pull/256); `2b460c8e15819afd54e62bed1d7334d0e6a78a8e`
- `chore/enterprise-pr-merge-guardrails-20261013` — former [PR #245](https://github.com/MSKazemi/github-trending-1000-study/pull/245); `4821e9f137cfef7e6e43f0c967ccdbe1023ec96b`
- `ci/issue-240-canonical-csv-artifact-validation` — former [PR #260](https://github.com/MSKazemi/github-trending-1000-study/pull/260); `d8916e13fb1b415b3d13b9ce0ff97742dfe0c75e`
- `fix/247-nested-symlink-clean-merge-20261013` — former [PR #267](https://github.com/MSKazemi/github-trending-1000-study/pull/267); `368083577709a71875a03ef46a71c598fde01757`
- `fix/followup-ledger-gate-issue-4` — former [PR #49](https://github.com/MSKazemi/github-trending-1000-study/pull/49); `489402cd6378b23195d751eca21f3bc717461f6d`
- `quality/244-premerge-artifact-gate` — former [PR #251](https://github.com/MSKazemi/github-trending-1000-study/pull/251); `bcad1eaff6176fbc61b297495ede01497422926a`
- `quality/canonical-artifact-ci-20261013` — former [PR #259](https://github.com/MSKazemi/github-trending-1000-study/pull/259); `fd119035a627033503af03c4d4dd1eb8a7eacaa4`
- `quality/extend-canonical-data-integrity-csv-20261013` — former [PR #263](https://github.com/MSKazemi/github-trending-1000-study/pull/263); `aa6c3e68fdac09fe0671e91af1c064caeac06bca`
- `research/company-intel-2026-001-openai` — former [PR #171](https://github.com/MSKazemi/github-trending-1000-study/pull/171); `4daf83b93014996d81c9fa766ebb3d33eca235cc`
- `research/company-intel-2026-014-replit-batch2` — former [PR #196](https://github.com/MSKazemi/github-trending-1000-study/pull/196); `2365dcf71b93dded6bddad386a6f16bd6cc23908`
- `research/company-intel-2026-016-amp-inc-batch2` — former [PR #197](https://github.com/MSKazemi/github-trending-1000-study/pull/197); `23a08bbc0758223ce6f1f3b9dbda53c809ca9df8`
- `research/company-intel-2026-018-qodo-batch2` — former [PR #198](https://github.com/MSKazemi/github-trending-1000-study/pull/198); `614bb47f3c5083ae3ec1668935f872985c0623af`
- `research/company-intel-2026-019-tabnine-batch2` — former [PR #199](https://github.com/MSKazemi/github-trending-1000-study/pull/199); `d684ab7e1029ff747029ada271a985b33489bb02`
- `research/company-intel-2026-020-augment-code-batch2` — former [PR #200](https://github.com/MSKazemi/github-trending-1000-study/pull/200); `0cf2615a68f1f5b23352128d7e323c88fc180228`
- `research/company-intel-2026-021-factory-batch2` — former [PR #201](https://github.com/MSKazemi/github-trending-1000-study/pull/201); `f21722ce344304188e67ad6dc6e161dc28968ab5`
- `research/company-intel-2026-023-cline-batch2` — former [PR #202](https://github.com/MSKazemi/github-trending-1000-study/pull/202); `b84162369141a1af362268bd5207823c206e7933`
- `research/company-intel-2026-024-zed-industries-batch2` — former [PR #203](https://github.com/MSKazemi/github-trending-1000-study/pull/203); `f9884c462154ae0f291ab4ee45020f13a03245d3`
- `research/independent-page-qa-2026-10-12` — former [PR #52](https://github.com/MSKazemi/github-trending-1000-study/pull/52); `190327b6e57574b6050b8f55067bad3064ff1d2b`
- `research/issue-6-rank-drift-oct2026` — former [PR #188](https://github.com/MSKazemi/github-trending-1000-study/pull/188); `38728426909558fda5fcab618ea044eef48c7b8f`
- `research/issue-71-005-meta-screen` — former [PR #191](https://github.com/MSKazemi/github-trending-1000-study/pull/191); `b0b25a5aeca78a0d4498646674a018dd1d3771f3`
- `research/issue-72-006-amazon-screen` — former [PR #192](https://github.com/MSKazemi/github-trending-1000-study/pull/192); `8a8cdf217e57d6db13f14f685e5d4984cacd2af6`
- `research/issue-80-014-replit-screen` — former [PR #212](https://github.com/MSKazemi/github-trending-1000-study/pull/212); `4a6b4581e90a0d648b88a21d6facd3c6bd43df2a`
- `research/issue-85-018-qodo-screen` — former [PR #213](https://github.com/MSKazemi/github-trending-1000-study/pull/213); `4e9ade4ead17265465560e61ed83d263d001891b`
- `research/issue-86-019-tabnine-screen` — former [PR #215](https://github.com/MSKazemi/github-trending-1000-study/pull/215); `226d12fa0523f7a0af3620fb58b87398a1b76a26`
- `research/issue11-evidence-registry-20261012` — former [PR #184](https://github.com/MSKazemi/github-trending-1000-study/pull/184); `bb87be18c105ae9c54ef2c0fae5401ca3517d5e5`
- `research/issue22-package-trust-gate-20261012` — former [PR #186](https://github.com/MSKazemi/github-trending-1000-study/pull/186); `d4619a9a1903ff53efc5fc89d14e54b43b9ea88d`
- `research/trending-independent-page-qa-issue2` — former [PR #54](https://github.com/MSKazemi/github-trending-1000-study/pull/54); `e129d5ac16caff7d983b91d85588bc74b659a0d5`

These are not automatically redundant. Source claims in company reports must remain provisional until first-party URLs and dates are independently checked; contradictory, null, and missing evidence must not vanish during consolidation.

## Governance and action plan

1. Finish a code/security review of [#280](https://github.com/MSKazemi/github-trending-1000-study/pull/280) and have an authorized admin enforce protection of `main` plus `branch-archive/**` tags before privileged retirement. As observed today, `main` is **unprotected**, `/rulesets` is empty, and `delete_branch_on_merge` is **false**. The original push-triggered cleanup has correctly been disabled.
2. Consolidate the 12 open draft company/intelligence PRs by source-level crosswalk; do not merge unverified claims as empirical evidence. Preserve each unique source/event, date, uncertainty, correction, test and original SHA.
3. Only after human review, use a fresh manually approved allowlist and `git push --force-with-lease` (or equally atomic server-side compare/delete). Verify backups and post-action refs. **Never rerun the old 2026-10-13 manifest merely to match stale SHAs.**
4. Use one canonical branch/PR per engineering capability and avoid simultaneous duplicate agent changes to the same source report. Target ≤10 active implementation branches as a **WIP heuristic**, not a scientific result or an energy-saving claim.
5. Keep the study's goal explicit: understand AI-era development, functional reuse, real downstream adoption and lifecycle cost, with evidence-graded practical repository lessons. Repository/branch counts, stars and synthetic CI do not prove environmental benefit.

Related issues: [#279](https://github.com/MSKazemi/github-trending-1000-study/issues/279) (consolidation), [#277](https://github.com/MSKazemi/github-trending-1000-study/issues/277) (atomic retirement), [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) (rulesets). [Prior archived batch](BRANCH_RETIREMENT_AND_NO_LOSS_2026_10_13.md) retained 59 exact original commit tags. This file reports **zero new branch deletions**.
