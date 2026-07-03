# CrypNuevo Mentor Agent — Improvement Plan

Status: draft v1 · Date: 2026-06-13 · Owner: mayorcryptox

This plan turns the current markdown knowledge base into the **"CrypNuevo Trading Mentor"** agent described in the target system prompt: an objective, teaching-first mentor that ingests a chart, applies CrypNuevo's exact methodology, and returns a fixed 7-section verdict.

## Decisions locked (from intake)

- **Primary goal:** Live trade decisions *and* teaching, delivered through the target 7-section output format.
- **Automation:** Hybrid — keep the markdown core, add live data feeds (price, DXY/SPX, BTC.D, Hyblock liquidations, CPI/FOMC calendar).
- **Scope:** One trader (CrypNuevo), polished to "established."
- **Markets:** Strategy-first and **market-agnostic**. Primary focus BTC, gold, and crypto, but the methodology (liquidity, wick fills, EMA mean-reversion, ranges, sweeps) applies to any market. The agent must apply the *method* to whatever chart is brought, not hardcode BTC.
- **Trade history:** No personal trades; learning loop is built only on the trader's own public material.

## The core gap

The target prompt depends on three concepts that exist in the source notes but are **not yet codified as first-class, followable rules** in `profiles/first-trader.md`:

1. **Hyblock liquidation clusters / heatmaps** as a primary read (not just Setup 6 confluence).
2. **W-patterns / double bottoms & M-patterns / double tops** as named, triggerable setups.
3. **Exact scaling logic** (e.g. 25% / 50% / 75% scale-in and scale-out) with conditions.

Closing this gap is the spine of Phase 1–2. Everything else supports it.

---

## Phase 1 — Rebuild the agent's spine (output + identity)  ·  ✅ DONE (2026-06-13)

Goal: the agent reliably produces the exact target structure, every time.

1. **Rewrite `prompts/system-mentor.md`** to encode the "CrypNuevo Trading Mentor" persona and the fixed 7-section output:
   - Current Market Structure → What Matches Right Now → What Is Still Missing → Exact Conditions for Entry → Risk Management & Targets → Psychology Note → Final Recommendation (EXECUTE / PARTIAL SCALE / WAIT FOR [condition] / NO SETUP).
   - Preserve the identity boundary: it is a *mentor trained on public material*, not the real person. (The "CrypNuevo Trading Mentor" name is a persona; it must not claim to BE CrypNuevo.)
   - Bake in the "never just say wait — say the *specific* missing condition" rule.
2. **Rewrite `prompts/chart-review.md`** to match the new structure (retire the old 14-section format or keep it as a deep-dive variant).
3. **Add a one-line `AGENT.md` / loader** that states: read system-mentor.md + profile + relevant library notes before answering. Makes the agent reproducible in any session.

Deliverable: paste a chart → get the exact 7-section format with CrypNuevo language.

## Phase 2 — Polish the profile to "established"  ·  high priority

Goal: every concept the output format demands is a codified rule with conditions, trigger, invalidation, and evidence link.

1. **Add codified setups** to the playbook in `profiles/first-trader.md`:
   - **W-pattern / double-bottom long** and **M-pattern / double-top short** (sweep of equal lows/highs → reclaim → second leg). Evidence already in weekly-update-index (Oct 27 2024, May 26 2024).
   - **Hyblock liquidation-magnet read** elevated to a primary step: identify long vs short liquidation clusters, treat untaken clusters as magnets, require a cluster to be *taken* before reversal entries.
2. **Codify scaling logic** — turn the scattered 25/50/75% observations into an explicit, conditional **scale-in / scale-out playbook** (entry tranches on confirmation/retest; profit tranches at wick-fill / mid-range / range-high). Evidence: trading-dna.md, before-after-patterns.md, Apr 8 2024 post.
3. **Fill the empty folders:**
   - `library/first-trader/risk-rules/` — position sizing, max risk per idea, R:R floor, no-trade triggers, event-day rules.
   - `library/first-trader/personality-notes/` — tone, recurring phrases, psychology lines (feeds the "Psychology Note" section).
4. **Build a Setup Router** (`library/first-trader/setup-router.md`): a decision tree mapping observed chart conditions → which of the 15+ setups applies → what trigger/invalidation to quote. This is what lets the agent "silently analyze, then pick the right setup." · ✅ DONE (2026-07-03) — routes Setups 1-20 with global gates and a trigger-quality check.
5. Flip profile `Confidence level` to `established` once 1–4 are done and evals pass.

## Phase 3 — Hybrid live-data layer  ·  medium priority

Goal: the agent fetches current context instead of relying only on what you paste.

1. **`prompts/market-context.md`** — a routine that assembles current context before any review.
2. **Live feeds** (via WebFetch/WebSearch or small scripts in a new `tools/` dir):
   - BTC/ETH spot price + 4H/1D structure.
   - DXY, SPX, BTC dominance, TOTAL3.
   - Economic calendar — flag CPI/FOMC/Powell/labor days for the current week.
   - Liquidation heatmap — Hyblock/Coinglass. (Likely manual-paste or screenshot first; investigate API access.)
3. **Auto-inject** the assembled context into the chart-review flow so "What Is Still Missing" can reference real, current levels.

Note: heatmap data is the hardest to automate; expect a manual screenshot step initially, automate later.

## Phase 4 — Evaluation & feedback loop  ·  medium priority

Goal: changes are regression-tested, not vibe-checked.

1. **Rewrite `evaluations/test-cases.md`** into scored golden cases that assert the new 7-section output (e.g. "given equal lows untaken, agent says WAIT FOR sweep + reclaim, not EXECUTE"). · ✅ DONE (2026-07-03) — 21 router-aware cases (A1-E3) with expected route/verdict + automatic fails.
2. **Add a rubric** (`evaluations/scoring-rubric.md`): points for structure adherence, correct setup match, specific (not generic) missing-conditions, honest no-trade calls, evidence citation. · ✅ DONE (2026-07-03) — 6 dimensions / 100 pts, pass ≥ 85 + zero automatic fails, run-log template.
3. **Self-critique pass** prompt the agent can run on its own answer before finalizing. · ✅ DONE (2026-07-03) — 7-question pass in the rubric, wired into system-mentor workflow.
4. Run the rubric after every profile/prompt change; log regressions in the acceptance checklist.

## Phase 5 — Session logging & continuous polish  ·  ongoing

Goal: a durable record that sharpens the profile over time.

1. **`sessions/first-trader/` review log** template matching the new output; one file per review.
2. Periodically mine new CrypNuevo posts/videos → ingest via `prompts/source-ingestion.md` → update profile only when a pattern repeats across evidence.
3. Track which setups the agent flags most and whether the trader's own follow-ups confirmed them (before/after curation).

---

## Suggested execution order

1. Phase 1 (spine) — immediate, unblocks everything.
2. Phase 2.1–2.4 (codify W/M patterns, Hyblock, scaling, router, fill folders).
3. Phase 4.1–4.2 (golden cases + rubric) — so Phase 2 changes are verifiable.
4. Phase 3 (live data) — once the offline agent is sharp.
5. Phase 5 — ongoing.

## Open questions

- Hyblock: do you have a paid API key, or will we screenshot-paste heatmaps for now?
- Live price/macro: OK to pull from free public sources (e.g. exchange APIs, a calendar site) via WebFetch?
- ~~Markets~~ → Resolved: market-agnostic, method-first (BTC/gold/crypto primary).
