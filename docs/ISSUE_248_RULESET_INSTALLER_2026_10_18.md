# Issue #248 — guarded, one-command GitHub ruleset administration

**Prepared:** 2026-10-18. **Live readback at preparation:** main `61e60134a17d903e81a9350413924261340578b3`, `protected=false`, repository rulesets `[]`. This is a historical snapshot, not an executable approved SHA. These commands and tests have **not installed any settings**. Official source policy is in [main.json](../ops/rulesets/main.json) and [branch-archive-tags.json](../ops/rulesets/branch-archive-tags.json); the comprehensive [administrator runbook](ISSUE_248_RULESET_ADMIN_REVIEW.md) remains authoritative for independent security approval, exception handling, and real denied-operation verification.

## Purpose and authorization boundary

The previous runbook contains many manual GET/POST commands. A partly completed attempt could mistakenly recreate the archive ruleset, use a moved main SHA, or proceed without looking for inherited policies. The standard-library module `scripts/install_reviewed_rulesets.py` offers **default read-only preflight** and explicit, conservative installation/resume. It is a human-operated admin tool, **not a CI workflow**, scheduled automation, or a route through the ChatGPT GitHub App. The current connected GitHub App has no repository **Administration:write** capability; GitHub rulesets cannot be applied from this chat.

A qualified non-author security/methods reviewer must first approve exact policy contents and the administrator's operating plan. Identify a distinct eligible PR reviewer before installing the strict one-approval main ruleset, or normal merging could deadlock for a solo maintainer. The operator's `--review-ref` is merely a **self-attested pointer**, not independently authenticated approval. The script permanently reports `independent_review_verified=false` and `negative_enforcement_tests_verified=false` until external evidence is separately documented.

## Use on an independently authorized administrator's machine

Use Python 3.10+ from a checkout containing the reviewed pinned policy blobs. Use an environment-provided GitHub token with permitted repository Administration:write or an approved token provisioning mechanism. Never paste or commit the token or store it in GitHub issue comments. The script only reads `GH_TOKEN` or `GITHUB_TOKEN` from its process environment; it never takes a token argument or includes it in console output. It accepts **only** `MSKazemi/github-trending-1000-study`; all HTTP requests target `https://api.github.com`, authenticated redirects are denied, and only `POST /repos/.../rulesets` is allowed.

1. Obtain genuine independent security approval of the exact current policy files and an eligible ongoing reviewer, then **personally inspect GitHub main and the five check results**. Record the exact 40-digit approved **current main commit SHA**, source policy blob SHAs, time, reviewer identity, approval and rollback strategy in an appropriately controlled security/change record. The two required Git policy blob hashes are hard-pinned in the script; any policy change must be re-reviewed and intentionally updated, not silently accepted.
2. Preflight without writes; supply your **independently reviewed actual current main SHA**, not the old example or a value silently grabbed on the command line:

   ```bash
   python -m scripts.install_reviewed_rulesets \
     --repo MSKazemi/github-trending-1000-study \
     --reviewed-main-sha "$RULESET_EXPECTED_MAIN_SHA"
   ```

   This requires authenticated visibility of repository admin permission. It checks exact default branch/commit, five current GitHub Actions checks on that main SHA, complete bounded ruleset inventory including inherited rules, rule JSON and the two pinned Git blobs. It stops on unrelated/duplicate policies, unexpected protection, moved main, incomplete check results, failed CI, compromised required status contexts and malformed responses. `mode=preflight_only` and `write_attempted=false` **do not** assert deployed security.

3. **Only following authorized independent review** run the explicit separate installation, with an authentic change reference already recorded:

   ```bash
   python -m scripts.install_reviewed_rulesets \
     --repo MSKazemi/github-trending-1000-study \
     --reviewed-main-sha "$RULESET_EXPECTED_MAIN_SHA" \
     --apply --review-ref SECURITY-REVIEW-REFERENCE
   ```

   The script creates the immutable archive-tag ruleset **first**, reads it back, checks main SHA/CI and rules again, then creates main rules and performs a second full policy readback. It will not silently overwrite an existing ruleset or retry a potentially successful but interrupted POST. There is no atomic pair-create transaction.

4. If the first POST succeeded and only a verified archive ruleset remains, independently review live state and use `--apply --resume --review-ref YOUR-REAL-APPROVAL-REFERENCE` to explicitly resume. **Never** re-run `--apply` without investigating an ambiguous network/HTTP result; it intentionally refuses an archive-only state unless `--resume` is supplied. A main-only state, inherited policy, unrelated rule, wrong scope, changed main, or unauthorized actor aborts for separate reconciliation. No automatic rollback or Git ref deletion is attempted.

5. After an installed readback (or already-installed no-op), run the independent GET-only `scripts.audit_github_rulesets` from the runbook and conduct controlled *real* GitHub server enforcement tests: reject unreviewed/stale/failing-CI/unresolved-discussion merges, direct/force/delete main refs, and a sacrificial archive-tag mutation; also verify an approved PR positive merge. Record actual IDs, actors, time, exact refs and GitHub server rejection decisions before closing #248. Branch retirement #277 is **still prohibited** without its separately approved fresh no-loss plan, immutable tag tests and source-restoration verification.

## Operator failure cases and non-claims

On partial state, an uncertain POST, or mismatched server response, stop. Read GitHub settings directly before deciding whether to resume. Review/study approval cannot be inferred from the caller's supplied `--review-ref`, CI results, exact-commit checks, policy JSON, or a GitHub `protected=true` flag. Passing synthetic regression tests establishes the program's *simulated* behavior only; it does not prove that GitHub accepted or enforced the rules in production.

**Practical repository lessons:** require independent SHA-pinned preflight; make admin tools GET-only by default; guard the write step behind a deliberate operator decision; never retry an ambiguous POST blindly; support an explicit inspected partial resume; fail closed on inherited/duplicate policies and unknown CI applications; verify both live policy shape **and real server rejections** before calling a repository protected.


## Additional admin-byte integrity hardening (2026-10-18)

The original guarded installation implementation read policy bytes once to check the pinned Git blob digest and **reopened the path** to parse JSON. An attacker or concurrent process could theoretically change those bytes between operations. The revised version uses the repository's existing bounded, descriptor-validated `read_research_input_bytes` once, then hashes and strictly parses *that same byte array*. The shared reader refuses leaf symlinks and nonregular files, checks opened-file size, and never reads beyond 131,073 bytes. New tests reject symlinks, modified-byte payloads and oversized data while confirming the unmodified reviewed payloads load. This is local input-integrity hardening, **not** a substitute for the independent security review of actual GitHub policy installation and enforcement.
