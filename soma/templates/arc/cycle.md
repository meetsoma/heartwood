---
type: arc
status: open
status_note: ""            # session id
title: "<arc name — QUOTE it if it contains a colon-space>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
description: ""            # one sentence
tags: []                   # lowercase filters
---

# <arc name>

## Why this arc exists

<What made this a body of work rather than a task. If you cannot say why these cycles belong
 together, you have a folder, not an arc.>

## Through-line

<The one sentence a reader needs to understand every cycle inside. This is the section that makes
 an arc an arc — a directory with members and no through-line is a folder pretending to be a
 grouping.>

## Phases

| # | phase | status | gate (done =) |
|---|---|---|---|
| 01 | [`01-<slug>`](01-<slug>/cycle.md) | open | a **checkable** condition, not a feeling |
| 02 | [`02-<slug>`](02-<slug>/cycle.md) | | |

**Ordinals are per-arc.** Two arcs may each have an `02`; that is fine. **Cite a phase by slug,
never by number** — a bare number identifies nothing once a second arc exists.

## Gates

<Falsifiable conditions for the arc as a whole. "Done = <command> exits 0", not "done = it works".>

> **Every gate must be falsifiable.** Ask *"what input would make this report failure?"* No answer
> means you wrote a decoration, not a gate.

## Members from other projects

| project | what | why it's here |
|---|---|---|
| `<project>@` | symlinked cycles | an arc spans projects **by symlink** — never by moving another project's cycle |

*(Delete if none. `cycles/<arc>/<project>@ -> ../../<project>/.soma/cycles`)*

> Moving a cycle out of its owning project breaks that project's record. A symlink lets an arc claim
> membership without taking custody.
>
> ⚠ **Only symlink if your tooling cannot see across trees.** If your registry already discovers every
> tree, a symlink buys nothing and costs two things: a census that double-counts (anything following
> links counts the target twice), and a duplicated group in any dashboard. One estate measured a
> **113-cycle (21%) inflation** from three of them and removed all three once its indexer was
> tree-aware. Delete this section if you have no foreign members.

## State

<Where this stands NOW. Update when a phase closes — a stale arc status is worse than none,
 because it is read as current.>
