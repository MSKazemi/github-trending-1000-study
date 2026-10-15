# Version-specific pre-install security and license screen — issue #22

**Status:** offline **self-declared evidence validator**, 2026-10-12; not a package scanner, legal opinion, signature verifier or installation utility. Partially addresses [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22).

```bash
python -m trending_study.package_review --input REVIEW.json
python -m unittest tests.test_package_review -v
```

The JSON includes `candidate`: `ecosystem`, `package_name`, exact `version`, `registry_url` (HTTPS without embedded secrets), `artifact_sha256` (64-hex when verified or explicit `null` when not yet known), `first_available_at_utc`, `spdx_expression` (null means unknown and cannot be a license pass); `task_frozen_at_utc`; and the exact six `checks` keys: `registry_identity`, `license_compatibility`, `known_advisories`, `release_provenance`, `functional_fit`, `maintenance_suitability`. Each check declares `status: pass|fail|unknown` and a pass has an HTTPS `evidence_url`.

**Decision rules:** any supplied failed gate ⇒ `reject`; unknown ⇒ `defer`; all pass ⇒ `review_ready` **not install approval**. A first-availability timestamp after the frozen user task is rejected to avoid retrospective leakage. All reported checks are self-declared; HTTPS format does **not** authenticate the registry, digest, reviewer, file content, OSV feed, source or release history.

## Required actual security evidence (not implemented by this tool)

1. Resolve exact official registry namespace and publisher; preserve version+artifact digest and issuance date through an authorized source API. Confirm package and source identities separately, including renames and withdrawn versions.
2. Inspect exact distributed artifact vs source commit, signature/attestation provenance where available, SPDX expression against downstream obligations, all licenses and transitive dependency constraints.
3. Query appropriately timed OSV/vendor disclosures; a negative scan is not proof of absence of vulnerabilities. Record advisory date relative to task and evaluation dates, as well as maintenance signals, compatibility, permissions and missingness.
4. Validate functional fit with independently frozen tests in a secret-free isolated environment **only after explicit approval**. Record all failed package searches and avoid typosquat probes that install candidates.
5. Have a qualified independent reviewer verify URLs/digests/owner, license and threat model before reliance. Security tools and OpenSSF scores are evidence layers, not approvals.

**Practical lesson:** for every suggested reusable library in your repositories, insist on exact registry version and verified license/provenance before copying or installing it. Neither GitHub stars nor a 'green' scanner proves safe reuse.

See [supply-chain protocol](SUPPLY_CHAIN_PROVENANCE_2027.md), [reuse-first guide](REUSE_FIRST_PLAYBOOK.md) and [independent gold-set judging](REUSE_GOLD_STANDARD_2027.md).

## 2026-10-13 preinstall fail-closed improvements

The candidate check now rejects moving aliases (`latest`, `main`, `HEAD`, ranges), verifies **PyPI** official `pypi.org` host and exact package name/version in the declared registry URL (other ecosystems still require their own official-identity check), and treats SPDX `NONE`/`NOASSERTION` as **non-granting** for a license pass. It rejects evidence URLs with credentials/fragments, and future frozen task timestamps. A package with first-availability after the historical task cutoff is **rejected**, even if its publication date is future-dated. SHA-256 values and asserted sources remain **unverified strings** until independently fetched/compared.

**Additional fail-closed engineering review (2026-10-13):** Even if an alleged package release is after the frozen task baseline, **all six submitted checks and evidence URLs must still be structurally valid**; temporal rejection does not bypass schema validation or conceal unknowns. The rejection output retains `temporal_availability` and any independently unknown/failing gates. The validator binds only declared **PyPI** package names and versions to the official registry URL: non-PyPI ecosystems are automatically `defer` with `official_registry_identity_binding` in `unknown_checks`, regardless of self-reported six-pass assertions. This is intentional; official binding for npm/Maven/NuGet/etc. requires ecosystem-specific implementations and independent tests. A malformed PyPI name containing path/query controls is rejected. No review-ready result is installation permission; `automatic_install_approved` is always false.

