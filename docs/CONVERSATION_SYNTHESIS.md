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
