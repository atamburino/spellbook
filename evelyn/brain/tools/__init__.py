"""Tools Evelyn can call. Each module exposes:

- SPEC: the Anthropic tool-use JSON schema for the tool(s) it defines.
- handle(name, input, memory): executes a tool call and returns a string
  result to hand back to the model.

agent.py aggregates SPECs and dispatches handle() by tool name — see
brain/tools/registry.py.
"""
