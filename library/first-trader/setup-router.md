# CrypNuevo Setup Router — Chart Conditions → Playbook Setup

Created: 2026-07-03 · Fulfills IMPROVEMENT-PLAN Phase 2.4

## Purpose

A decision tree that maps what is actually visible on a chart to the numbered setups in `profiles/first-trader.md`. The mentor runs this silently before answering, so the review names the specific setup, trigger, and invalidation instead of a generic liquidity read.

Rules of use:

1. Run the DNA Decision Pipeline first (state → liquidity map → HTF → stops → target-vs-entry → trigger → invalidation → targets → risk). The router assumes those facts are known.
2. More than one setup can match; name the primary and mention the secondary as confluence.
3. If NO branch matches with a definable trigger + invalidation, the answer is **no trade / watchlist only** (`crypnuevo-antipatterns-no-trade-rules.md`). Never force a route.
4. Filters that override any branch: weekend/bank-holiday thinness, CPI/FOMC/Powell within the session (Setup 10 rules), mid-range position ("no man's land" — flat), crowded/late entry chasing into opposing liquidity.

## Step 0 — Global gates (check before routing)

| Question | If YES |
| --- | --- |
| Is a high-impact event (CPI/FOMC/Powell/labor) imminent or just released? | Only Setup 10 logic applies. Wait 30-45 min, trade the second structure, be flat into the release. |
| Is it a weekend or bank holiday? | Distrust the move; expect retrace/CME-gap fill early week. Usually watchlist only. |
| Is price mid-range with no independent trigger? | Flat. Name the extremes/quarters you'd act at instead. |
| Is the obvious move a vertical impulse into thin conditions with liquidation clusters on both sides? | Consider **Bart Simpson double-sided run** (profile Strategy Map): don't chase the impulse; plan the full retrace as a scenario. |

## Step 1 — What is the market state?

- **RANGING / CONSOLIDATING** → go to Step 2A.
- **TRENDING** → go to Step 2B.
- **AT/AROUND A KEY 50MA** (1W/1D/4h/1h) → go to Step 2C.
- **POST-NEWS IMPULSE** → Setup 10 (News Imbalance After FOMC/CPI).
- **ALTCOIN QUESTION** (not BTC itself) → go to Step 2D.

## Step 2A — Ranging market

| Observed condition | Route to |
| --- | --- |
| Price at range high/low or liquidation cluster; no sweep yet | **Setup 1** (Range Extreme Deviation) — watch for failed acceptance / retest-rejection. If untested, "WAIT FOR" the sweep, not a touch entry. |
| Price swept beyond the range edge and returned inside | **Setup 5** (Full Range Deviation Reversal); if the swept level was an obvious round number/breakout level, also **Setup 8** (Manipulation Sweep Reversal). |
| Third visit to the SAME extreme (two prior taps visible; one retest + one deviation in either order) | **Setup 19** (Three Taps Range Rotation) — entry after the third tap confirms (sweep→reclaim or rejection with momentum loss). |
| Sweep of equal lows / support box then reclaim, second low holding higher | **Setup 16** (W-Pattern / Double-Bottom Long); if the sweep hit a marked support/liquidity box, **Setup 7** (Support-Box Sweep To Mid-Range) covers the mid-range target logic. |
| Sweep above equal highs / range high, failed acceptance, second high lower | **Setup 17** (M-Pattern / Double-Top Short). |
| Obvious S/R with retail stops clustered just beyond it; sweep into that zone then return | **Setup 11** (Stop-Loss Zone Sweep). |
| Large unfilled wick/imbalance inside or near the range | **Setup 2** (Wick Fill / Wick Magnet); manage manually — limit at 50%, judge the reaction, no hard stop in the fill zone. |
| 50% fill done, no strong rejection, consolidation holding | **Setup 9** (100% Wick-Fill Continuation). |
| Heatmap/Hyblock/order book shows a dense cluster near a chart level | **Setup 6** (Order-Book Liquidity Target) as target/confluence; delta >20-25B = squeeze context. |
| "Breakout" through a textbook trendline, round number, or equal highs/lows into thin/trapped liquidity | **Setup 18** (Liquidity-Run Fade) — let the run finish, validate the wick cross-exchange, trade the return through the level. |

