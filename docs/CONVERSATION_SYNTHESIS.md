# Research conversation synthesis and decision history
**Compiled:** 2026-10-11 | **Status:** source-of-truth synthesis of relevant research discussion, **not** a verbatim transcript of every private chat.

## Scope, preservation and privacy
This public file consolidates research objectives, methodological alternatives, explicitly adopted design decisions, limitations and proposed next work from the project discussions on 2026-10-11 and earlier relevant open-source growth planning. It intentionally excludes unrelated personal chats, private correspondence, confidential discussions and any claim that a full conversation export was performed. Human decisions and results should be recorded here as new dated entries, with links to commits/issues and, where appropriate, archival identifiers. Information added later should be appended, not silently backdated.

## 2026-10-11 — Name, aim and first study proposal
- The repository was named `MSKazemi/github-trending-1000-study` to communicate GitHub, Trending, 1,000 sample size and empirical research.
- Research questions: what drives **observed GitHub visibility**, sustained growth, onboarding, community engagement, software engineering and repository sustainability?
- Original proposed dimensions: name/description/topics/SEO, README/install/tutorials, contributor affordances, CI/testing/releases, stars/forks, governance/security, AI-agent instructions, and maintenance.
- Important early caution: **GitHub Trending != top-1,000 by lifetime stars**; the ranking formula is opaque, and merely visiting Trending today cannot reconstruct historical membership.
- Proposed dataset: `>=1,000` **unique repos observed trending**, dated raw captures, page position, filters, SHA-256, stable GitHub IDs when available, provenance and explicit exclusion accounting.

## 2026-10-11 — Scientific methods and design decisions
- **Prospective 12-week recruitment target** across daily/weekly/monthly and chosen language views; separately sourced `~1,000` comparison repos; enrollment followed at 7/14/30/60/90/180 days. The goal of 2,000 total repos is provisional pending pilot power analysis. Recruitment + follow-up exceed 180 calendar days.
- Distinguish **appearance events** from unique repos; first observation != first-ever trending.
- Primary outcome proposal: 30-day **net star change**, plus signed `log1p(S30)-log1p(S0)`; secondary outcomes community response/retention, 90/180-day changes, repeat visibility and engineering maturity.
- Rank and stars do not prove software quality, user adoption or causal benefit. Forks, commits, CI badges, README length and issue counts are misleading without definitions and denominators.
- Matching/control strata: baseline popularity, age, language, type, owner and observation week; imperfect frame and unobserved confounding must be disclosed.
- Methods proposed: missingness/attrition audit, negative-binomial or robust models chosen with diagnostics, survival analysis of first response, multiple-test control, chronological holdout, language/project-type sensitivity checks, Jaccard/Kendall/ranking analysis.
- Metrics not generally obtainable for other maintainers' public repos: traffic views/clones/referrers. Do **not** manufacture these from stars.
- Open issues: sampling-frame validity, source permissions, parser gold set, preregistration/power, longitudinal collectors, ranking audit, qualitative coding, systematic literature review.

## 2026-10-11 — Extension toward usefulness and 2027
- **New research purpose:** distinguish useful software from popular yet low-utility or high-maintenance projects in a rapidly expanding AI-assisted development ecosystem.
- **User-centered goal:** help solo/open-source developers decide **what to build, what to reuse, when to stop**, how to conserve tokens and engineering time, and how to validate usefulness independently of code quantity or stars.
- **Methodological change:** Github-observable metrics alone cannot establish user impact; add opt-in user/task validation and maintainer time/tokens logs. Do not infer AI-authored code from a mere `AGENTS.md`, model name in README or code style.
- **Two linked studies, not one conflated dataset:** (A) observational GitHub Trending/public comparator cohorts, (B) opt-in prospective task-level AI-assisted development evaluation. Cross-study triangulation is required before making strong 2027 advice.
- **Recommendations require an evidence trail**: explicit RQ, prespecified metric, comparison, effect size/uncertainty, validity threats, cost, applicability and a replicable lesson card. Absent results, label *hypothesis*, *design heuristic* or *research question*.
- **2027:** scenario planning with dated checkpoints, not predictions presented as accomplished facts.

