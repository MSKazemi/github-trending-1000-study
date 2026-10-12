# Independent feasibility task-screen card (pilot only)

**Use one copy per hash-selected public issue candidate. Two genuine human reviewers independently fill their own cards, without viewing each other's answers, before inspecting possible reusable components or any agent implementation. This template is not an ethics approval, consent record, frozen task specification or gold label.**

## Source binding
- Original reduced frame path / Git commit:
- `GH-<numeric ID>` candidate ID:
- Canonical public issue link:
- Frame capture completion UTC:
- Reviewer pseudonymous ID and UTC date:
- Reviewer role/independence attestation:
- Issue state as checked; issue changed or closed since capture? (yes/no/unknown):
- Exact upstream repository commit/version baseline checked; evidence URL:
- Safety/privacy/right-to-use assessment reference (no secret/user information):

## Screen before searching existing implementations
| Question | Value (pass/fail/unknown) | Evidence and rationale |
|---|---|---|
| Is this a concrete **bounded software task** with externally observable acceptance? | | |
| Can the problem be specified independently of a suggested patch or already known solution? | | |
| Is there a feasible clean-room, isolated, permitted environment for evaluation? | | |
| Can tests be authored by a party independent of the code-generating agent? | | |
| Is it safe to assess without live secrets, production accounts or harm? | | |
| Is there preexisting patch/solution/PR contamination or public hidden-test leakage risk? | | |
| Do required dependencies/assets/license allow the proposed study and distribution? | | |
| Is the original issue reporter's identity/context unnecessary to the task? | | |
| Is developer consent / ethics approval required before implementation or logs? | | |

- **Screen recommendation:** `eligible_for_independent_spec_drafting` / `excluded_pre_assignment` / `needs_adjudication`.
- **Reason code:** `unsafe` / `underspecified` / `nonreproducible` / `rights` / `scope` / `leakage` / `unknown` / `other` (define in protocol).
- Neutral task requirements draft location (not yet frozen):
- Negative requirements / constraints:
- Proposed independent acceptance author (not model author):
- Reviewer disagreement and C-adjudication reference:
- Expected task difficulty rating and rater uncertainty (exploratory only):

## After task spec/acceptance freeze and methods approval — separate evidence
- Frozen task/spec and acceptance SHA-256, UTC, approver:
- Model/agent execution allowed? Permissions, environment, version constraints:
- Independently sourced candidate pools (at least two channels), query/time/version details:
- **Reuse opportunity:** unknown / adjudicated viable / adjudicated not viable (never guess at intake).
- Verified component's exact identity, release-time availability, license and integrity:
- Independent functional, security and maintenance checks; disagreement:
- Consented participant, preregistered assignment, safety stop, real human-time accounting:
- Outcome and follow-up measured later; separate from this pre-search card:

**Never backfill approvals, ask agents to write their own gold tests, or exclude tasks because no reusable library was found. Do not create unsolicited PRs or contact maintainers to meet a sampling quota.**
