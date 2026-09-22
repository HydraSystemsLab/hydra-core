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

    def write_published(self, event: dict[str, object], filename: str | None = None) -> None:
        event_id = str(event["event_id"])
        self.write_event(f"risk-events/2026/{filename or event_id}.json", event)

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

    def test_rejects_duplicate_event_id(self) -> None:
        event = valid_event("HRE-2026-DUPLICATE")
        self.write_published(event)
        self.write_published(event, filename="HRE-2026-OTHER")

        self.assertIn("duplicate published event_id", "\n".join(self.findings()))

    def test_rejects_filename_that_differs_from_event_id(self) -> None:
        self.write_published(valid_event("HRE-2026-IDENTITY"), filename="HRE-2026-WRONG")

        self.assertIn("filename must equal event_id", "\n".join(self.findings()))

    def test_rejects_recorded_time_before_occurrence(self) -> None:
        event = valid_event("HRE-2026-TIME")
        event["recorded_at"] = "2026-06-30T23:59:59Z"
        self.write_published(event)

        self.assertIn("recorded_at precedes occurred_at", "\n".join(self.findings()))

    def test_rejects_event_stored_outside_occurrence_year(self) -> None:
        event = valid_event("HRE-2026-YEAR")
        event["occurred_at"] = "2025-12-31T23:59:59Z"
        self.write_published(event)

        self.assertIn("directory year differs from occurred_at year", "\n".join(self.findings()))

    def test_rejects_unknown_relationship_target(self) -> None:
        event = valid_event("HRE-2026-CORRECTION")
        event["correction_of"] = "HRE-2026-MISSING"
        self.write_published(event)

        self.assertIn(
            "correction_of does not identify an earlier published event",
            "\n".join(self.findings()),
        )

    def test_rejects_self_relationship(self) -> None:
        event = valid_event("HRE-2026-SELF")
        event["supersedes"] = "HRE-2026-SELF"
        self.write_published(event)

        self.assertIn("supersedes must not reference the same event", "\n".join(self.findings()))

    def test_rejects_forward_relationship(self) -> None:
        earlier = valid_event("HRE-2026-EARLIER")
        earlier["supersedes"] = "HRE-2026-LATER"
        later = valid_event("HRE-2026-LATER")
        later["occurred_at"] = "2026-07-02T10:00:00Z"
        self.write_published(earlier)
        self.write_published(later)

        self.assertIn(
            "supersedes does not identify an earlier published event",
            "\n".join(self.findings()),
        )

    def test_rejects_two_relationship_semantics_on_one_event(self) -> None:
        original = valid_event("HRE-2026-ORIGINAL")
        correction = valid_event("HRE-2026-CORRECTION")
        correction["occurred_at"] = "2026-07-02T10:00:00Z"
        correction["correction_of"] = "HRE-2026-ORIGINAL"
        correction["supersedes"] = "HRE-2026-ORIGINAL"
        self.write_published(original)
        self.write_published(correction)

        self.assertIn(
            "must not set both correction_of and supersedes",
            "\n".join(self.findings()),
        )

    def test_rejects_missing_local_evidence_reference(self) -> None:
        event = valid_event("HRE-2026-MISSING-REF")
        event["public_evidence_refs"] = ["../../governance/missing.md"]
        self.write_published(event)

        self.assertIn("public evidence reference does not exist", "\n".join(self.findings()))

    def test_rejects_local_evidence_reference_that_escapes_repository(self) -> None:
        event = valid_event("HRE-2026-ESCAPE")
        event["public_evidence_refs"] = ["../../../outside.md"]
        self.write_published(event)

        self.assertIn("public evidence reference escapes repository", "\n".join(self.findings()))

    def test_accepts_withheld_evidence_without_public_reference(self) -> None:
        event = valid_event("HRE-2026-WITHHELD")
        self.write_published(event)

        self.assertEqual(self.findings(), [])


if __name__ == "__main__":
    unittest.main()
