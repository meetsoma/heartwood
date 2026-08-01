---
name: cycles
description: |
  Start, track and close work records — project / arc / cycle / phase, four cycle variants, and what
  closing actually requires. Implements the heartwood protocol (heartwood is the protocol's name;
  this skill is the thing you use).
  Use whenever starting work that deserves a record (pick a shape, scaffold from a template), while
  working (the record is where reasoning and decisions accumulate, not the context window), and when
  marking work done, stopped, or replaced (close, park, or supersede).
  Trigger words: cycle, arc, phase, closing, closed, parked, superseded, heartwood, "what shipped",
  "record this", "start a cycle", "close this out".
version: 1.0.0
license: CC-BY-4.0
origin: heartwood spec v0.1.0
seeded-from: "https://github.com/meetsoma/heartwood v0.1.0 — spec/README.md, spec/cycle-format.md, spec/closing.md (see Provenance below)"
---
<!-- SEAMS: (payload-relative — resolves inside soma/, works in any install)
            ← ../../body/heartwood.md (the doorway body file — read that first if it's loaded)
            → ../../amps/muscles/close-a-cycle.md (the closing sequence this skill delegates to)
            (outside the payload — spec lives in the repo, NOT the install. URLs only, never relative.)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/README.md (the project/arc/cycle model)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md (the spine + four variants)
            ← https://github.com/meetsoma/heartwood/blob/main/spec/closing.md (what closed/parked/superseded require) -->
<!-- UPDATE WHEN: a new variant is added, the spine changes, or the closing rules change -->

# Heartwood — pick, scaffold, fill, close

You're opening or closing a piece of recorded work. This is the four-step playbook. It assumes the
spec's reasoning is already known — read it once at
https://github.com/meetsoma/heartwood/blob/main/spec/README.md ,
https://github.com/meetsoma/heartwood/blob/main/spec/cycle-format.md , and
https://github.com/meetsoma/heartwood/blob/main/spec/closing.md if you can reach the network. If you
can't, or if this is all you have (a bare `/hub install heartwood`), the four steps below are
self-contained — this file is the procedure; the URLs are the *why*, not a dependency.

## 0. Decide what you are holding

Most mistakes here are made before any file is written, by scaffolding the wrong shape. Start here.

```
What do you have?
│
├─ an IDEA, no acceptance yet
│     → not a cycle. Write it where ideas live. A cycle with no stopping
│       condition can never close — it can only be abandoned.
│
├─ ONE piece of work
│     → templates/cycle/  (or a variant — §1)
│
├─ ONE piece of work that belongs to a larger body
│     → templates/phase/ inside <arc-slug>/NNN-slug/
│
├─ TWO OR MORE cycles on the same SUBJECT
│     → an arc. templates/arc/ + a phase per part.
│       ⚠ Same subject, NOT same kind. "audit" is how work was done;
│         nobody browses by it. Group by what it is ABOUT.
│
└─ work that is finished
      → §4. If it is an arc: templates/closed/_completed.md
```

### Do these loose cycles belong together?

**Detect by SHARED FILE REFERENCES, not shared words** — two cycles editing the same code are the
same subject regardless of vocabulary, and fuzzy text matching misses exactly that. If your host has
a registry, ask it (`soma-cycles-registry.py overlap`); otherwise grep the `Files` sections.

Then decide by **measured cost, never by feel**:

```
>=2 cycles on one subject?
├─ no  → leave it. A singleton is not an arc.
└─ yes → count LIVE refs to their paths (exclude sessions, preloads, archives)
         ├─ < ~25   → ASSEMBLE NOW, whatever their status. Cost is the constraint.
         ├─ >= ~25  → every phase complete?  yes → assemble (refs stopped growing)
         │                                    no  → declare the arc in frontmatter, assemble later
         └─ spans PROJECTS? → symlink the foreign member in. NEVER move another
                              project's cycle — it breaks that project's record.
```

🔑 **"Assemble on completion" is a proxy for cost, never a principle.** When cost is measured and
low, completeness is irrelevant. Measured once: 16 refs vs 192 — two orders of magnitude separate
the arcs that move from the one that waits, and it is one command to find out.

### Bringing an existing folder up to standard

Conforming an arc that predates this format is its own job, and it has one rule that is easy to skip:

> **Every fact you delete from a `status:` string must already exist in the body.** Check it as a
> diff, not by eye. A fact with no body home is not compression, it is deletion.

**Condense only what is CLOSED or SHIPPED.** A live cycle's working narrative is doing its job —
deleting it destroys the reasoning mid-flight. Normalise its frontmatter and leave the body alone.

## 0b. The frontmatter contract

The templates ship these fields bare, with no explanatory comments — **the rules live here, once.**
A comment inside a template is copied into every file scaffolded from it, so teaching in the template
means teaching duplicated across the whole corpus and drifting from this page.

| field | rule |
|---|---|
| `type` | `cycle` or `arc` |
| `status` | **ONE word** from `open · active · closed · shipped · parked · superseded` |
| `status_note` | **a session id and nothing else** (`"s01-3ce947"`). For a terminal cycle, the session that closed it |
| `title` | quoted — an unquoted colon breaks YAML |
| `arc` | the arc slug, if it belongs to one |
| `created` / `updated` | dates; `closed:` only when terminal |
| `depends_on` | name the **blocker**, never "later" |
| `description` | one sentence — registries and dashboards index this |
| `tags` | lowercase; how a reader **filters** for this later |

🔴 **`status_note` is not a summary.** Detail belongs in the BODY — `State`, `Still open`,
`What shipped`. **Prose in `status_note` is the same defect as prose in `status`, one field over.**

Measured on a real corpus: 26% of cycles carried a `status` longer than 25 characters, and the first
attempt to fix it simply moved the prose sideways — notes reached 293 characters. The field is a
machine state and a pointer; nothing else.

**Why one word matters:** a registry buckets on `status`. Free prose means a cycle reading
`active — phase 2 shipped` gets classified **Closed** because a substring matched, and no output ever
says so.

## 1. Pick the variant

Before scaffolding anything, decide what kind of work this is. Getting this wrong is the single
most common failure mode this spec exists to prevent — using `standard` for measurement work is why
audits end up without a denominator.

| if the work is... | variant | non-negotiable |
|---|---|---|
| building or shipping a thing | `standard` | — |
| two or more rival approaches, run in parallel | `branching` | `Convergence criteria` written **before** either branch starts |
| measuring something that already exists | `audit` | `Denominator` — the population + how you enumerated it |
| learning something that might get thrown away | `spike` | `Timebox` written at the start; `Keep or discard` answered explicitly |

If you're not sure: can you write a single falsifiable `Acceptance` line right now? If yes, it's a
cycle (pick the variant from the table). If the honest answer is "several different Acceptance
lines, for related reasons," it's an arc — go to §1a first.

### 1a. Does this need an arc?

Only if the work has a **through-line that will outlive any single cycle** — a reason several
related pieces of work belong together, not just one Goal. If so:

1. Create `arc-slug/` (no number — the slug is the identity).
2. Get `../../templates/arc/cycle.md` into `arc-slug/cycle.md` **first**, before any numbered phase.
   Write "Why this arc exists" before scaffolding a single phase — an empty through-line is the tell
   you started too early.
3. Then treat each phase as its own cycle: steps 2-4 below, inside `arc-slug/NNN-slug/`.

## 2. Scaffold

**The templates install with this payload** — they sit beside this skill at `templates/`, so
scaffolding is a local copy with no network and no clone required.

```bash
# paths are relative to the installed payload root (e.g. .soma/)
cp templates/cycle/cycle.md   <path>/NNN-slug/cycle.md              # standard cycle, no arc
cp templates/variants/<variant>/cycle.md <path>/NNN-slug/cycle.md   # audit | branching | spike
cp templates/arc/cycle.md     <arc-slug>/cycle.md                   # an arc's through-line file
cp templates/phase/cycle.md   <arc-slug>/NNN-slug/cycle.md          # a cycle that belongs to an arc
cp templates/closed/_completed.md <arc-slug>/_completed.md          # the arc's closing map
```

**Pick by shape, not by habit:**

| you are starting | use |
|---|---|
| one piece of work, no arc | `templates/cycle/` |
| a body of work with ordered parts | `templates/arc/`, then `templates/phase/` per part |
| measuring something that exists | `templates/variants/audit/` — denominator mandatory |
| rival approaches in parallel | `templates/variants/branching/` — criteria BEFORE the branches |
| learning, may be discarded | `templates/variants/spike/` — timebox at the start |
| closing an arc | `templates/closed/` — see §closing |

`<path>` is the project's cycle root (or `arc-slug/` if this phase belongs to an arc). `NNN` is the
next unused ordinal **in this arc or project** — per-tier, not global (the model's numbering rule:
https://github.com/meetsoma/heartwood/blob/main/spec/README.md , §3). Never cite the number alone
once you leave this directory; cite the full `project/arc-slug/NNN-slug` path.

Immediately: **quote the title.** `title: Mood: clinical preset` is invalid YAML that renders blank
in every consumer instead of erroring — this defect went unnoticed for months in one real project.
`title: "Mood: clinical preset"` is correct.

## 3. Fill the open half

Required to open: `Goal` (one sentence — what will be TRUE, not what you'll do) and `Acceptance`
(the falsifiable form of Goal — a command or observation someone else can check). If you can't write
`Acceptance`, `Goal` isn't a goal yet; don't scaffold further until you can.

Everything else in the open half (`Spec`, `Risks`, `Files`, and the variant-specific sections)
earns its place — fill what's true, skip what isn't, don't pad.

## 4. Close

This is its own procedure — see `../../amps/muscles/close-a-cycle.md` for the mechanical sequence.
The short version: `What shipped` (with commits) and `Decisions` (including the option you rejected)
are required; every closed-half sentence must name **how** it was verified, not just assert that it
was (full reasoning: https://github.com/meetsoma/heartwood/blob/main/spec/closing.md , §2); and the
final status is `closed` only if `Acceptance` was actually met — otherwise it's `parked` (stopped,
may resume) or `superseded` (replaced — link the replacement).

If this cycle lives inside an arc, closing it doesn't auto-update the arc's own phase-gate table —
check whether `arc-slug/cycle.md` needs its gate flipped too.

## Traps

- 🔴 Unquoted title with a colon → silent blank render, not an error. Quote it.
- 🔴 `status` is a controlled set (`open | active | closed | parked | superseded`), not prose. Put
  narrative in `status_note`, not in `status` itself — one project reached 187 distinct status
  strings across 494 cycles by not following this.
- Cycle numbers are per-arc/per-project, not global — `"04"` appearing 5 times across one real
  estate is why bare-number citations are ambiguous outside their own directory.
- An arc directory with numbered phases and no root `cycle.md` is incomplete — scaffold the arc's
  own through-line first, not last.

## Provenance

This playbook is derived from the heartwood spec v0.1.0 —
https://github.com/meetsoma/heartwood — specifically `spec/README.md` (the project/arc/cycle
model), `spec/cycle-format.md` (the spine, measured against 38 shipped cycles in a real project,
not designed from taste), and `spec/closing.md` (what closing requires). This file is the
agent-facing procedure; the spec is the reasoning it compresses.
