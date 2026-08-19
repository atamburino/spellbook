"""The 'text my wife' tool — deliberately a dry-run stub by default.

Actually sending a text means talking to *something* outside your own
machine (a carrier, iMessage, Twilio) — that's the one piece of this
project that can't be purely local. So this tool defaults to SAFE: it logs
what it would have sent and returns that to Evelyn/you, and only ever
sends for real if you explicitly set EVELYN_ALLOW_SEND=true in .env *and*
have wired send_text() below to something real.

To make it real, pick one:
- macOS + iMessage: shell out to `osascript` against Messages.app.
- Twilio (SMS, any phone): a few lines with the `twilio` package.
- A self-hosted bridge (e.g. matrix/signal bridges) if you want it fully
  outside big-tech infra too.
"""

from __future__ import annotations

import os

SPEC = [
    {
        "name": "send_text",
        "description": (
            "Send a text message to a contact. By default this is a dry "
            "run — it will NOT actually send anything until the user has "
            "explicitly configured a real send path."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "contact": {"type": "string", "description": "Who to text, e.g. 'wife'."},
                "message": {"type": "string"},
            },
            "required": ["contact", "message"],
        },
    }
]


def _send_for_real(contact: str, message: str) -> str:
    """Wire this up to an actual provider once you trust it. Left
    unimplemented on purpose — see module docstring."""
    raise NotImplementedError(
        "EVELYN_ALLOW_SEND is true but send_text() has no real provider "
        "wired up yet. Implement _send_for_real() in message_tool.py."
    )


def handle(name: str, tool_input: dict) -> str:
    if name != "send_text":
        raise ValueError(f"message_tool cannot handle {name!r}")

    contact = tool_input["contact"]
    message = tool_input["message"]
    allow_send = os.getenv("EVELYN_ALLOW_SEND", "false").strip().lower() == "true"

    if not allow_send:
        return (
            f"[DRY RUN — EVELYN_ALLOW_SEND is off] Would text {contact!r}: "
            f"{message!r}. No message was actually sent."
        )

    _send_for_real(contact, message)
    return f"Sent to {contact}: {message!r}"
