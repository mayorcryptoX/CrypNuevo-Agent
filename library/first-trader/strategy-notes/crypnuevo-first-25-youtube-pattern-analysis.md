# CrypNuevo First 25 YouTube Videos: Pattern Analysis

## Scope

- Trader: CrypNuevo
- Source set: first 25 long-form YouTube videos, oldest-first
- Date range: 2023-04-17 to 2023-05-16
- Channel: https://www.youtube.com/@CrypNuevo
- Source notes:
  - `sources/first-trader/videos/youtube-batch-001-oldest-videos-2023-04-17-to-2023-04-21.md`
  - `sources/first-trader/videos/youtube-batch-002-videos-006-to-010-2023-04-22-to-2023-04-26.md`
  - `sources/first-trader/videos/youtube-batch-003-videos-011-to-025-2023-04-27-to-2023-05-16.md`
  - `sources/first-trader/videos/video-006-025-evidence-extract.txt`

This note converts the first 25 videos into a recognition model: what patterns to identify, what confirms them, what invalidates them, and how the strategy behaves across normal sessions, weekends, and macro-event days.

## Core Finding

The first 25 videos do not show a simple indicator strategy. They show a liquidity-first decision system.

His process is:

1. Start with the weekly roadmap, usually from the Sunday update.
2. Identify the market state: range, support test, EMA pivot, wick imbalance, liquidity run, or macro-event holding pattern.
3. Mark liquidity above and below price before choosing direction.
4. Use EMA behavior, session timing, DXY/SPX, macro calendar, and liquidation heatmaps as confluence.
5. Define the next likely target only after deciding which imbalance or liquidity pool is more attractive.
6. Wait for confirmation or accept that the plan is invalidated.

The repeated theme is not "price will go up" or "price will go down." It is "what liquidity is price likely engineering, filling, or trapping?"

## Pattern 1: Wick Fill / Wick Magnet

### Recognition

Look for a large wick left behind by a fast move. He treats the wick as a chart imbalance and liquidity zone.

Strong signs:

- The wick is large relative to surrounding candles.
- The wick sits near a liquidation cluster or prior structure.
- Price has not fully revisited the wick.
- The current market is ranging, retracing, or lacking strong continuation away from the wick.

### Targets

- First practical target: 50% wick fill.
- Full target: 100% wick fill.
- If the wick aligns with a heatmap liquidation zone, the wick target gains weight.

### Confirmation

- Price starts accepting toward the wick rather than rejecting away.
- Lower-timeframe EMA allows the direction, especially 1h50EMA or 4h50EMA.
- Session behavior supports a run toward the wick.
- No fresh opposing imbalance appears that changes the plan.

### Invalidation

- Clean acceptance away from the wick.
- A fresh wick or news event creates a stronger opposite target.
- Price reaches the area but fails to reclaim/reject the needed EMA or range level.

## Pattern 2: Liquidity Pool First, Wick Second

### Recognition

When both a wick and a liquidation pool exist, he often asks which has more incentive to be hit first.

Strong signs:

- Heatmap shows a larger or closer liquidation pool than the wick.
- Price is in a weekend range or tight consolidation.
- Traders are likely positioned heavily in one direction, creating stop-loss fuel.

### Typical Sequence

1. Price ranges or consolidates.
2. Traders build positions and stops.
3. Price runs the nearest or largest liquidity pool.
4. If the move leaves a wick behind, price can later retrace that new wick.
5. After the liquidity pool is hit, the next target may become the old wick or the next pool.

### Recognition Rule

Do not treat a wick target in isolation. Ask whether a larger liquidation pool sits closer or has better positioning incentive.

## Pattern 3: Daily 50EMA As Structural Pivot

### Recognition

In videos 6-25, the daily 50EMA becomes a major BTC state line.

Bullish/supportive state:

- Daily candle closes above daily 50EMA.
- Liquidity sweep below the level quickly reclaims it.
- Price uses daily 50EMA as support after repeated tests.

Bearish/risk state:

- Daily candle closes below daily 50EMA after multiple support holds.
- Retest fails from below.
- Macro data or DXY supports downside.

### Confirmation

- Daily close matters more than an intraday wick.
- A quick loss and reclaim can be a fakeout.
- A clean close below after repeated support tests changes structure.

### Invalidation

- For longs: acceptance below daily 50EMA, especially after a failed reclaim.
- For shorts: sweep below daily 50EMA followed by close/reclaim above it.

