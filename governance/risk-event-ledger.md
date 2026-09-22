# Hydra Risk Event Ledger

> **Selected public governance history — not current authorization.**

This ledger is not a trade journal and not a performance record. Entries describe governance posture at the recorded time. Historical `LIVE_*` wording is not current authorization. Current public posture lives only in the dated [Public Operating Posture](../status/public-operating-posture.md).

Corrections are appended or explicitly annotated; history is not silently rewritten. Private evidence may be withheld, and absence of a public entry does not prove absence of a private incident.

This page contains published Structured V1 records backed by authoritative JSON and a preserved legacy Markdown archive. Neither format discloses current engine permission, public-user permission, a complete incident history, or a track record.

## When To Add An Entry

Add an entry when a release or operational event changes any of the following:

- enforcement behavior
- disarm, pause, or rearm semantics
- supervisory authority or control boundaries
- observability required to validate safe state
- recovery gating after a material risk or integrity event

Do not add an entry for purely editorial changes that leave governance meaning unchanged.

## Format Transition

The first section contains published Structured V1 records generated from the
authoritative JSON files under [`risk-events/YYYY/`](../risk-events/README.md).
Each JSON record retains its event ID and complete public fields.

The later legacy archive preserves the original February–June 2026 Markdown
entries. Those entries predate Structured V1 and lack event IDs, exact
timestamps, state axes, and evidence references; none of those missing facts
are inferred or invented here. Synthetic examples remain documentation fixtures
and never become ledger history.

## Structured V1 Records

Records are ordered chronologically from oldest to newest by `occurred_at`,
with `recorded_at` and `event_id` as deterministic tie-breakers. `occurred_at`
is the evidence-supported UTC time of the event or transition. `recorded_at` is
when the public record was prepared and may be later.

<!-- BEGIN GENERATED STRUCTURED EVENT INDEX -->

