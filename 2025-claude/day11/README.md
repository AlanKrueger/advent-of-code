# 2025 Day 11: Reactor

Mode: practice · clock started 2026-11-25T23:31:42+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `724` | 0:00:15 | 0 |
| 2 | `473930047491888` | 0:00:39 | 0 |

## Approach
Part 1: The device graph is a DAG, so count paths from `you` to `out` with a memoized DFS.
Part 2: Paths through both `dac` and `fft` are the products of segment counts, svr->dac->fft->out plus svr->fft->dac->out (in a DAG only one order can be nonzero).

## Log
- Both parts correct on the first try; examples matched.
- The first part 2 submission hit the site's rate limit (exit 2, "2s left"), probably from other agents submitting on the same account; a retry a few seconds later went through.
- This puzzle is from before the model's training cutoff, so the time is optimistic compared with an unseen puzzle.
