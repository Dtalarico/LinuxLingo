# LinuxLingo — Master Specification

## Document Status

**Project:** LinuxLingo  
**Document:** `LINUXLINGO_MASTER_SPEC.md`  
**Role:** Canonical architecture and design specification  
**Status:** Active  
**Development Model:** Terminal-first Python MVP

This document is the authoritative design specification for LinuxLingo.

Older LinuxLingo concept papers and design drafts are archived reference material. Their useful ideas are consolidated here.

Current project state belongs in `PROJECT_CONTINUITY.md`.

Program logic belongs in `linuxlingo.py`.

Training data belongs in `scenario_bank.json`.

---

# 1. Project Overview

LinuxLingo is a terminal-first Linux learning system designed to build real command-line fluency through active recall, repetition, scenario-based practice, troubleshooting, and progressively more difficult terminal tasks.

The central idea is:

**Linux should be learned like a language.**

- Commands are vocabulary.
- Flags are grammar.
- Pipelines are sentence structure.
- Real terminal tasks are conversation.

The learner should progress from recognizing commands to producing and using them naturally.

Core learning model:

**problem → command → execution**

---

# 2. The Problem

Linux is often taught through:

- long videos
- passive reading
- lectures
- command lists
- tutorials
- large projects introduced before basic terminal confidence develops

These approaches can create recognition without production.

A learner may recognize `mkdir`, `grep`, or `chmod` when shown the command but still freeze when asked to solve a real problem from a blank terminal.

LinuxLingo is designed to close that gap.

The goal is not simply:

> “I have seen this command.”

The goal is:

> “I know what to type, why I am typing it, and what result I expect.”

---

# 3. Core Learning Philosophy

LinuxLingo emphasizes:

1. Active recall
2. Command production
3. Repetition
4. Progressive difficulty
5. Scenario-based problem solving
6. Real terminal interaction
7. Error diagnosis
8. Practical verification
9. Adaptive reinforcement
10. Mastery rather than simple exposure

Linux fluency is treated as a conditioned skill.

The learner repeatedly translates:

**situation → reasoning → command execution**

---

# 4. Minimum Viable Product

The initial LinuxLingo MVP is a Python command-line application.

The MVP should:

- load drills from a JSON bank
- present Linux tasks
- accept typed responses
- evaluate responses
- provide feedback
- track basic performance
- reinforce missed concepts
- progressively expose the learner to more difficult commands

The first MVP should remain intentionally simple.

It does NOT require:

- a mobile application
- a web interface
- a graphical desktop application
- a simulated terminal
- containerized training environments
- complex artificial-intelligence infrastructure

Those may be added later.

The first objective is to prove that the terminal-first training model works.

---

# 5. Canonical Project Files

LinuxLingo currently uses five canonical files.

## `README.md`

Public-facing project overview.

It explains:

- what LinuxLingo is
- why it exists
- the basic learning philosophy
- the high-level architecture
- current project status

---

## `PROJECT_CONTINUITY.md`

Operational handoff document.

It records:

- current project state
- completed work
- important recent decisions
- what is currently being developed
- the next exact task

Its purpose is to allow a fresh development or AI-assisted work session to recover project state quickly.

It must remain concise.

It must NOT contain the growing command bank.

---

## `LINUXLINGO_MASTER_SPEC.md`

This document.

It contains:

- architecture
- design doctrine
- learning philosophy
- question architecture
- training tiers
- adaptive tutoring principles
- command-bank architecture
- development direction

---

## `linuxlingo.py`

Python CLI engine.

The engine will progressively handle:

- loading training data
- selecting drills
- presenting questions
- accepting user input
- validating responses
- recording results
- controlling sessions
- adaptive drill selection
- mastery tracking

The engine should remain reasonably small and understandable.

---

## `scenario_bank.json`

Canonical command and drill bank.

It stores training data including:

- drill IDs
- question types
- difficulty
- categories
- tags
- prompts
- valid answers
- explanations
- validation checks where appropriate
- mastery metadata where appropriate

