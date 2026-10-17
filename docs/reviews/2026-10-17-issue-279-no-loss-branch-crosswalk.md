# Issue #279 — pinned no-loss branch crosswalk (2026-10-17)

**Status: engineering inventory complete for a fixed SHA, retirement NOT approved.** This AI-assisted read-only crosswalk is not independent human source, rights, security, scientific or branch-retirement review. No branch or tag has been deleted or moved. No study observations or source claims are validated.

## Fixed scope and reproducibility

- Repository: `MSKazemi/github-trending-1000-study`.
- Comparison base: `main@62254996c69fc8c359650b801b6e4935048c4f21` (snapshot, **not** a living reference).
- Retrieved through the connected GitHub REST and compare/tree APIs on 2026-10-17; the APIs are not an atomic snapshot.
- Original **53 refs including main**, excluding this report's subsequently created audit branch; 52 non-main branches compared against exactly `62254996c69fc8c359650b801b6e4935048c4f21`.
- **Six open PRs**, all drafts (#435–#440), held automatically.
- 18 non-main branch tips are already ancestral to the pinned main (ahead=0); 6 are ahead with no base-behind commits; 28 have diverged history. These groups sum to 52. 6 live PR-head refs are held, regardless of ancestry.
- 183 GitHub compare changed-file entries were indexed across 52 branches, with per-file exact branch/main Git blob SHA and 51 same-path blob matches. Note that even a matching file blob is not proof of semantic or legal source acceptance.
- Independent current GitHub rulesets request returned `[]`, and main branch was `protected=false`. **No administrator enforcement**; #248 and #277 are unresolved.
- These eight disjoint, numbered immutable Git-blob-backed JSON manifests together comprise the complete crosswalk: `ops/branch-retirement/review-only-2026-10-17/part-00.json` (batch 0, source Git blob `24d7b8d97b700c550999a5f5d9f78f6810460bfb`); `ops/branch-retirement/review-only-2026-10-17/part-01.json` (batch 1, source Git blob `11d7b5e2034211a75e361630886300ebfafa119c`); `ops/branch-retirement/review-only-2026-10-17/part-02.json` (batch 2, source Git blob `e9bab8f7300848d2dee105224152b226ee50c5de`); `ops/branch-retirement/review-only-2026-10-17/part-03.json` (batch 3, source Git blob `7a4e2ab708af15f53b96ce03d8a3255d7a6d9b75`); `ops/branch-retirement/review-only-2026-10-17/part-04.json` (batch 4, source Git blob `b9ef905fa1effb83148a1d049969b48466f4a7a7`); `ops/branch-retirement/review-only-2026-10-17/part-05.json` (batch 5, source Git blob `a14f02ad67390b929054946cc1c798f604387a04`); `ops/branch-retirement/review-only-2026-10-17/part-06.json` (batch 6, source Git blob `ef3aeee660176ce305724a63432c53c995419243`); `ops/branch-retirement/review-only-2026-10-17/part-07.json` (batch 7, source Git blob `3339cbe8c3fa3e2666d8836c1d4b6c3f469668dd`).

## Classification contract

Each record retains original branch name, exact observed 40-digit tip, `protected`, linked open PR numbers/heads/draft states, GitHub compare `status/ahead_by/behind_by`, and every changed file's change kind, old path (for renames), exact branch blob, exact pinned-main blob, exact same-path byte identity, and same-byte candidate paths on main. No source-citation validity or negative-test equivalence is implied. The 52 source refs still exist at the audit checkpoint. **No manifest here is an executable deletion allowlist.**

- `hold-open-pr`: active draft (including #435 retirement safety). Never retire.
- `hold-ancestor-await-protected-recovery`: Git history is already included in main as of exact base; still requires a current SHA/live-PR recheck, protected tag of original tip, verified restoration and separately approved leased deletion under #277.
- `hold-diverged-file-and-source-review`: some history is not ancestral to main. Crosswalk is a *triage starting point*, not a finding of semantic no-loss. Preserve original branch, chronology, contradictory/null sources, missing data, distinct citations, tests and results; compare behavior and migrate meaningful unique files through qualified reviewed PR or frozen tagged artifact.

## Research collisions and exceptions

- The historical company collision families (Meta, Amazon, Replit, Qodo, Tabnine, Amp, Augment, Factory, Cline and Zed) are documented in `docs/reviews/2026-10-14-five-company-prs-review.md` and PR #300's versioned source/event crosswalk on main. Earlier overlapping company branches may already be retired and are **outside the 53 live-ref inventory**; preserve historical archive tags and original PR discussion. Publisher leads are candidates, **not independently verified user adoption, real tasks or environmental savings**. Never collapse by company name alone: compare source URL, date, event identity, historical correction, negative/contradictory finding and license at an actual commit.
- The six October 17 draft PR heads are retained unmodified. Current authorship of a source report is not independent review; keep drafts staged until explicit qualified decision.
- Important diverged special cases include post-merge history (`ci/research-json-integrity-247`, `ci/restore-canonical-integrity-gate-20261013`, `research/issue6-trending-overlap-audit-20261012`, `research/issue-7-literature-ledger-oct2026`, `research/issue-22-supply-chain-gate-oct2026`) and closed/unmerged work (`fix/followup-ledger-gate-issue-4`, `audit/pr-merge-gate-log-20261013`). Preserve tests, historic documentation and citation chains before retirement. The included file blobs are not claim adjudication.

## Stop gates for next authorized cleanup

1. Establish real `main` required-check/independent-review protections and separately **immutable archive-tag protection** with a negative enforcement test (#248).
2. Obtain independent qualified security/source review, inspect every held diverged branch's unique *meaning*, migrations, original PR comments and exact source identities; avoid false redundancy from squash merges.
3. Freshly inventory all branches/pages, all PR pages, live full ref SHA, tags, merge ancestry and main; fail closed if *anything* changed. Make a new bounded reviewed **execution** manifest, not a copy of this JSON.
4. Prove that each exact old branch tip has a protected recovery tag and restoration works, then use server-side Git `--force-with-lease` under narrowly authorized manual maintenance window (#277). Never use unguarded REST delete; retain detailed per-ref logs and verify ref absence without rewriting any archive.
5. Recheck remaining open implementation workstreams and gradually enforce a maximum of ten simultaneous **active** implementation branches. Raw historical branch count and the 6 draft heads must not be called scientific results or proof of achieving this policy.

**Practical maintenance lesson:** use content-addressed no-loss ledgers, one canonical PR per capability, source-event identity for research collisions, and protected recovery with fail-closed deletion. Merge engineering and scientific signoff are different activities. 
