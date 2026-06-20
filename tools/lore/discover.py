"""
LORE API Discovery Script — run this first.

Probes the LORE API to map available endpoints, assets, data types,
and schemas. Writes a human-readable summary to tools/lore/api-map.md
and prints the raw JSON for inspection.

Usage:
    python tools/lore/discover.py

Output:
    tools/lore/api-map.md  — full API map (update this as you learn more)
    stdout                 — live probe results
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Allow running from repo root or from tools/lore/
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import tools.lore.client as lore

# Candidate base URLs to probe (LORE hasn't published docs publicly — try both)
CANDIDATE_BASES = [
    "https://api.loremoney.com",
    "https://loremoney.com/api",
    "https://loremoney.com",
]

# Candidate introspection/catalog endpoints to try
CATALOG_ENDPOINTS = [
    "/",
    "/v1",
    "/v2",
    "/health",
    "/ping",
    "/status",
    "/catalog",
    "/assets",
    "/markets",
    "/instruments",
    "/endpoints",
    "/schema",
    "/docs",
    "/openapi.json",
    "/swagger.json",
    "/v1/catalog",
    "/v1/assets",
    "/v1/markets",
    "/v1/instruments",
    "/v1/schema",
    "/v1/health",
    "/v2/catalog",
    "/v2/assets",
    "/v2/markets",
    # LORE-specific likely paths
    "/edge-atlas",
    "/v1/edge-atlas",
    "/edge-atlas/maps",
    "/v1/edge-atlas/maps",
    "/research-leads",
    "/v1/research-leads",
    "/pattern-replay",
    "/v1/pattern-replay",
    "/regimes",
    "/v1/regimes",
    "/funding",
    "/v1/funding",
    "/oi",
    "/v1/oi",
    "/liquidations",
    "/v1/liquidations",
    "/ohlcv",
    "/v1/ohlcv",
    "/candles",
    "/v1/candles",
]

OUTPUT_FILE = Path(__file__).resolve().parent / "api-map.md"


def probe_endpoint(base: str, endpoint: str) -> tuple[bool, dict | str]:
    """Returns (success, result)."""
    try:
        data = lore.get(endpoint, base_url=base)
        return True, data
    except PermissionError as e:
        return False, f"ACCESS_DENIED: {e}"
    except Exception as e:
        msg = str(e)
        if "404" in msg or "Not Found" in msg:
            return False, "404"
        if "401" in msg:
            return False, "401_AUTH"
        return False, f"ERROR: {msg}"


def find_working_base() -> str | None:
    """Try candidate bases and return the first that gives any non-404 response."""
    print("Detecting LORE API base URL...")
    for base in CANDIDATE_BASES:
        try:
            result = lore.get("/", base_url=base)
            print(f"  ✓ Reachable: {base}")
            return base
        except PermissionError:
            # 401/403 means the base is real, auth is the issue
            print(f"  ✓ Reachable (auth required): {base}")
            return base
        except Exception as e:
            if "401" in str(e) or "403" in str(e):
                print(f"  ✓ Reachable (auth required): {base}")
                return base
            print(f"  ✗ {base}: {e}")
    return None


def main():
    print("=" * 60)
    print("LORE API Discovery")
    print("=" * 60)

    # Step 1: verify key is set
    try:
        import tools.lore.client as c
        c._get_key()
        print("✓ API key found in environment\n")
    except EnvironmentError as e:
        print(f"\n❌ {e}\n")
        sys.exit(1)

    # Step 2: find working base URL
    base = find_working_base()
    if not base:
        print("\n❌ Could not reach any LORE API base URL.")
        print("Check your internet connection or contact LORE support for the correct base URL.")
        sys.exit(1)

    print(f"\nUsing base: {base}\n")

    # Step 3: probe all candidate endpoints
    hits: dict[str, dict | str] = {}
    misses: list[str] = []

    print("Probing endpoints...")
    for ep in CATALOG_ENDPOINTS:
        ok, result = probe_endpoint(base, ep)
        if ok:
            print(f"  ✓ {ep}")
            hits[ep] = result
        elif result not in ("404", "401_AUTH"):
            # Non-404 failure — still interesting
            print(f"  ? {ep} → {result}")
            hits[ep] = result
        else:
            misses.append(ep)

    print(f"\nFound {len(hits)} responsive endpoints, {len(misses)} returned 404/auth.\n")

    # Step 4: write api-map.md
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# LORE API Map",
        f"",
        f"Generated: {now}",
        f"Base URL: {base}",
        f"",
        f"Run `python tools/lore/discover.py` to regenerate.",
        f"",
        f"---",
        f"",
        f"## Responsive Endpoints",
        f"",
    ]

    for ep, result in hits.items():
        lines.append(f"### `{ep}`")
        lines.append("")
        if isinstance(result, dict):
            lines.append("```json")
            lines.append(json.dumps(result, indent=2)[:2000])  # cap at 2k chars
            lines.append("```")
        else:
            lines.append(f"> {result}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Endpoints That Returned 404",
        "",
        "These were probed but did not exist on this API version:",
        "",
    ]
    for ep in misses:
        lines.append(f"- `{ep}`")

    lines += [
        "",
        "---",
        "",
        "## Next Steps",
        "",
        "1. Review the responsive endpoints above.",
        "2. Update `tools/lore/client.py` BASE_URL if the correct base is different.",
        "3. Run individual fetchers: `fetch_market.py`, `fetch_liquidations.py`, etc.",
        "4. Update this file manually as you discover more endpoint patterns.",
    ]

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Wrote api-map.md → {OUTPUT_FILE}")

    # Step 5: print hit summary to stdout
    if hits:
        print("\nTop-level keys found across all responses:")
        all_keys: set[str] = set()
        for result in hits.values():
            if isinstance(result, dict):
                all_keys.update(result.keys())
        for k in sorted(all_keys):
            print(f"  - {k}")

    print("\nDone. Open tools/lore/api-map.md for the full report.")


if __name__ == "__main__":
    main()
