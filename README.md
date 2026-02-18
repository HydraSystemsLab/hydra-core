# Hydra Core

**Status:** Research & architecture phase. Selective components published.

Risk-enforced system architecture for automated decision systems.

Losses are expected. Escalation is not.

---

## Philosophy

Most automated trading systems fail not because of bad entries,  
but because of weak risk enforcement, poor execution discipline,  
and the ability for humans or code to escalate risk.

Hydra is designed around a simple principle:

> If a rule can be broken, it eventually will be.

Hydra systems are built so that:

- risk limits are enforced at the system level  
- execution is gated, observable, and reversible by design  
- failure modes are anticipated, not reacted to  

---

## What This Is

- A reference implementation of risk-first system design  
- Multi-engine architecture with independent failure domains  
- Guardrails that enforce discipline, not signals  

---

## What This Is Not

- A trading strategy  
- A signal generator  
- A plug-and-play money machine  

---

## Core Concepts

- **Risk First**: Exposure is constrained before any decision is allowed  
- **Engine Isolation**: Each engine fails independently  
- **Hard Disarms**: Systems can and will shut themselves down  
- **Observability**: Every action is logged, auditable, and replayable  
- **No Escalation**: Losses do not trigger larger bets  

---

## Status

Hydra Core is under active development.

This repository currently documents architecture and design principles.  
Code components will be published selectively.

---

## Risk Event Ledger

Hydra maintains a public **Risk Event Ledger** documenting system-level enforcement events.

This ledger records:

- Disarms  
- Constraint violations  
- Guardrail updates  
- Risk-domain changes  
- Rearms after verification  

It does **not** include:

- Trade outcomes  
- Strategy logic  
- Performance metrics  

The purpose is simple:

> Enforcement should leave evidence.

→ [`governance/risk-event-ledger.md`](governance/risk-event-ledger.md)
