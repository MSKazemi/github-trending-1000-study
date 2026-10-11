# Build useful software without wasting your time or AI tokens

**Purpose:** a free/organic decision protocol for a solo developer, small research team or OSS maintainer. A practical **heuristic**, not a scientific finding of this study. Evaluate projects against the best existing alternative before optimizing GitHub growth.

## Step 0 — Define the real target outcome
Complete one sentence: **For [specified user], when [situation], this helps them [job], measured by [externally checkable outcome] compared with [baseline].** Avoid 'I want to build an AI tool' as the problem definition. Declare whether the project is a deployed tool, reusable library, research artifact, community reference or educational project; usefulness differs by archetype.

## Step 1 — Discovery before code
- List 3–5 actual alternatives and the exact gap (cost, latency, reliability, compatibility, workflows, UX, privacy, portability, policy constraints). Compare with adopting an existing project, extending it, writing a tutorial or doing nothing.
- Ask a few potential users to demonstrate a current workflow and its failure; ask what they actually did last time rather than 'would you use?' Record recruitment bias. A tiny interview sample is **directional**, not statistical validation.
- Identify failure/safety modes, maintainers and dependency risk. Stop or narrow if the differentiator cannot be articulated.

## Step 2 — Set a bounded validation budget
Before agent coding, define **time box, token budget where known, acceptance test, external user proof and stopping criterion**. Suggested 3-pass structure:
- **Discovery pass:** a short fixed allotment (e.g. 2 hours) for alternatives and user tasks; reduce scope or stop without a meaningful gap.
- **Thin-slice pass:** one reproducible end-to-end user task with a test and a clean-install path; do not build dashboards/auth/advanced architecture unless the slice requires them.
- **Independent check:** somebody who did not build it attempts the task without coaching; capture verified success and specific friction. If the same blocker repeats, fix it before adding features.

The example durations are **user-configurable defaults, not universal scientifically determined thresholds**. A safety-critical task demands a larger validation budget.

## Step 3 — Choose a build strategy by evidence, not excitement
| Option | Favor when | Avoid when |
|---|---|---|
| Reuse a maintained existing tool | solves the job at low setup/maintenance cost | genuine gap remains and must be custom |
| Contribute extension to established OSS | a bounded unmet feature integrates cleanly | governance/licensing/security don't fit |
| Write docs/example/benchmark | confusion rather than capability is main obstacle | real capability is missing |
| Build a small new tool | no acceptable alternative and acceptance task is concrete | feature list is broad and user need unverified |
| Research prototype | a falsifiable research question + replication plan exists | claimed production value without users/validation |
| Full product/platform | independently evidenced recurring workflow demand | maintenance and support cannot be sustained |

## Step 4 — Explicit AI-agent work contract
A Claude Code/Codex agent should be asked to:
1. Read `AGENTS.md`, scope, existing code and acceptance criteria.
2. Search and compare **existing reusable components** before writing new code.
3. Propose smallest change, tests and risks; get approval for high-impact actions.
4. Implement a bounded task with pinned dependencies and no new feature creep.
5. Run tests, security/privacy checks and a clean-install or real task reproduction.
6. Show **exact evidence** of correctness and changed docs; state what was not tested.
7. Log human time, agent wait, review/rework, input/output tokens if observable, and follow-up defects. No synthetic 'productivity gains'.

Prompt:
> Implement exactly one user-validated task. First audit reuse vs new code. Write acceptance tests before the implementation, keep the patch small, and make every claim reproducible. Do not add frameworks, agents, dashboards or abstractions without a measured requirement. Stop and ask for direction if the test or evidence is insufficient. Update docs, report tests and the full effort log.

## Step 5 — First external validation, not first stars
Before promotion verify a clean install, one meaningful task run, limitations/security policy, recognizable problem/solution in README, example and support path. Ask a real non-maintainer to attempt the task. Record how many **eligible people attempted** and succeeded; testimonials alone are lower-evidence.

For organic dissemination, use relevant communities respectfully, useful tutorials and a demonstrably working release. No paid campaigns, star exchanges, bought traffic, spam or hollow PRs.

## Step 6 — Decide continue / pivot / archive
- **Continue** when a priority problem exists, tests pass, independent usage or research replication is increasing, and benefits exceed expected lifecycle cost.
- **Pivot** when the problem is real but the solution is hard to understand, adopt or maintain; target the biggest observed friction first.
- **Pause/archive** when no independent need appears after a prespecified appropriate validation cycle, alternatives already solve it, repeat repairs dominate, or safety/maintenance risk exceeds expected value.
- **Publish an honest research artifact** when the software answers an important scientific question but broad adoption is not its goal.

Do not classify an entirely new niche tool as worthless simply because its stars or users are initially zero. Distinguish **unknown** from **proven low value**.

## Weekly portfolio review (15–30 minutes, optional)
For each idea record one user/task outcome, nearest competing alternative, verified tests, independent activity, total human hours, AI token count (or unknown), unresolved regressions, next smallest experiment, and a pause/pivot/continue decision with a date. Do **not** optimize for tokens saved per se if it degrades validated outcomes.

See [cost measurement](TOKEN_TIME_ECONOMICS.md), [usefulness](USEFULNESS_FRAMEWORK.md) and [example assessment](../examples/idea_card.example.json).
