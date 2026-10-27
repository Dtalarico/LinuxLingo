# LinuxLingo — Documentation, Provenance, and Historical Continuity Policy

**Policy identifier:** LL-DOC-001
**Status:** APPROVED — 2026-10-27
**Project:** LinuxLingo
**Scope:** Repository documentation, design specifications, continuity records, scenario banks, implementation records, instructional evidence, and Git commits
**Authority:** Project author

## 1. Governing Principle

**The future must know what the past was thinking.**

LinuxLingo shall preserve not only what was built, taught, practiced, or verified, but also what was intended, understood, assumed, questioned, and decided at the time. The repository is both a software-development record and a historical account of how Linux command-line fluency is investigated, taught, and developed.

A future reader must be able to reconstruct the original objective, assumptions, constraints, alternatives, evidence, decisions, actions, outcomes, errors, corrections, uncertainties, and next steps. **Truth may evolve. History must not be silently erased.**

## 2. Human Readability — Write for the Author's Mother

Adopt Baby Cloud's standard: **Write so that an intelligent person without an engineering education can understand the work.**

Explain what happened, why it matters, how the relevant system operates, and what comes next. Expand unfamiliar acronyms, explain technical terms and operational purposes, identify relevant relationships and boundaries, and use concrete examples. Preserve precise technical language alongside plain-English explanations; neither substitutes for the other.

**Review test:** Could the author's mother follow the explanation without already knowing Linux?

## 3. Relationship to Existing Project Authorities

This policy supplements rather than replaces or diminishes the existing design and instructional framework.

- `README.md`: public-facing purpose, overview, and direction.
- `LINUXLINGO_MASTER_SPEC.md`: canonical instructional architecture, system boundaries, design principles, and long-term specification.
- `PROJECT_CONTINUITY.md`: durable operational handoff, current implementation state, decisions, and next work.
- `linuxlingo.py`: actually implemented Python application logic.
- `scenario_bank*.json`: training content, accepted textual answers, explanations, and drill provenance.
- `docs/documentation-policy.md`: historical-preservation, documentation, evidence, authorship, and continuity standards.

The Adaptive Infrastructure Tutoring Prompt is a related versioned *instructional* specification. Its operational rules must not be represented as LinuxLingo implementation merely because the design references them. Baby Cloud BC-DOC-001 is an originating source for the shared historical documentation philosophy.

If requirements appear to conflict, record the specific tension and obtain author clarification before modifying a governing specification.

## 4. Historical Intent and Decision Provenance

For material instructional, architectural, or implementation decisions, preserve as applicable: date; decision-maker; original intent and prior state; problem or constraint; initial assumptions and uncertainty; evidence available at the time; alternatives and trade-offs; decision rationale and authorization; consequences and dependencies; subsequent execution; verification; risks and outstanding questions; and links to earlier records.

Scale the amount of detail to the significance of the decision. Do not confuse a later revised decision with proof that the original decision was mistaken. Significant changes to teaching architecture, validation, source coverage, data structures, or implementation direction require durable reasoning.

## 5. Work-State Classification

Distinguish:

- **PROPOSED:** suggested, not authorized.
- **APPROVED:** specifically authorized, not necessarily performed.
- **EXECUTED:** action or modification actually performed.
- **VERIFIED:** result checked against explicit criteria with supporting evidence.

Not every activity needs the same formal sequence, but no record may imply stronger proof than exists. An approved feature is not implemented software; running without an exception does not verify all behavior; external grader approval does not independently establish Linux state; assisted reproduction does not prove independent mastery.

## 6. Historical Preservation and Explicit Corrections

Use an **append-only historical model of evolution**. Do not delete, silently replace, or rewrite historical intentions, decisions, observations, failures, and corrections merely to make the record cleaner.

Corrections shall identify the prior statement, its error or discrepancy, how the discrepancy was found, the corrected understanding, the kind of change involved (documentation, design, implementation, or verification), and links to evidence. Preserve the prior historical context. A documentation correction is not necessarily a design change; conflicting observations require analysis rather than erasure.

For a living current-state document, an explicitly authorized and traceable status update may be needed to prevent obsolete claims from masquerading as current facts. Preserve the earlier state through dated entries and Git history; do not silently revise historical entries. Stylistic cleanup is not authorization to rewrite records.

## 7. Operational Purpose Before Syntax

