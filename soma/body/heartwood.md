---
type: content
name: heartwood
status: active
lazy: true
created: 2026-08-01
updated: 2026-08-01
description: "HEARTWOOD — the work-record protocol. Arcs, cycles, the four cycle variants, and what closing requires. Read BEFORE seeding, writing, or closing a cycle."
---

# Heartwood — the work record

**Installed via the heartwood payload.** This file is the doorway: it exists so the agent knows the
protocol is here and how to reach it, without loading the whole spec into every prompt.

## The model

```
project/ → arc/ → NNN-slug/cycle.md
```

An **arc** is a themed body of work with a stated through-line, holding **many** cycles. A **cycle**
is a directory — not a file — because cycles accumulate evidence (reports, audits, drafts) and that
evidence belongs beside the record explaining it.

## Before you write a cycle

**Pick the variant first.** Using `standard` for measurement work is why audits end up without a
denominator.

| variant | when |
|---|---|
| `standard` | build and ship a thing |
| `branching` | rival approaches in parallel — criteria written BEFORE the branches |
| `audit` | measure something that exists — denominator mandatory |
| `spike` | learn; may be discarded — timebox written at the start |

Scaffold from `templates/cycle/` or `templates/variants/<variant>/`.

## The two rules that carry most of the value

1. **Record the option you REJECTED.** A decision without its alternative is a preference. The
   rejected option is the only thing that stops the next person relitigating it.
2. **An audit states its denominator and how it enumerated.** "8 are broken" is unreadable;
   "8 of the 34 found by `grep -rln` over these 4 dirs" is checkable.

## Closing a cycle

Required: `What shipped` (with commits) and `Decisions`. Recommended: `Bugs caught`.

**A cycle with shipped work and a permanently empty `Bugs caught`, across a whole project, means
closing is being performed rather than done.** It is the cheapest signal that the record is real.

## Traps

- 🔴 **Quote any title containing a colon.** `title: Mood: clinical preset` is invalid YAML and
  renders **blank** in every consumer instead of erroring. Six cycles in one project carried this
  silently for months.
- 🔴 **`status` is a controlled set, not prose.** One project reached **187 distinct status values
  across 494 cycles, 156 used exactly once**, because the field was doing three jobs at once. Keep
  the state in `status`; put provenance in `status_note`.
- **Numbers are per-project IDs, not global ones.** They stay unique within a project and collide
  across an estate — do not treat `036` as an identifier outside its own tree.

## Full spec

The spec lives in the heartwood REPO, not in this installed payload — read it over the network:
https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md (the spine, the variants, and
the measured evidence each section rests on). Read it when authoring a variant or changing the
format; the doorway above is enough for routine use.

<!-- SEAMS: (outside the payload — URL only, never a relative path; this file installs standalone)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md -->
