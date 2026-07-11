"""Create a focused weekly learning workspace for a course."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def normalize_course(value: str) -> str:
    course = re.sub(r"\s+", "-", value.strip()).upper()
    if not re.fullmatch(r"[A-Z]+-\d+[A-Z0-9-]*", course):
        raise argparse.ArgumentTypeError("use a course code such as CS-530")
    return course


def prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def next_week(root: Path, course: str) -> int:
    course_dir = root / course
    weeks: list[int] = []
    if course_dir.exists():
        for path in course_dir.iterdir():
            match = re.fullmatch(r"Week-(\d+)", path.name, re.IGNORECASE)
            if path.is_dir() and match:
                weeks.append(int(match.group(1)))
    return max(weeks, default=0) + 1


def week_dashboard(course: str, week: int, title: str) -> str:
    label = f"Week {week:02d}"
    heading = f"{label}: {title}" if title else label
    return f"""# {course} — {heading}

## This week's target

In one sentence: what should I be able to explain or do by the end of this week?

## Minimum viable week

- [ ] Preview the headings, objectives, assignment rubric, and summary
- [ ] Choose 3–5 ideas that matter most
- [ ] Explain each idea in [findings.md](findings.md)
- [ ] Test myself without looking at the notes
- [ ] Complete [journal.md](journal.md), if assigned
- [ ] Write the three-line weekly recap below

## Assignment

- Deliverable:
- Due:
- Definition of done:
- Questions or risks:

## Retrieval check

Answer from memory before checking the notes:

1. What are the three most important ideas this week?
2. How are they connected?
3. Where would I use them in real software?
4. What am I still fuzzy about?

## Weekly recap

- I learned:
- I can now:
- Next week I should remember:
"""


def findings_index(course: str, week: int) -> str:
    return f"""# {course} Week {week:02d} Findings

This is the index and review sheet. Add a topic file only when an idea needs more room.

## Learning queue

| Topic | Why it matters | Confidence (1–5) | Note |
| --- | --- | ---: | --- |
| Example topic | Connection to the objective or assignment | 1 | [Open](findings/01-example-topic.md) |

## Explain it simply

For each important idea, write:

- **Plain English:** What is it, without textbook language?
- **WoW analogy:** What familiar system, class, encounter, or mechanic behaves similarly?
- **Software example:** Where would this appear in a real codebase?
- **Boundary:** Where does the analogy stop working?
- **Self-test:** What question can I answer without looking?

## Connections

How do this week's ideas connect to earlier weeks or to each other?

## Muddiest point

What still does not make sense, and what is the smallest question that would unblock it?
"""


def journal(course: str, week: int, assignment: str) -> str:
    assignment = assignment or f"Module {week} Journal"
    return f"""---
assignment: {assignment}
date: YYYY-MM-DD
author: Andy Tamburino
course: {course}
title: Journal Title
subtitle:
---

Opening paragraph goes here.

## Section Heading

Body paragraph goes here.

## Challenges

Body paragraph goes here.

## References

Reference entry goes here.
"""


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a weekly learning workspace.")
    parser.add_argument("--course", help="Course code, such as CS-530.")
    parser.add_argument("--week", type=int, help="Week number (1 or greater).")
    parser.add_argument("--title", default="", help="Optional weekly theme.")
    parser.add_argument("--assignment", default="", help="Optional journal assignment name.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT / "Notes", help=argparse.SUPPRESS)
    args = parser.parse_args()
    interactive = args.course is None or args.week is None

    try:
        args.course = normalize_course(args.course or prompt("Course", "CS-530"))
    except argparse.ArgumentTypeError as error:
        parser.error(str(error))

    if args.week is None:
        suggested_week = next_week(args.root, args.course)
        raw_week = prompt("Week", str(suggested_week))
        try:
            args.week = int(raw_week)
        except ValueError:
            parser.error("week must be a number")

    if interactive and not args.title:
        args.title = prompt("Weekly topic (optional)")
    if interactive and not args.assignment:
        args.assignment = prompt("Assignment name (optional)")

    if args.week < 1:
        parser.error("--week must be 1 or greater")

    week_dir = args.root / args.course / f"Week-{args.week:02d}"
    if week_dir.exists():
        parser.error(f"week already exists: {week_dir}")

    (week_dir / "findings").mkdir(parents=True)
    (week_dir / "sources").mkdir()
    write_new(week_dir / "README.md", week_dashboard(args.course, args.week, args.title))
    write_new(week_dir / "findings.md", findings_index(args.course, args.week))
    write_new(week_dir / "findings" / ".gitkeep", "")
    write_new(week_dir / "journal.md", journal(args.course, args.week, args.assignment))
    write_new(week_dir / "sources" / ".gitkeep", "")
    print(week_dir)


if __name__ == "__main__":
    main()
