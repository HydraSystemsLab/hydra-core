from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import FormatChecker

from scripts import risk_event_validation as validator


ROOT = Path(__file__).resolve().parents[1]


def valid_event(event_id: str) -> dict[str, object]:
    return {
        "$schema": "../../schemas/risk-event.schema.json",
        "$id": f"urn:hydra:risk-event:{event_id.lower()}",
        "schema_version": "1.0.0",
        "event_id": event_id,
        "occurred_at": "2026-07-01T10:00:00Z",
        "recorded_at": "2026-09-22T12:00:00Z",
        "scope": "PRIVATE_EXECUTION_SCOPE",
        "event_type": "FIX_COMPLETED",
        "reason_code": "CONTROL_BOUNDARY_REPAIRED",
        "action_code": "VALIDATION_HARDENED",
        "public_summary": "A synthetic test record exercises published event collection validation.",
        "historical_context": "This test record has no operational meaning and exists only inside a temporary test repository.",
        "evidence": {
            "tier": "NOT_APPLICABLE",
            "disclosure": "WITHHELD",
            "generated_at": "2026-09-22T11:55:00Z",
            "tested_gate": None,
            "limitations": ["Test fixture only."],
        },
        "public_evidence_refs": [],
        "current_authorization_disclaimer": "Historical event only; not current authorization.",
    }


class PublishedRiskEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "schemas").mkdir()
        schema = ROOT / "schemas/risk-event.schema.json"
        (self.root / "schemas/risk-event.schema.json").write_text(
            schema.read_text(encoding="utf-8"), encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_event(self, relative_path: str, event: dict[str, object]) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(event), encoding="utf-8")

    def findings(self) -> list[str]:
        schema = json.loads((self.root / "schemas/risk-event.schema.json").read_text(encoding="utf-8"))
        return validator.validate_published_events(self.root, schema, FormatChecker())

    def test_discovers_only_year_partitioned_published_events(self) -> None:
        self.write_event("risk-events/2026/HRE-2026-TEST.json", valid_event("HRE-2026-TEST"))
        self.write_event("examples/risk-events/synthetic.json", valid_event("SYNTHETIC-TEST"))

        paths = validator.iter_published_events(self.root)

        self.assertEqual(
            [path.relative_to(self.root).as_posix() for path in paths],
            ["risk-events/2026/HRE-2026-TEST.json"],
        )

    def test_published_event_rejects_example_marker(self) -> None:
        event = valid_event("HRE-2026-TEST")
        event["x-example-only"] = True
        self.write_event("risk-events/2026/HRE-2026-TEST.json", event)

        self.assertIn("published event must not set x-example-only", "\n".join(self.findings()))


if __name__ == "__main__":
    unittest.main()
