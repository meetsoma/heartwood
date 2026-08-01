---
name: close-a-cycle
type: muscle
description: "The closing sequence for a heartwood cycle: fill What shipped + Decisions, check the evidence bar (HOW verified, not THAT), pick closed vs parked vs superseded, flip status, check whether the parent arc's gate needs updating too."
triggers: [close, closing, ship, shipped, done, complete, finish, status, cycle, heartwood, park, parked, supersede, superseded]
tags: [heartwood, cycles, closing, evidence, status]
created: 2026-08-01
updated: 2026-08-01
---
<!-- SEAMS: (payload-relative — resolves inside soma/, works in any install)
            ← ../../skills/cycles/SKILL.md §4 (points here for the mechanical version)
            (outside the payload — spec lives in the repo, NOT the install. URLs only, never relative.)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/closing.md (the full reasoning this muscle mechanizes)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md (the spine sections this sequence fills) -->
<!-- UPDATE WHEN: spec/closing.md's required sections or status vocabulary changes -->

# Close a cycle

## TL;DR

Fill `What shipped` (with commits) and `Decisions` (with the option you rejected) — the only two
sections required to close, regardless of variant. Every sentence in the closed half must name
*how* it was verified, not just assert *that* it was. Then pick the real status: `closed` only if
`Acceptance` was actually met; `parked` if you stopped without finishing; `superseded` if something
else replaced it — and link that something else.

## The sequence

1. **`What shipped`** — commits, not descriptions. "Implemented the fix" is not an entry; `a1b2c3d
   — guard added to /api/admin/users` is. If the work diverged from `Spec`, say so here; divergence
   is information, not a confession.

2. **`Decisions`** — every real choice, and for each one, the option you rejected and why. A
   decision without its alternative is a preference — it gives the next reader nothing to push
   against if they'd have chosen differently.

3. **`Bugs caught`** — if the cycle turned up any defects while shipping, list them. Don't leave
   this empty by default: an empty `Bugs caught` on one cycle is unremarkable, but an empty
   `Bugs caught` on *every* cycle in a project is the cheapest available sign that closing has
   become a checkbox rather than a step (full reasoning:
   https://github.com/meetsoma/heartwood/blob/main/spec/closing.md , §3).

4. **Evidence-bar pass** — re-read everything just written in steps 1-3. For each factual sentence,
   ask: does it name a command, a count, a commit, a URL someone could re-check? If a sentence
   reads like "tested and working" with nothing to re-run, either add the how or mark it
   unverified. Don't let a hope through wearing a period.

5. **Pick the status** — one of:

   | status | when |
   |---|---|
   | `closed` | `Acceptance` was actually met; steps 1-4 are complete |
   | `parked` | work stopped before finishing, may resume later — say why, in `Decisions` or `status_note` |
   | `superseded` | different work replaced this cycle's Goal — link the replacement cycle in `Decisions` |

   If the honest status needs more than one word of explanation, put the explanation in
   `status_note`, not in `status` — keep `status` filterable.

6. **Update `updated:`** in frontmatter to today.

7. **Check the parent arc.** If this cycle lives inside an `arc-slug/`, closing it does not
   auto-flip the arc's own `cycle.md` phase-gate table — open it and update the row for this phase
   if the gate condition is now met.

## Anti-pattern this prevents

Flipping `status: closed` because the cycle is being *abandoned*, not because it's *finished*.
Once that status is set, an arc's phase table shows a green gate for work that never shipped, and
the record actively misleads the next reader. If you're not sure the Goal was met, it isn't — use
`parked` or `superseded` instead. Neither is a failure state; both are more honest than a false
`closed`.

## Related

- `../../skills/cycles/SKILL.md` — the full pick/scaffold/fill/close playbook this muscle is one
  step of (payload-relative)
- https://github.com/meetsoma/heartwood/blob/main/spec/closing.md — the full reasoning, the
  evidence-bar rule, and why `Bugs caught` matters as a corpus-level signal, not a per-cycle one
- https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md — the spine these three
  sections belong to, and the `status` controlled vocabulary

## Provenance

Derived from heartwood spec v0.1.0, `spec/closing.md` §7 (the closing checklist) —
https://github.com/meetsoma/heartwood .
