# Hydra Quant Private-Alpha Contract

This document is the canonical public operating contract for the planned Hydra Quant private alpha. It describes intended scope and governance expectations; it is not a claim that the alpha is currently available and it is not a binding legal agreement.

Current availability is defined by the dated [Public Operating Posture](../status/public-operating-posture.md).

## Purpose

The private alpha is intended to:

- test usability and decision legibility
- test evidence labels and provenance displays
- test reconciliation between dashboard values and canonical ledgers
- test operational reliability, freshness handling, and recovery behavior
- collect qualified feedback from serious testers
- accumulate forward-shadow evidence without representing it as execution evidence

The alpha is not proof of guaranteed profitability, stable returns, positive expectancy, or readiness for public execution.

## Intended Users

The intended founding cohort is limited to:

- serious systematic traders
- technical operators
- prop-risk-aware testers
- users willing to evaluate shadow software without demanding guaranteed signals

Invitation suitability does not imply investment suitability, personalized advice, or entitlement to future access.

## Planned Initial Scope

Everything in this section is **planned until the dated public posture explicitly says it is available**.

- approximately 3–5 founding testers
- invite-only access
- a read-only authenticated Hydra Control Room
- Guardian posture and operating-mode visibility
- public-safe market and regime context
- engine or research status without private logic
- forward-shadow decisions
- paper or shadow portfolio results labelled with their evidence class
- decision and veto explanations
- feed freshness and public-safe system health
- evidence classification and provenance
- feedback and incident reporting
- an approximately 30-day initial testing window

Read-only user access and `SHADOW` operating mode are distinct controls: read-only limits what a user can do; `SHADOW` prevents the system from submitting orders for that user.

## Explicit Exclusions

The planned initial alpha includes:

- no public-user live trading
- no public-user order submission
- no public-user broker or account connection
- no broker credential collection
- no copy-trading guarantee
- no minimum monthly return or other return commitment
- no personalized financial advice
- no private strategy source, parameters, thresholds, or model features
- no claim that every research engine is approved
- no claim that green system health means positive expectancy
- no silent transition to `DEMO` or `LIVE`
- no promise of permanent free access
- no promised future paid-beta price

No progression from shadow to demo or live is promised.

## Tester Operating Expectations

These are operational expectations for a controlled test. Future legal terms, privacy terms, and any other binding conditions must be reviewed separately before access is granted.

- Access may be withdrawn to protect users, evidence integrity, or the system.
- Shadow or paper results must never be represented as live execution.
- Bugs, stale values, contradictions, and reconciliation failures should be reported promptly.
- Credentials and access links must not be shared.
- Screenshots or recordings may require review if they expose private-alpha information, other users, or protected fields.
- Alpha terms and functionality may change before beta.
- Feedback may inform product development without guaranteeing adoption of a suggestion.
- Testers must not attempt to bypass read-only, authorization, or sanitization boundaries.

Security concerns must follow the private route in [SECURITY.md](../SECURITY.md), not a public issue.

## Alpha-To-Beta Gates

Each gate is necessary where applicable, but the list is not sufficient by itself and does not create an automatic promotion:

- authenticated access has been reviewed
- user authorization and isolation have been reviewed
- dashboard values reconcile with canonical ledgers
- evidence tiers are unambiguous throughout the user surface
- public/private leakage review finds no unresolved material exposure
- health and freshness failures fail closed
- incident, containment, and recovery processes have been exercised
- access revocation has been exercised
- real tester usage and retention are acceptable for the claims being considered
- forward-shadow evidence supports only the specific claims being made
- no unresolved critical security issue remains
- user-facing wording has been reviewed for truth and evidence classification

A beta decision requires an explicit governance review, updated release materials, and a current public posture. Meeting a metric or reaching the end of a test window does not promote the product automatically.

## Claim Separation

The alpha must keep these claims independent:

1. system operability
2. runner health
3. execution readiness
4. strategy edge
5. public-user permission

A healthy dashboard may support an operability claim. It cannot, by itself, support an edge or permission claim.

## Related Contracts

- [Public Operating Posture](../status/public-operating-posture.md)
- [Public Evidence Policy](../governance/public-evidence-policy.md)
- [Multi-Axis State Model](../architecture/state-model.md)
- [Control Room Concept](control-room-concept.md)
- [Security Policy](../SECURITY.md)