The bank should be able to grow independently from the Python engine.

---

# 6. Code and Data Separation

LinuxLingo separates program behavior from training content.

The basic architecture is:

`linuxlingo.py`

↓

loads

↓

`scenario_bank.json`

↓

selects drill

↓

presents task

↓

learner responds

↓

response is evaluated

↓

result is recorded

↓

next drill is selected

The growing command bank should NOT be hard-coded permanently inside the Python program.

This separation allows the drill bank to grow from dozens to hundreds or eventually thousands of exercises without requiring the core engine to be rewritten each time.

---

# 7. Question Architecture

LinuxLingo should support multiple question formats.

The MVP may begin with only the simplest formats and expand gradually.

---

## Type A — Knowledge / Recognition

Example:

**Question:**  
What command prints the current working directory?

**Answer:**  
`pwd`

Purpose:

- reinforce meaning
- support terminology recall
- establish foundational knowledge

Recognition questions should support Linux fluency but should not dominate the system.

---

## Type B — Scenario Command

Primary training format.

Example:

**Task:**  
Create a directory named `projects`.

**Answer:**  
`mkdir projects`

Purpose:

- build command recall
- connect real tasks to terminal commands
- train production rather than recognition

---

## Type C — Error Correction

Example:

**Broken command:**

`ls --alll`

**Task:**  
Correct the command.

Possible answers:

`ls --all`

or

`ls -a`

Purpose:

- build troubleshooting ability
- reinforce syntax
- reinforce flag knowledge
- develop debugging instincts

---

## Type D — Fill in the Blank

Example:

`____ -l`

Answer:

`ls`

Purpose:

- reinforce syntax
- reinforce command recognition
- provide lighter retrieval practice

---

## Type E — Reverse Recognition

Example:

**Command:**

`chmod 755 script.sh`

**Task:**  
Explain what the command does.

Purpose:

- connect syntax to behavior
- strengthen comprehension

---

## Type F — Command Construction

Example:

Requirements:

- list files
- use long format
- show human-readable file sizes

Answer:

`ls -lh`

Purpose:

- teach flags as composable grammar
- build command construction ability

---

## Type G — Terminal Simulation

Example:

`~/practice$`

Task:

Create a directory named `projects`.

Answer:

`mkdir projects`

Purpose:

- increase realism
- connect drills to real terminal context

---

# 8. MVP Question Flow

For the initial MVP, LinuxLingo should remain simple.

The basic loop may be:

1. Select one drill.
2. Present one task.
3. Accept one response.
4. Grade or validate the response.
5. Provide feedback.
6. Record the result.
7. Move to the next drill.

This keeps the first implementation understandable and testable.

---

# 9. Future Multi-Question and Extended Task Support

Linux usage often involves sequences rather than isolated commands.

LinuxLingo should eventually support extended question groups and multi-step operational tasks.

Future sessions may present:

- several related questions at once
- command sequences
- chained administrative tasks
- troubleshooting workflows
- multi-stage scenarios
- longer terminal missions

Example:

**Scenario:**

A new project directory must be created, entered, populated with a file, and verified.

Possible sequence:

`mkdir project`

`cd project`

`touch notes.txt`

`ls -l`

The architecture should eventually support this kind of extended interaction.

However:

**The MVP will begin with one task at a time.**

Multi-question and extended scenario support is a planned capability, not an immediate requirement.

---

# 10. Validation Philosophy

Whenever practical, LinuxLingo should validate successful system state rather than only compare exact command strings.

Example:

Task:

Create a directory named `project`.

One valid command is:

`mkdir project`

Instead of only checking whether the learner typed exactly that text, LinuxLingo may verify:

`test -d project`

If the directory exists, the operation succeeded.

This allows multiple technically valid solutions where appropriate.

State-based validation more closely resembles real Linux administration.

Not every drill requires state validation.

Recognition and conceptual questions may still use answer comparison.

---

# 11. Scenario Bank Structure

A scenario may use a structure similar to:

{
  "id": "LL001",
  "type": "scenario",
  "difficulty": "beginner",
  "tags": ["filesystem", "directories"],
  "prompt": "Create a directory named 'projects'.",
  "answers": ["mkdir projects"],
  "explanation": "The mkdir command creates a directory."
}

A scenario requiring state validation may later include:

{
  "id": "LL002",
  "type": "scenario",
  "difficulty": "beginner",
  "tags": ["filesystem", "directories"],
  "prompt": "Create a directory named 'workspace'.",
  "answers": ["mkdir workspace"],
  "check": "test -d workspace",
  "explanation": "mkdir creates a directory."
}

The exact JSON schema may evolve.

The permanent rule is:

**training data remains separate from program logic.**

---

# 12. Adaptive Tutoring Model

LinuxLingo should eventually behave as an adaptive tutor rather than a simple random quiz generator.

The adaptive system should track what the learner actually knows.

Important principles include:

- test one concept at a time when appropriate
- identify strong and weak areas
- reinforce missed concepts
- reduce unnecessary repetition of mastered concepts
- distinguish recognition from true recall
- delay contaminated retests
- vary context when retesting
- track the quality of mastery evidence
- progressively increase difficulty

The system should attempt to determine:

- what has been introduced
- what has been tested
- what has been answered correctly
- what has been answered incorrectly
- what appears mastered
- what needs more practice
- what has not yet been covered

---

# 13. Mastery Evidence

Not every correct answer proves equal understanding.

LinuxLingo should eventually distinguish between:

- independent recall
- successful application in a new context
- delayed recall
- immediate recall
- recognition
- elimination
- guessing
- answer leakage
- correction immediately after being shown the answer

Stronger mastery evidence includes:

- independent command production
- correct use in a new scenario
- delayed recall
- successful troubleshooting

Weaker mastery evidence includes:

- obvious elimination
- repeated identical prompts
- answers revealed by the question itself
- immediate retesting after correction

---

# 14. Delayed Retesting

If a learner misses a concept and is immediately shown the correct answer, asking the same question again does not prove independent recall.

The answer remains active in working memory.

LinuxLingo should eventually:

1. explain the error
2. move to another concept
3. return to the missed concept later
4. use a different scenario when possible

The delayed retest provides better evidence of real learning.

---

# 15. Question Quality

LinuxLingo questions should avoid poor assessment design.

Questions should avoid:

- ambiguous stems
- unstated assumptions
- nonsense distractors
- answer leakage
- technically impossible alternatives
- wording that accidentally reveals the command
- repetitive questions that test nothing new

The correct answer should be correct because the learner understands the system, not merely because every alternative is absurd.

---

# 16. Immediate Repair

When the learner answers incorrectly, LinuxLingo should provide enough explanation to repair the misunderstanding.

Feedback may include:

- whether the answer was correct
- the expected command
- a concise explanation
- the role of the command
- relevant flag meaning
- why the learner's answer failed

The goal is not merely grading.

The goal is model repair.

---

# 17. Difficulty Model

Initial difficulty levels may include:

- beginner
- intermediate
- advanced

Difficulty should consider:

- command complexity
- number of required concepts
- number of flags
- path complexity
- command chaining
- troubleshooting requirements
- system impact
- amount of reasoning required

Difficulty should not simply mean that a command is obscure.

---

# 18. Basic Tier — Foundation

## Goal

Move the learner from terminal fear to functional literacy.

The learner should be able to navigate Linux and perform essential file operations without constantly consulting a cheat sheet.

---

## Navigation

Commands may include:

- `pwd`
- `ls`
- `cd`
- `clear`

Concepts include:

- current directory
- parent directory
- home directory
- relative paths
- absolute paths

---

## File and Directory Management

Commands may include:

- `mkdir`
- `rmdir`
- `touch`
- `cp`
- `mv`
- `rm`

---

## Viewing and Output

Commands may include:

- `cat`
- `less`
- `head`
- `tail`
- `echo`

---

## Basic Editing

Tools may include:

- `nano`
- introductory `vi`
- introductory `vim`

---

## Redirection and Pipes

