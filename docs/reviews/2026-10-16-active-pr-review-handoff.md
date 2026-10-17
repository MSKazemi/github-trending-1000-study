# Open-PR review handoff and no-loss merge sequence — 2026-10-16

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study)
**Evidence status:** AI-assisted GitHub read-only inspection plus bounded offline source edits on an existing issue branch. **Not an independent human review, security audit, scientific acceptance, issue closure, or permission to merge.**
**Main at inspection:** `1e656cfcbceb4995467280b796e77e870c6c5f39`.

## Current hard merge gates

- GitHub reported **11 open PRs**, all `mergeable=true`; only #302 is Draft. All 11 submitted-review lists were **empty** and all 11 inline-review-thread lists returned **zero** threads. Thus no independent reviewer has approved any of them at this checkpoint.
- Each preexisting exact-head PR CI run listed below reported success, including the Python 3.10/3.12/3.13/3.14 matrix and `research-artifacts`. Successful synthetic tests do not prove empirical results, rights, safety, or human-methods acceptance.
- Current `main` reported `protected=false`; the repository rulesets endpoint returned `[]`. The connected app cannot fetch detailed branch protection (403), so do not infer server enforcement. Do not fake GitHub review records or use an automated agent as its own independent human reviewer.
- No `.github/CODEOWNERS`, root `CODEOWNERS`, or `docs/CODEOWNERS` file was present on current main. **Reviewer identity is unresolved**; do not invent or assign an unknown person.
- None of these PRs may be considered merge-ready under [the canonical merge gate](../PR_MERGE_QUALITY_GATE_2026_10_13.md) until its specifically qualified independent review is actually recorded. Owner delegation to an AI is authorization to prepare work, not external reviewer consent.

## Review queue: four smaller independent-path engineering changes first

