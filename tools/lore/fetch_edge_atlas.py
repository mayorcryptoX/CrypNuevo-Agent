"""
LORE Edge Atlas Fetcher — historical pattern outcomes for BTC setups.

Edge Atlas has 748 maps and 8.3M outcome rows.
This script queries it for a given setup type and conditions.

Usage:
    python tools/lore/fetch_edge_atlas.py --list-maps
    python tools/lore/fetch_edge_atlas.py --map range_low_sweep
    python tools/lore/fetch_edge_atlas.py --map range_low_sweep --funding negative --oi expanding
    python tools/lore/fetch_edge_atlas.py --raw

Options:
    --list-maps     List all available Edge Atlas maps
    --map           Map/setup name to query
    --funding       Filter: positive | negative | neutral
    --oi            Filter: expanding | contracting
    --raw           Print raw JSON
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

ASSET = "BTC"

_ATLAS_LIST_ENDPOINTS = [
    "/v1/edge-atlas/maps",
    "/v1/edge-atlas",
    "/edge-atlas/maps",
    "/edge-atlas",
    "/v1/atlas/maps",
    "/atlas/maps",
    "/v1/atlas",
]

_ATLAS_QUERY_ENDPOINTS = [
    "/v1/edge-atlas/maps/{map}",
    "/v1/edge-atlas/{map}",
    "/edge-atlas/maps/{map}",
    "/edge-atlas/{map}",
    "/v1/atlas/maps/{map}",
    "/atlas/maps/{map}",
    "/v1/atlas/{map}",
]

_ATLAS_SEARCH_ENDPOINTS = [
    "/v1/edge-atlas/search",
    "/v1/edge-atlas/query",
    "/edge-atlas/search",
    "/v1/atlas/search",
    "/v1/atlas/query",
]


def _try_list(params: dict) -> tuple[str, dict] | None:
    for ep in _ATLAS_LIST_ENDPOINTS:
        try:
            data = lore.get(ep, params=params)
            return ep, data
        except Exception as e:
            if "404" not in str(e):
                print(f"  [{ep}] {e}", file=sys.stderr)
    return None


def _try_query(map_name: str, params: dict) -> tuple[str, dict] | None:
    for tmpl in _ATLAS_QUERY_ENDPOINTS:
        ep = tmpl.replace("{map}", map_name)
        try:
            data = lore.get(ep, params=params)
            return ep, data
        except Exception as e:
            if "404" not in str(e):
                print(f"  [{ep}] {e}", file=sys.stderr)
    # Also try search endpoint with map as param
    for ep in _ATLAS_SEARCH_ENDPOINTS:
        try:
            p = {**params, "map": map_name, "setup": map_name}
            data = lore.get(ep, params=p)
            return ep, data
        except Exception as e:
            if "404" not in str(e):
                print(f"  [{ep}] {e}", file=sys.stderr)
    return None


def _extract_stats(data: dict | list) -> dict:
    """Try to pull forward returns + win rate + MAE from whatever LORE returns."""
    if isinstance(data, list) and data:
        data = data[0] if isinstance(data[0], dict) else {"raw": data}
    if not isinstance(data, dict):
        return {}

    stats: dict = {}
    for key in ("n", "count", "sample_size", "samples"):
        if key in data:
            stats["sample_size"] = data[key]
    for key in ("win_rate", "win_pct", "accuracy"):
        if key in data:
            stats["win_rate"] = data[key]
    for key in ("forward_return_24h", "ret_24h", "return_24h"):
        if key in data:
            stats["forward_24h"] = data[key]
    for key in ("forward_return_48h", "ret_48h", "return_48h"):
        if key in data:
            stats["forward_48h"] = data[key]
    for key in ("forward_return_72h", "ret_72h", "return_72h"):
        if key in data:
            stats["forward_72h"] = data[key]
    for key in ("mae", "max_adverse_excursion", "max_drawdown", "mdd"):
        if key in data:
            stats["mae"] = data[key]
    for key in ("vs_control", "edge_vs_control", "alpha", "control_diff"):
        if key in data:
            stats["vs_matched_control"] = data[key]
    return stats


def print_maps(result: tuple[str, dict] | None):
    if not result:
        print("Could not reach Edge Atlas. Run `discover.py` to map the API first.")
        return
    ep, data = result
    print(f"# LORE Edge Atlas — Available Maps")
    print(f"Source: `{ep}`")
    print()
    print("```json")
    print(json.dumps(data, indent=2)[:3000])
    print("```")


def print_markdown(map_name: str, result: tuple[str, dict] | None, funding: str, oi: str):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# Edge Atlas: BTC / {map_name} — {now}")
    print()

    if not result:
        print("## Status: Endpoint Not Yet Discovered")
        print()
        print("Run `python tools/lore/discover.py` first. Then run `--list-maps` to see available map names.")
        return

    ep, data = result
    stats = _extract_stats(data)

    print(f"## Query")
    print(f"- Map: `{map_name}`")
    print(f"- Asset: BTC")
    if funding:
        print(f"- Funding filter: {funding}")
    if oi:
        print(f"- OI filter: {oi}")
    print()

    print("## Statistics")
    if stats:
        print(f"| Metric | Value |")
        print(f"|---|---|")
        for k, v in stats.items():
            label = k.replace("_", " ").title()
            print(f"| {label} | {v} |")
    else:
        print("Could not auto-extract stats — review raw data below.")
    print()

    print("## CrypNuevo Interpretation")
    print()
    n = stats.get("sample_size", "?")
    wr = stats.get("win_rate", "?")
    ret24 = stats.get("forward_24h", "?")
    mae = stats.get("mae", "?")
    ctrl = stats.get("vs_matched_control", "?")
    print(f"- **Sample size (N):** {n} historical occurrences")
    print(f"- **Win rate:** {wr}")
    print(f"- **Median forward return 24h:** {ret24}")
    print(f"- **Max adverse excursion (MAE):** {mae} — place stops beyond this")
    print(f"- **vs Matched Control:** {ctrl} — positive = setup has real edge vs random")
    print()
    print("*Use sample size (N) to judge reliability. N < 20 = treat as anecdotal. N > 50 = statistically meaningful.*")
    print()

    print("## Raw Data")
    print("```json")
    print(json.dumps(data, indent=2)[:2000])
    print("```")
    print()
    print("---")
    print("*Paste this into your CrypNuevo mentor chat for quantitative setup validation.*")


def main():
    ap = argparse.ArgumentParser(description="Query LORE Edge Atlas for BTC setup outcomes")
    ap.add_argument("--list-maps", action="store_true", help="List all available Edge Atlas maps")
    ap.add_argument("--map", default="range_low_sweep",
                    help="Edge Atlas map/setup name (default: range_low_sweep)")
    ap.add_argument("--funding", choices=["positive", "negative", "neutral"],
                    help="Filter by funding rate direction")
    ap.add_argument("--oi", choices=["expanding", "contracting"],
                    help="Filter by OI direction")
    ap.add_argument("--raw", action="store_true", help="Print raw JSON")
    args = ap.parse_args()

    if args.list_maps:
        print("Fetching Edge Atlas map list...", file=sys.stderr)
        result = _try_list({"asset": ASSET, "symbol": ASSET})
        print_maps(result)
        return

    params = {"asset": ASSET, "symbol": ASSET}
    if args.funding:
        params["funding"] = args.funding
    if args.oi:
        params["oi"] = args.oi

    print(f"Querying Edge Atlas: {args.map}...", file=sys.stderr)
    result = _try_query(args.map, params)

    if args.raw:
        print(json.dumps({"endpoint": result[0] if result else None,
                          "data": result[1] if result else None}, indent=2))
        return

    print_markdown(args.map, result, args.funding, args.oi)


if __name__ == "__main__":
    main()
