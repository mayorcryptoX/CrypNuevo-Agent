"""
LORE Regime Fetcher — BTC current volatility regime.

Regime context tells us which CrypNuevo setups are highest-probability:
- trending_high_vol  → momentum + wick-fill continuation setups dominant
- trending_low_vol   → range extreme deviation + sweep setups dominant
- ranging            → full range playbook (Three Taps, sweep of extremes)
- choppy / unclear   → flat / no-trade default

Usage:
    python tools/lore/fetch_regime.py
    python tools/lore/fetch_regime.py --raw
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

ASSET = "BTC"

_REGIME_ENDPOINTS = [
    "/v1/regimes/{asset}",
    "/v1/regime/{asset}",
    "/v1/market/{asset}/regime",
    "/v1/market/{asset}/regimes",
    "/regimes/{asset}",
    "/regime/{asset}",
    "/v1/context/{asset}",
    "/v1/market-context/{asset}",
    "/v1/conditions/{asset}",
]

# CrypNuevo setup recommendations per regime
_REGIME_SETUP_MAP = {
    "trending_low_vol": [
        "Setup 1: Range Extreme Deviation (sweep of range extremes likely)",
        "Setup 11: Stop-Loss Zone Sweep (stops clustered at obvious levels)",
        "Setup 18: Liquidity-Run Fade (textbook breakouts are traps in low vol)",
    ],
    "trending_high_vol": [
        "Setup 2: Wick Fill / Wick Magnet (large imbalances left by momentum)",
        "Setup 9: 100% Wick-Fill Continuation (if 50% fill holds)",
        "Setup 10: News Imbalance (wait for second structure after event)",
    ],
    "ranging": [
        "Setup 1: Range Extreme Deviation (full range playbook)",
        "Setup 5: Full Range Deviation Reversal",
        "Three Taps Pattern (watch for 3rd tap at range extreme)",
        "Setup 7: Support-Box Sweep to Mid-Range",
    ],
    "choppy": [
        "NO SETUP — flat/choppy = no man's land. Wait for range or trend to develop.",
    ],
}


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


def _extract_regime_label(data: dict | list) -> str | None:
    """Try to extract a regime string from whatever LORE returns."""
    if isinstance(data, dict):
        for key in ("regime", "current_regime", "label", "type", "state", "condition"):
            if key in data and isinstance(data[key], str):
                return data[key].lower()
        # Nested
        if "current" in data and isinstance(data["current"], dict):
            return _extract_regime_label(data["current"])
    if isinstance(data, list) and data:
        return _extract_regime_label(data[-1])
    return None


def print_markdown(result: tuple[str, dict] | None):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# BTC Volatility Regime — {now}")
    print()

    if not result:
        print("## Status: Endpoint Not Yet Discovered")
        print()
        print("Run `python tools/lore/discover.py` to map available endpoints.")
        return

    ep, data = result
    regime = _extract_regime_label(data)

    print(f"## Source: `{ep}`")
    print()
    print("## Current Regime")
    print(f"- **Label:** {regime or 'unknown — check raw output'}")
    print()

    if regime:
        best_match = None
        for key in _REGIME_SETUP_MAP:
            if key in regime:
                best_match = key
                break

        if best_match:
            print("## CrypNuevo Setup Recommendations For This Regime")
            for s in _REGIME_SETUP_MAP[best_match]:
                print(f"- {s}")
        else:
            print("## Setup Guidance")
            print("Regime label not recognized — review raw data and match to CrypNuevo playbook manually.")
    print()

    print("## Raw Data")
    print("```json")
    print(json.dumps(data, indent=2)[:1500])
    print("```")
    print()
    print("---")
    print("*Paste this block into your CrypNuevo mentor chat for regime context.*")


def main():
    ap = argparse.ArgumentParser(description="Fetch BTC volatility regime from LORE")
    ap.add_argument("--raw", action="store_true", help="Print raw JSON")
    args = ap.parse_args()

    print("Fetching BTC regime data...", file=sys.stderr)
    result = _try_endpoints(_REGIME_ENDPOINTS, {"symbol": ASSET})

    if args.raw:
        print(json.dumps({"endpoint": result[0] if result else None,
                          "data": result[1] if result else None}, indent=2))
        return

    print_markdown(result)


if __name__ == "__main__":
    main()