## Previous related organic growth constraints carried forward
Prior GitHub dissemination discussions emphasized 0 paid promotion; genuine discoverability through clear onboarding, relevant docs/examples and community participation; no buying/faking/exchanging stars, spam or engagement manipulation. Such practices are **candidate interventions to test**, not proven causal recipes. Keep the research repo transparent about methods; when adapting lessons to third-party project READMEs, avoid promotional language or untested success claims.

## Working project outputs
- [Prospective cohort study](STUDY_DESIGN.md) and [protocol](PROTOCOL.md)
- [Trending black-box audit](TRENDING_ALGORITHM_AUDIT.md)
- [Usefulness and evidence theory](USEFULNESS_FRAMEWORK.md)
- [AI-assisted development substudy](AI_CODING_STUDY_2027.md)
- [Evidence-to-lesson pipeline](EVIDENCE_TO_LESSON_PROTOCOL.md)
- [Developer value playbook](DEVELOPER_DECISION_PLAYBOOK.md)
- [2027 scenarios](FUTURES_2027.md)
- [AI-era references](REFERENCES_AI_2027.md) and [claim ledger](CLAIM_LEDGER.md)

## Decision/change log
| Date | Decision | Status | Why | Follow-up |
|---|---|---|---|---|
| 2026-10-11 | Use 1,000 observed Trending repos | target, not attained | Repeatable public research frame | Validate collection |
| 2026-10-11 | Include similarly sized comparator | draft | Expose selection bias | Freeze sampling protocol |
| 2026-10-11 | Prospective 7–180-day measures | draft | Avoid purely cross-sectional hype | Implement snapshots |
| 2026-10-11 | Add independent *usefulness* track | draft | Stars/commits != impact | Pilot user outcomes |
| 2026-10-11 | Add AI productivity substudy | draft | AI activity != net efficiency | Define task-level protocol |
| 2026-10-11 | Only evidence-graded lessons | accepted methodological rule | Prevent claims unsupported by data | Lesson card + claim ledger |

## How to update
A proposal is **not** a recorded result. For each substantive change add date, exact study phase, rationale, issue/PR link, whether decided before inspecting outcomes, and any divergence from frozen protocol. Raw private conversation archives must **not** be dumped into this public repository by default.


## 2026-10-11 — Full study discussion checkpoint and green mission amendment
All substantive user research prompts **through the green/sustainable coding request** have been recorded verbatim in [research-notes/conversation-checkpoint-2026-10-11.md](../research-notes/conversation-checkpoint-2026-10-11.md). Assistant findings and actions are consolidated with exact document links, not copied as a private raw transcript. The central *normative objective* is now to **help others discover and reuse high-quality existing software instead of unnecessarily generating duplicate code**, and to reduce human effort, token use, electricity and lifecycle maintenance **when evidence shows a true benefit**.

This changes emphasis but does not establish a study result: GitHub Trending is a useful **observable attention sample**, not a trustworthy proxy for software quality, code reuse or green performance. An independent OSS reuse frame and randomized task-level reuse comparison are necessary. Read [green mission](GREEN_REUSE_MISSION_2027.md), [Trending audit](TRENDING_VALIDITY_AUDIT.md), [experiment](REUSE_FIRST_EXPERIMENT.md), [metrics](REUSE_SUSTAINABILITY_METRICS.md) and [source registry](../references/green_reuse_sources_2026.json).

**Proposed plan amendment:** early drafts suggested 12-week recruitment; newer draft proposes 2026-11 to 2027-04 to cover 2027 availability and complete 180-day followups by late 2027. The extension needs frozen preregistration and pilot-based power review **before** confirmatory enrollment; date/period choices are design hypotheses, not existing evidence.


