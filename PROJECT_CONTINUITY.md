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


---

## October 31, 2026 — at/cron scheduling video harvest

**Status:** APPROVED by author for repository update. Video viewed and discussed; no independent terminal execution or lab completion claimed.

**Source:** Supplemental RHCSA RHEL 8 video, “Schedule tasks using at and cron,” with author-provided screenshots and guided discussion. Some screenshots were blurry and were not treated as verified command evidence. The presenter’s demonstrations were on RHEL 8, not the author’s lab machine.

**Corpus change:** Added LL186–LL200 (15 drills) to `scenario_bank_2.json`, following LL185. Corpus total **200** (LL001–LL200); existing entries and engine unchanged. Commit `3050b8b112121c1af1908428fd91c2bb1b5b8b14`. Source is observed video/guided reasoning, not demonstrated student mastery.

**Observed video mechanisms:** `at now + 1 minute`, interactive `at>` commands followed by Ctrl+D/end-of-input, `atq`, `atrm`, `at 3pm + 3 days -f script.sh`, `crontab -e`, `crontab -l`, `crontab -u cengland -e`, and the system cron locations under `/etc`. A failed `atrm 1` returned “Cannot find jobid 1”; the job was no longer pending, but execution was not independently established by that message. The video showed `atrm 3` without an error, but no subsequent queue verification. The video demonstrated `man at` and discussed manual/reference documentation. The author also requested `info cron` and `info at` as useful reference commands; their Info-node availability is installation-dependent.

**Scheduling model:** `at` submits one-time work, whereas cron runs recurring jobs whenever its schedule matches. Cron's five standard time fields were explored, including comma-separated hours and weekdays: `30 9,15 * * 1,4` means Monday/Thursday at 09:30 and 15:30. For the first Friday of a month, the discussion explained why `0 9 1-7 * 5` is unsuitable under common Cronie/Vixie OR semantics for restricted day-of-month/day-of-week fields, and illustrated a shell weekday condition with an escaped percent sign. More complex fallback examples were hypothetical requirements analysis, not code executed or approved for deployment.

**Paths and execution context:** The instructor's root-owned crontab included `echo "test" > crontest.txt` without an absolute output path. A later listing located `/root/crontest.txt`. The author recognized that relative redirection and the cron working directory caused the unexpected location. Distinguish root the account, `/root` the home directory, and `/` the filesystem root. Do not generalize that every cron implementation or every root job always starts in `/root`. The instructor's separate script invocation used `/home/cengland/Documents/script.sh`.

**Other learning:** `ls -lhtra` was decomposed; `-t` (modification-time ordering) was newly identified by the author, and `-r` reverses that ordering. `ls -lhS` sorts by size (uppercase S), while `ls -lsh` displays allocated disk usage alongside logical size (lowercase s). `du -sh` and `df -h` were discussed as related capacity-inspection tools; not demonstrated by the video in this session. Author emphasized that storage capacity planning focuses on actual allocated usage, and that correct requirements matter before correct scripts.

**Assistance and authorship:** The author supplied video screenshots, discovered and reasoned about the relative-path issue, asked scheduling and storage questions, and authorized updating the repository. The assistant explained mechanisms and drafted scenario content and this historical entry. No claims of independently completed exercises or tests.

**Next step:** Resume NOS-120 cron/scripting lab using the existing screenshot-first, command-review-before-execution workflow. Verify actual commands and results in the lab before upgrading any learning claim from exposure to demonstrated proficiency.


---

## October 31, 2026 — Cengage LA-006 automation lab harvest

**Authorization:** Author approved an additive harvest. **Execution:** Added LL201–LL215 to new scenario_bank_3.json; updated linuxlingo.py to load the third bank; added dated Master Spec discussion. Earlier 200 drills remain intact. Target corpus is 215 drills across three banks, pending smoke test.

**Observed work:** Created and inspected an at job; configured /etc/crontab for weekday backups; created an executable Bash reporting script and redirected its output; configured a oneshot systemd service and weekday timer; ran daemon-reload, enable --now, and list-timers --all. The terminal displayed the new timer with its associated service and next activation on November 2 at 08:00. The lab verifier passed. This does not establish that a future scheduled run has occurred.

