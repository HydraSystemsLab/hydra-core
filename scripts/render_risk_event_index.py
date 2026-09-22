#!/usr/bin/env python3
"""Render or verify the public structured risk-event ledger index."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from scripts.risk_event_validation import check_structured_event_index, write_structured_event_index
except ModuleNotFoundError:  # direct script execution
    from risk_event_validation import check_structured_event_index, write_structured_event_index


ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the rendered index is stale.")
    args = parser.parse_args(argv)
    if args.check:
        findings = check_structured_event_index(ROOT)
        if findings:
            for finding in findings:
                print(f"ERROR: {finding}")
            return 1
        print("PASS: structured risk-event index is current")
        return 0
    write_structured_event_index(ROOT)
    print("UPDATED: governance/risk-event-ledger.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
