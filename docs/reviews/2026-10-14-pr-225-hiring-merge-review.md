# PR #225 — hiring-methods integration and research-validity review (2026-10-14)

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) · **PR:** [#225](https://github.com/MSKazemi/github-trending-1000-study/pull/225) · **Issues:** [#220](https://github.com/MSKazemi/github-trending-1000-study/issues/220)–[#224](https://github.com/MSKazemi/github-trending-1000-study/issues/224).

## Accepted integration scope, NOT accepted scientific findings

Archive the versioned **exploratory lead registers** and **proposed methods** with offline data-integrity regressions. This is *not* an approved hiring census, completed protocol, independently fact-checked job corpus, operational source monitor, validated AI forecast or published empirical study. Keep #220–#224 open for scientific review.

- 18 historical seed leads from five groups and a separate six-lead expansion from NVIDIA and Google. The 24 records are purposively selected **links**, not 24 active or distinct hires.
- The 18-row source audit retains initial seed provenance, changes per-lead access classification without rewriting the seed, and quarantines a **Cursor-branded URL whose body names SpaceXAI** from company inference.
- In the expansion, only one lead was labeled directly accessed in the 2026-10-13 screen; the other five were classified from search-indexed source text. Never promote indexed-only records to confirmed live openings.
- Employer/ATS URL syntax, unfilled publication dates, disjoint requisition identifiers, evidence-class consistency and CSV structure have offline assertions. **None authenticate content or rights.**
- The branch was 279 commits behind `main` at review; all ten original PR paths were absent from `main`. Integrate via a non-destructive merge commit retaining `main` and the PR's full history; verify the post-integration diff is additive.

## Limited source spot-check, 2026-10-14

These checks were performed against public source pages but are **not** independent second-human verification, complete link QA or a retained licensed snapshot.

| Source lead | Limited observed result | Evidence limitation |
|---|---|---|
| [OpenAI Codex AI Systems](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/) | Public role text accessible; describes agent harness, sandboxing and evaluation | No initial posting date or filled-vacancy verification |
| [Anthropic Claude Code performance](https://job-boards.greenhouse.io/anthropic/jobs/5098025008) | Public role text accessible; describes engineering evaluation infrastructure | No publication or hiring-outcome verification |
| [Cursor RL Environments](https://cursor.com/fr/careers/software-engineer-rl-environments) | Cursor URL returned role text explicitly identifying SpaceXAI | **Identity hold preserved**, cannot attribute role to Cursor |
| [NVIDIA Workday JR2025164](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-High-Performance-AI-Engineer--Agentic-AI_JR2025164) | Accessible URL yielded no extractable page body in this read path | Insufficient to establish whether role is active or source complete |
| [Google agentic commerce](https://www.google.com/about/careers/applications/jobs/results/111103097220014790-senior-software-engineer-agentic-commerce-scaling-serving-latency) | Source read failed | Failure is **missing evidence**, not evidence of no listing |

## Engineering release gates

1. Inspect the complete changed-path list and confirm no existing research code, cohort evidence, CI, or unrelated material was deleted.
2. Run the repository's **current** `Tests` workflow on the exact final PR head, including Python 3.10/3.12/3.13/3.14, `research-artifacts`, `compileall`, `unittest` and CLI checks. The earlier [run 1132](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38452510870) passed **only the older Python 3.10/3.12 jobs** and is not sufficient alone.
3. Require a mergeable PR against the then-current `main`, no unresolved review threads, and an expected-head-SHA-protected merge. Record the final run and commit on the PR.
4. Leave scientific review issues open; do not assert that repository-CI success constitutes publisher/source, rights, employment, forecast or independent reviewer verification.

## Required follow-up before scientific use

- Human-authenticate every source and real employer; independently review licenses, ATS terms, retention/snapshot permissions and original publication dates.
- Adjudicate the Cursor/SpaceXAI conflict, record failed/inaccessible official pages and maintain the denominator.
- Approve/preregister eligibility, sampling frame and method/codebook. Actually double-code with independent humans and report agreement/uncertainty; collect prospective UTC observations and product/outcome counterevidence.
- Never treat sampled job advertisements, role counts or a positive GitHub CI run as causal evidence of future products, engineering productivity, CO2 reduction or company headcount.

## Practical lessons for maintainers of other repositories

Version raw observations and correction ledgers separately, make missing values explicit, quarantine inconsistent provenance before aggregation, treat CI as a *data-structure* gate rather than a scientific claim verifier, and sync stale branches with current `main` without erasing either history. Deploy reproducible independent tests of accepted task completion and real software reuse before claiming benefits from developer-agent trends.

**AI-assisted analysis and artifact authoring:** yes. Independent human scientific signoff: **not performed**.
