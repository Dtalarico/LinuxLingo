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
1. Continue expanding `scenario_bank.json` with real Linux commands and scenarios.
2. Refactor `linuxlingo.py` so drills load from `scenario_bank.json` instead of remaining hard-coded.
3. Preserve the current schema unless a deliberate architecture change is made.
4. Continue adding adaptive tutoring behavior gradually after the MVP data-loading flow works.
5. Continue building toward multi-question and multi-step Linux sessions later.

---

## Working Rules
- Work one step at a time during implementation.
- Do not unnecessarily redesign working architecture.
- Preserve separation between code and data.
- Prefer real-world command scenarios over trivia.
- Keep the repository structure lean.
- Update this file at the end of every substantial work session.
- When starting a new ChatGPT conversation, provide this file first so the assistant can recover project state.
- After reading this file, the assistant should ask only for the current project files needed for the requested task.

---

## Fresh-Session File Request Protocol

After reading `PROJECT_CONTINUITY.md`, a fresh ChatGPT instance should determine which current files are needed before continuing.

Ask for files based on the task:

### If working on the Python engine
Request:
- `linuxlingo.py`
- `scenario_bank.json`

### If working on the command or drill bank
Request:
- `scenario_bank.json`

Request `LINUXLINGO_MASTER_SPEC.md` only if the task depends on architecture, schema, tiering, or learning-design rules.

### If changing architecture or project doctrine
Request:
- `LINUXLINGO_MASTER_SPEC.md`

Also request:
- `linuxlingo.py`
- `scenario_bank.json`

if the proposed architecture change affects current implementation or data structure.

### If updating public project documentation
Request:
- `README.md`

Also request other files only if needed to verify current implementation or project state.

### If only discussing next steps
`PROJECT_CONTINUITY.md` may be sufficient by itself.

Do not ask for every project file automatically.

Always inspect the current authoritative file before changing it.

---

## Session Update Format
At the end of each substantial work session, update:

### Completed
- Created and committed `LINUXLINGO_MASTER_SPEC.md`
- Created and committed `linuxlingo.py`
- Created and committed `scenario_bank.json`
- Seeded the initial scenario bank with MVP drills and real Linux coursework/practice commands

### Changed
- Adaptive tutoring concepts are now part of the master specification.
- Future multi-question and multi-step Linux sessions are part of the long-term architecture.
- MVP remains intentionally simple and terminal-first.
- `scenario_bank.json` is the authoritative training-data file.
- `linuxlingo.py` is the authoritative engine file.

### Current State
- GitHub repository structure is established.
- All five canonical project files now exist.
- Initial Python MVP exists.
- Initial JSON command/scenario bank exists.
- Python still contains hard-coded drills and has not yet been refactored to load the JSON bank.

### Next Exact Task
Refactor `linuxlingo.py` so it loads drills from `scenario_bank.json`.
