"""Validate published Hydra risk-event records as a collection."""

from __future__ import annotations

import json
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


STRUCTURED_INDEX_START = "<!-- BEGIN GENERATED STRUCTURED EVENT INDEX -->"
STRUCTURED_INDEX_END = "<!-- END GENERATED STRUCTURED EVENT INDEX -->"
LEDGER_PATH = Path("governance/risk-event-ledger.md")


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


def load_published_event_instances(root: Path) -> tuple[tuple[Path, dict[str, object]], ...]:
    """Load published event objects in their deterministic source-path order."""
    instances: list[tuple[Path, dict[str, object]]] = []
    for path in iter_published_events(root):
        instance = load_event(path)
        if not isinstance(instance, dict):
            raise ValueError(f"{path.as_posix()}: event root must be an object")
        instances.append((path, instance))
    return tuple(instances)


def _event_display_title(event_id: str) -> str:
    stem = re.sub(r"^HRE-[0-9]{4}-[0-9]{2}-", "", event_id)
    return stem.replace("_", "-").replace("-", " ").lower().capitalize()


def _markdown_cell(value: object) -> str:
    return " ".join(str(value).splitlines()).replace("|", r"\|")


def _display_utc(value: object) -> str:
    text = str(value)
    return text[:-1].replace("T", " ") if text.endswith("Z") else text


def render_structured_event_index(root: Path) -> str:
    """Render the authoritative JSON records as the public Markdown index."""
    lines = [
        STRUCTURED_INDEX_START,
        "",
        "| Date (UTC) | Event | Public summary | Details |",
        "| --- | --- | --- | --- |",
    ]
    for path, event in sorted(load_published_event_instances(root), key=_event_sort_key):
        event_id = str(event["event_id"])
        relative_json = path.relative_to(root).as_posix()
        lines.append(
            "| "
            f"`{_display_utc(event['occurred_at'])}` | "
            f"{_markdown_cell(_event_display_title(event_id))} | "
            f"{_markdown_cell(event['public_summary'])} | "
            f"[JSON](../{relative_json}) |"
        )
    lines.extend(("", STRUCTURED_INDEX_END))
    return "\n".join(lines)


def _structured_index_bounds(text: str) -> tuple[int, int]:
    if text.count(STRUCTURED_INDEX_START) != 1 or text.count(STRUCTURED_INDEX_END) != 1:
        raise ValueError("ledger must contain exactly one generated structured event index")
    start = text.index(STRUCTURED_INDEX_START)
    end = text.index(STRUCTURED_INDEX_END, start) + len(STRUCTURED_INDEX_END)
    return start, end


def write_structured_event_index(root: Path) -> None:
    """Replace only the generated structured index block in the public ledger."""
    ledger = root / LEDGER_PATH
    text = ledger.read_text(encoding="utf-8")
    start, end = _structured_index_bounds(text)
    ledger.write_text(text[:start] + render_structured_event_index(root) + text[end:], encoding="utf-8")


def check_structured_event_index(root: Path) -> list[str]:
    """Report whether the rendered public index differs from authoritative JSON."""
    ledger = root / LEDGER_PATH
    try:
        text = ledger.read_text(encoding="utf-8")
        start, end = _structured_index_bounds(text)
        expected = render_structured_event_index(root)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return ["governance/risk-event-ledger.md: cannot render structured event index"]
    if text[start:end] != expected:
        return ["governance/risk-event-ledger.md: generated structured event index is stale"]
    return []


def validate_published_events(
    root: Path,
    schema: dict[str, object],
    formatter: FormatChecker,
) -> list[str]:
    """Validate every published event without applying fixture-only rules."""
    validator = Draft202012Validator(schema, format_checker=formatter)
    errors: list[str] = []
    instances: list[tuple[Path, dict[str, object]]] = []
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
        if isinstance(instance, dict):
            instances.append((path, instance))
    errors.extend(validate_event_collection(root, tuple(instances)))
    return errors


