# Scripts

These scripts support the weekly learning workspace.

## Create a Weekly Workspace

From the repository root, run:

```powershell
.\newweek
```

Press Enter to accept the default course and suggested next week. To create a week without prompts, pass every value explicitly:

```powershell
.\newweek `
  --course CS-530 `
  --week 2 `
  --title "Intelligent Agents" `
  --assignment "Module Two Journal"
```

This creates one folder under `Notes/<course>/Week-##/` containing the weekly overview, findings index, expanded findings, sources, and a Markdown journal draft. The command refuses to overwrite an existing week.

## Requirement

- Python 3.10 or newer
