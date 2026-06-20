"""
LORE Market Fetcher — BTC OHLCV + Funding Rate + Open Interest.

Usage:
    python tools/lore/fetch_market.py --timeframe 4h
    python tools/lore/fetch_market.py --timeframe 1d --lookback 30
    python tools/lore/fetch_market.py --timeframe 1h --lookback 48 --raw

Options:
    --timeframe   Candle timeframe: 1m 5m 15m 30m 1h 4h 1d  (default: 4h)
    --lookback    Number of periods to fetch               (default: 50)
    --raw         Print raw JSON instead of markdown brief
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

ASSET = "BTC"

# Endpoint candidates — will be confirmed after discover.py runs
_OHLCV_ENDPOINTS = [
    "/v1/ohlcv/{asset}",
    "/v1/candles/{asset}",
    "/v1/market/{asset}/ohlcv",
    "/v1/market/{asset}/candles",
    "/ohlcv/{asset}",
    "/candles/{asset}",
]

_FUNDING_ENDPOINTS = [
    "/v1/funding/{asset}",
    "/v1/market/{asset}/funding",
    "/funding/{asset}",
]

_OI_ENDPOINTS = [
    "/v1/oi/{asset}",
    "/v1/open-interest/{asset}",
    "/v1/market/{asset}/oi",
    "/v1/market/{asset}/open-interest",
    "/oi/{asset}",
]


def _try_endpoints(templates: list[str], asset: str, params: dict) -> tuple[str, dict] | None:
    """Try each endpoint template and return (endpoint, data) on first success."""
    for tmpl in templates:
        ep = tmpl.replace("{asset}", asset)
        try:
            data = lore.get(ep, params=params)
            return ep, data
        except Exception as e:
            if "404" not in str(e):
                # Non-404 error is interesting — log and continue
                print(f"  [{ep}] {e}", file=sys.stderr)
    return None


def fetch_ohlcv(timeframe: str, lookback: int) -> dict | None:
    params = {"timeframe": timeframe, "limit": lookback, "symbol": ASSET}
    result = _try_endpoints(_OHLCV_ENDPOINTS, ASSET, params)
    if result:
        return {"endpoint": result[0], "data": result[1]}
    # Try with lowercase asset slug
    result = _try_endpoints(_OHLCV_ENDPOINTS, ASSET.lower(), params)
    if result:
        return {"endpoint": result[0], "data": result[1]}
    return None


def fetch_funding(lookback: int) -> dict | None:
    params = {"limit": lookback, "symbol": ASSET}
    result = _try_endpoints(_FUNDING_ENDPOINTS, ASSET, params)
    if result:
        return {"endpoint": result[0], "data": result[1]}
    result = _try_endpoints(_FUNDING_ENDPOINTS, ASSET.lower(), params)
    return {"endpoint": result[0], "data": result[1]} if result else None


def fetch_oi(lookback: int) -> dict | None:
    params = {"limit": lookback, "symbol": ASSET}
    result = _try_endpoints(_OI_ENDPOINTS, ASSET, params)
    if result:
        return {"endpoint": result[0], "data": result[1]}
    result = _try_endpoints(_OI_ENDPOINTS, ASSET.lower(), params)
    return {"endpoint": result[0], "data": result[1]} if result else None


def _summarize_list(data: dict) -> dict:
    """Extract a simple summary from whatever list/dict LORE returns."""
    if isinstance(data, list) and data:
        latest = data[-1] if isinstance(data[-1], dict) else {}
        return {"count": len(data), "latest": latest, "oldest": data[0] if isinstance(data[0], dict) else {}}
    if isinstance(data, dict):
        return data
    return {"raw": str(data)[:500]}


def print_markdown(ohlcv: dict | None, funding: dict | None, oi: dict | None, timeframe: str):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# BTC Market Context — {timeframe.upper()} — {now}")
    print()

    print("## OHLCV")
    if ohlcv:
        summary = _summarize_list(ohlcv["data"])
        print(f"- Endpoint: `{ohlcv['endpoint']}`")
        print(f"- Records: {summary.get('count', 'N/A')}")
        if "latest" in summary and summary["latest"]:
            print(f"- Latest candle: {json.dumps(summary['latest'], indent=2)[:400]}")
    else:
        print("- Could not fetch — run `discover.py` to find the correct endpoint.")
    print()

    print("## Funding Rate")
    if funding:
        summary = _summarize_list(funding["data"])
        print(f"- Endpoint: `{funding['endpoint']}`")
        if "latest" in summary and summary["latest"]:
            print(f"- Latest: {json.dumps(summary['latest'], indent=2)[:400]}")
    else:
        print("- Could not fetch — endpoint not yet discovered.")
    print()

    print("## Open Interest")
    if oi:
        summary = _summarize_list(oi["data"])
        print(f"- Endpoint: `{oi['endpoint']}`")
        if "latest" in summary and summary["latest"]:
            print(f"- Latest: {json.dumps(summary['latest'], indent=2)[:400]}")
    else:
        print("- Could not fetch — endpoint not yet discovered.")
    print()

    print("---")
    print("*Paste this block into your CrypNuevo mentor chat for live market context.*")


def main():
    ap = argparse.ArgumentParser(description="Fetch BTC market data from LORE")
    ap.add_argument("--timeframe", default="4h",
                    choices=["1m", "5m", "15m", "30m", "1h", "4h", "1d"],
                    help="Candle timeframe (default: 4h)")
    ap.add_argument("--lookback", type=int, default=50,
                    help="Number of periods to fetch (default: 50)")
    ap.add_argument("--raw", action="store_true",
                    help="Print raw JSON instead of formatted brief")
    args = ap.parse_args()

    print(f"Fetching BTC market data [{args.timeframe}, last {args.lookback} periods]...",
          file=sys.stderr)

    ohlcv = fetch_ohlcv(args.timeframe, args.lookback)
    funding = fetch_funding(args.lookback)
    oi = fetch_oi(args.lookback)

    if args.raw:
        print(json.dumps({
            "ohlcv": ohlcv,
            "funding": funding,
            "oi": oi,
        }, indent=2))
        return

    print_markdown(ohlcv, funding, oi, args.timeframe)


if __name__ == "__main__":
    main()
