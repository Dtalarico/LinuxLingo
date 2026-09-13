# LinuxLingo
Duolingo-style Linux terminal trainer for building real command-line fluency through hands-on drills, repetition, and scenario-based practice.

## Overview

LinuxLingo is a terminal-first Linux learning project designed to build actual command-line fluency through active recall, repetition, and hands-on practice.

The core idea is simple:

**Linux should be learned like a language.**

- Commands are vocabulary.
- Flags are grammar.
- Pipelines are sentence structure.
- Real terminal tasks are conversation.

Instead of relying primarily on lectures, videos, or command recognition, LinuxLingo trains the learner to translate a real problem into the correct command and execute it.

**problem → reasoning → command → execution → verification**

---

## Project Goal

LinuxLingo aims to move learners from:

> “I recognize that command.”

to:

> “I know what to type, why I am typing it, and what result I expect.”

The emphasis is on developing terminal reflexes and practical confidence rather than memorizing isolated facts.

---

## MVP

The initial LinuxLingo MVP is a Python command-line application.

The MVP currently:

- loads drills from a separate JSON bank
- presents Linux command drills
- accepts typed command responses
- uses real-world scenarios
- provides immediate pass/fail feedback and explanations
- tracks a basic session score
- normalizes whitespace for answer comparison
- keeps program logic separate from training content

The current safe MVP does not execute arbitrary learner-entered commands. Rich state validation, adaptive selection, mastery tracking, and persistent learner data remain future work.

---

## Core Architecture

LinuxLingo separates the training engine from the training data.

### `linuxlingo.py`

Contains the Python CLI engine and program logic.

### `scenario_bank.json`

Contains the growing command and scenario bank, including:

- drill IDs
- question types
- difficulty levels
- categories and tags
- prompts
- valid answers
- explanations
- source provenance
- validation metadata where appropriate

This separation allows the command bank to grow without requiring the core Python engine to be constantly rewritten.

### `PROJECT_CONTINUITY.md`

Maintains the current development state of the project so work can continue cleanly across development sessions and fresh AI-assisted work sessions.

### `LINUXLINGO_MASTER_SPEC.md`

Contains the canonical project architecture, learning philosophy, tier structure, design decisions, and long-term development doctrine.

---

## Learning Model

LinuxLingo is built around several principles:

### Active Recall

The learner must produce commands from memory rather than simply recognize them.

### Command Production

Exercises ask the learner to solve an actual terminal problem.

Example:

> Create a directory named `projects`.

Expected command:

`mkdir projects`

### Scenario-Based Practice

Commands are taught in realistic contexts instead of as disconnected vocabulary.

### Error Correction

Learners diagnose broken commands, incorrect flags, syntax errors, path mistakes, and common terminal failures.

### Verification

The long-term model is not merely command recall. Learners should know how to confirm that a command actually produced the intended state.

### Progressive Difficulty

Training begins with foundational commands and gradually progresses toward:

- flags and arguments
- pipelines
- command chaining
- troubleshooting
- system administration
- multi-step fluency missions

---

## Planned Training Areas

LinuxLingo will progressively cover areas such as:

- navigation
- files and directories
- viewing and manipulating text
- search tools
- pipes and redirection
- permissions
- users and groups
- process management
- system information
- package management
- networking
- storage
- services
- archiving and compression
- containers
- shell scripting
- troubleshooting

---

## Command Bank Development

The command bank is intended to grow from real Linux usage.

Commands encountered during coursework, labs, system administration practice, troubleshooting, and certification study are converted into LinuxLingo drills with source provenance.

Preferred workflow:

**LAB → LEARN → HARVEST → COMMIT → MOVE ON**

The long-term value of the project depends heavily on building a large, structured, high-quality training corpus rather than merely creating a large application.

As of September 13, 2026, the bank contains **100 drills (LL001–LL100)**. Recent harvests include filesystem/navigation work, Vim, wildcards, text processing, AWK, shell history, identity/context commands, time-based `find` searches, relative-vs-absolute path troubleshooting, and Docker image/container operations.

---

## Development Strategy

Current development order:

1. Preserve the terminal-first Python/JSON architecture.
2. Continue harvesting real coursework and lab material after each learning unit.
3. Preserve source provenance and useful troubleshooting context.
4. Improve answer validation beyond normalized exact matching.
5. Add performance persistence, mistake review, and mastery/coverage tracking.
6. Add adaptive drill selection and delayed retesting.
7. Introduce safe state-based validation.
8. Add advanced multi-step scenarios and troubleshooting drills.
9. Expand interfaces only after the terminal-first learning engine is stable.

---

## Future Vision

Possible future LinuxLingo features include:

- adaptive practice
- mastery tracking
- mistake review
- spaced repetition
- streak mechanics
- configurable practice sessions
- certification-focused command packs
- RHCSA-aligned training
- sandboxed Linux environments
- automated system-state validation
- container-based labs
- web or desktop interfaces

These are future layers.

The immediate priority is building a strong terminal-first Linux fluency engine and a high-quality command bank.

---

## Project Status

**Current Phase:** Active MVP and command-bank development.

**Current corpus:** 100 drills, LL001–LL100.

LinuxLingo is under active development, with GitHub serving as the active source of truth.

---

## Author

**David Michael Talarico**

Cloud Infrastructure student focused on Linux, systems administration, cloud computing, networking, and virtualization.
