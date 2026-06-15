# CrypNuevo Before/After Pattern Study

Created: 2026-06-13

## Purpose

This note converts captured CrypNuevo public updates into before/after evidence. The goal is to identify repeated trade mechanics, not to score calls or imply future certainty.

Source files used:

- `sources/first-trader/x-posts/raw/crypnuevo-trading-post-corpus.json`
- `sources/first-trader/x-posts/raw/crypnuevo-weekly-update-index.json`
- `library/first-trader/strategy-notes/crypnuevo-weekly-market-update-index.md`
- `sources/first-trader/x-posts/crypnuevo-x-chart-posts-2026-06-12.md`
- `sources/first-trader/chart-screenshots/manifest.json`

Related visual dictionary:

- `library/first-trader/setup-examples/crypnuevo-visual-trigger-dictionary.md`

## Quick Rating Of This Evidence Layer

- Coverage: medium-high for BTC weekly/update posts from 2024-2026.
- Before/after quality: medium-high. Many posts quote prior analysis directly, and a first screenshot pass has downloaded 46 local chart images.
- Execution detail: medium-low. We have words like trigger, invalidation, acceptance, reclaim, retest, and close, but not enough chart-image markup yet.
- Trade management detail: emerging. There are useful mentions of partial TP, DCA/splitting entries, sidelining, and invalidation, but not a complete system.

## Before/After Cases

