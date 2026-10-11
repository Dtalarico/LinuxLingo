# RHCSA Independent Practice Lab — Design Record
**Date:** 2026-10-11
**Status:** FUTURE DESIGN; not yet implemented or assessed.
**Related:** LINUXLINGO_MASTER_SPEC.md, PROJECT_CONTINUITY.md, Adaptive Infrastructure Tutoring Prompt v10.

## Purpose
Bridge the gap between recognizing Linux commands in study questions and independently administering a working system. Preserve this plan now without interrupting the current NOS-120 Chapter 4 midterm study.

## Existing resources
- Learner already has a working local RHEL 10 virtual machine and free Red Hat Developer subscription.
- Learner is watching Sander van Vugt RHCSA instruction; use it to identify topics, then perform tasks independently.
- Cisco/NDG Linux Essentials can supply optional introductory hands-on reinforcement.
- Red Hat Interactive Labs are a general product-specific catalog, **not** the missing comprehensive RHCSA lab curriculum. Avoid recommending unrelated product demos or AI-assisted command line tools as an RHCSA substitute.
- Main practice environment: learner's own dedicated, non-production RHEL VM, with clean snapshots.
- Confirm contemporary RHCSA EX200 objectives and target OS version from Red Hat before finalizing scope.

## Study priority
**Present:** Continue NOS-120 Chapter 4 20-question blocks and course midterm. Source weighting remains review questions → flashcards → summary → discovery → hands-on → ancillary, without dropping chapter-wide scope.
**Future:** Complement classroom learning with independent RHCSA practical tickets and consistent delayed retesting.
**Target:** June 2027 readiness is a planning objective, not a promise of passing or a guaranteed date.
**Cadence:** Aim for an additional hour of practice a day when sustainable; adjust during exam weeks.

## Learning and practice modes
1. **DO → SEE → NAME → REMEMBER (guided):** Complete command, realistic expected output, precise command/option/argument meanings, verification. Count as instruction, not independent performance.
2. **Assisted repetition:** Learner executes a related task with changed inputs and optional hints. Record assistance.
3. **Independent trouble ticket:** Provide desired final state, baseline and constraints *without command solution*. Learner selects commands and works in RHEL 10.
4. **Verification and troubleshooting:** Learner provides genuine terminal evidence of system state; test function, permissions, and persistence as relevant; allow local manuals and built-in help.
5. **Delayed varied retest:** Fresh scenario days later; no hints until requested. Record retention and ability to transfer understanding.

Workflow: **TASK → PLAN → EXECUTE → OBSERVE → VERIFY → DOCUMENT → RESET/RETEST.**

### Example ticket (no answer provided)
Create `confidential.txt` and configure it so the owner can read and write, owning group can read, and others have no permission. Verify file type, mode, owner and group with real terminal evidence. Do not pre-supply commands in independent mode.

## Practice ticket / engineering notebook schema
- Ticket ID/date; source and official exam objective
- Domain (filesystem, permissions, users/groups, services, SELinux, networking, partitions/LVM, packages, boot, etc.)
- Prerequisites, baseline VM state, snapshot/checkpoint
- Desired end state and constraints
- Learner command transcript
- Actual terminal output and observed state (not invented or typed descriptions)
- Verification command(s) and result; reboot/persistence test when relevant
- Hints/assistance requested; errors and repair steps
- Evidence classification: independent / assisted / instructional / failed / unclear / environment failure
- Weakness, coverage, next spaced-retest target
- Safe cleanup/reset actions and lessons learned

## Safety/operations
- Use a dedicated non-production RHEL 10 VM. Protect graded coursework VMs, host disks and irreplaceable data.
- Make clean snapshots before risky operations, particularly partitioning, storage, boot and network changes.
- Never store passwords, tokens, student records or other secrets in the public repository.
- Do not automatically execute untrusted learner commands or equate a syntactically accepted answer with verified system state.
- Permit independent use of installed `man` pages and built-in command help, consistent with actual exam restrictions; avoid unauthorized outside assistance in a simulated exam.

## Mastery and assessment
Keep distinct: coverage gap, immediate post-teaching recall, assisted completion, independently verified operation, delayed independent retention, cross-scenario transfer, and environmental failures. The 95% target applies to **demonstrated coverage and skill**, not merely multiple-choice accuracy. RHCSA readiness requires independently solving representative objective-mapped tickets within time limits, handling errors, and validating reboot persistence when applicable.

## Implementation path (not started)
1. Validate VM/snapshots and current RHCSA objectives.
2. Create a minimal first ticket bank from already-covered NOS-120 concepts; avoid duplicating every quiz as a lab.
3. Maintain the engineering notebook and evidence ledger.
4. Test and refine ticket format after a few supervised sessions.
5. Later map all RHCSA objective families to independent and timed practice tickets.
6. If LinuxLingo software gains safe state validation, keep it isolated/sandboxed and separate from the current text-answer MVP.

## Relationship to repository
This is an **additive planning document**, not an implementation claim. It does not change LinuxLingo's current Python/JSON engine, scenario IDs, source material priority, or prior master specification. Preserve this document as the starting point for future RHCSA lab development.