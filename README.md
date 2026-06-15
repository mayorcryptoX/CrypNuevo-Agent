# Trader Mentor Knowledge Base

This project is a local Codex knowledge base for building one style-informed trading mentor from public trader material.

The assistant is not the real trader and must never claim to be. It should answer as a mentor trained on the trader's public style, strategy, examples, and risk language.

## Main Goal

Build a structured library from public videos, transcripts, X posts, chart explanations, and trade recaps, then use that library to review your own BTC, crypto, and gold charts.

The ideal answer should help you understand:

- What the chart is showing
- What context is missing
- What levels, liquidity, invalidation, and confirmation matter
- Whether your idea matches the trader's known playbook
- What to check before risking money

## Folder Map

- `sources/` - raw public source references and original notes
- `library/` - cleaned summaries, strategy notes, personality notes, setup examples, and risk rules
- `profiles/` - the living trader profile used by the assistant
- `prompts/` - reusable prompts for ingestion, chart review, trade review, and learning mode
- `examples/` - high-quality example analyses and reference outputs
- `evaluations/` - tests and checklists for answer quality
- `sessions/` - your own chart reviews and study sessions

## First Trader Workflow

1. Choose one trader.
2. Copy `templates/trader-profile-template.md` into `profiles/<trader-slug>.md`.
3. For each public source, copy `templates/source-template.md` into the right `sources/<trader-slug>/...` folder.
4. Paste the source link, transcript/post text, chart notes, and your observations.
5. Use `prompts/source-ingestion.md` to turn the raw source into a clean library note.
6. Save the clean note in `library/<trader-slug>/`.
7. Update the trader profile only when a rule, setup, habit, or repeated phrase appears across evidence.
8. Test the profile with `evaluations/acceptance-checklist.md`.

## Evidence Rules

- Prefer public material.
- Keep source URLs and dates.
- Store summaries, tags, and short excerpts only.
- Do not paste huge copyrighted transcripts into final assistant answers.
- Separate facts from interpretation.
- If the library does not support a claim, the assistant should say so.

## Safety Boundary

This project is for education, chart review, and decision support. It should not produce guaranteed calls, impersonate a trader, or encourage blind entries. Every review should include invalidation and risk context.

