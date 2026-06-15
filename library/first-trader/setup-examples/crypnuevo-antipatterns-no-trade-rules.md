# CrypNuevo Anti-Patterns And No-Trade Rules

Created: 2026-06-13

## Purpose

This note defines when the mentor should reject a trade idea, lower confidence, or ask for missing information instead of manufacturing a setup. It exists to prevent hallucinated conviction.

The assistant should be comfortable saying:

- "I would not trade this."
- "Too crowded."
- "Risk/reward is poor."
- "No edge here."
- "The information is too poor to judge."
- "This is a watchlist idea, not a trade."

## Core Rule

If the chart does not show enough context, trigger, invalidation, and reward potential, the answer should default to **skip / wait / no trade**, not forced bullish or bearish analysis.

Do not turn every chart into a setup.

## No-Trade Verdicts

Use one of these verdicts in every chart review:

| Verdict | Meaning | Action |
| --- | --- | --- |
| No trade | Setup is missing edge, context, trigger, invalidation, or R:R. | Skip. Wait for new structure. |
| Watchlist only | Interesting level or liquidity exists, but no trigger yet. | Set alerts and define trigger/invalidation. |
| Conditional trade | Setup could become valid if specific conditions appear. | Name exact trigger, invalidation, and target. |
| Valid setup | Enough confluence exists, with clear trigger and invalidation. | Review risk/reward and execution quality. |

## Probability Language

Use probability as an honest confidence band, not as certainty.

| Band | Label | When To Use |
| --- | --- | --- |
| 0-20% | No edge / avoid | Missing HTF context, no trigger, poor R:R, or contradictory structure. |
| 20-40% | Weak / watch only | One interesting factor exists, but confirmation is missing. |
| 40-55% | Neutral / uncertain | Bulls and bears both have valid arguments; wait for acceptance/rejection. |
| 55-65% | Conditional edge | Setup has some confluence but still needs execution trigger. |
| 65-75% | Good setup | Clear liquidity target, trigger, invalidation, and acceptable R:R. |
| 75%+ | Rare / high confluence | Only use when multiple stored-profile factors align and invalidation is clean. Avoid overusing this. |

Never present a probability as a true statistical backtest unless a backtest exists. Phrase it as "my confidence read" or "setup quality estimate."

## Anti-Patterns

### 1. Information Too Poor

Reject or pause when:

- Only one low-timeframe screenshot is provided.
- HTF context is missing.
- Current price, timeframe, exchange, or session is unclear.
- Liquidity above/below cannot be identified.
- No entry, stop, target, or invalidation is provided and cannot be inferred responsibly.

Honest feedback:

- "Information quality is too poor for a trade call."
- "I can map scenarios, but I would not trade from this screenshot alone."
- "Need HTF context and the invalidation before this becomes reviewable."

### 2. Mid-Range Noise

Reject or lower confidence when price is sitting in the middle of a range without a separate trigger.

Why it matters:

- CrypNuevo evidence repeatedly favors range extremes, deviations, liquidity pools, wick fills, and EMA decision lines.
- Mid-range often has poor R:R and unclear invalidation.

Honest feedback:

- "No edge here; this is mid-range."
- "I would wait for range high, range low, or a clean reclaim/rejection."

### 3. Level Touch Without Reaction

Reject when the only argument is that price touched support/resistance, EMA, wick, or liquidity.

Required improvement:

- candle close
- reclaim
- retest
- rejection
- return inside range
- failed acceptance
- session confirmation

Honest feedback:

- "A touch is not a trigger."
- "This is a level of interest, not an entry."

### 4. Poor Risk/Reward

Reject when invalidation is far away or the nearest target is too close.

Common signs:

- Entry is late after the move already happened.
- Stop must sit beyond a wide wick/range.
- First target is inside chop or too near entry.
- Trade direction is into obvious nearby liquidity against the position.

Honest feedback:

- "Risk/reward is poor."
- "Even if direction is right, the entry quality is bad."
- "The trade idea may be correct, but the execution is not."

### 5. Crowded Obvious Trade

Lower confidence when the setup is too obvious to retail:

- Breakout long after a big green candle into resistance.
- Breakdown short after a big red candle into support.
- Longing range high because momentum feels strong.
- Shorting range low because fear is high.

CrypNuevo-style caution:

- Ask where retail stops are.
- Ask whether price may sweep first.
- Watch for fakeout/deviation.

Honest feedback:

- "Too crowded."
- "This looks like the place where late traders get trapped."
- "I would rather wait for the sweep and reaction."

### 6. Event Volatility Without Second Structure

Reject trading directly into or immediately after CPI/FOMC/Powell/high-impact news.

Required improvement:

- wait for event candle to settle
- identify imbalance left by the move
- wait for reclaim/retest/rejection
- define invalidation after the new structure forms

Honest feedback:

- "No trade before the event resolves."
- "The first news candle is not the setup; it usually creates the setup."

### 7. Weekend Or Thin-Liquidity Trap

Lower confidence on weekend moves, bank holidays, or thin session impulses unless the plan is specifically about CME gap / wick retrace.

Honest feedback:

- "Weekend move, lower trust."
- "I would not chase this until weekday liquidity confirms or retraces it."

### 8. Missing Invalidation

Reject when the user cannot say where the idea is wrong.

Honest feedback:

- "No invalidation, no trade."
- "If we cannot define where the thesis fails, this is not a setup."

### 9. Contradictory Liquidity

Lower confidence when liquidity is strong on both sides and price is between both pools.

Honest feedback:

- "Both sides have a case; wait for one side to be swept."
- "This is a map, not a trade."

### 10. Profile Evidence Missing

Reject trader-specific claims when the stored profile does not support them.

Honest feedback:

- "I do not have enough stored evidence to say CrypNuevo would use that rule."
- "This may be valid TA, but it is not yet supported by this profile."

## Required No-Trade Output

When rejecting a trade, use this structure:

```markdown
### Verdict
No trade / watchlist only.

### Confidence
20-40% setup quality. This is not a win probability; it is a confluence/read quality estimate.

### Why I Would Skip
- ...

### What Would Change My Mind
- ...

### Minimum Data Needed
- ...
```

## Minimum Data Checklist

Before giving anything above 55% setup quality, require:

- market and timeframe
- current price area
- HTF structure
- liquidity above and below
- entry trigger
- invalidation
- first target
- R:R estimate
- session/news context
- what cancels the idea

If three or more of these are missing, default to **No trade** or **Watchlist only**.

## Profile Update Candidate

Add no-trade language directly to prompts and chart review outputs:

- explicit verdict
- setup-quality percentage
- skip reason
- what would make it tradeable
- missing data checklist
