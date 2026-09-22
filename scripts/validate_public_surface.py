#!/usr/bin/env python3
"""Validate Hydra Core's public documentation contract without exposing findings."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

try:
    from scripts.risk_event_validation import validate_published_events
except ModuleNotFoundError:  # direct script execution
    from risk_event_validation import validate_published_events

try:
    import yaml
except ImportError:  # pragma: no cover - exercised by dependency-failure path
    yaml = None

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError:  # pragma: no cover - exercised by dependency-failure path
    Draft202012Validator = None
    FormatChecker = None
    SchemaError = Exception


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".superpowers",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}
CANONICAL_FILES = (
    "README.md",
    "docs-map.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "architecture/public-surface-registry.md",
    "architecture/state-model.md",
    "governance/public-evidence-policy.md",
    "governance/risk-event-ledger.md",
    "governance/risk-event-ledger-policy.md",
    "governance/risk-event-schema.md",
    "governance/threat-model.md",
    "product/hydra-quant-private-alpha.md",
    "product/control-room-concept.md",
    "status/public-operating-posture.md",
    "status/public-operating-posture.json",
    "schemas/public-operating-posture.schema.json",
    "schemas/risk-event.schema.json",
    "examples/risk-events/README.md",
    "examples/risk-events/synthetic-duplicate-execution.json",
    "examples/risk-events/synthetic-model-authority-boundary.json",
    "risk-events/README.md",
    "release-notes/v0.1.0-pre-alpha.1.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/governance-question.yml",
    ".github/workflows/docs-quality.yml",
    "scripts/validate_public_surface.py",
    "tests/test_validate_public_surface.py",
    "requirements-docs.txt",
    "package.json",
    "package-lock.json",
)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
AUTOLINK_RE = re.compile(r"<(https?://[^>]+)>")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*>", flags=re.IGNORECASE)
CONCEPT_DISCLAIMER = (
    "Conceptual placeholder — this is not a production screenshot and does not "
    "represent live account state or live performance."
)
STATE_INVARIANT = (
    "Execution is eligible only when trust is `SAFE`, permission is `ARMED`, "
    "lifecycle is `NORMAL`, the configured operating mode permits execution, "
    "and every required gate passes."
)


def relative(path: Path, root: Path = ROOT) -> str:
    """Return a stable repository-relative display path."""
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def is_excluded(path: Path, root: Path = ROOT) -> bool:
    """Exclude dependencies, caches, VCS internals, and deliberate failing fixtures."""
    try:
        parts = path.resolve().relative_to(root.resolve()).parts
    except ValueError:
        parts = path.parts
    if any(part in EXCLUDED_DIRS for part in parts):
        return True
    return len(parts) >= 3 and parts[:3] == ("tests", "fixtures", "fail")


def iter_files(root: Path = ROOT, suffixes: set[str] | None = None) -> Iterable[Path]:
    """Yield public repository files in deterministic order."""
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file() or is_excluded(path, root):
            continue
        try:
            path.resolve().relative_to(root.resolve())
        except ValueError:
            continue
        if suffixes is None or path.suffix.lower() in suffixes:
            yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def prose_lines(text: str) -> Iterable[tuple[int, str]]:
    """Yield lines outside fenced code blocks."""
    fence: str | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in {"```", "~~~"}:
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            yield line_number, line


def github_slug(raw: str) -> str:
    """Approximate GitHub's stable heading slug rules for repository prose."""
    value = re.sub(r"<[^>]+>", "", raw)
    value = re.sub(r"[`*_~]", "", value).strip().lower()
    value = "".join(character for character in value if character.isalnum() or character in " _-")
    return re.sub(r"\s+", "-", value)


