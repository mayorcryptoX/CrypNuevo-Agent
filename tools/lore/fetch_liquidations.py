"""
LORE Liquidation Fetcher — BTC liquidation clusters and recent events.

This is the Hyblock-equivalent: where are the densest long/short
liquidation clusters? Those are the price magnets in CrypNuevo's method.

Usage:
    python tools/lore/fetch_liquidations.py
    python tools/lore/fetch_liquidations.py --lookback 24
    python tools/lore/fetch_liquidations.py --raw

Options:
    --lookback   Hours of recent liquidation events to fetch (default: 48)
    --raw        Print raw JSON
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

ASSET = "BTC"

_LIQ_ENDPOINTS = [
    "/v1/liquidations/{asset}",
    "/v1/market/{asset}/liquidations",
    "/v1/liq/{asset}",
    "/v1/forced-close/{asset}",
    "/liquidations/{asset}",
    "/liq/{asset}",
    # LORE may group by cluster
    "/v1/liquidations/{asset}/clusters",
    "/v1/liquidation-clusters/{asset}",
    "/v1/liq-clusters/{asset}",
    # Hyblock-style heatmap
    "/v1/heatmap/{asset}",
    "/v1/liquidation-heatmap/{asset}",
]


def _try_endpoints(templates: list[str], params: dict) -> tuple[str, dict] | None:
    for tmpl in templates:
        for slug in [ASSET, ASSET.lower()]:
            ep = tmpl.replace("{asset}", slug)
            try:
                data = lore.get(ep, params=params)
                return ep, data
            except Exception as e:
                if "404" not in str(e):
                    print(f"  [{ep}] {e}", file=sys.stderr)
    return None


def print_markdown(result: tuple[str, dict] | None, lookback: int):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# BTC Liquidation Clusters — {now}")
    print()

    if not result:
        print("## Status: Endpoint Not Yet Discovered")
        print()
        print("Run `python tools/lore/discover.py` first to map available endpoints.")
        print("Once the correct liquidation endpoint is confirmed, update `_LIQ_ENDPOINTS` in this file.")
        return

    ep, data = result
    print(f"## Source")
    print(f"- Endpoint: `{ep}`")
    print(f"- Lookback: {lookback}h")
    print()

    print("## Raw Data (first 2000 chars)")
    print("```json")
    print(json.dumps(data, indent=2)[:2000])
    print("```")
    print()

    # Attempt to extract cluster data for CrypNuevo-style interpretation
    clusters = []
    if isinstance(data, list):
        clusters = data
    elif isinstance(data, dict):
        for key in ("clusters", "liquidations", "data", "levels", "heatmap"):
            if key in data and isinstance(data[key], list):
                clusters = data[key]
                break

    if clusters:
        print("## Interpretation Guide (CrypNuevo method)")
        print()
        print("The following clusters are **price magnets**.")
        print("CrypNuevo's rule: price is pulled toward the densest untaken liquidation cluster.")
        print("A cluster is 'taken' when price wicks through it. Until then, it remains a target.")
        print()
        print(f"Found {len(clusters)} clusters/events:")
        for i, c in enumerate(clusters[:10]):  # top 10
            print(f"  {i+1}. {json.dumps(c)}")
        if len(clusters) > 10:
            print(f"  ... and {len(clusters) - 10} more (use --raw for full list)")
    print()
    print("---")
    print("*Paste this block into your CrypNuevo mentor chat for liquidation context.*")


def main():
    ap = argparse.ArgumentParser(description="Fetch BTC liquidation data from LORE")
    ap.add_argument("--lookback", type=int, default=48,
                    help="Hours of recent events to fetch (default: 48)")
    ap.add_argument("--raw", action="store_true", help="Print raw JSON")
    args = ap.parse_args()

    print("Fetching BTC liquidation data...", file=sys.stderr)
    params = {"limit": args.lookback, "symbol": ASSET, "hours": args.lookback}
    result = _try_endpoints(_LIQ_ENDPOINTS, params)

    if args.raw:
        print(json.dumps({"endpoint": result[0] if result else None,
                          "data": result[1] if result else None}, indent=2))
        return

    print_markdown(result, args.lookback)


if __name__ == "__main__":
    main()
