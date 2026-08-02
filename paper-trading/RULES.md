# Paper Trading Experiment — Rules

An experiment to test one question: **do Claude's stock picks make money?**

No real money is involved. No brokerage account is connected. Nothing in this
directory can place an order.

## Stake

$1,000.00 of imaginary cash, funded 2026-08-02.

## Risk constraints

Set by the account owner, enforced here by design:

- **Long only.** No short positions.
- **No margin.** Cash account semantics — you cannot spend money you don't have.
- **No options, futures, or leveraged/inverse ETFs.** Nothing with a payoff that
  can exceed the capital committed to it.
- **Max 25% of portfolio value in any single name** at time of entry.
- **Max 4 open positions.**

Maximum possible loss is the $1,000. That is the point of the constraints.

## Integrity controls

The experiment is worthless without these, because the failure mode of any
"AI picks stocks" exercise is hindsight editing.

1. **Picks are committed to git before the market opens.** The commit timestamp
   is the proof. A pick that isn't in a commit made before the open doesn't count.
2. **No editing or deleting past entries.** Losses stay in the log. Corrections
   are appended, never overwritten.
3. **Every mark records its source.** Price, source URL, and time observed.
4. **The benchmark is recorded alongside.** Beating a coin flip is not the bar;
   beating buy-and-hold SPY is.

## Data limitations — read this before believing any number here

This session's egress policy blocks every market data API (Yahoo, Polygon,
Alpaca, Alpha Vantage, Finnhub, stooq all refused at the proxy). The only
working channel is web search, which returns *prose summaries* of quotes.

Consequences, stated plainly:

- **Prices are approximate.** A test on 2026-08-02 returned two different closes
  for SPY on the same date ($744.21 and $747.03) from different sources.
- **No intraday data.** There are no minute or hourly bars available.
- **Therefore this is not day trading.** True day trading needs intraday fills.
  Positions here are entered near the open and marked at the close, using
  whatever price can be corroborated. Slippage and spread are not modeled.
- **Fills are assumed, not real.** A real order might not fill at the marked price.

Any result produced under these conditions carries error bars wider than most
of the edge a strategy could plausibly have. Treat the output as a directional
sanity check, not as a track record.

## Statistical honesty

One trading day is noise. A single day's result — win or lose — says nothing
about whether the picks are any good. Sample sizes on the order of dozens of
trades begin to be weakly informative. Nothing produced in one morning should
change anyone's mind about anything.

This is stated up front so a lucky first day doesn't get read as skill.

## What this experiment cannot become

This is a closed simulation. It does not graduate into live trading by flipping
a flag, because there is no broker integration here and none is planned in this
directory. If real trading is ever built, it is a separate system with its own
review, and the human places or explicitly approves the orders.
