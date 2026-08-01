---
type: spec
name: heartwood-cycle-format
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# Cycle format

> One spine, four variants. The spine is not designed — it is what 38 real cycles converged on.

## Where this came from

The section vocabulary below was **measured, not invented**. Across 38 shipped cycles in one
project, sections occurred at these frequencies:

```
Decisions 16 · Goal 11 · What shipped 7 · Acceptance 6 · Spec 5
Bugs caught + fixed during shipping 5 · Risks 4 · Files 4 · Decisions (closing) 4
```

Nobody wrote that template first. It emerged, which is the strongest evidence a format is right —
and it is why this spec starts from usage rather than from taste.

## The spine

A cycle has an **open half** and a **closed half**. The open half is a claim about what will happen;
the closed half is evidence about what did.

| section | half | holds |
|---|---|---|
| **Goal** | open | one sentence. What is true when this is done? |
| **Spec** | open | what specifically gets built or changed |
| **Acceptance** | open | how anyone can check it — the falsifiable form of Goal |
| **Risks** | open | what could go wrong, and what you would see first |
| **Files** | open | the blast radius, named before you touch it |
| **What shipped** | closed | what actually landed, with commits |
| **Decisions** | closed | choices made and *why*, especially the rejected option |
| **Bugs caught** | closed | defects found while shipping this |

Only **Goal** and **Acceptance** are required to open a cycle. Only **What shipped** and
**Decisions** are required to close one. Everything else earns its place.

### Why `Bugs caught` matters more than it looks

It is the section nobody designs and everybody ends up writing. A cycle with shipped work and an
empty `Bugs caught` is not suspicious on its own — but across a project, *all* of them empty means
the closing step is being performed rather than done. It is the cheapest available signal that the
record reflects real work.

### Why `Decisions` outranks everything

It is the most-used section (16 of 38) because it is the only one that survives contact with the
future. `What shipped` is recoverable from git. `Decisions` \u2014 particularly **the option you
rejected and why** \u2014 exists nowhere else, and is precisely what the next person needs in order not
to relitigate it.

**Record the rejected option.** A decision without its alternative is a preference.

## Variants

Not all work is shipping work. A variant declares itself in frontmatter (`variant: branching`) and
adds sections to the spine; it never removes `Goal`.

| variant | when | adds |
|---|---|---|
| **standard** | build and ship a thing | (the spine) |
| **branching** | two or more rival approaches in parallel | `Branches` \u00b7 `Convergence criteria` \u00b7 `Verdict` |
| **audit** | measure something that already exists | `Denominator` \u00b7 `Method` \u00b7 `Findings` \u00b7 `What I could not measure` |
| **spike** | learn something; may be thrown away | `Question` \u00b7 `Timebox` \u00b7 `Answer` \u00b7 `Keep or discard` |

### branching

**Convergence criteria must be written before either branch begins.** A branching cycle whose
criteria appear after the branches is a justification, not an experiment. The `Verdict` is one of
*pick-one*, *synthesize*, or *both-keep* — and *both-keep* should be rare enough to require an
argument.

### audit

**`Denominator` is mandatory and comes first.** "8 writers are broken" is unreadable; "8 of the 34
writers found by `grep -rln` over these 4 directories" is checkable. An audit that does not state
how it enumerated has reported a vibe.

**`What I could not measure` is mandatory too.** A clean audit with no blind spots declared is
almost always an audit that did not look for them.

### spike

**`Timebox` is written at the start and honoured.** A spike that runs long has become a standard
cycle without anyone deciding to promote it. `Keep or discard` must be answered explicitly — an
unanswered spike leaves code in the tree that nobody owns.

## Frontmatter

```yaml
---
type: cycle
variant: standard          # standard | branching | audit | spike
status: open               # open | active | closed | parked | superseded
title: "Short imperative phrase"    # QUOTE it — an unquoted colon breaks YAML
created: 2026-08-01
updated: 2026-08-01
---
```

⚠️ **Quote any title containing a colon.** `title: Mood: clinical preset` is invalid YAML and will
render blank in every consumer rather than erroring. Six cycles in one project carried this defect
for months, invisible, because the tooling silently skipped what it could not parse.

## Status vocabulary

Statuses are a **controlled set**, not prose. One project accumulated **187 distinct status values
across 494 cycles, 156 of them used exactly once** — because the field was quietly doing three jobs:
state, provenance, and narrative.

Keep the state. Move the rest:

```yaml
status: closed
status_note: "auto-flipped s01-17d700 — report.md confirms completion"
```

A status of `shipped (auto-flipped s01-17d700 — report confirms)` is three fields in a trench coat,
and it makes the corpus unfilterable.
