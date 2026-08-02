---
type: cycle
variant: standard
status: open
status_note: ""            # session id
title: "<imperative phrase — QUOTE it, an unquoted colon breaks YAML>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
description: ""            # one sentence
tags: []                   # lowercase filters
---

# <title>

## Goal

<One sentence. What is TRUE when this is done? Not what you will do — what will be true.>

## Acceptance — gates

<The falsifiable form of Goal. If you cannot write a command here, the Goal is not a goal yet.

 Prefer the table: a gate is a COMMAND with a pass criterion and today's measured value, so
 drift is visible in both directions. Prose acceptance cannot be run, and an acceptance
 nobody can run is a wish.>

| # | gate | command | pass | now |
|---|---|---|---|---|
| G1 |  |  |  |  |
| G2 |  |  |  |  |

<Then answer, in one line: WHAT WOULD MAKE THESE GATES A LIE?
 A gate with no answer is decoration — it cannot fail, so its green means nothing.
 Common answers: it only sees valid input · it measures a stub, not the real path ·
 it asserts existence rather than operation · its denominator is silently reduced.>

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
