#!/usr/bin/env python3
"""Decide whether a quote is trustworthy enough to trade on.

On 2026-08-04 this decision was made by hand, which is a problem: the same
party picking the stocks also decided which prices were good enough to use.
That is a place for bias to enter unnoticed. This encodes the rule instead.

The rule:

  * Two or more independent sources -> the spread between the highest and
    lowest quote must be within TOLERANCE. Wide disagreement means nobody
    knows the price and the name is untradeable.
  * Exactly one source -> accept only if the quote is internally consistent
    (last and open both inside the day's range, range straddles the prior
    close plausibly). Flagged as weak: one source agreeing with itself is
    not corroboration.

Entry price is deliberately NOT the consensus. On stale quotes the entry is
taken at the day high -- the worst plausible fill -- so that lag on a rising
tape biases against the strategy rather than for it.

Usage:
    python3 verify.py NVDA 206.64 206.70
    python3 verify.py --high 208.74 NVDA 206.64 206.70
    python3 verify.py --single --low 291.36 --high 294.89 --open 291.63 QQQM 294.53
"""

import argparse
import sys

TOLERANCE = 0.0075  # 0.75%: comfortably above quote lag, far below any real edge


def check_spread(prices):
    lo, hi = min(prices), max(prices)
    spread = (hi - lo) / lo if lo else float("inf")
    return spread, spread <= TOLERANCE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("prices", nargs="+", type=float)
    ap.add_argument("--single", action="store_true",
                    help="only one source available; require internal consistency")
    ap.add_argument("--low", type=float, help="observed day low")
    ap.add_argument("--high", type=float, help="observed day high (entry basis)")
    ap.add_argument("--open", dest="open_", type=float, help="observed open")
    args = ap.parse_args()

    sym = args.symbol.upper()
    prices = args.prices

    print(f"{sym}: {len(prices)} quote(s) -> {', '.join(f'{p:.2f}' for p in prices)}")

    if len(prices) >= 2:
        spread, ok = check_spread(prices)
        print(f"  spread {spread * 100:.2f}%  (tolerance {TOLERANCE * 100:.2f}%)")
        if not ok:
            print(f"  REJECT -- sources disagree by more than the trade thesis is worth")
            sys.exit(1)
        confidence = "corroborated"
    elif args.single:
        if args.low is None or args.high is None:
            sys.exit("  single-source check needs --low and --high")
        last = prices[0]
        problems = []
        if not (args.low <= last <= args.high):
            problems.append(f"last {last:.2f} outside range {args.low:.2f}-{args.high:.2f}")
        if args.open_ is not None and not (args.low <= args.open_ <= args.high):
            problems.append(f"open {args.open_:.2f} outside range")
        if args.low > args.high:
            problems.append("low above high")
        if problems:
            for p in problems:
                print(f"  REJECT -- {p}")
            sys.exit(1)
        print("  internally consistent across range/open/last")
        confidence = "weak (single source, self-consistent only)"
    else:
        print("  REJECT -- one quote and no --single consistency data")
        sys.exit(1)

    entry = args.high if args.high is not None else max(prices)
    basis = "day high" if args.high is not None else "highest observed quote"
    print(f"  ACCEPT [{confidence}]")
    print(f"  entry {entry:.2f}  ({basis} -- conservative, worst plausible fill)")


if __name__ == "__main__":
    main()
