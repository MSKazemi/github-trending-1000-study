# Offline registry pair-packet integrity

Issue #15's registry pilot is an offline, source-bounded package-name lead
frame. It neither installs packages nor validates a human research cohort.

The `audit-pairs` command validates the complete packet's schema before
counting submitted reviewer decisions. A valid content fingerprint is necessary
but does not replace schema validation. `nominated_pair_count` must equal the
number of pair records; pair IDs, task IDs and task/component combinations
must be unique, and every nominated task must appear in the packet's task frame.
Malformed identities, unsupported schema versions, inconsistent uncertainty
flags and undeclared fields are rejected. One submitted decision cannot be
multiplied by repeating a pair record.

All three subcommands read every input through the shared
`data_integrity.load_research_json_file` reader (see the 2026-10-15
maintainer-review correction below). Duplicate object keys, nonstandard or non-finite numeric values,
overflow, underflow and invalid UTF-8 fail before publishing a result.
Outputs retain the existing write-once publication contract.

**2026-10-15 input-safety correction.** The first draft passed `Path.read_bytes()`
to that strict parser; this silently followed leaf symlinks and read an unbounded
input before parsing. All three CLI modes now open each input nonblocking and
without following its final symlink (on platforms with the required OS flags),
verify the opened descriptor is an ordinary file, cap the actual read at
`MAX_FILE_BYTES + 1`, and sanitize malformed JSON diagnostics so sensitive
object keys and local file paths are not echoed. The same bound applies to each
input separately, not to the sum of the several input files. On platforms
without these safe-open flags, the CLI fails closed. This is not a guarantee
against hostile ancestor-directory replacement. Offline synthetic tests cover
oversized sparse files, directories, symlinks, FIFOs, private duplicate keys,
and no-output-on-failure behavior. This corrects a code safety defect, not
scientific sample validation.

**2026-10-15 maintainer-review correction (supersedes the bespoke reader
described above).** The module-local `_read` duplicated the repository's
shared bounded reader. It now delegates to
`data_integrity.load_research_json_file`, the house pattern also used by
`package_review`, `literature_ledger` and other strict CLIs, and maps its
fixed diagnostics to `RegistryFrameError` without echoing paths or keys. The
oversized/symlink/FIFO/directory/duplicate-key/no-output regressions are kept
unchanged and still pass. On platforms without `O_NOFOLLOW`, the shared
reader's pre-open symlink check applies instead of failing closed.

Run the offline regression checks with:

```bash
python -m unittest discover -s tests -p test_quiet_reuse_registry_integrity.py -v
python -m unittest discover -s tests -v
```

Every new reviewer, task and package fixture is synthetic. Reviewer identity,
independence, source rights, source authenticity, task correctness, release
availability, license and security still require actual external verification.
Neither a content fingerprint nor a successful structural audit establishes
scientific acceptance. The output flags for authenticated human reviewers and
issue #15 scientific acceptance remain false.

The `prepare-pairs` command now requires the original `--manifest` and `--plan`
alongside `--selection`. It deterministically derives `select_registry(manifest,
plan)` and compares the complete selection before admitting any nominations.
Changing selected package IDs, source records, seed, quotas or provenance/count
fields requires deriving a new selection from those inputs; an edited list
cannot nominate an off-frame package while retaining the original hashes.
This checks consistency of submitted artifacts, not source authenticity: an
invented source manifest/plan cannot become independently verified evidence by
passing the comparison.

`audit-pairs` likewise requires `--manifest` and `--plan`. A packet's
`packet_sha256` is computed by whoever wrote the packet, so before counting any
review the audit re-derives `select_registry(manifest, plan)` and requires the
packet's `selection_plan_sha256` and `selection_source_sha256` to equal the
fresh selection's hashes and every pair's `package_id` to be a selected lead.
An off-frame package or a re-bound plan/source hash can no longer be counted
by recomputing the packet fingerprint.

The manifest reader also recomputes each segment's Git tree-object SHA-1 from
its entries (mode `100644`, name, blob SHA, byte-sorted names) and requires it
to equal the declared `directory_tree_sha`. Dropping, adding, renaming or
re-hashing an entry while adjusting `declared_count` therefore fails. This
binds the listing to a content address; it does not prove that the upstream
repository actually served that tree.

This is a compatibility correction to a new, unmerged pilot interface with no
existing repository consumers. Python callers must supply the original inputs
as `prepare_pair_packet(selection, tasks, nominations, manifest, plan)` and
`audit_pair_reviews(packet, review_a, review_b, manifest, plan)`.
Existing selection/result output fields are preserved. For example:

```bash
python -m trending_study.quiet_reuse_registry prepare-pairs \
  --manifest /path/to/original-manifest.json --plan /path/to/original-plan.json \
  --selection /path/to/selection.json --tasks /path/to/frozen-tasks.json \
  --nominations /path/to/nominations.json --output /path/to/new-pair-packet.json
```

Reuse review: the existing standard-library-only public strict JSON helper and
write-once publisher satisfy this task without another dependency or JSON
parser. The MIT-licensed repository's existing validators and tests were
inspected. Python's official JSON documentation describes duplicate-key and
nonstandard-number defaults: <https://docs.python.org/3/library/json.html>.
No public-package installation or external code execution was needed.


## 2026-10-15 task/reviewer chronology guard

The pair-audit verifier now rejects any submitted reviewer timestamp earlier
than any task's recorded frozen baseline. Previously an otherwise internally
consistent fictitious review could be dated **before** its task existed while
still increasing the provisional-fit numerator. This rule applies even if the
coder's report has no decisions; an empty but pre-task report is not a valid
post-baseline review event. Regression tests cover a pre-task report and a
re-fingerprinted packet with its task date moved after both reviewers' dates.
At/after-baseline timestamps only establish internal chronology: task-freeze
independence, release availability, package rights, reviewer identities and
actual functional tests all still require a qualified external audit. This
is not evidence that the issue's 50 human-adjudicated pairs have been obtained.


