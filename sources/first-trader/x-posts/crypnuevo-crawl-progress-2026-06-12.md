# CrypNuevo X Crawl Progress - 2026-06-12

## Current Logged-In Coverage

- Profile reports: 9,944 total posts.
- Media tab reports: 3,332 photos & videos.
- Media grid status IDs captured: 487.
- Date-search media posts captured with text: 787.
- Merged unique media status IDs captured: 1,023.
- Grid-only status detail pages recovered: 145 of 236.
- Grid-only status detail pages remaining: 91.
- Status detail pages needing retry because X returned zero articles: 26.
- Trading-relevant corpus entries captured: 860.
- Weekly/Sunday/update candidates captured: 205.
- Last updated: 2026-06-13, weekly/trading-focused pass.

Raw files:

- `sources/first-trader/x-posts/raw/crypnuevo-media-grid-links.json`
- `sources/first-trader/x-posts/raw/crypnuevo-search-media-posts.json`
- `sources/first-trader/x-posts/raw/crypnuevo-coverage-report.json`
- `sources/first-trader/x-posts/raw/crypnuevo-status-details.json`
- `sources/first-trader/x-posts/raw/crypnuevo-status-detail-retry-needed.json`
- `sources/first-trader/x-posts/raw/crypnuevo-weekly-update-index.json`
- `sources/first-trader/x-posts/raw/crypnuevo-trading-post-corpus.json`
- `library/first-trader/strategy-notes/crypnuevo-weekly-market-update-index.md`

## What Worked

- Logged-in X profile access is confirmed.
- Media tab exposed a media grid and allowed collection down to roughly mid-2024 before the visual pagination stopped.
- X date search worked for:
  - 2026-01 through 2026-06
  - 2025-01 through 2025-12
  - 2024-01 through 2024-06 via weekly retry windows
  - 2024-07-01 through 2024-07-08
  - 2024-08 through 2024-12
- Search results include useful post text, not only media links.

## What Failed Or Needs Retry

X search started returning `Something went wrong. Try reloading.` after many queries. This appears to be an X search/page-service error or temporary throttle, not a true no-result condition.

Known failed windows needing retry after the 2026-06-13 run:

- 2023-12-01 to 2024-01-01
- 2024-07-08 to 2024-07-15
- 2024-07-15 to 2024-07-22
- 2024-07-22 to 2024-07-29
- 2024-07-29 to 2024-08-01
- All pre-2024 windows remain pending.

## Next Crawl Plan

1. Continue grid-only status detail recovery for the remaining 91 IDs.
2. Retry 26 zero-article status pages with longer waits or a fresh tab.
3. Let X search cool down, then retry failed search windows and continue backward through 2023, 2022, and 2021.
4. Open collected media status IDs in batches and capture:
   - original post text
   - images/media count
   - CrypNuevo replies under the post
   - thread continuation posts
5. Give extra priority to weekly/Sunday market updates, weekly recaps, and posts referring to prior Sunday projections.
6. Convert high-signal chart posts into cleaned setup examples.

## Important Boundary

This is not complete yet. The current archive is a strong logged-in first tranche, but it is not all 9,944 posts and not all 3,332 media items.
