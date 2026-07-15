# Risk Doctrine

## North Star

Hydra prioritizes survivability and bounded failure over activity.

The control objective is to mechanically block defined unsafe actions while the documented boundaries and enforcement controls are operating as designed. This is an engineering objective, not a guarantee of safety, security, or profit.

## Principles

1. Losses are expected.
2. Defined exposure and loss limits must be enforced.
3. Escalation after loss is prohibited.
4. Risk controls must be able to block actions, not merely report them.
5. Missing, stale, or contradictory control state fails closed.
6. Recovery follows reconciliation and verification.
7. No trade is a valid output.

Failure to enforce a defined limit is a control incident. It must trigger containment, evidence preservation, and governed recovery appropriate to the affected scope.

## Mechanically Enforced Boundaries

Within documented scope and while controls operate as designed, the system should block:

- new exposure with missing or invalid required protective constraints
- unauthorized risk escalation after loss
- bypass of an applicable disarm or recovery condition
- new exposure after a hard risk or integrity event
- exposure beyond applicable enforced limits
- order submission from `OBSERVE_ONLY` or `SHADOW`

These boundaries reduce defined risks. They do not eliminate market risk, implementation defects, external failure, or residual risk.

## No Trade

Hydra does not participate unless the full state invariant and every required gate pass for the requested action. Inactivity is an acceptable governed result.

## Accountability

Material actions, vetoes, disarms, containment decisions, lifecycle changes, rearms, and promotions should leave enough evidence to explain their scope, authority, reason, and limitations.
