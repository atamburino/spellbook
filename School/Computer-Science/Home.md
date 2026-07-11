# Master's in Computer Science

This section is for class notes, assignment patterns, and deterministic document generation for the master's program.

## Structure

- [Classes](Classes/README.md): one page per class, with links to notes and recurring assignments.
- [Journals](Journals/README.md): draft journals in Markdown, then generate formatted Word documents.
- [Templates](Templates/journal-template.md): reusable draft templates.
- [Scripts](scripts/README.md): document generation tools.

## Journal Workflow

1. Create a new draft from the template.
2. Write the journal in Markdown.
3. Run the journal builder.
4. Submit the generated `.docx`.

```powershell
python School\Computer-Science\scripts\new_journal.py `
  --assignment "Module Five Activity" `
  --title "Semaphore Synchronization and Deadlock Prevention"

python School\Computer-Science\scripts\build_journal.py `
  School\Computer-Science\Journals\drafts\module-five-activity.md
```

## Formatting Target

The journal generator is based on the provided sample document:

- US Letter page size
- 1-inch margins
- Times New Roman
- 12 pt body text
- Double-spaced paragraphs
- Centered assignment/date opening block
- Centered bold section headings
- References section at the end when included