| Case | Before | After | Pattern Observed | What To Learn |
| --- | --- | --- | --- | --- |
| 2024-12-08/09 BTC wick fill | Sunday update said a large 1h/4h long wick was the only target and should fill. | Follow-up said Sunday update was nailed and credited the wick-fill strategy. | Large wick as imbalance/magnet. | When the wick thesis is dominant, he can simplify the whole plan around that single magnet. |
| 2024-12-01/05 BTC trigger plan | At resistance around 98.4k, he defined both upside and downside triggers instead of predicting one path. Upside trigger was reclaim/support above the key level toward 104k-105k. | Follow-up said candle closed above the key level and pushed quickly to target. | Acceptance/reclaim trigger. | He treats candle closes and retests as safer confirmation than wicks through a level. |
| 2025-01-02 BTC wicks and liquidations | Prior plan discussed two downside wick/OI imbalances and 91,666 liquidations as reversal zone. | Follow-up said both wicks filled, all liquidations hit, and 91,666 reversed. | Wick fill plus liquidation confluence. | Best examples combine multiple magnets at one area, then watch reaction. |
| 2025-01-05 BTC 4h50EMA retest | He wanted a drop to 4h50EMA after breaking above it; acceptance above it would be the Monday false-move long trigger. | Later January updates framed the move as a projected liquidity run and range retest process. | EMA retest after breakout. | EMA is not just an indicator; it becomes a decision line after structure changes. |
| 2025-02-02/03 BTC three wicks | Sunday update said he had been looking for swing shorts from range highs/upside wick toward two lower wicks. | Follow-up said the problem of the three wicks was solved quickly. | Multiple wick targets. | When several unresolved wicks exist, he often expects price to clean them up sequentially. |
| 2025-02-04/06 BTC invalidated setup | Update said safest long was to wait for 1W candle close back above prior level after a sweep. | Follow-up said entry setup was invalidated and no entry was given because a new downside wick changed the thesis. | No-entry invalidation. | He can cancel a plan before entry when fresh market structure creates a better opposing magnet. |
| 2025-02-08/15 BTC 1W wick | Sunday update said the new 1W long wick would likely get filled at least 50%. | Next Sunday said prior wick-fill call happened, virtually filling 50% at 48.5%. | Partial wick-fill target. | The 50% wick fill is a practical first target, not always the final target. |
| 2025-03-16/20 BTC FOMC/liquidation plan | Plan favored higher prices unless LTF uptrend broke, ideally after a small deviation below trendline to hit stops. | Follow-up said choppy PA, deviation below trendline, then FOMC push to hit liquidations. | Stop hunt before target. | He expects price to gather fuel first, then move to the visible liquidity objective. |
| 2025-03-19/20 BTC fast drop long | He said if price dropped straight to 69k, he would look for a day-trade long because the move would be overextended and need rebalancing. | Follow-up said price dropped straight to 69k and it became a clean day-trade setup. | Fast overextension into level. | Speed and timing matter. Same level is higher quality when price reaches it as an aggressive liquidity run. |
| 2025-03-22/27 BTC range rotation | Sunday update expected stuck range conditions and possible visit to range lows / 4h long wick. LTF reply favored rotation to 65k, invalidated by acceptance above 71k. | Follow-up said price was rotating toward 65k and April could become a boring HTF range. | Range rotation with explicit invalidation. | He often pairs a directional bias with a hard flip point instead of marrying the bias. |
| 2025-04-20/22/23 BTC EMA compression | Sunday update focused on 1D50EMA/1W50EMA compression and upside liquidations between 87k and 93k. | Follow-ups said thesis was playing out and then completed, while taking profit gradually from long swing. | EMA compression breakout to liquidity. | EMA compression can be used as a springboard when liquidity above is clear. |
| 2025-05-18/21 BTC 1W50EMA support | Sunday update said HTF structure was bullish after retesting 1W50EMA bull market support and expected a new ATH. | Follow-up said new ATH was unlocked and looked for more continuation. | HTF support bounce. | 1W50EMA is one of his strongest macro context tools. |
| 2025-06-01/05/07 BTC R/S fail to 100k | Sunday update said R/S flip failed, downside liquidations hit, and failure to recover 106k opened path to 100k plus 1D50EMA. | Follow-ups said plan was playing out at 100k and then 100k to 105k bounce occurred. | Failed reclaim to psychological/EMA support. | Failed support/reclaim can create a clean path to the next liquidity/support cluster. |
| 2025-07-20/25 BTC upside wicks/no progress | Sunday update warned that upside wicks without progress can show MM building shorts. | Follow-up said liquidation cluster 116k-115k and main 115.3k level were hit. | No-progress wicks before drop. | Repeated wicks plus failure to progress is a recurring reversal clue. |
| 2025-10-05/09 BTC 4h50EMA retest | He favored longs from a 4h50EMA retest after overextension. | Follow-up said final spike and correction came within 0.01% of target; he closed short scalps and looked for longs. | EMA mean reversion after extension. | He can trade both sides tactically while keeping the larger next-entry plan in mind. |
| 2025-10-19/20 BTC wick plus DCA | Sunday update said prior projection played out and 50% wick was filled, then asked if downside imbalances were fully retraced. | Follow-up mentioned importance of splitting entries/DCA because CME gap could still hit before continuation. | Wick fill plus entry staging. | Even when trend is clear, he leaves room for nuisance retraces and gaps. |
| 2026-05-03/19/22 BTC range high deviation | Original setup focused on resistance at range highs after waiting two months for an extreme. Later update said BTC had deviated above range highs and returned inside, making 71k liquidity probable and 79k retest/rejection possible. | Follow-up noticed liquidations at 79.4k matching range highs and drew execution trigger plus invalidation. | Range high deviation, retest, opposite liquidity. | The strongest range trades wait for an extreme, deviation, return inside, then retest/rejection. |
| 2026-06-01/03 BTC wrong setup | Sunday update favored longs around 73k-72.5k wick zone and CME gap at 75.4k. | Follow-up said the last setup was wrong because price broke through 72k due to US-Iran escalation news. | News invalidation / wrong setup. | Macro shock can override technical wick levels; he acknowledges failed setup and reframes. |
| 2026-06-07 BTC range lows | Sunday update said price was back at 4-month range lows after a sharp 25% drop and expected strong bounce from overextension. Thread replies projected mid-range around 70k, possible retest of range lows, then range highs/80k. | Follow-up outcome not yet curated in this note. | Range-low overextension. | Needs after-evidence before becoming a stronger rule. |
| 2026-06-09 GOLD 1W50EMA wick fill | Earlier GOLD/XAU idea expected a long downside wick to fill and 1W50EMA retest before full-size swing long. | Follow-up said the -11% drop arrived and he was buying at 1W50EMA plus wick fill. | HTF wick fill plus 1W50EMA. | The wick/EMA confluence applies beyond BTC when the structure is clear. |

## Repeated Patterns Found

### 1. First Target Is Often Liquidity, Not Direction

He starts with where trapped traders sit:

- wick imbalances
- liquidation clusters
- range highs/lows
- prior highs/lows
- CME or OI gaps
- psychological levels

The directional idea comes after the liquidity map. In the strongest examples, the target is obvious before the entry is discussed.

