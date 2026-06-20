"""
LORE Pattern Replay — Find historical BTC analogs to current conditions.

Answers: "When has BTC done this exact thing before, and what happened next?"

Usage:
    python tools/lore/research_analogs.py --describe "BTC swept range lows, funding negative, OI expanding, 4h close above support"
    python tools/lore/research_analogs.py --describe "BTC at weekly 50MA, rejected twice, forming M-pattern"
    python tools/lore/research_analogs.py --n 10
    python tools/lore/research_analogs.py --raw
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

ASSET = "BTC"

_REPLAY_ENDPOINTS = [
    "/v1/pattern-replay",
    "/v1/pattern-replay/search",
    "/v1/pattern-replay/match",
    "/pattern-replay",
    "/pattern-replay/search",
    "/v1/replay",
    "/v1/replay/search",
    "/v1/analogs",
    "/v1/analogs/search",
    "/v1/similar",
    "/v1/match",
    "/v1/patterns/search",
    "/v1/patterns/match",
]


def _try_replay(description: str, n: int) -> tuple[str, dict] | None:
    params = {
        "asset": ASSET,
        "symbol": ASSET,
        "query": description,
        "description": description,
        "n": n,
        "limit": n,
    }
    body = {
        "asset": ASSET,
        "symbol": ASSET,
        "query": description,
        "description": description,
        "n": n,
        "limit": n,
    }
    for ep in _REPLAY_ENDPOINTS:
        # Try GET first
        try:
            data = lore.get(ep, params=params)
            return ep, data
        except Exception as e:
            if "404" not in str(e) and "405" not in str(e):
                print(f"  GET [{ep}] {e}", file=sys.stderr)
        # Try POST for search-style endpoints
        if "search" in ep or "match" in ep or "replay" in ep:
            try:
                data = lore.post(ep, body=body)
                return ep, data
            except Exception as e:
                if "404" not in str(e) and "405" not in str(e):
                    print(f"  POST [{ep}] {e}", file=sys.stderr)
    return None


def print_markdown(description: str, result: tuple[str, dict] | None, n: int):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"# LORE Pattern Replay: BTC Analogs — {now}")
    print()
    print(f"**Query:** {description}")
    print(f"**Top N:** {n}")
    print()

    if not result:
        print("## Status: Endpoint Not Yet Discovered")
        print()
        print("Pattern Replay requires the correct endpoint. After running `discover.py`,")
        print("update `_REPLAY_ENDPOINTS` in this file with the confirmed path.")
        return

    ep, data = result
    print(f"## Source: `{ep}`")
    print()

    # Try to extract analog entries
    analogs = []
    if isinstance(data, list):
        analogs = data
    elif isinstance(data, dict):
        for key in ("analogs", "matches", "results", "patterns", "data", "similar"):
            if key in data and isinstance(data[key], list):
                analogs = data[key]
                break

    if analogs:
        print(f"## Top {len(analogs)} Historical Analogs")
        print()
        for i, analog in enumerate(analogs[:n], 1):
            if not isinstance(analog, dict):
                continue
            date = analog.get("date") or analog.get("timestamp") or analog.get("time") or f"Analog {i}"
            ret = analog.get("forward_return") or analog.get("return") or analog.get("outcome") or "—"
            context = analog.get("context") or analog.get("regime") or analog.get("conditions") or ""
            print(f"### {i}. {date}")
            if context:
                print(f"- Context: {context}")
            print(f"- Forward return: **{ret}**")
            # Print remaining fields
            for k, v in analog.items():
                if k not in ("date", "timestamp", "time", "forward_return", "return",
                             "outcome", "context", "regime", "conditions"):
                    print(f"- {k}: {v}")
            print()
    else:
        print("## Raw Data")
        print("```json")
        print(json.dumps(data, indent=2)[:2000])
        print("```")

    print("## CrypNuevo Interpretation")
    print()
    print("Review each analog for the follow-through pattern:")
    print("- **Same sweep + reclaim → sustained move:** High-probability confirmation")
    print("- **Swept + reclaim → chopped:** Caution — wait for stronger trigger")
    print("- **No sustained follow-through in most analogs:** Lower your size or skip")
    print()
    print("---")
    print("*Paste this into your CrypNuevo mentor chat for historical analog context.*")


def main():
    ap = argparse.ArgumentParser(description="Find historical BTC analogs via LORE Pattern Replay")
    ap.add_argument("--describe", default="BTC swept range lows, funding negative, OI expanding",
                    help="Natural language description of current market conditions")
    ap.add_argument("--n", type=int, default=5, help="Number of analogs to return (default: 5)")
    ap.add_argument("--raw", action="store_true", help="Print raw JSON")
    args = ap.parse_args()

    print(f"Searching for BTC analogs: '{args.describe}'...", file=sys.stderr)
    result = _try_replay(args.describe, args.n)

    if args.raw:
        print(json.dumps({"endpoint": result[0] if result else None,
                          "data": result[1] if result else None}, indent=2))
        return

    print_markdown(args.describe, result, args.n)


if __name__ == "__main__":
    main()
