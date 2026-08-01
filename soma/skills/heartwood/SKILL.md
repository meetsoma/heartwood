---
name: heartwood
description: |
  The work-record protocol — project/arc/cycle, four cycle variants, and what closing requires.
  Use whenever starting new work that deserves a record (pick a variant, scaffold from a template),
  or whenever marking existing work done, stopped, or replaced (close, park, or supersede a cycle).
  Trigger words: cycle, arc, closing, closed, parked, superseded, heartwood, "what shipped",
  "record this", "start a cycle".
version: 1.0.0
license: CC-BY-4.0
origin: heartwood spec v0.1.0
seeded-from: spec/README.md, spec/cycle-format.md, spec/closing.md
---
<!-- SEAMS: ← ../../../spec/README.md (the project/arc/cycle model)
            ← ../../../spec/cycle-format.md (the spine + four variants)
            ← ../../../spec/closing.md (what closed/parked/superseded require)
            ← ../../body/heartwood.md (the doorway body file — read that first if it's loaded)
            → ../../amps/muscles/close-a-cycle.md (the closing sequence this skill delegates to) -->
<!-- UPDATE WHEN: a new variant is added, the spine changes, or the closing rules change -->

# Heartwood — pick, scaffold, fill, close

You're opening or closing a piece of recorded work. This is the four-step playbook. It assumes the
spec is already read once (`../../../spec/README.md`, `../../../spec/cycle-format.md`,
`../../../spec/closing.md`) — this file is the procedure, not the reasoning behind it.

## 1. Pick the variant

Before scaffolding anything, decide what kind of work this is. Getting this wrong is the single
most common failure mode this spec exists to prevent — using `standard` for measurement work is why
audits end up without a denominator.

| if the work is... | variant | non-negotiable |
|---|---|---|
| building or shipping a thing | `standard` | — |
| two or more rival approaches, run in parallel | `branching` | `Convergence criteria` written **before** either branch starts |
| measuring something that already exists | `audit` | `Denominator` — the population + how you enumerated it |
| learning something that might get thrown away | `spike` | `Timebox` written at the start; `Keep or discard` answered explicitly |

If you're not sure: can you write a single falsifiable `Acceptance` line right now? If yes, it's a
cycle (pick the variant from the table). If the honest answer is "several different Acceptance
lines, for related reasons," it's an arc — go to §1a first.

### 1a. Does this need an arc?

Only if the work has a **through-line that will outlive any single cycle** — a reason several
related pieces of work belong together, not just one Goal. If so:

1. Create `arc-slug/` (no number — the slug is the identity).
2. Copy `../../../templates/arc/cycle.md` to `arc-slug/cycle.md` **first**, before any numbered
   phase. Write "Why this arc exists" before scaffolding a single phase — an empty through-line is
   the tell you started too early.
3. Then treat each phase as its own cycle: steps 2-4 below, inside `arc-slug/NNN-slug/`.

## 2. Scaffold

```bash
# standard cycle, no arc
cp ../../../templates/cycle/cycle.md <path>/NNN-slug/cycle.md

# a variant
cp ../../../templates/variants/<variant>/cycle.md <path>/NNN-slug/cycle.md

# an arc's own through-line file
cp ../../../templates/arc/cycle.md <arc-slug>/cycle.md
```

`<path>` is the project's cycle root (or `arc-slug/` if this phase belongs to an arc). `NNN` is the
next unused ordinal **in this arc or project** — per-tier, not global (spec/README.md §3). Never
cite the number alone once you leave this directory; cite the full `project/arc-slug/NNN-slug` path.

Immediately: **quote the title.** `title: Mood: clinical preset` is invalid YAML that renders blank
in every consumer instead of erroring — this defect went unnoticed for months in one real project.
`title: "Mood: clinical preset"` is correct.

## 3. Fill the open half

Required to open: `Goal` (one sentence — what will be TRUE, not what you'll do) and `Acceptance`
(the falsifiable form of Goal — a command or observation someone else can check). If you can't write
`Acceptance`, `Goal` isn't a goal yet; don't scaffold further until you can.

Everything else in the open half (`Spec`, `Risks`, `Files`, and the variant-specific sections)
earns its place — fill what's true, skip what isn't, don't pad.

## 4. Close

This is its own procedure — see `../../amps/muscles/close-a-cycle.md` for the mechanical sequence.
The short version: `What shipped` (with commits) and `Decisions` (including the option you rejected)
are required; every closed-half sentence must name **how** it was verified, not just assert that it
was (`spec/closing.md` §2); and the final status is `closed` only if `Acceptance` was actually met —
otherwise it's `parked` (stopped, may resume) or `superseded` (replaced — link the replacement).

If this cycle lives inside an arc, closing it doesn't auto-update the arc's own phase-gate table —
check whether `arc-slug/cycle.md` needs its gate flipped too.

## Traps

- 🔴 Unquoted title with a colon → silent blank render, not an error. Quote it.
- 🔴 `status` is a controlled set (`open | active | closed | parked | superseded`), not prose. Put
  narrative in `status_note`, not in `status` itself — one project reached 187 distinct status
  strings across 494 cycles by not following this.
- Cycle numbers are per-arc/per-project, not global — `"04"` appearing 5 times across one real
  estate is why bare-number citations are ambiguous outside their own directory.
- An arc directory with numbered phases and no root `cycle.md` is incomplete — scaffold the arc's
  own through-line first, not last.