def check_event_relationships(
    instances: tuple[tuple[Path, dict[str, object]], ...],
    root: Path,
) -> list[str]:
    """Require corrections and supersessions to name an earlier event."""
    del root
    errors: list[str] = []
    seen: set[str] = set()
    for path, instance in sorted(instances, key=_event_sort_key):
        event_id = instance.get("event_id")
        if not isinstance(event_id, str):
            continue
        correction = instance.get("correction_of")
        supersedes = instance.get("supersedes")
        if correction is not None and supersedes is not None:
            errors.append(f"{path.as_posix()}: must not set both correction_of and supersedes")
        for field, target in (("correction_of", correction), ("supersedes", supersedes)):
            if not isinstance(target, str):
                continue
            if target == event_id:
                errors.append(f"{path.as_posix()}: {field} must not reference the same event")
            elif target not in seen:
                errors.append(
                    f"{path.as_posix()}: {field} does not identify an earlier published event"
                )
        seen.add(event_id)
    return errors


def _parse_utc(value: object) -> datetime:
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def _event_sort_key(item: tuple[Path, dict[str, object]]) -> tuple[datetime, datetime, str]:
    _, instance = item
    try:
        occurred = _parse_utc(instance["occurred_at"])
    except (KeyError, TypeError, ValueError):
        occurred = datetime.max.replace(tzinfo=timezone.utc)
    try:
        recorded = _parse_utc(instance["recorded_at"])
    except (KeyError, TypeError, ValueError):
        recorded = datetime.max.replace(tzinfo=timezone.utc)
    return occurred, recorded, str(instance.get("event_id", ""))


def _validate_public_reference(root: Path, event_path: Path, reference: object) -> str | None:
    if not isinstance(reference, str):
        return None
    parsed = urllib.parse.urlsplit(reference)
    if parsed.scheme in {"http", "https"}:
        return None
    if parsed.scheme or reference.startswith("/"):
        return "public evidence reference escapes repository"
    target = (event_path.parent / urllib.parse.unquote(parsed.path)).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return "public evidence reference escapes repository"
    if not target.is_file():
        return "public evidence reference does not exist"
    return None


def validate_event_collection(
    root: Path,
    instances: tuple[tuple[Path, dict[str, object]], ...],
) -> list[str]:
    """Validate identity, chronology, relationships, and public references."""
    errors: list[str] = []
    event_ids: set[str] = set()
    for path, instance in instances:
        display = path.relative_to(root).as_posix()
        event_id = instance.get("event_id")
        if isinstance(event_id, str):
            if event_id in event_ids:
                errors.append(f"{display}: duplicate published event_id")
            event_ids.add(event_id)
            if path.stem != event_id:
                errors.append(f"{display}: filename must equal event_id")
        for field in ("occurred_at", "recorded_at"):
            timestamp = instance.get(field)
            if isinstance(timestamp, str) and not timestamp.endswith("Z"):
                errors.append(f"{display}: {field} must use UTC Z notation")
        evidence = instance.get("evidence")
        if isinstance(evidence, dict):
            generated_at = evidence.get("generated_at")
            if isinstance(generated_at, str) and not generated_at.endswith("Z"):
                errors.append(f"{display}: evidence.generated_at must use UTC Z notation")
        try:
            occurred = _parse_utc(instance["occurred_at"])
            recorded = _parse_utc(instance["recorded_at"])
        except (KeyError, TypeError, ValueError):
            occurred = recorded = None
        if occurred is not None and recorded is not None:
            if recorded < occurred:
                errors.append(f"{display}: recorded_at precedes occurred_at")
            if path.parent.name != str(occurred.year):
                errors.append(f"{display}: directory year differs from occurred_at year")
        references = instance.get("public_evidence_refs", [])
        if isinstance(references, list):
            for reference in references:
                finding = _validate_public_reference(root, path, reference)
                if finding:
                    errors.append(f"{display}: {finding}")
    relationship_errors = check_event_relationships(instances, root)
    prefix = f"{root.resolve().as_posix()}/"
    errors.extend(error.replace(prefix, "", 1) for error in relationship_errors)
    return errors
