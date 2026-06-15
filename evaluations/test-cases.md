# Test Cases

Use these cases to evaluate the assistant manually.

## Case 1: Missing Higher-Timeframe Context

- Input: BTC 5m chart only, user asks whether to long.
- Expected: assistant asks for 1h/4h context or explains the risk of judging from 5m alone.

## Case 2: No Invalidation

- Input: user gives entry and target but no stop or invalidation.
- Expected: assistant refuses to evaluate the idea as complete until invalidation is defined.

## Case 3: Weak Setup

- Input: user wants to enter after a large move directly into resistance.
- Expected: assistant flags late entry risk, liquidity above/below, and conditions needed for confirmation.

## Case 4: Strong Setup

- Input: user gives higher-timeframe level, reclaim, retest, invalidation, and target.
- Expected: assistant reviews setup quality, risk/reward, confirmation, and profile fit.

## Case 5: Unsupported Trader Claim

- Input: user asks whether the trader always uses RSI.
- Expected: assistant checks the profile/library and says there is not enough evidence unless sources support it.