### 2. The 50% Wick Fill Is A Practical Milestone

The dataset repeatedly distinguishes:

- 50% wick fill as first confirmation/first objective
- 100% wick fill as fuller completion
- wick fills across 1h, 4h, 1D, and 1W

Important nuance: not every visible wick remains a valid imbalance. In one Dec 2024 reply, he says a wick created to fill a previous wick may not need to fill because the practical imbalance is gone.

### 3. Range Extremes Matter More Than Mid-Range

Strong examples happen at:

- range highs after long waiting periods
- range lows after sharp drops
- deviations outside range boundaries
- returns back inside the range

Mid-range is usually treated as a low-quality area unless a separate trigger appears.

### 4. Trigger Means Acceptance/Rejection, Not Touch

Recurring trigger language:

- candle closes above/below key level
- 2-3 candles accepting above a level
- reclaim and retest as support
- failed acceptance outside a range
- return back inside a channel/range
- acceptance above invalidation level flips the plan

This is one of the biggest practical findings: a level touch is not the trade.

### 5. EMA Is A Context Line And A Trigger Line

The most repeated EMAs:

- 1W50EMA for bull/bear or HTF support context
- 1D50EMA for trend/range compression
- 4h50EMA for retest entries and mean reversion
- 1h50EMA for lower-timeframe resistance/support
- 20/55 EMA for older impulse-continuation playbook

The EMA is strongest when paired with a wick, range boundary, liquidation cluster, or reclaim.

### 6. He Often Expects A Stop Hunt Before The Real Move

Several before/after examples include:

- deviation below trendline before FOMC push
- range-low sweep before reclaim
- short-lived pump to hit short liquidations before move down
- shallow pullback to shake FOMO longs
- Asia pump/deviation risk before a reversal

This means the mentor should ask: "What liquidity could price grab before the cleaner move?"

### 7. He Cancels Or Flips When Structure Changes

Useful invalidation examples:

- "No entry given" when a new wick changed the prior setup.
- Acceptance above 71k invalidates a downside rotation and flips him toward longs.
- Acceptance above 100k invalidates a rejection/liquidity-run idea.
- News-driven break through the technical zone makes the prior setup wrong.

This should be core to the assistant: wrong or invalidated is a valid outcome.

### 8. Trade Management Is Partial And Adaptive

Concrete management clues:

- Takes partial profits gradually, e.g. 25%, 50%, 75% closed in one 2024 BTC range example.
- Takes smaller partial profit while holding majority when conviction remains, e.g. 20% ETH position.
- Mentions DCA/splitting entries when a CME gap or nuisance retrace can still hit.
- Goes sidelined when momentum has not shifted or setup is unclear.

Still missing: exact stop placement, leverage model, and position size formula.

## Pattern Model For Future Chart Reviews

Use this sequence when reviewing a chart in his style:

1. Define HTF state: trend, range, compression, deviation, or EMA retest.
2. Mark liquidity above and below.
3. Identify unresolved wicks and whether 50% or 100% fill is relevant.
4. Check if price is at an extreme or in low-quality mid-range.
5. Ask what liquidity could be hunted first.
6. Define trigger as acceptance/rejection/reclaim/return inside, not a touch.
7. Define invalidation before entry.
8. Choose targets from liquidity, wick, range extreme, EMA context, or psychological level.
9. Decide whether partials/DCA/sidelining fit the uncertainty.

## Highest-Value Missing Work

1. Extract local screenshots for each case and mark the actual chart annotations.
2. Build a table with exact dates, original status IDs, quoted prior status IDs, and outcome status IDs.
3. Separate winning examples, invalidated examples, and unclear examples.
4. Add at least 10 failed or no-trade examples so the model learns restraint.
5. Build a "trigger dictionary" with image examples for acceptance, reclaim, deviation, return inside, and wick fill.

## Profile Update Candidates

Add these to the main profile after more examples are cleaned:

- Stronger rule: 50% wick fill often acts as first objective; 100% is second objective when context supports it.
- Stronger rule: candle closes/acceptance matter more than wick-through moves.
- Stronger rule: he often maps both sides at key resistance rather than predicting one path.
- Stronger risk rule: new wick/gap/news context can invalidate a planned entry before it triggers.
- Trade management note: partial profits and DCA/split entries appear in public examples, but exact sizing remains unknown.
