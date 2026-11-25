#!/usr/bin/env python3
"""Advent of Code helper for Claude's automated runs.

Commands:
  wait    YEAR DAY             sleep until the puzzle unlocks, then fetch it
  fetch   YEAR DAY             download puzzle text, examples and input
  submit  YEAR DAY PART ANSWER submit an answer (or check it, if already solved)
  status  YEAR DAY             show what is solved and the attempt log
  report  YEAR DAY             print a markdown timing table for the day README

Files live in <YEAR>-claude/dayNN/. puzzle.md and input are gitignored;
log.json and example-N files are committed.

Session cookie: ~/.config/aoc/session (or $AOC_SESSION_FILE), contents only.
"""

from __future__ import annotations

import argparse
import fcntl
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
import os

REPO = Path(__file__).resolve().parent.parent
BASE = "https://adventofcode.com"
USER_AGENT = (
    "github.com/AlanKrueger/advent-of-code tools/aoc.py "
    "(automated runs by Claude Code; owner-operated)"
)
SESSION_FILE = Path(os.environ.get("AOC_SESSION_FILE", Path.home() / ".config/aoc/session"))
THROTTLE_FILE = Path.home() / ".cache/aoc/last-request"
SUBMIT_LOCK = Path.home() / ".cache/aoc/submit.lock"
MAX_COOLDOWN_WAIT = 300  # seconds to keep retrying "answered too recently"
MIN_INTERVAL = 3.0  # seconds between any two requests to the site
MAX_WRONG = 3  # wrong answers allowed per part before we stop
EST = timezone(timedelta(hours=-5))  # AoC unlocks at midnight UTC-5


# ---------------------------------------------------------------- utilities

def now() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


def unlock_time(year: int, day: int) -> datetime:
    return datetime(year, 12, day, 0, 0, 0, tzinfo=EST)


def day_dir(year: int, day: int) -> Path:
    return REPO / f"{year}-claude" / f"day{day:02d}"


def log_path(year: int, day: int) -> Path:
    return day_dir(year, day) / "log.json"


def load_log(year: int, day: int) -> dict:
    p = log_path(year, day)
    if p.exists():
        return json.loads(p.read_text())
    return {"year": year, "day": day, "unlock": iso(unlock_time(year, day)),
            "started": None, "parts": {"1": {"attempts": []}, "2": {"attempts": []}}}


def save_log(year: int, day: int, log: dict) -> None:
    p = log_path(year, day)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(log, indent=2) + "\n")


def session() -> str:
    try:
        token = SESSION_FILE.read_text().strip()
    except FileNotFoundError:
        sys.exit(f"No session cookie at {SESSION_FILE}. Put your AoC session cookie value there.")
    if not token:
        sys.exit(f"{SESSION_FILE} is empty.")
    return token


def throttle() -> None:
    THROTTLE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        last = float(THROTTLE_FILE.read_text())
    except (FileNotFoundError, ValueError):
        last = 0.0
    wait = MIN_INTERVAL - (time.time() - last)
    if wait > 0:
        time.sleep(wait)
    THROTTLE_FILE.write_text(str(time.time()))