## Pattern 4: 1h/4h 50EMA As Execution Gate

### Recognition

He often knows the likely target but still waits because the lower-timeframe EMA blocks execution.

Long-side gate:

- Break above 1h50EMA or 4h50EMA.
- Retest it as support.
- Continue toward liquidity or wick target.

Short-side gate:

- Reject from 1h50EMA or 4h50EMA.
- Lose the EMA and accept below it.
- Continue toward lower liquidity.

### Practical Rule

A target can be correct while the entry is still poor. If price is below lower-timeframe resistance, he often waits for reclaim/retest before longing. If price is above support, he avoids blind shorting into support.

## Pattern 5: Session-Based Liquidity Runs

### Recognition

Asia, London, and New York are part of the edge, especially in normal weekday liquidity.

Repeated models:

- Asia pumps or dumps, London holds/ranges, New York reverses.
- Asia holds, London makes the directional move, New York reverses.
- Asia move can be a trap if later sessions do not accept it.

### Confirmation

- London must hold/range after Asia move for the New York reversal idea to stay alive.
- If London continues the move strongly instead of holding, the reversal setup weakens.
- A session move into a known liquidity pool or wick is more meaningful than a random session candle.

### Invalidation

- Expected holding session fails.
- Price accepts beyond the level instead of deviating.
- The move reaches a stronger next liquidity pool and does not reverse.

## Pattern 6: Weekend Range / Low-Liquidity Trap

### Recognition

Weekend BTC conditions are treated as low-liquidity and less reliable.

Common weekend behavior:

- Range/chop.
- Fakeouts.
- Wicks that set up next-week targets.
- 1h50EMA catch-up before the next real move.

### Practical Rule

Do not apply weekday session logic blindly on weekends. Weekend ranges are often preparation zones where liquidity builds for the next weekday move.

## Pattern 7: Macro Event Holding Pattern

### Recognition

Before FOMC, CPI, or similar high-impact data, price often holds inside a range or around an EMA.

His behavior:

- Expect false moves and spikes.
- Avoid trading shortly before and after FOMC/CPI unless the plan is specific.
- Let the data reveal direction.
- After the event, watch for liquidity pools or wicks left behind by the volatility.

Specific early rule:

- He says he dislikes trading 30 minutes before FOMC and about 45 minutes after the press conference.

### Confirmation

- Post-data reclaim/retest of an EMA or range level.
- Price leaves liquidity behind and later returns to it.
- DXY reacts in a way that supports the BTC direction.

### Invalidation

- Data-driven acceptance through the planned level.
- Violent event candle leaves a fresh imbalance that becomes a better target than the old plan.

## Pattern 8: Liquidity Run Disguised As Reversal

### Recognition

He is suspicious of moves that invite retail into the wrong side.

Red flags:

- Price stops just above or below a major liquidation zone instead of taking it.
- A suspicious wick appears near a huge liquidation cluster.
- The move encourages obvious longs/shorts with stops clustered nearby.
- Price is below resistance but retail is trying to long.

### Interpretation

The move may be designed to increase liquidity before the real run. In video 25, he frames a suspicious wick above a liquidation zone as a run-for-liquidity setup: lure longs, build stops below, then hit the downside target.

### Confirmation

- Price fails to progress after the suspicious wick.
- EMA resistance holds.
- Heatmap shows a clear target where stops/liquidations are likely stacked.

## Pattern 9: Large Candle Imbalance

### Recognition

After an unusually large candle, he tracks the imbalance left by that candle.

Two trade paths:

- Trade the initial move if already positioned or fast enough.
- Trade the retrace/fill of the imbalance left by the candle.

### Confirmation

- Price begins retracing the large candle.
- Lower-timeframe structure supports the retrace.
- No strong EMA or macro barrier blocks the fill.

### Invalidation

- Strong continuation with no reclaim/retrace.
- New structure makes a different liquidity pool more important.

## Pattern 10: Altcoin HTF Preparation And BTC Dominance

### Recognition

The first 25 videos include LINK, ADA, and BTC dominance. These are not short-term altcoin entries; they are high-timeframe preparation.

For altcoins, he maps:

- Monthly/weekly/daily range high.
- Range low.
- Range midpoint.
- Prior liquidity pools.
- Downside and upside imbalances.
- Whether the bottom is actually proven or only hoped for.

BTC dominance filter:

