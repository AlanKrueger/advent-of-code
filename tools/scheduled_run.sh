#!/bin/bash
# Entry point for the systemd timers (see tools/systemd/).
#
#   scheduled_run.sh precheck   ~1 hour before unlock: cookie, git, CLI sanity checks
#   scheduled_run.sh run        a few minutes before unlock: start Claude on the day
#
# What "tonight" means is decided from the date in US Eastern time a few minutes
# from now (puzzles unlock at midnight ET):
#   - Dec 1..LIVE_LAST_DAY of LIVE_YEAR: a live run in the main checkout.
#   - REHEARSAL_DATES: a rehearsal. Same timer, same headless Claude, same skill,
#     but on an already-solved REHEARSAL_YEAR day in a throwaway git worktree,
#     with a pretend unlock at the coming midnight and `git push --dry-run`.
#     Nothing is submitted (the site already has those answers) or pushed.
#   - anything else: exit quietly.
#
# Overrides for testing: AOC_TARGET=rehearsal|live, AOC_YEAR, AOC_DAY, AOC_UNLOCK.

set -uo pipefail

MAIN=/home/alan/Projects/Personal/advent-of-code
LIVE_YEAR=2026
LIVE_LAST_DAY=12          # update if the 2026 event turns out to have 25 days
REHEARSAL_YEAR=2025
REHEARSAL_DATES="11-26 11-27 11-28 11-29 11-30"
STATE="$HOME/.local/state/aoc"
REHEARSAL_WT="$STATE/rehearsal-worktree"
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin"

mkdir -p "$STATE/logs"
mode=${1:-run}
stamp=$(date +%Y%m%d-%H%M%S)
log="$STATE/logs/$stamp-$mode.log"
exec > >(tee -a "$log") 2>&1

say() { echo "[$(date '+%F %T %Z')] $*"; }
alert() {
    say "ALERT: $*"
    notify-send -u critical "Advent of Code run" "$*" 2>/dev/null || true
}

# Decide tonight's target from the ET date 15 minutes from now.
target_md=$(TZ=America/New_York date -d '+15 min' +%m-%d)
target_month=${target_md%-*}; target_day=$((10#${target_md#*-}))
kind=${AOC_TARGET:-}
if [[ -z $kind ]]; then
    if [[ $target_month == 12 && $target_day -le $LIVE_LAST_DAY && $(TZ=America/New_York date -d '+15 min' +%Y) == "$LIVE_YEAR" ]]; then
        kind=live
    elif [[ " $REHEARSAL_DATES " == *" $target_md "* ]]; then
        kind=rehearsal
    else
        say "Nothing scheduled for $target_md ET."; exit 0
    fi
fi

if [[ $kind == live ]]; then
    year=${AOC_YEAR:-$LIVE_YEAR}; day=${AOC_DAY:-$target_day}; workdir=$MAIN
    unset AOC_UNLOCK
else
    # Rehearse a different solved day each night: Nov 26 -> day 1, Nov 27 -> day 2, ...
    year=${AOC_YEAR:-$REHEARSAL_YEAR}
    day=${AOC_DAY:-$(( (target_day - 26) % 12 + 1 ))}
    export AOC_UNLOCK=${AOC_UNLOCK:-$(TZ=America/New_York date -d "$(TZ=America/New_York date -d '+15 min' +%F) 00:00" --iso-8601=seconds)}
    workdir=$REHEARSAL_WT
fi
say "mode=$mode kind=$kind year=$year day=$day unlock=${AOC_UNLOCK:-real} workdir=$workdir"

prepare_git() {
    git -C "$MAIN" fetch -q origin || { alert "git fetch failed"; return 1; }
    if [[ $kind == live ]]; then
        [[ $(git -C "$MAIN" rev-parse --abbrev-ref HEAD) == main ]] || { alert "main checkout is not on main"; return 1; }
        git -C "$MAIN" pull -q --ff-only origin main || { alert "git pull --ff-only failed in $MAIN"; return 1; }
    else
        # Fresh throwaway worktree at origin/main, with tonight's day folder removed
        # so the run starts from scratch. Only this scratch copy is touched.
        git -C "$MAIN" worktree remove --force "$REHEARSAL_WT" 2>/dev/null
        rm -rf "$REHEARSAL_WT"
        git -C "$MAIN" worktree prune
        git -C "$MAIN" worktree add -q --detach "$REHEARSAL_WT" origin/main || { alert "could not create rehearsal worktree"; return 1; }
        rm -rf "$REHEARSAL_WT/$year-claude/day$(printf %02d "$day")"
    fi
}

precheck() {
    local ok=0
    command -v claude >/dev/null || { alert "claude CLI not on PATH"; ok=1; }
    prepare_git || ok=1
    (cd "$workdir" && python3 tools/aoc.py check "$year" "$day") || { alert "aoc.py check failed (cookie?)"; ok=1; }
    python3 -c "import numpy, scipy, networkx, sympy, z3" || { alert "solver libraries missing"; ok=1; }
    [[ $ok == 0 ]] && say "Pre-check passed." || say "Pre-check FAILED."
    return $ok
}

run() {
    precheck || alert "pre-check failed; trying the run anyway"
    local push_note=""
    if [[ $kind == rehearsal ]]; then
        push_note="This is a REHEARSAL of the unattended midnight run, on an already-solved
day in a throwaway worktree. Follow the skill exactly as for a live run (use \`wait\`),
except: in the commit step, commit normally but push with
\`git push --dry-run origin HEAD:main\` instead of a real push."
    fi
    local prompt="/aoc $year $day

You were started by a scheduled job a few minutes before the puzzle unlocks. Nobody
is watching: don't ask questions; follow the skill, and if you must stop, say why in
the day README (or, if there is none yet, in your final message).
$push_note"
    say "Starting claude in $workdir"
    cd "$workdir" || { alert "cannot cd to $workdir"; return 1; }
    claude -p "$prompt" \
        --permission-mode acceptEdits \
        --allowedTools "Bash(python3:*)" "Bash(timeout:*)" "Bash(git:*)" "Bash(cat:*)" \
            "Bash(ls:*)" "Bash(grep:*)" "Bash(sed:*)" "Bash(head:*)" "Bash(tail:*)" \
            "Bash(wc:*)" "Read" "Write" "Edit" "Glob" "Grep" "Skill" \
        --output-format stream-json --verbose > "$STATE/logs/$stamp-claude.jsonl"
    local rc=$?
    say "claude exited with $rc"
    local d="$workdir/$year-claude/day$(printf %02d "$day")"
    if [[ -f $d/log.json ]]; then
        (cd "$workdir" && python3 tools/aoc.py report "$year" "$day")
    else
        alert "no log.json for $year day $day after the run"
    fi
    [[ $kind == live ]] && git -C "$MAIN" log --oneline -1 origin/main
    [[ $rc == 0 ]] || alert "claude exited with $rc"
}

case $mode in
    precheck) precheck ;;
    run) run ;;
    *) echo "usage: $0 precheck|run"; exit 2 ;;
esac
