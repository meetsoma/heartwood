---
type: spec
name: heartwood-cycle-format
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# Cycle format

> One spine, four variants. The spine is not designed — it is what 38 real cycles converged on.

## Where this came from

The section vocabulary below was **measured, not invented**. Across 38 shipped cycles in one
project, sections occurred at these frequencies:

```
Decisions 16 · Goal 11 · What shipped 7 · Acceptance 6 · Spec 5
Bugs caught + fixed during shipping 5 · Risks 4 · Files 4 · Decisions (closing) 4
```

Nobody wrote that template first. It emerged, which is the strongest evidence a format is right —
and it is why this spec starts from usage rather than from taste.

## The spine

A cycle has an **open half** and a **closed half**. The open half is a claim about what will happen;
the closed half is evidence about what did.

| section | half | holds |
|---|---|---|
| **Goal** | open | one sentence. What is true when this is done? |
| **Spec** | open | what specifically gets built or changed |
| **Acceptance** | open | how anyone can check it — the falsifiable form of Goal |
| **Risks** | open | what could go wrong, and what you would see first |
| **Files** | open | the blast radius, named before you touch it |
| **What shipped** | closed | what actually landed, with commits |
| **Decisions** | closed | choices made and *why*, especially the rejected option |
| **Bugs caught** | closed | defects found while shipping this |

Only **Goal** and **Acceptance** are required to open a cycle. Only **What shipped** and
**Decisions** are required to close one. Everything else earns its place.

### Acceptance is a GATE, not a sentence

`Acceptance` is the only section whose job is to be *run*. Measured across a 616-cycle corpus:
**109 cycles carry an Acceptance and only 25 of those contain anything runnable** — so the section
most responsible for falsifiability is prose four times out of five.

A gate is a **command**, a **pass criterion**, and **today's measured value**:

```
| # | gate                  | command                        | pass  | now |
|---|-----------------------|--------------------------------|-------|-----|
| G1| no orphaned records   | `bin/check-orphans --count`    | 0     | 12  |
| G2| import stays under 2s | `time bin/import fixtures/`    | <2.0s | 3.4s|
```

Recording `now` is what makes it a gate rather than a wish: drift becomes visible in both
directions, and a gate that was green and went red is a signal instead of a surprise.

**Then answer one question: what would make this gate a lie?** A gate with no answer cannot fail,
and a check that cannot fail is decoration. The recurring answers are worth knowing:

- it only ever sees valid input (needs a negative control)
- it measures a stub or a file, not the executing path
- it asserts *existence* where it should assert *operation*
- its denominator was silently reduced, so a clean result means "not measured"

A uniformly extreme result — everything passing, everything failing — is a broken-probe signature,
not a finding.

### Why `Bugs caught` matters more than it looks

It is the section nobody designs and everybody ends up writing. A cycle with shipped work and an
empty `Bugs caught` is not suspicious on its own — but across a project, *all* of them empty means
the closing step is being performed rather than done. It is the cheapest available signal that the
record reflects real work.

### Why `Decisions` outranks everything

It is the most-used section (16 of 38) because it is the only one that survives contact with the
future. `What shipped` is recoverable from git. `Decisions` — particularly **the option you
rejected and why** — exists nowhere else, and is precisely what the next person needs in order not
to relitigate it.

**Record the rejected option.** A decision without its alternative is a preference.

## Variants

Not all work is shipping work. A variant declares itself in frontmatter (`variant: branching`) and
adds sections to the spine; it never removes `Goal`.

| variant | maturity | when | adds |
|---|---|---|---|
| **standard** | **stable** — 38 real instances | build and ship a thing | (the spine) |
| **branching** | ⚠ **speculative** — 1 instance, spec does NOT match it | two or more rival approaches in parallel | `Branches` · `Convergence criteria` · `Verdict` |
| **audit** | ⚠ **speculative** — **zero** instances | measure something that already exists | `Denominator` · `Method` · `Findings` · `What I could not measure` |
| **spike** | ⚠ **speculative** — zero instances | learn something; may be thrown away | `Question` · `Timebox` · `Answer` · `Keep or discard` |

> 🔴 **Only `standard` is evidenced.** A corpus review across three real trees (s01-8b4389) found
> exactly one branching cycle in the wild, and **none of the three sections specced here match what
> it wrote** — the shape was invented around a single case. `audit` and `spike` have zero instances.
>
> They are kept because the distinctions are argued below and cost nothing to ignore, but **do not
> treat them as validated.** Presenting four equal variants when three are untested is exactly the
> confident-and-wrong rendering this format warns about. Promote a variant when real cycles use it,
> not when the reasoning sounds good.

### branching

**Convergence criteria must be written before either branch begins.** A branching cycle whose
criteria appear after the branches is a justification, not an experiment. The `Verdict` is one of
*pick-one*, *synthesize*, or *both-keep* — and *both-keep* should be rare enough to require an
argument.

### audit

