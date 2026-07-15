# Failure Modes

This public specification defines conceptual detection, enforcement, safe outcomes, recovery, and residual risk. It does not disclose private thresholds, routes, schemas, or procedures.

Unless a narrower policy applies, unresolved integrity or lifecycle ambiguity results in `AMBIGUOUS`, `DISARMED`, and `RECOVERY_REQUIRED`. Known unauthorized execution paths result in `UNSAFE`, `DISARMED`, and `RECOVERY_REQUIRED`. New exposure is blocked; only explicitly defined containment may remain eligible.

## Duplicate Execution

**Failure:** More than one submission or fill is associated with one authorized intent boundary.

**Detection:** Idempotency keys, acknowledgements, fills, or state transitions show repeated lifecycle activity.

**Enforcement action:** Halt the affected path, disarm its scope, preserve evidence, and block replay.

**Expected safe outcome:** No further duplicate exposure is introduced; defined containment may reduce unresolved exposure.

**Recovery requirement:** Reconcile authoritative order and position state, prove idempotency behavior, and validate restart replay controls.

**Residual risk:** External retries, delayed acknowledgements, or incomplete venue records may preserve uncertainty.

## Broker Or Symbol-Domain Mismatch

**Failure:** An intent, price, contract, or constraint is interpreted in the wrong execution or symbol domain.

**Detection:** Normalized symbol identity, contract specification, precision, session, or data-source domain fails to match the authorized route.

**Enforcement action:** Reject the route and mark trust `AMBIGUOUS` or `UNSAFE` according to known exposure.

**Expected safe outcome:** The mismatched request does not create new exposure.

**Recovery requirement:** Reconcile mappings and specifications, validate normalization, and repeat domain-boundary tests.

**Residual risk:** External specification changes and aliases can evade incomplete mapping inventories.

## Clock Drift

**Failure:** System time diverges enough to invalidate ordering, freshness, expiry, or session decisions.

**Detection:** Trusted UTC, monotonic, and source timestamps disagree outside the applicable control contract.

**Enforcement action:** Block time-sensitive decisions and new exposure; preserve the observed clocks.

**Expected safe outcome:** Stale or misordered information is not treated as current.

**Recovery requirement:** Restore trusted time, reconcile affected event ordering, and revalidate freshness and session gates.

**Residual risk:** Network delay and source-clock error can remain indistinguishable from local drift.

## Timezone Or Session Misalignment

**Failure:** Calendar, daylight-saving, market-session, or timezone interpretation applies the wrong trading window.

**Detection:** Independent calendar checks or replayed boundary cases disagree with the configured session.

**Enforcement action:** Block affected decisions and narrow the scope to observation.

**Expected safe outcome:** No action is taken under an unproved session interpretation.

**Recovery requirement:** Validate timezone sources, calendars, holidays, and boundary cases against the authorized domain.

**Residual risk:** Venue schedule changes or exceptional sessions may not be known in advance.

## Partial-Fill Ambiguity

**Failure:** Filled, remaining, cancelled, or exposed quantity cannot be reconciled.

**Detection:** Order, fill, and position sources disagree or a terminal lifecycle state is missing.

**Enforcement action:** Freeze new exposure, mark the scope `AMBIGUOUS`, and allow only defined containment.

**Expected safe outcome:** Unknown exposure is not compounded.

**Recovery requirement:** Reconcile authoritative fills, orders, and positions; verify any containment and terminal states.

**Residual risk:** Late corrections and external reporting gaps may delay certainty.

## Acknowledgement Or Order-State Ambiguity

**Failure:** Submission, acknowledgement, rejection, cancellation, or terminal order state is unknown or contradictory.

**Detection:** Expected lifecycle events are absent, delayed, duplicated, or inconsistent across authoritative sources.

**Enforcement action:** Halt further submissions on the path and enter `RECOVERY_REQUIRED`.

**Expected safe outcome:** New requests do not stack on unresolved order state.

**Recovery requirement:** Query and reconcile canonical lifecycle state, then validate acknowledgement and retry handling.

**Residual risk:** External systems may remain unavailable or return eventually consistent state.

## Restart Replay Or Idempotency Failure

**Failure:** Restart replays an intent, loses a lock, or cannot prove whether prior work completed.

