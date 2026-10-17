# Issue #279 — selective no-loss archival integration of two divergent branches

**Read-only checkpoint:** 2026-10-18 (Europe/Rome). The reviewed current `main` was `61e60134a17d903e81a9350413924261340578b3` (`main.protected=false`); the paginated branch listing returned **70** references and **three open draft PRs** (#460, #465, #466). This is a moving, **non-atomic** snapshot; it is not a current deletion allowlist and it does not classify all 70 branch histories as safe to retire.

## Material preserved without changing canonical code

We compared the original Git trees at `38728426909558fda5fcab618ea044eef48c7b8f` and `d4619a9a1903ff53efc5fc89d14e54b43b9ea88d` with the pinned main tree. Their seven source paths were **absent** from the current main working tree, but absence of the same path does not establish scientifically novel or superior functionality. Exact raw Git blobs (documents, code, tests and synthetic fixture) have been crosswalked to `research-notes/branch-draft-archive/2026-10-18-two-research-prototypes/README.md` and verified via `tests/test_historical_research_drafts_archive.py`. The proposed merge commit retains both historic branch commits as additional Git parents; no historical source row or canonical module is overwritten, and no raw fixture is promoted into active research evidence.

**Intentionally unresolved:** independent methods/security/source review of old prototypes versus canonical `trending_study.trending_overlap`, ranking proxy and package-review tools; verified protected archive restoration; mutable main; current branch-tip/PR-membership recheck immediately prior to any actual retirement. The scripts archived here are not executable installations and have not been scientifically validated.

**Decision:** preserve in main as a passive exact-byte archive, keep original research branches, do **not delete or declare semantic merger completion**, and keep #279/#277/#248 and the real-data issues #6/#22 open for external gates.

**Practical lesson for maintainers:** when agents produce parallel alternative implementations, archive unique original bits with a stable crosswalk and only select a canonical implementation after independent acceptance testing. Merging every history with automatic 'theirs' resolution risks reinstating obsolete security code.
