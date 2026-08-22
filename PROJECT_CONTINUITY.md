# LinuxLingo Project Continuity

## Purpose
This file is the operational handoff document for LinuxLingo.

Its job is to let a fresh ChatGPT instance quickly recover the current project state without needing the full conversation history.

This file must be updated at the end of every substantial LinuxLingo work session.

---

## Current Project State
- Project: LinuxLingo
- Repository: GitHub
- Development phase: Initial build / repository setup
- Current workflow: GitHub web interface
- Older concept and design documents have been moved into an Archive folder in Google Drive.
- Active development now continues from the current GitHub repository.

---

## Canonical Project Files
- README.md
- PROJECT_CONTINUITY.md
- LINUXLINGO_MASTER_SPEC.md
- linuxlingo.py
- scenario_bank.json

---

## File Responsibilities

### README.md
Public-facing project overview.

### PROJECT_CONTINUITY.md
Tracks:
- current project state
- recent decisions
- what was completed
- what is in progress
- next exact task

This file should stay concise.

### LINUXLINGO_MASTER_SPEC.md
Canonical architecture, learning philosophy, tier structure, design decisions, and long-term project doctrine.

### linuxlingo.py
Python CLI engine and program logic.

### scenario_bank.json
Canonical command and drill bank.

All commands, drills, scenarios, answers, tags, explanations, difficulty levels, and related training data belong here.

The growing command bank should NOT be duplicated inside this continuity file.

---

## Current Architecture Decisions
- LinuxLingo is a terminal-first Linux command fluency trainer.
- The MVP is a Python CLI application.
- Program logic stays separate from training data.
- `linuxlingo.py` contains engine logic.
- `scenario_bank.json` contains the growing drill bank.
- Real Linux commands used in coursework, labs, and practice should be harvested into the command bank.
- Avoid unnecessary extra project files.
- GitHub is the active source of truth for development.
- Google Drive is used for archived design material and reference documents.
- GitHub web interface will be used for now.
- GitHub Desktop and command-line Git can be introduced later.

---

## Learning Design
LinuxLingo trains command-line fluency through:
- active recall
- command production
- repetition
- scenario-based drills
- error correction
- progressive difficulty
- eventual multi-command fluency missions

Core model:

problem → command → execution

Commands are vocabulary.  
Flags are grammar.  
Pipelines are sentence structure.

---

## Command Bank Continuity
- Canonical bank file: `scenario_bank.json`
- New commands and drills are added there.
- This continuity file should record only:
  - bank status
  - naming conventions
  - category decisions
  - structural changes
  - next bank-development task

Do not maintain a duplicate command list here.

---

## Current Development Priorities
1. Complete the GitHub repository structure.
2. Preserve and add the existing Python MVP.
3. Create `scenario_bank.json`.
4. Seed the bank with real commands already used in Linux coursework and practice.
5. Consolidate older design material into `LINUXLINGO_MASTER_SPEC.md`.
6. Continue expanding the command bank over time.

---

## Working Rules
- Work one step at a time during implementation.
- Do not unnecessarily redesign working architecture.
- Preserve separation between code and data.
- Prefer real-world command scenarios over trivia.
- Keep the repository structure lean.
- Update this file at the end of every substantial work session.
- When starting a new ChatGPT conversation, provide this file first so the assistant can recover project state.

---

## Session Update Format
At the end of each substantial work session, update:

### Completed
- What was finished

### Changed
- Architecture or design decisions made

### Current State
- What is working now

### Next Exact Task
- The single next development action

---

## Current Next Exact Task
Finish repository setup and create the remaining canonical files.
