# What Hydra Is

Hydra is software that trades financial markets by fixed rules, places its own
orders, and protects itself with hard limits. It is built to be judged on how
it behaves when things go wrong, not only on how it performs when things go
right.

This page is written for non-engineers. The formal version is the
[System Overview](../architecture/system-overview.md).

## The Three Parts

Think of Hydra as an autopilot with circuit breakers.

1. **The strategies (the brain).** Each strategy is a written set of rules, for
   example "when an index has fallen unusually hard, buy; sell when it
   recovers or hits its stop." The rules are precise enough for a computer to
   follow exactly and to test on years of past data.
2. **The executor (the hands).** It connects to a broker through MetaTrader 5,
   a standard trading platform, and places each trade with a protective stop
   already attached, so every trade has a maximum loss before it opens.
3. **The supervisor (the circuit breakers).** A separate authority, Hydra
   Guardian, checks every proposed action against risk limits and system
   health. It can block a trade, stop trading for the day, or switch trading
   off entirely. Strategies cannot overrule it.

Hydra runs on rented servers in data centres, not on a home computer, so it
does not depend on one person's internet connection or being awake.

## Why Automate

Most discretionary traders lose money through behaviour: holding losing trades,
trading to win back losses, or abandoning a plan after a bad week. A system
cannot do any of that. Because its rules are fixed, they can also be tested
before any money is at risk.

Automation brings its own failure modes: stale prices, duplicated orders,
broken connections, software updates and silent crashes. Most of Hydra's
engineering goes into containing those. See [Why Trading Bots Fail](../doctrine/why-most-bots-fail.md).

## How Strategies Are Chosen

Hydra treats strategy selection like a controlled trial:

1. The tests and pass marks are written down before the results exist.
2. Strategies are selected on one period of historical data.
3. They are checked on a later period that played no part in selecting them.
4. They are checked once more on sealed data that nobody has looked at.
5. Trading costs are deliberately set higher than expected.
6. Thousands of reshuffled histories estimate how bad an unlucky run could be.

A strategy that only looks good on the data it was chosen on fails at step 3 or
4 and is dropped.

## What Hydra Does Not Claim

- It does not claim to be profitable. Tests describe the past under stated
  assumptions; they do not predict the future.
- It does not sell trading signals or give investment advice.
- It does not publish self-reported performance. See the
  [track record policy](track-record.md).

## Learn More

- [How risk is controlled](how-risk-is-controlled.md)
- [Frequently asked questions](faq.md)
- [Public risk events](../governance/risk-event-ledger.md)
