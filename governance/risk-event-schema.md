# Risk Event Schema

Structured risk-event V1 is a prospective, sanitized public record format. It does not retroactively convert the legacy Markdown ledger.

The normative machine-readable contract is [schemas/risk-event.schema.json](../schemas/risk-event.schema.json).

## Required Core Fields

| Field | Contract |
| --- | --- |
| `$schema` | Repository-relative path to the V1 schema |
| `$id` | Stable public identifier for this record; may be a repository-relative URI reference |
| `schema_version` | `1.0.0` |
| `event_id` | Owner-approved public identifier; unique within the public ledger |
| `occurred_at` | Supported UTC event time |
| `recorded_at` | Supported UTC record-publication time, not earlier than occurrence |
| `scope` | Sanitized public scope; never an account, host, or private path |
| `event_type` | One of the retained legacy-compatible event types |
| `reason_code` | Public-safe uppercase reason category |
| `action_code` | Public-safe uppercase enforcement or governance action |
| `public_summary` | Bounded public explanation without protected detail |
| `historical_context` | What the record meant at its recorded time |
| `evidence` | Evidence tier, disclosure, tested gate, limitations, and generation time |
| `public_evidence_refs` | Sanitized URI references; may be empty when disclosure explains why |
| `current_authorization_disclaimer` | Exact schema-required non-authorization statement |

## Optional State

`before_state` and `after_state` may record supported trust, permission, lifecycle, and mode values. Omit an unsupported axis; never infer it from narrative or retrofit it into a legacy entry.

State is scoped and follows the [Multi-Axis State Model](../architecture/state-model.md). A before/after tuple is historical evidence, not a command or current status.

## Evidence Classification

Evidence tier uses the five classes in the [Public Evidence Policy](public-evidence-policy.md), plus `NOT_APPLICABLE` for a governance-only record. Disclosure is one of `PUBLIC`, `PARTIAL`, `WITHHELD`, or `NOT_APPLICABLE`.

An empty `public_evidence_refs` array is valid only when the evidence disclosure and limitations make the absence clear. It does not support a stronger claim.

## Corrections

Use `correction_of` to correct a prior structured record and `supersedes` when a later governance decision replaces an earlier one in its stated scope. Both preserve history.

## Extensions

Extension names must match `x-...`. Values are limited to public-safe scalars or arrays of scalars. Extensions cannot override core fields, loosen validation, or carry private implementation, credentials, accounts, paths, endpoints, payloads, schemas, or research details.

## Legacy Boundary

Existing Markdown entries remain legacy records because they lack supported event IDs, exact timestamps, multi-axis state, and structured evidence. No conversion date or missing fact is invented.

The [synthetic examples](../examples/risk-events/README.md) demonstrate schema shape only. They are not events and must never be copied into the historical ledger as facts.