| Order | PR and scope | Inspected exact head | Successful head CI | Reviewer must independently verify |
| --- | --- | --- | --- | --- |
| 1 | [#425](https://github.com/MSKazemi/github-trending-1000-study/pull/425): goldset diagnostic redaction | `69d02f95664fafd74d85b640036bbb7c4074bd86` | [38930766286](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38930766286) | Malformed-schema/duplicate/unknown IDs do not expose sensitive input or CLI filename; fail-closed unrecognized fields and compatibility |
| 2 | [#426](https://github.com/MSKazemi/github-trending-1000-study/pull/426): repeated news URL selectors | `477141bc4c246a203901e3b7514cf990c2052b64` | [38930663841](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38930663841) | Order-sensitive repeated keys avoid false suppression; unique-key reorder still deduplicates; URL-level identity is not event-level factual identity |
| 3 | [#428](https://github.com/MSKazemi/github-trending-1000-study/pull/428): hiring-host lexical safety | `bc6bc58e19060b47196ccc49eff3bf551b2f2c07` | [38964259002](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38964259002) | Valid interior-hyphen labels work; local, edge-hyphen, numeric IPv4 alias and ASCII DEL forms fail; no claim of DNS/redirect/transport SSRF safety |
| 4 | [#429](https://github.com/MSKazemi/github-trending-1000-study/pull/429): package-evidence numeric hosts | `865f0d1b2047e94059a41d29476cc464df3ed226` | [38931239853](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931239853) | Legacy loopback spellings are rejected as ledger URLs while ordinary public domains remain allowed; actual package provenance and network security are still unverified |

These four PRs touch **twelve distinct changed-file paths** (three each, no identical paths) based on GitHub's full changed-filename inventories, but semantic compatibility still requires current-base review. Following any approved merge, recheck the next PR's exact head and merged-base CI before proceeding; the original head CI is not a substitute for testing the combined tree.

## Higher-risk / protocol / evidence PRs

| PR | Exact inspected head | Successful head CI | Additional approval boundary |
| --- | --- | --- | --- |
| [#417](https://github.com/MSKazemi/github-trending-1000-study/pull/417) | `85f76b0a5a6f7fbb8d3fcf8e367c703d32ea4e8a` | [38953185528](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38953185528) | Human review of stale snapshot, ref protection and advisory-only branch prune; zero branch deletion authority |
| [#418](https://github.com/MSKazemi/github-trending-1000-study/pull/418) | `7aa40f766a1c5dbc4356da0306533aafc927d5a6` | [38953056870](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38953056870) | Qualified bibliographic, provenance, source-rights and actual literature-screen protocol review |
| [#293](https://github.com/MSKazemi/github-trending-1000-study/pull/293) | `705273e0a1bec1f0206fdf170a612e7aa21977d8` | [38953393959](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38953393959) | Source/registry rights, package-to-repository identity, independent real task-component rater review |
| [#298](https://github.com/MSKazemi/github-trending-1000-study/pull/298) | `4aa3ccce7e9431369973a41abda6a846c6c5d238` | [38931060295](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931060295) | Hiring source permissions and two genuinely distinct blinded human coders; synthetic fixtures are not empirical agreement |
| [#290](https://github.com/MSKazemi/github-trending-1000-study/pull/290) | `8853ff5da8da63468a11a3b80d9c2cd44ba892d1` | [38931512003](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931512003) | Scientific approval of frame/denominators, temporal leakage, rank proxy, holdout; no prohibited Trending capture |
| [#302](https://github.com/MSKazemi/github-trending-1000-study/pull/302) | `80a2fdd1fd7940d87befc6613d2dc71147505a46` | [38932139921](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38932139921) | **Draft, administrative/security hold**: review ruleset JSON against current main, then authorized live application and read-back / negative enforcement; cannot claim installed protection |
| [#427](https://github.com/MSKazemi/github-trending-1000-study/pull/427) | `de5279eb38acd5dda7287f7159497a93a48b631e` **before this handoff file** | [38953959000](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38953959000) **before this handoff file** | This archival audit PR also needs review; a new commit changes its head and requires fresh CI |

Direct filename intersection among the ten implementation PRs #290/#293/#298/#302/#417/#418/#425/#426/#428/#429 is exactly **`README.md`**, touched by #290 and #298. The current per-PR filename inventories contain 57 entries and 56 distinct file paths. Preserve both nonredundant README additions during sequential integration; filename disjointness cannot establish absence of semantic coupling. No unreviewed research source should be promoted to an authenticated corpus.

## Actionable human-review protocol

1. Identify a **real qualified nonauthor maintainer/security/methods reviewer**, ask their consent, and request a GitHub review on the **specific exact PR head**. The current repo does not identify an eligible reviewer, and the AI cannot invent one.
2. The reviewer reads the full diff, runs independent negative/acceptance checks, checks supply-chain/source/licensing/privacy constraints as applicable, and records an actual review decision via GitHub. Agents may prepare but must never impersonate this role.
3. Re-fetch `main`, each reviewed PR head, all five `pull_request` CI jobs, reviews and conversation resolutions. If a head/base changed, re-test the integrated tree and request renewed review where required.
4. Use a GitHub expected-head SHA guard and approved method to merge **one PR at a time**. Verify `main` tree paths and the separate **push-triggered** five-job run; stop and revert safely if regression evidence appears.
5. Keep associated scientific issues open until real source permissions, independent judgments, actual observations and documented scientific acceptance exist. Never retire a branch based solely on ahead/behind ancestry or synthetic results.

## Practical lessons for my other repositories

- Make human review and exact latest-base CI **GitHub-enforced rules**, not just policy prose: document scope, reviewer eligibility, required job names, nonbypass and failed-negative-case testing.
- Pair permissive parsing tests (legitimate hyphenated hostnames) with adversarial denial tests (numeric loopback aliases, DEL, credentials, path escapes), and state explicitly what syntax checks cannot verify.
- Preserve raw scientific source evidence, false negatives, missingness, repeated-selector ordering and chronological timestamps. A checked box, green CI, one screened source list, or star count does not prove causal or real user benefit.
- Keep one task-sized PR per issue; inspect overlaps and test the **combined main tree** after every accepted merge. Prefer independently accepted user tasks to lines of code or branch/PR volume.
