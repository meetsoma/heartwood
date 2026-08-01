---
type: cycle
status: open
status_note: ""            # AT MOST a session id (e.g. "s01-3ce947"). NOT a summary.
                           # Detail belongs in the BODY (State / Still open / What shipped).
                           # Prose here is the same defect as prose in `status`, one field over.
title: "<phase title — QUOTE it if it contains a colon-space>"
arc: <arc-slug>                # which arc owns this phase
created: YYYY-MM-DD
updated: YYYY-MM-DD
depends_on: []                 # other phases or arcs — name the BLOCKER, never "later"
description: ""            # one sentence, indexed by registries and dashboards
tags: []                   # lowercase; how a reader FILTERS for this later
---

<!-- A phase is a cycle that belongs to an arc. It uses the cycle enum and the cycle spine;
     the ordinal lives in the DIRECTORY name (01-, 02-), never in frontmatter, so phases can be
     reordered without editing them. If a phase has no arc, it is just a cycle — use
     templates/cycle/ instead. -->

# <NN> — <phase title>

## Goal

<One sentence. What is TRUE when this phase alone is done — not what you will do.>

## DO

1. Concrete, ordered, each one checkable.
2. If a step cannot be checked, it is a decision to make, not a step to do — split it out.

## Gate (done =)

**One falsifiable condition.** Not "improved" — *"`<command>` exits 0"*, *"the live page serves X"*,
*"the running process holds the new value"*.

> Ask: **what input would make this report failure?** If nothing could, it is not a gate, it is
> decoration. And verify on the **executing path** — a file being correct is not the same as the
> process that reads it being correct.

## State

**Verified <date> by <how>:** …

Mark claims carried in from elsewhere `INHERITED` and give a one-command recheck beside them.
**Never carry a status field forward as if it were evidence** — a status is a claim someone made,
not a measurement someone took.

## Notes

Traps, watch-outs, and the measurements that justified a decision.

> **These survive compression verbatim when the arc closes.** The story of how you got here does
> not. Compression is for narrative, never for evidence.

<!-- SEAMS: <files this phase touches> -->
<!-- UPDATE WHEN: this phase closes, or its blocker clears -->