def heading_anchors(path: Path) -> set[str]:
    """Build anchors, including numeric suffixes for duplicate headings."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for _, line in prose_lines(read_text(path)):
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = github_slug(match.group(2))
        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        anchors.add(anchor)
    return anchors


def normalize_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def external_links(root: Path = ROOT) -> set[str]:
    links: set[str] = set()
    for path in iter_files(root, {".md"}):
        for _, line in prose_lines(read_text(path)):
            targets = [normalize_link_target(raw) for raw in LINK_RE.findall(line)]
            reference = REFERENCE_DEF_RE.match(line)
            if reference:
                targets.append(normalize_link_target(reference.group(1)))
            targets.extend(AUTOLINK_RE.findall(line))
            for target in targets:
                parsed = urllib.parse.urlsplit(target)
                if parsed.scheme in {"http", "https"}:
                    links.add(target)
    for path in iter_files(root, {".yml", ".yaml"}):
        links.update(re.findall(r"https?://[^\s\"'<>]+", read_text(path)))
    return links


def check_canonical_files(root: Path = ROOT) -> list[str]:
    return [f"missing canonical file: {name}" for name in CANONICAL_FILES if not (root / name).is_file()]


def check_markdown(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in iter_files(root, {".md"}):
        text = read_text(path)
        display = relative(path, root)
        if not text.endswith("\n"):
            errors.append(f"{display}: file must end with a newline")
        fence: str | None = None
        previous_heading = 0
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                errors.append(f"{display}:{line_number}: trailing whitespace")
            if "\t" in line:
                errors.append(f"{display}:{line_number}: tab character")
            stripped = line.lstrip()
            marker = stripped[:3]
            if marker in {"```", "~~~"}:
                if fence is None:
                    fence = marker
                elif marker == fence:
                    fence = None
                continue
            if fence is None:
                heading = HEADING_RE.match(line)
                if heading:
                    level = len(heading.group(1))
                    if previous_heading and level > previous_heading + 1:
                        errors.append(f"{display}:{line_number}: heading level jumps from {previous_heading} to {level}")
                    previous_heading = level
        if fence is not None:
            errors.append(f"{display}: unclosed Markdown fence")
        for match in re.finditer(r"```mermaid\s*\n(.*?)```", text, flags=re.DOTALL | re.IGNORECASE):
            body = match.group(1).strip()
            if not body or not re.search(r"\b(flowchart|graph|sequenceDiagram|stateDiagram|classDiagram)\b", body):
                errors.append(f"{display}: Mermaid block lacks a recognized diagram declaration")
    return errors


def check_internal_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for source in iter_files(root, {".md"}):
        for line_number, line in prose_lines(read_text(source)):
            targets = [normalize_link_target(raw) for raw in LINK_RE.findall(line)]
            reference = REFERENCE_DEF_RE.match(line)
            if reference:
                targets.append(normalize_link_target(reference.group(1)))
            for target in targets:
                parsed = urllib.parse.urlsplit(target)
                if parsed.scheme in {"http", "https", "mailto"}:
                    continue
                decoded_path = urllib.parse.unquote(parsed.path)
                destination = source if not decoded_path else (source.parent / decoded_path).resolve()
                try:
                    destination.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"{relative(source, root)}:{line_number}: local link escapes repository")
                    continue
                if not destination.is_file():
                    errors.append(
                        f"{relative(source, root)}:{line_number}: missing local link target {decoded_path or source.name}"
                    )
                    continue
                fragment = urllib.parse.unquote(parsed.fragment).lower()
                if fragment and destination.suffix.lower() == ".md":
                    anchors = anchor_cache.setdefault(destination, heading_anchors(destination))
                    if fragment not in anchors:
                        errors.append(
                            f"{relative(source, root)}:{line_number}: missing anchor #{fragment} in {relative(destination, root)}"
                        )
    return errors


def _forbidden_path_patterns() -> tuple[re.Pattern[str], ...]:
    unix_home = re.escape("/" + "home" + "/")
    unix_service = re.escape("/" + "srv" + "/")
    windows_drive = r"\b[A-Za-z]:\\"
    return tuple(re.compile(pattern) for pattern in (unix_home, unix_service, windows_drive))


def boundary_violations(path: Path, text: str, root: Path = ROOT) -> list[str]:
    """Return safe category-only findings; never echo a suspected secret value."""
    findings: list[str] = []
    display = relative(path, root)
    lines = text.splitlines()

    for pattern in _forbidden_path_patterns():
        for line_number, line in enumerate(lines, start=1):
            if pattern.search(line):
                findings.append(f"{display}:{line_number}: forbidden private absolute path")

    credential_pattern = re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|secret|password|credential)\b\s*[:=]\s*[\"']?[A-Za-z0-9_./+\-=]{12,}"
    )
    token_patterns = (
        re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    )
    account_pattern = re.compile(
        r"(?i)\b(?:account|login|client)[ _-]?(?:id|number)\b\s*[:=]\s*[\"']?[A-Za-z0-9_-]{6,}"
    )
    for line_number, line in enumerate(lines, start=1):
        if credential_pattern.search(line) or any(pattern.search(line) for pattern in token_patterns):
            findings.append(f"{display}:{line_number}: likely credential material (value withheld)")
        if account_pattern.search(line):
            findings.append(f"{display}:{line_number}: likely account identifier (value withheld)")

    historical_ledger = display == "governance/risk-event-ledger.md"
    dynamic_tokens = (
        "C" + "15396",
        "B" + "5",
        "BTC" + "USD_D",
        "XAU" + "USD_A",
        "AUD" + "JPY_E",
        "LIVE" + "_ON",
    )
    dynamic_phrases = (
        "approved " + "live-money",
        "current private " + "posture",
        "funded " + "account",
        "execution" + " = online",
    )
    if not historical_ledger:
        lowered = text.lower()
        for token in dynamic_tokens:
            if re.search(rf"(?<![a-z0-9]){re.escape(token.lower())}(?![a-z0-9])", lowered):
                findings.append(f"{display}: dynamic engine/status identifier outside historical ledger")
        for phrase in dynamic_phrases:
            if phrase.lower() in lowered:
                findings.append(f"{display}: changing operational claim outside historical ledger")

    markers = ("TO" + "DO", "T" + "BD")
    for line_number, line in prose_lines(text):
        for marker in markers:
            if re.search(rf"\b{re.escape(marker)}\b", line, flags=re.IGNORECASE):
                findings.append(f"{display}:{line_number}: unlabeled placeholder marker {marker}")

    media_descriptors = [" ".join(image.groups()) for image in IMAGE_RE.finditer(text)]
    media_descriptors.extend(image.group(0) for image in HTML_IMAGE_RE.finditer(text))
    for descriptor in media_descriptors:
        if re.search(r"(?i)\b(?:control[ -]?room|dashboard|screenshot)\b", descriptor):
            if CONCEPT_DISCLAIMER not in text:
                findings.append(f"{display}: screenshot-like media lacks the exact conceptual disclaimer")
    return findings


def check_public_boundary(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in iter_files(root):
        try:
            text = read_text(path)
        except (UnicodeDecodeError, OSError):
            continue
        errors.extend(boundary_violations(path, text, root))
    return errors


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def check_json_and_schemas(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    invalid_json: set[Path] = set()
    for path in iter_files(root, {".json"}):
        try:
            load_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{relative(path, root)}: invalid JSON ({exc.__class__.__name__})")
            invalid_json.add(path.resolve())

    if Draft202012Validator is None or FormatChecker is None:
        errors.append("schema validation dependencies are unavailable; install requirements-docs.txt")
        return errors

    posture_schema_path = root / "schemas/public-operating-posture.schema.json"
    risk_schema_path = root / "schemas/risk-event.schema.json"
    try:
        posture_schema = load_json(posture_schema_path)
        risk_schema = load_json(risk_schema_path)
        Draft202012Validator.check_schema(posture_schema)
        Draft202012Validator.check_schema(risk_schema)
    except (OSError, json.JSONDecodeError, SchemaError) as exc:
        errors.append(f"schema definition invalid ({exc.__class__.__name__})")
        return errors

    formatter = FormatChecker()
    posture_validator = Draft202012Validator(posture_schema, format_checker=formatter)
    risk_validator = Draft202012Validator(risk_schema, format_checker=formatter)

    posture_path = root / "status/public-operating-posture.json"
    try:
        posture = load_json(posture_path)
    except (OSError, json.JSONDecodeError) as exc:
        if posture_path.resolve() not in invalid_json:
            errors.append(f"{relative(posture_path, root)}: invalid JSON ({exc.__class__.__name__})")
    else:
        for error in sorted(posture_validator.iter_errors(posture), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "root"
            errors.append(f"{relative(posture_path, root)}:{location}: schema validation failed")

    event_ids: set[str] = set()
    for path in sorted((root / "examples/risk-events").glob("*.json")):
        try:
            instance = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            if path.resolve() not in invalid_json:
                errors.append(f"{relative(path, root)}: invalid JSON ({exc.__class__.__name__})")
            continue
        for error in sorted(risk_validator.iter_errors(instance), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "root"
            errors.append(f"{relative(path, root)}:{location}: schema validation failed")
        if isinstance(instance, dict):
            event_id = instance.get("event_id")
            if event_id in event_ids:
                errors.append(f"{relative(path, root)}: duplicate public event_id")
            if isinstance(event_id, str):
                event_ids.add(event_id)
            if instance.get("x-example-only") is not True:
                errors.append(f"{relative(path, root)}: synthetic fixture must set x-example-only true")
            if not str(instance.get("public_summary", "")).startswith("Synthetic example:"):
                errors.append(f"{relative(path, root)}: synthetic summary is not explicitly labelled")
            try:
                if parse_utc(str(instance["recorded_at"])) < parse_utc(str(instance["occurred_at"])):
                    errors.append(f"{relative(path, root)}: recorded_at precedes occurred_at")
            except (KeyError, TypeError, ValueError):
                pass
    errors.extend(validate_published_events(root, risk_schema, formatter))
    return errors


def check_posture_contract(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    path = root / "status/public-operating-posture.json"
    try:
        posture = load_json(path)
    except (OSError, json.JSONDecodeError):
        return ["status/public-operating-posture.json: cannot inspect posture contract"]
    if not isinstance(posture, dict):
        return ["status/public-operating-posture.json: posture root must be an object"]

    required_values = {
        "release_stage": "PRE_V1",
        "product_stage": "PRIVATE_ALPHA_PREPARATION",
        "external_access": "CLOSED_INVITE_ONLY_PREPARATION",
        "public_user_mode": "READ_ONLY_FORWARD_SHADOW",
        "public_user_broker_connection": "DISABLED",
        "public_user_order_submission": "DISABLED",
        "public_user_live_execution": "DISABLED",
        "control_room_status": "CONCEPTUAL_IN_DEVELOPMENT",
    }
    for field, expected in required_values.items():
        if posture.get(field) != expected:
            errors.append(f"status/public-operating-posture.json:{field}: required public posture value is absent")

    try:
        as_of = parse_utc(str(posture["as_of"]))
        review_due = parse_utc(str(posture["review_due_at"]))
        stale_after = parse_utc(str(posture["stale_after"]))
        if not as_of < review_due <= stale_after:
            errors.append("status/public-operating-posture.json: posture time ordering is invalid")
    except (KeyError, TypeError, ValueError):
        errors.append("status/public-operating-posture.json: posture timestamps are invalid")

    source_commit = str(posture.get("source_commit", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        errors.append("status/public-operating-posture.json: source_commit must be a full SHA")

    markdown = read_text(root / "status/public-operating-posture.md")
    if "UNKNOWN/REVIEW_REQUIRED" not in markdown:
        errors.append("status/public-operating-posture.md: stale behavior is missing")
    if "Private engine-level permission is not disclosed" not in markdown:
        errors.append("status/public-operating-posture.md: private permission separation is missing")

    alpha = read_text(root / "product/hydra-quant-private-alpha.md").lower()
    for phrase in ("read-only", "forward-shadow", "no public-user live trading", "no public-user order submission"):
        if phrase not in alpha:
            errors.append("product/hydra-quant-private-alpha.md: required read-only/shadow or disabled-execution wording is missing")

    state_model = read_text(root / "architecture/state-model.md")
    if STATE_INVARIANT not in state_model:
        errors.append("architecture/state-model.md: exact execution invariant is missing")
    if "`ARMED` in `SHADOW` authorizes shadow processing only" not in state_model:
        errors.append("architecture/state-model.md: shadow ARMED boundary is missing")

    concept = read_text(root / "product/control-room-concept.md")
    disclaimer = "Conceptual placeholder — this is not a production screenshot and does not represent live account state or live performance."
    if disclaimer not in concept:
        errors.append("product/control-room-concept.md: required conceptual disclaimer is missing")
    return errors


def check_posture_freshness(root: Path = ROOT, now: datetime | None = None) -> list[str]:
    """Fail after the published posture's inclusive freshness boundary."""
    path = root / "status/public-operating-posture.json"
    try:
        posture = load_json(path)
        stale_after = parse_utc(str(posture["stale_after"]))
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return ["status/public-operating-posture.json: cannot evaluate posture freshness"]
    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None:
        return ["freshness evaluation time must include a timezone"]
    if instant > stale_after:
        return ["status/public-operating-posture.json: public posture is stale"]
    return []


