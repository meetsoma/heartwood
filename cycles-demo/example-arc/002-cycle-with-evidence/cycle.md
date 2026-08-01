---
type: cycle
variant: audit
status: closed
title: "A cycle that accumulated evidence"
session: s01-8b4389
created: 2026-08-01
updated: 2026-08-01
---

# A cycle that accumulated evidence

## Goal

Show why a cycle is a DIRECTORY, not a file.

## Denominator

3 files in `notes/` — the complete set produced by this cycle, enumerated by `ls notes/`.

## Method

Everything this cycle generated lives in `notes/`, beside the record explaining it. As a flat
`cycle-2.md` those artifacts would have had nowhere to live, and would have drifted into some
unrelated folder — which is exactly what happened to five draft files in the corpus this format
was derived from. They sat in `plans/` for three months, disconnected from any record.

## Findings

A cycle directory costs nothing when empty and is the only thing that works when it isn't.

## What I could not measure

Whether authors keep evidence beside cycles once the directory exists, or revert to scattering it.
That needs a corpus older than this demo.

## Decisions

`variant: audit` here, to exercise a second variant in the fixture. **Rejected:** using `standard`
for everything, which would leave three of four variants untested by the fixture.
