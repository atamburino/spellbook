"""The agent loop: this is Evelyn's brain.

The pattern is the standard Claude tool-use loop — send the conversation
plus a list of tools, and if Claude wants to call one, run it locally and
feed the result back, repeating until Claude replies with plain text. That
loop is the whole trick behind "AI that can do things," not just "AI that
can talk."

This module knows nothing about voice, wearables, or any particular
client — client/ptt_cli.py (or a future phone/watch client) just calls
Evelyn.respond(text) and gets text back. Swap the client without touching
this file, or swap the model/tools without touching the client.
"""

from __future__ import annotations

import os

from anthropic import Anthropic
from dotenv import load_dotenv

from brain.memory import Memory
from brain.tools import registry

load_dotenv()

SYSTEM_PROMPT = """\
You are Evelyn, the user's personal AI assistant. You are direct, warm, \
and competent — closer to a sharp chief-of-staff than a customer service \
bot. Keep replies conversational and short by default; this is a voice \
assistant, not a chat window, so avoid long lists or markdown unless the \
user is clearly looking at a screen.

You have tools for memory (remembering facts, recalling past \
conversation), a local calendar, and sending texts. Use them proactively: \
if the user tells you something worth remembering, remember it without \
being asked. If they ask what you just talked about, use recall before \
answering. Always confirm before sending a text or booking an event if \
any detail is ambiguous.
"""


class Evelyn:
    def __init__(self, memory: Memory | None = None):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Copy .env.example to .env "
                "and fill it in."
            )
        self.client = Anthropic(api_key=api_key)
        self.model = os.getenv("EVELYN_MODEL", "claude-sonnet-5")
        self.memory = memory or Memory()
        self.messages: list[dict] = []

    def respond(self, user_text: str) -> str:
        self.memory.log_turn("user", user_text)
        self.messages.append({"role": "user", "content": user_text})

        # Tool-use loop: keep going until Claude stops asking for tools.
        while True:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                tools=registry.all_specs(),
                messages=self.messages,
            )
            self.messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason != "tool_use":
                final_text = "".join(
                    block.text for block in response.content if block.type == "text"
                )
                self.memory.log_turn("evelyn", final_text)
                return final_text

            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                result = registry.dispatch(block.name, block.input, self.memory)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )
            self.messages.append({"role": "user", "content": tool_results})
