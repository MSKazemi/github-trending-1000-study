# GitGuardian #096 — dated primary-source cross-check (2026-10-15)

**Status:** assistant-performed public documentary spot check, **not** an independent non-author human review, site-access permission clearance, longitudinal observation or test of installed product behavior. The [24-event candidate ledger](096-gitguardian.events.csv), [report](096-gitguardian.md) and [30-query screen](096-gitguardian.search-log.md) remain the canonical evidence and must be independently reviewed before promotion.

## Targeted primary sources and correction boundaries

| Candidate ledger record | Direct public source (read 2026-10-15, date granularity only) | Narrowly supported statement | What remains unsupported |
| --- | --- | --- | --- |
| GG096-2026-008 | [GitGuardian self-hosted 2026.7 release, July 24](https://docs.gitguardian.com/releases/self-hosted/2026-07-changelog) | Vendor page identifies v2026.7.0 on 2026-07-24 and explicitly warns that **Developer Endpoint Protection is not functional on self-hosted 2026.7.0**; operators dependent on it should defer that upgrade/contact vendor | No claim this applies to all SaaS releases, all deployments, or current later versions; no independent installation test |
| GG096-2026-016 (overlap group with 015) | [GitGuardian SaaS release archive, September 25](https://docs.gitguardian.com/releases/saas) | Vendor says AI Hooks withhold some tool output from Claude Code/Codex/Vibe models, but **Codex and Vibe still keep raw output in local session files**; it also identifies agent-specific gaps in coverage, including outputs reaching models for other tools | No general protection guarantee, no verified external recall/false-negative rates, and no assurance transcripts have been cleaned retroactively |

Both are **first-party release documents**. They independently cross-check *that the vendor disclosed a limit*, not the actual extent of protection. A direct current-page read on 2026-10-15 is not a preservation of the original July/September response body. Both sources may be mutable. Event dates and initial publication dates must not be silently merged; keep source-date precision.

## Proposed qualified factual/security review

1. Independently reopen both sources and check the specific dated release/version and relevant scope, then check a pinned or archived publication snapshot when rights permit.
2. Examine contrary versions or affected agent types without equating partial output interception to complete secret containment. Record each disagreement/correction as an append-only ledger entry.
3. Review GG096-2026-015 and 016 as **one overlapping capability group**, not two independent efficacy observations. Confirm endpoint-installation and local transcript exclusions before any reuse advice.
4. Only an authorized offline mock-secret protocol may evaluate behavioral effectiveness. Do not use real secrets, customer transcripts, private telemetry or live credential tests.

**Scientific disposition:** this spot check supports selected attributed vendor disclosure claims, not six-month systematic completeness, independently measured security improvement, company-wide roadmaps, actual adoption, participant consent or energy/carbon outcomes. Keep [issue #164](https://github.com/MSKazemi/github-trending-1000-study/issues/164) open pending actual qualified review and traceable final acceptance.

**Practical lesson:** for an agent-enabled repository, include a synthetic-token test for *both provider output and local transcript persistence*, with an explicit bypass/denied-action denominator, before trusting a hook or scanner. Mere vendor support lists are not proof of end-to-end containment.
