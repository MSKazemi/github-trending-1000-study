# Verified merged-branch retirement — 2026-10-13

**State at initial review:** 123 branches, 39 open draft PRs, 65 merged PRs; 60 exact head-to-merged-PR branch matches are eligible for *independent revalidation*. The branch list and draft status are time-bound observations, not research findings.

## Strict no-loss retirement

The [committed allowlist](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json) pins **each of the 60 branches** to a GitHub PR number, exact last-reviewed head SHA and merged commit SHA. It is not a wildcard or retrospective inference from a branch name. The source main SHA for this inventory is `6339775d73886b24f746139cdf55a34384f88c33`.

The [offline standard-library retirement implementation](../scripts/retire_merged_branches.py) and [negative tests](../tests/test_retire_merged_branches.py) fail closed unless each GitHub branch remains unprotected and unchanged, the PR is actually merged to `main`, and **no open PR** references the branch. Before removing the branch ref, a recovery tag `refs/tags/branch-archive/2026-10-13/<original-branch-name>` must exist and point to the exact original commit. The script verifies this recovery ref and rechecks the branch and open PR state immediately before deleting. Existing tags with different SHAs block deletion. Partial failures remain logged and do **not** authorize further deletions outside the plan. No study dataset or source document is rewritten.

The original integration ([PR #275](https://github.com/MSKazemi/github-trending-1000-study/pull/275)) introduced a **push-triggered one-time cleanup**; that historical run must be audited independently, not presumed successful or race-free. The revised [GitHub Actions workflow](../.github/workflows/retire-verified-branches.yml) is **manual-dispatch only**: `audit` (default, read-only `contents: read`) checks live GitHub state; `retire` requires the exact confirmation `RETIRE_VERIFIED_MERGED_BRANCHES` and grants scoped `contents: write`. Neither normal pushes nor merging a PR may automatically retire a branch. The destructive CLI also requires `--confirm RETIRE_VERIFIED_MERGED_BRANCHES`. **An additional fail-closed deployment gate** requires an administrator to set the repository Actions variable `BRANCH_RETIREMENT_APPROVED` to the exact string `true`; when unset (the default), the write-capable job is skipped even if someone supplies the confirmation phrase. Before setting the variable, an actual qualified independent reviewer must record the approved PR head, SHA-lease threat model, main/archive-tag rulesets, restore verification, and an authorized maintenance window. Merely setting the variable is not proof those reviews occurred. Keep it unset until all conditions are demonstrated; reset it after a bounded retirement operation.

**Race-safety improvement:** a second GET before GitHub REST DELETE does **not** prevent another contributor pushing between those calls. Instead, the revised script uses an authenticated `git push --force-with-lease=refs/heads/<branch>:<expected_sha> ... :refs/heads/<branch>` for Git's server-side atomic expected-SHA comparison. A concurrent update or restricted deletion rejects the push; the script never retries with a new SHA or force-removes the altered head. It verifies the branch has disappeared after a successful lease. Immediately before the lease it also rechecks the exact archive tag SHA and open-PR count; if a tag is deleted/repointed or a PR appears during preflight, the operation fails without deleting the branch. An open PR can still appear after the final PR query without changing the branch SHA; this is not an atomic GitHub PR/ref transaction. Operators must pause creation of new PRs against the selected heads during the explicitly approved retirement window, and must enforce recovery-tag protection separately. Access tokens are sent through an ephemeral Git configuration environment variable, never embedded in the remote URL or command line. 

A current `main` ancestry check requires each verified PR merge commit to be reachable from `main`. Absent branches are treated as successfully retired **only** if their original SHA is still recoverable through the exact archive tag. A list of 100 open PR results is treated as incomplete and blocks destructive action, rather than assuming there are no other referencing PRs. Archive-tag governance still requires repository administrator rules.

**Recovery:** The original code/commit is reachable via its archival tag, original merged PR and GitHub history. A branch can be recreated from the tag if required. A squash merge does not make pre-squash history an ancestor of `main`; archiving the original source SHA protects that history rather than assuming squash preservation alone is enough. Tags should not be deleted without a separate recovery/retention decision.

## Exclusions and safety boundaries

- **39 open draft PR branches:** retain; source/claim review and overlapping company reports are incomplete. Do not bulk-merge or delete them.
- **5 branches advanced since their PR merged:** quarantine for diff and provenance review; an old green check does not attest newer commits.
- **18 other branches without an open or currently merged PR:** investigate individually, including 17 closed-unmerged PR branches and any unmatched branch. Do not infer supersession from a title alone.
- **`main`** is never eligible. Protected branches, mismatched head SHA, current open PRs, insufficient token permissions or unverified archival refs fail closed.

Remaining branches after full success: approximately **63**, including draft and unresolved research branches. The strategic target is at most 5–10 focused **active** development branches at a time once open company intelligence drafts have genuine source verification and are combined into coherent evidence ledgers. Fewer branches is a maintainability goal, **not** evidence of improved software usefulness or lower electricity use.

## Next branch consolidation phase

1. Group overlapping company screens into canonical per-company evidence registers and one or two review PRs. Preserve every distinct source lead and its provenance; do not treat vendor statements as independent measurements.
2. Compare post-merge changed branch heads to original merged PR heads; cherry-pick unique, tested improvements into a focused PR or archive those commits with an explicit review record before pruning.
3. For closed-unmerged alternatives, retain meaningful security/measurement tests and source references in canonical modules. Use the original PR discussion as a supersession crosswalk.
4. Enable branch protection and required checks/review in GitHub repository settings; workflow policies are not an enforced human-approval substitute.
5. Avoid automatically opening one branch per company or hypothesis without a real reviewer and an acceptance plan. Track future research leads as issues or immutable data entries until implementation is warranted.

**Scientific caution:** This is repository housekeeping. It does not establish GitHub Trending collection permission, the 1,000-project cohort, external human task acceptance, verified adoption or carbon savings.


## Read-only audit and controlled recovery

A live `audit` run also detects an archive tag that already points at a *different* commit and reports `blocked_archive_tag_conflict` without modifying any refs. A missing tag before first approved retirement is expected; it is created and verified only in the separately authorized `retire` phase. This does not replace independent source/method review or administrator protection of recovery tags.

1. Review the [no-loss branch allowlist](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json), current base/head SHAs, and full original PR discussions. Run GitHub Actions **Retire verified merged branches** on `main` in `audit` mode. The audit does no writes; treat any blocked result as a reason to investigate, not authorization to edit expected SHAs.
2. Before any separately authorized `retire` execution, confirm the 2026-10-13 original cleanup run has fully finished, original archive tags exist and remain reachable, no active author is writing to target branches, and tag-protection/branch-protection requirements have been reviewed. Do not rerun an older unreviewed workflow implementation.
3. If approved, dispatch `retire` manually with exact confirmation. Check the resulting GitHub Actions log, statuses, original SHA-to-tag mapping, and the complete post-run branch list. A failed lease means **retain and reclassify**, not bypass.
4. Preserve open Draft PRs and closed-unmerged or changed-after-merge heads until source-level evidence, distinct tests, protocol limits, and independent approvals are reconciled. GitHub branch cleanup is an engineering operation, not validated scientific collection or sustainable-computing evidence.

## PR #284 safety-hold provenance retained during reconciliation

The following historical section records the **protective state of `main` introduced in PR #284 on 2026-10-14**. PR #280 proposes to replace the intentionally failing read-only hold with a **manual read-only audit and a separate SHA-leased retire job** only after qualified independent security review and admin ruleset enforcement. If PR #280 is eventually approved and merged, interpret the retained section as an audit record, not as a claim the intentionally failing hold remains active.

## Temporary destructive-workflow safety hold — 2026-10-14

**Control change, not a scientific result.** On 2026-10-14 the default branch still exposed the older retirement workflow with a `push` trigger and job-wide `contents: write`. That version deletes GitHub branch refs via REST after a separate read, leaving a time-of-check/time-of-use race. The original [2026-10-13 cleanup run](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38463086727) preserved and retired 59 exact heads and blocked the 60th changed head; those recovery tags are **historical** and are not being changed by this safety hold.

Until the SHA-leased manual-only replacement in [PR #280](https://github.com/MSKazemi/github-trending-1000-study/pull/280) completes **independent qualified security/administrative review**, this workflow is intentionally **manual-only, read-only, and fails with an explicit safety-hold error**. It has no branch-retirement API call, Git credential, ref mutation, `contents: write`, or automatic event trigger. A new small offline regression rejects any future automatic retirement workflow event, and requires explicit confirmation if an execution command is introduced.

**Re-enablement gates:** separately review the exact PR head and full integration diff, verify passing Python 3.10/3.12/3.13/3.14 and research-artifacts CI, require SHA-lease deletion and a confirmed original-SHA archive tag, arrange an independent security review and enforce `main` plus recovery-tag rulesets. Only then replace this hold with a manual, read-only `audit` and separately confirmed `retire` mode. Do not rerun the old 60-item allowlist merely to reach 60/60; its altered branch must remain held pending provenance checks. The recorded October 14 snapshot was 69 refs and 30 open PRs (29 draft), and may change concurrently.

**Practical lesson:** stop a dangerous automatic workflow first, then review and deploy its safe replacement. Passing synthetic CI and fewer branches do not demonstrate human review, valid study sources, software reuse, or environmental savings.

## 2026-10-14 integration security gate: read-only path only

The upgraded `git push --force-with-lease` method and its adversarial tests are integrated **as dormant code**. The workflow can be dispatched in `audit` mode with `contents: read`, but the `retire` job has an explicit unconditional `false && ...` job condition. This condition is a deliberate hard stop: **even an administrator setting `BRANCH_RETIREMENT_APPROVED=true` and entering the confirmation cannot trigger branch deletion using this workflow**. The privileged job is not approved or executable at this stage.

Enabling the job requires **another focused PR** that removes the literal `false`, with fresh exact-head tests, genuine qualified independent security review, administrator-enforced `main` branch rules and protected immutable recovery tags. A fresh SHA-pinned allowed-list and independent preflight must then be reviewed separately. No current GitHub interface used in this conversation provides those administrator protections or proof of independent approval. Never reinterpret this engineering merge as permission to retire the six changed branches, 27 closed-unmerged branches, 13 open PRs or the 23 unchanged merged-head candidates in [the October 14 snapshot](BRANCH_RECONCILIATION_2026_10_14.md).

**Scientific boundary:** these security controls and branch counts say nothing about whether AI coding increased independently verified downstream software reuse or reduced lifecycle kWh/CO2e.

## 2026-10-14 operator feedback: explicit failure, never silent skip

With the privileged `retire` job structurally disabled (`false &&`), a manual workflow dispatch selecting `retire` now runs a separate **read-only rejection job** that emits an explicit GitHub Actions error and exits nonzero. Otherwise GitHub could show an all-jobs-skipped result that an operator might mistake for completed cleanup. The `audit` input still runs only read-only live checks. No one can turn on deletion merely by setting a repository variable or entering the confirmation; enabling remains a separate PR with independent security review, enforced branch and archive-tag protections, and a new exact-head recovery/retirement plan. Synthetic CI demonstrates only workflow structure, not that administrators have configured those protections or that source archives are independently verified.

## Dormant credential transport: disable inherited diagnostics

Before passing the ephemeral Authorization header to Git, the dormant deletion
implementation removes inherited `GIT_TRACE*` selectors and `GIT_CURL_VERBOSE`,
and explicitly disables normal, curl and Trace2 outputs, including trace targets
configured in Git settings. Otherwise Trace2 environment logging could write the
credential header to a file even with subprocess stdout/stderr captured. An
offline regression uses a synthetic credential and the real Git `version`
command to check this boundary without a network request or ref mutation.
This hardening leaves the unconditional workflow retirement hold in place and
does not constitute independent security review or retirement authorization.


## 2026-10-15 privileged Git transport isolation follow-up (proposed PR #294)

The dormant SHA-leased deletion transport is additionally hardened on PR #294: discard inherited `GIT_CONFIG_*` and tracing environment, suppress system/global configuration, disable Git hooks using `core.hooksPath=os.devnull` at command invocation, and keep the one narrowly scoped ephemeral HTTPS authorization header. A synthetic regression checks these controls even when host configuration tries to override hooks/credentials. No authorized branch deletion or live credential use has occurred. This does **not** grant approval to enable privileged cleanup, establish archive-tag protection, or replace independent security review. Recheck the exact final head and CI after this addition.

## 2026-10-16 issue #277 proposed frozen-main and repository-path hardening

**Status: proposed patch for independent security review, not a deployed/approved retirement.** A code review found that the original validated `source_main_sha` field was **not enforced** during execution: the command could use the live `main` for ancestry checks even after the operator-approved plan's base snapshot became stale. The original repository-name regex also accepted a bare `.` or `..` owner/repository component, potentially making an authenticated REST path or Git remote ambiguous.

This proposed correction rejects dot-segment repository identities both when parsing a plan and when constructing a `GitHubClient`. It fails **before any archive/tag mutation** unless current `main` equals the exact `source_main_sha` pinned in the approved plan, and rechecks it for each retirement candidate and again directly before its leased deletion. The corresponding offline tests simulate stale initial state, a change between initial preflight and candidate validation, and a change after the recovery tag was created; in every case **no branch deletion occurs**.

The original 60-branch allowlist remains intentionally unchanged at main SHA `6339775d73886b24f746139cdf55a34384f88c33`. It **must fail** against the newer observed main SHA rather than silently replacing an approval or treating current metadata as historical evidence. A qualified reviewer must prepare an independently reviewed **new immutable plan** when a future maintenance window is authorized, retaining original tags, recorded SHA histories, negative tests and source decisions. Never relabel stale evidence by merely editing a hash.

These checks narrow a time-of-check/time-of-use window but do **not** create an atomic transaction across GitHub `main`, PR creation and archived refs. The existing exact-SHA Git push lease only protects the **branch being deleted**. Actual server-enforced main and archive-tag rulesets, qualified independent review, an operator maintenance freeze for new PRs, read-only live preflight, and a separately approved manual destructive mode remain mandatory. The workflow's unconditional `false &&` destructive-job guard stays intact. No branches were retired by this patch.

**Practical maintainer lesson:** a frozen SHA field must be an *enforced precondition*, not decorative metadata. Test owner/repo identities with `./` and `../` adversarial cases, reject source-state drift between checks, preserve exact original provenance, and prefer refusing to delete rather than making a cleanup count look complete.

## 2026-10-17 strict privileged cleanup-plan input follow-up

A separate fail-closed review found that the dormant retirement CLI originally
used a **stat-then-unbounded-read** of the operator plan, with Python's permissive
JSON decoding. A replaced plan file, leaf symlink, FIFO, duplicated JSON
property, NaN/Infinity literal or nonintegral `merged_pr` could escape the
reviewed byte/schema preconditions. Plan fields including the frozen main SHA
must not be subject to ambiguous last-key-wins JSON parsing.

The proposed script now opens the plan once with descriptor-level regular-file
checks, nonblocking and no-follow flags where supported, and a **35,000-byte
actual-read bound**. JSON decoding refuses duplicate keys, NaN/Infinity,
floating-point and overlong integer spellings. Parser failures use fixed
messages that do not expose a private plan path or field. The retirement plan,
archived original commits, approval snapshot, and disabled destructive GitHub
Actions job remain unchanged. Adversarial offline tests cover ambiguous keys,
malformed numeric spellings, symlink/directory/oversize files, no GitHub-client
construction on invalid input, and a valid offline dry run.

This script is deliberately executable as `python scripts/retire_merged_branches.py`
(the documented workflow form); direct file execution does not include the
repository root in Python's module import path, so the standalone privileged
boundary implements a small strict decoder instead of depending on an implicit
PYTHONPATH or dynamically importing another module. This is format safety,
**not** plan authorship/signature verification or a full hostile-filesystem
sandbox; directory ancestry, permissions and atomicity of changing GitHub refs
remain separate security problems. New exact-head CI and independent qualified
human security review are required before merge. Absolutely no branch deletion
or privileged execution occurred.

**Practical maintainer lesson:** evaluate the exact bytes used by a privileged
operation, not merely a prior file-size check. Reject duplicate JSON keys
before they can alter an approved source SHA or branch list.

## 2026-10-17 privileged Git environment hardening

The same focused retirement preflight found that dropping only `GIT_CONFIG_*`
and trace variables left dangerous inherited Git controls such as
`GIT_SSL_NO_VERIFY=1`, `GIT_ASKPASS`, and `GIT_EXEC_PATH` intact. With an
ephemeral Authorization header attached to a privileged HTTPS Git process,
these settings could disable TLS verification or invoke untrusted helpers.
The proposed Git subprocess environment now drops **all** inherited `GIT_*`
variables plus `SSH_ASKPASS` / `SSH_ASKPASS_REQUIRE`, and then explicitly
sets only the required safe Git config, trace-disable and noninteractive flags.
A synthetic subprocess inspection injects hostile values and asserts they are
not passed to Git. This is defense in depth and still assumes a trusted runner,
executable path and HTTPS proxy/CA environment. No credential was used on a
real Git remote and the destructive workflow remains disabled. Final-head CI
and independent security review remain required.

## 2026-10-17 authenticated API redirect hard stop

A focused security review of the existing privileged `GitHubClient.request`
found a concrete standard-library risk: Python's default
`urllib.request.HTTPRedirectHandler` can propagate an ordinary
`Authorization` header to a redirected Request, including when a GitHub
API endpoint returns `Location: https://other-host/...`. That would give
an unexpected redirect target access to the bearer token if automatically
followed. A synthetic, no-network redirect regression verifies the risk
boundary without exposing any real credential.

The proposed client now sends the GitHub bearer header as an
**unredirected header** and creates an opener with an explicit redirect
denial handler. Any HTTP 30x response is an error, including same-host
renames; it must trigger operator review rather than automatic token-bearing
retries. No live GitHub API request, archive publication, branch deletion or
privileged retirement took place. This is a defense against automatic
redirect forwarding, **not** proof that a malicious inherited proxy,
runner/CA trust configuration, account permissions, or future network
transport is fully secure. The destructive workflow remains disabled and
independent qualified security review, a new authorized plan and exact-head
CI are still required before merge or future activation.

**Practical maintainer lesson:** an HTTPS URL and correct initial host do
not imply an authenticated HTTP client will stay on that host. For token
requests, check redirect handling and test no-credential-forwarding directly.


## 2026-10-17 live immutable archive-tag verification

**Additional P0 protection for #277:** a successful Git SHA lease alone does not keep the *backup* immutable. The retirement engine previously created and verified a recovery tag without checking whether GitHub's separately administered archive-tag ruleset was actually installed. The engine now reads the complete bounded live repository/inherited ruleset inventory, checks the unique active repository tag ruleset, denies bypass actors and narrowed archive globs, and requires both update and deletion protection for `refs/tags/branch-archive/**/*`. Missing, duplicated, inactive, inherited, incomplete or weakened policy fails closed. These checks run at the start of destructive execution, before each recovery-tag mutation and **again immediately before** the Git SHA-leased branch deletion. A mid-operation policy change blocks deletion after an archive tag is created. Read-only audit mode remains available with no installed rules, and the privileged GitHub Actions retirement job remains disabled.

Synthetic tests cover absent protection, inactive/enforcement-only policy, permissive bypasses, partial archive namespaces, absent update/deletion rules, direct function calls and policy movement between archive publication and deletion. No tag/branch has been created or deleted. **This is a safety precondition, not proof of real server enforcement.** GitHub main/tag rules remain uninstalled at the checked readback; #248 and #277 still require owner/admin application, independent qualified security review, a source-preserving plan and controlled real negative-enforcement tests before any destructive work or issue closure.

**Practical lesson:** for no-loss branch cleanup, secure *both ends* of the transfer: an atomic SHA-leased delete protects the source, but a mutable archive tag undermines recovery. Inspect live tag policy as late as possible, and never equate configuration readback with verified denial of unauthorized operations.

## 2026-10-17 malformed merged-PR metadata must fail closed

The read-only/privileged branch retirement verifier previously assumed that a
merged PR's nested `head.repo` and `base` fields were always objects.
A deleted fork or partially returned API payload can contain `null` there;
the resulting `AttributeError` interrupted the audit rather than producing
a determinate **blocked** row. The verifier now requires complete nested
object shapes and returns `blocked_pr_not_identical_and_merged` before
creating an archive or calling a deletion lease. Offline adversarial tests
cover missing/null/non-object PR and nested repository/base data and confirm
**zero archive writes and zero deletions**.

**Non-negotiable operational hold:** As verified on 2026-10-17,
`main.protected=false` and repository rulesets were empty. The cleanup
workflow's destructive job remains unconditionally disabled; this merge
must not remove that hold. The original 2026-10-13 branch manifest's frozen
`source_main_sha` remains stale and must not be silently refreshed. Actual
cleanup needs enforced immutable archive tags, a new independently reviewed
SHA-pinned plan, a live authorized preflight, and a separately approved manual
execution with readback and recovery. This branch's engineering tests are
**not** security review or authorization to delete any refs.

**Practical lesson:** missing or malformed remote metadata is not evidence
that a destructive condition succeeded. Require complete verified nested
objects before any archive write or SHA-leased mutation.

## 2026-10-17 direct retirement-helper input boundary

A review of the independently callable `retire_one()` helper found that
`execute()` checked the full operator plan schema, but direct callers
could submit an unvalidated branch name, commit digest, merge PR number or
unexpected private sidecar keys before the helper constructed authenticated
GitHub API requests. A previous patch already required a frozen main commit
for direct destructive calls. This additional change **reuses the exact
single-item validator** in both `validate_plan()` and `retire_one()`
for destructive *and read-only* entry points, and enforces repository/client
identity before any network request. The negative regression checks
dot-segment/ref-injection names, malformed digests, noninteger and oversized
PR numbers, extra fields and invalid object types; none may reach `get()`,
tag creation or leased deletion. Original CI fixtures still test successful
offline plan execution.

This prevents one input-validation bypass; it does **not** prove that a
supplied frozen SHA was actually approved by a human, that live GitHub
ref/tag protections are installed, or that a real retirement plan is eligible.
No tag, branch or actual research datum was modified. The privileged workflow
remains disabled, and independent security/admin review is required.

**Maintainer lesson:** a lower-level privileged helper is itself a trust
boundary. Apply the same exact-schema and provenance checks there rather
than assuming every caller used the high-level command.
