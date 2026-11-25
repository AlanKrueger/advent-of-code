# 2025 Day 6: Trash Compactor

Mode: practice · clock started 2026-11-25T23:31:43+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `3525371263915` | 0:00:20 | 0 |
| 2 | `6846480843636` | 0:00:32 | 0 |

## Approach
Part 1: Pad all lines to equal width, split the worksheet into problems at all-space columns, read each row slice as a number, and add or multiply per the operator row.
Part 2: Same blocks, but each column within a block forms one number (digits top to bottom). Column order doesn't matter for + or *, so no reversal is needed.

## Log
- Both parts were written before submitting part 1, since the puzzle is from before the model's training cutoff; part 2 was checked against the part 2 example before submitting. Time is optimistic compared with an unseen puzzle.
- Leading and trailing spaces in each line are significant (they set column alignment), so the input must not be stripped per line. All input lines happen to be the same width; the code pads anyway.
