# Risk Event Ledger Policy

This policy governs which events qualify for selected public governance history and how records are appended, corrected, structured, and sanitized. Release maturity belongs in [Release Posture](release-posture.md); version semantics belong in [Versioning Policy](versioning-policy.md).

The ledger is not a trade journal, research notebook, complete incident register, or performance record.

## Qualifying Events

An event generally qualifies when it materially changes or tests:

- enforcement, veto, pause, disarm, or rearm behavior
- supervisory authority or a control boundary
- operating-mode authority or promotion
- recovery conditions after risk, integrity, or ambiguity
- evidence required to prove safety-critical state
- containment for a meaningful failure class
- public governance interpretation of one of those controls

Routine trades, fills, expected losses, parameter tuning, strategy optimization, ordinary maintenance, and purely editorial changes do not automatically qualify.

The threshold is governance significance, not operational volume. When significance is uncertain, seek owner review; do not fabricate an event merely to document a repository change.

## Selected Public History

Public records may be a sanitized subset of private governance evidence. Each public entry must be true within its disclosed scope and must label evidence that is partial, withheld, or not applicable.

- Private evidence may be withheld.
- Absence of a public entry does not prove absence of a private incident.
- A public entry does not prove completeness of investigation or permanent resolution.
- Historical permission or `LIVE_*` wording is not current authorization.
- Current public-user posture is sourced only from the dated public posture record.

## Append-Only Rule

Once published, an event remains part of the historical record unless removal is required to contain sensitive information or comply with an overriding obligation. Normal factual correction is append-only:

1. publish a new structured correction record
2. reference the earlier `event_id` through `correction_of` or `supersedes`
3. explain the corrected public interpretation
4. preserve the original record with an explicit annotation where practical

Do not rewrite history to improve marketing or convert a historical state into current authorization.

Legacy Markdown entries have no event IDs. Do not invent IDs or timestamps for them. A future correction may cite a precise legacy heading in public evidence text without pretending that heading was a V1 identifier.

## Structured V1

Structured V1 begins prospectively with the first owner-approved event recorded after schema adoption. A V1 record must:

- validate against [risk-event.schema.json](../schemas/risk-event.schema.json)
- use one of the retained event types
- use UTC date-time values for occurrence and recording
- identify a sanitized scope, reason code, action code, and public summary
- separate historical context from current authorization
- classify evidence and disclosure
- include public evidence references or explain why none are public
- include before/after state only when supported by evidence
- carry the required current-authorization disclaimer

The schema contract is documented in [Risk Event Schema](risk-event-schema.md).

## Correction And Supersession

`correction_of` means a later record corrects a factual or interpretive defect while preserving the earlier event. `supersedes` means a later governance decision replaces an earlier policy or posture for its defined scope.

Neither field deletes history. Neither implies current authorization outside the later record's scope and time.

## Public/Private Review

Before publication, review each record for:

- credentials, secrets, accounts, balances, and broker configuration
- private paths, hosts, endpoints, repositories, reports, or logs
- order payloads and private execution wiring
- protected strategy rules, parameters, thresholds, features, and schemas
- actionable real-time entries or exits
- unsupported performance or authorization inference

Sanitize or withhold protected evidence. Do not replace it with invented identifiers, links, times, transitions, or stronger prose.

## Extension Rules

V1 extensions use an `x-...` property defined by the schema. Extensions must be public-safe scalar data or arrays of public-safe scalar data. They may not weaken required fields, override core semantics, carry private payloads, or become an unreviewed parallel schema.

## Review Responsibilities

An editor proposing a ledger event should be able to state:

- why the event is governance-significant
- which failure class, boundary, or transition it affects
- what evidence supports every published fact
- whether a correction or supersession relationship exists
- what remains private or uncertain
- why the wording cannot be read as current authorization or performance

Related documents:

- [Risk Event Ledger](risk-event-ledger.md)
- [Risk Event Schema](risk-event-schema.md)
- [Failure Modes](failure-modes.md)
- [Public Evidence Policy](public-evidence-policy.md)
