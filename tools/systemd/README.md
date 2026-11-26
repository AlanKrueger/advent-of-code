# Scheduled runs

Two systemd user timers drive the unattended runs, both in US Eastern time every
night in November and December. `tools/scheduled_run.sh` decides what each night is:

| Timer | When (ET) | Does |
|-------|-----------|------|
| `aoc-precheck.timer` | 23:00 | cookie works, git up to date, CLI and libraries present |
| `aoc-run.timer` | 23:55 | starts headless `claude -p "/aoc YEAR DAY"`, which waits for the unlock |

- **Nov 26–30:** rehearsal. An already-solved 2025 day (Nov 26 is day 1, Nov 27 is day 2, …)
  in a throwaway worktree at `~/.local/state/aoc/rehearsal-worktree`, with a pretend
  unlock at midnight. Answers are checked against the site, not submitted, and the
  push is `--dry-run`.
- **Dec 1–12, 2026:** live, in the main checkout. Change `LIVE_LAST_DAY` in the script
  if the event has 25 days.

Logs are in `~/.local/state/aoc/logs/` (`*-run.log` is the summary, `*-claude.jsonl`
the full transcript). Failures also raise a desktop notification.

## Install / remove

```bash
for u in aoc-precheck.service aoc-precheck.timer aoc-run.service aoc-run.timer; do
  ln -sf "$PWD/tools/systemd/$u" ~/.config/systemd/user/$u; done
systemctl --user daemon-reload
systemctl --user enable --now aoc-precheck.timer aoc-run.timer
```

```bash
systemctl --user disable --now aoc-precheck.timer aoc-run.timer
```

## Rehearse right now

```bash
systemd-run --user --unit=aoc-rehearsal-now --collect -p Type=oneshot -p TimeoutStartSec=2h \
  --setenv=AOC_TARGET=rehearsal --setenv=AOC_DAY=3 \
  --setenv=AOC_UNLOCK=$(date -d '+3 min' --iso-8601=seconds) \
  /bin/bash "$PWD/tools/scheduled_run.sh" run
```
