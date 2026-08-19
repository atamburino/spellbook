"""A local-first calendar tool.

Events live in a single .ics file in data/ (never committed — see
.gitignore), so "book something on my calendar" works out of the box with
no cloud account, no OAuth, nothing to sign up for. The .ics file is a
standard format any real calendar app can subscribe to or import, so this
is a genuine bridge to Apple/Google Calendar later, not a toy format —
swap this module for one that talks to the Google Calendar or EventKit API
and nothing else in the codebase changes.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta
from pathlib import Path

from icalendar import Calendar, Event

DEFAULT_ICS_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "calendar.ics"

SPEC = [
    {
        "name": "add_calendar_event",
        "description": (
            "Add an event to the user's calendar. Times must be ISO 8601 "
            "(e.g. '2026-08-20T15:00:00'). Ask the user for anything "
            "ambiguous (which day, timezone) before calling this."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "description": "ISO 8601 start time."},
                "end": {
                    "type": "string",
                    "description": "ISO 8601 end time. Optional — defaults to start + 30 min.",
                },
                "notes": {"type": "string", "description": "Optional description."},
            },
            "required": ["title", "start"],
        },
    },
    {
        "name": "list_upcoming_events",
        "description": "List upcoming events on the user's calendar.",
        "input_schema": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Max number of events to return. Default 10.",
                }
            },
            "required": [],
        },
    },
]


def _load(ics_path: Path) -> Calendar:
    if ics_path.exists():
        return Calendar.from_ical(ics_path.read_bytes())
    cal = Calendar()
    cal.add("prodid", "-//Evelyn//local-calendar//")
    cal.add("version", "2.0")
    return cal


def _save(cal: Calendar, ics_path: Path) -> None:
    ics_path.parent.mkdir(parents=True, exist_ok=True)
    ics_path.write_bytes(cal.to_ical())


def handle(name: str, tool_input: dict, ics_path: Path = DEFAULT_ICS_PATH) -> str:
    cal = _load(ics_path)

    if name == "add_calendar_event":
        start = datetime.fromisoformat(tool_input["start"])
        end_raw = tool_input.get("end")
        end = datetime.fromisoformat(end_raw) if end_raw else start + timedelta(minutes=30)

        event = Event()
        event.add("uid", str(uuid.uuid4()))
        event.add("summary", tool_input["title"])
        event.add("dtstart", start)
        event.add("dtend", end)
        event.add("dtstamp", datetime.now())
        if tool_input.get("notes"):
            event.add("description", tool_input["notes"])

        cal.add_component(event)
        _save(cal, ics_path)
        return f"Added '{tool_input['title']}' to the calendar at {start.isoformat()}."

    if name == "list_upcoming_events":
        limit = tool_input.get("limit", 10)
        now = datetime.now()
        events = []
        for component in cal.walk("VEVENT"):
            dtstart = component.get("dtstart").dt
            if isinstance(dtstart, datetime) and dtstart.replace(tzinfo=None) < now:
                continue
            events.append((dtstart, str(component.get("summary"))))
        events.sort(key=lambda e: str(e[0]))

        if not events:
            return "No upcoming events."
        return "\n".join(f"- {dt}: {summary}" for dt, summary in events[:limit])

    raise ValueError(f"calendar_tool cannot handle {name!r}")
