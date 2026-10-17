# Hiring source URL lexical host correction — issue #222

**Date:** 2026-10-16. **Scope:** an offline, deliberately limited data-format correction for a *proposed* requisition observation study. No employer page was fetched and no human/source rights approval is inferred.

The current `trending_study.hiring_observations._url` parser enforced canonical public HTTPS sources but used `[a-z0-9]+(?:[.-][a-z0-9]+)*` for hostnames. That pattern wrongly rejected ordinary valid DNS labels with interior hyphens, such as `careers.jobs-board.invalid`. Pre-excluding common host syntax could silently bias the proposed approved-employer source frame.

The guard now accepts ASCII DNS labels of up to 63 characters with letters, digits and *interior* hyphens, but refuses empty labels, leading/trailing hyphens and hosts longer than 253 characters. It preserves rejection of localhost, local/internal domains, non-global literal IPs, credentials, unsafe path encodings, redirects/search-misses treated as missing, and unauthorized network access.

Synthetic tests check valid hyphenated hosts, edge-hyphen and overlong labels, and representative internal/private hosts. Acceptance of a host string is **not** DNS resolution, proof of an actual employer, source permission, time-stamped observation, requisition identity, actual closure or a hire. Future network collection must undergo its own allowlist and connection-time DNS/SSRF security review.

**Practical maintainer lesson:** input validation should reject dangerous/ambiguous evidence without excluding ordinary valid source formats that would distort a sampling frame. Record rejected-source counts as missingness, not verified negative outcomes.

## Additional numeric-host hardening (same-day merge preparation)

A follow-up review found that strict `ipaddress.ip_address` parsing does not recognize legacy numeric IPv4 aliases such as `127.1`, decimal integer `2130706433`, octal `0177.0.0.1`, or hexadecimal `0x7f000001`. Some URL/network stacks interpret them as loopback destinations. The offline URL validator now rejects fully numeric/hex/octal dotted host forms as ambiguous before considering them acceptable public-source metadata. Synthetic negative tests cover six examples. This remains a lexical check only: DNS rebinding, redirects, and connection-time network restrictions are not addressed; the instrument performs no network access. Human security review and successful CI on the *new* head are still required.

## Canonical control-character boundary

The review additionally found that the prior URL gate rejected code points below ASCII 33 but not the nonprinting DEL character (ASCII 127). The offline validator now rejects DEL throughout a candidate source URL; a synthetic test covers both a trailing and embedded DEL path byte. This is deterministic lexical hardening only, not approval to fetch the supplied URL or a substitute for transport-level origin checks.

## 2026-10-17 validation traceback data minimization

The standalone proposed hiring-observation instrument previously translated
`IntakeError` and URL parser `ValueError` *inside* exception handlers using
`raise HiringObservationError(...) from exc`. A malformed timestamp parsed by
`datetime.fromisoformat`, or a rejected query parser field, can persist in the
chained exception traceback even if the top-level error message is safe.
The instrument now raises stable public `HiringObservationError` messages
**after** the underlying exception handler has exited. New synthetic tests
inspect complete formatted tracebacks, causes and contexts for private marker
strings. No real employer or participant data are required.

This prevents the specified **error-chain** disclosure pathway only; input
may still be held in memory, explicitly logged by a caller, or deliberately
written in a valid operator-controlled result. No automatic collection or
permission to observe people is introduced.

**Maintainer lesson:** audit nested exception causes, not just the final
CLI error text, when research tooling may process sensitive identifiers.

## 2026-10-17 single-label intranet host exclusion

Follow-up engineering inspection found that `_url()` still considered
`https://build-server/jobs/J1` and `https://intranet/jobs/J1` eligible
public-source URL strings despite prohibiting localhost and local suffixes.
Undotted hostnames can resolve via split-horizon, internal DNS or search
domains; a single label is not a defensible public employer origin for the
proposed study. The offline structural gate now requires at least two
syntactically valid DNS labels, while preserving previously accepted ordinary
and interior-hyphenated public hostname spellings.

A synthetic regression covers single-label rejection directly and through
the declared source index, plus valid multi-label controls. The rule neither
resolves DNS nor fetches a source. It does **not** prove that a multi-label
host is public, owned by an employer, safe to connect to, authorized for
research, or historically observed. All independent source, methods,
consent and longitudinal review requirements remain open.

**Practical lesson:** consistency between validators matters: requiring
the public HTTPS scheme is insufficient if a source validator still admits
intranet-only hostnames through otherwise valid DNS-label syntax.