Preserve **operation before syntax** and **problem → reasoning → command → execution → verification**.

Before introducing unfamiliar operations, establish objective, purpose, prior knowledge, functional difference from known methods, expected behavior/output, and success criteria. When commands seem redundant, explain the actual mechanism that differs and when an administrator chooses each method. Teach the operation and relationship before expecting syntax memorization.

## 8. Atomic Semantics, System Boundaries, and Instructional Scope

**New concepts: expand first; familiar concepts: compress later.** Introduce one unfamiliar abstraction at a time when practical, before combining complex commands.

Differentiate user identity from shell environment; group membership from file ownership; path resolution from permissions; standard output from standard error; runtime service state from boot policy; command output from interactive completion; system behavior from grader bookkeeping. Where important, specify source, destination, direction, interface, layer, and state before/after.

Pipelines and composition are legitimate later skills, not excuses for concealing new semantics. Before assigning manual/reference reading, identify the exact needed information, relevant section, and sufficient stopping point.

## 9. Observable Results and Verification

Every teaching or operating procedure should expose appropriate starting state, action, expected changes, representative success/failure signatures, relevant output fields, misleading or ignorable text, verification method, and observable stopping condition. Explain commands that succeed silently.

For layered or partially successful outcomes, identify which steps succeeded, which warned/failed, what state remains, and how it can be verified. A verified user switch can coexist with a home-directory warning. Do not reduce such outcomes to an unsupported binary success/failure label.

**Verification instructions require identifiable verification methods.**

## 10. Evidence Integrity and Provenance

Distinguish **system-generated evidence** (real stdout/stderr, exit status, filesystem/process/configuration state), **human narration** (reported descriptions), and **external platform bookkeeping** (grader results, required recording steps, preferred command forms).

Manually writing `Permission denied` is not evidence that Linux produced that error. A grader rejecting a valid command does not prove Linux rejected it. A high score does not alone prove independence.

Record evidence source/date, command and context, expected and actual result, discrepancies, verification, warranted conclusion, and limits where relevant. Mark illustrative outputs as illustrative. Never invent tests, output, source coverage, execution, or mastery.

## 11. Instructional Failure Classification

Preserve distinct categories:

- **Retrieval failure:** taught material cannot be independently recalled or applied.
- **Coverage failure:** required knowledge has not been adequately introduced.
- **State-interpretation failure:** missing, ambiguous, or misleading telemetry prevents interpreting actual outcomes.

Use targeted delayed practice for retrieval failure, missing instruction for coverage failure, and explicit state observation/model repair for interpretation failure. A defective question or reasonable prior-model inference must not automatically count as learner incompetence.

## 12. Source Ingestion and Drill Provenance

Maintain **LAB → LEARN → HARVEST → COMMIT → MOVE ON**.

Harvest authentic coursework, labs, troubleshooting, or other properly identified sources. Preserve a drill's source/context, operational objective, expected behavior, valid alternatives, explanation, success/failure conditions, grading limitations, and relation to existing curriculum. Do not inflate counts or turn every quiz fact into a drill.

The existing Master Spec governs stable global IDs, numbered banks, and code/data separation. The current engine's normalized textual exact matching is a limitation, not a claim that all correct Linux solutions share one spelling.

## 13. Mastery Evidence and Learning History

Distinguish exposure, guided execution, recognition, independent command production, architectural reasoning, application in a new setting, troubleshooting, actual state verification, and delayed recall. Guessing, elimination, answer leakage, and immediate repetition are weaker evidence than unaided delayed performance. Preserve defective/contaminated question status; do not misreport a demonstrated answer as independently retrieved.

The Adaptive Infrastructure Tutoring Prompt remains authoritative for its own question cadence, scoring, state, and retesting rules; do not needlessly duplicate or change that protocol here.

## 14. Progressive Documentation Competence

The student is the intended author of the engineering record. Preserve the apprenticeship:

**assistant demonstrates → student and assistant co-write → student drafts and assistant critiques → student documents and verifies independently.**

AI-assisted historical records are valid when attributed; they do not prove unaided authorship. Progressively train documentation of objectives, starting state, reasoning, commands, real output, failures, troubleshooting, verification, lessons, uncertainties, and next steps. The assistant is a tutor, reviewer, and coach—not a permanent ghostwriter.

## 15. Implementation Truth and Future Design

