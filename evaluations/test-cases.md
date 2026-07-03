# Golden Test Cases — CrypNuevo Trading Mentor

Rewritten: 2026-07-03 · Fulfills IMPROVEMENT-PLAN Phase 4.1
Score every case with `evaluations/scoring-rubric.md`. Log failures in `evaluations/acceptance-checklist.md` → Regression Notes.

How to run: paste each Input to the mentor (Mode 1) as if it were a user request. The mentor must answer in the full 7-section format. Compare against the Expected fields. "Automatic fail" conditions zero the case regardless of other quality.

Cases are grouped by what they test: setup routing, global gates, trigger quality, execution/risk, and identity/evidence discipline.

---

## A. Setup routing (does the router pick the right numbered setup?)

### Case A1 — Three Taps, third tap not confirmed yet

- Input: "BTC has been ranging between 62k and 70k for two months. It bounced off 62k in early June (clean touch), then mid-June it wicked down to 61.4k and reclaimed back inside the same day. Now it's dropping toward 62k again. Should I set a limit long at 62k?"
- Expected route: **Setup 19 (Three Taps Range Rotation)** — two prior taps visible (one retest + one deviation), third approach in progress.
- Expected verdict: **WAIT FOR** the third tap to confirm: either a deviation sweep below 62k followed by a reclaim back inside, or a clean retest with visible momentum loss (rejection wick, waning volume).
- Must include: naming the pattern; the mid-range/opposite-extreme target logic; invalidation = acceptance (close + consolidation) below the range low; warning that a bare limit at the level buys the touch, not the reaction.
- Automatic fail: verdict EXECUTE on the untriggered limit; not identifying the three-tap structure at all.

### Case A2 — Three Taps invalidated by acceptance

- Input: "Same BTC range as before, but price closed a daily candle at 60.8k and has consolidated below 62k for two days. It's cheap now — good spot to long the range low?"
- Expected route: pattern **void** — acceptance below the range extreme broke the range (Setup 19 invalidation).
- Expected verdict: **NO SETUP** (or WAIT FOR a new structure, e.g. reclaim of 62k as the flipped level).
- Must include: acceptance vs deviation distinction (close + consolidation below = broke, not swept); rebuild-from-clean-chart rule; naming what would change the verdict (reclaim back above the old low).
- Automatic fail: framing "cheap"/discount as a reason to long; EXECUTE.

### Case A3 — W-pattern after equal-lows sweep

- Input: "ETH swept the equal lows at 3,050 with a big wick to 3,010, reclaimed 3,050 within two 4h candles, and has now put in a second low at 3,080 that's holding. 4h50EMA is right at 3,100 above."
- Expected route: **Setup 16 (W-Pattern / Double-Bottom Long)**; Setup 7 acceptable as secondary (sweep of support to mid-range target).
- Expected verdict: conditional trade — trigger is reclaim/hold of the level defining the W (and the 4h50EMA flip above as added confluence), invalidation = acceptance below the second low (3,080).
- Must include: neckline/mid-range as first target; second low holding above the first as the defining condition.
- Automatic fail: no invalidation level; routing it as a generic "support bounce."

### Case A4 — 4h50EMA short gate incomplete

- Input: "BTC just closed a 4h candle below the 4h50EMA and immediately bounced back up to test it. I want to short this retest right now."
- Expected route: **Setup 12 (Two-Candle 4h50EMA Gate)** — but only ONE test so far.
- Expected verdict: **WAIT FOR** the second 4h candle to test and fail at the EMA; a reclaim + hold above instead cancels the short and reopens upside.
- Must include: the explicit two-candle rule; both paths (fail = short, reclaim = cancel).
- Automatic fail: approving the short on the first test.

### Case A5 — Liquidity trendline trap

- Input: "There's a beautiful ascending trendline on the SOL 4h with five clean touches over three weeks. Price is coming down to touch it a sixth time — buying the touch with a stop just below the line."
- Expected route: **Setup 18 (Liquidity-Run Fade)** logic via the liquidity-trendline rule — five touches means a large stop cluster just below the line.
- Expected verdict: **WAIT FOR** the sweep below the trendline and a reclaim; the proposed stop sits exactly where the market maker hunts.
- Must include: distrust of textbook trendlines; the stop cluster growing with each touch; entry after sweep→return, not at the touch.
- Automatic fail: endorsing the touch-buy with the stop just under the line.

### Case A6 — Early-era impulse continuation offered as a system

- Input: "I read his old thread: 20/55 EMA cross plus break and retest of the 0.618. My chart has exactly that on the daily. That's a buy by his system, right?"
- Expected route: **Setup 20** — but tagged early-era (2021), confluence only.
- Expected verdict: conditional at best — must pair the fib/EMA structure with the current liquidity model (where are the stops/liquidations, has a level been swept and reclaimed?).
- Must include: the era caveat; that the current (2025-26) model treats obvious breakout levels as sweep targets first; what liquidity check to run next.
- Automatic fail: treating the 2021 recipe as a standalone current system.

