# Scripts

These scripts generate deterministic school documents from Markdown drafts.

## Create A Weekly Workspace

From the repository root, run the interactive shortcut:

```powershell
.\newweek
```

Press Enter to accept the default course and suggested next week. The shortcut automatically uses either the `py` launcher or `python`, depending on what is installed.

To create a week without prompts, pass every value explicitly:

```powershell
.\newweek `
  --course CS-530 `
  --week 2 `
  --title "Intelligent Agents" `
  --assignment "Module Two Journal"
```

This creates one self-contained folder under `Notes/<course>/Week-##/` with:

- `README.md`: the week's objective, checklist, assignment, retrieval questions, and recap
- `findings.md`: the topic index and confidence tracker
- `findings/`: initially empty; add small notes only when a concept needs more room
- `sources/`: PDFs and other source material
- `journal.md`: the submission draft, ready for `build_journal.py`

The command refuses to overwrite an existing week.

## Requirements

- Python 3.10 or newer
- `python-docx`

Install the dependency if your Python environment does not already have it:

```powershell
python -m pip install python-docx
```

## Create A Draft

```powershell
python School\Computer-Science\scripts\new_journal.py `
  --assignment "Module Five Activity" `
  --title "Semaphore Synchronization and Deadlock Prevention"
```

## Build A DOCX

```powershell
python School\Computer-Science\scripts\build_journal.py `
  School\Computer-Science\Journals\drafts\example-journal.md
```

The builder intentionally matches the provided journal sample:

- Letter page
- 1-inch margins
- Times New Roman 12 pt
- Double spacing
- Centered title block
- Centered bold section headings
