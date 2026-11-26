---
name: aoc
description: Solve one Advent of Code day end to end as fast as possible — fetch, solve both parts, submit, log, commit and push. Use for "/aoc YEAR DAY", live midnight runs, and practice runs on past years.
---

# /aoc YEAR DAY

Speed matters: the clock starts at unlock (live) or first fetch (practice). Don't
pause to ask questions; the owner has given standing approval to submit answers and
push to `main`. Work in the repo root. All site access goes through `tools/aoc.py`.

If the prompt says a coordinator will commit (parallel practice runs), do steps 1–7,
skip step 8, and write only inside your own day folder.

## Steps

1. **Fetch.** `python3 tools/aoc.py wait YEAR DAY` for a live run (sleeps until
   unlock), or `fetch` for a practice run. This writes `YEAR-claude/dayNN/`:
   `puzzle.md` (text), `input`, `example-N` (every `<pre>` block), `log.json`.
2. **Read `puzzle.md`.** Identify which `example-N` file is the sample input and the
   expected sample answer stated in the text.
   - Every code block becomes an `example-N` file. Usually `example-1` is the sample
     input; later blocks are often diagrams or intermediate output, not inputs.
   - Numbering continues when part 2 unlocks: part 2's blocks get the next numbers.
   - Expected answers are usually bold numbers, shown as `` `**N**` `` in `puzzle.md`.
   - Note any parameter that differs between example and real input (e.g. "after 10
     steps" in the example vs 1000 for the real input).
3. **Write `solve.py`** in the day folder. Convention:
   `python3 solve.py [FILE] [PARAMS...]` (default `input`) prints part 1, and part 2
   once written, one per line as `part1: X` / `part2: Y`. Use the optional extra
   arguments for example-vs-real parameters, with the real value as the default.
   - Stdlib first. Installed and fine to use when they're a clear win: numpy, scipy
     (e.g. `scipy.optimize.milp` for integer programs), networkx (graphs), sympy
     (algebra), z3 (constraint solving). Don't install packages mid-run; if something
     else is missing, write the stdlib approach.
   - Write straightforward code first; optimize only if it is too slow (> ~30 s).
   - Always run with `timeout 60 python3 solve.py ...` so a slow attempt can't hang
     the run. Never `pkill`/`kill` by pattern; other runs may share the machine.
   - You may draft part 2 from a guess before it unlocks, but only submit it after
     reading the real part 2 text and matching its example. If you recognise the
     puzzle from training data, say so in the README log (it affects the benchmark).
4. **Check the example** before every submission. If the example answer doesn't
   match, fix the code; never submit an answer the example contradicts.
5. **Submit**: `python3 tools/aoc.py submit YEAR DAY 1 ANSWER`. Run each submit as its
   own command with a long Bash timeout (e.g. 600000 ms): it may wait in a shared
   queue or the site's cooldown, printing "(waiting …)" lines while it does.
   - Exit 0: correct. The tool prints the part 2 text (also now in `puzzle.md`).
   - Exit 1: wrong (log notes too high/too low). Re-read the puzzle for a missed
     rule, check edge cases, then try again. The tool refuses repeated answers.
   - Exit 2: unexpected response, or still rate-limited after the tool's own waiting
     (it queues submits across processes and waits out the site's cooldown for up to
     5 minutes by itself). Read the message before doing anything else.
   - Exit 3: three wrong answers. **Stop**, write what you know in the README under
     "Needs a human", commit and push what you have.
6. **Part 2** the same way, extending `solve.py`. On the final day (day 12 in 12-day
   years, day 25 in older years) part 2 is usually a free star that needs every other
   star. If the page offers it (all other stars earned), claim it with
   `python3 tools/aoc.py submit YEAR DAY 2 0`; otherwise note it in the README and skip.
7. **README.md** in the day folder (template below). Paste the full output of
   `python3 tools/aoc.py report YEAR DAY`, including its "Mode" line.
8. **Commit and push** only this day's folder (plus any `tools/` fixes you made):
   ```
   git add YEAR-claude/dayNN
   git commit -m "YEAR-claude/dayNN"
   git push origin HEAD:main
   ```
   `puzzle.md` and `input` are gitignored and must stay out of the commit.
   If the push is rejected, `git pull --rebase origin main` then push again.
   Never force-push, never delete or rewrite existing files outside this day's folder.

## Day README template

```markdown
# YEAR Day N: <puzzle title>

<timing table from `aoc.py report`>

## Approach
Part 1: <one or two sentences>
Part 2: <one or two sentences>

## Log
- <what happened, in order: misreadings, wrong answers and why, slow first attempts>

## Needs a human
<only if stopped early>
```

Write the README plainly. No puzzle text beyond a short paraphrase (the puzzle
text is the site author's; don't copy it into the repo).
