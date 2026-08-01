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

## Members from elsewhere

| member | where it lives | why it's here |
|---|---|---|
| `<slug>/` | moved in | related work, consolidated — one folder, one place to read |
| `<slug>` | left in place, `arc: <this-arc>` in its frontmatter | too many inbound refs to move cheaply, or a foreign estate |

*(Delete if none.)*

> **Prefer MOVING. Membership is a frontmatter fact, not a filesystem fact.**
>
> An arc claims a cycle with `arc: <slug>` in that cycle's frontmatter — the registry groups on it
> wherever the file sits. So the folder is for **humans**, and the only question a move has to answer
> is *what does it cost in referrer updates?* Measure inbound refs; under ~25, move it and fix the
> referrers; over that, leave it and declare `arc:`.
>
> ⛔ **Don't reach for a symlink.** It looks like consolidation and isn't: it gives a reader two
> places one cycle might be, while giving the indexer nothing it couldn't already discover by
> walking trees. One estate measured a **113-cycle (21%) inflation** from three of them, removed all
> three, and lost nothing. **The one exception** is a foreign estate whose record you must not take
> custody of (a client's tree, a repo you don't own) — then link it and **write the reason in this
> table**, because an unexplained link gets deleted.

## State

<Where this stands NOW. Update when a phase closes — a stale arc status is worse than none,
 because it is read as current.>
