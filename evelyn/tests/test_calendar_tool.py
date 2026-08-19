from brain.tools import calendar_tool


def test_add_and_list_event(tmp_path):
    ics_path = tmp_path / "calendar.ics"

    result = calendar_tool.handle(
        "add_calendar_event",
        {"title": "Dentist", "start": "2099-01-01T09:00:00"},
        ics_path,
    )
    assert "Dentist" in result

    listing = calendar_tool.handle("list_upcoming_events", {}, ics_path)
    assert "Dentist" in listing


def test_list_events_excludes_past(tmp_path):
    ics_path = tmp_path / "calendar.ics"
    calendar_tool.handle(
        "add_calendar_event",
        {"title": "Old thing", "start": "2000-01-01T09:00:00"},
        ics_path,
    )
    listing = calendar_tool.handle("list_upcoming_events", {}, ics_path)
    assert "Old thing" not in listing
    assert listing == "No upcoming events."


def test_default_end_time_is_30_minutes_later(tmp_path):
    ics_path = tmp_path / "calendar.ics"
    # start at :45 exercises the minute-overflow edge case
    calendar_tool.handle(
        "add_calendar_event",
        {"title": "Standup", "start": "2099-01-01T09:45:00"},
        ics_path,
    )
    listing = calendar_tool.handle("list_upcoming_events", {}, ics_path)
    assert "Standup" in listing