## 2026-10-15 distinguish synthetic concordance from the 50-human acceptance target

Earlier reports computed `still_needed_for_50_provisional = 50 -
concordant_provisional_fit`. That number describes the remaining **candidate
matching-label** count only: even perfect synthetic A/B concordance supplies
**zero externally authenticated independent human reviews**. The output now
also returns `externally_authenticated_human_pairs: 0` and
`still_needed_for_50_authenticated_human_pairs: 50`, without allowing
self-supplied rater IDs, invented test links or labels to decrement the true
scientific review requirement. The original provisional counter is preserved
for backward-compatible offline feasibility diagnostics, but should never be
presented as completed scientific progress. To reduce the real remaining
number, a **separate provenance-verified, qualified human review workflow**
will need a new audited schema and signed/traceable source records. This tool
cannot authenticate that external process or certify issue #15's 50-pair gate.

## 2026-10-16 exact Cargo release guard

A nominated `version` is now either `null` (unknown) or a bounded **concrete Cargo `X.Y.Z` release identifier**, optionally containing standard prerelease/build suffixes. Range/moving selectors such as `latest`, `main`, `1.*`, `^1.0.0`, `>=1.0.0`, whitespace and path-like versions are rejected. The audit repeats the validation on the submitted packet **after** the user-controlled fingerprint is recomputed; forging a new packet hash cannot turn a moving version into a provisional passing pair. The release identity is still *self-declared*: syntax does not prove crates.io availability, version-specific license, repository identity, source rights, historical availability or real tested task fit.

Two synthetic regression methods exercise both nomination and packet-audit boundaries, including legitimate prerelease/build syntax. The issue #15 50-pair genuinely independent human screening and external source checks remain pending. A recorded `concordant_provisional_fit` is **not** a validated human task outcome.

## Pinned release syntax follow-up (2026-10-16)

The offline nomination validator now refuses noncanonical SemVer numeric spellings with leading zeroes in major/minor/patch or purely numeric prerelease components (for example `01.2.3`, `1.2.03`, `1.2.3-rc.01`). It retains ordinary pinned releases such as `0.2.0-alpha.3` and `2.1.4+build.5`. Six negative fixture versions guard this boundary. This is only lexical consistency with SemVer-style Cargo versions: it does **not** prove that the named crate, version, source artifact, release date, license or any reviewed task-component pair exists or is acceptable. The independently authenticated 50-pair scientific acceptance gate remains entirely unmet.

## 2026-10-17 full-traceback privacy correction

The existing bounded registry pilot returned fixed CLI error *text*, but its
malformed UTC date converter retained the raw `datetime.fromisoformat`
`ValueError` as a chained cause. Its shared JSON-loader wrapper used
`raise ... from None` **inside** the handler, which suppresses printed context
but does not clear `__context__`. Finally, invoking `argparse.error` inside
an untrusted read/validation exception could attach raw paths or JSON keys
to `SystemExit` for telemetry to inspect.

The offline module now raises public bounded errors only **outside** low-level
exception handlers, and invokes argparse failure after the handler has exited.
Synthetic tests check full formatted traceback output, explicit exception
causes/contexts and command-line stderr for private markers. Existing input
limits, validation contracts, write-once publication, and source records
remain unchanged.

This is a narrow engineering/privacy improvement, not a guarantee against
arbitrary caller logs, intentional successful exports, false manifests or
invented reviewer identity. There is still **no** authenticated repository
cohort or 50 independently human-reviewed task/package pairs.

**Maintainer lesson:** use complete exception and CLI failure traces in
negative-input tests. A safe-looking string may hide private nested causes.

## 2026-10-17 pinned public registry listing cross-check

A separate **read-only GitHub Contents API** retrieval compared the precise
upstream `rust-lang/crates.io-index` commit
`9b349b77adb46425be15e386ef38f31061be3ca9` against both committed
bounded source-manifest segments:

- `contents/2?ref=<pinned-sha>`: 725 upstream entries; all 725 manifest
  package names **and individual Git blob SHAs** matched; no extra entries
- `contents/3/a?ref=<pinned-sha>`: 282 upstream entries; all 282 manifest
  package names **and individual Git blob SHAs** matched; no extra entries

This independently re-queries *those two exact paths* and establishes a
**1,007/1,007 snapshot-name/blob match**, rather than relying solely on a
self-reported manifest. The bytewise SHA bound and Git tree-object SHA
reproduction checks remain in the code. It does **not** authenticate the
human sampler, make two handpicked paths representative of all crates.io or
GitHub repositories, validate any software version/license/security, prove
source crawl permissions, or establish genuine independent task-component
review. Accordingly `source_listings_independently_authenticated` in the
synthetic/audit CLI remains deliberately **false**, since the CLI itself makes
no authenticated upstream requests and cannot carry this chat-level check
as an attested input. Issue #15 still needs authentic human review.

**Reproduction:** read the exact two GitHub API URLs stored as `source_url`
in `research-notes/issue-15-crates-index-bounded-listing-2026-10-14.json`,
compare the complete returned (name, blob SHA) maps against every
`entries[].package_name`/`entries[].blob_sha`, and reject any omissions or
extras. No registry packages were fetched, installed or executed.

**Practical lesson:** a self-consistent hash should be checked against an
external, version-pinned source whenever available, and conclusions must
remain limited to the actually inspected sampling frame.