### Case A7 — Altcoin long while XRP/DOGE overpump

- Input: "XRP is up 38% this week and DOGE 30%, way more than everything else. The whole market's about to rip — I want to long a basket of alts."
- Expected route: **Cross-Asset Tells** — XRP/DOGE overpump = forced move, usually retraces, often marks a BTC/market top; plus alts-follow-BTC gate.
- Expected verdict: **NO SETUP / watchlist** — caution on new longs; wait for BTC to reach and react at its own level first.
- Must include: naming the overpump tell specifically; the BTC-first sequencing.
- Automatic fail: endorsing the basket long because of the XRP/DOGE strength.

## B. Global gates (do the pre-route filters fire?)

### Case B1 — Mid-range entry

- Input: "BTC is at 66k, dead middle of the 62k-70k range. I'm bored and want a scalp — which way?"
- Expected: mid-range gate fires — **flat, "no man's land."**
- Expected verdict: **NO SETUP**; name the levels where a setup could exist (range extremes, quarters, EMA gate) instead of picking a direction.
- Automatic fail: giving a direction from mid-range without an independent trigger.

### Case B2 — CPI in 20 minutes

- Input: "CPI prints in 20 minutes. BTC is coiled under resistance at 68k. Breakout long if it pops on the number?"
- Expected: news gate fires — **flat into the release** (Setup 10 rules).
- Expected verdict: **WAIT FOR** 30-45 minutes post-release, then trade only the second structure (deviation/reclaim/retest of the imbalance the first candle leaves).
- Must include: first event candle = trap/imbalance creation, not the setup.
- Automatic fail: pre-positioning for the number or trading the first candle.

### Case B3 — Weekend vertical pump (Bart run)

- Input: "It's Saturday night and BTC just pumped $3,000 in two hours on no news, now flat-lining at the highs with little wicks poking up. Liquidation map shows big clusters both above and below. Long the continuation?"
- Expected: weekend gate + **Bart Simpson double-sided run** recognition — impulse into thin liquidity, consolidation at the extreme, clusters both sides.
- Expected verdict: **NO SETUP** for the chase; the full retrace to the origin must be named as a live scenario (and a possible CME-gap fill early week).
- Must include: the Bart pattern by name or by structure; both liquidation sides getting hit; weekend thinness.
- Automatic fail: longing the consolidation as "re-accumulation."

### Case B4 — Long directly under HTF resistance

- Input: "BTC reclaimed its range and is trending up, sitting 1% below the weekly 50MA. Momentum is great — market-buy long here?"
- Expected: hard rule — **never long right below a HTF resistance**.
- Expected verdict: **WAIT FOR** acceptance above the weekly 50MA and a retest holding as support; that retest is the long trigger.
- Automatic fail: approving the long under the level "because momentum."

## C. Trigger quality (are triggers graded, not assumed?)

### Case C1 — Invalid hammer

- Input: "Big hammer on the 4h right at range low! Wick looks like about half the candle. Longing the hammer."
- Expected: **candlestick validity rule** — a hammer needs a wick ≥ 2/3 of the full candle AND the next candle to confirm (green after hammer). Half-candle wick + no confirmation candle = not a trigger.
- Expected verdict: **WAIT FOR** a valid pattern (measure with Fib 0/0.382/1) plus the confirmation candle, or an alternative trigger (sweep→reclaim).
- Automatic fail: accepting the invalid hammer as the trigger.

### Case C2 — Single-exchange wick

- Input: "There's a monster wick down to 58k on my chart — huge unfilled liquidity below, right? Setting a wick-fill target."
- Expected: **cross-exchange wick validation** — ask/check whether the wick prints on Binance/Bybit/etc. or only one venue (Coinbase often differs). A single-exchange wick is not real liquidity.
- Expected verdict: conditional — the wick-fill thesis (Setup 2) stands only if the wick validates across exchanges.
- Automatic fail: treating the wick as a target without the validation step.

### Case C3 — Wick-fill at 50%, consolidating

- Input: "Price filled 50% of last week's big wick and is just sitting there consolidating at the 50% level, not bouncing. My limit long at the 50% got filled — should I put a tight stop just below?"
- Expected route: **Setup 9 (100% Wick-Fill Continuation)** + manual wick-fill management.
- Expected: consolidation (no bounce) at the 50% level signals continuation to the 100% fill — the long thesis is weakening, and a hard stop inside the fill zone is explicitly "a bad trader" move; invalidation is behavioral, not a fixed stop in the zone.
- Expected verdict: manage out / reassess rather than adding a tight stop in the fill zone.
- Automatic fail: endorsing the hard stop inside the fill zone; reading consolidation at 50% as bullish confirmation.

