# Versioning Policy

Hydra Core is currently pre-v1.
That status is intentional.

This repository documents doctrine, architecture, governance, and operating expectations for a risk-first system whose public governance surface is still being stabilized.

## What Pre-v1 Means

Pre-v1 means the public structure and language are converging, but the project does not yet claim that its governance model is fully settled.

In practice, pre-v1 means:

- document structure may still be reorganized for clarity
- terminology may still be tightened where ambiguity remains
- governance coverage may expand as additional failure classes are formalized
- public release discipline matters more than feature breadth

It does not mean governance is optional.
It means the public standard is still being refined before it is declared stable.

## What Could Qualify Hydra Core For V1 Later

Hydra Core would be a candidate for v1 when the public governance layer is stable enough that a serious operator can rely on it as the durable description of Hydra's control model.

That would typically require:

- stable doctrine around risk, disarm, and fail-closed behavior
- stable architectural descriptions of Core, Quant, and Guardian responsibilities
- documented treatment of major failure classes and recovery expectations
- a risk event ledger practice that demonstrates consistent governance evidence
- fewer structural changes to core public concepts between releases

Reaching v1 is not primarily about publishing more code.
It is about stabilizing the public governance contract.

V1 would not imply frozen strategies, fixed engine logic forever, or an end to parameter changes.
It would indicate that the architecture, doctrine, and governance model have become stable enough to serve as a durable public reference.

## What Belongs In The Risk Event Ledger

The risk event ledger should record changes or events that materially affect enforcement, containment, disarm behavior, supervisory control, or the interpretation of system-level safety.

Examples include:

- new disarm classes or changes to disarm semantics
- enforcement fixes after a constraint violation or integrity failure
- changes to system-wide gating, risk-domain boundaries, or recovery controls
- observability changes required to validate supervisory state
- verified rearm after a material enforcement event

Examples that do not belong in the ledger include:

- normal strategy tuning
- parameter adjustments within an existing control model
- day-to-day optimization that does not alter enforcement or safety posture
- routine editorial cleanup, wording improvements, or document restructuring that does not change governance meaning

## Change Classification Before Release

Every change to Hydra Core should be classified before release.
The purpose is to avoid mixing cosmetic edits with governance-bearing edits.

Use the following routing rules:

- **Editorial change:** wording, formatting, ordering, typo fixes, or structural cleanup that does not change doctrine, enforcement expectations, authority boundaries, or recovery semantics
- **Clarifying governance change:** language that makes an existing rule easier to interpret without changing the underlying control model; this usually does not require a ledger entry, but the editor should be able to explain why the meaning is unchanged
- **Governance change:** any update that changes what is enforced, what must be observed, when disarm or rearm is expected, how failure classes are treated, or where supervisory authority sits; this should be reflected in the risk event ledger
- **Architecture-significant change:** any update that changes the public responsibility boundary between Core, Quant, Guardian, execution, monitoring, or recovery; this should be treated as governance-significant even if no code is published here

If a change cannot be confidently kept in the editorial or clarifying class, it should be treated as governance-significant by default.

## Release Discipline

Before publishing a change set, the editor should be able to answer:

- does this change alter governance meaning or only presentation
- does this change introduce, remove, tighten, or relax an enforcement expectation
- does this change affect disarm, veto, pause, recovery, or rearm semantics
- does this change move a responsibility boundary between public system components
- does this change require a corresponding risk event ledger entry

If those questions cannot be answered cleanly, the change set is not yet ready for release.

## What Should Remain Stable

The following should become increasingly stable as Hydra Core matures:

- risk-first doctrine
- fail-closed operating bias
- the separation of responsibilities between Core, Quant, and Guardian
- the requirement that enforcement leave observable evidence
- the expectation that recovery follows verification
- the public description of supervisory authority and operating constraints

## What May Evolve

The following may continue to evolve during pre-v1 and, where justified, after v1:

- strategy logic inside Hydra Quant
- engine-level filters, market-specific logic, and decision heuristics
- parameters and thresholds that do not change the underlying control model
- how failure classes are grouped and described
- how public architecture is presented for clarity
- event schema refinements that improve governance visibility
- additional governance documents covering new supervisory concerns

Changes in these areas should preserve the underlying control philosophy even when the presentation becomes sharper.

Related documents:

- [Failure Modes](failure-modes.md)
- [Risk Event Ledger](risk-event-ledger.md)
- [System Overview](../architecture/system-overview.md)
