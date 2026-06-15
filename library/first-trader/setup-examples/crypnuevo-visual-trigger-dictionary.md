# CrypNuevo Visual Trigger Dictionary

Created: 2026-06-13

## Purpose

This file links repeated CrypNuevo setup concepts to local chart screenshots captured from public X media. It should be used with `crypnuevo-before-after-patterns.md` when teaching the assistant what a trigger looks like visually.

Local screenshot archive:

- `sources/first-trader/chart-screenshots/`
- `sources/first-trader/chart-screenshots/manifest.json`

Current archive size: 46 downloaded chart images across 17 setup themes.

## Trigger Dictionary

| Visual Trigger | Best Local Screenshots | Visual Cues | Mentor Rule |
| --- | --- | --- | --- |
| Range high deviation and retest | `sources/first-trader/chart-screenshots/range-high-deviation-retest/range-high-deviation-retest__2057594557089366448__01.jpg` | Range highs marked, price back under the high, retest zone, invalidation above range highs, liquidity pool below. | Do not short only because price touched range high. Wait for deviation/return inside, retest/rejection, and clear invalidation. |
| 50% wick-fill objective | `sources/first-trader/chart-screenshots/major-wick-fill/major-wick-fill__1865821132051423658__01.jpg` | Large wick with a horizontal 50% level marked as the first target. | Treat 50% wick fill as a practical first objective. Only expect 100% if context still supports continuation. |
| Wick fill plus liquidation reversal | `sources/first-trader/chart-screenshots/wicks-liquidations-reversal/wicks-liquidations-reversal__1874863094838476946__01.jpg` | Range lows/highs, exact liquidation/reversal level, wick through the level, bounce away from liquidity. | Stronger reversal evidence appears when wick fill and liquidation level converge. Reaction matters after the sweep. |
| Conservative entry after sweep | `sources/first-trader/chart-screenshots/invalidated-entry-new-wick/invalidated-entry-new-wick__2019119406719135830__01.jpg` | Weekly chart, sharp sweep below support, marked conservative/safe entry after reclaim. | If longing a sweep is risky, safer entry waits for reclaim/close back above the key level. |
| EMA retest trigger | `sources/first-trader/chart-screenshots/ema-retest-trigger/ema-retest-trigger__1875979872881013058__01.jpg` | 4h50EMA retest area after breakout, projected false move, acceptance above EMA. | EMA retest is useful when price recently broke away and returns to test it. Acceptance above is the trigger, not the EMA touch. |
| Dual trigger at resistance | `sources/first-trader/chart-screenshots/dual-trigger-at-resistance/dual-trigger-at-resistance__1863291992073179389__01.jpg` | Resistance level with both upside and downside trigger possibilities. | At key resistance, map both paths: reclaim and hold for long, sweep/fail back below for short. |
| Range rotation with invalidation | `sources/first-trader/chart-screenshots/range-rotation-invalidates-flips/range-rotation-invalidates-flips__2035744069960249780__01.jpg` | LTF rotation level, invalidation/flip condition above the level. | A directional range plan should include a hard level where the idea is invalidated or flips. |
| Range low overextension | `sources/first-trader/chart-screenshots/range-low-overextension/range-low-overextension__2063657770243555470__01.jpg` | Price at multi-month range lows after sharp drop, planned mid-range/range-high path. | Range low alone is not enough; bounce case improves when the drop is stretched and liquidity above is visible. |
| Failed setup / news break | `sources/first-trader/chart-screenshots/wrong-setup-news-break/wrong-setup-news-break__2062145223501709612__01.jpg` | Level breaks through the planned zone after macro/news shock. | Technical wick/level setup can fail when news overrides the chart. Acknowledge wrong setup and rebuild from new structure. |
| Three-wick cleanup | `sources/first-trader/chart-screenshots/three-wicks-range-high-short/three-wicks-range-high-short__1886136109228249308__01.jpg` | Multiple unresolved wicks across the range, swing short from range high toward lower wick targets. | Several unresolved wicks can define sequential cleanup targets, especially from range extremes. |
| Before/after wick bounce | `sources/first-trader/chart-screenshots/before-after-wick-bounce/before-after-wick-bounce__1811019364063236238__01.jpg` | Before/after image showing wick fill, bounce, and liquidation target hit. | This is a clean teaching example for wick fill first, reaction second, then next liquidity target. |
| Three Taps Pattern at range extreme | No local screenshot yet — see source thread https://x.com/CrypNuevo/status/2066280050085777618 (tweet 2/5 shows historical examples) | Range low/high marked with three labelled touches. Second or third tap is a wick/deviation below/above the level (order varies). After third tap, price rotates away from the extreme. | Three touches of the same extreme create the setup — not one or two. Tap 2 and Tap 3 can be a retest or a deviation in either order; what matters is all three are visible. Deviation tap = stop-loss sweep + breakout-trader trap. Entry only after the third tap confirms (sweep→reclaim or rejection candle). Never enter mid-range between taps. Invalidation = candle acceptance beyond the range extreme. |
| 1W50EMA plus wick fill | `sources/first-trader/chart-screenshots/gold-1w50ema-wick-fill/gold-1w50ema-wick-fill__2064278256308601204__01.jpg` | Gold chart with 1W50EMA and wick-fill confluence. | The HTF EMA plus wick-fill model can apply outside BTC when the structure is clear. |
| Bear-market question at 1W50EMA | `sources/first-trader/chart-screenshots/bear-market-1w50ema-wick/bear-market-1w50ema-wick__1898815785990336932__01.jpg` | 1W50EMA retest and long-wick fill used to avoid premature bear-market conclusion. | 1W50EMA is a context filter. Do not declare regime shift without confluence. |
| News/event week plan | `sources/first-trader/chart-screenshots/news-week-plan/news-week-plan__1853202540889821422__01.jpg` | Election/FOMC week with marked support and safer entry zone. | During major events, use fewer trades and clearer levels; wicks can trigger entries, but only with a plan. |