**Checks still required for any real deployment:** resolve exact package URL (purl) and artifact content hash from an authorized registry; verify registry/maintainer identity, signs of typosquatting, version-specific OSV advisories and update timestamps, full SPDX license expression and obligations, provenance/SLSA if available, dependency graph/SBOM, permissioned sandboxed functionality and support lifecycle. Query OSV with exact package/version and process complete pagination; "no returned advisory" is **not** a security guarantee. Never auto-install on any automatic `review_ready` report.

**Technical references:** [SPDX normative license-expression grammar](https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/); [OSV version-specific query API](https://github.com/google/osv.dev/blob/master/docs/api/post-v1-query.md); [Package URL specification](https://github.com/package-url/purl-spec). These are check sources, not evidence that any candidate in this study passed those checks.

**Practical lesson:** before an agent adds a dependency to your repo, pin official package identity and version, audit license/security/maintenance, test in an isolated environment, and retain the *rejected candidate* as evidence for future reuse searches.


## 2026-10-13 unknown-artifact follow-up

The pre-install screen now accepts **explicit `artifact_sha256: null`** as unresolved evidence, not as a zero hash, an automatically excluded package, or a verified artifact. It always includes `artifact_sha256` among `unknown_checks` and returns `defer` unless another declared gate fails (then `reject`). Omitting the field entirely remains a malformed-input error. Even six self-reported passing gates **cannot** produce `review_ready` without an exact declared artifact digest; a declared hex digest is not independently authenticated by this CLI. Two negative regressions cover the missing/unknown states. This preserves viable *candidate discovery* while refusing unverified *installation*.

## 2026-10-13 quality regression: exact-release lexical validation

The offline validator now accepts pinned **release-like** strings with ordinary letters, such as `1.0.post1` and `1.2.0-nightly.1`, while rejecting whitespace, tabs/newlines, range or wildcard characters, paths and moving aliases. Earlier character-class escaping accidentally treated letters `t` and `n` as forbidden; two regression tests detect both the false rejection and invalid selectors. This is **syntactic filtering only**: arbitrary release-like text can still describe a nonexistent or unpublished artifact. No release is trusted or installed without independently checking the exact official registry and artifact bytes. For non-PyPI ecosystems, the parser currently checks HTTPS syntax but **does not verify the official registry host**; these inputs require independent identity review.

**Integration warning:** [PR #186](https://github.com/MSKazemi/github-trending-1000-study/pull/186) implements a separate `package_trust` API for the same issue; do not present the two outputs as independent security confirmations or merge both as unrelated security decisions. Align a single versioned public interface and retain useful test cases/docs before removing either implementation. Changes in this branch remain a proposal subject to actual security and maintainer review.


## Consolidation from overlapping PR #186 (2026-10-13)

To preserve useful provenance requirements without shipping two conflicting
security-decision APIs, this canonical `package_review` CLI now accepts **optional**
`candidate.purl` and `candidate.source_commit`. For the currently supported
PyPI ecosystem, a supplied purl must be a single unambiguous
`pkg:pypi/name@version`, with the same normalized package name and exact
version as the official `pypi.org/project/name/version/` binding. A supplied
source commit must be a pinned lowercase 40-hex Git SHA. Malformed, moving,
contradictory or non-PyPI purl values fail closed; unknown provenance remains
**unknown** rather than being replaced with fabricated identifiers.

These optional fields are **self-declared structural assertions**. Neither
their presence nor a well-formed purl/SHA verifies a release, source-artifact
correspondence, publisher ownership, legal license compatibility or security.
The independent release verification steps above remain mandatory before reuse.
PR #186 retains its independent source history and synthetic examples as
superseded background; a second live `package_trust` CLI is deliberately not
introduced into the canonical user interface. Regression tests exercise both
well-formed and contradictory identity inputs.

## 2026-10-13 URL integrity hardening (post-merge review)

The canonical pre-install evidence gate now validates the entire **structural** HTTPS URL for both declared registry locations and self-reported pass evidence, rather than trusting a parsed hostname while ignoring semicolon parameters, hidden queries, malformed ports, bracket errors or whitespace. In particular, Python's URL parser may discard embedded newlines and separate trailing `;` parameters from the path: these are rejected before identity comparison. Malformed hosts/ports must raise the documented `PackageReviewError` rather than escaping as raw parser exceptions. Genuine clean evidence links continue to pass. The new negative regression tests exercise these bypass cases.

**Validity boundary:** a structurally clean HTTPS link is not authenticated evidence of a working release, correct bytes, provenance, license compatibility, advisory completeness or trusted publisher. The tool continues to **never approve automatic installation**. Any unknown or unsupported registry origin is deferred until independent checks occur. Existing report inputs are not overwritten.

## 2026-10-14 package input integrity

The CLI and `evaluate_file(path)` now use the existing research JSON decoder,
rejecting duplicate object keys (including contradictory fail/pass gate labels),
nonstandard numbers, numeric overflow/underflow and invalid UTF-8. Inputs must be
regular non-symlink files of at most the shared 16 MiB byte limit; devices, FIFOs,
directories and oversized files are rejected. The opened descriptor is inspected
and reads are bounded, including when a file grows after the size check. Deep
JSON decoder errors produce a nonzero CLI error without a traceback or a report.
Decoder failures use a fixed diagnostic, including nesting-limit errors, so
arbitrary private duplicate-key names, filenames and decoder context are not
echoed to the terminal or exposed through a chained exception.

PyPI URL and optional purl bindings now apply the same
[PyPA name normalization](https://packaging.python.org/en/latest/specifications/name-normalization/):
case-folding and replacing each run of hyphens, underscores or periods with one
hyphen. Thus `Fictional__Pkg` can bind to `fictional-pkg`; a different normalized
name or an inexact version still fails. This resolves a false rejection of
equivalent registry names, without authenticating any registry or artifact.

These are offline structural checks only. Existing output fields and decisions
retain their limits: source checks remain self-declared and
`automatic_install_approved` remains false. Independent package, license,
provenance, advisory, functional and human security review are still outstanding
for any real reuse candidate.

### 2026-10-15 PyPI path-identity hardening

The offline gate requires a literal ASCII project/version path on the official
PyPI host, rejecting percent-escaped or Unicode URL segments before applying
[PyPA normalized project-name equality](https://packaging.python.org/en/latest/specifications/name-normalization/).
Otherwise decoding a URL first and then applying Unicode `casefold()` can
confuse a non-ASCII character such as long-s (`ſ`) with an ASCII package name.
This is intentionally narrower than URL parsing in general: an escaped URL must
be resolved and authenticated independently, not silently treated as a pinned
identity. The gate still only validates self-declared input; it does not
establish a real distribution, artifact digest, rights, provenance, or approval.


## 2026-10-15 schema and negative-source safety correction

The offline evidence gate now rejects undeclared top-level, candidate and
per-check fields, rather than silently ignoring an arbitrary extra string that
could contain private user data or a competing unchecked security claim.
Declared `evidence_url` values are validated **for pass, fail and unknown**
states: a source URL with embedded credentials, query tokens or malformed
ports does not become safe simply because a check reports failure or
uncertainty. A passing gate still requires an evidence URL; a failing or
unknown gate may omit one. Synthetic negative tests exercise all three
unknown-field locations and both non-pass statuses. These rules validate
submission shape, not the truth of a source or actual package safety.

**Follow-up (2026-10-15):** a failing or unknown gate may omit `evidence_url`
*or* set it to `null`, which this repository uses for an explicitly unknown
value (`{"status": "unknown", "evidence_url": null}` defers, as on `main`
before this branch); any non-null value must still be a clean HTTPS URL, and a
pass still requires one. HTTPS URLs with an explicit port `0` are rejected as a
malformed authority. `evaluate_file` now reuses the shared
`data_integrity.load_research_json_file` bounded reader instead of a local
copy; errors remain `PackageReviewError` with fixed diagnostics that do not
echo the input path or private object keys.
