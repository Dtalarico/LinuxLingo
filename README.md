# LinuxLingo
Duolingo-stule Linux terminal trainer for building real command line fluency through hands-on drills. repetition, and scenario-based practice.

## Overview

LinuxLingo is a terminal-first Linux learning project designed to build actual command-line fluency through active recall, repetition, and hands-on practice.

The core idea is simple:

**Linux should be learned like a language.**

- Commands are vocabulary.
- Flags are grammar.
- Pipelines are sentence structure.
- Real terminal tasks are conversation.

Instead of relying primarily on lectures, videos, or command recognition, LinuxLingo trains the learner to translate a real problem into the correct command and execute it.

**problem → command → execution**

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

The MVP will:

- present Linux command drills
- accept typed command responses
- use real-world scenarios
- provide feedback
- track performance
- draw training data from a separate JSON drill bank
- progressively expand from basic commands to multi-command tasks

The project intentionally begins as a small terminal application before expanding into more complex interfaces.

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
- validation information where appropriate

This separation allows the command bank to grow without requiring the core Python engine to be constantly rewritten.

### `PROJECT_CONTINUITY.md`

Maintains the current development state of the project so work can continue cleanly across development sessions and fresh AI-assisted work sessions.

### `LINUXLINGO_MASTER_SPEC.md`

Will contain the canonical project architecture, learning philosophy, tier structure, design decisions, and long-term development doctrine.

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

Learners will eventually diagnose broken commands, incorrect flags, syntax errors, and common terminal mistakes.

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
- shell scripting
- troubleshooting

---

## Command Bank Development

The command bank is intended to grow from real Linux usage.

Commands encountered during coursework, labs, system administration practice, troubleshooting, and certification study can be converted into LinuxLingo drills.

The long-term value of the project depends heavily on building a large, structured, high-quality training corpus rather than merely creating a large application.

---

## Development Strategy

Current development order:

1. Establish the GitHub repository and project structure.
2. Preserve and refine the existing Python MVP.
3. Create the initial `scenario_bank.json`.
4. Begin building the real command and scenario bank.
5. Consolidate earlier design work into `LINUXLINGO_MASTER_SPEC.md`.
6. Improve question handling and validation.
7. Add performance tracking and mastery systems.
8. Add advanced scenario and troubleshooting drills.
9. Expand only after the terminal-first MVP is stable.

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
- web or desktop interfaces

These are future layers.

The immediate priority is building a strong terminal-first Linux fluency engine and a high-quality command bank.

---

## Project Status

**Current Phase:** Initial MVP build and command-bank development.

LinuxLingo is under active development.

---

## Author

**David Michael Talarico**

Cloud Infrastructure student focused on Linux, systems administration, cloud computing, networking, and virtualization.
