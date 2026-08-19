"""Aggregates every tool module into one spec list + dispatcher, so
agent.py doesn't need to know how many tools exist or how each is
implemented — it just calls all_specs() and dispatch().

Adding a new tool = write a new module with SPEC + handle(), then add it
to _MODULES below.
"""

from __future__ import annotations

from brain.memory import Memory
from brain.tools import calendar_tool, memory_tool, message_tool

# Order here is just presentation order to the model — doesn't matter.
_MODULES = [memory_tool, calendar_tool, message_tool]

# Which tool names live in which module, so dispatch() knows where to send
# a call without every module needing to guess whether it owns a name.
_OWNER = {
    tool["name"]: module
    for module in _MODULES
    for tool in module.SPEC
}


def all_specs() -> list[dict]:
    return [tool for module in _MODULES for tool in module.SPEC]


def dispatch(name: str, tool_input: dict, memory: Memory) -> str:
    module = _OWNER.get(name)
    if module is None:
        return f"Unknown tool: {name!r}"

    if module is memory_tool:
        return memory_tool.handle(name, tool_input, memory)
    if module is message_tool:
        return message_tool.handle(name, tool_input)
    if module is calendar_tool:
        return calendar_tool.handle(name, tool_input)

    raise AssertionError(f"registry.py doesn't know how to call {module}")
