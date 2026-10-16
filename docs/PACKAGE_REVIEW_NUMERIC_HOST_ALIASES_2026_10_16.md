# Supply-chain evidence URL numeric-host aliases (issue #22)

**Date:** 2026-10-16. **Scope:** existing offline package/license/security-evidence validator, not a network client or security certification.

## Failure mode and narrow correction

Python's strict `ipaddress.ip_address` rejects noncanonical numeric IPv4 strings, while legacy DNS/libc and URL stacks can interpret `127.1`, `2130706433`, `0x7f000001`, and `0177.0.0.1` as special loopback destinations. The current format-only supply-chain gate already rejects canonical non-global addresses and local/internal hosts; this hardening rejects the obvious all-numeric/hex/octal host alias patterns as **ambiguous evidence hosts** before an evidence URL enters a review packet.

One deterministic synthetic regression checks six alternative numeric aliases and an ordinary named public-domain example. This does **not** perform DNS lookup, establish that a domain actually resolves globally, protect a future HTTP transport against redirects or rebinding, authenticate license/OSV/provenance or approve automatic installation. A future network fetcher must implement connection-time routing/redirect restrictions independently.

**Reuse-first choice:** augment `trending_study.package_review._clean_https_url` rather than building another package gate; no dependencies or live package calls.

## Unfinished scientific and safety gates

#22 requires official pinned registry identity/version/digest/license, genuine advisory/provenance evidence, controlled execution, task-first acceptance and qualified external human security/source review. A `review_ready` result only means that supplied fields are structurally complete, not trustworthy. **Do not close #22 from this regression or green CI alone.**

**Practical maintainer lesson:** a validator should reject confusing host spellings as data-integrity risks, but only an independently vetted network client can enforce actual transport safety.