**Detection:** Checkpoints, idempotency records, persisted state, and authoritative outcomes cannot be reconciled.

**Enforcement action:** Gate startup, keep permission `DISARMED`, and block automatic replay.

**Expected safe outcome:** Restart does not bypass disarm or duplicate prior exposure.

**Recovery requirement:** Reconcile every affected intent and position, prove deduplication, and validate checkpoints before lifecycle normalization.

**Residual risk:** Incomplete persistence or external side effects may prevent full reconstruction.

## Stale Control State

**Failure:** Permission, trust, lifecycle, mode, constraint, or policy state exceeds its validity or version boundary.

**Detection:** Time-to-live, version, signature, authority, or source checks fail.

**Enforcement action:** Treat state as missing, fail closed, and block new exposure.

**Expected safe outcome:** A last-known permissive value is not reused as current.

**Recovery requirement:** Load authoritative current state and validate coherence across every affected layer.

**Residual risk:** A source can be fresh but wrong; freshness is not semantic correctness.

## Feed Stall Or Corruption

**Failure:** Required market, risk, or supervisory input is stale, missing, malformed, or internally inconsistent.

**Detection:** Freshness, sequence, schema, domain, and cross-source checks fail.

**Enforcement action:** Block decisions that rely on the input and disarm any scope that cannot remain trustworthy without it.

**Expected safe outcome:** New exposure is not based on stale or corrupt data.

**Recovery requirement:** Restore and reconcile fresh input, assess the affected interval, and validate downstream state.

**Residual risk:** Correlated sources may repeat the same erroneous data.

## Data Leakage Or Lookahead Contamination

**Failure:** Research or evidence uses information unavailable at decision time or leaks between evaluation partitions.

**Detection:** Time-order, feature lineage, split, replay-integrity, or independent review checks identify contamination.

**Enforcement action:** Quarantine affected evidence and freeze dependent promotion or public claims.

**Expected safe outcome:** Contaminated results do not justify authority or marketing claims.

**Recovery requirement:** Rebuild clean evidence, rerun integrity checks, and correct affected public statements.

**Residual risk:** Subtle shared-data lineage can remain undetected.

## Model-Authority Escalation

**Failure:** A model influences action, size, route, permission, or mode beyond its explicitly approved boundary.

**Detection:** Authority manifests, route checks, decision provenance, or negative tests show an unauthorized effect.

**Enforcement action:** Veto the action, disarm the integration, and classify a known boundary escape as `UNSAFE`.

**Expected safe outcome:** Model output cannot enlarge authority or bypass Guardian.

**Recovery requirement:** Restore the approved boundary, review evidence and failure behavior, and repeat authority tests.

**Residual risk:** Indirect influence through shared features or configuration may be difficult to identify.

## Shadow-To-Live Boundary Escape

**Failure:** A shadow-only scope reaches an order-capable demo or live route.

**Detection:** Environment, destination, credential, route, and mode checks show a forbidden connection or payload path.

**Enforcement action:** Hard-reject the route, disarm the scope, revoke affected capability, and preserve evidence.

**Expected safe outcome:** `SHADOW` produces no order submission.

**Recovery requirement:** Prove route isolation, remove order-capable authority, and repeat negative boundary tests.

**Residual risk:** Misconfiguration outside the evaluated boundary can recreate a route.

## Manual Bypass

**Failure:** A person attempts to override disarm, constraints, lifecycle, mode, or evidence requirements outside authorized containment.

**Detection:** Authorization, audit, configuration, or state history shows an unapproved change or action.

**Enforcement action:** Reject the action, revoke or narrow affected authority, and require incident review.

**Expected safe outcome:** Operator urgency does not silently expand permission.

**Recovery requirement:** Reconcile resulting state, review access and procedure, and validate independent enforcement.

**Residual risk:** Privileged insiders and external systems may retain powers beyond application controls.

## Dashboard Data Leakage

**Failure:** A public or alpha surface exposes private fields, other users' data, protected logic, or unsanitized operational material.

**Detection:** Payload allowlist tests, authorization tests, review, or incident reports identify prohibited content.

**Enforcement action:** Suppress the affected surface, revoke access where needed, and contain further disclosure.

