# Advent of Code repo

- `2023/`, `2024/`: the owner's hand-written solutions. Don't modify them.
- `<year>-claude/dayNN/`: Claude's solutions (`solve.py`, `README.md`, `log.json`, `example-N`).
- `tools/aoc.py`: the only way to talk to adventofcode.com (throttled, cached, logs timing).
  Session cookie is read from `~/.config/aoc/session`; never print it or copy it anywhere.
- To solve a day, use the `/aoc YEAR DAY` skill.

Rules:
- Puzzle inputs and puzzle text are gitignored. Never commit them (don't `git add -f`).
- Additive commits only: no force-push, no history rewrites, no deleting existing files.
- Standing approval for AoC runs: submit answers via `tools/aoc.py` (max 3 wrong per part)
  and push solved days straight to `main`.
- Python 3, stdlib preferred; numpy, scipy, networkx, sympy and z3 are installed (via apt).
