# LinuxLingo Project Continuity

## Purpose
This file is the operational handoff document for LinuxLingo. It lets a fresh development or AI-assisted session recover the current state without needing the full conversation history.

Update this file after every substantial LinuxLingo work session.

---

## Instructional authorship and cross-session handoff

The project's goal includes teaching the student to **write clear, accurate technical and engineering records independently**, not merely collecting entries that an AI assistant writes on the student's behalf. Earlier assistant-written records are useful continuity artifacts but are **not evidence of independent student authorship**.

Progressive writing apprenticeship: **assistant demonstrates → student and assistant co-write → student drafts and assistant critiques → student documents and verifies independently**. Preserve the student's reasoning, command choices, mistakes, troubleshooting and authentic system evidence. State assistance received honestly; do not replace student learning with automatic polishing.

**When starting a new chat or work session:** read this continuity file, the README and the relevant sections of the Master Spec before making project assumptions. Recover the last verified implementation state, open decisions, learning method, student-authored versus assisted evidence, and next exact task. Ask for live verification of any system state that may have changed. GitHub is durable recorded context, **not a copy of the assistant's internal memory**, and no assistant should claim to know unrecorded past actions. Update continuity after substantive work without erasing history or exposing secrets.

Related repositories: [RHCSA training framework](https://github.com/Dtalarico/rhca-training/blob/main/docs/PRACTICAL_LAB_FRAMEWORK.md) governs practical Linux administration competence; [Baby Cloud](https://github.com/Dtalarico/baby-cloud) records integrated infrastructure engineering. LinuxLingo remains a separate terminal-fluency training application and corpus. Do not equate completing drills or having assistant-authored entries with independent administration or documentation proficiency.

---

## Current Project State
- Project: LinuxLingo
- Repository: GitHub (`Dtalarico/LinuxLingo`)
- Development model: terminal-first Python MVP growing toward an adaptive terminal-fluency system.
- GitHub is the active source of truth.
- The engine now loads two numbered JSON banks: `scenario_bank.json` and `scenario_bank_2.json`.
- Loaded corpus: **171 drills, LL001–LL171**.
- `scenario_bank.json` contains LL001–LL100.
- `scenario_bank_2.json` begins with LL101 and currently contains LL101–LL171 (71 drills; verified against the JSON bank on October 26, 2026).
- `LINUXLINGO_MASTER_SPEC.md` now contains the September 14 adaptive-teaching doctrine as canonical architecture, including operation-before-syntax, atomic semantics, one-abstraction-at-a-time sequencing, explicit state telemetry, expected failure states, partial-success interpretation, state-interpretation failure, nested-shell state, and evidence-vs-reporting distinctions.

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

Canonical adaptive-teaching doctrine now lives in the Master Spec and includes:

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

Important distinctions:

1. **Retrieval failure:** the learner was taught the concept but cannot independently retrieve/apply it.
2. **Coverage failure:** the source/course/lab asks for a command or concept that the learner has not actually been introduced to.
3. **State-interpretation failure caused by missing telemetry:** the learner may perform the right operation but be unable to interpret the result because the system or course does not expose which sub-step succeeded, failed, or remains unchanged.

These should not be scored or remediated identically. State-interpretation failure should trigger model repair, explicit verification, and later retesting rather than being treated automatically as a knowledge failure.

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
- LL133–LL160: October 3 service-management, process inspection, state interpretation, networking endpoint reasoning, and Bash completion work.

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

This is directly aligned with the Master Spec's validation philosophy and coverage-failure doctrine.

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

These lessons are no longer continuity-only notes; they are now promoted into `LINUXLINGO_MASTER_SPEC.md` as canonical design doctrine.

---

## October 3 Service Management / Process / Completion Harvest
New drill material added in LL133–LL160:

- `systemctl status`, `start`, `stop`, `restart`, `reload`, `enable`, `disable`, and `is-enabled`
- runtime-state versus boot-policy distinction
- `ps -ef` and its UID/PID/PPID/C/STIME/TTY/TIME/CMD fields
- `ps -ef | grep ssh`, `ufw`, and `apache2`
- `pstree -p | grep ssh` and `pstree -p | grep apache2`
- legacy/deprecated `service ssh restart` syntax for recognition
- `Loaded: loaded`, `enabled`, `active (running)`, and `active (exited)`
- Main PID, PPID 1/systemd parent relationship, daemon TTY `?`, and accumulated CPU TIME
- IP-address versus port responsibility
- Bash prefix completion with `systemctl re` plus double-Tab

Operational and teaching lessons captured:

- `systemd` is the manager; `systemctl` is the interface used to query/control it.
- Current runtime state and boot-time policy are separate dimensions and must be taught separately.
- `systemctl status`, `ps -ef`, and `pstree -p` expose different layers of evidence rather than being interchangeable ways to “look at a service.”
- `active (exited)` is not inherently failure; setup-style units such as UFW can finish their work and leave the unit active without a persistent service process.
- Restart and reload solve different operational problems: restart creates fresh process state; reload asks a running service to reread configuration when supported.
- Deprecated syntax should be preserved as recognition knowledge without making legacy form the primary modern operating path.
- Tab completion is a shell-discovery/self-rescue mechanism. Double-Tab may visibly list matching candidates, but this is interactive shell assistance rather than ordinary command stdout.
- Technical teaching should distinguish “show on screen,” “produce command output,” “filter output,” and “display completion candidates.” Loose verbs create false ambiguity.
- Plain English should accompany canonical terminology: official term + ordinary-language translation + purpose + system relationship.
- The learner's preferred model remains: do not teach incantations; teach the system the command is exposing.

These lessons have also been promoted into the Master Spec as canonical doctrine under mechanism-precise language/shell discovery and service management as a state model.

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
- Do not count missing-telemetry/state-interpretation failure automatically as ordinary learner failure.
- Harvest useful coursework after each lab when practical.
- Keep scenario-bank files to roughly 100 drills each and continue the numbered-bank convention as the corpus grows.
- Accept multiple valid Linux forms when they are genuinely equivalent.
- Treat brittle autograder syntax as platform behavior, not as Linux doctrine.
- Teach operation before syntax.
- Teach atomic semantics before compressed syntax.
- Prefer one new abstraction per teaching step when possible.
- Always distinguish system state, human narration, and platform bookkeeping.
- When teaching a state transition, expose a verification method and expected result.
- Teach representative failure signatures before expecting the learner to diagnose them independently.
- Make commit messages specific enough that repository history explains what changed.

---

## Completed
- Repository structure established.
- Python MVP created and separated from JSON training data.
- Scenario corpus expanded through LL160.
- September 4 filesystem/navigation/Vim/wildcard harvest completed.
- September 4 text-processing/AWK harvest completed.
- September 13 directory-management/shell-history harvest completed.
- September 13 Docker harvest completed.
- September 14 find/locate/whereis/which harvest completed.
- September 14 permissions/users/groups/identity-context harvest completed through LL132.
- October 3 service-management/process/completion harvest completed through LL160.
- Engine updated to load multiple numbered scenario banks and detect duplicate drill IDs.
- Numbered scenario-bank scaling convention documented.
- `scenario_bank_2.json` established for LL101 onward.
- README updated to reflect the 160-drill loaded corpus and current harvest.
- Autograder-vs-real-Linux design lesson captured explicitly.
- Atomic-semantics, expected-failure, verification-telemetry, nested-shell, and evidence-vs-narration teaching lessons captured explicitly.
- September 14 adaptive-teaching doctrine promoted into `LINUXLINGO_MASTER_SPEC.md` as canonical architecture.

---

## Remaining Documentation Work
- David should personally reread/review `LINUXLINGO_MASTER_SPEC.md` for fidelity when convenient.
- Add the actual current Adaptive Infrastructure Tutoring Prompt as its own Markdown file only after retrieving and reviewing the real current prompt source and version lineage. Do not infer or invent a version number.

---

## Current Priority
Continue the per-lab harvest workflow. Add new drills to `scenario_bank_2.json` until that bank is approximately full, then create `scenario_bank_3.json` and add it to the engine's configured bank list.

## Next Exact Task
Continue the current NOS-120 lab from the next instruction after Bash/systemctl completion practice. Harvest only genuinely new material, preserving the exact lab mechanism and plain-English system model.

---

## October 4, 2026 — Manage Server Startup harvest

**Harvested:** LL161–LL171.

New material:
- `useradd -m user01`
- `echo "user01:Passw0rd!" | chpasswd`
- `id user01`
- `systemctl get-default`
- `systemctl isolate multi-user.target`
- `systemctl isolate graphical.target`
- `systemctl set-default multi-user.target`
- `systemctl set-default graphical.target`
- `systemctl reboot`
- runtime target vs persistent boot default
- `readlink -f /etc/systemd/system/default.target` for direct state verification

Observed Cengage grading defect:
- Linux correctly reported `graphical.target` with `systemctl get-default`.
- `readlink -f /etc/systemd/system/default.target` resolved to the graphical target.
- systemd explicitly recreated the `default.target` symlink to `graphical.target`.
- Cengage still failed the GUI-default objective and produced an 82% score.
- Preserve this as concrete evidence for LinuxLingo's doctrine that system-state correctness and autograder acceptance are separate concerns.

**Current corpus:** 171 drills, LL001–LL171.

**Next work:** Continue the current NOS-120 lab sequence, harvest only genuinely new mechanisms/syntax, then proceed with the planned Linux midterm study cycle.


---

## October 27, 2026 — Shared documentation philosophy synthesis (approved and implemented)

**Authority:** Project author approved the staged append-only implementation after review of the proposed policy and six-file scope.

**Sources reviewed:** All 7 files on the LinuxLingo main tree, all 17 files on the Baby Cloud main tree, and the supplied full Adaptive Infrastructure Tutoring Prompt v11 (with preserved prior modules). Tree inventories were not truncated. This current-tree review was **not** an exhaustive audit of earlier Git revisions.

**Original intent:** Preserve both repositories' existing principles, strengthening LinuxLingo with Baby Cloud's human-readable historical decision provenance, and carrying relevant LinuxLingo operational/evidence distinctions back to Baby Cloud. The shared standards are complementary, not a merger of project identities.

**Approved and executed LinuxLingo changes:**
1. New `docs/documentation-policy.md` (LL-DOC-001): append-only historical model, human readability, provenance, decision-state labels, evidence fidelity, learner independence, and continuity.
2. Dated appendix to `LINUXLINGO_MASTER_SPEC.md`: policy relationship and teaching-specific provenance.
3. Dated appendix to `README.md`: accessible public orientation and links.
4. This dated continuity entry.

**Implementation exclusions:** No edits to `linuxlingo.py`, `scenario_bank.json`, `scenario_bank_2.json`, `.gitignore`, historical harvest narratives, or the existing body of the Master Spec. The earlier correction of LL101–LL171 remains separate; the 171-drill corpus is not a consequence of this policy work. Adding the actual v11 source as its own repository artifact remains a separately reviewable task.

**Verification gate:** Git commit identifiers for the changes are available in the main branch history. The new policy's text and appended sections should be retrieved again for post-commit comparison. Existing code and learning functionality have not been changed by this documentation initiative.

**Next step:** Complete the separately approved reciprocal additions to Baby Cloud policy and README, then resume coursework. Future documentation or instructional updates require their own evidence and authorization.

---

## October 30, 2026 — Supplemental process-management harvest and instructional clarification

**Status:** APPROVED by project author for append-only implementation on October 30; video observed and questions discussed, not independent terminal demonstrations.

**Source:** A 16-minute NOS-120 supplemental process-management video (the video presenter is distinct from course instructor Darvish), followed by an extended guided discussion. Source observations are separated from explanations, examples, and proposed exercises; no claim is made that the author executed every command.

**Corpus addition:** LL172–LL185 (14 drills), appended to `scenario_bank_2.json`. Existing LL001–LL171 remain in their original order. Corpus total: **185**. The engine and bank configuration remain unchanged.

**New learning areas:** interactive `top` monitoring and sorting; `ps -o` field selection versus `ps -p` process selection; `pidof`; `pkill`; `kill` signals; explicit `nice -n` relative adjustments; `renice` changes to existing processes; inspecting NI; and observe–change–verify reasoning. Previously covered `ps -ef` and `systemctl start` mechanisms were not duplicated. Video examples including `systemctl start auditd`, `ps -edf`, and signal-display variants are retained here as source context for later review, not as claims of a successful machine operation. Distribution/service policy may restrict `auditd` manual startup.

**Instructional incident — hidden initial state:** The video described `nice -n 10` as producing niceness 10 without explicitly establishing the launching process's niceness. The author asked what the initial value was. The precise model is **inherited niceness + requested relative adjustment = resulting niceness**, within system permissions and limits; zero is common but is not a verified universal starting state. A beginner cannot be expected to know which premises an instructor considers typical. State the premise and show a way to observe it.

**Instructional incident — unnecessary command compression:** During tutoring, the assistant introduced `ps -o pid,ni,comm -p 1234` before explaining why both options were present. The author questioned the complexity. Repair: `-o` answers *which fields?*; `-p` answers *which process?*; only combine them when the task requires both. The example PID 1234 was invented for teaching and must not be represented as a real observed PID.

**Instructional incident — ambiguous marks and values:** The discussion distinguished `nice -4` (legacy shorthand for a positive adjustment on the GNU utility) from `nice -n -4` (a negative numeric adjustment), and relative `nice` from GNU/Linux `renice` absolute target values. Prefer explicit `-n` teaching syntax; a dash used as an option marker is not automatically a numeric negative sign. Permissions for raising scheduling priority must be addressed.

**Teaching conclusion:** Simplification that hides necessary preconditions can increase learning complexity. For beginners, explain the operation, initial conditions, each new option, observable output, failure modes, and verification **before** condensing syntax. This extends, rather than replaces, existing operation-before-syntax and atomic-semantics rules. Distinguish **observed video content**, **guided reasoning**, **validated drill content**, and **independently executed terminal evidence**.

**Historical/assistance attribution:** The author supplied the questions, challenged assumptions and unnecessary complexity, approved scope, and contributed the learning insight; the assistant drafted the new drill/data and documentation text. This does not establish independent student authorship or measured mastery.

**Next work:** Resume per-lab harvests. Revisit process scheduling with an actual terminal session for independent retrieval, output inspection, and evidence of results; treat the first video harvest as exposure and guided understanding rather than demonstrated mastery.
