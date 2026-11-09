# LinuxLingo

**A terminal-first Python trainer for Linux command-line fluency through scenarios, active recall, and practical troubleshooting.**

**Author:** David M. Talarico  
**Last documented project status:** November 9, 2026  
**Implementation:** Working-source Python CLI MVP and three JSON scenario banks  
**Current documented corpus:** 264 drills (LL001–LL264; 100 + 100 + 64), according to the November 8 engineering records  
**Next portfolio priority:** Reproducible CLI demonstration and automated tests

> **Learning principle:** Linux should be learned like a language: commands as vocabulary, flags as grammar, pipelines as composition, and real terminal tasks as conversation.

## What currently exists

| Component / capability | Implemented or documented status |
|---|---|
| `linuxlingo.py` | Python command-line application that loads the configured JSON scenario banks, presents random practice prompts, accepts typed answers and tracks a session score |
| Scenario banks | Three numbered JSON banks, documented as 264 drills in the latest dated harvest |
| Basic feedback | Whitespace-normalized string matching against accepted answers; PASS / FAIL and an expected-answer example, with explanation when supplied |
| Duplicate-ID protection | Loader rejects duplicate IDs across valid loaded drills |
| Safe command handling | Learner-entered command text is compared as text; the MVP does **not** execute arbitrary learner commands |
| Automated test suite / verified clean-install demo | **Not yet demonstrated in the repository** |
| Persistent mastery, adaptive scheduling, delayed retests | **Proposed, not implemented in the current CLI** |
| Actual Linux system-state validation / sandbox | **Proposed, not implemented** |

**Evidence boundary:** These implementation descriptions come from inspection of tracked source and dated documentation. A clean-machine execution or automated test suite was **not performed** as part of the November 9 documentation reorganization. The documented count should be validated by the planned corpus tests before it becomes a fresh independently verified test result.

## The problem and design approach

Many Linux learning experiences reward recognizing or reproducing command strings without checking whether a learner understands the underlying operation, environment, expected state change, or troubleshooting process.

LinuxLingo's approach is **problem → reasoning → command → execution → verification**, with a strict distinction between **coverage failure** (the concept was not actually taught) and **retrieval failure** (it was taught but cannot yet be recalled). The current CLI implements a limited typed-response drill engine; the broader instructional system is specified for future development.

See the [canonical Master Specification](LINUXLINGO_MASTER_SPEC.md) for the full educational model, Skate Shell compositional teaching analogy, source-ingestion doctrine, validation philosophy, and planned progression.

## Running the current prototype

The main program is [`linuxlingo.py`](linuxlingo.py), with three configured JSON sources:

- [`scenario_bank.json`](scenario_bank.json)
- [`scenario_bank_2.json`](scenario_bank_2.json)
- [`scenario_bank_3.json`](scenario_bank_3.json)

From a local checkout with an appropriate Python 3 interpreter:

```sh
python linuxlingo.py
```

The program loads available configured banks, selects prompts, evaluates typed text answers, displays a running session score, and accepts `exit` to quit. It uses Python standard-library modules; no third-party Python import is visible in the current entry-point script. **A clean-environment compatibility check, exact supported Python version, and reproducible test run are upcoming evidence goals**, not established guarantees.

## Next development and verification milestones

The near-term goal is to make the actual MVP easy for a hiring manager or Linux practitioner to **run, inspect, and verify**, then improve it carefully.

1. **LL-P1 — Reproducible demo:** Supported environment, repeatable sample session, real output and documented failure/exit behavior.
2. **LL-P2 — Automated tests:** Scenario-bank integrity and ID checks, loader failure cases, whitespace/answer comparison, and non-execution boundary.
3. **LL-P3 — Validation improvements:** Evaluate safe equivalence rules rather than overfitting correct Linux operations to one accepted text string.
4. **LL-P4 — Guided-to-independent workflow:** Demonstrate a real supported learning sequence with explicit feedback and evidence of what was actually tested.
5. **LL-P5–LL-P7 — Corpus provenance, maintenance, and reviewer demonstration:** Evidence-linked content checks, regression tests, clear technical decisions and a concise portfolio narrative.

The complete acceptance criteria and honest statuses are in [Portfolio Readiness and Evidence Roadmap](docs/portfolio-readiness.md). Completing every envisioned future feature is **not** a prerequisite to using the existing project as a portfolio artifact.

## Architecture and documentation

The existing MVP separates **Python application logic** from **JSON learning content**. Additional tutoring, adaptive learning, state-verification and advanced question types remain architecture/design subjects until implemented.

Use **selective, version-controlled diagrams** (e.g., editable SVG or Mermaid) when they materially clarify the program, scenario flow or validation system—not a diagram for every command or historical discussion. See [documentation policy](docs/documentation-policy.md). No new diagram is claimed to have been created by the README reorganization.

| Reader wants to know | Where to go next |
|---|---|
| Current state, milestones, handoff, and dated development evidence | [Project Continuity](PROJECT_CONTINUITY.md) |
| Intended learning architecture, teaching method and design choices | [LinuxLingo Master Specification](LINUXLINGO_MASTER_SPEC.md) |
| Existing application behavior | [Python CLI source](linuxlingo.py) |
| Actual practice content | [Three scenario banks](scenario_bank.json) and the numbered follow-on banks linked above |
| Required proof for a professional portfolio | [Portfolio readiness roadmap](docs/portfolio-readiness.md) |
| Documentation, diagram and evidence standards | [Documentation policy](docs/documentation-policy.md) |
| Guided lab and certification learning references | [Guided Linux Practice Resources](GUIDED_LINUX_PRACTICE_RESOURCES.md) |
| Complete earlier README with development chronology | [README historical archive](README-HISTORY.md) |

## Development and evidence principles

- **LAB → LEARN → HARVEST → COMMIT → MOVE ON:** Real Linux tasks inform practice content, but source content is not proof of independent mastery.
- Preserve original decisions, failed attempts and revisions in dated project records. Distinguish **PROPOSED / APPROVED / EXECUTED / VERIFIED**.
- State clearly which capabilities are in running code versus specifications, tutoring assistance, external labs or future aspirations.
- Keep the README **current-first and brief**; store chronological detail in the Master Spec, continuity and appropriately indexed archives.
- Link actual tests, reproducible examples and small, useful diagrams when available. Never invent passing test results.

## Historical preservation

The [entire pre-reorganization README](README-HISTORY.md) is preserved intact, along with existing Master Spec and continuity entries and Git history. Readers can find the original chronology without navigating through it before reaching the current software.
