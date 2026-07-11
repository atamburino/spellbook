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

## Weekly Learning Workflow

Keep each week's learning and deliverable together. Generate the workspace, work from its `README.md`, and use `findings.md` as the only index you need to maintain.

```powershell
.\newweek
```

Answer the short prompts; pressing Enter accepts the suggested course and next week. The shortcut automatically uses either `py` or `python`, depending on what is installed. Command-line flags remain available when you want to skip the prompts.

The workflow is intentionally small: preview, pick the few ideas that matter, explain them using plain English plus a familiar analogy, retrieve them from memory, then write the assignment. Reading every page is not the default goal; being able to explain and apply the week's objectives is.

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
