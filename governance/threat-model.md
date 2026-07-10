# Threat Model

## Purpose And Status

This is a public design-level threat model for Hydra Core governance and the planned Hydra Quant private alpha. It helps reviewers reason about authority, data, evidence, and user boundaries.

It is not formal verification, a penetration-test report, a third-party security assessment, regulatory approval, certification, or a guarantee of security.

## Protected Assets

- Guardian supervisory authority and policy integrity
- trust, permission, lifecycle, and mode state
- exposure, intent, order, acknowledgement, fill, and recovery integrity
- credentials, configuration, accounts, and access authority
- private strategy logic, thresholds, features, schemas, and research artefacts
- evidence provenance, classification, and canonical ledgers
- dated public posture and release truth
- authenticated-alpha user identity, isolation, and revocation
- sanitized public and alpha payloads

## Trust Boundaries

| Boundary | Primary concern |
| --- | --- |
| Public governance ↔ private implementation | Public documents must govern without leaking protected implementation or implying availability. |
| Strategy/model ↔ Guardian | Intent or model output must not create supervisory authority. |
| Guardian ↔ execution | A supervisory allow is still subject to state, mode, destination, and execution gates. |
| Execution ↔ external venue/data domain | Identity, symbol, time, lifecycle, and external truth may differ or fail. |
| Operator ↔ supervisory controls | Privilege and urgency must not bypass disarm, recovery, or mode boundaries. |
| Canonical ledgers ↔ sanitized views | Public/dashboard values must reconcile without carrying protected fields. |
| Authenticated alpha user ↔ other users/private internals | Authorization, isolation, read-only, and revocation must hold. |
| CI/public repository ↔ private material | Publication checks must prevent paths, secrets, statuses, and protected artefacts from crossing. |

## Actors And Failure Sources

- authorized operators making mistakes or exceeding authority
- invited testers sharing access or content
- external attackers seeking credentials, data, or control
- compromised dependencies or accounts
- faulty models, strategies, integrations, or dashboards
- stale, corrupt, duplicated, or misclassified data
- external venue, feed, clock, network, and infrastructure failures
- documentation editors unintentionally publishing dynamic or private truth

The model includes both malicious action and ordinary failure. Intent does not change the required containment.

## In-Scope Threats

- unauthorized authority escalation or route access
- `SHADOW` reaching an order-capable destination
- lower-layer override of Guardian or lifecycle restrictions
- replay, duplicate execution, and order-state ambiguity
- stale, missing, contradictory, or forged control state
- symbol, domain, clock, timezone, and session mismatch
- credentials, private configuration, or protected logic entering public surfaces
- dashboard authorization failure or cross-user leakage
- evidence contamination, duplication, selective omission, or tier inflation
- public posture becoming stale while still displayed as current
- correlated dependency failures defeating isolation assumptions
- failed access revocation or copied invitation credentials
- health or readiness being represented as edge, performance, or public permission

## Alpha-Specific Threats

- invite or credential sharing
- screenshots exposing private-alpha or protected information
- broken object- or user-level authorization
- payloads containing hidden internal fields even when the interface hides them
- stale or mislabelled forward-shadow decisions
- dashboard values drifting from canonical ledgers
- failure to revoke access promptly and completely
- alpha wording implying live execution, advice, or guaranteed signals
- a read-only interface calling an order-capable endpoint
- one tester receiving another tester's state or feedback

## Out-Of-Scope Claims

This public model does not publish or claim to assess:

- private strategy quality or protected strategy rules
- undisclosed infrastructure topology or account configuration
- exhaustive implementation-specific attack paths
- legal, regulatory, tax, or investment suitability
- third-party venue security beyond its effect on Hydra's boundaries
- guaranteed resistance to every insider, supply-chain, or zero-day threat

An item being out of public scope does not mean it is unimportant or unreviewed privately.

## Mitigation Model

- independent Guardian authority and restrictive state composition
- separate trust, permission, lifecycle, and operating-mode axes
- fail-closed handling of missing, stale, or contradictory state
- explicit mode and destination isolation
- idempotency, lifecycle reconciliation, and recovery gating
- public-safe allowlists rather than denylist-only sanitization
- evidence-tier metadata, provenance, and non-combination rules
- posture expiry with `UNKNOWN/REVIEW_REQUIRED` behavior
- least-privilege authenticated access and tested revocation
- repository validation for links, schemas, private boundaries, dynamic posture, and placeholders
- append/correction governance history rather than silent revision

Mitigations must be tested in their actual scope. The presence of a control in a document is not evidence that an implementation is operating correctly.

## State And Failure Mapping

| Threat condition | Default public state response | Failure-mode mapping |
| --- | --- | --- |
| Unresolved integrity, acknowledgement, or exposure state | `AMBIGUOUS`, `DISARMED`, `RECOVERY_REQUIRED`; block new exposure | Partial-fill ambiguity; acknowledgement ambiguity; restart replay |
| Known boundary bypass or unauthorized route | `UNSAFE`, `DISARMED`, `RECOVERY_REQUIRED`; contain and revoke | Model-authority escalation; shadow-to-live escape; manual bypass |
| Known impaired but bounded dependency | `DEGRADED`; block new exposure except defined containment | Feed stall; clock drift; correlated infrastructure |
| Stale public posture | Public truth becomes `UNKNOWN/REVIEW_REQUIRED`; freeze current claims | Public-posture drift |
| Security disclosure affecting user access | Revoke affected access and require scoped incident recovery | Dashboard leakage; secret/config exposure |
| Contaminated or misclassified evidence | Quarantine evidence and freeze dependent promotion | Data leakage; tier misclassification; duplicate datasets |

The mapping is a default, not a substitute for event-specific authority and recovery conditions. A public-truth incident does not silently assert an unrelated private execution state unless the affected control boundary is shared.

## Public/Private Boundary

Public reporting may describe the failure class, affected public claim, state effect, enforcement outcome, evidence classification, and residual risk. It must not publish secrets, accounts, private paths, endpoints, order payloads, protected schemas, model features, or actionable strategy logic.

Private evidence may be withheld. Withholding must be labelled and cannot be used to imply that a stronger claim has been proved.

## Residual Risks

- unknown shared dependencies can defeat intended isolation
- privileged compromise can reach controls below the public model
- external systems may return delayed, inconsistent, or incomplete truth
- sanitization may miss newly introduced protected fields
- sparse or regime-limited evidence can be misinterpreted even when labelled
- public copies can outlive corrections and revocations
- implementation defects can prevent documented controls from operating as designed

Defined unsafe actions are intended to be mechanically blocked while the documented boundaries and enforcement controls are operating as designed. Residual risk remains.

Related documents:

- [Failure Modes](failure-modes.md)
- [State Model](../architecture/state-model.md)
- [Control Boundaries](../architecture/control-boundaries.md)
- [Security Policy](../SECURITY.md)
