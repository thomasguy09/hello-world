#!/usr/bin/env python3
"""Mark the paper portfolio to market and print a P&L report.

Arithmetic lives here rather than in prose so the numbers are reproducible
and not subject to mental-math errors.

Usage:
    python3 report.py SPY=744.21 NVDA=200.75
"""

import json
import sys
from pathlib import Path

LEDGER = Path(__file__).parent / "ledger.json"


def load():
    with LEDGER.open() as f:
        return json.load(f)


def parse_prices(args):
    prices = {}
    for arg in args:
        if "=" not in arg:
            sys.exit(f"bad argument {arg!r}, expected SYMBOL=PRICE")
        sym, _, raw = arg.partition("=")
        try:
            prices[sym.upper()] = float(raw)
        except ValueError:
            sys.exit(f"bad price in {arg!r}")
    return prices


def main():
    led = load()
    prices = parse_prices(sys.argv[1:])

    cash = led["cash"]
    rows = []
    holdings_value = 0.0
    missing = []

    for pos in led["positions"]:
        sym = pos["symbol"]
        if sym not in prices:
            missing.append(sym)
            continue
        last = prices[sym]
        cost = pos["shares"] * pos["entry_price"]
        value = pos["shares"] * last
        holdings_value += value
        rows.append((sym, pos["shares"], pos["entry_price"], last, value - cost))

    if missing:
        sys.exit(f"no price supplied for open position(s): {', '.join(missing)}")

    total = cash + holdings_value
    start = led["starting_cash"]
    pnl = total - start
    pct = (pnl / start * 100) if start else 0.0

    print(f"{'SYMBOL':<8}{'SHARES':>9}{'ENTRY':>11}{'LAST':>11}{'P&L':>12}")
    print("-" * 51)
    for sym, sh, entry, last, row_pnl in rows:
        print(f"{sym:<8}{sh:>9.4f}{entry:>11.2f}{last:>11.2f}{row_pnl:>+12.2f}")
    if not rows:
        print("(no open positions)")
    print("-" * 51)
    print(f"{'cash':<8}{cash:>43.2f}")
    print(f"{'holdings':<8}{holdings_value:>43.2f}")
    print(f"{'TOTAL':<8}{total:>43.2f}")
    print(f"\nstarting  {start:>10.2f}")
    print(f"P&L       {pnl:>+10.2f}  ({pct:+.2f}%)")

    bench = led.get("benchmark") or {}
    bench_entry = bench.get("entry_price")
    bench_sym = bench.get("symbol")
    if bench_entry and bench_sym in prices:
        bench_pct = (prices[bench_sym] - bench_entry) / bench_entry * 100
        print(f"{bench_sym:<9} {bench_pct:>+10.2f}%  (buy and hold)")
        print(f"vs bench  {pct - bench_pct:>+10.2f} pts")
    elif bench_entry:
        print(f"\n({bench_sym} benchmark entry {bench_entry:.2f} — pass "
              f"{bench_sym}=<price> to compare)")


if __name__ == "__main__":
    main()