def request(path: str, data: dict | None = None) -> str:
    throttle()
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    req = urllib.request.Request(BASE + path, data=body, headers={
        "User-Agent": USER_AGENT,
        "Cookie": f"session={session()}",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode()


# ------------------------------------------------------------ HTML -> text

class ArticleParser(HTMLParser):
    """Turns <article class="day-desc"> blocks into markdown and collects <pre> examples."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_article = 0
        self.in_pre = False
        self.in_code = False
        self.out: list[str] = []
        self.pre_blocks: list[str] = []
        self._pre_buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article" and "day-desc" in (a.get("class") or ""):
            self.in_article += 1
            return
        if not self.in_article:
            return
        if tag == "h2":
            self.out.append("\n## ")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "pre":
            self.in_pre = True
            self._pre_buf = []
            self.out.append("\n\n```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.out.append("`")
        elif tag == "em" and not self.in_pre:
            self.out.append("**")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "a":
            self.out.append("[")
            self._href = a.get("href", "")

    def handle_endtag(self, tag):
        if not self.in_article:
            return
        if tag == "article":
            self.in_article -= 1
            self.out.append("\n")
        elif tag == "h2":
            self.out.append("\n")
        elif tag == "pre":
            self.in_pre = False
            self.pre_blocks.append("".join(self._pre_buf))
            self.out.append("```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = False
            self.out.append("`")
        elif tag == "em" and not self.in_pre:
            self.out.append("**")
        elif tag == "a":
            self.out.append(f"]({self._href})")

    def handle_data(self, data):
        if not self.in_article:
            return
        if self.in_pre:
            self._pre_buf.append(data)
        self.out.append(data)

    def markdown(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def parse_puzzle(page: str) -> ArticleParser:
    p = ArticleParser()
    p.feed(page)
    # Answers only appear in "Your puzzle answer was <code>X</code>" paragraphs.
    p.answers = [html.unescape(x) for x in
                 re.findall(r"Your puzzle answer was <code>([^<]*)</code>", page)]
    return p


def main_text(page: str) -> str:
    m = re.search(r"<main>(.*?)</main>", page, re.S)
    text = m.group(1) if m else page
    text = re.sub(r"<(style|script)\b.*?</\1>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


# ---------------------------------------------------------------- commands

def cmd_fetch(year: int, day: int, quiet: bool = False) -> ArticleParser:
    d = day_dir(year, day)
    d.mkdir(parents=True, exist_ok=True)
    log = load_log(year, day)
    if log["started"] is None:
        # Live runs time from unlock; practice runs time from first fetch.
        log["started"] = iso(max(now(), unlock_time(year, day)))
        log["mode"] = "live" if now() - unlock_time(year, day) < timedelta(hours=1) else "practice"
        save_log(year, day, log)

    page = request(f"/{year}/day/{day}")
    p = parse_puzzle(page)
    (d / "puzzle.md").write_text(p.markdown())
    for i, block in enumerate(p.pre_blocks, 1):
        f = d / f"example-{i}"
        if not f.exists():
            f.write_text(block)
    inp = d / "input"
    if not inp.exists():
        inp.write_text(request(f"/{year}/day/{day}/input"))

    if not quiet:
        print(f"Wrote {d.relative_to(REPO)}/puzzle.md, input, {len(p.pre_blocks)} example block(s)")
        if p.answers:
            print(f"Already solved on site: {len(p.answers)} part(s)")
    return p


def cmd_wait(year: int, day: int) -> None:
    target = unlock_time(year, day) + timedelta(seconds=1)
    while (delta := (target - now()).total_seconds()) > 0:
        print(f"Unlocks in {timedelta(seconds=int(delta))}", flush=True)
        time.sleep(min(delta, 60 if delta > 120 else max(delta, 0.2)))
    for attempt in range(20):
        try:
            cmd_fetch(year, day)
            return
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise
            time.sleep(min(2 + attempt, 10))
    sys.exit("Puzzle still not available after retries.")


def post_answer(year: int, day: int, part: int, answer: str) -> tuple[str, float]:
    """POST an answer, holding a cross-process lock so parallel runs on one account
    queue instead of tripping the site's per-account cooldown. Waits out
    "answered too recently" responses. Returns (message text, seconds spent waiting)."""
    SUBMIT_LOCK.parent.mkdir(parents=True, exist_ok=True)
    waited = 0.0
    with open(SUBMIT_LOCK, "w") as lock:
        t0 = time.time()
        fcntl.flock(lock, fcntl.LOCK_EX)
        waited += time.time() - t0
        while True:
            msg = main_text(request(f"/{year}/day/{day}/answer",
                                    {"level": str(part), "answer": answer}))
            if "too recently" not in msg:
                return msg, waited
            m = re.search(r"(?:(\d+)m\s*)?(\d+)s left", msg)
            pause = (int(m.group(1) or 0) * 60 + int(m.group(2)) + 1) if m else 10
            if waited + pause > MAX_COOLDOWN_WAIT:
                return msg, waited
            print(f"Cooldown: waiting {pause}s", flush=True)
            time.sleep(pause)
            waited += pause


def cmd_submit(year: int, day: int, part: int, answer: str) -> int:
    log = load_log(year, day)
    plog = log["parts"][str(part)]
    if plog.get("solved"):
        print(f"Part {part} already recorded as solved: {plog['answer']}")
        return 0
    prior = [a for a in plog["attempts"] if a["answer"] == answer]
    if prior:
        print(f"Already tried {answer}: {prior[-1]['result']}. Not resubmitting.")
        return 1
    wrong = sum(1 for a in plog["attempts"] if a["result"] in ("wrong", "too high", "too low"))
    if wrong >= MAX_WRONG:
        print(f"STOP: {wrong} wrong answers for part {part}. Leave a note for the human.")
        return 3

    # If the site already shows an answer for this part (e.g. the user solved it
    # by hand in a past year), check locally instead of submitting.
    page = request(f"/{year}/day/{day}")
    known = parse_puzzle(page).answers
    t = now()
    if len(known) >= part:
        result = "correct" if known[part - 1] == answer else "wrong"
        note = "checked against answer already on site"
    else:
        msg, waited = post_answer(year, day, part, answer)
        t = now()
        note = msg[:300]
        if "That's the right answer" in msg or "finished every puzzle" in msg:
            result = "correct"
        elif "too recently" in msg:
            print(msg)
            return 2  # still rate limited after MAX_COOLDOWN_WAIT; not counted
        elif "not the right answer" in msg:
            result = "too high" if "too high" in msg else "too low" if "too low" in msg else "wrong"
        elif "right level" in msg:
            print(msg)
            return 2
        else:
            print("Unrecognized response:", msg)
            return 2

    attempt = {"time": iso(t), "answer": answer, "result": result, "note": note}
    if len(known) < part and waited:
        attempt["cooldown_wait_s"] = round(waited, 1)
    plog["attempts"].append(attempt)
    if result == "correct":
        plog["solved"] = iso(t)
        plog["answer"] = answer
    save_log(year, day, log)
    print(f"Part {part}: {answer} -> {result}")
    if result == "correct" and part == 1:
        cmd_fetch(year, day, quiet=True)  # pull part 2 text
        text = (day_dir(year, day) / "puzzle.md").read_text()
        i = text.find("## --- Part Two ---")
        print("\n" + (text[i:] if i >= 0 else "(Part Two section not found in puzzle.md)"))
    return 0 if result == "correct" else 1


def fmt(td: timedelta) -> str:
    s = int(td.total_seconds())
    return f"{s // 3600:d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def cmd_report(year: int, day: int) -> None:
    log = load_log(year, day)
    start = parse_iso(log["started"])
    print(f"Mode: {log.get('mode', '?')} · clock started {log['started']}\n")
    print("| Part | Answer | Time from start | Cooldown waits | Wrong attempts |")
    print("|------|--------|-----------------|----------------|----------------|")
    for part in ("1", "2"):
        pl = log["parts"][part]
        wrong = sum(1 for a in pl["attempts"] if a["result"] != "correct")
        cool = sum(a.get("cooldown_wait_s", 0) for a in pl["attempts"])
        cool_s = f"{cool:.0f}s" if cool else "—"
        if pl.get("solved"):
            print(f"| {part} | `{pl['answer']}` | {fmt(parse_iso(pl['solved']) - start)} | {cool_s} | {wrong} |")
        else:
            print(f"| {part} | — | unsolved | {cool_s} | {wrong} |")


def cmd_status(year: int, day: int) -> None:
    print(json.dumps(load_log(year, day), indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["wait", "fetch", "submit", "status", "report"])
    ap.add_argument("year", type=int)
    ap.add_argument("day", type=int)
    ap.add_argument("part", type=int, nargs="?")
    ap.add_argument("answer", nargs="?")
    a = ap.parse_args()
    if a.command == "submit":
        if a.part not in (1, 2) or a.answer is None:
            ap.error("submit needs PART (1 or 2) and ANSWER")
        sys.exit(cmd_submit(a.year, a.day, a.part, a.answer.strip()))
    {"wait": cmd_wait, "fetch": cmd_fetch, "status": cmd_status, "report": cmd_report}[a.command](a.year, a.day)


if __name__ == "__main__":
    main()
