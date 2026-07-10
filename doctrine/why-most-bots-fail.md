# Why Trading Bots Fail

> A promising idea is not evidence of a survivable system.

Automated trading systems can fail even when their entry logic appears promising.
Uncontained system-level *failure modes* are a separate source of risk.

This document explains why.

---

## 1. Profitability Is Not the Same as Survival

A system can be profitable and still be structurally unsafe.

Backtest optimization often favors:

* High win rates
* Smooth equity curves
* Optimised parameters

Live conditions can expose:

* Escalation
* Fragility
* Undefined behaviour under stress

Favorable historical results do not prove operational survivability.

Failure may come from strategy weakness, operational weakness, or both.
This doctrine focuses on what the surrounding system permits when things go wrong.

---

## 2. Discipline Is Not a Control Mechanism

“Just follow the rules” is not risk management.

Discipline:

* Is voluntary
* Degrades under pressure
* Fails silently

If a system depends only on discipline, its control model is incomplete and may be unsafe.

A rule that relies solely on overrideable discretion is not an enforced control.
A limit that can be silently ignored is not an enforced limit.

Human operators and automated code can both escalate risk under stress.
Defined escalation paths should be mechanically blocked within documented control boundaries.

---

## 3. Risk Rules vs Risk Enforcement

Many systems document risk rules.
Documentation alone does not enforce them.

Examples of defined (but unenforced) rules:

* “Max daily loss: `<defined limit>`”
* “No trading after X losses”
* “Reduce size after drawdown”

If these rules live:

* In documentation
* In strategy code only
* In a human’s head

They do not by themselves control behavior.

Enforcement means the documented controls can:

* Reject a defined ineligible request
* Disarm the affected scope
* Halt the affected execution path

Discretionary bypass is not permitted. Any exceptional containment authority must be explicit, narrower than normal execution, and recorded.

---

## 4. Escalation Amplifies Loss

Escalation can turn ordinary losses or operational defects into catastrophic losses.

Escalation patterns look like:

* Increasing size after losses
* Removing stops “temporarily”
* Switching modes mid-session
* Re-entering after disarm
* Letting a bot keep trading “to recover”

These behaviours are not merely theoretical edge cases.
If a system permits them, they remain credible recurring failure risks.

An identified failure mode remains a credible risk until its likelihood and impact are reduced by tested controls.

---

## 5. Signals Do Not Replace Controls

AI can make idea generation cheaper.
It does not make a trading system governed or survivable.

It does not replace:

* Risk governance
* Execution discipline
* Failure containment
* Operational maturity

A more complex signal inside a fragile system can increase risk.

Complexity without enforcement can accelerate failure.

---

## 6. Engine Isolation Matters

Single-system designs concentrate failure.

When one strategy breaks, a poorly isolated design can propagate the failure widely.

Isolated engines:

* Are intended to fail independently
* Can be stopped within a narrower scope
* Reduce, but do not eliminate, cross-engine contamination

Survivable systems assume components will fail.
They are designed to contain a failure to the narrowest practical domain while accounting for shared dependencies.

---

## 7. Trade Stops And System Disarms

Trade stops and system disarms address different scopes.

A trade stop is intended to constrain one position or trade.
A disarm withdraws permission from a broader governed scope.

Disarms should trigger on:

* Daily loss
* Equity drawdown
* Repeated execution errors
* Missing or invalid constraints

Once disarmed:

* Defined execution paths must mechanically block new exposure
* Restarting must not clear the disarm
* Evidence must explain the reason and scope

---

## 8. Observability Is Part of Risk

If you cannot answer:

* Why a trade was allowed
* Why a trade was blocked
* Why the system stopped

Then the relevant state is `AMBIGUOUS`, and new exposure should be blocked until authoritative explanation and reconciliation are restored.

Logs are not only debugging tools.
Safety-relevant records also support governance and recovery.

Opacity can hide failure until recovery becomes materially harder.

---

## 9. Survivable Systems Accept Losses

Losses are expected.
Escalation is not.

A survivable system:

* Accepts being wrong
* Refuses to double down
* Prioritises staying alive over being active

The goal is not to avoid every drawdown.
The goal is to mechanically constrain defined escalation and exposure paths while the documented controls operate as designed.

---

## 10. Operational Resilience

Operational resilience is not evidence of strategy edge or profitability.

Strategies decay.
Execution environments change.
Rulesets evolve.

What can improve over time:

* Constraint enforcement
* Failure containment
* Operational discipline

Prediction alone is not enough.

Durable operating value comes from mechanically blocking defined unsafe actions while documented boundaries and enforcement controls are operating as designed.

---

**Status:** Doctrine draft. Strategy-agnostic. Architecture-first.
