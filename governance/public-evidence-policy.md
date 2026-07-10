# Public Evidence Policy

This policy defines how Hydra Systems classifies and communicates public evidence. Evidence must support only the claim actually tested.

Historical backtest, replay, forward shadow, demo execution, and verified live execution are separate evidence classes. They must not be merged into one track record, and counts from different classes must not be added.

## Claim Domains Stay Separate

Evidence about one domain cannot silently prove another:

1. **System operability** — whether defined components can perform their intended technical function.
2. **Runner health** — whether a process or dependency is responding within its health contract.
3. **Execution readiness** — whether execution preconditions and required controls pass for a stated scope.
4. **Strategy edge** — whether evidence supports a bounded claim about decision quality or expectancy.
5. **Public-user permission** — whether a public user is authorized to connect or execute.

Operational `LIVE_READY` does not prove edge. Runner health does not prove strategy quality. Private operational permission does not prove public-user permission.

`PASS`, `AMBER`, `RED`, `FROZEN`, and similar verdicts must always name the tested gate, scope, evidence time, and limitations. A `PASS` is a bounded result, not permanent safety or profit.

## Common Metadata

Where applicable, every published result must identify:

- strategy or system version
- instrument and symbol domain
- broker or data-source domain at a public-safe level
- symbol-normalization status
- timestamp range and generation date
- timezone and session assumptions
- sample size and independent opportunity count
- costs, spread, commission, latency, and slippage treatment
- gross versus net treatment
- executable versus theoretical status
- in-sample and out-of-sample split
- replay-integrity status
- lookahead, leakage, and duplicate-data checks
- forward versus reconstructed data
- source classification and sanitized provenance
- known limitations and material negative findings

If required provenance cannot be disclosed, the result must label that limitation. Withholding a private source never permits stronger public wording.

## Tier 1 — Historical Backtest

### Meaning

A specified system version was evaluated after the fact on historical data under documented assumptions.

### Non-Meaning

It is not prospective behavior, a record of contemporaneous decisions, evidence of executable fills, demo execution, verified live execution, or current authorization.

### Minimum Required Metadata

All applicable common metadata, plus:

- dataset vintage and acquisition boundary
- in-sample/out-of-sample or walk-forward design
- parameter-selection process
- cost and fill model
- lookahead and leakage review
- duplicate-record and independent-opportunity treatment

### Permitted Public Wording

> In a historical backtest of version `<version>` over `<period>`, under the stated assumptions and limitations, the tested metric was `<result>`.

### Prohibited Inference

Do not infer forward behavior, actual fills, current edge, future returns, execution readiness, or user access.

### Typical Limitations

Regime selection, overfitting, survivorship bias, synthetic fill assumptions, incomplete costs, data revisions, symbol mismatch, and dependence between opportunities.

## Tier 2 — Replay

### Meaning

Recorded chronological inputs were processed later through a specified system version to test decision, state, or execution-path behavior.

### Non-Meaning

Replay does not mean the decisions were recorded when the market data originally arrived. It is not forward shadow, demo execution, live execution, or proof that the original operational environment can be reconstructed perfectly.

### Minimum Required Metadata

All applicable common metadata, plus:

- replay source and capture completeness
- chronology and ordering guarantees
- replay clock and session model
- warm-up and initialization treatment
- version parity and replay-integrity result
- whether outputs were reconstructed or had been recorded previously

### Permitted Public Wording

> In a replay using recorded inputs from `<period>`, version `<version>` produced `<bounded result>`; this was reconstructed evidence, not contemporaneous execution.

### Prohibited Inference

Do not call replay forward evidence, add replay events to forward counts, or imply executable/live performance.

### Typical Limitations

Missing events, ordering differences, simplified latency, warm-up mismatch, environment drift, and incomplete reconstruction of venue behavior.

## Tier 3 — Forward Shadow

### Meaning

Decisions were recorded prospectively as new data arrived, while order submission remained disabled for the evaluated scope.

### Non-Meaning

Forward shadow is not demo or live execution. It does not demonstrate fill quality, market impact, broker acceptance, realized slippage, or live-money performance.

### Minimum Required Metadata

All applicable common metadata, plus:

- prospective recording start and end
- decision timestamp and data-freshness policy
- order-submission-disabled attestation
- shadow price and hypothetical fill methodology
- outages, gaps, exclusions, and late records
- count of independent forward opportunities

### Permitted Public Wording