Do not conflate vision with deployed software. At the October 27, 2026 review baseline, LinuxLingo's Python CLI loaded two JSON banks containing 171 drills (LL001–LL171), checked duplicate IDs, performed normalized textual answer matching, and provided basic feedback and scoring. It did **not** execute arbitrary entered commands or implement persistent learner models, adaptive selection, delayed retesting, or state-based validation.

This dated baseline is historical, not a permanently guaranteed current state. **`PROJECT_CONTINUITY.md` remains authoritative for the current implementation state and counts.** Planned features retain PROPOSED status until supported by implementation and verification evidence.

## 16. Git History and Change Management

Use forward-moving, intelligible Git commits, normally one coherent logical change per commit, with messages explaining the change. Preserve published history: do not force-push, rebase, or squash to conceal older records. Clearly link corrections to the prior state; distinguish policy, implementation, content additions, and unrelated cleanup. Verify changes and respect project-author approval before editing or committing.

Git history supports but does not alone guarantee historical understanding: human-readable dated reasoning must accompany important changes.

## 17. Cross-Project Principles and Boundaries

LinuxLingo develops terminal fluency through instructional design, retrieval, drills, feedback, and eventual adaptive verification. Baby Cloud develops integrated infrastructure through design, procurement, physical deployment, operations, and troubleshooting.

They share traceable evidence, historical continuity, transparent assistance, and growing independent competence. Cross-reference and transfer useful ideas with original attribution, but do not turn the repositories into identical systems or duplicate each other's entire methodology. An operational Baby Cloud experience may inform a drill; a LinuxLingo instructional insight may improve Baby Cloud commissioning.

## 18. Durable Continuity Across Work Sessions

Repositories are durable handoff records, **not copies of an assistant's private conversation memory**. Before substantive work, consult the README, continuity file, relevant Master Spec/policy sections, and actual task-specific source documents. An archival reading requires the entire requested tree, not only representative handoffs.

Recover last verified state, last decision, approved-but-unexecuted work, discrepancies, implementation limits, learning requirements, and next authorized action. Verify live state when it could have changed. Update continuity after material progress without erasing chronology or claiming unrecorded actions.

## 19. Privacy, Security, and Responsible Publication

Do not publish secrets, tokens, passwords, private credentials, sensitive identifiers, confidential records, or unnecessary personal details. Preserve useful provenance via redaction and safe references to privately retained evidence. State publicly visible verification limitations candidly.

## 20. Review and Acceptance Test

Before approving material documentation changes, ask:

1. Can a nontechnical reader understand what happened and why?
2. Are the original intent, assumptions, constraints, evidence, alternatives, and rationale traceable?
3. Are PROPOSED, APPROVED, EXECUTED, and VERIFIED separate?
4. Are real system evidence, human reports, and platform results distinct?
5. Are success, failure, partial success, uncertainty, and verification accurately represented?
6. Are mechanism and operational boundaries understandable?
7. Is learner reasoning and missing instruction preserved without misclassification?
8. Is assistance accurately attributed?
9. Are corrections linked without historical erasure?
10. Are existing implementation and future ambitions distinguishable?
11. Can another person resume the work without conversational memory?
12. Does the change respect both projects' distinct governing specifications?
13. Is the Git change coherent and reviewable?
14. Did the project author authorize the specific change?

Unmet criteria require correction or an explicit limitation, not invented certainty.

## 21. Policy Maintenance and Future Evolution

Before proposing a new policy revision, reread governing requirements; distinguish absent rules from failures to execute existing ones; recommend only the smallest durable necessary addition; avoid duplication; retain prior wording and history; obtain the author's authorization.

**An adequately specified rule must be executed, not repeatedly rewritten.**

## 22. Final Governing Standard

Document the development of understanding as carefully as the development of software. Successful software, successful instruction, and demonstrated independent competence are related but different claims. Preserve the reasoning, tests, failures, uncertainty, and corrections that formed each.

**The future must know what the past was thinking — and what the past actually proved.**

---

**Approved source lineage (2026-10-27):** Baby Cloud BC-DOC-001; LinuxLingo README, Master Spec, continuity, implementation, and scenario banks; Adaptive Infrastructure Tutoring Prompt v11 with preserved earlier modules.

**Implementation record:** See the dated 2026-10-27 addition to `PROJECT_CONTINUITY.md` for implementation evidence and exact Git commits.