| Date (UTC) | Event | Public summary | Details |
| --- | --- | --- | --- |
| `2026-07-09 20:14:28` | Stale runtime artifact retirement | Stale runtime artifacts were removed from operational authority and retained only as historical material. | [JSON](../risk-events/2026/HRE-2026-07-STALE-RUNTIME-ARTIFACT-RETIREMENT.json) |
| `2026-07-11 09:39:48` | Private digital operational repair | Execution provenance, single-writer behavior, idempotency, and ambiguous-outcome retention were hardened. | [JSON](../risk-events/2026/HRE-2026-07-PRIVATE-DIGITAL-OPERATIONAL-REPAIR.json) |
| `2026-07-25 09:08:11` | Risk plane nonrouting recovery | Risk-plane recovery was constrained to a non-routing state ineligible for execution and promotion. | [JSON](../risk-events/2026/HRE-2026-07-RISK-PLANE-NONROUTING-RECOVERY.json) |
| `2026-08-26 11:02:17.026052` | Legacy runtime authority removed | A legacy execution-capable runtime was disabled and removed from operational authority. | [JSON](../risk-events/2026/HRE-2026-08-LEGACY-RUNTIME-AUTHORITY-REMOVED.json) |
| `2026-08-27 11:43:13.799408` | Gateway timestamp integrity repair | Invalid backward source time was quarantined and normalized inside a read-only market-data scope. | [JSON](../risk-events/2026/HRE-2026-08-GATEWAY-TIMESTAMP-INTEGRITY-REPAIR.json) |
| `2026-09-12 00:54:11` | Account bound guardian admission | Admission began requiring account-bound Guardian state, inventory, durable reservations, and explicit operator controls. | [JSON](../risk-events/2026/HRE-2026-09-ACCOUNT-BOUND-GUARDIAN-ADMISSION.json) |
| `2026-09-15 07:38:11` | Heartbeat continuity invalidation | Source loss and observation gaps began invalidating same-day readiness while retaining their causes for recovery. | [JSON](../risk-events/2026/HRE-2026-09-HEARTBEAT-CONTINUITY-INVALIDATION.json) |
| `2026-09-18 15:59:31` | Supervisory enforcement promotion | A supervisory evaluator moved from shadow observation to enforced admission veto while native sizing authority remained separate. | [JSON](../risk-events/2026/HRE-2026-09-SUPERVISORY-ENFORCEMENT-PROMOTION.json) |
| `2026-09-20 15:47:13` | Risk policy constraint correction | Obsolete fixed constraints were retired while applicable proportional limits and historical risk latches remained enforced. | [JSON](../risk-events/2026/HRE-2026-09-RISK-POLICY-CONSTRAINT-CORRECTION.json) |
| `2026-09-21 02:07:41` | Connection continuity disarm | Connection continuity ambiguity invalidated current readiness and required evidence-bound recovery. | [JSON](../risk-events/2026/HRE-2026-09-CONNECTION-CONTINUITY-DISARM.json) |
| `2026-09-21 07:57:39` | Evidence bound connection recovery | Flat inventory, complete interval history, preserved risk anchors, identity, and a fresh native acknowledgment qualified the recovery decision. | [JSON](../risk-events/2026/HRE-2026-09-EVIDENCE-BOUND-CONNECTION-RECOVERY.json) |
| `2026-09-21 14:07:41` | Response framing continuity disarm | Response-framing ambiguity created a separate continuity incident and invalidated current readiness. | [JSON](../risk-events/2026/HRE-2026-09-RESPONSE-FRAMING-CONTINUITY-DISARM.json) |
| `2026-09-21 15:27:29` | Response framing recovery | A sealed receipt verified reconciliation and continuity recovery for the response-framing incident. | [JSON](../risk-events/2026/HRE-2026-09-RESPONSE-FRAMING-RECOVERY.json) |
| `2026-09-21 16:00:00` | Shadow sizing authority violation | A shadow sizing suggestion incorrectly replaced the native candidate presented to an enforced admission identity check. | [JSON](../risk-events/2026/HRE-2026-09-SHADOW-SIZING-AUTHORITY-VIOLATION.json) |
| `2026-09-21 23:23:25` | Maintenance transport disarm | An authorized listener pause caused a transport timeout and correctly forced evidence-bound recovery. | [JSON](../risk-events/2026/HRE-2026-09-MAINTENANCE-TRANSPORT-DISARM.json) |
| `2026-09-22 07:02:21` | Maintenance transport recovery | Exact outage, inventory, complete history, terminal-request, risk-anchor, identity, and fresh-acknowledgment evidence supported same-day recovery. | [JSON](../risk-events/2026/HRE-2026-09-MAINTENANCE-TRANSPORT-RECOVERY.json) |
| `2026-09-22 07:07:21` | Native sizing boundary repair | The enforced supervisor was corrected to evaluate the exact native volume candidate while a separate sizing suggestion remained shadow-only. | [JSON](../risk-events/2026/HRE-2026-09-NATIVE-SIZING-BOUNDARY-REPAIR.json) |
| `2026-09-22 07:07:36` | Maintenance transport rearm | Following evidenced recovery, intended entry, management, and operator controls were restored with normal lifecycle and armed permission. | [JSON](../risk-events/2026/HRE-2026-09-MAINTENANCE-TRANSPORT-REARM.json) |

<!-- END GENERATED STRUCTURED EVENT INDEX -->

Run `python scripts/render_risk_event_index.py` after changing authoritative
event JSON. The public-surface validator fails when this generated index is
stale.

---

## Legacy archive: February–June 2026

### Legacy Allowed EVENT_TYPE Values

`DISARM | FIX_COMPLETED | REARM | ENGINE_PAUSED | CONSTRAINT_VIOLATION | MANUAL_INTERVENTION | RISK_LIMIT_BREACH`

---

### 2026-02-01 — BTCUSD_D

**EVENT_TYPE:** DISARM
**REASON:** TRAILING_STOP_VALIDATION_INCOMPLETE
**ACTION:** TRADING_HALTED
**STATUS:** FIX_UNDER_DEVELOPMENT

---

### 2026-02-04 — BTCUSD_D

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** TRAILING_STOP_VALIDATION_VERIFIED
**ACTION:** CODE_PATCHED_AND_VERIFIED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-05 — BTCUSD_D