## Step 2B — Trending market

| Observed condition | Route to |
| --- | --- |
| Clean acceptance in trend direction, no pullback structure | **No trade** — never short against momentum; never chase. Name the level where you'd engage. |
| Impulse + ABC correction, bullish 20/55 EMA cross, 0.618 retest holding | **Setup 20** (early-era Impulse Continuation) — confluence only, pair with a liquidity-based trigger. |
| Trend pausing at a HTF wick/imbalance | **Setup 2 / 9** (wick-fill logic in trend context). |
| Vertical pump, momentum cooling, EMA/support loss + failed sweep of highs | **Setup 17** (M-Pattern) — only after the momentum filter passes; shorting "because it's high" is banned. |
| Obvious ascending trendline with repeated touches (stop cluster growing beneath) | **Setup 18** (Liquidity-Run Fade) — expect the sweep below before continuation; distrust the textbook line. |

## Step 2C — At a key 50MA

| Observed condition | Route to |
| --- | --- |
| 4h50EMA lost; two 4h candles testing it as resistance | **Setup 12** (Two-Candle 4h50EMA Gate, short side). |
| 4h50EMA reclaimed and holding as support | **Setup 12** (long side) — cancels the short gate. |
| Repeated wicks into the EMA with no further progress (absorption) | **Setup 3** (EMA Supported Reversal After Absorption) — MM position-building tell. |
| Price right BELOW a HTF resistance (e.g. weekly 50MA) | **No long** — hard rule. Wait for acceptance above, then the retest is the long trigger. |
| 1W50EMA deviation on a weekly chart | Regime check, not a trade: bear only confirmed by weekly close below + retest as resistance. |

## Step 2D — Altcoins

| Observed condition | Route to |
| --- | --- |
| BTC stable/up, BTC.D at resistance or rejecting, alt lagged BTC | **Setup 13** (BTC.D Fade For Altcoin Catch-Up). |
| Alt at HTF range low after drawdown, BTC not breaking down | **Setup 4** (Altcoin HTF Range Preparation) — zones of interest, not immediate entries. |
| BTC near HTF support, ETH/alts showing relative strength, clear spot zone | **Setup 15** (Spot Buying Opportunity). |
| XRP and/or DOGE pumping far more than the rest of the alt market | **Reversal tell** (Cross-Asset Tells) — forced move, often a local/market top; cut long aggressiveness. |
| BTC has not yet reached/reacted at its own level | **Wait** — alts follow BTC; no alt entry before the BTC reaction. |

## Step 3 — Trigger-quality check (applies to every route)

Before quoting the entry, verify:

- **Reaction, not touch**: sweep → reclaim / retest / rejection / acceptance exists or is precisely named as the missing condition.
- **Candlestick validity**: a hammer/shooting-star trigger only counts with wick ≥ 2/3 of the candle AND a confirmation candle (green after hammer, red after shooting star).
- **Cross-exchange wick validation**: a wick that exists on only one exchange is not real liquidity.
- **Session context**: does the session model (Asia/London/NY) support or threaten the route?
- **Invalidation drawn**: exact level/condition where the idea is wrong. No invalidation, no trade.
- **Execution plan**: laddered limits (biggest/lowest at highest confluence), preset TPs (e.g. 66/33), breakeven stop once it runs, flat into news.

## Output contract

The router's result feeds the 7-section review: name the matched setup by number and name in "What Matches Right Now," the failed branch conditions in "What Is Still Missing," and the branch's trigger/invalidation in "Exact Conditions For Entry."
