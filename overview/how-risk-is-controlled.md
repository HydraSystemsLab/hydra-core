# How Risk Is Controlled

Hydra assumes that losses and failures will happen. Its controls aim to keep
each one small, visible and recoverable. This page explains them in plain
English; the formal rules are in [Control Boundaries](../architecture/control-boundaries.md)
and the [Risk Doctrine](../doctrine/risk-doctrine.md).

## Layers Of Protection

| Layer | What it does | Example |
| --- | --- | --- |
| Per-trade limit | Every trade opens with a stop-loss held at the broker | A trade's maximum loss is fixed before it is placed |
| Exposure caps | Limits on how much can be at risk at once, per market and in total | A new trade is refused if it would exceed the total cap |
| Daily and overall loss limits | Trading stops for the day, or entirely, when losses approach a threshold | Positions are closed and trading is disarmed near the daily limit |
| Supervisor veto | Hydra Guardian checks every proposed action and can say no | A trade is blocked because the price feed is stale |
| Fail closed | Missing, stale or contradictory information stops new trading | After a restart, trading waits until records are reconciled |
| Human approval | Live changes need a written, approved procedure | A software update is requalified before trading resumes |

Hydra's own limits are set tighter than the external rules it operates under,
so normal bad days stay well inside the line.

## When Something Goes Wrong

1. **Stop.** New trading halts for the affected part of the system.
2. **Preserve.** Logs and records are kept as evidence.
3. **Reconcile.** The system's records are checked against the broker's.
4. **Review.** A person decides what happened and approves the fix.
5. **Record.** The incident goes into the private log and, with private detail
   removed, into the [public risk-event ledger](../governance/risk-event-ledger.md).
6. **Resume deliberately.** Restarting or waiting does not re-enable trading on
   its own.

## Examples Of What The Controls Catch

These are the kinds of event the ledger records:

- A price arrives too old to trust, so the trade is refused rather than placed
  on stale information.
- The trading platform updates itself overnight, so the new version is held
  back until it has been tested again.
- A component stops answering its health check in time, so it stops itself
  rather than continue unsupervised.
- A display problem is found in testing, before it can affect live trading.

## Limits Of These Controls

Controls reduce risk; they do not remove it. Markets can gap past a stop, a
broker can fail, and software can contain undiscovered faults. The controls
are an engineering objective, not a guarantee. See [Failure Modes](../governance/failure-modes.md)
and the [Threat Model](../governance/threat-model.md).
