# Published Risk Events

This directory contains owner-approved structured risk-event records. Records
are selected public governance history, not a complete incident register,
trade journal, performance record, or current authorization.

Each event is stored under its occurrence year and validates against the
[risk-event schema](../schemas/risk-event.schema.json). Synthetic examples
remain separate under [`examples/risk-events`](../examples/risk-events/README.md).

## Date Semantics

`occurred_at` records the evidence-supported UTC time of the event, decision,
or state transition. It is not replaced by the publication date. `recorded_at`
records when the reviewed public document was prepared and therefore may be
later. The containing year is always the UTC year from `occurred_at`. A
public-safe `x-operational-date` may preserve a different local operating date
when that distinction matters.

The chronological [ledger index](../governance/risk-event-ledger.md#structured-v1-records)
shows each occurrence timestamp. Published records are immutable; corrections
are new linked records.