> In a forward-shadow observation covering `<period>` and `<count>` independent opportunities, version `<version>` recorded `<bounded result>` with order submission disabled.

### Prohibited Inference

Do not describe shadow returns as executed, live, realized, or available to users. Do not project monthly or annual returns from a small or insufficient sample.

### Typical Limitations

Hypothetical fills, no market impact, untested broker lifecycle behavior, sparse opportunities, incomplete regimes, and differences between observation and execution infrastructure.

## Tier 4 — Demo Execution

### Meaning

Orders and lifecycle events were reconciled in a segregated demo or simulation environment under a stated system version and period.

### Non-Meaning

Demo execution is not live-money execution. It does not prove live liquidity, live slippage, funding behavior, public availability, or broker/account compatibility outside the stated domain.

### Minimum Required Metadata

All applicable common metadata, plus:

- demo-environment classification
- order, acknowledgement, fill, rejection, and terminal-state reconciliation
- partial-fill treatment
- environment-specific spread, commission, latency, and slippage
- isolation from live credentials and routes
- unresolved lifecycle ambiguities

### Permitted Public Wording

> In segregated demo execution over `<period>`, version `<version>` reconciled `<bounded lifecycle result>` in the stated environment.

### Prohibited Inference

Do not present demo outcomes as live-money behavior, a public-user capability, or evidence of future profitability.

### Typical Limitations

Simulation-specific fills, different liquidity and rejection behavior, simplified market impact, environment configuration differences, and domain-specific broker behavior.

## Tier 5 — Verified Live Execution

### Meaning

Actual live-money orders and fills for a bounded historical period were reconciled against authoritative evidence, with public-safe provenance and limitations recorded.

### Non-Meaning

Verified live execution is not current authorization, future edge, permanent safety, public-user access, regulatory approval, or a return guarantee.

### Minimum Required Metadata

All applicable common metadata, plus:

- bounded verification period
- system and control version
- sanitized execution domain
- authoritative order/fill reconciliation method
- gross and net treatment
- spread, commission, latency, slippage, rejection, and partial-fill treatment
- unresolved discrepancies and excluded records
- verifier role or source classification without private identifiers

### Permitted Public Wording

> For the historical period `<period>`, verified live-execution evidence for version `<version>` supports the bounded claim `<claim>`, subject to the stated sample and limitations.

### Prohibited Inference

Do not infer current permission, public availability, future performance, guaranteed returns, or unchanged operating conditions. Historical live events are not current authorization.

### Typical Limitations

Small samples, regime concentration, changing costs or liquidity, account/domain specificity, operational interventions, and incomplete transferability to future conditions.

## Publication Rules

- Evidence tiers cannot be merged into one track record.
- Counts from different tiers cannot be added.
- Small samples must be labelled prominently.
- Negative findings cannot be silently omitted where omission changes interpretation.
- Gross values cannot be presented as net.
- Theoretical values cannot be presented as executable.
- Reconstructed observations cannot be presented as forward observations.
- Annualized or monthly projections are prohibited when evidence is insufficient for that inference.
- Guaranteed-return, stable-return, and zero-risk wording is prohibited.
- Publication of actionable real-time entries or exits is prohibited until the legal and regulatory position has been reviewed.
- A promotion decision must identify the exact evidence used and remains a governance event, not an automatic result threshold.

## Compact Public Result Card Contract

Every public result card must display the following fields, or mark a field `NOT_APPLICABLE` with a reason:

| Field | Required display |
| --- | --- |
| Evidence tier | One of the five named tiers |
| Claim | The precise bounded statement supported |
| Tested gate | Named gate when a verdict is shown |
| Version | Strategy/system identifier suitable for public release |
| Domain | Instrument/symbol and public-safe data or execution domain |
| Normalization | Symbol-normalization status |
| Period | UTC range plus timezone/session assumptions |
| Sample | Observations and independent opportunity count |
| Economics | Costs, spread, commission, latency, and slippage treatment |
| Measurement | Gross/net and executable/theoretical |
| Data timing | Forward/reconstructed and replay-integrity status |
| Integrity | Lookahead, leakage, split, and duplicate-data checks |
| Generated | Generation timestamp |
| Limitations | Small-sample label, known negatives, exclusions, and withheld provenance |
| Source | Sanitized evidence classification and references |
| Authorization | “Historical evidence is not current authorization” |

The card must remain understandable without access to private evidence. If sanitization prevents a claim from being supported publicly, the claim must be narrowed or withheld.
