# Operator Runbook

This public runbook defines supervisory expectations without exposing private commands, paths, accounts, endpoints, or execution procedures.

The operator's job is not to force continuity. It is to preserve trustworthy control.

## Before Any Execution Becomes Eligible

For the named scope, an operator must be able to verify:

- trust is currently `SAFE`
- permission is explicitly `ARMED`
- lifecycle is `NORMAL`
- the configured mode permits the requested action and destination
- every required gate passes on current state
- no stricter higher-layer restriction applies
- observability can reconcile recent intents, exposure, and lifecycle outcomes

A running process, green health check, restored feed, or valid strategy intent is insufficient.

## Safe Startup

Startup establishes process availability; it does not establish execution eligibility. After interruption, treat unresolved prior intent, exposure, locks, mode, or permission as `AMBIGUOUS`, `DISARMED`, and `RECOVERY_REQUIRED` until authoritative reconciliation proves otherwise.

Diagnostics may remain available. New exposure remains blocked.

## Responding To A Disarm

On disarm:

- stop new exposure in the affected scope
- preserve state and evidence
- identify the triggering authority, gate, and reason
- determine whether broader correlated scope is affected
- permit only explicitly defined containment actions
- record recovery conditions before considering restoration

The burden of proof changes from “why stop” to “why resume.”

## Contradiction And Missing State

When sources disagree, apply the intersection of permitted actions and use the more restrictive posture. Do not average verdicts, prefer the newest permissive value without authority checks, or fill a missing value from operator expectation.

Stale state is missing state. If a public posture record expires, display `UNKNOWN/REVIEW_REQUIRED` rather than its old values as current.

## Recovery Review

Before clearing `RECOVERY_REQUIRED`, verify at a public-safe conceptual level:

- the cause and scope are understood
- exposure, orders, fills, and intents reconcile where applicable
- control, data, time, and mode state are coherent and fresh
- enforcement and idempotency controls have been tested as required
- evidence is preserved and corrections are recorded
- residual risk and affected dependencies are reviewed
- the proper authority approves lifecycle normalization

Restart, elapsed time, and operator confidence are not recovery evidence.

### Interval-Bound Recovery

For a transport or observation interruption, bind the exact outage interval,
incident, scope, account authority, source identity, and code identities. Across
that interval, reconcile positions, pending orders, orders, and deals between
the broker's authoritative history, durable ledger, Guardian records, and
source evidence. Account for manual and unrelated activity as well as
strategy-owned activity.

Distinguish historical terminal records from outstanding work. Every affected
intent must have a known terminal outcome or remain unresolved; current flat
inventory alone cannot prove that no execution occurred. Preserve accumulated
losses, applicable high-water marks, limits, and anchors rather than resetting
or reconstructing a more permissive day.

Recovery requires a fresh source acknowledgment that binds the validated
decision and identities. Do not reuse another incident's receipt or substitute
a fabricated broker reconnect. A maintenance transport interruption retains
its own classification and does not alter the broker-disconnect contract.

## Rearm Review

Rearm is separate from recovery. Before changing `DISARMED` to `ARMED`, verify lifecycle is already `NORMAL`, trust is `SAFE`, the destination and mode are correct, every gate passes, and no higher-layer disarm remains.

Record who or what authority granted rearm, its scope, its evidence, and its time. Rearm does not authorize a specific trade or mode promotion.

## Mode Promotion

Never promote mode because a target metric was reached, a testing window ended, or a runner remained healthy. Promotion requires explicit evidence classification, authority boundaries, public/private review, failure testing, and a governance decision.

`ARMED` in `SHADOW` remains shadow-only. It cannot authorize a demo or live order.

## Operator Truth Surfaces

An operator surface should show, for the disclosed scope:

- each state axis and observation time
- effective action eligibility
- named gate verdicts and reasons
- freshness and provenance
- unresolved exposure or lifecycle ambiguity
- active incidents and recovery conditions
- last reconciliation and decision authority

Dashboards support decisions only when their values reconcile with canonical state. Visibility is not enforcement.

## Governance Recording

Review the [Risk Event Ledger Policy](../governance/risk-event-ledger-policy.md) when an event materially changes enforcement, authority, containment, recovery, rearm, mode promotion, or safety-critical evidence. Routine trades and strategy tuning do not automatically qualify.

Related documents:

- [State Model](../architecture/state-model.md)
- [Failure Modes](../governance/failure-modes.md)
- [Threat Model](../governance/threat-model.md)
- [Operating Principles](operating-principles.md)
