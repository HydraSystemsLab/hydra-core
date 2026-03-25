# Failure Modes

This document defines public governance expectations for selected failure classes.
It is intentionally conceptual.
It describes detection, enforcement, and expected safe outcomes without exposing private implementation details.

Hydra assumes failures will occur.
The relevant governance question is whether they are detected early enough and contained safely enough.

## Duplicate Execution

**Failure:** More than one execution occurs from what should have been a single authorized opportunity.

**Detection:** Execution records, acknowledgements, or state transitions indicate duplicated fills, repeated submissions, or replay against the same intent boundary.

**Enforcement action:** Halt the affected engine or execution path, preserve evidence, and require verification before rearm.

**Expected safe outcome:** Further duplicate exposure is prevented and the failure is contained to the smallest practical domain.

## Stale Or Ambiguous System State

**Failure:** The system cannot reliably determine current risk, execution, or supervisory state.

**Detection:** State disagreement between layers, expired control state, contradictory observability records, or missing confirmation of prior actions.

**Enforcement action:** Fail closed, reject new execution, and move to a paused or disarmed state until state can be re-established.

**Expected safe outcome:** The system stops acting under uncertainty rather than compounding uncertainty with new exposure.

## Feed Stall

**Failure:** Required market or supervisory inputs stop updating or become too stale to trust.

**Detection:** Liveness checks fail, expected update cadence is broken, or feed freshness falls outside acceptable bounds.

**Enforcement action:** Block new decisions that rely on the stalled feed and disarm if continued operation would rely on untrustworthy inputs.

**Expected safe outcome:** The system does not open or extend exposure using stale information.

## Execution Stall

**Failure:** Intents are generated but execution acknowledgements, rejects, or terminal states do not arrive as expected.

**Detection:** Expected execution lifecycle events are missing, delayed beyond tolerance, or left in unresolved intermediate states.

**Enforcement action:** Freeze further execution on the affected path, elevate supervisory review, and require recovery validation before resuming.

**Expected safe outcome:** The system avoids stacking unknown exposure on top of unresolved execution state.

## Restart Ambiguity

**Failure:** After restart or recovery, the system cannot prove whether prior intent, exposure, locks, or disarm conditions were fully resolved.

**Detection:** Recovery checks cannot reconcile persisted state, observability records, and current operating context into one coherent view.

**Enforcement action:** Keep the system gated, prevent automatic rearm, and require explicit safe-state validation before execution resumes.

**Expected safe outcome:** Restart does not become a bypass around disarm, constraint, or reconciliation logic.

## Correlated Engine Loss

**Failure:** Multiple engines degrade together in a way that suggests shared infrastructure, shared assumptions, or shared market stress is defeating isolation.

**Detection:** Concurrent or near-concurrent loss, disarm, or abnormal behavior across independent engines exceeds expected independence.

**Enforcement action:** Escalate from local containment to broader supervisory restrictions, including pausing related engines or system-wide disarm if needed.

**Expected safe outcome:** Correlation is treated as a risk event and the system contains portfolio-level damage instead of assuming local failures are independent.

## Governance Notes

- Detection without enforcement is insufficient.
- Rearm should follow verified recovery, not elapsed time.
- When safe state cannot be demonstrated, the expected operating result is inactivity.

Related documents:

- [Risk Doctrine](../doctrine/risk-doctrine.md)
- [Operating Principles](../operations/operating-principles.md)
- [Risk Event Ledger](risk-event-ledger.md)
