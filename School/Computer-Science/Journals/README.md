# Journals

Write journal drafts in `drafts/` using Markdown plus a small metadata block. Generated Word documents go in `generated/`.

## Build A Journal

```powershell
python School\Computer-Science\scripts\build_journal.py `
  School\Computer-Science\Journals\drafts\example-journal.md
```

## Create A New Draft

```powershell
python School\Computer-Science\scripts\new_journal.py `
  --assignment "Module Five Activity" `
  --title "Semaphore Synchronization and Deadlock Prevention"
```

## Draft Format

```md
---
assignment: Module Five Activity
date: May 23, 2026
author: Andy Tamburino
course: CS 000
title: Semaphore Synchronization and Deadlock Prevention
subtitle: Semaphores and Concurrent Access
output: ../generated/module-five-activity-tamburino.docx
---

Opening paragraph goes here.

## Instructions on How to Run the Program

Body paragraph goes here.

## References

Reference entry goes here.
```