## Visual Pattern Notes

### Acceptance Beats Touch

The strongest charts distinguish the level from the trigger. A touch creates attention; acceptance, reclaim, candle close, return inside, or retest creates the trade condition.

### Invalidation Is Drawn On The Chart

Several screenshots place invalidation directly on the chart. This is important for the mentor assistant: it should ask where the setup is wrong before discussing targets.

### Liquidity Zones Are Often Boxed

CrypNuevo often marks liquidity as a box rather than a single line. Reviews should avoid over-precise entries when the source chart shows a zone.

### The Best Charts Combine Factors

The highest-signal screenshots usually combine:

- range extreme
- wick fill
- liquidation pool
- EMA behavior
- retest/rejection or acceptance
- invalidation

One isolated factor is weaker.

## Screenshot Harvest Notes

Downloaded groups:

- `gold-1w50ema-wick-fill`
- `range-low-overextension`
- `wrong-setup-news-break`
- `range-high-deviation-retest`
- `range-rotation-invalidates-flips`
- `weekly-wick-fill-50-percent`
- `invalidated-entry-new-wick`
- `three-wicks-range-high-short`
- `range-triggers-daytrade`
- `ema-retest-trigger`
- `wicks-liquidations-reversal`
- `major-wick-fill`
- `dual-trigger-at-resistance`
- `news-week-plan`
- `before-after-wick-bounce`
- `short-squeeze-projection`
- `bear-market-1w50ema-wick`

## Next Cleanup Pass

1. Rename the very best 15 screenshots with human-readable labels.
2. Add status IDs and source URLs to every row in this dictionary.
3. Create image contact sheets for faster visual review.
4. Separate "before chart" and "after chart" files when a status contains both.
5. Add failed/no-entry screenshots to balance the winning examples.
