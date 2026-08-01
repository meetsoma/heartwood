---
type: spec
name: heartwood-closing
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# Closing

> What "closed" is allowed to mean, what it requires, and the three states people conflate:
> closed, parked, superseded.

A cycle opens with a claim (`Goal`, `Acceptance` — see `cycle-format.md`). Closing is where that
claim gets settled against reality. This document is about the settling, not the building — it
assumes the open half of the spine already exists and is about what has to be true before you flip
`status: closed`.

## 1. What's required

Two sections, no exceptions, regardless of variant:

- **`What shipped`** — with commits. Not "implemented the feature" — the commit hashes that did it.
  If work diverged from `Spec`, that divergence is recorded here; it's information, not a confession.
- **`Decisions`** — choices made and *why*, with the option you rejected. `cycle-format.md` already
  makes the case for why this is the highest-value section in the whole spine (16 of 38 measured
  cycles used it, more than any other); closing is where it gets written, because the rejected
  option is usually only visible in hindsight.

`Bugs caught` is recommended, not required — §3 covers why it earns a place anyway.

Nothing else in the closed half is mandatory. A cycle with `What shipped` and `Decisions` and
nothing else is a complete, honest record. A cycle with five decorative closed-half headings and no
commits in `What shipped` is not — see §4.

## 2. The evidence bar: HOW, not THAT

A closing claim has to name **how** it was verified, not just assert **that** it was. This is the
same rule Trait 9 states for gates in general (`amps/muscles` in the consuming agent, if it has
one): a check that can't fail isn't a check, and a closing note that can't be disputed isn't
evidence.

Compare:

> ❌ "Tested and working."

> ✅ "Ran the regression suite (`pytest tests/auth/ -v`, 34/34 pass); manually drove the login flow
> in a browser against the staging admin panel and confirmed the 403 on an unauthenticated request
> (commit `a1b2c3d`)."

The first is a claim about a claim. The second names a command, a count, and an artifact someone
else could re-run or re-open. `What shipped` entries should read like the second — cite the commit,
name the check, state the count. If you can't name how you verified something, you verified nothing
and the entry should say "not verified" rather than imply it was.

This generalizes past `What shipped`: any sentence in the closed half that describes a state of the
world ("the leak is fixed," "all endpoints are guarded now") needs its verification named in the
same breath, or it's a hope wearing a period.

## 3. `Bugs caught` as a realness signal

`cycle-format.md` already states the individual-cycle case: an empty `Bugs caught` on one cycle
isn't suspicious — some work genuinely ships clean. The signal is at the corpus level, not the
cycle level.

Across a whole project, if **every** closed cycle has an empty `Bugs caught`, that's not evidence of
unusually clean work — it's evidence the closing step is being performed rather than done. Real
shipping work turns up something: an edge case, a typo in a check, a wrong assumption caught before
it landed. A corpus with zero recorded defects across dozens of cycles is a corpus where closing has
become a checkbox, not a step.

This is why `Bugs caught` earns a place in the required-adjacent tier even though no single instance
of it is mandatory: **it's the cheapest available signal, read in aggregate, for whether closing
notes reflect real work.** If you're auditing a project's cycle corpus and want one number to start
with, count the empty `Bugs caught` fields as a fraction of closed cycles.

## 4. The anti-pattern: closed while abandoned

The failure this spec exists to prevent: a cycle's `status` says `closed`, and the work it describes
is not finished — it was stopped, and "closed" was used because there was no other word for "I'm not
touching this again." That single overloaded status then lies to everyone downstream: an arc's phase
table shows a green gate for work that never shipped, and nobody re-opens it because the record says
it's done.

Heartwood keeps three distinct closed-adjacent states specifically so "I stopped" is never forced to
say "I finished":

| status | means | requires |
|---|---|---|
| **closed** | the Goal was met. Work is finished. | `What shipped` + `Decisions`, evidence bar met (§2) |
| **shipped** | closed, AND it reached the world — public repo, live site, published package. Usually the last cycle in an arc. | everything `closed` requires, plus a pointer to the live thing (URL, tag, package) |
| **parked** | deliberately stopped, not finished, may resume. | a one-line reason it stopped, in `Decisions` or a `status_note` |
| **superseded** | replaced by different work; this cycle's Goal is no longer the plan. | a link to the cycle that replaced it |

