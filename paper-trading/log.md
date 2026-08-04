# Trading Log

## 2026-08-04 — Session 1 (entry)

Entered mid-session, roughly 1:15 PM ET, about 2h45m before the close. This was
supposed to run Monday pre-open; the scheduled Routines were never approved and
so never fired, and the pre-open commit control could not be honored. Noted so
nobody later reads this as the clean run the rules describe.

### Market context

Strong risk-on tape. Nasdaq +2%, S&P 500 +1.5% at a record high, Dow +1.7%.
Driver was optimism on a Strait of Hormuz deal — WTI crude off 5% on hopes
mediators avert US airstrikes on Iran — plus a good earnings batch. Palantir
+27% on blowout results and raised guidance. AMD reports after the bell.

### Positions

| Symbol | Shares | Entry | Cost | Weight |
|--------|--------|-------|------|--------|
| NVDA   | 1.1976 | 208.74 | $249.99 | 25% |
| QQQM   | 0.8478 | 294.89 | $250.01 | 25% |
| cash   |        |        | $500.00 | 50% |

**NVDA** — AI momentum, reclaimed the $210 technical level, up ~3% on the day.
Earnings are 2026-08-26, so there is no earnings event inside a short hold.
The thesis is momentum continuation on a strong tape. That is a weak thesis and
I want it on the record as weak.

**QQQM** — Nasdaq-100 beta. Honestly this is not a stock pick at all; it is a
bet that a risk-on day keeps being risk-on. Chose the ETF partly because
broad-index quotes came back internally consistent while individual names did not.

### Known flaws in this entry, stated before the outcome is known

1. **These two positions are not diversified.** NVDA is a top-ten QQQM holding
   at roughly 8-9% weight. This is one factor bet — large-cap AI/tech momentum —
   expressed twice, not two independent ideas.
2. **I am buying after the move, not before it.** Entering at 1:15 PM on a day
   already up 1.5-2%, near a record high. Chasing strength is the single most
   common retail error and I am doing it because the clock forced the entry.
3. **50% cash is not a view.** It is what was left after MSFT and DAL failed
   price verification. It will mute the result in both directions.
4. **The overnight gap is unmanaged.** AMD reports after the bell tonight; a big
   move there moves semis and the Nasdaq at tomorrow's open, and there is no
   stop and no way for me to react while the market is closed.

### Data quality — what was rejected and why

The rule was: a price must corroborate across independent sources, or the name
does not get traded.

- **DAL — rejected.** Two sources gave $81.33 and $85.85 for the same moment.
  A 5.5% spread is wider than the entire trade thesis.
- **MSFT — rejected.** Irreconcilable. One search returned last $479.20 with a
  prior close of $487.65 and a 52-week range of $349.20-$553.72; a follow-up
  returned articles describing the stock "near $389," "down 27% from all-time
  high," "entering a bear market after a 21% drop," and separately "after a 25%
  three-day rally" and "+15.51% on earnings." Those describe different weeks
  blended together. No defensible entry price exists.
- **NVDA — accepted.** Two independent searches agreed: ~$206.65 last,
  $200.75 prior close, day range $196.85-$208.74. One summary mislabeled the
  intraday quote as a "close," but the numbers corroborate.
- **QQQM — accepted, weaker.** Single source, but internally consistent: last
  $294.53 at 10:38 EDT, prior close $288.27, open $291.63, range
  $291.36-$294.89. Consistency across five fields is decent evidence.
- **SPY benchmark — accepted.** $767.77 last, $757.67 prior close, range
  $760.52-$768.09, and the 52-week high equal to the day high, which matches the
  reported record-high tape.

### The staleness haircut

Every quote available is 1-3 hours old on a tape moving 1.5-2%. Stale prices on
a rising market bias *in my favor* — record a low entry, book a gain that never
happened. To push the bias the other way, every entry is recorded at the **high
of the observed day range**, the worst plausible fill, rather than the last
trade. The SPY benchmark gets the identical treatment so the comparison stays
symmetric.

This makes the recorded result pessimistic relative to a real fill. That is the
correct direction of error for an experiment testing whether these picks are any
good.

### Prediction, on the record

I expect this to land within roughly ±1.5% of SPY, dominated by noise rather
than by anything in the reasoning above. Committed before the close so it can be
checked.

## 2026-08-04 — Session 1 (post-close, INCOMPLETE)

Checked at 16:10 ET. No P&L is recorded because none can be computed honestly.

### Error found: the NVDA entry was a day stale

The quotes used to enter NVDA at 13:05 — last ~206.65, prior close 200.75,
range 196.85-208.74, open 197.69 — were the **2026-08-03** session, not 08-04.

The reconciliation that exposed it: a post-close source reported NVDA
"+2.3% to 211.48 after climbing 2.9% in the previous session." That only works
if ~206.70 was Monday's close. A direct check confirmed NVDA closed 206.70 on
2026-08-03.

So the "conservative day high" of 208.74 was **Monday's** high. The whole point
of that haircut was to make lag bias against the strategy. Applied to the wrong
day, it did the opposite — roughly 1.3% of gain on that position that never
existed. Entry corrected to 211.48, shares 1.1976 -> 1.1821. The original values
are preserved in ledger.json under positions[].correction.

The correction may still be too generous: 211.48 was an early-session trade, not
08-04's high, and the true conservative basis is probably higher.

### verify.py has a hole

It compares prices *across sources* and passes anything agreeing within 0.75%.
It never checks the **as-of date**. Two sources both quoting a stale session
agree perfectly and pass clean. That is exactly what happened here — and it
happened three hours after the tool was written and validated "4 for 4" against
the same day's decisions.

The lesson is not that the tolerance was wrong. It is that the tool tested the
thing that was easy to test, and the actual failure came in through the
dimension nobody instrumented.

### QQQM: basis holds, but partial

QQQM's entry data was genuinely 08-04 — its stated prior close of 288.27 matches
Monday's 288.11 close. The basis is sound. But the 294.89 "day high" was
observed at 10:38 ET and the tape kept rallying all afternoon, so the real
08-04 high is likely higher. Same direction of flattery, smaller magnitude.

### What is actually known

- **SPY closed 771.77**, +1.86% from 757.67, consistent with the reported +1.8%
  index move to a record.
- **NVDA and QQQM closes were not published** as of 16:10 ET. Searches returned
  07-31 and 08-03 data.

No P&L. Marking two of three legs with prices from the wrong day is what caused
this entry to be wrong in the first place, and doing it again to produce a number
on demand would be the same mistake with more confidence attached.