## 2026-10-11 — Critical research gap follow-up
The user asked: "Go head which aspects I did not considered which is important". We audited the implemented and draft documentation and identified 12 P0–P2 omissions/underdeveloped areas, especially independently adjudicated task-code ground truth, full task eligibility (avoid selection of reusable-only tasks), heterogeneous discovery/pool incompleteness, supply-chain trust and true lifecycle break-even. Additional concerns are upstream maintainer burden, comprehension/knowledge transfer, leakage/benchmark gaming, public-interest objectives, ecosystem/version drift, interference and bounded search overhead.

Read [critical gap audit](CRITICAL_RESEARCH_GAPS_2027.md), [gold judging protocol](REUSE_GOLD_STANDARD_2027.md), [trust guidance](SUPPLY_CHAIN_PROVENANCE_2027.md), [life cycle](FULL_LIFECYCLE_BREAK_EVEN_2027.md), [human burden](MAINTAINER_EXTERNALITIES_2027.md), and [scientific governance](SCIENTIFIC_GOVERNANCE_2027.md). These are **protocol designs only**, and do not establish any empirical sustainability outcome.


## 2026-10-11 — Five-year hypothetical academic/CEO/CTO advisory request
The user requested a strategic critique from the perspectives of full professors and executive technical/business leadership, concrete guidelines/aspects to check, possible 2027–2031 developments, and a five-year plan assessing consequences for the study objective. Original question is preserved in [the dated user-prompt checkpoint](../research-notes/conversation-checkpoint-2026-10-11.md). Our proposed answer is a **hypothetical advisory framework, not representation of real reviewers or endorsements**. Core changes: independent falsifiable science, maintainers/security and total ecological cost, adaptive multi-agent versioning, no speculative growth/usage claims, annual decision gates and possible future task-to-component evidence registry only after experimental benefit. New docs: [advisory perspectives](ADVISORY_BOARD_STRATEGY_2027_2031.md), [roadmap](FIVE_YEAR_ROADMAP_2027_2031.md), [scenarios](FUTURE_SCENARIOS_2027_2031.md), [scorecard](LEADERSHIP_SCORECARD_2027_2031.md), [governance](RESEARCH_PROGRAM_GOVERNANCE_2027_2031.md), [inception](INCEPTION_CHECKLIST_2026_2027.md).


## 2026-10-12 — User requested implementation ("Go head")
We inspected the public repo and issue #27, confirmed no completed 1,000-repo cohort, no formal preregistration and no verified live page audit. The existing `parse-trending` conflated processing time with collection provenance and accepted a user-provided observation date, risking invalid longitudinal baselines. The pilot feature branch implements client-recorded capture SHA/UTC manifest, strict `pilot-parse`, documentary `pilot-preflight`, a synthetic regression suite and explicit `not_enrolled`/human-review states. A draft v0.3 consolidates study A/B estimands without claiming the design is officially frozen; all source permission, real sample audit, numeric IDs, power, participant consent and reviewer approval remain pending. Source discussion checkpoint: [2026-10-12 implementation note](../research-notes/conversation-checkpoint-2026-10-12.md). Technical documentation: [pilot SOP](PILOT_CAPTURE_AND_PREFLIGHT.md).


## 2026-10-12 — Second "go head" implementation: independent Trending page audit
The user requested continued hands-on work after PR #40. We selected [issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2) after verifying the repo and existing PRs. Existing code already rejected structurally partial `article.Box-row` pages, but could not identify an off-selector row omitted during layout drift, nor compute actual externally labeled ranked precision/recall. A new offline, write-once `audit-pages` evaluator binds two self-attested complete-page labels to source SHA/UTC, reports rater conflicts and exact TP/FP/FN including page-level parser rejection, with sample QA readiness **never conflated** with source or scientific signoff. Tests simulate 36 rows across all three windows, and are **not** real observations. The current runner couldn't resolve GitHub's live raw page, so actual human page QA remains pending. See [full runbook](INDEPENDENT_PAGE_AUDIT_2026_10_12.md) and [dated conversation checkpoint](../research-notes/conversation-checkpoint-2026-10-12.md).
