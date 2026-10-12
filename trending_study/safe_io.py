"""Write-once provenance storage for small research artifacts (stdlib-only).

Stage complete bytes, then hard-link into a new destination. Hard-link creation
is atomic and fails if a destination already exists; os.replace would clobber.
A multi-file bundle is NOT one filesystem transaction. If publishing one file
succeeds and another fails, preserved files are never deleted automatically:
the bundle must be manually inspected and is not valid until complete.
"""
import json
import os
from pathlib import Path
import tempfile


class ProvenanceWriteError(ValueError):
    """A research artifact cannot be published without risking prior data."""


def _paths(items):
    paths = [Path(path) for path in items]
    canonical = [path.resolve(strict=False) for path in paths]
    if len(canonical) != len(set(canonical)):
        raise ProvenanceWriteError("input/output destinations or bundle paths overlap")
    return paths


def refuse_existing(*paths):
    """Check for existing files or symlinks BEFORE performing network requests."""
    for path in _paths([p for p in paths if p is not None]):
        if path.exists() or path.is_symlink():
            raise ProvenanceWriteError(f"refusing to overwrite existing artifact: {path}")


def disjoint(*paths):
    """Reject path collisions, including aliases through preexisting symlinks."""
    _paths([p for p in paths if p is not None])


def _json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def jsonl_bytes(rows):
    return "".join(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n"
                   for row in rows).encode("utf-8")


def publish_once(entries):
    """Publish [(path, bytes)] without overwriting prior data.

    All payloads are staged before any destination is linked. There is no
    all-or-nothing guarantee across multiple paths; callers must validate the
    source/manifest pair before treating it as eligible research evidence.
    """
    entries = [(Path(path), data) for path, data in entries]
    if not entries:
        raise ProvenanceWriteError("no output artifacts supplied")
    _paths([path for path, _ in entries])
    refuse_existing(*(path for path, _ in entries))
    if any(not isinstance(data, bytes) for _, data in entries):
        raise ProvenanceWriteError("all staged artifacts must contain bytes")
    staged = []
    published = []
    try:
        for path, data in entries:
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix=".capture-pending-", dir=path.parent, delete=False
            ) as stage:
                staged.append(Path(stage.name))
                stage.write(data)
                stage.flush()
                os.fsync(stage.fileno())
        for (path, _), stage in zip(entries, staged):
            # Never use replace/rename here: they can destroy an earlier capture.
            os.link(stage, path)
            published.append(str(path))
    except OSError as exc:
        state = "partial bundle: " + ", ".join(published) if published else "no output published"
        raise ProvenanceWriteError(
            f"write-once publication failed ({state}); inspect artifacts before retrying"
        ) from exc
    finally:
        for stage in staged:
            stage.unlink(missing_ok=True)


def publish_json(path, value):
    publish_once([(path, _json_bytes(value))])


def publish_jsonl(path, rows):
    publish_once([(path, jsonl_bytes(rows))])