**`parked` is not a failure state.** Priorities shift; a cycle two-thirds done that loses its reason
to continue is honestly `parked`, not `closed`. What makes it honest is that `parked` doesn't claim
`What shipped` matches `Acceptance` — it just says work stopped, and (ideally) why.

**`superseded` must link the replacement.** A superseded cycle without a pointer to what replaced it
is indistinguishable from one that was simply dropped — the whole value of the status is that
someone lands here and knows where to look next. Put the link in `Decisions`:

```
Superseded by 04-rate-limiting/cycle.md — the session-model spike (03) showed the fix belonged
one layer down, in the rate limiter, not in this cycle's auth-token approach.
```

## 5. Frontmatter for the closed-adjacent states

Same controlled vocabulary `cycle-format.md` defines for `status` — no new values invented here,
just the three used at close time:

```yaml
status: closed        # Goal met, What shipped + Decisions present, evidence bar met
status: shipped        # closed AND live — name where (URL, tag, package). Default to `closed` if unsure.
status: parked         # stopped, not finished, may resume — see Decisions for why
status: superseded     # replaced — Decisions links the replacement
```

If a status needs more than one word to explain, that's what `status_note` is for — the same escape
hatch `cycle-format.md` gives the general case, so `status` stays filterable and the story goes
somewhere that doesn't corrupt it:

```yaml
status: closed
status_note: "verified against staging, commit a1b2c3d — see What shipped"
```

## 6. Worked example

A cycle whose `Acceptance` was "every `/api/admin/*` route rejects unauthenticated requests." Two
drafts of the same `What shipped` entry — the first fails the evidence bar (§2), the second passes
it:

> ❌ **Draft 1:** "Added the auth guard to the admin routes. Tested it, works fine now."

> ✅ **Draft 2:** "Guard added in `a1b2c3d`, applied to all 6 routes under `/api/admin/*` (enumerated
> via `grep -rl 'admin' src/routes/`). Regression test added in the same commit
> (`tests/admin-auth.spec.ts`, 6 cases, one per route) — all fail-closed on a missing token. Manually
> confirmed a 403 against staging for an unauthenticated `GET /api/admin/users`."

Draft 1 is unfalsifiable — there's nothing in it a skeptical reader could go check. Draft 2 gives
three independent things to re-verify: a commit, a test file with a count, and a manual repro
against a real environment. Same underlying work; only the second is evidence.

This is also where `Decisions` earns its keep on the same cycle — the entry might continue:

> Rejected a per-route decorator approach in favor of one router-level middleware — decorators
> would've required touching all 6 route files individually and risked a 7th route being added
> later without one. Middleware fails closed by default; a new route has to opt OUT, not in.

That sentence is the one nothing else in the repo will ever recreate. The commits are in git
regardless; the reasoning for the rejected decorator approach exists nowhere else.

## 7. Closing checklist

In order:

1. Fill `What shipped` — commits, and any divergence from `Spec`.
2. Fill `Decisions` — including the rejected option.
3. Fill `Bugs caught` if there were any (§3 — don't leave it empty out of habit).
4. Check the evidence bar (§2) on every closed-half sentence: does it name *how*, not just *that*?
5. Pick the real status: `closed` only if `Acceptance` is actually met. Otherwise `parked` (stopped,
   may resume) or `superseded` (replaced — link it).
6. Update `updated:` in frontmatter.
7. If this cycle lives inside an arc, check whether the arc's own `cycle.md` phase table (see
   `README.md` §4) needs its gate flipped too — closing a cycle doesn't auto-update its arc.

## Related

- `README.md` — the project/arc/cycle model this closing procedure operates inside
- `cycle-format.md` — the spine (`What shipped`, `Decisions`, `Bugs caught`) and the `status`
  controlled vocabulary this document extends with `parked` / `superseded` usage rules
- `../soma/amps/muscles/close-a-cycle.md` — the agent-facing procedural version of §7
