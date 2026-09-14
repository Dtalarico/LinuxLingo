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
- The engine now loads two numbered JSON banks: `scenario_bank.json` and `scenario_bank_2.json`.
- Loaded corpus: **115 drills, LL001–LL115**.
- `scenario_bank.json` contains LL001–LL100.
- `scenario_bank_2.json` begins with LL101 and currently contains LL101–LL115.

---

## Canonical / Active Project Files
- `README.md`
- `PROJECT_CONTINUITY.md`
- `LINUXLINGO_MASTER_SPEC.md`
- `linuxlingo.py`
- `scenario_bank.json`
- `scenario_bank_2.json`

`.gitignore` is repository infrastructure.

---

## Scenario Bank Scaling Convention
The training corpus is deliberately split into numbered JSON files instead of allowing one file to grow indefinitely.

Working convention:

- `scenario_bank.json` = LL001–LL100
- `scenario_bank_2.json` = approximately LL101–LL200
- `scenario_bank_3.json` = approximately LL201–LL300
- continue the numbered pattern as needed

The ~100-drill boundary is an organizational target, not a hard semantic boundary. The goals are to keep individual JSON files readable, easier to inspect and maintain, and faster/cleaner to work with as the corpus grows.

Rules:
- Drill IDs remain globally unique across every bank.
- `linuxlingo.py` combines all configured banks into one runtime drill pool.
- Duplicate IDs across banks are rejected explicitly.
- New coursework harvests go into the currently active numbered bank until it is roughly full, then the next numbered bank is created.
- Source provenance remains attached to each drill regardless of which bank stores it.

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
Current learning pipeline:

**SOURCE CONTENT → INGESTION → ADAPTIVE TEACHING → LINUXLINGO RETRIEVAL/PRACTICE → TERMINAL EXECUTION → FEEDBACK → DELAYED/VARIED RETESTING → FLUENCY**

Important distinction:

1. **Retrieval failure:** the learner was taught the concept but cannot independently retrieve/apply it.
2. **Coverage failure:** the source/course/lab asks for a command or concept that the learner has not actually been introduced to.

These should not be scored or remediated identically.

---

## Source Ingestion Doctrine
Preferred coursework workflow:

**LAB → LEARN → HARVEST → COMMIT → MOVE ON**

Harvest real commands, flags, path semantics, troubleshooting lessons, verification steps, and source provenance while the lab is still fresh.

Do not blindly convert every quiz fact into a drill.

---

## Current Bank State
- LL001–LL042: original MVP/coursework foundations.
- LL043–LL070: September 4 filesystem/navigation/Vim/wildcard work.
- LL071–LL081: September 4 display-lines/text-processing/AWK work.
- LL082–LL096: September 13 Cengage directory-management/shell-history work.
- LL097–LL100: September 13 Docker container work.
- LL101–LL115: September 14 Cengage `find`, `locate`, `updatedb`, `whereis`, and `which` work, stored in `scenario_bank_2.json`.

---

## September 14 Find / Locate Harvest
New drill material added:

- create multiple absolute-path files with one `touch`
- refresh the locate database with `updatedb`
- inspect locate database statistics with `locate -S`
- search JPG paths with `locate`
- narrow locate searches to `/root`
- count locate results with `-c`
- distinguish `whereis` from `which`
- `find /etc -type f -name "*.conf"`
- case-insensitive filename matching with `-iname`
- ownership filtering with `-user`
- size filtering with `-size`
- modification-time filtering with `-mmin`
- execute commands on find results with `-exec ... {} \;`

The September 14 session also produced strong design evidence about autograding:

- A valid Linux command can produce the intended result while a brittle grader still rejects it because the command string does not match the grader's expected form.
- Quoting, path expression, and wildcard handling can differ while remaining valid shell/Linux behavior.
- LinuxLingo should prefer semantic correctness and, where safe, state-based validation over narrow exact-string grading.
- When multiple valid command forms exist, the bank should preserve reasonable alternatives instead of teaching one arbitrary spelling as the only truth.
- Lab-platform requirements such as repeated `history -a` should be distinguished from normal Linux operating practice.

This is directly aligned with the Master Spec's existing validation philosophy and coverage-failure doctrine.

---

## Engine State
- Engine loads configured numbered JSON banks at startup.
- Current banks: `scenario_bank.json` + `scenario_bank_2.json`.
- Duplicate drill IDs are rejected explicitly.
- Required drill fields are validated.
- Basic whitespace normalization is used for answer comparison.
- Feedback uses each drill's explanation field.
- User-entered commands are not automatically executed.

Important limitation:
- Answer validation is still normalized exact matching.
- Safe semantic/state validation remains future work.

---

## Working Rules
- One implementation step at a time.
- Preserve original design intent.
- Preserve code/data separation.
- Prefer real operational scenarios over trivia.
- Preserve source provenance.
- Do not count an unintroduced concept as ordinary retrieval failure.
- Harvest useful coursework after each lab when practical.
- Keep scenario-bank files to roughly 100 drills each and continue the numbered-bank convention as the corpus grows.
- Accept multiple valid Linux forms when they are genuinely equivalent.
- Treat brittle autograder syntax as platform behavior, not as Linux doctrine.
- Make commit messages specific enough that repository history explains what changed.

---

## Completed
- Repository structure established.
- Python MVP created and separated from JSON training data.
- Scenario corpus expanded through LL115.
- September 4 filesystem/navigation/Vim/wildcard harvest completed.
- September 4 text-processing/AWK harvest completed.
- September 13 directory-management/shell-history harvest completed.
- September 13 Docker harvest completed.
- September 14 find/locate/whereis/which harvest completed.
- Engine updated to load multiple numbered scenario banks and detect duplicate drill IDs.
- Numbered scenario-bank scaling convention documented.
- `scenario_bank_2.json` established for LL101 onward.
- README updated to reflect the 115-drill loaded corpus and bank-splitting convention.
- Autograder-vs-real-Linux design lesson captured explicitly.

---

## Remaining Documentation Work
- David should personally reread/review `LINUXLINGO_MASTER_SPEC.md` for fidelity.
- The Master Spec should eventually be revised to replace its remaining singular-bank wording with the numbered-bank architecture when the next architecture review is done.
- Add the Adaptive Infrastructure Tutoring Prompt as its own Markdown file when ready.

---

## Current Priority
Continue the per-lab harvest workflow. Add new drills to `scenario_bank_2.json` until that bank is approximately full, then create `scenario_bank_3.json` and add it to the engine's configured bank list.

## Next Exact Task
Finish the remaining September 14 NOS-120 labs, harvest the genuinely new material into `scenario_bank_2.json`, then update this continuity file again.
