---
type: cycle
variant: standard
status: open
status_note: ""            # AT MOST a session id (e.g. "s01-3ce947"). NOT a summary.
                           # Detail belongs in the BODY (State / Still open / What shipped).
                           # Prose here is the same defect as prose in `status`, one field over.
title: "<imperative phrase — QUOTE it, an unquoted colon breaks YAML>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
description: ""            # one sentence, indexed by registries and dashboards
tags: []                   # lowercase; how a reader FILTERS for this later
---

# <title>

## Goal

<One sentence. What is TRUE when this is done? Not what you will do — what will be true.>

## Acceptance

<The falsifiable form of Goal. How does anyone else check it?
 If you cannot write a command or an observation here, the Goal is not yet a goal.>

- [ ]
- [ ]

## Spec

<What specifically gets built or changed.>

## Risks

<What could go wrong — and WHAT YOU WOULD SEE FIRST. A risk without a symptom is a worry.>

| risk | first symptom |
|---|---|
|  |  |

## Files

<Blast radius, named BEFORE touching anything. Surprises here are the finding.>

---
<!-- ── below this line is written at CLOSING ─────────────────────────────── -->

## What shipped

<What actually landed, with commits. If it diverged from Spec, say so here — divergence is
 information, not failure.>

## Decisions

<Choices made and WHY. Record the option you REJECTED and why — a decision without its
 alternative is a preference, and the rejected option is what stops the next person
 relitigating it.>

## Bugs caught

<Defects found while shipping this. An empty section here across a whole project means
 closing is being performed rather than done.>
