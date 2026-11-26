# 2024 Day 24: Crossed Wires

Mode: practice · clock started 2026-11-26T00:06:50+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `45213383376616` | 0:02:42 | 117s | 0 |
| 2 | `cnk,mps,msq,qwf,vhm,z14,z27,z39` | 0:05:05 | 109s | 0 |

## Approach
Part 1: Memoised recursive evaluation of each gate's output, then read the z wires as a binary number.
Part 2: The circuit is a ripple-carry adder. Flag gate outputs that break its structure: z outputs other than the top bit must come from XOR; XORs not on x/y inputs must output z; x/y XORs (except bit 0) must feed an XOR; ANDs (except bit 0) must feed an OR. That flags exactly 8 wires. A throwaway check tried all 105 pairings of those 8 and found exactly one that makes the circuit add 30 random 45-bit pairs correctly.

## Log
- Recognised the puzzle from training data (the ripple-carry adder with four swapped output pairs), so I wrote the structural-rule approach for part 2 before part 2 unlocked.
- The part 2 example is an AND-only toy circuit that the adder rules don't apply to, so I verified with the random-addition check instead of the example.
- Both parts were correct on the first submit.
