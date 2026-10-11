# Verified reference register for AI-era OSS research — 2026-10-11

**Purpose:** starting bibliography, not a systematic-review result. Dates refer to publication or the version available at the stated review date. Research findings must be interpreted only within their sampled population and tasks. Prefer primary academic/official sources; flag vendor/platform sources. No 2027 outcome is claimed.

| Key | Source / link | Class | Relevance and caveat |
|---|---|---|---|
| R01 | [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/), 2025; updated 2026 | platform, descriptive | Large increase in developers, repos/commits/PRs; reflects activity, **not causal impact** or quality. |
| R02 | Forsgren et al. [The SPACE of Developer Productivity](https://doi.org/10.1145/3454122.3454124), ACM Queue 2021 | peer-reviewed framework | Activity alone does not measure productivity: satisfaction, performance, activity, collaboration, efficiency/flow matter. |
| R03 | Becker et al. [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089), 2025 | independent randomized trial / preprint | 16 experienced developers, 246 mature-project tasks; AI allowed condition averaged **19% longer** in this study. **Not** a universal AI speed estimate. |
| R04 | METR [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/), 2026 | independent study update | Late-2025 estimates compromised by developer/task selection, concurrent-agent time tracking. Authors do **not** claim reliable current causal uplift. |
| R05 | DORA/Google [2025 State of AI-assisted Software Development](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) | large observational survey; sponsored research | AI described as an amplifier of organizational capability, not guaranteed efficiency; survey and company-level associations. |
| R06 | DORA [Balancing AI tensions: Moving from AI adoption to effective SDLC use](https://dora.dev/insights/balancing-ai-tensions/), 2026 | organizational research interpretation | More throughput can coexist with more delivery instability, depending on systems and verification practices. |
| R07 | CHAOSS [Starter Project Health](https://www.chaoss.community/kb/metrics-model-starter-project-health/) | community standards/model | Human response, closure ratio, contributor concentration, release practice; bots and differing repo types matter. |
| R08 | Robbes et al. [Agentic Much? Adoption of Coding Agents on GitHub](https://doi.org/10.1145/3822180), ACM TOSEM 2026 | peer-reviewed empirical mining | Large-scale study of *attributable traces* of agent adoption; partial detection; adoption != usefulness. Prefer journal/revised version over early arXiv draft if estimates differ. |
| R09 | Robbes et al. [Agentic Very Much! Adoption of Coding Agent in New GitHub Projects](https://arxiv.org/abs/2606.07448), 2026 | preprint | New projects appear to have greater agent adoption; selection and partial attribution limit generalization. |
| R10 | Li et al. [AIDev: Studying AI Coding Agents on GitHub](https://arxiv.org/abs/2602.09185), 2026 | dataset preprint | Large observed agent-authored PR corpus; PR acceptance is not equivalent to real product usefulness. Evaluate licensing/coverage before reuse. |
| R11 | Pinna et al. [Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance](https://arxiv.org/abs/2602.08915), 2026 | preprint | Task type strongly varies PR acceptance; beware project/task/agent selection, and acceptance ≠ functional correctness. |
| R12 | [Security in the age of AI teammates: An empirical study of agentic pull requests on GitHub](https://doi.org/10.1016/j.infsof.2026.108333), Information and Software Technology, online Sep 2026 | journal pre-proof | Security-related agentic PRs reviewed more cautiously; context/complexity and human scrutiny matter. Samples/keyword filters are not unbiased security rates. |
| R13 | Michels et al. [Vibe Coding: Practice, Performance, Productivity, and Risk — A State-of-the-Art Review](https://arxiv.org/abs/2608.20446), Aug 2026 | preprint narrative review | Synthesizes sometimes inconsistent claims; **not peer-reviewed or fully systematic** at this checkpoint. |
| R14 | GitHub [Repository Traffic REST API](https://docs.github.com/en/rest/metrics/traffic), reviewed Oct 2026 | official API | Traffic/clones/referrers require repository access; not an arbitrary-public-repo metric. |
| R15 | Kalliamvakou et al. [The Promises and Perils of Mining GitHub](https://doi.org/10.1145/2597073.2597074), MSR 2014 | peer-reviewed | Population frames, repository/project distinction, misleading metadata and selection effects. |
| R16 | [GitHub Trending](https://github.com/trending), reviewed Oct 2026 | observed platform UI | Daily/weekly/monthly displayed lists; exact full ranking formula is not published for reliable reconstruction. |

## How to validate and maintain bibliography
1. Before calling this a systematic review, log ACM, IEEE, Scopus/OpenAlex and scholar search queries/dates, inclusion criteria, reviewer decisions and snowballing; follow [RELATED_WORK.md](RELATED_WORK.md).
2. Store DOI/arXiv/official canonical URL, version/date, venue, study type, population, primary outcomes, effect sizes/intervals and limitations. Avoid substituting summaries for the underlying methods.
3. Different versions can disagree: prefer the newest primary final version and document version drift. For R03/R04, retain both because their interpretations **differ**.
4. Vendor/platform descriptions (R01/R05/R06) can establish what was reported, but are not randomized causal evidence.
5. Re-review fast-changing AI-agent claims quarterly through 2027. **Never backdate new findings.**
6. No paper or platform source here supports a single universal numerical threshold that separates useful and useless GitHub repositories.

## Literature gaps this project can target
- Jointly observing Trending exposure, independent user value and subsequent maintenance in the same longitudinal cohort.
- Distinguishing copycat/template activity from verified novel functionality without penalizing honest educational forks.
- Experimental study of AI workflow tradeoffs after reviewers' and future maintainers' costs are counted.
- Project-type-sensitive lessons with falsifiable implementation checklists and a record of *failed* hypotheses.
