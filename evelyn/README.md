# Evelyn

A local-first personal AI assistant "brain" — the JARVIS/EDITH-shaped
project. This is the MVP: a persistent agent loop with tool-calling and
memory you own, driven from a push-to-talk CLI. No wake word, no
wearable, no cloud memory yet — those come once this core loop earns its
keep.

## Why this shape

The fictional version is instant and omniscient; the real version is a
network round-trip and a database. What's actually achievable today:

- **The brain** is a standard Claude tool-use loop (`brain/agent.py`):
  send the conversation + a list of tools, run whatever tool Claude asks
  for, feed the result back, repeat until it has a plain-text answer.
- **Memory** (`brain/memory.py`) is a single SQLite file in `data/`,
  never committed, never leaving your machine. Two tables: durable facts
  ("wife's name" → "Sam") and a full conversation log for "what did we
  just talk about" style recall.
- **Tools** (`brain/tools/`) are small, independent modules — memory,
  a local `.ics` calendar, and a text-message stub. Adding a new one
  means adding a new module and one line in `registry.py`; nothing else
  needs to change.
- **The client** (`client/ptt_cli.py`) is deliberately just a
  type-a-line-get-a-line-back terminal loop. It's the thinnest possible
  front-end on purpose, so voice I/O and a wearable can be swapped in
  later without touching the brain at all.

## Setup

```bash
cd evelyn
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # then fill in ANTHROPIC_API_KEY
```

## Run it

```bash
python -m client.ptt_cli
```

Try things like:
- "Remember that my wife's name is Sam."
- "What's on my calendar?" / "Book a dentist appointment tomorrow at 3pm."
- "What did we just talk about?"
- "Text my wife I'm running 10 minutes late." (dry-run by default — see below)

## Test

```bash
pytest
```

## Safety notes

- **Calendar** is a local `.ics` file (`data/calendar.ics`) — nothing
  leaves your machine. It's a real calendar format, so any app can
  import/subscribe to it later.
- **Texting** (`brain/tools/message_tool.py`) is a dry-run stub by
  default: it will tell you what it *would* send, and never actually
  sends anything unless you set `EVELYN_ALLOW_SEND=true` in `.env` *and*
  implement `_send_for_real()` with a provider you trust (iMessage via
  `osascript`, Twilio, a Signal/Matrix bridge, etc.).
- `data/` and `.env` are gitignored. Nothing personal should ever land in
  this repo.

## Roadmap

This MVP proves the brain (memory + tools + agent loop) works before
spending effort on voice or hardware. Rough order:

1. **✅ MVP** — this: push-to-talk CLI, local memory, local calendar,
   dry-run texting.
2. **Voice I/O** — swap the CLI's `input()`/`print()` for local Whisper
   (speech-to-text) and a TTS engine (ElevenLabs for quality, or Piper
   for fully local). The brain doesn't change.
3. **Wake word** — Porcupine ("Hey Evelyn") for always-listening on a
   phone or small device, instead of push-to-talk.
4. **Real integrations** — swap the local `.ics` calendar for Google
   Calendar/EventKit, wire up real texting, add more tools (home
   automation, notes, email) via the same `registry.py` pattern. MCP
   servers are worth checking here before hand-rolling — a lot of these
   integrations already exist as MCP tools.
5. **A real client** — a phone app or Apple Watch complication that
   streams audio to wherever the brain is running (a home server is
   simplest: keeps memory fully local while any device can be a mic).
6. **Wearable** — once the software's solid, look at DIY open-source
   pendants/glasses (e.g. the Friend/OpenGlass projects) or build a
   minimal ESP32 mic client that talks to the same brain server.
