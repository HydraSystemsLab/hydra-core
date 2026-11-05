# Hydra Core

**Hydra is automated trading infrastructure built around one idea: a trading
system should be judged by how it fails, not only by how it makes money.**

Hydra Core is the public, documented front of Hydra Systems. It explains what
Hydra is, how it controls risk, and what it records when something goes wrong.
The trading strategies themselves stay private.

[What Hydra is](overview/what-is-hydra.md) · [How risk is controlled](overview/how-risk-is-controlled.md) · [Track record policy](overview/track-record.md) · [FAQ](overview/faq.md) · [Current status](status/public-operating-posture.md) · [Hydra Systems](https://hydrasystems.tech)

## Choose Your Path

| You are… | Start with | Then read |
| --- | --- | --- |
| An investor, partner or curious reader | [What Hydra is](overview/what-is-hydra.md) | [How risk is controlled](overview/how-risk-is-controlled.md), [Track record policy](overview/track-record.md), [FAQ](overview/faq.md) |
| A trader | [Why trading bots fail](doctrine/why-most-bots-fail.md) | [How risk is controlled](overview/how-risk-is-controlled.md), [Public risk events](governance/risk-event-ledger.md) |
| An engineer or reviewer | [System overview](architecture/system-overview.md) | [Control boundaries](architecture/control-boundaries.md), [State model](architecture/state-model.md), [Failure modes](governance/failure-modes.md), [Full index](docs-map.md) |

## Hydra In Plain English

- **Rules, not feelings.** Every strategy is a fixed set of written rules that a
  computer follows exactly. Nothing is traded on instinct or tips.
- **Tested before trusted.** Rules are chosen on one period of historical data,
  checked on a later period they were never chosen on, and checked once more
  on sealed data. Costs are deliberately set higher than expected.
- **Risk controls can say no.** A separate supervisory layer can block a trade,
  stop trading for the day, or switch the system off. Strategies cannot
  override it.
- **When in doubt, stop.** Stale prices, missing data or a contradiction in the
  system's own records stop new trades until a person reviews them.
- **Failures are written down.** Incidents, including ones caught before any
  harm, are recorded in a [public risk-event ledger](governance/risk-event-ledger.md)
  with the private detail removed.

## Products

- **Hydra Guard** (in final testing): a MetaTrader 5 add-on that keeps an
  account inside prop-firm rules. It tracks daily and maximum loss room,
  enforces stop-losses and exposure caps, and locks trading before a limit is
  breached. It does not trade or give signals. [About Hydra Guard](https://hydrasystems.tech/guard/)
- **Hydra Quant**: the governed trading layer these documents describe. Private.

## What We Publish And What We Don't

| Published here | Kept private |
| --- | --- |
| How the system is structured and controlled | Strategy logic and parameters |
| How failures are classified, contained and recovered | Account, broker and connection details |
| Sanitized risk events | Logs, credentials and protected research |
| The dated public status | Any performance figure not independently verified |

Hydra Core makes no claim of profitability. Any future performance figures
will be linked to independent, third-party verified records, never
self-reported numbers. See the [track record policy](overview/track-record.md).

## For Engineers

Hydra separates decision generation, supervisory authority, execution
validation, observability and recovery, so that no single component can
authorize a trade on its own. The central invariant is:

> Execution is eligible only when trust is `SAFE`, permission is `ARMED`,
> lifecycle is `NORMAL`, the configured operating mode permits execution, and
> every required gate passes.

Eligibility is conditional, never an instruction. Missing or contradictory
state fails closed.

Formal specifications:

- [Control Boundaries](architecture/control-boundaries.md)
- [Multi-Axis State Model](architecture/state-model.md)
- [Failure Modes](governance/failure-modes.md) and [Threat Model](governance/threat-model.md)
- [Public Evidence Policy](governance/public-evidence-policy.md)
- [Risk Event Ledger and Schema](governance/risk-event-ledger.md)
- [Operator and Recovery Expectations](operations/operator-runbook.md)
- [Complete Documentation Index](docs-map.md)

## The Hydra Family

- **Hydra Systems**: the operation and umbrella.
- **Hydra Quant**: the private systematic-trading platform.
- **Hydra Guardian**: the internal supervisory and risk authority inside Hydra
  Quant. Not sold separately.
- **Hydra Guard**: a separate, standalone risk-protection tool for MetaTrader 5
  traders, in development. Guard is a product; Guardian is an internal
  component. See the [Public Surface Registry](architecture/public-surface-registry.md).
- **Hydra Core**: this repository, the public specification.

## Who Is Behind Hydra

Hydra Systems is founded and run by **Ibz**, an independent systematic trader
and engineer based in the UK, who builds and operates Hydra with a small team of
AI engineering assistants under human review and approval.

## Enquiries

Engineers, partners and investors can write to
[hello@hydrasystems.tech](mailto:hello@hydrasystems.tech). Happy to discuss the
architecture, risk controls, evidence standards and collaboration. Strategy
logic, parameters and account details are not shared.

## Status

Hydra Core is pre-v1. Current availability and public-user permissions are
defined only by the dated [Public Operating Posture](status/public-operating-posture.md).
When that record expires, readers should treat availability as unknown rather
than assume it continues.

No software release, tag or reuse licence has been published. See the
[Release Posture](governance/release-posture.md), [Versioning Policy](governance/versioning-policy.md)
and [Contributing Guide](CONTRIBUTING.md).

## Important Notice

Trading leveraged products carries a high risk of loss. Nothing in this
repository is investment advice, an offer, or a promise of returns. Past or
simulated results do not indicate future results.