**`Denominator` is mandatory and comes first.** "8 writers are broken" is unreadable; "8 of the 34
writers found by `grep -rln` over these 4 directories" is checkable. An audit that does not state
how it enumerated has reported a vibe.

**`What I could not measure` is mandatory too.** A clean audit with no blind spots declared is
almost always an audit that did not look for them.

### spike

**`Timebox` is written at the start and honoured.** A spike that runs long has become a standard
cycle without anyone deciding to promote it. `Keep or discard` must be answered explicitly — an
unanswered spike leaves code in the tree that nobody owns.

## Frontmatter

```yaml
---
type: cycle
variant: standard          # standard | branching | audit | spike
status: open               # open | active | closed | shipped | parked | superseded
title: "Short imperative phrase"    # QUOTE it — an unquoted colon breaks YAML
created: 2026-08-01
updated: 2026-08-01
---
```

⚠️ **Quote a value containing `: ` (colon followed by SPACE).** `title: Mood: clinical preset` is
invalid YAML and renders blank in every consumer rather than erroring.

**The narrow rule is the useful one.** `title: soma:meta scaffolding caps` parses fine — a colon
with no space after it is legal. An earlier draft of this spec said "any colon", which is wrong and
would flag valid documents; an over-broad rule gets ignored wholesale, taking the real one with it.
*(Correction from a corpus review, s01-8b4389.)*

Evidence: 6 cycle.md files in one project were unparseable on this exact pattern, found by parsing
38 of them  [measured]. They had gone unnoticed because the old layout named files `cycle-N.md`, so
no validator ever scanned them — **that duration is inference, not measurement**, and the files were
fixed in the same session, so the original count can no longer be re-confirmed from current state.

## Status vocabulary

Statuses are a **controlled set**, not prose. One project accumulated **187 distinct status values
across 494 cycles, 156 of them used exactly once** — because the field was quietly doing three jobs:
state, provenance, and narrative.

Keep the state. Move the rest:

```yaml
status: closed
status_note: "auto-flipped s01-17d700 — report.md confirms completion"
```

A status of `shipped (auto-flipped s01-17d700 — report confirms)` is three fields in a trench coat,
and it makes the corpus unfilterable.

### Two terminal states: `closed` and `shipped`

**`closed` describes the record. `shipped` says it also reached the world.** Both are terminal and
the closing agent chooses — `closed` is the default; `shipped` is for work that went live: a public
repo, a deployed site, a published package. In practice `shipped` is most often the LAST cycle in an
arc, because that is the one that ships the arc.

**Why not one word.** Only one of the four variants actually ships. An `audit` produces findings and
merges nothing. A `spike` is often discarded on purpose — that is a successful spike. A `branching`
cycle converges on a decision. Forcing `shipped` onto those asserts a release that never happened.
But forcing `closed` onto a production release throws away the one distinction a reader most wants:
**did this reach anyone?**

**Choosing:** if a stranger could see the result, it `shipped`. Otherwise it `closed`.

<!-- CORRECTED s01-593a6d (Curtis). This section previously argued FOR a single terminal state and
     against `shipped` entirely. That was right about audits and spikes and wrong about releases.
     Measured cause: across 262 real cycles `shipped` appears 39 times and `closed` 7 — the corpus
     had already made this distinction and the spec was erasing it. -->

This is the same seam the rest of the spec runs on: heartwood specifies the ARTIFACT, a workflow
protocol specifies the PROCESS.

