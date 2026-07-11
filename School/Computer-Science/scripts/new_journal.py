"""Create a new master's journal Markdown draft."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUTHOR = "Andy Tamburino"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "journal"


def today_label() -> str:
    return date.today().strftime("%B %d, %Y").replace(" 0", " ")


def draft_text(args: argparse.Namespace) -> str:
    assignment_slug = slugify(args.assignment)
    author_slug = slugify(args.author.split()[-1])
    output_name = f"{assignment_slug}-{author_slug}.docx"

    return f"""---
assignment: {args.assignment}
date: {args.date}
author: {args.author}
course: {args.course}
title: {args.title}
subtitle: {args.subtitle}
output: ../generated/{output_name}
---

Opening paragraph goes here.

## Section Heading

Body paragraph goes here.

## Challenges

Body paragraph goes here.

## References

Reference entry goes here.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new journal draft.")
    parser.add_argument("--assignment", required=True, help="Assignment name, such as 'Module Five Activity'.")
    parser.add_argument("--title", required=True, help="Journal title.")
    parser.add_argument("--subtitle", default="", help="Optional subtitle.")
    parser.add_argument("--course", default="CS 000", help="Course code/name.")
    parser.add_argument("--author", default=DEFAULT_AUTHOR, help="Student name.")
    parser.add_argument("--date", default=today_label(), help="Display date.")
    parser.add_argument("--out", type=Path, help="Optional draft output path.")
    args = parser.parse_args()

    output = args.out
    if output is None:
        output = DEFAULT_ROOT / "Journals" / "drafts" / f"{slugify(args.assignment)}.md"

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(draft_text(args), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