**EVENT_TYPE:** REARM
**REASON:** TRAILING_STOP_FIX_DEPLOYED
**ACTION:** TRADING_RESUMED
**STATUS:** LIVE_ON_FUNDED_ACCOUNT

---

### 2026-02-05 — AUDJPY_E

**EVENT_TYPE:** ENGINE_PAUSED
**REASON:** VALIDATION_FAILURE_IN_RESEARCH
**ACTION:** ENGINE_HALTED
**STATUS:** OFFLINE_FOR_REDESIGN

---

### 2026-02-09 — BTCUSD_D

**EVENT_TYPE:** CONSTRAINT_VIOLATION
**REASON:** MULTIPLE_EXECUTIONS_FROM_SINGLE_SIGNAL
**ACTION:** ENGINE_HALTED
**STATUS:** INVESTIGATION_IN_PROGRESS

---

### 2026-02-10 — BTCUSD_D

**EVENT_TYPE:** MANUAL_INTERVENTION
**REASON:** MANUAL_EXIT_DETECTED
**ACTION:** REVIEW_REQUIRED
**STATUS:** PROCESS_UPDATE_PENDING

---

### 2026-02-11 — BTCUSD_D

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** SINGLE_EXECUTION_GUARDRAIL_IMPLEMENTED
**ACTION:** CODE_PATCHED_AND_VERIFIED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-11 — BTCUSD_D

**EVENT_TYPE:** REARM
**REASON:** SINGLE_EXECUTION_GUARDRAIL_DEPLOYED
**ACTION:** TRADING_RESUMED
**STATUS:** LIVE_UNDER_UPDATED_GUARDRAILS

---

### 2026-02-13 — BTCUSD_D

**EVENT_TYPE:** RISK_LIMIT_BREACH
**REASON:** LOT_SIZE_OVERRIDE
**ACTION:** ACCOUNT_STOPPED
**STATUS:** LOT_SIZE_ENFORCEMENT_REQUIRED

---

### 2026-02-15 — BTCUSD_D

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** LOT_SIZE_ENFORCEMENT_MOVED_TO_SYSTEM_LAYER
**ACTION:** CODE_PATCHED_AND_VERIFIED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-15 — BTCUSD_D

**EVENT_TYPE:** REARM
**REASON:** LOT_SIZE_ENFORCEMENT_DEPLOYED
**ACTION:** TRADING_RESUMED
**STATUS:** LIVE_UNDER_ENFORCED_SIZING

---

### 2026-02-17 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** PER_ENGINE_LOSS_GUARDIAN_IMPLEMENTED
**ACTION:** RISK_DOMAINS_ISOLATED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-17 — SYSTEM

**EVENT_TYPE:** REARM
**REASON:** PER_ENGINE_GUARDIANS_DEPLOYED
**ACTION:** SYSTEM_RESUMED
**STATUS:** LIVE_UNDER_ISOLATED_RISK_DOMAINS

---

### 2026-02-18 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** EVENT_SCHEMA_UPDATED
**ACTION:** OBSERVABILITY_IMPROVED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-18 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** TIMEZONE_ALIGNMENT_ACROSS_ENGINES
**ACTION:** TIME_HANDLING_STANDARDIZED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-02-19 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** GATING_BEHAVIOR_STANDARDIZED_ACROSS_ENGINES
**ACTION:** EXECUTION_GATES_STANDARDIZED
**STATUS:** LIVE_UNDER_CONSISTENT_GATING

---

### 2026-02-19 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** SESSION_BLOCKERS_VALIDATION_CORRECTED
**ACTION:** SESSION_GATING_STANDARDIZED
**STATUS:** LIVE_UNDER_CORRECT_SESSION_CONTROLS

---

### 2026-02-24 — XAUUSD_A

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** XAU_STOP_LOSS_EDGE_CASE_HANDLING_REFINED
**ACTION:** SL_VALIDATION_HARDENED
**STATUS:** LIVE_UNDER_UPDATED_SL_CONTROLS