**Expected safe outcome:** The leaking view no longer serves protected material.

**Recovery requirement:** Remove the source field, review payload generation and isolation, assess disclosure, and test sanitized output.

**Residual risk:** Previously viewed, cached, or captured information may not be recoverable.

## Secret Or Configuration Exposure

**Failure:** A secret, token, credential, private endpoint, protected configuration, or account detail enters a public surface.

**Detection:** Pre-publication scans, repository review, provider alerts, or incident reports identify an exposure category.

**Enforcement action:** Revoke or rotate affected authority, contain publication, and avoid repeating the value in diagnostics.

**Expected safe outcome:** The exposed material can no longer authorize new access where revocation is available.

**Recovery requirement:** Complete rotation, access review, history and downstream assessment, and public-boundary validation.

**Residual risk:** Copies, caches, forks, or third-party logs may persist after removal.

## Evidence-Tier Misclassification

**Failure:** Historical, replay, shadow, demo, or live evidence is labelled as a stronger or different class.

**Detection:** Provenance, timing, execution, or metadata review contradicts the displayed tier.

**Enforcement action:** Retract or correct the claim and freeze any dependent promotion.

**Expected safe outcome:** Users are not asked to treat weaker evidence as stronger evidence.

**Recovery requirement:** Reclassify the evidence, restore required metadata, and review dependent decisions and wording.

**Residual risk:** Corrected claims may continue circulating outside controlled surfaces.

## Public-Posture Drift

**Failure:** A changing product or permission statement becomes stale, contradictory, or duplicated outside the canonical posture.

**Detection:** Expiry checks, canonical-field comparison, or documentation validation identifies drift.

**Enforcement action:** Display `UNKNOWN/REVIEW_REQUIRED` and block the stale value from being presented as current.

**Expected safe outcome:** Durable architecture does not become an unverified status page.

**Recovery requirement:** Conduct owner review and update the Markdown and JSON posture records together.

**Residual risk:** External copies and search indexes may retain superseded statements.

## Correlated Infrastructure Failure

**Failure:** Shared data, clock, network, storage, identity, or supervisory dependencies impair multiple supposedly isolated scopes.

**Detection:** Concurrent anomalies share dependency, timing, or failure signatures beyond expected independence.

**Enforcement action:** Broaden containment beyond local engines and disarm every scope that depends on untrusted infrastructure.

**Expected safe outcome:** Local isolation assumptions do not hide system-wide risk.

**Recovery requirement:** Identify the common dependency, validate independent recovery, and reassess failure-domain boundaries.

**Residual risk:** Hidden shared dependencies may survive the initial analysis.

## Correlated Engine Loss

**Failure:** Multiple engines lose or degrade together because of shared market exposure or assumptions rather than infrastructure alone.

**Detection:** Concurrent loss, disarm, or abnormal behavior exceeds the documented independence assumption.

**Enforcement action:** Apply portfolio-level restriction or disarm rather than treating each event as isolated.

**Expected safe outcome:** Aggregate damage is constrained by the broader authority domain.

**Recovery requirement:** Reassess correlation, exposure aggregation, and the evidence supporting engine independence.

**Residual risk:** Correlation can rise abruptly in unseen regimes.

## Duplicate Datasets As Independent Opportunities

**Failure:** Repeated, overlapping, or derived records are counted as independent evidence.

**Detection:** Dataset lineage, hash, time-range, event-identity, and dependency analysis finds overlap.

**Enforcement action:** Invalidate combined counts and freeze claims that depend on false independence.

**Expected safe outcome:** Sample size is not inflated by duplicate evidence.

**Recovery requirement:** Deduplicate, recompute independent opportunity counts, and revise interpretation and public results.

**Residual risk:** Near-duplicate or derived datasets may evade simple matching.

## Governance Rule

Detection without enforcement is incomplete. Enforcement without recovery evidence is incomplete. A safe outcome is bounded containment, not proof that no loss or residual risk exists.

Related documents:

- [State Model](../architecture/state-model.md)
- [Threat Model](threat-model.md)
- [Risk Event Ledger Policy](risk-event-ledger-policy.md)
- [Public Evidence Policy](public-evidence-policy.md)
