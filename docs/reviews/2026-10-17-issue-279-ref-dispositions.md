# Issue #279 — 52-branch no-loss disposition and safe-retirement holds (2026-10-17)

**Read-only, historical pinned SHA assessment. No branch deletion authorization.** This ledger is based on [the original crosswalk](./2026-10-17-issue-279-no-loss-branch-crosswalk.md) and its eight frozen JSON batches. The information is not a GitHub transaction: one draft head (#440) moved and another PR changed state after capture; re-inventory before every action. Independent human source, security, methods and admin reviews have not occurred.

## Quantified triage without false assurances

| Classification | Branch tips | Exact statement and next step |
|---|---:|---|
| Git ancestor of frozen main | 18 | Original branch tip commit is already reachable from pinned `main@62254996c69fc8c359650b801b6e4935048c4f21`; no unique non-ancestral commit. Preserve branch PR history; require protected exact-tip recovery tag and live lease before deletion |
| Diverged but all compared changed file blobs equal by path | 3 | Complete GitHub file-diff path list is byte-identical on pinned main, but historical branch commits **are not ancestral**. Preserve original commit SHA in immutable recovery tag before any retirement |
| Open PR head | 6 | Mandatory hold. On the date captured these were PR #435–#440 (draft status later changed); no branch retirement while open |
| Other divergent source or code differences | 25 | Mandatory file/test/source-event/negative-finding comparison. No no-loss or semantic equivalence inference and no authorized deletion |
| **Total non-main heads** | **52** | **0 authorized to delete by this ledger** |

**Why this does not prove that branch count is solved:** opening and merging a PR can increase or leave unchanged the count of retained refs; deleting heads also requires server-side ruleset enforcement (#248), a protected immutable recovery tag with tested restoration, and a separately approved Git `--force-with-lease` deletion (#277). The six open-PR head refs in this *snapshot* do not establish the current number of active implementation workstreams; other untracked or agent-assigned WIP may exist. Target <=10 truly active implementation branches, not a vanity raw ref figure.

## Exact per-ref disposition (not deletion approval)

| Branch tip at snapshot | Ahead / behind | Same-path blobs / compared files | Class | Source part |
|---|---:|---:|---|---|
| `audit/branch-merge-readiness-20261016` `245a8b496673` | 1 / 296 | 1 / 1 | byte-equal; hold for tag | `part-00.json` |
| `audit/issue-100-provisional-ledger-preservation-20261016` `f67990a82fdf` | 0 / 285 | 0 / 0 | ancestral; hold for tag | `part-00.json` |
| `audit/merge-disposition-20261016-evening` `520479809983` | 0 / 264 | 0 / 0 | ancestral; hold for tag | `part-00.json` |
| `audit/pr-merge-gate-log-20261013` `2b460c8e1581` | 1 / 715 | 0 / 1 | requires content/source review | `part-00.json` |
| `chore/enterprise-pr-merge-guardrails-20261013` `4821e9f137cf` | 5 / 748 | 0 / 9 | requires content/source review | `part-00.json` |
| `chore/248-reviewable-ruleset-payloads-20261014` `2c2494ffb265` | 0 / 266 | 0 / 0 | ancestral; hold for tag | `part-00.json` |
| `ci/enterprise-pr-qa-gates-issue-240` `fd4209a82047` | 8 / 486 | 4 / 5 | requires content/source review | `part-00.json` |
| `ci/issue-240-canonical-csv-artifact-validation` `d8916e13fb1b` | 6 / 711 | 0 / 3 | requires content/source review | `part-01.json` |
| `ci/research-json-integrity-247` `e98d19fcb58c` | 9 / 713 | 0 / 5 | requires content/source review | `part-01.json` |
| `ci/restore-canonical-integrity-gate-20261013` `e19087a17263` | 3 / 673 | 1 / 2 | requires content/source review | `part-01.json` |
| `docs/ten-issue-merge-disposition-20261016` `5b4e139d6c0f` | 1 / 291 | 1 / 1 | byte-equal; hold for tag | `part-01.json` |
| `feat/issue-23-lifecycle-sensitivity-envelope-20261016` `a6646fdf14c8` | 5 / 295 | 4 / 4 | byte-equal; hold for tag | `part-01.json` |
| `fix/followup-ledger-gate-issue-4` `489402cd6378` | 3 / 791 | 0 / 3 | requires content/source review | `part-01.json` |
| `fix/issue-19-goldset-input-safety-20261016` `2654dddf69f4` | 3 / 295 | 2 / 3 | requires content/source review | `part-01.json` |
| `fix/issue-22-license-evidence-public-url-20261016` `9675bb6e36e7` | 3 / 295 | 2 / 3 | requires content/source review | `part-02.json` |
| `fix/issue-222-requisition-closure-interval-20261016` `b7f0359a1fbe` | 3 / 295 | 2 / 3 | requires content/source review | `part-02.json` |
| `fix/10-cost-ledger-and-study-tracker-consolidation-20261017` `c990eefdb292` | 0 / 60 | 0 / 0 | ancestral; hold for tag | `part-02.json` |
| `fix/10-cost-ledger-safe-file-reader-20261016` `1e656cfcbceb` | 0 / 284 | 0 / 0 | ancestral; hold for tag | `part-02.json` |
| `fix/19-goldset-redacted-errors-20261016` `fc21f35a9d51` | 0 / 272 | 0 / 0 | ancestral; hold for tag | `part-02.json` |
| `fix/22-noncanonical-ipv4-urls-20261016` `db8db8077560` | 0 / 276 | 0 / 0 | ancestral; hold for tag | `part-02.json` |
| `fix/22-pypi-duplicate-slash-20261017` `643c43066a8d` | 1 / 0 | 0 / 3 | open PR hold | `part-02.json` |
| `fix/24-maintainer-burden-input-and-overflow-20261016` `351c4f335eb3` | 0 / 180 | 0 / 0 | ancestral; hold for tag | `part-03.json` |
| `fix/24-unknown-effort-not-zero-20261017` `b86b99ed0ff3` | 1 / 0 | 0 / 2 | open PR hold | `part-03.json` |
| `fix/56-news-query-order-20261016` `b137d3018054` | 0 / 271 | 0 / 0 | ancestral; hold for tag | `part-03.json` |
| `fix/56-preserve-unique-query-order-20261017` `0bbd29e24e4c` | 1 / 0 | 0 / 3 | open PR hold | `part-03.json` |
| `fix/222-cross-source-requisition-collision-20261017` `3f4178e7096d` | 1 / 0 | 0 / 3 | open PR hold | `part-03.json` |
| `fix/222-dns-label-syntax-20261016` `43246acd6dc6` | 0 / 269 | 0 / 0 | ancestral; hold for tag | `part-03.json` |
| `fix/222-reject-single-label-public-source-hosts-20261017` `3327845f303d` | 0 / 192 | 0 / 0 | ancestral; hold for tag | `part-03.json` |
| `fix/247-nested-symlink-clean-merge-20261013` `368083577709` | 3 / 671 | 0 / 3 | requires content/source review | `part-04.json` |
| `fix/277-direct-retire-frozen-main-20261017` `f09e3310a9f5` | 1 / 0 | 0 / 2 | open PR hold | `part-04.json` |
| `fix/277-retirement-frozen-main-and-repo-validation-20261016` `9a965eeb822b` | 0 / 176 | 0 / 0 | ancestral; hold for tag | `part-04.json` |
| `fix/279-branch-tip-recheck-20261016` `85f76b0a5a6f` | 0 / 269 | 0 / 0 | ancestral; hold for tag | `part-04.json` |
| `integration/five-fix-pr-ci-rehearsal-20261016` `9b9e781b8030` | 3 / 284 | 5 / 17 | requires content/source review | `part-04.json` |
| `integration/five-pr-no-loss-20261016` `82e116e288a9` | 3 / 294 | 26 / 38 | requires content/source review | `part-04.json` |
| `quality/canonical-artifact-ci-20261013` `fd119035a627` | 8 / 713 | 2 / 8 | requires content/source review | `part-04.json` |
| `quality/extend-canonical-data-integrity-csv-20261013` `aa6c3e68fdac` | 4 / 711 | 0 / 4 | requires content/source review | `part-05.json` |
| `quality/244-premerge-artifact-gate` `bcad1eaff617` | 11 / 740 | 0 / 6 | requires content/source review | `part-05.json` |
| `research/independent-page-qa-2026-10-12` `190327b6e575` | 8 / 790 | 0 / 8 | requires content/source review | `part-05.json` |
| `research/issue6-trending-overlap-audit-20261012` `cc37e2014dd0` | 16 / 764 | 1 / 4 | requires content/source review | `part-05.json` |
| `research/issue11-evidence-registry-20261012` `bb87be18c105` | 4 / 764 | 0 / 4 | requires content/source review | `part-05.json` |
| `research/issue22-package-trust-gate-20261012` `d4619a9a1903` | 4 / 764 | 0 / 4 | requires content/source review | `part-05.json` |
| `research/issue-6-coverage-chronological-proxy-20261014` `07b83034d440` | 0 / 231 | 0 / 0 | ancestral; hold for tag | `part-05.json` |
| `research/issue-6-rank-drift-oct2026` `387284269095` | 3 / 764 | 0 / 3 | requires content/source review | `part-06.json` |
| `research/issue-7-literature-ledger-oct2026` `4172d37e7741` | 15 / 750 | 0 / 3 | requires content/source review | `part-06.json` |
| `research/issue-7-literature-source-screen-20261016` `fcd28b373073` | 0 / 271 | 0 / 0 | ancestral; hold for tag | `part-06.json` |
| `research/issue-15-registry-cohort-pilot-20261014` `1f02a5c58fc8` | 0 / 248 | 0 / 0 | ancestral; hold for tag | `part-06.json` |
| `research/issue-22-supply-chain-gate-oct2026` `9e0ea7654def` | 24 / 764 | 0 / 3 | requires content/source review | `part-06.json` |
| `research/issue-100-github-changelog-ledger-20261016` `4ffbb5c953cf` | 4 / 297 | 0 / 3 | requires content/source review | `part-06.json` |
| `research/issue-223-hiring-blind-agreement` `397f76044c62` | 0 / 260 | 0 / 0 | ancestral; hold for tag | `part-06.json` |
| `research/ten-issue-evidence-gates-20261017` `1e656cfcbceb` | 0 / 284 | 0 / 0 | ancestral; hold for tag | `part-07.json` |
| `research/trending-independent-page-qa-issue2` `e129d5ac16ca` | 17 / 791 | 0 / 11 | requires content/source review | `part-07.json` |
| `research/24-maintainer-feasibility-report-20261017` `132fa159baae` | 9 / 0 | 0 / 8 | open PR hold | `part-07.json` |

## Unresolved source and behavior review queue

Among 25 unreviewed non-PR branch tips, exact file differences do not prove a change is novel: file content can evolve, be moved, or have equivalent negative tests implemented under another name. The machine-readable [disposition index](../../ops/branch-retirement/review-only-2026-10-17/disposition-index.json) names the source branch SHA, per-branch changed-file counts, exact same-path identities and paths not found at the pinned main path or any same-blob alternate path. Absence of a same-blob match does not imply that the canonical implementation lacks functionality. Preserve older closed-unmerged PRs, post-merge commits and historical source citations.

Known collision families and verification path: Meta #191/#228, Amazon #192/#229, Replit #196/#212/#230, Qodo #198/#213/#232/#271, Tabnine #199/#215/#233, Amp #197/#231, Augment #200/#234, Factory #201/#236, Cline #202/#237, Zed #203/#238. Earlier batch-2 publisher narratives and vendor source leads require source URL/date/event-ID, availability/status, negative-result, contradicted-version and rights checks. The main-tree crosswalk and [five-company historical review](./2026-10-14-five-company-prs-review.md) make these candidate records discoverable, **not independently authenticated**. No observed adoption, saved engineer time, reuse or carbon impact follows from publisher sources.

## Executable offline evidence integrity

Run `python scripts/check_branch_no_loss_crosswalk.py --root .` and `python -m unittest tests.test_branch_no_loss_crosswalk -v`. The validator checks the eight preserved parts, duplicate SHA/ref/PR/path and JSON key ambiguity, exact status arithmetic, move/ancestry contradictions, file-blob assertions and that every `deletion_authorized` flag is explicitly false. It has no network or mutation capability. A successful offline check **is not** independent API freshness, source legality, unobserved semantics or tag immutability verification.

## Owner-action blockers inspected

The GitHub connector for this repository can read repository metadata, commit/merge PR code, and publish docs, but has no exposed GitHub API operations to configure repository rulesets, create protected archive Git tags, dispatch retirement jobs or atomically delete remote branch refs. I cannot pretend these admin mutations have happened. Their implementation remains tracked by #248 and #277. The privileged retirement job on main is intentionally unconditionally disabled; do not work around it through CI-on-push or a wildcard cleanup. The branch-count target requires separate verified authorization and readback.

**Practical lesson:** integrate one canonical capability at a time; keep source events in a collision-proof, dated evidence ledger; validate frozen provenance with fail-closed tests; treat branch housekeeping as a reversible operation with exact immutable Git evidence. Ordinary green CI is not an independent science or security approval.