---

### 2026-02-24 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** TIMEZONE_EDGE_CASE_ALIGNMENT_REFINED
**ACTION:** TIME_HANDLING_HARDENED
**STATUS:** LIVE_UNDER_STRICT_TIME_CONTROLS

---

### 2026-02-26 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** GATING_EDGE_CASE_VALIDATION_REFINED
**ACTION:** EXECUTION_GATES_HARDENED
**STATUS:** LIVE_UNDER_REINFORCED_GATING

---

### 2026-02-27 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** SESSION_BLOCKER_EDGE_CASE_CORRECTION
**ACTION:** SESSION_GATING_REINFORCED
**STATUS:** LIVE_UNDER_STRICT_SESSION_CONTROLS

---

### 2026-03-03 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** GUARDIAN_STALE_LOCK_RESOLVED
**ACTION:** LOCK_STATE_VALIDATION_HARDENED
**STATUS:** LIVE_UNDER_VERIFIED_GUARDIAN_STATE

---

### 2026-03-03 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** EVENT_SCHEMA_EXTENDED_FOR_GUARDIAN_STATE_VALIDATION
**ACTION:** OBSERVABILITY_LAYER_UPDATED
**STATUS:** READY_FOR_DEPLOY

---

### 2026-06-03 — ML_REGIME

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** REGIME_CLASSIFICATION_CONTEXT_REQUIRED
**ACTION:** REGIME_GUARD_FAIL_CLOSED_BEHAVIOR_HARDENED
**STATUS:** NO_AUTONOMOUS_EXECUTION_AUTHORITY

---

### 2026-06-20 — FEED_HEALTH

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** STALE_FEED_COULD_BE_MISREAD_AS_NO_SIGNAL
**ACTION:** FRESH_BAR_AND_BRIDGE_HEALTH_CHECKS_REQUIRED_BEFORE_SIGNAL_INTERPRETATION
**STATUS:** RECOVERY_GATED_ON_FRESH_DATA

---

### 2026-06-24 — ML_GUARDIAN

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** MODEL_AUTHORITY_BOUNDARY_REQUIRED
**ACTION:** ML_RESTRICTED_TO_SHADOW_META_FILTER
**STATUS:** NO_LIVE_ROUTING_AUTHORITY

---

### 2026-06-24 — B5

**EVENT_TYPE:** ENGINE_PAUSED
**REASON:** PROMOTION_EVIDENCE_INSUFFICIENT
**ACTION:** KEPT_SHADOW_NO_SEND
**STATUS:** RESEARCH_ONLY_PENDING_MORE_EVIDENCE

---

### 2026-06-25 — BTC_C15396

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** LIVE_REPLAY_PARITY_WARMUP_MISMATCH
**ACTION:** LOOKBACK_AND_PARITY_VALIDATION_HARDENED
**STATUS:** LIVE_UNDER_PARITY_MONITORING

---

### 2026-06-26 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** LIVE_POSTURE_VISIBILITY_INSUFFICIENT
**ACTION:** OPERATOR_BRIEF_CONTROL_ROOM_AND_PROOF_PACK_ADDED
**STATUS:** LIVE_UNDER_EXPANDED_OBSERVABILITY

---

### 2026-06-27 — BTC_RISK_DOMAIN

**EVENT_TYPE:** ENGINE_PAUSED
**REASON:** NON_APPROVED_LANE_ORDER_CAPABILITY_DETECTED
**ACTION:** NON_APPROVED_LANES_QUARANTINED
**STATUS:** LIVE_AUTHORITY_REMOVED_PENDING_EVIDENCE

---

### 2026-06-30 — SYSTEM

**EVENT_TYPE:** FIX_COMPLETED
**REASON:** ACCOUNT_ACTIVITY_DEADLINE_VISIBILITY_REQUIRED
**ACTION:** FUNDED_INACTIVITY_SENTINEL_ADDED_TO_OPERATOR_BRIEF_AND_CONTROL_ROOM
**STATUS:** OPERATOR_CONTROLLED_ACTIVITY_RISK_MONITORING
