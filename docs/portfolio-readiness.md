# LinuxLingo — Portfolio Readiness and Evidence Roadmap

**Established:** 2026-11-09  
**Status:** Author-directed portfolio-development goals; not employer-specific hiring requirements and not evidence of completed work.  
**Audience:** Linux / infrastructure hiring reviewers, especially potential Red Hat or Kyndryl interviewers.  
**Project identity:** LinuxLingo is a terminal-first, scenario-based Linux fluency trainer. It must solve an instructional problem, not become a documentation-only portfolio.

## Existing strengths and honest implementation boundary

The repository already contains an actual Python CLI prototype (`linuxlingo.py`) and JSON scenario banks (currently documented as **264 drills, LL001–LL264** in three banks as of November 8), as well as a detailed learning architecture, command-syntax teaching doctrine, provenance and dated engineering decisions.

The current source shows a simple interactive loop that loads configured JSON banks, asks random scenario questions, accepts textual answers, performs normalized string matching, displays pass/fail with optional explanation and keeps a session score. **It does not execute student-entered shell commands**, perform system-state validation, persist progress or implement the proposed adaptive learner model. More extensive written specifications are not evidence that these features exist.

A portfolio should let a reviewer run this actual MVP, see automated tests and learn from measured examples; it should not demand completion of every envisioned feature before the author applies for work.

## Priority portfolio milestones and acceptance evidence

### LL-P1 — Reproducible, verifiable MVP demo (highest near-term priority)
**Goal:** Make the existing CLI easy for a reviewer to run.

**Acceptance:** README with supported Python version, prerequisites and exact invocation; sample session with real nonsecret input/output; documented dependency expectations; reproducible example showing loading, scoring, wrong-answer feedback and graceful exit. Test on a clean supported environment and record the actual result/date. Avoid claiming a runtime test merely because code was inspected.

### LL-P2 — Automated loader and answer-validation tests
**Goal:** Demonstrate disciplined software verification rather than relying only on manual use.

**Acceptance:** Tests for multiple banks, unique identifiers, malformed records, absent/empty banks, expected normalization behavior, incorrect answers and safe non-execution of learner input. Add checks of corpus ID continuity/count and explain what deliberately remains unvalidated. Commit test source and observed pass/fail outputs; only report counts actually verified by execution.

### LL-P3 — Explicit assessment of accepted-answer limitations
**Goal:** Avoid teaching students to guess one brittle string when Linux permits equivalent valid operations.

**Acceptance:** Document concrete equivalent/non-equivalent command cases, safety boundaries and a staged design for better validation. Implement and test one narrow, safe improvement if useful; record alternative approaches and why they are accepted/rejected. Do not promise general semantic or live system-state checking until it exists. Reflect coverage-vs-retrieval distinction in test cases.

### LL-P4 — Guided-to-independent learning workflow
**Goal:** Make at least one complete learning workflow usable rather than only described in the master specification.

**Acceptance:** Reproducible lesson or scenario set demonstrating operation-before-syntax, argument-role scaffolding, meaningful feedback, explicit verification, and a later unaided retest where applicable. Clearly differentiate what is present in the CLI from instructional materials or human-led tutoring. Record real test observations rather than claiming measured learning gains without evaluation.

### LL-P5 — Maintained corpus and provenance
**Goal:** Prove the training data are coherent, reviewable and expandable.

**Acceptance:** Machine-readable schema and bank-count/ID checks; examples linking a drill to its source/goal, expected operation, constraints and explanation; maintain backward compatibility of existing drills. Distinguish content authored with assistance from independently validated correctness. Avoid committing private coursework/credentials.

### LL-P6 — Engineering-quality maintenance and failure recovery
**Goal:** Demonstrate maintainability and troubleshooting relevant to infrastructure work.

**Acceptance:** Small, reviewable Git changes; a short issue/failure-to-fix case study; executable tests with regression results; meaningful error messages; and a documented safe recovery strategy for malformed inputs or configuration. If practical, automate a non-destructive validation workflow in CI.

### LL-P7 — Hiring-manager demonstration package
**Goal:** Make the portfolio legible in minutes.

**Acceptance:** README links to a one-minute overview, quickstart, verified demo, test results, key instructional architecture and one or two engineering decisions; skills-to-evidence table; clear lists of implemented features versus aspirational architecture and authorship/assistance. Add **selective** version-controlled diagrams only if they improve comprehension.

## Optional later features — not hiring prerequisites

Full adaptive selection, mastery persistence, spaced repetition, live Linux sandbox, genuine system-state grading, UI and certification curriculum are future design goals, **not completed implementation claims**. They can become subsequent portfolio milestones after a useful, tested MVP.

## Operating and change rules

- Explicitly track **PROPOSED / APPROVED / EXECUTED / VERIFIED** with links to tests or genuine observations.
- Do not claim learner effectiveness from drill count alone or from one guided practice session.
- Preserve the existing Master Spec, prior decisions and documented command bank history; use additive status updates and small commits.
- Maintain only a few meaningful, source-versioned diagrams when needed, clearly labeled proposed versus implemented.
- Respect author approval before changing runtime behavior or training content.
- The milestones are a targeted evidence roadmap, **not a guarantee of a hiring outcome or a requirement to complete them all before applying**.
