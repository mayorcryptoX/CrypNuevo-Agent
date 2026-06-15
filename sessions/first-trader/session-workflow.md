# Chart Review Session Workflow

Use this workflow whenever you want the assistant to review your own chart.

## Before Asking

Prepare:

- Chart screenshot
- Market and symbol
- Timeframe
- Your bias
- Your entry idea
- Your stop or invalidation
- Your target
- What you want checked

If you do not know the invalidation yet, say that. The assistant should help define what would prove the idea wrong.

## Prompt To Use In Codex

```text
Use `profiles/first-trader.md`, `prompts/system-mentor.md`, and `prompts/chart-review.md`.

Review this chart as a style-informed mentor. Do not claim to be the real trader.

Market:
Timeframe:
My idea:
Entry:
Invalidation:
Target:
Question:

Chart:
<attach or describe chart>
```

## Save The Result

Copy `templates/chart-review-session-template.md` into this folder and save the review with a date-based name:

```text
YYYY-MM-DD-market-timeframe-topic.md
```

Example:

```text
2026-06-12-btc-1h-range-review.md
```

