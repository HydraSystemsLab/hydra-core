# Risk Event Review Process

This process keeps the selected public risk-event history current without
moving protected evidence into public coordination. The ledger remains a
sanitized governance record rather than a complete incident register.

## Review Triggers

Open a review after any material:

- disarm, rearm, or engine pause
- operating-mode promotion
- supervisory or live-authority boundary change
- use or change of a recovery contract
- risk-policy change
- evidence correction that changes a governance conclusion
- retirement of a legacy runtime with operational authority

Also perform a catch-up review at least monthly, including months in which no
public event is ultimately published.

## Review Inputs

Bind the review interval and source identities first. Discover candidate causal
episodes from approved operational, broker, ledger, Guardian, release, and
recovery sources. Commit subjects and issue text may help locate evidence but
do not establish event facts.

For every candidate, record privately:

- the exact evidence-supported occurrence time and later recording time
- scope, failure class, authority boundary, and state transition
- authoritative evidence locations and identities
- before and after state axes that are actually supported
- enforcement result, recovery conditions, and separate rearm evidence
- disclosure class, public-safe facts, limitations, and proposed disposition

## Adjudication

Assign one disposition to each causal episode:

- `PUBLISH`: evidence supports a sanitized structured event
- `DEFER`: a required fact, exact time, or transition remains unsupported
- `MERGE_WITH_EPISODE`: repeated work belongs to one already identified cause
- `EXCLUDE`: policy says the activity is not a risk-ledger event

Deduplicate retries, restarts, repeated proposals, and repair commits by
strategy state and causal episode. Keep records separate when failure class,
authority boundary, scope, or lifecycle transition differs. Recovery clearance
and rearm are distinct decisions.

## Public Coordination Boundary

A public issue records only the review interval, sanitized source categories,
candidate episode names, exclusions, evidence status, redaction status, and
owner disposition. Protected evidence and values remain in approved private
storage. Never include credentials, accounts, balances, private paths, hosts,
endpoints, logs, order payloads, protected parameters, actionable prices, or
real-time permission.

## Publication And Verification

Use the evidence-supported UTC transition time for `occurred_at` and the public
preparation time for `recorded_at`. Validate schema, identity, chronology,
relationships, and public references. Review the full public diff for protected
material and unsupported claims. Publish corrections through a new linked
record; do not silently rewrite an existing event.

Record a monthly review even when every candidate is deferred or excluded. A
review with no published event confirms only that the interval was assessed; it
does not prove that no private incident occurred.
