# LinuxLingo Project Continuity

## Purpose
This file is the operational handoff document for LinuxLingo. It lets a fresh development or AI-assisted session recover the current state without needing the full conversation history.

Update this file after every substantial LinuxLingo work session.

---

## Current Project State
- Project: LinuxLingo
- Repository: GitHub (`Dtalarico/LinuxLingo`)
- Development model: terminal-first Python MVP growing toward an adaptive terminal-fluency system.
- GitHub is the active source of truth.
- Older concept/design documents remain archived reference material in Google Drive and should be consulted when revising canonical architecture so the current MVP does not accidentally redefine the original project vision.
- `scenario_bank.json` is the authoritative training corpus.
- `linuxlingo.py` loads drills from `scenario_bank.json`; the original five hard-coded drills have been removed from the engine.

---

## Canonical Project Files
- `README.md`
- `PROJECT_CONTINUITY.md`
- `LINUXLINGO_MASTER_SPEC.md`
- `linuxlingo.py`
- `scenario_bank.json`

`.gitignore` is repository infrastructure rather than a canonical design/data document.

A future canonical Markdown file will preserve the current Adaptive Infrastructure Tutoring Prompt in the repository and will be referenced by the appropriate project documentation.

---

## Architecture

### `linuxlingo.py`
Python CLI engine. Program behavior belongs here.

### `scenario_bank.json`
Canonical drill/training bank. Commands, prompts, valid answers, tags, explanations, source provenance, difficulty, and validation metadata belong here.

### `LINUXLINGO_MASTER_SPEC.md`
Canonical architecture, learning philosophy, training model, and long-term doctrine. It describes LinuxLingo the system, not merely the present MVP implementation.

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

The original project vision remains authoritative: Duolingo-style micro-drills create enough meaningful repetitions to build command-line muscle memory, then progress through Basic, Fluency/Bridge, and Professional/RHCSA-oriented operation.

---

## Adaptive Tutoring Relationship
LinuxLingo is the CLI practice/retrieval layer of a larger learning workflow.

Current learning pipeline:

**SOURCE CONTENT → INGESTION → ADAPTIVE TEACHING → LINUXLINGO RETRIEVAL/PRACTICE → TERMINAL EXECUTION → FEEDBACK → DELAYED/VARIED RETESTING → FLUENCY**

The adaptive tutoring method should teach concepts before LinuxLingo treats them as expected independent recall.

Important distinction:

1. **Retrieval failure:** the learner was taught the concept but cannot independently retrieve/apply it.
2. **Coverage failure:** the source/course/lab asks for a command or concept that the learner has not actually been introduced to.

These are different failures and should not be scored or remediated identically. A future mastery system should track source exposure/coverage separately from retrieval performance.

---

## Source Ingestion Doctrine
The largest scaling bottleneck is no longer merely writing quiz logic; it is converting trustworthy Linux source material into structured training data efficiently and accurately.

Potential sources include coursework/labs, Linux Essentials/LPIC material, RHCSA study material, real administration tasks, troubleshooting sessions, and authoritative command documentation.

Ingestion should preserve provenance. Do not blindly convert every quiz fact into a command drill.

Preferred coursework workflow:

**LAB → LEARN → HARVEST → COMMIT → MOVE ON**

Harvest after each lab when practical rather than after several labs; this preserves more granular data about exposure, reasoning, difficulty, and genuinely new material.

---

## Current Bank State
- `scenario_bank.json` now contains **100 drills: LL001–LL100**.
- 28 drills, LL043–LL070, were harvested from earlier September 4 NOS-120 work.
- 11 drills, LL071–LL081, were harvested from the September 4 display-lines / text-processing / AWK lab.
- 15 drills, LL082–LL096, were harvested from the September 13 Cengage LDM-004 directory-management lab.
- 4 drills, LL097–LL100, were harvested from the September 13 Configuring Docker Containers lab.
- Earlier September 4 material includes navigation, wildcard/globbing behavior, `type`, PATH/`which`, nested directory creation, quoting/escaping spaces, `cp`, recursive `cp`, `mv`, `rm`, `rmdir`, recursive directory removal, brace expansion, `ls -lh`, Vim fundamentals, shell history, and Bash built-in help.
- LL071–LL081 add `head`, `head -1`, `head -v`, `tail`, `tail -v`, `df | tail +2`, `nl` with output redirection, `tac`, AWK whole-record and field selection, and the Bash/AWK single-quote language boundary.
- LL082–LL096 add `su`, recursive `ls -R`, multiple-directory creation, relative-path copy/move operations, move-and-rename behavior, relative-vs-absolute path correction, `grep -i`, `history -a`, `id`, searching `.bashrc`, and `find ... -newermt`.
- LL097–LL100 add Docker image listing, image building/tagging, detached container execution with port publishing, and running-container verification.
- Some quiz-derived recognition items remain and may later be reviewed for value.

---

## September 4 Text-Processing / AWK Harvest
The completed Cengage lab produced unusually high-value design evidence despite being short.

New command/content primitives include:

- `head` and `tail` default line behavior
- `-v` as forced filename-heading / verbose behavior
- starting `tail` at line 2 to remove a header from piped output
- `nl` for line numbering
- transformed output redirected with `>`
- `tac` for reverse line order, including the operational reason it is useful when newest records are appended at the bottom
- `awk` as a utility that interprets programs written in the AWK language
- AWK records and fields (`$0`, `$1`, `$2`)
- AWK action blocks and `print`
- Bash single quotes as the boundary that preserves embedded AWK syntax from shell expansion

The session reinforced an important teaching requirement: **layer ownership must be explicit when one language invokes another.** A learner should be able to identify which interpreter owns each piece of syntax rather than memorizing opaque command strings.

