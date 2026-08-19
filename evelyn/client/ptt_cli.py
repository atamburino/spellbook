"""Push-to-talk CLI client — the MVP front-end for Evelyn.

Deliberately text-in/text-out, no microphone, no wake word. That's not
laziness: the point of an MVP is to prove the brain (memory + tools + the
agent loop) is actually good before spending time on voice I/O, wake-word
detection, or a wearable. Once this feels right, this file is exactly
where a Whisper-transcribed mic input and a TTS-spoken output slot in —
everything above the "type a line, get a line back" boundary stays the
same.

Run: python -m client.ptt_cli
"""

from __future__ import annotations

from rich.console import Console
from rich.prompt import Prompt

from brain.agent import Evelyn

console = Console()


def main() -> None:
    console.print("[bold cyan]Evelyn[/] is listening. Type a message, or 'quit' to stop.\n")
    evelyn = Evelyn()

    while True:
        try:
            user_text = Prompt.ask("[bold green]you[/]")
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]bye.[/]")
            break

        if user_text.strip().lower() in {"quit", "exit"}:
            console.print("[dim]bye.[/]")
            break
        if not user_text.strip():
            continue

        reply = evelyn.respond(user_text)
        console.print(f"[bold cyan]evelyn[/]: {reply}\n")


if __name__ == "__main__":
    main()