- BTC.D rising: BTC outperforms alts, altcoins are fragile.
- BTC.D falling: altcoins are safer and can outperform.
- Best altcoin environment: BTC up or stable while BTC.D falls.
- Worst altcoin environment: BTC down while BTC.D rises, because altcoins can make new lows.

## Confluence Stack

Strong CrypNuevo-style setups usually combine several of these:

- Liquidity pool or liquidation heatmap target.
- Unfilled wick or candle imbalance.
- Daily/1h/4h 50EMA state.
- Range high/low, prior support/resistance, or range midpoint.
- Session timing.
- DXY inverse pressure and SPX risk context.
- Macro calendar awareness.
- Clear invalidation and no blind entry into support/resistance.

Weak setups usually have only a level touch and no confirmation.

## Decision Tree For Recognizing His Strategy

### Step 1: Define Market State

Ask:

- Is price ranging, trending, consolidating, or reacting to a macro event?
- Is it at daily 50EMA, 1h50EMA, 4h50EMA, range high, range low, or a long wick?
- Is this normal weekday liquidity, weekend liquidity, or news-event volatility?

### Step 2: Mark Liquidity Both Ways

Ask:

- Where are the obvious liquidation pools above and below?
- Which prior wick is unfilled?
- Which large candle imbalance remains?
- Are stops likely sitting above highs or below lows?

### Step 3: Decide The Likely Magnet

Prioritize:

1. Large nearby liquidation pool.
2. Unfilled wick with heatmap confluence.
3. Range extreme or opposite side of range.
4. EMA retest/reclaim area.
5. Macro-event imbalance left behind.

### Step 4: Wait For Execution Gate

For longs:

- Avoid longing directly below 1h/4h EMA resistance unless there is a strong reason.
- Prefer reclaim, retest as support, then continuation.

For shorts:

- Avoid shorting directly above daily/1h/4h support unless support is lost or rejected.
- Prefer rejection, loss, retest from below, then continuation.

### Step 5: Check Invalidation

Invalidate or reduce confidence when:

- The planned session behavior fails.
- Price accepts beyond the level rather than deviating.
- Daily close changes the EMA structure.
- Macro data creates a fresh stronger imbalance.
- A new wick appears that changes the target map.

## High-Confidence Pattern Templates

### Template A: Wick Fill Long

- Setup: downside wick remains unfilled; price is near support or has swept liquidity.
- Confirmation: reclaim/hold of daily or lower-timeframe 50EMA.
- Entry style: wait for reaction/reclaim, not the wick touch alone.
- Targets: 50% wick fill, then 100% if momentum and context support.
- Invalidation: acceptance below support or fresh downside structure.

### Template B: Wick Fill Short

- Setup: upside wick remains unfilled; price is below resistance or after a failed pump.
- Confirmation: rejection from 1h/4h50EMA or range high.
- Targets: 50% and 100% wick fill, or lower liquidation pool.
- Invalidation: reclaim and acceptance above resistance.

### Template C: Liquidity Sweep And Reclaim

- Setup: price runs liquidation below support or above resistance.
- Confirmation: quick return back above/below the key level, preferably with EMA reclaim.
- Targets: opposite liquidity pool or range midpoint/extreme.
- Invalidation: acceptance outside the swept level.

### Template D: News Event Liquidity Return

- Setup: FOMC/CPI creates a fast move and leaves liquidity/wick behind.
- Confirmation: wait at least for the immediate event volatility to cool; watch reclaim/retest.
- Targets: event wick, event liquidity pool, EMA retest.
- Invalidation: post-news acceptance in the opposite direction.

### Template E: Altcoin Preparation Zone

- Setup: altcoin is in HTF bear-market range.
- Confirmation: BTC stable/up and BTC.D falling.
- Targets: range midpoint, range high, upside imbalances.
- Risk: if BTC falls and BTC.D rises, altcoins can make new lows.

## What The First 25 Videos Still Do Not Fully Prove

- Exact position sizing formula.
- Exact stop-loss placement rule across setups.
- Whether he scales in and out systematically.
- How he quantitatively weights heatmap liquidity against EMA and session confluence.
- Whether his lower-timeframe execution trigger has a strict visual checklist beyond reclaim/retest/rejection.

## Agent Recognition Rule

When reviewing a chart in CrypNuevo style, do not start by predicting direction. Start by identifying:

- the liquidity map,
- the wick/imbalance map,
- the EMA state,
- the session/news context,
- and the invalidation.

Only then decide whether the chart matches a known playbook.
