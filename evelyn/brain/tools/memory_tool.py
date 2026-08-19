"""The memory tool: lets Evelyn remember durable facts and recall past
conversation. This is what makes "what did we just talk about?" work, and
what lets facts like "my wife's name is X" persist across sessions instead
of being re-explained every time.
"""

from __future__ import annotations

from brain.memory import Memory

SPEC = [
    {
        "name": "remember_fact",
        "description": (
            "Store or update a durable fact about the user for future "
            "conversations, e.g. key='wife's name', value='Sam'. "
            "Use this whenever the user tells you something worth "
            "remembering long-term, not just for this conversation."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Short label for the fact."},
                "value": {"type": "string", "description": "The fact itself."},
            },
            "required": ["key", "value"],
        },
    },
    {
        "name": "recall_conversation",
        "description": (
            "Search recent conversation history and stored facts for "
            "context. Use this to answer questions like 'what did we just "
            "talk about' or to check whether you already know something "
            "about the user before asking them again."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "What to search for. Leave empty (or use a generic "
                        "word like 'recent') to just get the last several turns."
                    ),
                }
            },
            "required": ["query"],
        },
    },
]


def handle(name: str, tool_input: dict, memory: Memory) -> str:
    if name == "remember_fact":
        memory.remember_fact(tool_input["key"], tool_input["value"])
        return f"Remembered: {tool_input['key']} = {tool_input['value']}"

    if name == "recall_conversation":
        query = tool_input.get("query", "")
        turns = memory.recall(query) if query else memory.recent_turns()
        facts = memory.all_facts()

        lines = []
        if facts:
            lines.append("Known facts:")
            lines.extend(f"- {k}: {v}" for k, v in facts.items())
        if turns:
            lines.append("Relevant conversation:")
            lines.extend(f"- [{t.created_at}] {t.role}: {t.content}" for t in turns)
        return "\n".join(lines) if lines else "Nothing found in memory yet."

    raise ValueError(f"memory_tool cannot handle {name!r}")
