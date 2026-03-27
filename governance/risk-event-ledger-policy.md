# Risk Event Ledger Policy

This policy defines what the Hydra Risk Event Ledger is for and what it is not for.
The ledger exists to preserve governance evidence around material risk, enforcement, and control-boundary events.

It is not a trade journal.
It is not a research notebook.
It is not a changelog for routine tuning.

## Purpose

The ledger should record events and changes that materially affect:

- enforcement behavior
- disarm, pause, veto, or rearm semantics
- supervisory authority and control boundaries
- recovery gating after risk or integrity events
- observability required to prove safe state

The ledger helps show how Hydra hardens over time.
It provides governance memory for the moments when the operating model was tested, tightened, or changed.

## What Belongs In The Ledger

Qualifying entries generally include:

- system disarms caused by meaningful risk or integrity events
- verified fixes to enforcement gaps or control failures
- rearm decisions following material disarm conditions
- architecture changes that tighten supervisory authority or containment boundaries
- observability changes required to validate safety-critical state
- recovery policy changes after restart, ambiguity, or execution-state failures

The common test is whether the event changes how a serious operator should interpret Hydra's safety posture.

## What Does Not Belong

The ledger usually should not include:

- ordinary trades, fills, or performance outcomes
- normal parameter tuning within an unchanged control model
- routine strategy optimization and research iteration
- editorial document cleanup
- naming, wording, or structure changes that do not alter governance meaning
- day-to-day operational noise that does not affect supervisory interpretation

Normal parameter tuning and routine strategy optimization usually do not belong because they adjust decision quality, not governance meaning.
Unless they alter enforcement, containment, authority, or recovery semantics, they are not ledger events.

## Examples Of Qualifying Events

Examples that usually qualify:

- a new disarm class is introduced for a previously uncontained failure
- an execution ambiguity leads to a hard fail-closed change
- rearm is tightened so restart alone is no longer sufficient
- observability is extended so supervisory state can be validated instead of assumed
- control authority moves from an engine-local mechanism to a supervisory layer
- correlated engine failure leads to stronger containment boundaries

## Significance Thresholds

An event should be considered ledger-worthy when one or more of the following is true:

- it changes what the system will now block, halt, veto, or disarm
- it changes what evidence is required before rearm
- it changes which layer has authority over a safety-critical decision
- it changes how a known failure mode is contained
- it hardens the architecture after a material risk, integrity, or ambiguity event

If the editor cannot explain why an event is below these thresholds, it should be treated as governance-significant by default.

## Relationship To Architecture Hardening

The ledger is part of architecture hardening discipline.
Hardening is not only code change.
It is the process of making unsafe behavior harder to permit and easier to explain after the fact.

When Hydra tightens a control boundary, strengthens fail-closed behavior, improves supervisory evidence, or narrows recovery permission, the ledger should reflect that change.
This creates continuity between doctrine, architecture, and operational governance.

## Relationship To Governance

The ledger supports governance by answering questions such as:

- when did supervisory expectations materially change
- which failures caused architecture or policy hardening
- what must now be true before execution is considered safe again
- which events were treated as system-level rather than local noise

Its role is historical and interpretive.
It preserves the reasons behind enforcement changes, not just the fact that files changed.

Related documents:

- [Hydra Risk Event Ledger](risk-event-ledger.md)
- [Versioning Policy](versioning-policy.md)
- [Failure Modes](failure-modes.md)