**Interop with PHASE.** [PHASE](https://github.com/curtismercier/protocols) uses
`queued | active | shipped | parked | superseded` for its phase folders — the same five-state shape,
tracking the work rather than the record. Hosts running both map:

| heartwood (the record) | PHASE (the work) | |
|---|---|---|
| `open` | `queued` | the only true divergence — different word, same state |
| `active` | `active` | |
| `shipped` | `shipped` | identical meaning in both |
| `closed` | `shipped` | ⚠ **lossy** — PHASE has no word for *finished, never released* |
| `parked` | `parked` | |
| `superseded` | `superseded` | |

With `shipped` adopted, heartwood is a SUPERSET of PHASE's terminal vocabulary. **The mapping is
lossy in exactly one direction:** heartwood → PHASE collapses `closed` and `shipped` onto
`shipped`, so a round-trip through PHASE cannot recover the distinction. That is a property of
PHASE's vocabulary, not a defect in either — but a host that round-trips must keep `status_note`
or it will silently promote an audit into a release. Neither is a fork of the other.

<!-- CORRECTED s01-d1fa77: this table still had FIVE rows after 83cad3f added a sixth state, and
     mapped heartwood `closed` -> PHASE `shipped` with no row for heartwood's own `shipped` — so
     the spec's own interop table contradicted the enum three sections above it. Found by
     re-deriving the row count against the enum rather than reading the table. The prose already
     said "superset"; the table hadn't caught up. -->

---

## Gap analysis against a live 221-cycle corpus (s01-8b4389)

The spine above came from one project. Measuring a second, larger corpus (221 cycles, agent-run,
18 repos) shows what a single-project sample missed. Field usage there:

```
session 60% · depends_on 35% · spans_repos 34% · parent_cycle 29% · purpose 27% · tags 18%
```

### ADOPT — three additions

**1. `session` — provenance.** 60% usage, the most-used field after the basics. For agent-run work
this is not decoration: it records WHICH SELF made a claim, and a claim whose author is unknown
cannot be weighed. Any spec for agent projects that cannot answer "who wrote this" has a hole.

```yaml
session: s01-8b4389        # optional, but expected wherever an agent authored the cycle
```

**2. Rendering is an OPTIONAL projection.** A conforming `cycle.md` is renderable by any
PRISM-conformant viewer with no changes — frontmatter plus `##` headings is enough. Adding
`<!-- @section: name -->` anchors is optional and unlocks *surgical editing* (rewrite one section
without touching the file). **Neither is required.** Stating this costs nothing and prevents hosts
inventing incompatible render conventions.

**3. A validator contract.** A conforming tool MUST check, at minimum:

| check | why it exists |
|---|---|
| frontmatter parses as YAML | six cycles in one project were silently unreadable for months |
| `type: cycle` present | otherwise the document is invisible to discovery |
| `status` is in the declared set | one corpus reached 187 distinct values, 156 used once |
| `title` quoted if it contains `:` | the exact cause of the six unreadable files |

A validator that warns instead of failing is a validator nobody runs.

### DECLINE — two deliberate exclusions

**`spans_repos` / `depends_on` / `parent_cycle`** are real and used (34/35/29%), but they exist
because that corpus spans 18 repos. Speccing them would imply heartwood requires an estate.
**Hosts may add fields**; these are documented as a known extension, not part of the core.

**The process loop** (ground → decide → plan → build → verify → consolidate → reflect) belongs to a
workflow protocol, not here. **Heartwood specifies the ARTIFACT; a workflow protocol specifies the
PROCESS.** Merging them turns a format into a methodology, and methodologies get ignored where
formats get adopted.

### One honest note

In that corpus `updated` appears on only **19%** of cycles — while the spec above requires it. The
spec is ahead of the practice there, not behind it, and that gap is the direct cause of frontmatter
dates disagreeing with git history at scale.

---

## Corpus review (sibling, s01-8b4389)

> Method: read the gap analysis above, then read 20+ real cycle files across all four available
> corpora — `meetsoma/.soma/cycles` + `meetsoma/.soma/releases/cycles` (221 files, glob-verified),
> `personal/tincture-css/.soma/cycles` (39 files, the spine's own source), `personal/prism/.soma/
> cycles/001-renderer-spike` (the only branching example), and all 12 sibling protocol READMEs in
> `personal/protocols/` (not the 3 the premises admit to). Every count below is a literal grep/glob
> over those trees, re-run at review time — not inherited from the gap analysis. File paths cited
> throughout.

**Headline: the gap analysis measured FRONTMATTER FIELDS on the 221-cycle corpus and never checked
whether the CONTENT SPINE survived there. It did not.** Re-running the section-heading count that
produced “Decisions 16 · Goal 11 · …” against the 221-cycle corpus instead of the 39-cycle one:

```
Goal 21/221 (10%) · Acceptance 9/221 (4%) · Spec 0/221 (0%) · Risks 0/221 (0%)
Files 0/221 (0%) · What shipped 0/221 (0%) · Decisions 0/221 (0%) · Bugs caught 0/221 (0%)
```

Six of eight spine sections have **zero** literal instances in 221 real cycle files. This is not an
arc-vs-phase artifact — verified: only 12 of the 221 are arc-roots (a directory whose `cycle.md` has
numbered `cycle.md` children); the other **209 (95%) are standalone leaf cycles**, exactly the shape
the spine is written for. The spine, as literal heading text, essentially does not exist in the
corpus the gap analysis examined. It exists almost entirely in the 39-cycle corpus it was measured
from (`personal/tincture-css/.soma/cycles/**/cycle.md`, re-verified: Decisions 16, Goal 11, What
shipped 7, Spec 5, Bugs caught+fixed 5, Acceptance 5–7 depending on how `## Acceptance test` /
`## Spec/Acceptance — all checked` variants are counted, Risks 4, Files 4, Decisions (closing) 4 —
your numbers, independently reproduced). **The spine is real. It just hasn't ported to the second
project the gap analysis itself was run against, and nothing in the gap analysis noticed, because it
never read a document — only frontmatter keys.**

### Q1 — does the spine survive contact? Which sections carry weight vs. were promoted from noise?

Read in full: `edit-tool-resilience/cycle.md`, `shell-injection-hardening/cycle.md`,
`infra/003-soma-repo-topology/cycle.md`, `infra/ecosystem-identity/cycle.md` (all in
`meetsoma/.soma/`), plus `releases/cycles/meta/orchestration/cycle.md`, and
`substrate-foundation/001-foundation-light-dark-surface/cycle.md` +
`substrate-foundation/002-surface-untangle-theme-flavor/cycle.md` (both in
`personal/tincture-css/.soma/cycles/`).

- **Where the spine WAS used (tincture), it carries real weight, not decoration.** Cycle 002's
  `## Risks` names three specific, later-relevant failure modes (form-control dark-mode styling,
  Tailwind `@theme` interaction, a localStorage migration path) and `## Files` lists five concrete
  file paths with NEW/MODIFY/POSSIBLY-MODIFY qualifiers. Neither reads as filled-in-because-required.
- **But `Risks` and `Files` are correlated, not independently earned.** `grep -l '^## Risks$'` and
  `grep -l '^## Files$'` return the **exact same four files**
  (`substrate-foundation/002-.../cycle.md`, `substrate-foundation/003-.../cycle.md`,
  `registry-codegen/004-.../cycle.md`, `registry-codegen/005-.../cycle.md`) — cycles 2–5 of 39, all
  from the project's first week. **Cycles 6–37 (34 of 39) never use either section again.** The
  frequency table presents `Risks: 4` and `Files: 4` with the same visual weight as `Decisions
  (closing): 4`, but the latter recurs sporadically across the whole project while the former two are
  one early habit that got dropped, used together, never apart. Real weight when present; thin
  evidentiary basis for calling them part of a stable spine rather than a phase-1 experiment. (The
  spec already marks them optional — “everything else earns its place” — so this isn't a
  contradiction, but the table's uniform row styling oversells four correlated, time-clustered uses
  as equal in kind to sections used throughout a project's life.)
- **Real cycles reach for headings the spine doesn't name, constantly, and some are clearly load-
  bearing.** `edit-tool-resilience/cycle.md` uses `## SHIPPED` (not “What shipped”), `## Diagnosis
  verdict`, `## Candidate directions`, `## Provenance / routing caveat`. `shell-injection-hardening/
  cycle.md` uses `## Findings` (a table, closer to the `audit` variant's `Denominator`/`Findings`
  shape than to `standard`) and `## Decision Register` instead of `## Decisions`. `infra/003-…/
  cycle.md` uses `## DO` as its only real content heading, structured as an action list, not a closed-
  half record at all — because it's `status: seeded`, i.e. never shipped. None of these are noise;
  they're semantically equivalent to spine sections under different names, which the gap analysis's
  exact-string heading count would silently miss on both sides (undercounting spine adoption **and**
  overcounting spine absence).
- **A whole class of `cycle.md` files aren't cycles in the spec's sense at all.** `releases/cycles/
  meta/orchestration/cycle.md`: `type: cycle`, `status: living`, opening line **“This isn't a work
  cycle. It doesn't ship and close.”** It is PHASE's §9 meta-orchestration rhythm
  (`personal/protocols/phase/README.md` §9) wearing a `cycle.md` filename. A validator built from
  this spec's conformance rules (frontmatter parses, `status` in the declared set, etc.) would flag
  this file as broken — `living` isn't in `open | active | closed | parked | superseded` — when it is
  working exactly as designed, just not as a heartwood cycle. See §“Does heartwood already exist”
  below; this is the sharpest instance of that question.

**Verdict:** Goal, Decisions, What-shipped survive contact (used throughout a project's life, under
varying spellings, real content). Acceptance and Spec survive more weakly (present but thin, and
often merged: `## Spec / Acceptance — all checked` appears 4× in tincture as one heading, not two).
Risks, Files, Bugs-caught are real but far rarer and, for the first two, historically clustered — not
wrong to keep, wrong to present as equally canonical.

### Q2 — branching: does prism 001 match the specced shape, or was a shape invented around one case?

Read in full: `personal/prism/.soma/cycles/001-renderer-spike/cycle.md`, `branching-cycle.md`,
`branch-a/README.md`, `branch-b/README.md`, `phase-4/convergence.md`.

**A shape was invented. None of the three added sections (`Branches`, `Convergence criteria`,
`Verdict`) appears as a literal heading anywhere in the one real instance.**

- `cycle.md` (the cycle root) uses: `Trigger`, `Context`, `Phases`, `Decisions locked`, `Decisions to
  surface (convergence criteria — answer at Phase 4)` — “convergence criteria” exists only as a
  parenthetical inside a differently-named heading — `Future direction`, `Out of scope`, `Out-take`.
- `branch-a/README.md` and `branch-b/README.md` (the actual `Branches`) each use: `Hypothesis`,
  `Scope`, `Phases log`, `Planned artifacts`, `Known risks`. There is no cycle-root `## Branches`
  section listing them — the branches ARE separate files, addressed by frontmatter `companion:
  [./branch-a/README.md, ./branch-b/README.md]`, not summarized inline.
- The resolution — what heartwood specs as `## Verdict` — is not a heading in `cycle.md` at all. It's
  a **separate `type: decision` document** (`phase-4/convergence.md`) with sections `Context`,
  `Options`, `Decision`, `Consequences`, `Alternatives considered` — an ADR shape, richer than a
  pick-one/synthesize/both-keep line, including a per-criterion scoring table and a numbered list of
  9 follow-ups with evidence.
- **A required guardrail is missing from the spec entirely.** `branching-cycle.md` §5.1 (the
  methodology doc this was presumably drawn from) names an explicit, falsifiable **Hypothesis**,
  stated per branch before work starts, as one of three anti-motivated-reasoning guardrails — and it
  was actually used (`## Hypothesis` in both branch READMEs, and `convergence.md`'s decision text:
  “This was the hypothesis stated up front — explicitly to be falsified, not confirmed”). Heartwood's
  three added sections have no Hypothesis field. Convergence criteria without a stated hypothesis is
  half the anti-bias mechanism the source methodology actually depends on.
- **Even `branching-cycle.md`'s own prescription didn't match what happened.** Its §6 says the
  resolution “belongs in the cycle root, in a section called `resolution`.” The real resolution
  is not a `## resolution` heading in the cycle root — it's the separate decision document described
  above. Three different shapes exist for the same thing: heartwood's spec, the methodology doc's own
  spec, and what actually got written. All three disagree.

**Verdict: yes, invented.** Recommend either (a) mark `branching` `status: speculative` distinct from
the other three variants until a second instance exists (branching-cycle.md §7 already says this:
“want 3+ [validated uses] before publishing as a protocol spec” — heartwood has 1 and specs it
anyway), or (b) replace the three sections with what was actually used: `Hypothesis` (per branch, not
cycle-root), and point the resolution at a **linked decision document** rather than an inline
`Verdict` heading — closer to what closing.md already does for `superseded` (link the replacement).

### Q3 — does `audit` have a real example anywhere?

Searched all three corpora for `variant: audit` or a literal `## Denominator` heading: **zero real
matches.** `grep -rl` across `meetsoma/.soma/{cycles,releases/cycles}`,
`personal/tincture-css/.soma/cycles`, and `personal/prism/.soma/cycles` returns nothing. (One
unrelated file matched — `meetsoma/.soma/releases/cycles/child-parent-comms/team-s01-dcd604/
SIB-1-child-H-0.5.2-coverage.md` — a coverage report, not a cycle, using “Denominator” in its own
unrelated sense.)

The only `variant: audit` file that exists anywhere in reach is
`meetsoma/repos/heartwood/cycles-demo/example-arc/002-cycle-with-evidence/cycle.md` — **inside this
repo**, `created: 2026-08-01` (today), `session: s01-8b4389` (this review's own session hash). It is a
self-authored illustration, not field evidence. It should not be read as a second data point; it's
the same author demonstrating the shape they specced, same day.

**Verdict: confirmed zero real instances. Per your own instruction — “a variant with zero instances
may be speculation and should be marked draft rather than specified” — `audit` should carry that
mark.** `Denominator` and `What I could not measure` are well-argued in the abstract (and I don't
disagree with the reasoning), but nothing in three real corpora has tested whether they're the right
two fields, or whether real audits reach for something else, the way `shell-injection-hardening/
cycle.md`'s `## Findings` table did instead.

### Q4 — where does the spec CONTRADICT the corpora, not just exceed them?

**Status vocabulary is the clearest contradiction, not a stricter-than-practice gap.** Spec's
controlled set: `open | active | closed | parked | superseded`. Measured across all 221 meetsoma
cycle.md files: **`status: open` appears 0 times. `status: closed` appears 0 times.** The two words
the spec anchors the whole vocabulary on are absent from a 221-file corpus. What's actually there:

```
shipped 22 · seeded 16 · active 16 · queued 6 · "spec (not started)" 4 · living 3 · in-progress 3
… plus a long tail — 53 DISTINCT status values across 221 files, independently counted (the spec's
own “187 across 494” cited elsewhere is a different measurement of the same disease, same estate).
```

This matters because it's not “real practice hasn't caught up to the spec's discipline” (the framing
the existing “Status vocabulary” section uses for `updated`). It's that the spec chose different
words than anyone writes. `queued`/`shipped` (PHASE's own vocabulary,
`personal/protocols/phase/README.md` §4.2: `queued | active | shipped | parked | superseded`) is a
CLOSER match to what's actually in the corpus than heartwood's own `open`/`closed` — four of five
PHASE words appear in the wild; three of five heartwood words do (`active`, `parked`, `superseded` —
verified: `parked` and `superseded` both occur, just not counted in the table above since they weren't
in the top-8, but neither is `open`/`closed`, which is the point).

**Second contradiction: the `session` field's ADOPT recommendation, if taken as-is, mints a 7th
spelling instead of converging the corpus.** Re-measured independently: literal `session:` = 133/221
(60%, confirms your number exactly). But counting all provenance-field spellings actually in use
(`session`, `session_origin`, `session-seeded`, `session-opened`, `origin`, `session-updated`) =
**194/221 (88%)**. The field concept is used more than twice as often as the literal key you're
proposing to standardize on. Adopting `session:` without either deprecating the other five spellings
or stating which one is canonical-going-forward doesn't converge the corpus — it adds a fourth-or-
fifth option to a field that already has six.

**Third: the title-colon trap is real but not currently reproducible — and the existing rule is
overbroad.** Scanned 260 files (all of meetsoma + tincture) for the actual dangerous YAML pattern
(`title: X: Y` — unquoted, colon followed by a **space**). Zero live instances. The one raw-colon
match found (`meetsoma/.soma/cycles/services/190-.../cycle.md`, `title: soma:meta scaffolding caps
…`) parses fine under `yaml.safe_load` — no space after the colon, confirmed with a canary
(`yaml.safe_load('title: soma:meta scaffolding caps')` succeeds; `yaml.safe_load('title: Mood:
clinical preset')` raises). **This means the spec's own current rule — “Quote any title containing a
colon” (Frontmatter section, above) — is over-broad**, and an over-broad rule is a rule that gets
ignored wholesale, which loses the real one. **Correction, adopted after review: the rule is `: `
(colon-SPACE), not colon.** `title: soma:meta scaffolding caps` needs no quoting; `title: Mood:
clinical preset` does. State it narrowly in the Frontmatter section: *quote the title when its value
contains `: ` (colon followed by a space).*

On “six cycles … for months” — **unverifiable from current state, and should be labeled as such rather
than repeated.** Ground truth, corrected by the spec's author: 6 unparseable files were found at
`personal/tincture-css/.soma/cycles/` mid-migration on 2026-08-01 `[ran: yaml parse over 38]`, all
`title: Mood: clinical preset`-shaped, and fixed the same session — which is exactly what this
review independently observed (`013-mood-clinical-preset/cycle.md` is correctly quoted right now).
**“For months” is inference** (the old layout was never scanned, so nothing bounds how long the defect
sat there), **not measurement**, and the spec should mark it that way — e.g. “six cycles were found
unparseable when finally scanned; how long they'd been broken is unknown” — rather than asserting a
duration nothing measured.

### Q5 — what's over-specified, given "we don't want to complicate too much"?

1. **`branching`'s three sections (Q2) and `audit` entirely (Q3) are specified with the same
   confidence as `standard`/`spike`, which have real multi-instance support.** Simplest fix: state
   confidence per variant, not just once for the whole document (“Draft, v0.1” in README.md covers
   everything equally). One line each — “validated: 39 standard cycles / 1 branching instance / 0
   audit instances” — costs nothing and stops a reader treating four variants as four equally-earned.
2. **The 8-section spine table presents Goal/Decisions/What-shipped and Risks/Files/Bugs-caught with
   identical visual weight.** Per Q1, they aren't identical in kind — three are used throughout a
   project's life, three are a clustered early habit. Not a content cut, a presentation fix: tier the
   table (`core` vs `situational`) rather than one flat list of eight.
3. **The PRISM-conformant-rendering paragraph (ADOPT #2) generalizes from one file.** Across every
   corpus read for this review, exactly one real cycle-adjacent artifact uses `<!-- @section: name
   -->` anchors — `personal/prism/.soma/cycles/001-renderer-spike/phase-4/convergence.md`, written by
   PRISM's own author, in PRISM's own repo. The paragraph is honest that neither anchors nor rendering
   are required, and costs little as written — but its evidence base is a single self-referential
   example, not a demonstrated cross-project pattern, and should say so rather than imply general
   validation.
4. **Not over-specified, and worth saying so plainly since disagreement is the point here too:** the
   validator contract (ADOPT #3) and the `closed`/`parked`/`superseded` three-way split are both
   *under*-specified relative to what the corpus needs, not over. The corpus's 53 distinct status
   values and its `status: "superseded — shipped 2026-06-21, then … DELETED… status corrected
   s01-016071”`-style narrative statuses (`meetsoma/.soma/releases/cycles/edit-tool-resilience/
   cycle.md`) are the disease `status_note` is meant to cure, live, in the very corpus measured. Keep
   both; if anything, the validator contract should explicitly flag a `status:` value over N
   characters as a `status_note` candidate, since that's the exact live failure mode.

### Does heartwood already exist? (the load-bearing question)

**No spec in `personal/protocols/` defines a cycle's content spine, its variants, or what closing
requires.** Checked all 12 (not the 3 the premises admit to): `amp`, `amps`, `maps`, `breath-cycle`,
`phase`, `mlx`, `mlr`, `seams`, `seeds`, `atlas`, `identity`, plus the archived `three-layer`. Grepped
every README for `through-line|theme|grouping|body of work|multiple (phases|cycles|units)`: zero hits
outside PHASE and SEEDS, both read in full below. **Heartwood is not redundant with anything in the
family.** But it is not landing in empty territory either — two things complicate “should not exist in
its current form” without justifying deletion:

1. **MLX and MLR already assume the thing heartwood formalizes, by name, without defining it.**
   `personal/protocols/mlx/README.md` line 47: “**Cycle dossier** | Picking up that cycle | ‘Phase 6
   needs the SKILL.md stub’” — used as a filing destination across both specs, never specified. This is
   the strongest argument heartwood *should* exist: two published specs reference the artifact by name
   and neither says what's in it. Heartwood is the missing definition, not a competing one.
2. **PHASE's phase-folder (T2, `personal/protocols/phase/README.md` §4) is the closest sibling, and
   the overlap is real, not superficial.** PHASE's phase folder: a directory, one required top file
   (`README.md`, not `cycle.md`), everything else optional, frontmatter
   `status: queued|active|shipped|parked|superseded` (see Q4 — closer to the live corpus than
   heartwood's own vocabulary), a `preload-in.md`/`preload-out.md` handoff heartwood has no equivalent
   of. **The difference is real and worth keeping separate: PHASE configures the agent's BRAIN for the
   unit of work (which muscles/protocols/identity load); heartwood specifies the RECORD the unit of
   work leaves (Goal/Acceptance → What-shipped/Decisions).** PHASE's own README explicitly leaves
   README.md's *content* unspecified (§4.2 only constrains frontmatter). Heartwood could reasonably be
   read as “what goes inside a PHASE T2 README.md, when the phase is shipping work” rather than a
   parallel, competing directory convention — worth an explicit sentence saying that, since right now
   a reader has to infer it.
3. **The word “cycle” is already overloaded four ways in this ecosystem before heartwood adds a
   formal fifth-shaped meaning:** (a) Breath Cycle's session loop (inhale/process/exhale/rest,
   `personal/protocols/breath-cycle/README.md`), (b) PHASE §9's “meta-orchestration cycle” — a
   NEVER-CLOSING rhythm document, the literal opposite of heartwood's closable unit, (c) MLX/MLR's
   undefined “cycle dossier,” (d) heartwood's own cycle. This is not hypothetical: a real file,
   `meetsoma/.soma/releases/cycles/meta/orchestration/cycle.md`, is named `cycle.md`, carries
   `type: cycle`, and is sense (b) — `status: living`, opens with “This isn't a work cycle. It doesn't
   ship and close.” Any tool built from this spec's conformance rules needs an explicit way to skip
   files like this one, or it will flag a correctly-functioning document as broken. Recommend either a
   frontmatter escape hatch (`kind: meta` — which that exact file already carries, unprompted) or an
   explicit § in this spec naming the collision and how a validator should treat it.

**Verdict: heartwood should exist, but should say explicitly where it sits relative to PHASE T2 and
name the “cycle” collision rather than let a validator discover it.** Neither is a reason to fold
heartwood into another spec — the content-spine question (what makes a record trustworthy) is genuinely
unaddressed elsewhere.

### Also found, adjacent to this review's scope

**`spec/layout.md`** (new in this repo, untracked, same session s01-8b4389) substantially overlaps
`spec/README.md` §3–§4 — both cite the identical “494-cycle … `04` appears 5 times, `01` 5 times”
statistic, both argue numbering is per-project and an arc needs its own `cycle.md` entry, using the
same tincture-css examples (`registry-codegen/`, `037-tincture-revamp/`). Not reconciled here per your
instruction not to rewrite — flagging so the two aren't left silently saying the same thing twice with
different illustrations.

**Premises verified:**
- `session` 60% of meetsoma cycles — **confirmed exactly** (133/221).
- `updated` 19% — **confirmed** (44/221 = 20%, rounding).
- spine came from 38 tincture cycles — **confirmed independently**, all 8 counts reproduced from a
  fresh read of `personal/tincture-css/.soma/cycles/**/cycle.md` (39 files on disk; one is presumably
  unshipped or a duplicate against your “38 shipped” framing — not chased further, doesn't change the
  conclusion).
- “nothing else in `personal/protocols/` specifies the ARC loop” — **confirmed after reading all 12
  READMEs**, not the 3 admitted to. This was the correct call, for the reason given in §1 above (MLX/
  MLR need it and don't have it) — but it survives with a caveat (§2–3 above), not cleanly.

### Addendum — `spec/execution.md` (reviewed after first pass; not restarted)

Read in full: `spec/execution.md` (this repo), `meetsoma/.soma/releases/cycles/soma-dev/phases/{0-
orient,1-plan,2-build,3-verify,5-release,6-reflect}.md`, `soma-blog/phases/*.md` (8 files),
`upstream-pi/phases/*.md` (8 files) — 23 real phase files across three independent phase-folder
systems, not one.

**Q1 — does `execution:` belong in heartwood, or does it turn a format into a framework? Is the seam
thin anywhere?** The seam (“heartwood declares THAT and WHAT DONE MEANS; a runtime decides HOW”)
holds for four of five fields and is genuinely thin for one:

- `role`, `mode`, `next`, `inputs` are labels, a scope declaration, and branch conditions — none of
  them tell a runtime how to execute, only what to call and where to route. Consistent with the seam.
- **`success:` visibly overlaps `Acceptance`, which the spine already has.** Both are described the
  same way — “the falsifiable bar, written before the work” (execution.md) vs “the falsifiable form of
  Goal—how anyone can check it” (cycle-format.md, above). Nothing in either document says whether a
  cycle with both is supposed to write the bar twice (once for a human, once for a runner) or whether
  `execution.success` is meant to just restate `Acceptance` in frontmatter for machine access. Left
  unstated, an author has to guess. Recommend: either declare `execution.success` a **required mirror**
  of `Acceptance` (frontmatter copy of the body's falsifiable bar, for machines that don't parse
  markdown bodies) and say so explicitly, or drop the field and have a runner read `Acceptance` from
  the body directly — the second is less duplication and the spec's L0→L1 degrade story (“reads as
  documentation”) already implies a runner CAN parse the body.
- **`model:` is the thin point, and the one real corpus that supports the block disproves its own
  need for it.** In `soma-dev/phases/*.md` — the only one of three phase-folder systems checked that
  uses `role`/`model` at all (6 of 23 real phase files, 26%; `soma-blog` and `upstream-pi`, 16 files
  combined, use neither) — `model` is **fully determined by `role` in all 6 instances**:
  `reflector→claude-haiku-4-5` (0-orient, 6-reflect), `planner→claude-sonnet-4-6` (1-plan),
  `builder→claude-sonnet-4-6` (2-build), `verifier→claude-haiku-4-5` (3-verify),
  `releaser→claude-sonnet-4-6` (5-release). Zero counterexamples. If a runtime already owns a
  role→model mapping (which it must, since “model is a routing hint, not an instruction” and hosts
  “map to their own catalog” anyway), specifying `model` per-cycle is redundant with information the
  runtime already has, in the one dataset that actually uses the field. That's a runtime-owned mapping
  leaking into the format layer — the exact failure mode the seam argument is designed to prevent, and
  it's happening in execution.md's own supporting evidence. Recommend dropping `model` from the core
  block (a host that wants a per-cycle override can still add it as a documented extension, same as
  `spans_repos`/`depends_on` in the main gap analysis's DECLINE section) or reframing it explicitly as
  an override-only field, present only when a cycle needs to escape its role's default.

**Verdict: the seam holds, with one field (`model`) that violates it in the only corpus that tests it,
and one field (`success`) whose relationship to an existing spine section (`Acceptance`) is undefined.
Neither is fatal — both are one sentence away from resolved.**

**Q2 — is `next:` as a conditional branch justified by the corpora, or generalized from one phase
folder?** Checked all 23 real phase files across three systems for a routing/“next” section:

- **`soma-dev/phases/` (6 files with a `## → Next` section): genuinely mixed, not uniformly
  conditional.** `0-orient.md` branches 4 ways (new-feature / continuing / about-to-release /
  triage-only), `3-verify.md` branches 2 ways (pass→ship, fail→back-to-build), `5-release.md`
  branches 2 ways (ship→reflect, gate-failure→back). But `1-plan.md` and `2-build.md` are **simple
  single pointers** (`phases/2-build.md`, `phases/3-verify.md`), and `6-reflect.md` is terminal
  (`(session end)`). **3 of 6 branch, 2 of 6 don't, 1 of 6 ends.** The archived pre-orchestrator
  version of the same cycle shows the identical split, independently.
- **`soma-blog/phases/` (8 files): zero routing sections of any kind.** No `## → Next`, no
  conditional pointer — the pipeline is strictly linear (0-seed → 1-source → … → 6-reflect) and
  relies entirely on filename ordering. Routing doesn't appear because the workflow never branches.
- **`upstream-pi/phases/` (8 files): zero routing sections.** One file has a heading that matches
  “next” textually (`## Next-Session Verification Checklist` in `0-model-provider-audit.md`) but it's
  a checklist, not a routing pointer — a false positive on the search, not a counterexample.

**Verdict: justified, not over-generalized — but the justification is narrower than “phase folders use
conditional next.”** The accurate claim is: *conditional `next:` is real and earns its place
specifically in phase-folder systems that have retry loops or multiple entry points* (soma-dev, which
does), *and correctly does not appear where the workflow is linear* (soma-blog, upstream-pi, which
don't need it and don't have it). That's actually a **stronger** argument for keeping `next:` as
conditional-capable than a uniform 6/6 would have been — it means the shape tracks real branching
when present and imposes nothing when absent, which is what an optional field should do. Worth
citing the 3-of-6-branch, 2-of-6-single-pointer split in execution.md directly, rather than the flat
statement “a cycle that can end more than one way should say so” — the corpus shows both cases are
common and the field handles both without forcing either.
