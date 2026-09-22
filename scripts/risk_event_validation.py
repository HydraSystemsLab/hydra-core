"""Validate published Hydra risk-event records as a collection."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


def iter_published_events(root: Path) -> tuple[Path, ...]:
    """Return deterministic year-partitioned published event paths."""
    event_root = root / "risk-events"
    if not event_root.is_dir():
        return ()
    return tuple(
        sorted(
            path
            for path in event_root.glob("[0-9][0-9][0-9][0-9]/*.json")
            if path.is_file()
        )
    )


def load_event(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_published_events(
    root: Path,
    schema: dict[str, object],
    formatter: FormatChecker,
) -> list[str]:
    """Validate every published event without applying fixture-only rules."""
    validator = Draft202012Validator(schema, format_checker=formatter)
    errors: list[str] = []
    for path in iter_published_events(root):
        display = path.relative_to(root).as_posix()
        try:
            instance = load_event(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{display}: invalid JSON ({exc.__class__.__name__})")
            continue
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "root"
            errors.append(f"{display}:{location}: schema validation failed")
        if isinstance(instance, dict) and instance.get("x-example-only") is True:
            errors.append(f"{display}: published event must not set x-example-only")
    return errors


def check_event_relationships(
    instances: tuple[tuple[Path, dict[str, object]], ...],
    root: Path,
) -> list[str]:
    """Reserved collection hook; Task 2 adds relationship semantics."""
    del instances, root
    return []