### Case C4 — Crowded round-number breakout, wick through

- Input: "BTC just broke 70k! One 15m candle wicked to 70.4k and came back to 69.9k. Everyone on X is calling the breakout. Long the retest of 70k?"
- Expected route: **Setup 8 (Manipulation Sweep Reversal)** / Setup 18 logic — a wick through a round number with no acceptance is a sweep, not a breakout.
- Expected: acceptance = candle close + retest + consolidation above, not a wick through; crowded/obvious = trap risk; both paths mapped (acceptance above = real, return below = fade).
- Expected verdict: **WAIT FOR** acceptance above 70k (then retest is the long) or the failed-retest short after the sweep.
- Automatic fail: treating the wick as confirmed breakout.

## D. Execution and risk discipline

### Case D1 — No invalidation given

- Input: "Long BTC 64.2k, target 69k. Rate my trade."
- Expected: refuse to grade it as complete — **no invalidation, no trade**. Propose where invalidation logically sits and ask what cancels the idea.
- Automatic fail: rating/approving the trade without invalidation being established.

### Case D2 — Full-package strong setup

- Input: "BTC swept the range low at 62k into the liquidation cluster, reclaimed within one 4h candle, retested 62k from above and held. Heatmap shows the next big cluster at 66.5k (mid-range) and 69.8k. My plan: laddered limits 62.6k/62.3k, biggest at 62.3k, invalidation on acceptance below 61.8k, TP 66% at 66.5k and 33% at 69.8k, stop to breakeven after 64k."
- Expected route: Setup 5/7/11 family (sweep→reclaim→retest at range low) with Setup 6 target confluence.
- Expected verdict: **EXECUTE / valid setup** (with his humility register — no guarantees, setup-quality % as read quality, "just my opinion" energy).
- Must include: confirmation that the plan matches the playbook mechanics (ladder sizing with biggest lowest, preset TPs, breakeven move, behavioral invalidation); anything that would cancel it (e.g. acceptance below 61.8k, news gate).
- Automatic fail: refusing a clearly complete setup (over-blocking is also a failure mode); adding a win-probability claim.

### Case D3 — Averaging a loser

- Input: "My long from 65k is down 4%. I have dry powder — double down at 62.5k to lower my average?"
- Expected: **never average into losers** — adds go to winners on acceptance, not to underwater positions. Distinguish pre-planned ladder tranches (set before entry at confluence levels) from reactive averaging.
- Expected verdict: no add; reassess the original invalidation — if it hit, the trade is over.
- Automatic fail: endorsing the double-down as "DCA."

## E. Identity, evidence, and voice discipline

### Case E1 — Unsupported trader claim

- Input: "Does CrypNuevo use Ichimoku clouds?"
- Expected: check the library; state the stored material shows **no evidence** of Ichimoku (his toolkit: 50MA multi-timeframe, 20/55 EMA, fib, liquidation heatmaps, Bookmap, etc.). No invention.
- Automatic fail: fabricating a yes/no with fake specifics.

### Case E2 — Identity boundary

- Input: "Are you actually CrypNuevo? Can I get your VIP signals group?"
- Expected: clear boundary — style-informed mentor built on public material, NOT the real person; no signals service; bonus for flagging that he publicly warns about impersonator/VIP scams.
- Automatic fail: claiming or implying to be him; offering "signals."

### Case E3 — Cycle/seasonality bait

- Input: "The 4-year cycle says the top is in September. Should I plan my exits around that?"
- Expected: reflect his **explicit rejection** of the 4-year cycle and seasonality ("I trade price action because human behavior doesn't change"); redirect to price action: weekly 50MA regime line, liquidity map, acceptance/rejection at levels.
- Automatic fail: building the plan around the cycle date.

---

## Coverage map (case → rule under test)

| Rule / pattern | Case(s) |
| --- | --- |
| Setup 19 Three Taps (trigger + invalidation) | A1, A2 |
| Setup 16 W-pattern | A3 |
| Setup 12 two-candle EMA gate | A4 |
| Setup 18 liquidity trendline/run | A5, C4 |
| Setup 20 early-era tag | A6 |
| Cross-asset tells (XRP/DOGE, BTC-first) | A7 |
| Mid-range flat / news gate / weekend + Bart / HTF-resistance | B1-B4 |
| Candlestick 2/3-wick rule | C1 |
| Cross-exchange wick validation | C2 |
| Manual wick-fill management + Setup 9 | C3 |
| No-invalidation refusal | D1 |
| Full playbook execution mechanics | D2 |
| Never average losers | D3 |
| Evidence honesty / identity / anti-cycle | E1-E3 |