**Attribution:** Student reasoned independently about the timer/service architecture, cron weekday placement, and output redirection; assistant supplied or reviewed several commands. A mistyped enable command was rejected and corrected. This is assisted lab execution with observed verification, not unaided delayed recall. The earlier video-only LL186–LL200 harvest remains separately documented.

**Next:** Verify bank loading, ID uniqueness, total count and interactive execution. Add a systemctl quick-reference and delayed recall exercises in a separately reviewed learning session.


---

## November 3, 2026 — TechWorld with Nana Linux video: command harvest checkpoint

**Status:** APPROVED for this additive continuity checkpoint by the author. Video discussion only; no new scenario drills, code changes, terminal execution, tests, or demonstrated mastery claimed. This records candidates and teaching priorities for a later reviewed harvest.

**Source/provenance:** Author's spoken notes while watching a Linux commands/troubleshooting video identified as TechWorld with Nana. Exact video title, URL, cheat sheet, and exact presenter examples have not yet been independently captured or verified. Reminder scheduled to find/save the cheat sheet later on November 3.

**Corpus inventory at checkpoint:** Three scenario banks contain 215 drills total (LL001–LL215: 100 + 100 + 15). Checked command-related drill fields in all three banks before classifying the following items; do not interpret absence of a command-specific drill as proof the command never appears in any documentation.

**NEW DRILL CANDIDATES (not yet added):** `uname` (kernel/system identification, including `-r` and `-m`); `wc` (line/word/byte counts); `diff` (compare configuration files); `curl` (test URLs/HTTP endpoints). No command-specific drills found for these in the existing scenario banks at this checkpoint. Proposed scenarios need independent review, unique IDs, provenance, and author approval before adding.

