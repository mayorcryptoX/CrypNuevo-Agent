# CrypNuevo Visual Chart Style — How He Actually Draws His Trades

Created: 2026-06-13

## Purpose

This note is built from **direct visual inspection of his chart frames** (not transcripts). It catalogs his on-chart annotation vocabulary so the mentor agent can read a chart the way he marks one and describe setups in his visual language. Evidence is sampled high-resolution frames (1280×720) extracted from the videos.

Frame archives (20 frames + a contact sheet per video):
- `sources/first-trader/videos/chart-frames/batch-011-videos-131-137/`
- `sources/first-trader/videos/chart-frames/batch-012-videos-138-151/`
- Older, consistent style: `sources/first-trader/videos/chart-frames/batch-007..010/`

Style is **remarkably consistent from 2023 to 2026** — the same color code, the same box/arrow grammar.

## Chart Environment

- **Platform:** TradingView Pro, dark theme. Primary symbol **BTC/USDT on Binance**; cross-checks Coinbase for wick validity; charts equities (NVIDIA, Google on NASDAQ) as analogs with the same toolkit.
- **Timeframes:** 4h and 1D for structure/execution, **1W for bull/bear regime**. He switches the 50MA timeframe live to match.
- **Always-loaded indicators:** his own **"CrypNuevo Indicator V.1"** (settings string visible on charts: `LP ATR 30 ... Half Fill 1,000 98 3 GMT+1 ... London 0901-1501 ... New York 1501-2101 ... Asia 0001-0901 ... 50MA`), a plain **EMA**, and for macro work the **M2 Global Liquidity Index** and a **BTC Mining Cost** indicator (seen loaded in the indicator panel, e.g. frame `144-zLH0O8tNENk/frame-1123.jpg`).

## The Color/Shape Grammar (his visual vocabulary)

| Element | Looks like | Meaning |
|---|---|---|
| **Purple/blue smooth curve** | One weaving line on every chart | The **50 MA** ("50 mean") — the backbone, on 1h/4h/1D/1W |
| **Yellow solid horizontal lines, labeled** | "Range highs", "Mid range", "Range lows" | The core **range map** |
| **Yellow/orange dotted horizontals with price tags** | Thin dotted lines between the solids | **Range quarters** and secondary levels |
| **Named orange/yellow levels** | "HTF Resistance", "Local Resistance", "Local Support", "Local Low" | Key decision levels (e.g. HTF resistance pinned to round numbers like 100,000) |
| **White rectangle** | Box around a price zone, often labeled "RESISTANCE" / "SUPPORT" | Liquidity/structure treated as a **zone, not a line** |
| **Orange rectangle, "STOP LOSS ZONE"** | Box just above resistance / below support | Where retail stops sit — the **hunt target** |
| **Teal/green shaded box** | Big translucent block, e.g. "Liquidity Pool from liquidation cascade" | An **imbalance / liquidity pool** to be retraced |
| **Magenta/purple rectangle + down-arrow** | Small box at a wick / Local Low | **Wick-fill / target box** (where price is projected to go) |
| **Yellow box label "RANGE"** | Text tag inside the range | Marks the active range |
| **Yellow box "Exit sign: 1W50EMA S/R flip"** | Tag at a weekly 50MA breakdown | His **bear-market regime trigger** |
| **Hand-drawn white path/arrows** | Free-drawn V's and zigzags | **Projected route** from a level to a liquidity target |
| **Circle / ellipse (often "?" or "Liquidity run")** | Loop around a candle cluster | A **trap, retest, or liquidity run** decision point |
| **Yellow horizontal lines with ✓ check marks** | 2–3 stacked lines below range lows | His actual **laddered limit orders**; a ✓ = the order filled |
| **White box + up-arrow under support** | Small box with an arrow pointing up | A **buy / bounce zone** (esp. weekly 50MA retests) |

## Recurring Visual Setup Signatures

These are the repeated "pictures" his charts form. The agent should recognize and reproduce them.

### 1. The Range Map (his default starting picture)
Yellow **Range highs / Mid range / Range lows** + dotted quarters, candlesticks, the purple 50MA weaving through, current price as a dashed line.
Example: `batch-011.../133-V7aunrT9TPc/frame-0233.jpg` — BTC 4h with all four range levels labeled.

