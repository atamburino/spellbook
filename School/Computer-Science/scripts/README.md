# Scripts

These scripts generate deterministic school documents from Markdown drafts.

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
