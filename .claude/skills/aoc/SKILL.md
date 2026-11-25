---
name: aoc
description: Solve one Advent of Code day end to end as fast as possible — fetch, solve both parts, submit, log, commit and push. Use for "/aoc YEAR DAY", live midnight runs, and practice runs on past years.
---

# /aoc YEAR DAY

Speed matters: the clock starts at unlock (live) or first fetch (practice). Don't
pause to ask questions; the owner has given standing approval to submit answers and
push to `main`. Work in the repo root. All site access goes through `tools/aoc.py`.

## Steps

1. **Fetch.** `python3 tools/aoc.py wait YEAR DAY` for a live run (sleeps until
   unlock), or `fetch` for a practice run. This writes `YEAR-claude/dayNN/`:
   `puzzle.md` (text), `input`, `example-N` (every `<pre>` block), `log.json`.
2. **Read `puzzle.md`.** Identify which `example-N` file is the sample input and the
   expected sample answer stated in the text.
3. **Write `solve.py`** in the day folder. Convention:
   `python3 solve.py [FILE]` (default `input`) prints part 1, and part 2 once written,
   one per line as `part1: X` / `part2: Y`. Stdlib only unless a library is a big win.
   Write straightforward code first; optimize only if it is too slow (> ~30 s).
4. **Check the example** before every submission. If the example answer doesn't
   match, fix the code; never submit an answer the example contradicts.
5. **Submit**: `python3 tools/aoc.py submit YEAR DAY 1 ANSWER`.
   - Exit 0: correct. `puzzle.md` now includes part 2; continue with part 2.
   - Exit 1: wrong (log notes too high/too low). Re-read the puzzle for a missed
     rule, check edge cases, then try again. The tool refuses repeated answers.
   - Exit 2: rate-limited or unexpected response; read the message, wait as told.
   - Exit 3: three wrong answers. **Stop**, write what you know in the README under
     "Needs a human", commit and push what you have.
6. **Part 2** the same way, extending `solve.py`. On the final day (day 12 in 12-day
   years, day 25 in older years) part 2 is usually a free star that needs every other
   star; if the text says so, note it in the README and skip it if not yet eligible.
7. **README.md** in the day folder (template below). Fill the timing table with
   `python3 tools/aoc.py report YEAR DAY`.
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
