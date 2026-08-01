---
type: closing-map
status: closed
status_note: ""            # session id
title: "<arc-slug> — closing map"
arc: <arc-slug>
created: YYYY-MM-DD
updated: YYYY-MM-DD
description: ""            # one sentence
tags: []                   # lowercase filters
---

# <arc-slug> — closing map

> **Delete this blockquote when you use the template.**
>
> Write this at each **phase transition**, not at "done" — that is what keeps it cheap, and an arc
> has more transitions than a cycle does.
>
> **Compression is for narrative, never for evidence.** Traps, commit hashes and measured numbers
> stay VERBATIM. Compress the story of how you got there; never the number that settles an argument.
> The story remains recoverable from this file's own git history, which is why cutting it is safe.

## MAP (closing state — <session>)

### What shipped

| # | what | commit | verified by |
|---|---|---|---|
| 01 | … | `<sha>` | `git log -1 <sha>` → subject matched · file X opened · command Y ran |

> ⛔ **"The status field said shipped" is NOT verification.** If you could not check it, write
> `unverified — status field only` and leave it. An honest unverified list is worth more than a
> confident wrong one.

### Decisions

| id | decision | why | ruled by |
|---|---|---|---|
| D1 | … | the reasoning, and **the option you rejected** — a decision without its alternative is a preference | <who> |

### Source of truth

| topic | lives at |
|---|---|
| … | `path/to/thing` |

> This table is what makes a closed record *useful* rather than merely complete. Without it a reader
> learns what happened and still cannot find where the thing now lives.

### Still open

| what | blocked on |
|---|---|
| … | a NAMED blocker, never "later" |

> Closing does not mean nothing is left. A record that cannot express residue will either lie or
> stay open forever.

### What could not be measured

<The honest-limits section. What you could not check, and what it would take to check it.
 An empty section here usually means the denominator was never stated.>

### Reconciled with today's understanding — PARENT TO COMPLETE

| open item | verdict now | why it changed |
|---|---|---|
| … | still valid / **obsolete** / **now cheap** / **now blocked** / **reveals a new thing** | … |

> ⛔ **This table cannot be delegated.** A scribe can compress what happened; only the parent can
> rule whether a still-open item is still worth doing — that requires knowing what changed
> *elsewhere* since, which is exactly the context a delegate does not have.

---

**Closed when:** this file exists **and no phase remains open.** That is the whole definition, and
it is checkable. Everything below this line is history — keep it or move it to `_archive/`.
