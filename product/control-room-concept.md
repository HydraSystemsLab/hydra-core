# Hydra Control Room Concept

> **Conceptual placeholder — this is not a production screenshot and does not represent live account state or live performance.**

Hydra Control Room is the planned user-facing interface for legible system posture, forward-shadow decisions, evidence classification, and feedback. No real production dashboard screenshot currently exists.

## Conceptual Layout

The following text wireframe is a labelled design aid, not captured product output:

```text
+------------------------------------------------------------------+
| HYDRA CONTROL ROOM — CONCEPT                updated: <UTC time>   |
+----------------------+----------------------+--------------------+
| System posture       | Guardian verdict    | Operating mode     |
| <trust/permission/   | <gate + reason>      | <OBSERVE/SHADOW>   |
| lifecycle>           |                      |                    |
+----------------------+----------------------+--------------------+
| Market/regime context (public-safe, source and freshness shown)  |
+------------------------------------------------------------------+
| Research status      | Recent shadow decisions | Veto reasons   |
+----------------------+-------------------------+----------------+
| Shadow equity — EVIDENCE: FORWARD SHADOW — NOT LIVE PERFORMANCE  |
+------------------------------------------------------------------+
| Feed freshness | public-safe health | incidents | provenance     |
+------------------------------------------------------------------+
```

Placeholder values must use angle-bracket labels or obviously synthetic data. A concept preview must never use real account identifiers, balances, orders, or unlabelled performance values.

## Intended Panels

### System Posture

Displays the effective trust, permission, lifecycle, and mode values for the disclosed scope. If source state is missing, contradictory, or stale, it displays the restrictive effective posture rather than guessing.

### Guardian Verdict

Names the tested gate, result, reason category, timestamp, and scope. A verdict such as `PASS`, `AMBER`, `RED`, or `FROZEN` is incomplete unless the tested gate is named.

### Operating Mode

Separately displays `OBSERVE_ONLY`, `SHADOW`, `DEMO`, or `LIVE`. The planned initial external view is `SHADOW`; it must not imply order submission.

### Market And Regime Context

Shows sanitized context, its source classification, timestamp, normalization state, and freshness. It excludes protected model features and actionable private logic.

### Engine Or Research Status

Shows public-safe research lifecycle and availability labels without engine rules, protected parameters, or an inference of approval.

### Shadow Decisions And Veto Reasons

Shows recent forward-shadow decisions, blocks, and explanation categories with timestamps and evidence tier. It does not publish actionable real-time entries or exits.

### Shadow Equity

Shows a clearly labelled paper or forward-shadow series only when the evidence policy metadata is available. It must state that the series is not live performance and must not merge evidence tiers.

### Freshness, Health, Incidents, And Provenance

Shows feed freshness, public-safe runner or bridge health, unresolved incident indicators, last-updated time, and source provenance. Health must not be presented as strategy quality or public execution permission.

## Proposed Public-Safe Fields

- disclosed scope
- trust state and observation time
- permission state and observation time
- lifecycle state
- operating mode
- effective execution eligibility
- named Guardian gate and verdict
- public reason code and explanation
- feed age and freshness classification
- sanitized dependency health
- decision timestamp and evidence class
- evidence generation time and limitations
- unresolved public incident count
- data provenance classification
- last-reconciled and last-updated timestamps

## Prohibited Public Or Alpha Payload Fields

- secrets, tokens, or broker credentials
- internal paths, hostnames, endpoints, or private repository locations
- account IDs, balances, private account configuration, or order payloads
- unsanitized exceptions, stack traces, logs, or report paths
- private strategy rules, protected parameters, thresholds, or model features
- protected schemas or private execution wiring
- unsupported performance claims or mixed-tier track records
- actionable real-time entries or exits before legal and regulatory review

Payloads should be generated from an explicit public-safe allowlist. Hiding fields in the interface is not sufficient if the authenticated response still contains them.

## Three Distinct Surfaces

| Surface | Audience | Data posture | Non-claim |
| --- | --- | --- | --- |
| Marketing-site concept preview | Public | Static, conceptual, and unmistakably labelled | Not a product screenshot, current system state, or performance display |
| Authenticated alpha Control Room | Invited testers | Read-only, sanitized, forward-shadow, user-isolated | No broker connection, order submission, or live execution |
| Internal operator terminal | Authorized private operators | Private operational data under separate controls | Not a public product surface and not suitable for public payload reuse |

## Placeholder-Media Requirements

Any future image, video, or mockup must:

- carry the conceptual-placeholder disclaimer on or immediately beside the media
- use synthetic or redacted values
- avoid mimicking a verified live account
- identify the evidence class of any chart
- undergo public/private boundary review before publication

The concept must be replaced or revalidated when a real authenticated alpha interface exists; it must not drift into being represented as a production screenshot.
