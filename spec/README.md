---
type: spec
name: heartwood-model
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# The model

> project → arc → cycle. Three tiers, one job each.

## The tree

```
project/
└── arc-slug/                  # a themed body of work — no number, stable identity
    ├── cycle.md                # the arc's OWN cycle — its through-line (see §4)
    ├── 01-first-cycle/
    │   └── cycle.md
    ├── 02-second-cycle/
    │   ├── cycle.md
    │   ├── report.md           # evidence accumulated while the cycle was open
    │   └── audit-findings.md
    └── 03-third-cycle/
        └── cycle.md
```

Three tiers, three different questions:

| tier | answers | identity | changes shape when |
|---|---|---|---|
| **project** | whose work is this | a name, stable forever | never — this is the container |
| **arc** | what through-line groups these efforts | a slug, stable forever | the theme itself changes |
| **cycle** | what specifically opened and closed | `NNN-slug`, per-arc ordinal | every time work starts or ends |

This document is about the top two tiers and the seam between them. The cycle itself — spine,
variants, frontmatter — is `cycle-format.md`. Read both; they're one model split for length.

## 1. Why an arc holds MANY cycles

The naive version of this model is `project/ → cycle/`, with no middle tier. It fails within a few
cycles, for a specific reason: **a theme and a chunk of work are different sizes**, and collapsing
them loses the thing that made grouping useful in the first place.

An arc is not a phase that happens to be a cycle. A phase is *one* thing you're building; an arc is
*why* you're building several related things over time. "Add admin authentication" is a cycle.
"Harden the auth surface after the PII leak" is an arc — it might contain the admin-auth cycle, a
rate-limiting cycle, an audit cycle that measures which endpoints are still unguarded, and a spike
that tests a different session model. None of those four is a phase of the others. They're siblings
under one through-line.

The test for whether something is an arc or a cycle: **does it have a Goal, or does it have a
reason several Goals exist?** A cycle answers "what is true when this is done." An arc answers "why
do these particular done-things belong together." If you can write a single falsifiable Acceptance
line, you have a cycle — write it as `NNN-slug/cycle.md`, not as an arc.

Collapsing the tiers has a specific, observable failure mode: cycles multiply under one project with
no grouping, and six months later nobody can answer "what body of work was this part of" without
re-reading commit messages. The arc tier exists so that question has a one-hop answer: open the
arc's `cycle.md` (§4) and read the through-line.

## 2. Why a cycle is a DIRECTORY, not a file

The templates in this repo (`templates/cycle/cycle.md`, `templates/variants/*/cycle.md`) are single
files, which makes the directory requirement easy to miss on first read. It matters as soon as a
cycle does real work, because real cycles **accumulate evidence** that a single markdown file has
nowhere to hold:

- an audit's `Findings` might be a 200-line grep dump too long to inline
- a branching cycle's rival approaches might each need a working draft
- a shipped feature might carry a screenshot, a benchmark output, a migration script that ran once

A cycle-as-file forces a choice between bloating the record with raw evidence (making it unreadable)
or discarding the evidence (making `What shipped` and `Findings` unverifiable — see `closing.md`
§2, the evidence bar). A cycle-as-directory has no such tradeoff: `cycle.md` stays the readable
record, and `report.md`, `audit-findings.md`, `draft-a/`, whatever the work actually produced, sits
next to it. The directory is not overhead — it is where the evidence bar gets satisfied.

This is also why a cycle is addressed by its directory, not its file: `02-second-cycle`, not
`02-second-cycle/cycle.md`. The file is the record; the directory is the cycle.

## 3. Numbering — per-project IDs, not global ones

Cycle numbers (`01-`, `02-`, `036-`) are **positions within one project's arc**, not identifiers.
They are guaranteed unique inside their own tree and guaranteed to collide outside it, and treating
them as if they carried meaning across trees produces exactly the confusion you'd expect.

Two measurements make this concrete:

- **One project, 38 shipped cycles:** only **36 distinct numbers** appeared. Two numbers were
  reused after an earlier cycle closed and its slot was recycled — proof that the number tracks
  *position in a sequence*, not a permanent identity, even within a single project.
- **One estate, 494 cycles across many projects:** `"04"` appeared **5 times**, `"01"` appeared
  **5 times**. Citing "cycle 04" without a project name doesn't narrow the estate down at all — it
  names five different pieces of work.

The consequence: **cite cycles by `project/arc-slug/NNN-slug`, never by number alone.** A cross-arc
reference, a session log, an inbox letter — anywhere a cycle gets named outside its own directory —
needs the full path or it has named nothing. This is the same failure shape `cycle-format.md`
documents for `status` (a field asked to do more than its one job); here the field is the ordinal,
and the extra job it can't do is "be a global ID."

## 4. The arc's own `cycle.md` is its through-line

`templates/arc/cycle.md` is not a template for one more numbered cycle — it lives at the arc's root,
sibling to the numbered phase directories, and it is the arc's entry point. Its job:

- state **why the arc exists** in terms the reader can act on (§ "Why this arc exists" in the
  template — three sentences, in the reader's terms, not the fixer's)
- list every phase with a **falsifiable gate**, not a status feeling
- carry the **through-line**: the mental model someone inherits by reading this one file and
  nothing else

An arc directory that has phases but no root `cycle.md` is a folder pretending to be a grouping —
it has the shape of an arc (a directory with numbered children) without the one thing that makes
grouping useful: a stated reason the children belong together. Anyone opening it has to reconstruct
the through-line from the phases themselves, which is exactly the work the arc tier exists to save.
Practically: **an arc that is just `mkdir arc-slug && mkdir arc-slug/01-foo` is incomplete.** The
first file in a new arc is its own `cycle.md`, before the first phase.

## 5. Reading this model in practice

Scaffolding order, top to bottom:

1. Decide if the work needs an arc (§1's test) or is a standalone cycle.
2. If an arc: copy `templates/arc/cycle.md` to `arc-slug/cycle.md` and write the through-line
   *first* — an empty through-line is the tell you scaffolded before you knew why.
3. For each piece of work: copy `templates/cycle/cycle.md` (or a variant from
   `templates/variants/`) into `arc-slug/NNN-slug/cycle.md`.
4. Reference the cycle by its full path everywhere outside its own directory (§3).
5. Close per `closing.md` — required sections, the evidence bar, and what "closed" is not allowed
   to mean.

## What this model is not

- **Not a task tracker.** A cycle records work that already has a falsifiable Goal; a kanban board
  or a TODO list is upstream of this, not replaced by it.
- **Not a wiki.** An arc's through-line is a decision record, not an evolving explainer — when the
  understanding changes enough to need a rewrite, that's usually a new arc, or a note in the old
  one's `Decisions` saying what superseded it.
- **Not a substitute for git history.** `What shipped` names commits; it doesn't duplicate diffs.
  The cycle is the *why* and the *evidence-that-it-happened*, not a second copy of the *what*.

## Related

- `cycle-format.md` — the spine, the four variants, and the frontmatter each cycle carries
- `closing.md` — what "closed" requires, and what it must not mean
- `templates/arc/cycle.md` — the arc through-line template referenced in §4
- `templates/cycle/cycle.md`, `templates/variants/*/cycle.md` — the cycle templates referenced in §5
