"""
LORE Setup Research — Historical validation for CrypNuevo setups on BTC.

Given a setup type + market conditions, pulls matched controls and statistics
from LORE Edge Atlas to answer: "does this setup actually work historically?"

Usage:
    python tools/lore/research_setup.py --list-setups
    python tools/lore/research_setup.py --setup range_low_sweep
    python tools/lore/research_setup.py --setup range_low_sweep --funding negative --oi expanding
    python tools/lore/research_setup.py --setup wick_fill_50pct --regime ranging
    python tools/lore/research_setup.py --raw

Mapped to CrypNuevo playbook setups (use --list-setups to see LORE's names):
    range_low_sweep        → Setup 1 / Setup 5 / Setup 7 / Setup 8
    wick_fill              → Setup 2 / Setup 9
    ema_reversal           → Setup 3 / Setup 12
    range_deviation        → Setup 1
    stop_loss_sweep        → Setup 11
    news_imbalance         → Setup 10
    support_reclaim        → Setup 7
    liquidity_run_fade     → Setup 18
    three_taps             → Three Taps Pattern
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.lore.fetch_edge_atlas import _try_list, _try_query, _extract_stats
import tools.lore.client as lore

ASSET = "BTC"

# CrypNuevo setup name → LORE likely map name variants
SETUP_ALIASES = {
    "range_low_sweep":    ["range_low_sweep", "range_low_deviation", "support_sweep", "low_sweep"],
    "range_high_sweep":   ["range_high_sweep", "range_high_deviation", "resistance_sweep", "high_sweep"],
    "wick_fill":          ["wick_fill", "imbalance_fill", "wick_magnet", "gap_fill"],
    "wick_fill_50pct":    ["wick_fill_50", "imbalance_fill_50", "half_fill"],
    "wick_fill_100pct":   ["wick_fill_100", "imbalance_fill_100", "full_fill"],
    "ema_reversal":       ["ema_reversal", "ema_retest", "ma_reversal", "ema_bounce"],
    "stop_loss_sweep":    ["stop_loss_sweep", "sl_sweep", "stop_hunt", "stop_run"],
    "news_imbalance":     ["news_imbalance", "event_imbalance", "event_gap", "news_gap"],
    "support_reclaim":    ["support_reclaim", "support_recovery", "support_flip"],
    "liquidity_run_fade": ["liquidity_run", "liq_run_fade", "false_breakout_fade", "fakeout"],
    "three_taps":         ["three_taps", "triple_tap", "range_triple_touch", "third_tap"],
    "range_deviation":    ["range_deviation", "range_extreme_deviation", "range_extreme"],
}

def _try_aliases(canonical: str, params: dict) -> tuple[str, str, dict] | None:
    """Try all alias names for a setup and return (alias_used, endpoint, data) on first hit."""
    aliases = SETUP_ALIASES.get(canonical, [canonical])
    for alias in aliases:
        result = _try_query(alias, params)
        if result:
            return alias, result[0], result[1]
    return None


def print_research_brief(setup: str, alias: str | None, ep: str | None,
                         data: dict | list | None,
                         funding: str, oi: str, regime: str):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# LORE Setup Research: BTC / {setup}")
    print(f"*Generated: {now}*")
    print()

    if not data:
        print("## Status: No Data Found")
        print()
        print("Possible reasons:")
        print("- Run `discover.py` first to find the correct endpoint")
        print("- Run `fetch_edge_atlas.py --list-maps` to see available map names")
        print("- The setup name might differ in LORE's taxonomy — check `--list-setups`")
        return

    stats = _extract_stats(data)

    print("## Query Parameters")
    print(f"- Asset: BTC")
    print(f"- Setup: `{alias or setup}`")
    print(f"- Endpoint: `{ep}`")
    if funding:
        print(f"- Funding filter: {funding}")
    if oi:
        print(f"- OI filter: {oi}")
    if regime:
        print(f"- Regime filter: {regime}")
    print()

    print("## Historical Statistics")
    print()
    n = stats.get("sample_size", "?")
    wr = stats.get("win_rate", "?")
    ret24 = stats.get("forward_24h", "—")
    ret48 = stats.get("forward_48h", "—")
    ret72 = stats.get("forward_72h", "—")
    mae = stats.get("mae", "—")
    ctrl = stats.get("vs_matched_control", "—")

    print(f"| Metric | Value |")
    print(f"|---|---|")
    print(f"| Sample size (N) | **{n}** |")
    print(f"| Win rate | **{wr}** |")
    print(f"| Median forward return 24h | {ret24} |")
    print(f"| Median forward return 48h | {ret48} |")
    print(f"| Median forward return 72h | {ret72} |")
    print(f"| Max adverse excursion (MAE) | {mae} |")
    print(f"| vs Matched Control | {ctrl} |")
    print()

    print("## CrypNuevo Interpretation")
    print()
    # Sample size guidance
    if isinstance(n, int):
        if n < 10:
            print(f"⚠️  **N={n} is very small — treat as anecdotal, not statistical evidence.**")
        elif n < 30:
            print(f"📊 **N={n} — limited sample. Directional but not robust.**")
        elif n >= 50:
            print(f"✅ **N={n} — meaningful sample size. Results carry statistical weight.**")
    print()

    # MAE guidance for stop placement
    if mae and mae != "—":
        print(f"**Stop/invalidation guidance:** MAE = {mae}.")
        print(f"Place invalidation beyond the MAE to avoid being stopped out by normal noise.")
        print()

    # Edge vs control
    if ctrl and ctrl != "—":
        try:
            ctrl_val = float(str(ctrl).strip("%").strip("+"))
            if ctrl_val > 0:
                print(f"**Setup edge confirmed:** +{ctrl_val}% above matched control — this setup has real edge vs random entries.")
            elif ctrl_val < 0:
                print(f"**Weak edge:** {ctrl_val}% vs matched control — consider waiting for stronger confluence.")
            else:
                print("**Neutral edge vs control** — setup is in line with random entries at this level.")
        except ValueError:
            print(f"**vs Matched Control:** {ctrl}")
    print()

    print("## Raw Data (first 2000 chars)")
    print("```json")
    print(json.dumps(data, indent=2)[:2000])
    print("```")
    print()
    print("---")
    print("*Paste this into your CrypNuevo mentor chat to validate the setup with historical data.*")


def main():
    ap = argparse.ArgumentParser(description="Research BTC setup outcomes via LORE Edge Atlas")
    ap.add_argument("--list-setups", action="store_true",
                    help="List LORE's available Edge Atlas map names")
    ap.add_argument("--setup", default="range_low_sweep",
                    help="Setup to research (use --list-setups to see options)")
    ap.add_argument("--funding", choices=["positive", "negative", "neutral"],
                    help="Filter: only look at occurrences where funding was X")
    ap.add_argument("--oi", choices=["expanding", "contracting"],
                    help="Filter: only look at occurrences where OI was X")
    ap.add_argument("--regime", help="Regime filter (e.g. trending_low_vol, ranging)")
    ap.add_argument("--raw", action="store_true", help="Print raw JSON")
    args = ap.parse_args()

    if args.list_setups:
        print("Fetching available Edge Atlas maps...", file=sys.stderr)
        result = _try_list({"asset": ASSET})
        if result:
            print("# Available LORE Edge Atlas Maps (BTC)")
            print()
            print("```json")
            print(json.dumps(result[1], indent=2)[:4000])
            print("```")
            print()
            print("## CrypNuevo Setup Mapping")
            print("Use these map names with `--setup`:")
            for k, v in SETUP_ALIASES.items():
                print(f"  `{k}` → tries: {', '.join(v)}")
        else:
            print("Could not fetch map list. Run `discover.py` first.")
        return

    params = {"asset": ASSET, "symbol": ASSET}
    if args.funding:
        params["funding"] = args.funding
    if args.oi:
        params["oi"] = args.oi
    if args.regime:
        params["regime"] = args.regime

    print(f"Researching: {args.setup}...", file=sys.stderr)
    hit = _try_aliases(args.setup, params)

    if args.raw:
        if hit:
            _, ep, data = hit
            print(json.dumps({"endpoint": ep, "data": data}, indent=2))
        else:
            print(json.dumps({"endpoint": None, "data": None}, indent=2))
        return

    if hit:
        alias, ep, data = hit
        print_research_brief(args.setup, alias, ep, data, args.funding, args.oi, args.regime)
    else:
        print_research_brief(args.setup, None, None, None, args.funding, args.oi, args.regime)


if __name__ == "__main__":
    main()
