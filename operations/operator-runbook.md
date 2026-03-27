# Operator Runbook

This runbook defines the public operating expectations for human supervision around a governed Hydra system.
It is principles-first and intentionally does not expose private implementation procedures.

The operator's job is not to force continuity.
The operator's job is to preserve trustworthy control.

## Safe Startup Expectations

Before execution is allowed to resume, an operator should be able to confirm at a high level that:

- supervisory control is present and authoritative
- the system is not in a known disarm or recovery-required condition
- observability surfaces are current enough to support decision-making
- recent state is coherent enough to explain whether prior actions were completed, rejected, or left unresolved
- execution permission, if granted, is governed rather than assumed

Startup is not merely process availability.
It is the re-establishment of trustworthy operating state.

## What A Disarm Means

A disarm means permission to execute has been withdrawn.
It should be treated as a safety outcome, not as an inconvenience.

Operationally, a disarm means:

- no new exposure should be introduced
- the triggering condition must be understood before resumption is considered
- the burden of proof has shifted from "why stop" to "why resume"

Disarm is evidence that the control model is still active.

## When Not To Rearm

Do not rearm when:

- system state remains ambiguous, stale, or contradictory
- the cause of the disarm is not yet understood
- observability cannot explain current exposure or recent control decisions
- a restart has occurred without full reconciliation
- execution outcomes, rejects, or prior intents remain unresolved
- pressure to resume is based on missed opportunity rather than validated safety

Elapsed time is not a rearm condition.
Operator confidence is not a rearm condition.

## What Should Be Visible Before Execution Resumes

Before execution resumes, the operator should have enough truth surfaced to answer:

- what state the system is currently in
- why it entered that state
- whether any exposure, intent, or constraint state remains unresolved
- whether supervisory controls are active and authoritative
- what changed between disarm and proposed rearm

If those answers are not available, the system is not ready to resume.

## Why Operator Truth Surfaces Matter

Operators should not be asked to infer safety from silence.
They need visible, current, and coherent control evidence.

Truth surfaces matter because they:

- reduce the chance of rearming into ambiguity
- make disarm and veto behavior explainable
- preserve accountability for supervisory decisions
- separate verified recovery from hopeful recovery

Dashboards, logs, and alerts are useful only if they support authoritative interpretation of system state.
Visibility that cannot support a go or no-go decision is incomplete.

## When To Trigger Governance Recording Or Ledger Review

An operator should trigger governance recording or ledger review when an event materially affects:

- disarm, veto, pause, or rearm semantics
- supervisory authority or control boundaries
- required observability for proving safe state
- recovery expectations after a risk or integrity event
- containment behavior for a meaningful failure class

Examples include:

- a disarm caused by ambiguous execution or supervisory state
- a recovery path that required tighter validation than before
- a failure that exposed a gap in the public control model
- an architecture hardening change that moved authority between layers

Routine activity, expected losses, or ordinary strategy maintenance do not automatically belong in governance recording.
The threshold is governance significance, not operational noise.

Related documents:

- [Operating Principles](operating-principles.md)
- [State Model](../architecture/state-model.md)
- [Risk Event Ledger Policy](../governance/risk-event-ledger-policy.md)