### 2. Liquidity Run → Wick-Fill Projection
An **ellipse labeled "Liquidity run" with a "?"** around a deviation above the range, then a **white zigzag arrow** projecting down through Local Support into a **magenta wick-fill box** at the Local Low.
Example: `batch-012.../151-cYQgoHJSvuI/frame-0230.jpg` — the cleanest single illustration of his whole method (HTF Resistance 100k, RANGE box, Local Support/Low, liquidity-run ellipse, projection into the 80–83k target box).

### 3. Stop-Loss-Zone Hunt
A white **"RESISTANCE"** box with an orange **"STOP LOSS ZONE"** box stacked above it and **up-arrows** running into the zone — price sweeps the stops, then the real decision (accept = continue, reject = trap).
Example (historical, shows style continuity): `batch-009.../102-eM9QmrjPsbo-contact-sheet.jpg`.

### 4. Weekly 50MA Regime Read
1W chart, purple 50MA, **white boxes + up-arrows at each 50MA retest** (the bull-market buy zones), and a yellow **"Exit sign: 1W50EMA S/R flip"** box at the one breakdown that defined a bear phase.
Example: `batch-011.../137-cnwkr1vyol0/frame-0512.jpg`.

### 5. Laddered Staged Entry (execution close-up)
On the 4h, **two-to-three yellow limit-order lines below the range lows** (e.g. 100,350 / 99,158 / 97,108) with **✓ marks on the filled ones**, a teal liquidity-pool box overhead, and a small down-then-up projection.
Example: `batch-012.../140-5bMizMQu7_4/frame-0747.jpg` — his actual orders, drawn.

### 6. Equity Analog
NVIDIA/Google weekly with the **same 50MA + horizontal support + a circle around the swept low + a V-projection** back to highs — used to argue BTC will sweep lows then continue.
Example: `batch-012.../144-zLH0O8tNENk/frame-1123.jpg`.

### 8. Three Taps Pattern (range extreme — named by him Jun 2026)

Range map with three distinct touches of the same extreme (low or high). Two of the three touches are retests (price returns to the level cleanly); one is a deviation (a wick that briefly exceeds the level, sweeping stops). The order of retest vs deviation among taps 2 and 3 does not matter — both count.

Visually on his chart: the range low horizontal is labeled, three arrows or circles mark each touch, the deviation tap shows as a wick piercing below the range low, and a projected white path curves back up to mid-range after the third tap.

White-path annotation after tap 3 points from the range low upward — same "V" shape as a standard wick-fill projection but originating from the range extreme, not a single candle wick.

Source: `library/first-trader/setup-examples/crypnuevo-three-taps-range-pattern.md`
No local screenshot yet; examples shown in tweet 2/5 of https://x.com/CrypNuevo/status/2066280050085777618.

### 7. Hyblock Liquidation Read (separate tool, not TradingView)
The Hyblock "Liquidation Levels" screen: liquidation lines **colored by price** (blue/purple shorts above, warm red/pink longs below), a **magnitude histogram on the right**, and a **DELTA panel at the bottom** in billions (his >20–25B = squeeze threshold).
Example: `batch-012.../142-JGsADClc17s/frame-0951.jpg`.

## How To Read A Chart "Like Him" (visual checklist)

1. Put the **50MA** on and note which timeframe's 50MA price is reacting to.
2. Draw the **range**: highs, lows, mid, quarters (solid for majors, dotted for quarters).
3. Box the **liquidity zones** (wicks, liquidation-cascade pools) rather than using single lines.
4. Mark where **stops sit** (above resistance / below support) as the hunt target.
5. Identify if price is doing a **liquidity run** (circle + "?") before the real move.
6. Project the **route** as a hand-drawn path from the current level to the liquidity/wick target — V (sweep→recover) or zigzag (deviation→continuation).
7. Place the **entry as laddered limits** at the highest-confluence level, not one fixed price.
8. Confirm with **Hyblock** (delta + liquidation clusters) as context, never as the trigger.

## Cross-Checks Done

- Frames span batches 9 (2024), 11 (late-2024/early-2025), and 12 (late-2025/2026); the grammar is identical throughout, which is strong evidence this is a stable, deliberate system rather than ad-hoc drawing.
- Every visual element here corresponds to a transcript claim in `crypnuevo-trading-dna.md` and the batch notes, so the words and the charts agree.

## Possible Next Visual Work

- Build labeled "hero" crops of the 7 signature setups above for fast reference.
- Frame-sample the 41 Shorts (often single-setup explainers).
- Extract high-res frames for batches 7–10 (existing frames are only 320×180); re-run `_extract_frames.py` against `video-files/` if deeper historical visual detail is wanted.