def check_yaml_and_workflow(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if yaml is None:
        return ["YAML validation dependency is unavailable; install requirements-docs.txt"]
    for path in iter_files(root, {".yml", ".yaml"}):
        try:
            document = yaml.safe_load(read_text(path))
            if not isinstance(document, dict):
                errors.append(f"{relative(path, root)}: YAML root must be a mapping")
        except yaml.YAMLError:
            errors.append(f"{relative(path, root)}: invalid YAML")

    workflow_path = root / ".github/workflows/docs-quality.yml"
    if not workflow_path.is_file():
        return errors
    workflow = read_text(workflow_path)
    try:
        policy = yaml.load(workflow, Loader=yaml.BaseLoader)
    except yaml.YAMLError:
        return errors
    if not isinstance(policy, dict):
        return errors

    triggers = policy.get("on")
    expected_triggers = {"pull_request", "push", "workflow_dispatch", "schedule"}
    if not isinstance(triggers, dict) or set(triggers) != expected_triggers:
        errors.append(
            ".github/workflows/docs-quality.yml: triggers must be PR, main push, manual dispatch, and fixed weekly schedule only"
        )
    else:
        push_policy = triggers.get("push")
        branches = push_policy.get("branches") if isinstance(push_policy, dict) else None
        if branches != ["main"]:
            errors.append(".github/workflows/docs-quality.yml: push scope must be exactly main")
        if triggers.get("schedule") != [{"cron": "17 6 * * 1"}]:
            errors.append(".github/workflows/docs-quality.yml: weekly freshness schedule must be fixed")

    if policy.get("permissions") != {"contents": "read"}:
        errors.append(".github/workflows/docs-quality.yml: top-level permissions must be contents read only")

    concurrency = policy.get("concurrency")
    if not isinstance(concurrency, dict) or concurrency.get("cancel-in-progress") != "true":
        errors.append(".github/workflows/docs-quality.yml: concurrency cancellation is missing")

    jobs = policy.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        errors.append(".github/workflows/docs-quality.yml: workflow must define a validation job")
    else:
        for job_name, job in jobs.items():
            if not isinstance(job, dict):
                errors.append(f".github/workflows/docs-quality.yml: job {job_name} must be a mapping")
                continue
            if "permissions" in job:
                errors.append(f".github/workflows/docs-quality.yml: job {job_name} must not override permissions")
            if "timeout-minutes" not in job:
                errors.append(f".github/workflows/docs-quality.yml: job {job_name} lacks a timeout")

    if "persist-credentials: false" not in workflow:
        errors.append(".github/workflows/docs-quality.yml: checkout credentials must not persist")
    if "pull_request_target" in workflow or re.search(r"\bsecrets\s*\.", workflow):
        errors.append(".github/workflows/docs-quality.yml: unsafe trigger or secret reference")
    if re.search(r"(?i)(?:^|[,{\s:])write(?:\s*[,}\n]|$)", workflow):
        errors.append(".github/workflows/docs-quality.yml: write permission is prohibited")
    for line_number, line in enumerate(workflow.splitlines(), start=1):
        if "uses:" in line and not re.search(r"uses:\s+[^@\s]+@[0-9a-f]{40}\s+#\s+v?\d", line):
            errors.append(f".github/workflows/docs-quality.yml:{line_number}: action is not SHA-pinned with version comment")
    return errors


def probe_external_link(url: str, timeout: float = 8.0, attempts: int = 2) -> str | None:
    """Return a safe error category after bounded retries, or None when reachable."""
    headers = {"User-Agent": "Hydra-Core-Docs-Validator/1.0"}
    last_status: int | None = None
    last_error = "network error"
    for attempt in range(attempts):
        for method in ("HEAD", "GET"):
            request = urllib.request.Request(url, headers=headers, method=method)
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    status = int(response.status)
                    if 200 <= status < 400 or status in {401, 403}:
                        return None
                    last_status = status
            except urllib.error.HTTPError as exc:
                last_status = exc.code
                if exc.code in {401, 403}:
                    return None
                if method == "HEAD" and exc.code in {400, 404, 405}:
                    continue
                last_error = f"HTTP {exc.code}"
            except (urllib.error.URLError, TimeoutError, OSError):
                last_error = "network error or timeout"
            if method == "HEAD" and last_status not in {400, 404, 405}:
                break
        if attempt + 1 < attempts:
            time.sleep(0.5 * (attempt + 1))
    return f"HTTP {last_status}" if last_status is not None else last_error


def check_external_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for url in sorted(external_links(root)):
        result = probe_external_link(url)
        if result:
            errors.append(f"external link failed ({result}): {url}")
    return errors


OFFLINE_CHECKS = {
    "canonical": check_canonical_files,
    "markdown": check_markdown,
    "links": check_internal_links,
    "schemas": check_json_and_schemas,
    "boundary": check_public_boundary,
    "posture": check_posture_contract,
    "workflow": check_yaml_and_workflow,
}


def run_offline_checks(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for check in OFFLINE_CHECKS.values():
        errors.extend(check(root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        choices=("all", *OFFLINE_CHECKS.keys(), "freshness", "external"),
        default="all",
        help="Run all deterministic checks or one check family.",
    )
    parser.add_argument(
        "--as-of",
        help="UTC ISO timestamp for freshness checks, or 'now' for current UTC.",
    )
    args = parser.parse_args(argv)

    evaluation_time: datetime | None = None
    if args.as_of:
        try:
            evaluation_time = datetime.now(timezone.utc) if args.as_of == "now" else parse_utc(args.as_of)
        except ValueError:
            parser.error("--as-of must be 'now' or an ISO date-time with timezone")
        if evaluation_time.tzinfo is None:
            parser.error("--as-of must include a timezone")

    if args.check == "all":
        errors = run_offline_checks(ROOT)
        if evaluation_time is not None:
            errors.extend(check_posture_freshness(ROOT, evaluation_time))
        label = "offline public-surface validation"
    elif args.check == "freshness":
        errors = check_posture_freshness(ROOT, evaluation_time)
        label = "public posture freshness"
    elif args.check == "external":
        errors = check_external_links(ROOT)
        label = f"external links ({len(external_links(ROOT))} checked)"
    else:
        errors = OFFLINE_CHECKS[args.check](ROOT)
        label = args.check

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {label} reported {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"PASS: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
