---
type: arc
id: <arc-slug>                        # the SUBJECT. no number. stable — this is the identity.
status: "seeded — <one line: what state, what's next>"
project: meetsoma                     # WHOSE it is. the middle tier of project/arc/phase.
created: "YYYY-MM-DD (<soma>@<session-id>)"
updated: "YYYY-MM-DD (<soma>@<session-id> — what changed)"
tags: [<subject>, <domain>]
description: "One sentence a stranger could act on. Not 'improve X' — what changes, for whom."
seams: []                             # paths this arc touches; feeds `overlap` detection
edited_by: [s01-3ce947@meetsoma]
---

# <arc-slug> — <what it makes true>

> **Template.** Copy this directory: `cp -R cycles/_meta/cycle-template cycles/<arc-slug>`.
> Delete this blockquote. Rules: `body/cycles.md`. Closing: `cycles/_meta/CYCLE-CLOSING-MAP.md`.

## Why this arc exists

The problem in the reader's terms, not the fixer's. **What breaks, for whom, and what it costs.**
If you cannot say that in three sentences, the arc is not scoped yet — that is a finding, not a
failure. Write it down and stop.

## Phases

| # | Phase | Status | Gate (done =) |
|---|---|---|---|
| 01 | [`01-<slug>`](01-<slug>/cycle.md) | seeded | a **checkable** condition, not a feeling |
| 02 | [`02-<slug>`](02-<slug>/cycle.md) | blocked-on-01 | … |

**Ordinals are per-arc.** Two arcs may each have an `02`; that is fine. **Cite by slug, never by
number** — the old kind-folders had two `01`s, two `03`s and two `06`s, so a bare number identified
nothing.

**Every gate must be falsifiable.** *"What input would make this report failure?"* No answer means
you wrote a decoration, not a gate.

## Through-line

The mental model someone inherits by reading this and nothing else. **Why these phases are one thing
rather than several** — that is the entire justification for the arc existing as a folder.

## Members from other projects

| project | what | why it's here |
|---|---|---|
| `<project>@` | symlinked cycles | an arc spans projects **by symlink** — never by moving another project's cycle |

*(Delete if none. `cycles/<arc>/<project>@ -> ../../<project>/.soma/cycles`)*

## State

**Verified <date>:** what is actually true right now, and **how it was checked** — a command, a
commit, a file opened. Inherited claims get marked `INHERITED` plus their one-command recheck.

⚠ **A `status:` field is a claim, not evidence.** *"The status said shipped"* is not verification.

---

<!--
  ── WHEN THIS ARC CLOSES ────────────────────────────────────────────────────
  Collapse into `_completed.md` using cycles/_meta/CYCLE-CLOSING-MAP.md:

  ### What shipped        | # | what | commit | verified by |
  ### Decisions           | id | decision | why | ruled by |
  ### Source of truth     | topic | lives at |
  ### Still open          | what | blocked on |
  ### Reconciled with today's understanding — PARENT TO COMPLETE

  Do it at each PHASE transition, not at "done" — that is what makes it cheap.
  "Compression is for narrative, never for evidence": traps, hashes and measured
  numbers stay VERBATIM. An arc with a _completed.md and no open phases is closed.
-->

<!-- SEAMS: <the code/docs this arc governs> -->
<!-- UPDATE WHEN: a phase ships · the gate changes · a related cycle folds in -->
