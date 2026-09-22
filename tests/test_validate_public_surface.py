from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from scripts import validate_public_surface as validator


ROOT = Path(__file__).resolve().parents[1]


class PublicSurfaceValidatorTests(unittest.TestCase):
    def test_passing_fixture_has_no_boundary_findings(self) -> None:
        path = ROOT / "tests/fixtures/pass/public-copy.md"
        self.assertEqual(validator.boundary_violations(path, path.read_text(encoding="utf-8"), ROOT), [])

    def test_failing_fixture_exercises_boundary_categories(self) -> None:
        fixture = json.loads((ROOT / "tests/fixtures/fail/boundary-cases.json").read_text(encoding="utf-8"))
        findings: list[str] = []
        for case in fixture["cases"]:
            synthetic_text = "".join(case["parts"])
            findings.extend(validator.boundary_violations(Path(f"{case['name']}.md"), synthetic_text, ROOT))
        combined = "\n".join(findings)
        self.assertIn("forbidden private absolute path", combined)
        self.assertIn("unlabeled placeholder marker", combined)
        self.assertIn("dynamic engine/status identifier", combined)
        self.assertIn("likely credential material", combined)

    def test_internal_link_checker_rejects_missing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("# Test\n\n[Missing](absent.md)\n", encoding="utf-8")
            findings = validator.check_internal_links(root)
        self.assertEqual(len(findings), 1)
        self.assertIn("missing local link target", findings[0])

    def test_fenced_link_and_heading_are_not_rendered(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "README.md"
            path.write_text(
                "# Visible\n\n```markdown\n# Hidden\n[Missing](absent.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(validator.check_internal_links(root), [])
            self.assertNotIn("hidden", validator.heading_anchors(path))

    def test_duplicate_heading_anchors_are_numbered(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "headings.md"
            path.write_text("# One\n\n## Repeated\n\n## Repeated\n", encoding="utf-8")
            anchors = validator.heading_anchors(path)
        self.assertIn("repeated", anchors)
        self.assertIn("repeated-1", anchors)

    def test_boundary_scan_covers_unlisted_extensions_and_skips_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / "repo"
            root.mkdir()
            private_path = "/" + "ho" + "me" + "/operator/report"
            (root / "leak.sh").write_text(private_path, encoding="utf-8")
            outside = base / "outside.txt"
            outside.write_text(private_path, encoding="utf-8")
            (root / "outside-link").symlink_to(outside)
            findings = validator.check_public_boundary(root)
        self.assertEqual(len(findings), 1)
        self.assertIn("leak.sh", findings[0])

    def test_schema_check_handles_malformed_instances_safely(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "schemas").mkdir()
            (root / "status").mkdir()
            (root / "examples/risk-events").mkdir(parents=True)
            for name in ("public-operating-posture.schema.json", "risk-event.schema.json"):
                source = ROOT / "schemas" / name
                (root / "schemas" / name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
            (root / "status/public-operating-posture.json").write_text("{", encoding="utf-8")
            (root / "examples/risk-events/broken.json").write_text("{", encoding="utf-8")
            findings = validator.check_json_and_schemas(root)
        self.assertGreaterEqual(len(findings), 2)
        self.assertTrue(all("Traceback" not in finding for finding in findings))

    def test_screenshot_media_requires_exact_disclaimer(self) -> None:
        text = "".join(
            (
                "# Preview\n\n<",
                "img src=\"control-",
                "room.png\" alt=\"Control Room\">\n",
            )
        )
        findings = validator.boundary_violations(Path("preview.md"), text, ROOT)
        self.assertEqual(len(findings), 1)
        self.assertIn("exact conceptual disclaimer", findings[0])

    def test_workflow_policy_rejects_job_permission_override(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            workflow_path = root / ".github/workflows/docs-quality.yml"
            workflow_path.parent.mkdir(parents=True)
            workflow = (ROOT / ".github/workflows/docs-quality.yml").read_text(encoding="utf-8")
            workflow = workflow.replace(
                "    timeout-minutes: 10",
                "    permissions: {id-token: write}\n    timeout-minutes: 10",
            )
            workflow_path.write_text(workflow, encoding="utf-8")
            findings = validator.check_yaml_and_workflow(root)
        self.assertTrue(any("must not override permissions" in finding for finding in findings))

    def test_posture_freshness_fails_after_stale_after(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "status").mkdir()
            (root / "status/public-operating-posture.json").write_text(
                json.dumps({"stale_after": "2026-08-10T00:00:00Z"}),
                encoding="utf-8",
            )
            now = datetime.fromisoformat("2026-08-10T00:00:01+00:00")
            findings = validator.check_posture_freshness(root, now)
        self.assertIn("public posture is stale", "\n".join(findings))

    def test_posture_freshness_passes_at_stale_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "status").mkdir()
            (root / "status/public-operating-posture.json").write_text(
                json.dumps({"stale_after": "2026-08-10T00:00:00Z"}),
                encoding="utf-8",
            )
            now = datetime.fromisoformat("2026-08-10T00:00:00+00:00")
            self.assertEqual(validator.check_posture_freshness(root, now), [])

    def test_recovery_contract_names_required_interval_evidence(self) -> None:
        runbook = (ROOT / "operations/operator-runbook.md").read_text(encoding="utf-8")
        for phrase in (
            "outage interval",
            "positions, pending orders, orders, and deals",
            "historical terminal records",
            "fresh source acknowledgment",
        ):
            self.assertIn(phrase, runbook)

    def test_shadow_advice_cannot_change_live_candidate(self) -> None:
        boundaries = (ROOT / "architecture/control-boundaries.md").read_text(encoding="utf-8")
        self.assertIn(
            "A shadow advisory value cannot replace or resize an authoritative live candidate",
            boundaries,
        )

    def test_repository_offline_contract_passes(self) -> None:
        self.assertEqual(validator.run_offline_checks(ROOT), [])


if __name__ == "__main__":
    unittest.main()
