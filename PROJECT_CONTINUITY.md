# LinuxLingo Project Continuity

## Purpose
This file is the operational handoff document for LinuxLingo. It lets a fresh development or AI-assisted session recover the current state without needing the full conversation history.

Update this file after every substantial LinuxLingo work session.

---

## Current Project State
- Project: LinuxLingo
- Repository: GitHub (`Dtalarico/LinuxLingo`)
- Development model: terminal-first Python MVP
- GitHub is the active source of truth.
- Older concept/design documents remain archived reference material in Google Drive.
- `scenario_bank.json` is the authoritative training corpus.
- `linuxlingo.py` now loads drills from `scenario_bank.json`; the original five hard-coded drills have been removed from the engine.

---

## Canonical Project Files
- `README.md`
- `PROJECT_CONTINUITY.md`
- `LINUXLINGO_MASTER_SPEC.md`
- `linuxlingo.py`
- `scenario_bank.json`

`.gitignore` is repository infrastructure rather than a canonical design/data document.

---

## Architecture

### `linuxlingo.py`
Python CLI engine. Program behavior belongs here.

### `scenario_bank.json`
Canonical drill/training bank. Commands, prompts, valid answers, tags, explanations, source provenance, difficulty, and validation metadata belong here.

### `LINUXLINGO_MASTER_SPEC.md`
Canonical architecture, learning philosophy, training model, and long-term doctrine.

### `README.md`
Public-facing project overview.

### `PROJECT_CONTINUITY.md`
Operational state, recent decisions, completed work, and next exact task. Keep it concise; do not duplicate the drill bank here.

---

## Learning Doctrine
LinuxLingo treats Linux as a language:

- commands = vocabulary
- flags/options = grammar
- pipelines/chaining = sentence structure
- real terminal tasks = conversation

Core progression:

**problem → reasoning → command → execution → verification**

The learner should move from recognition to independent production and eventually to multi-step operational fluency.

---

## Adaptive Tutoring Relationship
LinuxLingo is the CLI practice/retrieval layer of a larger learning workflow.

Current learning pipeline:

**SOURCE CONTENT → INGESTION → ADAPTIVE TEACHING → LINUXLINGO RETRIEVAL/PRACTICE**

The adaptive tutoring method should teach concepts before LinuxLingo treats them as expected independent recall. LinuxLingo then provides repeated command production, varied scenarios, delayed retrieval, error repair, and eventually mastery tracking.

Important distinction:

1. **Retrieval failure:** the learner was taught the concept but cannot independently retrieve/apply it.
2. **Coverage failure:** the source/course/lab asks for a command or concept that the learner has not actually been introduced to.

These are different failures and should not be scored or remediated identically. A future mastery system should track source exposure/coverage separately from retrieval performance.

---

## Source Ingestion Doctrine
The largest scaling bottleneck is no longer merely writing quiz logic; it is converting trustworthy Linux source material into structured training data efficiently and accurately.

Potential sources include:
- coursework and labs
- Linux Essentials / LPIC material
- RHCSA study material
- real administration tasks
- troubleshooting sessions
- authoritative command documentation

Ingestion should preserve provenance. Drills should record enough source information to determine what material introduced the concept and to distinguish taught material from unsupported assessment demands.

Do not blindly convert every quiz fact into a command drill. Prefer material that contributes to command-line fluency, operational reasoning, self-rescue, or required exam recall.

---

## Current Bank State
- `scenario_bank.json` contains 42 drills: LL001–LL042.
- Bank is human-readable / pretty formatted.
- Week 2 NOS-120 material is represented.
- Some quiz-derived recognition items remain and may later be reviewed for value.
- Recent coursework has introduced additional filesystem/navigation material (wildcards/globbing, Vim fundamentals, paths, copying/moving/removing, brace expansion, command discovery) that has not yet been harvested into the bank.

---

## Engine State
Completed on 2026-09-04:
- Removed the five hard-coded drill objects from `linuxlingo.py`.
- Engine now loads the authoritative JSON bank at startup.
- Engine validates the top-level bank shape and required drill fields.
- Engine accepts all bank question types through a common prompt/answer loop.
- Basic whitespace normalization is used for answer comparison.
- Feedback uses the bank explanation field.
- User-entered commands are no longer automatically executed by the MVP.

Important limitation:
- `check` fields remain in the bank as future state-validation metadata, but the current safe MVP does not execute arbitrary learner input or state checks.
- Exact/normalized answer comparison is still simplistic and will eventually need richer validation.

---

## Working Rules
- One implementation step at a time.
- Do not unnecessarily redesign working architecture.
- Preserve code/data separation.
- Prefer real operational scenarios over trivia.
- Keep files human-readable.
- Preserve source provenance.
- Do not count an unintroduced concept as ordinary retrieval failure.
- Use state-based validation eventually where safe and appropriate.
- GitHub is the active development source of truth.

---

## Completed
- Repository structure established.
- Canonical project files created.
- Initial Python MVP created.
- Scenario bank created and expanded LL001–LL042.
- Week 2 NOS-120 commands/coursework harvested.
- Adaptive tutoring principles incorporated into project doctrine.
- Python MVP refactored to load the JSON bank rather than five hard-coded drills.

---

## Current Priority
Bring the documentation up to the current learning architecture and then harvest the newly learned NOS-120 filesystem/navigation material into `scenario_bank.json`.

## Next Exact Task
Audit and expand `scenario_bank.json` with the recent NOS-120 material, beginning with navigation/filesystem/globbing commands actually encountered in the labs, while preserving the existing schema and source provenance.
