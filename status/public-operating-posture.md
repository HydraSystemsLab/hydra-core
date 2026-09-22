# Public Operating Posture

> Dated public summary — not a real-time execution authorization.

**As of:** 2026-09-22 08:02:19 UTC

**Review due:** 2026-10-22 08:02:19 UTC, or earlier if any review trigger below occurs

**Stale after:** 2026-10-22 08:02:19 UTC

This is the only canonical location for changing public product posture. Durable architecture explains what the system is designed to permit; this page says only what Hydra Systems currently approves for public communication.

## Approved Public Summary

| Field | Public posture |
| --- | --- |
| Hydra Core phase | Pre-v1 |
| Hydra Quant phase | Private-alpha preparation |
| External availability | Closed; invite-only preparation |
| Planned initial external access | Read-only; `SHADOW` operating mode; forward-shadow evidence only |
| Public-user broker/account connection | Disabled |
| Public-user order submission | Disabled |
| Public-user live execution | Disabled |
| Hydra Control Room | Conceptual and in development |

No real production dashboard screenshot currently exists. Any public layout must be an unmistakably labelled concept or placeholder.

## Permission Boundaries

Public-user permission and internal operational permission are separate authority domains. This page discloses public-user permission only.

- Private engine-level permission is not disclosed here.
- Internal operational permission cannot be inferred from this page.
- An internal mode or historical live event does not grant access to a public user.
- Public-user execution remains disabled even if a private component is technically healthy or operationally ready.

Strategy existence, runner health, system operability, and execution readiness do not prove strategy edge. A private implementation also does not prove that a public product is available.

## Evidence And Release Context

- [Public Evidence Policy](../governance/public-evidence-policy.md)
- [Hydra Quant Private-Alpha Contract](../product/hydra-quant-private-alpha.md)
- [Release Posture](../governance/release-posture.md)
- [Versioning Policy](../governance/versioning-policy.md)

No profit guarantee is made, and no progression from shadow to demo or live is promised.

## Review And Staleness Policy

Review is required by the review-due time or earlier if Hydra Core maturity, Hydra Quant phase, external availability, public-user mode, a public-user permission, Control Room availability, or a referenced policy materially changes.

Once `stale_after` is reached without a reviewed replacement, consumers must display `UNKNOWN/REVIEW_REQUIRED`. They must not present the last recorded values as current, infer continuity, or silently extend the expiry. A review may confirm the same posture, but confirmation must update the dated Markdown and JSON records together.

The next review is triggered by time or material change. It is not a launch date.

## Machine-Readable Record

The equivalent structured record is [public-operating-posture.json](public-operating-posture.json), validated by the [public operating posture schema](../schemas/public-operating-posture.schema.json). Its `source_commit` identifies the source snapshot reviewed when this posture was prepared; it is not a self-referential hash of the commit containing the JSON file.
