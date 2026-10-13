# Branch lifecycle and no-loss consolidation audit — 2026-10-13

**State:** read-only review, **not** authorization to merge drafts or delete refs. Related [issue #276](https://github.com/MSKazemi/github-trending-1000-study/issues/276).

## Live inventory and scope

The GitHub API returned **123 branches** in an initial paginated inventory and **124** after a concurrent branch update. There were **39 open PRs, all Draft** at inspection. A moving repository snapshot means counts are not guaranteed current when this document is read. The default branch was `main`, SHA `6339775d73886b24f746139cdf55a34384f88c33`.

On that SHA the five GitHub Actions checks succeeded: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts`. GitHub branch metadata reported `main.protected=false`, and `/rulesets` returned `[]`. Detailed protection inspection was forbidden to the integration (403). Existing issue #254 records the administrative action required. **CI success is not a human research, security or source approval.**

A sample of more than 60 non-PR branches was compared against `main` with GitHub's ancestry comparator; many were **diverged**, frequently 50–140+ commits behind. A divergent branch is not safe to delete just because its filename already exists on main: squash-merged paths can have disjoint commit history and differing substance.

## Verified ancestor branches (not deleted)

| Branch | At audit: ahead of main | Behind main | Decision |
|---|---:|---:|---|
| `ci/enterprise-pr-qa-gates-issue-240` | 0 | 11 | Manual cleanup candidate after full-SHA recheck |
| `research/issue-18-energy-boundary-oct2026` | 0 | 52 | Manual cleanup candidate after full-SHA recheck |

The connector used for this audit does not expose remote branch deletion. Neither candidate has been deleted.

## Research collisions that must not be overwritten

| Company | Conflicting open PRs | Gate |
|---|---|---|
| Meta | #191 and #228 | Reconcile divergent source/chronology material |
| Amazon / AWS | #192 and #229 | Preserve distinct source evidence |
| Amp Inc. | #197 and #231 | Retain both observed first-pass leads |
| Replit | #212 and #230 | Reconcile source chronology and alternate records |
| Qodo | #213 and #232 | Verify conflicting facts and preserve counterevidence |

Also keep distinct code/methodology proposals under review: package-trust #186 vs #216, adoption measurement #185 vs #210, documentation rubric #183 vs #187. Drafts remain drafts until tests on integrated code, evidence provenance and qualified scientific review are complete. See [prior audit](PR_AUDIT_2026-10-13.md).

## Safe workflow (fail closed)

1. Freeze and record `main` and every branch tip as full SHA. Read **all** paginated branches/open PRs.
2. Compare `main SHA...branch SHA`. Preserve anything with `ahead_by > 0`, any PR head, and any protected ref. Do not interpret zero changed files or equal tree content as proof the branch was historically integrated.
3. For `ahead_by = 0`, confirm there is no open PR and no protected/ref dependency; compare the branch's **current** full SHA again before owner-approved deletion.
4. For diverged/squash-integrated work, compare code, unique historical evidence, citations, tests and negative outcomes; make one reviewed canonical integration PR before closing superseded drafts.
5. No force push, destructive ours/theirs merge or unreviewed conflict resolution. Require successful current integration-tree CI and independent human approvals as required by the project policy.
6. Once main has required branch protections, prune reviewed obsolete refs with exact-SHA lease checks, record the cleanup and verify the new main CI.

**Working target:** main + no more than ~10 concurrent feature branches. This is an operational WIP limit, **not** a quota for eliminating unique history. Keep future ideas as issues rather than simultaneously creating a branch per idea.

## Practical lessons for other repositories

Branch count is a maintainability signal but not a scientific research outcome. Distinguish **git ancestry**, **semantic inclusion**, and **evidence validity**. All three are needed before claiming no-loss consolidation. Prevent parallel AI agents from independently overwriting shared reports: serialize per-file integrations, require provenance, and use stable reviewed interfaces. Green CI tests engineering behaviors, not external source accuracy or environmental impact.
