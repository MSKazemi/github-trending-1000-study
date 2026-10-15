# Tailscale #099 — dated primary-source contradiction and deployment gate (2026-10-15)

**Scope:** Assistant-performed read-only spot check for [issue #167](https://github.com/MSKazemi/github-trending-1000-study/issues/167) and [26-event ledger](099-tailscale.events.csv). This is **not** independent human factual/security approval, an incident reproduction, a validated zero-trust deployment or an authorized agent data-collection run.

## Three high-value checks

| Primary source | Source-bound observation | Correction / unresolved risk |
| --- | --- | --- |
| [Changelog, Aug 25, 2026](https://tailscale.com/changelog) and [Aperture GA article, Aug 26, 2026](https://tailscale.com/blog/aperture-ga) | Changelog lists Aperture GA on **Aug 25**; public article is dated **Aug 26**. Both describe the same GA family, with gateway/model controls, logging and MCP integrations. | Preserve both dates in separate **publication/source vs underlying event** fields, never count two GA deployments. GA is company availability, not proof of blocked unauthorized model/tool calls. |
| [TS-2026-002 advisory, May 13, 2026](https://tailscale.com/security-bulletins) | The company describes an ACL-capability bypass in an **explicitly enabled web interface** and identifies **1.98.0 or newer** as fixed. | Scope affected environments to the interface/access preconditions; do **not** say every Tailscale client or ordinary tailnet was exploitable, and do not assume vulnerability absence after this fix. |
| [Tailscale Hugging Face postmortem, July 31, 2026](https://tailscale.com/blog/hugging-face-intrusion) | Tailscale's own account says a stolen credential was used after a sandbox escape/production access; it says no vulnerability in the Tailscale product was found or exploited. | The incident illustrates **credential and enrollment controls**, not proof the VPN caused the escape or that adopting Tailscale prevents lateral movement. Treat Hugging Face's timeline and Tailscale's response as the **same incident family**, not independent demonstrations. |

The links above are provider-authored sources. There is no immutable full-page capture/rights audit, no independently quantified product effectiveness, and no evidence that vendor GA implies safe operation for all plans, regions or versions. The original retrospective ends **October 12**: keep October 13 onward announcements outside the event numerator.

## Falsifiable repository pilot — proposal only

For a predeclared set of 12 synthetic agent network attempts, compare (A) the existing CI identity and least-privilege IAM+network ACL baseline against (B) a pinned Tailscale policy/Aperture gateway. Capture **all** allow/deny outcomes, deliberate credential-reuse and expired-token refusals, user approval events, cold-start/setup time and 30-day maintenance minutes. An independently designed hidden suite must prove **zero unauthorized synthetic reads** in each arm before any production trial. Keep the simpler baseline if equal security is achieved with less lifetime burden. No production credentials, transcripts, user identities or real protected services belong in Git.

**Handoff:** Request separate non-author technical/security and scientific screening of date/version identity, incident interpretation, rights, available policy features and task design before accepting PR #304. **Issue #167 and the draft PR stay open** without that review. This is documentary source checking, not a 1,000-repository study observation.

**Practical lesson:** test *approval, credential lifetime and denials* rather than advertising that a particular VPN or agent gateway is inherently secure.
