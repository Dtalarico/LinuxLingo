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
- Loaded corpus: **132 drills, LL001–LL132**.
- `scenario_bank.json` contains LL001–LL100.
- `scenario_bank_2.json` begins with LL101 and currently contains LL101–LL132.

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

Additional teaching doctrine reinforced by the September 14 permissions/user-context lab:

- **Operation before syntax.** Explain what operational problem a distinction solves before asking the learner to memorize the command form.
- **Atomic semantics before command compression.** Teach owner, group, supplementary membership, recursion, path, identity, and environment as separate ideas before combining them in dense commands.
- **One new abstraction per step whenever practical.** Do not make the learner infer path resolution, permission evaluation, shell nesting, and user context simultaneously.
- **Expected-state telemetry is part of instruction.** A step should say what success looks like, what common failure looks like, and how to verify the resulting state.
- **Teach failure signatures deliberately.** A learner cannot diagnose an authentication failure, permission denial, or missing-path warning reliably if the course has never shown what those failures look like.
- **Partial success must be explained.** A command can authenticate and switch identity successfully while a later environment step still emits a warning. Training should identify which layer succeeded and which failed.
- **Verification verbs require verification commands.** If the learner is told to “verify,” the lab should specify the observable command and expected result when that knowledge has not yet been taught.
- **Do not confuse evidence with narration.** Manually echoing the words `Permission denied` into a file does not capture or prove the actual system-generated failure; it only records a human-supplied description.
- **Nested shells are a stack.** `exit` closes one shell level, not “return to root” by magic. Training should expose the shell stack instead of assuming the learner infers it.

---

## Adaptive Tutoring Relationship
Current learning pipeline:

**SOURCE CONTENT → INGESTION → ADAPTIVE TEACHING → LINUXLINGO RETRIEVAL/PRACTICE → TERMINAL EXECUTION → FEEDBACK → DELAYED/VARIED RETESTING → FLUENCY**

Important distinction:

1. **Retrieval failure:** the learner was taught the concept but cannot independently retrieve/apply it.
2. **Coverage failure:** the source/course/lab asks for a command or concept that the learner has not actually been introduced to.

These should not be scored or remediated identically.

The September 14 permissions lab added a related distinction:

3. **State-interpretation failure caused by missing telemetry:** the learner may perform the right operation but be unable to interpret the result because the system or course does not expose which sub-step succeeded, failed, or remains unchanged.

This should not automatically be treated as a knowledge failure. The tutor should repair the missing system model and then retest.

---

## Source Ingestion Doctrine
Preferred coursework workflow:

**LAB → LEARN → HARVEST → COMMIT → MOVE ON**

Harvest real commands, flags, path semantics, troubleshooting lessons, verification steps, and source provenance while the lab is still fresh.

Do not blindly convert every quiz fact into a drill.

Do not promote brittle lab-platform bookkeeping into Linux doctrine. Preserve the distinction between:

- actual Linux behavior
- a platform's grading/reporting requirement
- a manually written description of system behavior

---

## Current Bank State
- LL001–LL042: original MVP/coursework foundations.
- LL043–LL070: September 4 filesystem/navigation/Vim/wildcard work.
- LL071–LL081: September 4 display-lines/text-processing/AWK work.
- LL082–LL096: September 13 Cengage directory-management/shell-history work.
- LL097–LL100: September 13 Docker container work.
- LL101–LL115: September 14 Cengage `find`, `locate`, `updatedb`, `whereis`, and `which` work.
- LL116–LL132: September 14 Cengage users/groups/ownership/permissions/user-context work.

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

## September 14 Permissions / Users / Context Harvest
New drill material added in LL116–LL132:

- `useradd`
- `passwd USER`
- `groupadd`
- supplementary-group membership with `usermod -aG`
- recursive user/group ownership with `chown -R OWNER:GROUP`
- octal permissions `750` and `640`
- directory-object inspection with `ls -ld`
- file inspection with `ls -l`
- `su USER` versus `su - USER`
- `whoami` for identity verification
- `exit` as one-level shell unwinding
- group-based read access
- intentional permission-denied file creation
- unrelated-user access denial

Operational lessons captured from the lab:

- `usermod` changes user membership; `chown` changes filesystem-object ownership. These are different relationships and should be taught separately before combined scenarios.
- `Payroll` in this lab is specifically a supplementary group for `PayrollEmployee`; terminology should remain precise enough to preserve that distinction.
- Absolute path resolution and permission evaluation are separate abstractions. The current working directory is irrelevant when the target is an absolute path, while access is determined by the effective user and applicable owner/group/other permissions.
- `su USER` changes effective user identity/permissions while preserving more of the current shell environment.
- `su - USER` changes identity and requests a login-style environment. A later warning about a missing home directory does not imply that authentication or identity switching failed.
- Silence after a successful command is normal Linux behavior, but beginner training should not assume the learner already knows that convention.
- A wrong-password failure signature and a post-login environment warning should be explicitly contrasted before expecting the learner to diagnose the difference.
- `exit` closes one nested shell at a time; “return to root” can require multiple exits depending on the shell stack.
- `echo "Permission denied" >> file` writes literal text supplied by the user. It does not capture the original error stream and should not be described as proving or recording the actual failure unless the distinction is made explicit.
- The learner independently reasoned that authentic evidence should come from the actual failing command rather than manually restating the failure text. stderr redirection exists for that purpose, but should not be introduced as syntax until the normal-output/error-output distinction has first been taught.

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
- Intentional-failure drills can currently test the command the learner should issue, but the MVP does not yet execute the command and verify that the expected failure actually occurred.

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
- Teach atomic semantics before compressed syntax.
- Prefer one new abstraction per teaching step when possible.
- Always distinguish system state, human narration, and platform bookkeeping.
- When teaching a state transition, expose a verification method and expected result.
- Make commit messages specific enough that repository history explains what changed.

---

## Completed
- Repository structure established.
- Python MVP created and separated from JSON training data.
- Scenario corpus expanded through LL132.
- September 4 filesystem/navigation/Vim/wildcard harvest completed.
- September 4 text-processing/AWK harvest completed.
- September 13 directory-management/shell-history harvest completed.
- September 13 Docker harvest completed.
- September 14 find/locate/whereis/which harvest completed.
- September 14 permissions/users/groups/identity-context harvest completed through LL132.
- Engine updated to load multiple numbered scenario banks and detect duplicate drill IDs.
- Numbered scenario-bank scaling convention documented.
- `scenario_bank_2.json` established for LL101 onward.
- README updated to reflect the 132-drill loaded corpus and current harvest.
- Autograder-vs-real-Linux design lesson captured explicitly.
- Atomic-semantics, expected-failure, verification-telemetry, nested-shell, and evidence-vs-narration teaching lessons captured explicitly.

---

## Remaining Documentation Work
- David should personally reread/review `LINUXLINGO_MASTER_SPEC.md` for fidelity.
- The Master Spec should eventually receive the September 14 adaptive-teaching doctrine during the next architecture review rather than being rewritten blindly from a partial fetch.
- Add the actual current Adaptive Infrastructure Tutoring Prompt as its own Markdown file only after retrieving and reviewing the real current prompt source.

---

## Current Priority
Continue the per-lab harvest workflow. Add new drills to `scenario_bank_2.json` until that bank is approximately full, then create `scenario_bank_3.json` and add it to the engine's configured bank list.

## Next Exact Task
Finish the remaining September 14 NOS-120 work, harvest genuinely new material into `scenario_bank_2.json`, then update this continuity file again.