Concepts may include:

- `>`
- `>>`
- `|`
- `grep`

---

## Basic Tier End State

The learner can:

- navigate directories
- create files and folders
- move and rename objects
- inspect file contents
- perform simple searches
- use basic redirection and pipelines

---

# 19. Fluency Track — The Bridge

## Goal

Move the learner from basic command familiarity to calm, repeatable Linux operation.

The Fluency Track develops:

- command sequencing
- system awareness
- diagnostic instincts
- command combinations
- practical administration habits

---

## Identity and Context

Commands may include:

- `whoami`
- `id`
- `groups`
- `sudo -l`
- `hostname`
- `hostnamectl`

Goal:

Understand:

- who the current user is
- what permissions they have
- what system they are operating

---

## Process Control

Commands may include:

- `ps`
- `ps aux`
- `top`
- `kill`
- `kill -9`
- `nice`
- `renice`
- `uptime`
- `jobs`
- `bg`
- `fg`

Goal:

Observe and control running processes.

---

## Package Management

Commands may include:

- `apt`
- `dnf`
- package update operations
- package upgrade operations
- `which`
- `whereis`
- `man`
- `--help`

Goal:

Install software, inspect software availability, and use Linux documentation for self-rescue.

---

## File Discipline

Commands may include:

- `find`
- `grep`
- `wc`
- `sort`
- `uniq`
- `cut`

Goal:

Find, filter, extract, organize, and verify information.

---

## Network Comfort

Commands may include:

- `ip a`
- `ip addr`
- `ping`
- `curl`
- `ssh`
- `hostname`

Goal:

Perform basic connectivity diagnosis and understand system network identity.

---

## Configuration Confidence

Commands and tools may include:

- `nano`
- `vi`
- `vim`
- `cat`
- `head`
- `tail`
- `diff`
- `history`

Goal:

Modify configuration files, verify changes, and recover from mistakes without panic.

---

# 20. Premium Tier — Professional Operations

## Goal

Develop professional Linux administration competence with eventual RHCSA alignment.

The Premium Tier emphasizes:

- permissions
- ownership
- services
- system health
- storage
- networking
- archives
- automation

---

## Permissions and Ownership

Commands may include:

- `chmod`
- `chown`
- `chgrp`
- `sudo`
- `umask`

---

## System Vitality and Services

Commands may include:

- `top`
- `htop`
- `df -h`
- `systemctl`
- `journalctl`

---

## Storage and Networking

Commands may include:

- `lsblk`
- `ssh`
- `scp`
- `rsync`
- `ip addr`
- `tar`
- `gzip`

---

## Automation

Topics may include:

- shell scripts
- Bash variables
- loops
- cron jobs

---

# 21. Command Categories

The scenario bank may organize commands into domains.

---

## Navigation

Examples:

- `pwd`
- `ls`
- `ls -l`
- `ls -a`
- `ls -la`
- `cd`
- `cd ..`
- `cd ~`

---

## File and Directory Management

Examples:

- `mkdir`
- `rmdir`
- `rm`
- `rm -r`
- `rm -rf`
- `cp`
- `cp -r`
- `mv`
- `touch`

---

## File Viewing and Inspection

Examples:

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `tail -f`
- `wc`
- `file`

---

## Search and Text Processing

Examples:

- `grep`
- `grep -r`
- `grep -i`
- `find`
- `locate`
- `which`
- `whereis`
- `cut`
- `sort`
- `uniq`

---

## Permissions and Ownership

Examples:

- `chmod`
- numeric permission modes
- symbolic permission modes
- `chown`
- `chgrp`
- `umask`

---

## Users and Groups

Examples:

- `useradd`
- `userdel`
- `usermod`
- `passwd`
- `groupadd`
- `groupdel`
- `groups`
- `id`

---

## Process Management

Examples:

- `ps`
- `ps aux`
- `top`
- `htop`
- `kill`
- `kill -9`
- `pkill`
- `jobs`
- `bg`
- `fg`

---

## System Information

Examples:

- `uname`
- `uname -a`
- `whoami`
- `who`
- `uptime`
- `hostname`
- `hostnamectl`
- `date`
- `lsblk`
- `free`
- `df`
- `df -h`
- `du`
- `du -sh`

---

## Networking

Examples:

- `ping`
- `ip addr`
- `ip link`
- `ip route`
- `ss`
- `curl`
- `wget`
- `ssh`

---

## Package Management

Ubuntu / Debian examples:

- `apt update`
- `apt install`
- `apt upgrade`
- `apt remove`

RHEL / Fedora examples:

- `dnf install`
- `dnf remove`
- `dnf update`
- `dnf search`
- `dnf info`
- `dnf list`

---

## Archiving and Compression

Examples:

- `tar`
- `tar -cvf`
- `tar -xvf`
- `tar -czvf`
- `tar -xzvf`
- `gzip`
- `gunzip`
- `zip`
- `unzip`

---

## Redirection and Pipelines

Examples:

- `>`
- `>>`
- `<`
- `|`
- `tee`

---

## System Control and Services

Examples:

- `poweroff`
- `reboot`
- `systemctl`
- `journalctl`

This category will grow as real coursework, labs, troubleshooting, and administration provide additional examples.

---

# 22. Fluency Missions

Advanced exercises should combine commands into realistic tasks.

These are not simply questions about individual commands.

They test whether the learner can sequence actions.

---

## Permission Denied Fix

Goal:

- inspect identity
- inspect permissions
- determine why access failed
- correct permissions
- verify success

---

## Locate + Extract + Save

Goal:

- locate information
- search for specific content
- extract matching information
- save the result

---

## System Stabilizer

Goal:

- identify a resource-heavy process
- inspect behavior
- reduce its impact or terminate it
- verify system stability

---

## Network Checkpoint

Goal:

- verify network configuration
- test reachability
- determine where communication fails

---

## Change + Prove

Goal:

- modify a configuration
- compare before and after
- verify the intended result

---

# 23. Command Chaining

Higher-level fluency should include command chaining and pipelines.

Example:

Task:

Create a directory named `test` and enter it.

Possible answer:

`mkdir test && cd test`

Pipelines and command chaining represent Linux sentence construction.

They should become more prominent after the learner develops sufficient command vocabulary.

---

# 24. Error Diagnosis

Linux administrators frequently encounter:

- incorrect commands
- wrong flags
- permission problems
- missing packages
- ownership issues
- failed services
- networking problems
- configuration mistakes

LinuxLingo should therefore treat troubleshooting as a core learning skill.

Error-diagnosis exercises may ask learners to:

- identify a mistake
- interpret an error
- provide a corrected command
- verify the repair

---

# 25. Session Architecture

An MVP training session may follow this flow:

1. Load `scenario_bank.json`
2. Select eligible drills
3. Present one drill
4. Accept user response
5. Validate or grade response
6. Record result
7. Provide feedback
8. Select the next drill
9. Continue until the selected session length ends
10. Display a summary

Possible session lengths may later include:

- 10 questions
- 20 questions
- 50 questions

Future versions may also support:

- multi-question blocks
- linked scenario sequences
- extended terminal missions

---

# 26. Mistake Review

Incorrect answers should become future learning material.

A review mode may display:

- original question
- learner answer
- correct answer
- explanation

Future versions may create a mistake queue.

Missed concepts can then return later in the same session or in future sessions.

---

# 27. Mastery System

LinuxLingo may track command mastery using stages such as:

## Learning

The learner has encountered the concept but has not demonstrated consistent recall.

## Practicing

The learner has answered correctly multiple times but still demonstrates occasional weakness.

## Mastered

The learner consistently recalls and applies the command correctly.

The exact scoring formula is not yet fixed.

Mastery should depend on evidence quality rather than simple raw correct-answer counts.

---

# 28. Category Mastery

Commands belong to categories such as:

- navigation
- filesystem
- permissions
- networking
- processes
- package management
- system information

LinuxLingo may eventually report category-level performance.

Examples:

- Navigation mastery
- Filesystem mastery
- Permissions mastery
- Networking mastery

This helps learners identify weak areas.

---

# 29. Readiness Target

LinuxLingo should eventually support an evidence-based readiness estimate.

A useful target is approximately:

**95% demonstrated readiness**

This should not simply mean 95% raw quiz accuracy.

Readiness may eventually consider:

- independent recall
- delayed recall
- practical execution
- ability to apply commands in new situations
- troubleshooting ability
- category coverage
- error patterns

The purpose is accurate operational confidence rather than false reassurance.

---

# 30. Streak System

Future versions may include daily practice streaks.

A streak may increase when the learner completes a qualifying training session.

The purpose is to reinforce consistent practice.

Streak mechanics are secondary to actual skill development.

LinuxLingo should not reward meaningless repetition merely to preserve a streak.

---

# 31. Command Bank Development Philosophy

The command bank is one of the most important parts of LinuxLingo.

The objective is not to build a large application with weak training content.

The objective is to build a structured, high-quality training corpus.

Commands should increasingly be harvested from:

- Linux coursework
- NOS labs
- system administration practice
- troubleshooting sessions
- certification study
- real command-line work

A single command can support multiple drills.

Example:

`lsblk`

Possible drill forms:

- recall the command
- explain what it does
- identify attached block devices
- interpret its output
- use it during a storage scenario
- diagnose a missing disk

This creates depth without artificially inflating the command count.

---

# 32. Command Bank Scale

Early MVP development may begin with approximately:

- 50 structured drills

A substantial first bank may contain:

- 80–120 drills

Later development may expand toward:

- 200–300 drills
- additional certification-specific packs
- larger specialized banks

The final size is not fixed.

Quality and meaningful variation matter more than an arbitrary total.

---

# 33. Development Strategy

Current development sequence:

1. Establish repository structure.
2. Preserve the existing Python MVP.
3. Create `scenario_bank.json`.
4. Seed the bank with real Linux commands.
5. Connect the JSON bank to the Python engine.
6. Implement reliable question selection.
7. Improve answer validation.
8. Add session scoring.
9. Add question-format variation.
10. Add state-based validation.
11. Add adaptive drill selection.
12. Add delayed retesting.
13. Add mistake review.
14. Add mastery tracking.
15. Add fluency missions.
16. Add extended multi-question scenarios.
17. Expand troubleshooting coverage.
18. Expand command coverage.
19. Consider additional interfaces only after the terminal-first engine is stable.

---

# 34. Current MVP Priority

The immediate priority is:

**build the command bank and connect it cleanly to the Python CLI engine.**

The project should resist premature complexity.

Do not become distracted by:

- visual polish
- mobile development
- web development
- elaborate infrastructure
- unnecessary architecture

before the underlying learning engine works.

---

# 35. Future Expansion

Possible future capabilities include:

- configurable practice sessions
- adaptive difficulty
- spaced repetition
- mistake queues
- mastery dashboards
- streak systems
- extended multi-question scenarios
- command-sequence missions
- certification-focused drill packs
- RHCSA-aligned practice
- system-state validation
- sandboxed Linux environments
- container-based labs
- automated repair simulations
- community command banks
- web interface
- desktop interface

These are future layers.

They are not requirements for the initial MVP.

---

# 36. Portfolio Value

LinuxLingo should function as a technical portfolio artifact demonstrating:

- Linux knowledge
- Python development
- CLI design
- JSON data architecture
- software organization
- troubleshooting logic
- adaptive learning-system design
- Git/GitHub workflow
- systems thinking

The repository should remain understandable enough that another developer, instructor, employer, or technical interviewer can examine the project and understand how it works.

---

# 37. Long-Term Vision

LinuxLingo may eventually become a broader interactive Linux training environment.

However, every future feature must support the same central purpose:

**building genuine command-line fluency through repeated command production, adaptive practice, and practical problem solving.**

The project should never lose that focus.

---

# 38. Design Motto

**Linux is not learned by reading.**

**Linux is learned by typing.**