**EXISTING COVERAGE / PRACTICE PRIORITY:** `find` is already covered by LL096 and LL109–LL115: modified dates, filename patterns, case-insensitive matching, ownership, size, recent modification, and `-exec`. Author explicitly wants stronger independent `find` proficiency. Video example as reported by author: `find / -name "*.conf"` (author's spoken transcription had spacing around `-name`; canonical syntax shown here). A narrower `find /etc -type f -name "*.conf"` matches existing LL109 closely. Do not add a duplicate drill merely to repeat this syntax; prioritize retrieval, variation, and verification practice.

**AUTHOR-REPORTED FAMILIARITY:** `pwd`, `cd`, `ls`, `cat`, `grep`, pipes, redirection, and `cp`. These were not individually audited for coverage in this checkpoint and familiarity is not a mastery claim.

**TROUBLESHOOTING CURRICULUM CANDIDATE:** Author values the video's application-not-running example, but identified a prerequisite gap: an instructor may assume the learner already knows what PostgreSQL is or which port it uses. PostgreSQL's conventional default TCP port is 5432, but actual application and database configuration must be discovered, not guessed. Suggested guided workflow: identify application/dependencies → inspect relevant configuration → discover listening ports/processes (e.g. `ss -lntp`) → check service state → test connectivity with a suitable tool → compare configuration versions → verify the result. These are proposed teaching steps, not observed lab execution or a confirmed video transcript. Explicitly distinguish defaults from actual observed service state, and coverage failure from retrieval failure.

**Next:** Obtain the video/cheat-sheet source; compare proposed exercises with current banks to prevent duplicate scenarios; co-design useful variations, especially `find` and troubleshooting; add new drills only with author review and separate approval. Maintain append-only historical documentation and honest evidence labels.


---

## November 3, 2026 — command candidates promoted to scenario bank

**Authorization:** Author explicitly directed: “Put the commands in the bank baby.” **Execution:** Appended eight drills, LL216–LL223, to existing `scenario_bank_3.json` (no prior drills removed or changed); the bank now has 23 drills. Total corpus: **223** across three banks (100 + 100 + 23). Bank change commit: `69080e6b0d0e196bb033bb0a92b6d778daf90820`.

**New exercises:** LL216–LL217 `uname -r` / `uname -m`; LL218–LL219 `wc -l` / `wc -w`; LL220–LL221 `diff` / `diff -u`; LL222–LL223 `curl -I` / `curl`. The examples are assistant-authored practice applications of the commands identified in the video discussion, **not verbatim confirmed presenter examples**. Provenance in each drill explicitly labels the author-reported TechWorld with Nana video harvest and guided discussion. `find` remains covered by LL096 and LL109–LL115; no duplicate `find` drill was added.

**Verification:** Re-fetched all three banks after the commit and parsed them as JSON; observed 223 total drill entries, 223 unique IDs, and complete contiguous LL001–LL223 IDs. This is structural data verification, **not** a Python engine runtime smoke test or student performance assessment. No terminal exercises were executed and no mastery is claimed.

**Next:** Run a local engine smoke test when a working copy is available; practice `find` and the new drills with varied tasks and observed terminal output. Capture the original video/cheat sheet URL for precise source attribution when available.


---

## November 8, 2026 — Snap package management, PowerShell on Linux, and assessment semantics

**Authorization:** The author requested a LinuxLingo repository update after the NOS-120 LabConnection Simulation 11.1 walkthrough. **Source:** Author-supplied screenshots and discussion from the guided Configure Snap Packages simulation, November 8, 2026. **Evidence level:** Guided lab interaction with observed terminal output; not independently assessed delayed recall, unrestricted host verification, or proof that the entire simulation was submitted or graded.

**Observed operations and results:** On the Ubuntu training VM, `snap search powershell` displayed PowerShell and preview entries with Microsoft as publisher; `snap install powershell --classic` reported PowerShell 7.3.2 installed; `snap list` showed core20, lxd, powershell, and snapd; `snap info powershell` showed package metadata, channels, and the installed version; `powershell` started a PowerShell session on Linux; and `Get-Host` identified the ConsoleHost version 7.3.2. The student correctly interpreted the installed Snap inventory, recognized Ubuntu also uses APT, and formulated an administrative sequence: discover, inspect, check existing state, change, verify. The mentor refined the order by moving package inspection ahead of installation. Snap and APT package inventories are separate; Snap's `--classic` option changes confinement and deserves a security explanation. The command `powershell` was observed in this training environment; modern PowerShell may use `pwsh`, so do not generalize the executable name across all installations.

**Assessment language problem, preserved as the author's critique:** A multiple-choice item asked how to launch PowerShell on a Linux terminal. Options mixed `Get-Host`, `Enter powershell`, `snap get -powershell`, and `None of these`. The author argued that `Enter powershell` is an English imperative, not the literal command `powershell`, while neighboring items used plain command strings such as `snap list` and `Get-Host`. The mentor judged `Enter powershell` the likely intended response, but a verified answer key was not obtained and the actual graded result of this question was not established. Record this as an **observed inconsistency of option format and interpretation**, not as proven grader error or demonstrated learner failure. Better question design either displays only literal commands consistently or frames each option as a consistent English instruction. Do not make the learner infer which format is intended.

**Drill harvest:** Added LL224–LL230 to `scenario_bank_3.json` without changing prior IDs; now 30 entries in bank 3 and 230 drills across all three banks (100 + 100 + 30). Drills target search, info, installed inventory, classic installation, APT/Snap separation, shell launch, and PowerShell host introspection. Multi-step discover → inspect → inventory → change → verify remains an instructional workflow candidate, not a newly implemented adaptive multi-step engine. The assessment ambiguity belongs in documentation, not as a misleading quiz item.

**Verification boundary:** Repository change and structural drill integrity can be checked from GitHub; no local Python runtime smoke test, independent command reproduction, external simulation grade, or student mastery test is asserted. Next: finish the current NOS-120 lab, capture any further evidence, and test the Python loader when a runnable working copy is available.


---

## November 8, 2026 — LD-004 RPM/APT guided lab harvest, verifier path diagnosis, and retrieval gaps

**Authorization:** Author explicitly requested an additive LinuxLingo harvest update after today's NOS-120 Cengage LD-004 Manage Software with RPM and APT exercises. **Source/evidence:** Multiple author-supplied screenshots and live guided discussion. This entry documents observed commands, reported platform feedback, and learning-design findings; it does not certify independent RHCSA readiness, complete course mastery or a final LD-004 grade.

**Observed operations:** On Linux01, `apt-cache pkgnames >> software-inventory.txt` generated a package-name inventory; the file initially landed in `/home/labuser/Desktop`. On Linux02, the same command landed in `/home/labuser`. The Linux01 verifier initially rejected the inventory while accepting Linux02 and the observed `zsh` / FileZilla installation checks. `ls -l` explicitly showed no Linux01 inventory at `/home/labuser/software-inventory.txt` and a file on Desktop. After `cd /home/labuser` and regenerating the output there, Linux01's inventory verifier passed. The specific hidden verifier rule was not inspected, but the directory is a strongly supported cause. Repeating `>>` appends data, potentially duplicating contents, not correcting the destination. `sudo su` preserves the current working directory in this case; `sudo su -` would normally put root in /root, which was not the intended path. A successful shell command and a grader's expected state are separate layers.

**Additional visible commands/concepts:** `less software-inventory.txt` viewed the inventory (the student's `less -p` and `less.txt` attempts revealed confusion about program names versus file extensions/options); `apt-cache show zsh` displayed package metadata; `sudo apt-get install zsh` and `sudo apt-get install filezilla` were used in the guided lab; `apt-cache depends zsh` and later `apt-cache depends filezilla` displayed required package relationships and recommendations; `dpkg -L filezilla` listed installed package files, contrasting uppercase `-L` with lowercase `-l`; `zgrep` and `grep` were introduced for filtered package-installation logs. The course's log location and literal `install` record marker were not introduced adequately before recall was expected. The screenshot showed `apt-get remove zsh` as a proposed command; the mentor explained the full-purge requirement; the expanded hint supplied `sudo apt-get remove --purge zsh` and `sudo apt-get autoremove --purge`. The author later switched to Linux02 and was working on FileZilla removal. **No final uninstall verifier result was shown**; do not claim full completion from the visible evidence.

**Independent versus assisted recall:** Student required repeated assistance with `apt-cache pkgnames`, `show`, `depends`, and the `install` subcommand, then independently recalled `apt-cache depends filezilla` and correctly interpreted its dependency listing. Student correctly identified that `sudo su` and `sudo su -` differ, interpreted the relative-path/file-placement mismatch after inspection, recognized `remove` as a valid Linux operation, and questioned the undocumented `/home/labuser` expectation. Most commands were guided and/or Cengage-hint validated. Independent delayed mastery is **not established**.

**Pedagogical/Product findings:** The author described excessive hint clicking and inadequate taught prerequisites in a supposedly hands-on course. LinuxLingo must teach command structure **program → subcommand/option → target → output** before expecting independent recall. Differentiate `apt-cache` subcommands from `dpkg` case-sensitive options, APT's `remove` versus `purge`, `depends` versus `recommends`, and commands versus instruction prose. Teach filesystem log conventions, expected log format, date filtering and safe command discovery (man/help) rather than demanding that the student infer these. Build guided terminal exercises with stable initial states, explicit cwd and paths, observable verification, short repeated attempts and delayed recall. Label coverage failures separately from retrieval failures. Avoid claiming the current Python answer-checking MVP already offers guided VM state validation.

**Changes:** Additive scenarios LL231–LL245 appended to scenario_bank_3.json (45 drills in bank 3, 245 overall across three banks), retaining LL001–LL230. These are educational practice artifacts, not proof of student proficiency. The separate `GUIDED_LINUX_PRACTICE_RESOURCES.md` already bookmarks LabEx, Linux Foundation LFS101, LinuxSim, The Linux Camp and RHCSA directions.

**Next:** Verify all banks parse and IDs remain contiguous and unique. Future tutoring should use teach → guided attempt → hint comparison → execute → inspect → spaced retest, and track both mastery and coverage. Verify the actual Linux02 removal/checker results before documenting lab completion.
