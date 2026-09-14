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

- loads drills from JSON scenario banks
- presents Linux command drills
- accepts typed command responses
- uses real-world scenarios
- provides immediate pass/fail feedback and explanations
- tracks a basic session score
- normalizes whitespace for answer comparison
- keeps program logic separate from training content
- validates duplicate drill IDs across configured banks

The current safe MVP does not execute arbitrary learner-entered commands. Rich state validation, adaptive selection, mastery tracking, and persistent learner data remain future work.

---

## Core Architecture

### `linuxlingo.py`
Contains the Python CLI engine and program logic. It currently loads the main bank plus a supplemental harvest bank.

### `scenario_bank.json`
Contains the original canonical corpus through LL100.

### `scenario_bank_additions.json`
Contains newly harvested coursework drills beginning with LL101. This keeps new harvests usable immediately while preserving the existing main bank intact; later consolidation remains possible.

### `PROJECT_CONTINUITY.md`
Maintains the current development state so work can continue cleanly across sessions.

### `LINUXLINGO_MASTER_SPEC.md`
Contains the canonical project architecture, learning philosophy, tier structure, design decisions, and long-term development doctrine.

---

## Learning Model

LinuxLingo is built around active recall, command production, scenario-based practice, error correction, verification, progressive difficulty, and practical self-rescue.

A key design principle is the distinction between:

- **retrieval failure** — a learner was taught something but cannot recall or apply it
- **coverage failure** — a course or assessment demands syntax or concepts that were not actually taught or scaffolded

The system should not treat those as the same failure.

---

## Command Bank Development

The command bank grows from real Linux usage: coursework, labs, system administration practice, troubleshooting, and certification study.

Preferred workflow:

**LAB → LEARN → HARVEST → COMMIT → MOVE ON**

As of September 14, 2026, LinuxLingo loads **115 drills (LL001–LL115)**.

Recent harvests include:

- filesystem and navigation
- Vim and shell history
- wildcards and quoting
- text processing and AWK
- `find` predicates and `-exec`
- `locate`, `updatedb`, and `locate -S`
- `whereis` and `which`
- Docker image/container operations

The September 14 Cengage work also reinforced an important product-design lesson: training should accept valid Linux solutions where appropriate rather than teaching learners to guess a brittle autograder's preferred command string.

---

## Development Strategy

1. Preserve the terminal-first Python/JSON architecture.
2. Continue harvesting real coursework and lab material after each learning unit.
3. Preserve source provenance and troubleshooting context.
4. Improve answer validation beyond normalized exact matching.
5. Add performance persistence, mistake review, and mastery/coverage tracking.
6. Add adaptive drill selection and delayed retesting.
7. Introduce safe state-based validation.
8. Add advanced multi-step scenarios and troubleshooting drills.
9. Consolidate supplemental harvest banks when useful without losing provenance.

---

## Future Vision

Possible future LinuxLingo features include adaptive practice, mastery tracking, mistake review, spaced repetition, streak mechanics, certification-focused packs, RHCSA-aligned training, sandboxed Linux environments, automated system-state validation, container-based labs, and later web or desktop interfaces.

The immediate priority remains building a strong terminal-first Linux fluency engine and a high-quality command corpus.

---

## Project Status

**Current Phase:** Active MVP and command-bank development.

**Current loaded corpus:** 115 drills, LL001–LL115.

GitHub is the active source of truth.

---

## Author

**David Michael Talarico**

Cloud Infrastructure student focused on Linux, systems administration, cloud computing, networking, and virtualization.
