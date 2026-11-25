# 2025 Day 10: Factory

Mode: practice · clock started 2026-11-25T23:31:44+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `507` | 0:00:19 | 0 |
| 2 | `18981` | 0:01:01 | 0 |

## Approach
Part 1: Lights are XOR over GF(2), so each button is pressed 0 or 1 times; try subsets in increasing size and take the first whose XOR matches the target.
Part 2: Minimum presses so the button sums hit the joltage vector exactly. Without scipy, used parity recursion: the set of buttons pressed an odd number of times must match the target's parity, so f(b) = min over matching subsets S (with effect <= b) of |S| + 2*f((b - effect(S)) / 2), memoized. Subsets are precomputed and grouped by parity pattern. Runs in about 0.4 s.

## Log
- Both parts correct on first submission.
- The first two part 2 submissions were rejected by the site's rate limit (exit 2, "2s left to wait"), probably because other agents were submitting other days on the same account at the same time. A retry loop with a short backoff got through.