Example layered command:

`awk '{print $1}' pw`

- Bash owns command invocation and shell quoting.
- Single quotes preserve the embedded text from Bash expansion.
- AWK owns `{ ... }`, `print`, and `$1`.
- `$1` is the first field of the current AWK record.

This aligns with the original LinuxLingo tiered design: teach concrete primitives, preserve their semantic boundaries, then compose them into larger command structures.

---

## September 13 Directory-Management / Shell-History Harvest
The LDM-004 lab was long and repetitive, but it produced useful operational material because the same filesystem primitives were exercised repeatedly in different path contexts.

High-value additions include:

- switching user context with `su user01`
- recursive directory inspection with `ls -R`
- creating several sibling directories in one `mkdir` command
- copying and moving files between sibling directories with `..` relative paths
- renaming files with `mv`
- distinguishing `/IT-temp` from `IT-temp` and therefore absolute from relative paths
- case-insensitive search with `grep -i`
- persisting current-session commands with `history -a`
- inspecting identity with `id`
- searching shell configuration with `grep alias ~/.bashrc`
- time-based file discovery using `find . -type f -newermt <date>`

The lab also exposed a useful training lesson: some automated graders inspect shell history rather than only filesystem end state. `history -a` is therefore worth knowing as a real Bash command, even though the repeated grading friction was specific to the lab platform.

---

## September 13 Docker Harvest
The Configuring Docker Containers lab added a compact container workflow:

- list local images with `docker images`
- build/tag an image with `docker build -t web2 .`
- run a named detached container with host/container port publishing using `docker run -d --name ... -p ...`
- verify running containers with `docker ps`

These drills belong in the fluency layer because they combine Linux CLI syntax with container operations rather than basic filesystem vocabulary.

---

## Engine State
- Engine loads the authoritative JSON bank at startup.
- Original five hard-coded drills are removed.
- Engine validates the top-level bank shape and required drill fields.
- Basic whitespace normalization is used for answer comparison.
- Feedback uses the bank explanation field.
- User-entered commands are not automatically executed.

Important limitation:
- `check` fields remain as future state-validation metadata, but the current safe MVP does not execute arbitrary learner input or state checks.
- Exact/normalized answer comparison remains simplistic and will eventually need richer validation.

---

## Master Spec Revision — 2026-09-05
`LINUXLINGO_MASTER_SPEC.md` was substantially revised after rereading the archived LinuxLingo concept documents in Google Drive.

The revision deliberately preserves the original overarching design rather than allowing the current Python/JSON MVP to redefine the project. It now explicitly integrates:

- original Duolingo-style micro-drill / command-muscle-memory concept
- Linux-as-language doctrine
- Basic → Fluency/Bridge → Premium/Professional progression
- active recall and terminal production
- varied question-format architecture
- terminal-first implementation strategy
- source ingestion and provenance
- adaptive teaching relationship
- coverage failure vs retrieval failure
- per-lab harvesting workflow
- current safe MVP limitations
- mastery evidence and delayed retesting
- future state validation and fluency missions
- distinction between current implementation and long-term system design

David intends to reread the revised Master Spec personally and review it for fidelity.

---

## Working Rules
- One implementation step at a time.
- Do not unnecessarily redesign working architecture.
- Preserve original design intent when modernizing documentation.
- Preserve code/data separation.
- Prefer real operational scenarios over trivia.
- Keep files human-readable.
- Preserve source provenance.
- Do not count an unintroduced concept as ordinary retrieval failure.
- Harvest useful coursework after each lab when practical.
- Use state-based validation eventually where safe and appropriate.
- Make commit messages specific enough that the project history explains what changed.
- GitHub is the active development source of truth.

---

## Completed
- Repository structure established.
- Canonical project files created.
- Initial Python MVP created.
- Python MVP refactored to load JSON rather than five hard-coded drills.
- Scenario bank expanded through LL100.
- September 4 NOS-120 material harvested into LL043–LL070.
- September 4 display-lines / text-processing / AWK lab harvested into LL071–LL081.
- September 13 directory-management / shell-history material harvested into LL082–LL096.
- September 13 Docker container material harvested into LL097–LL100.
- Bash/AWK interpreter-boundary learning captured as explicit drill material rather than only a memorized AWK command string.
- Absolute-vs-relative path failure from the September 13 lab captured as an error-correction drill rather than discarded as a mistake.
- Shell-history persistence (`history -a`) captured explicitly because it materially affected the lab workflow.
- Archived LinuxLingo concept documents reread to recover original overarching design intent.
- Master Spec revised on 2026-09-05 to integrate original vision with current adaptive/ingestion architecture.
- Continuity updated to reflect the revised architecture and per-lab harvesting workflow.

---

## Remaining Documentation Work
- David should personally reread/review the revised `LINUXLINGO_MASTER_SPEC.md` for fidelity; revise if his review identifies anything that does not accurately represent the project.
- Add the current Adaptive Infrastructure Tutoring Prompt to the repository as its own Markdown file and reference it from the appropriate canonical documentation.

---

## Current Priority
The scenario bank is current through the completed September 13 directory-management and Docker-container labs and has reached 100 drills. Continue using the per-lab harvest workflow so new coursework becomes training data while the details are still fresh.

## Next Exact Task
On the next completed Linux/CLI lab, harvest the genuinely useful commands, flags, path semantics, troubleshooting lessons, and verification steps into `scenario_bank.json`, then update this continuity file. Separately, David still plans to review `LINUXLINGO_MASTER_SPEC.md` for fidelity and add the standalone Adaptive Infrastructure Tutoring Prompt when ready.
