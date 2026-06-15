# CrypNuevo Corpus — Coverage & Evolution Audit

Date: 2026-06-13 · Purpose: answer two questions before doing more work —
(1) Do we need to collect more data? (2) Has his trading changed, and can we detect it?

## Headline findings

1. **Corpus is essentially complete.** Full clean transcripts through **video 151 (2026-01-20)**, X posts through **June 2026**, 46 curated screenshots across 17 themes, chart-frame samples (batches 7–10), and strong synthesis notes. Collecting more in general is busywork; only collect to fill a *named* gap.
2. **His method demonstrably evolved over 2 years** — captured in the evolution notes + the "2024-2026 Additions" section of `crypnuevo-trading-dna.md`. The change is real and material (see timeline).
3. **Primary gap is not data — it is staleness + lack of a change-tracker:**
   - `profiles/first-trader.md` (the file the agent loads) only reflects evidence **through video 130 / batch 010 (Dec 2024)**. The 2025–26 evolution never reached the profile.
   - No single artifact flags **current vs refined vs superseded**, so the agent can't reliably give *current* CrypNuevo.

## Coverage map

| Area | Evidence | Status |
| --- | --- | --- |
| Liquidity / wick-fill / imbalance | dense across all batches | **Strong** |
| 50MA backbone (1W/1D/4h/1h) | 107/130 videos | **Strong** |
| Range deviation / quarters | batches 5–11 | **Strong** |
| Session & weekly psychology | batches 4, 8 | **Strong** |
| 4h50EMA gate, stop-loss zones, M-patterns | batch 9 | **Strong** |
| Hyblock / heatmap / order book | batches 6–12 (delta thresholds in 12) | **Strong** (now codified-worthy) |
| Scaling / staged sizing / preset TPs | batches 8, 11, 12 | **Strong in source, NOT in profile** |
| W-pattern / double bottom | X posts + strategy-map "M/W patterns" | **Present, not codified as a setup** |
| Macro thesis (M2, gamma, mining cost, cycle-rejection) | batch 12 | **Current, NOT in profile** |
| Gold / non-BTC application | secondary mentions | **Thin** (method generalizes; few worked examples) |
| User's own trades | none | **Absent by design** |

## Evolution timeline (the change-detector)

- **2023 H1 (v1–55) — Foundation:** liquidity framework; wick-fill made explicit (50%/100%); weekly session psychology; range quarters/deviation procedural; CPI/FOMC wait-30-45-min rule.
- **2023 H2 (v56–100) — Cross-market + visual route-mapping:** DXY/SPX/BTC.D stack; turquoise boxes / projected paths; manipulation sweep; 100% wick-fill continuation; indicator being built.
- **2024 H1 (v101–115) — Stricter rules:** 4h50EMA two-candle gate; stop-loss-zone model; momentum timing filter; M-pattern; conditional BTC.D fade.
- **2024 H2 (v116–130) — Market-outlook format:** indicator launched (wick-fill/liquidity/sessions/50MA); swing vs day-trade separation; spot-buying & altseason frameworks.
- **2024 Q4–2025 Q1 (v131–137) — Execution & risk layer:** manual wick-fill management (no hard stop in fill zone); staged sizing; order-book spoof check; weekly 50MA promoted to bull/bear regime line.
- **2025 H2–2026 (v138–151) — Post-hiatus, CURRENT:** the *why* (exchange-owned MMs, FTX/Alameda ruling); liquidity-run / room-for-liquidity; liquidity trendlines; cross-exchange wick validation; new context tools (options gamma/gamma-flush, Hyblock delta >20–25B = squeeze, M2 global liquidity, BTC mining-cost floor); full execution mechanics (laddered limits, preset TPs e.g. 66/33, breakeven stops, flat-into-news, flat at mid-range); **bullish-2026 macro thesis; explicit rejection of the 4-year cycle and seasonality.**

**Constants (never changed):** liquidity-first, bias-neutral ("not a bull, not a bear"), 50MA backbone, "trade the reaction not the level," rebuild-on-invalidation, constant humility/disclaimers.

**Most important drift for the agent:** 2025–26 added (a) mechanical execution detail and (b) a macro thesis, and (c) he now *rejects* cycle/seasonality. An agent on pre-2025 data would under-specify execution and could lean on cycle narratives he no longer endorses.

## Recommended actions (no new collection required)

1. **Refresh the profile to current** — merge batches 011–012 into `profiles/first-trader.md` (mentality, setup playbook, tools, evidence index). Highest priority; fixes the staleness.
2. **Create a change-timeline artifact** (`library/first-trader/strategy-evolution-timeline.md` or fold into the profile) that tags each rule **current / refined / superseded** so the agent always answers with *current* CrypNuevo and can explain what changed.
3. **Then codify** W/M-patterns, Hyblock thresholds, and the staged-sizing/preset-TP scaling logic as first-class setups (Phase 2).
4. **Targeted collection only if:** new videos appear after v151, or we want more **gold / non-BTC worked examples** to prove market-agnostic application.
