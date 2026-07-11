---
assignment: Module Five Activity
date: May 23, 2026
author: Andy Tamburino
course: CS 000
title: Semaphore Synchronization and Deadlock Prevention
subtitle: Semaphores and Concurrent Access
output: ../generated/example-journal.docx
---

Synchronization tools use counters to control access to shared resources. A semaphore decreases the counter when a thread enters a controlled section and increases the counter when the thread exits. This makes it possible to coordinate concurrent work while protecting shared state.

## Instructions on How to Run the Program

Complete instructions for running the program are included in the README file submitted with the project. The README should include platform-specific commands, required dependencies, and expected output.

## Deadlock Prevention

Deadlock occurs when one or more processes cannot continue because they are waiting for resources that will never become available. Common deadlock conditions include mutual exclusion, hold and wait, no preemption, and circular wait.

## How the Semaphore Prevents Deadlock

The semaphore prevents deadlock by limiting the number of threads that can enter the controlled section at the same time. This keeps resource access predictable and prevents competing threads from holding partial access indefinitely.

## Challenges

The most significant challenge was maintaining readable output while threads executed in an unpredictable sequence. Consistent formatting and explicit synchronization helped keep the program behavior easier to inspect.

## References

Module Five resources. Process synchronization and deadlocks.
