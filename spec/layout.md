---
type: spec
name: heartwood-layout
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# What a `cycles/` folder looks like

> Every tree below is real. Nothing here is illustrative-but-hypothetical.

## The whole shape

```
.soma/cycles/                          <- the tree. one per project.
│
├── substrate-foundation/              <- an ARC. a themed body of work.
│   ├── 001-foundation-light-dark/
│   │   └── cycle.md
│   ├── 002-surface-untangle/
│   │   └── cycle.md
│   └── 003-component-migration-wave-1/
│       └── cycle.md
│
├── registry-codegen/                  <- another arc. 4 cycles.
│   ├── 004-registry-tokens-schema/cycle.md
│   ├── 005-codegen-registry-to-css/cycle.md
│   ├── 006-studio-reads-manifest/cycle.md
│   └── 007-component-migration-wave-2/cycle.md
│
├── v02-multi-axis-substrate/          <- 17 cycles. arcs are not evenly sized.
│   ├── 021-.../cycle.md
│   ├── …
│   └── 037-tincture-revamp/           <- a cycle that ACCUMULATED EVIDENCE
│       ├── cycle.md                       the record
│       └── drafts/                        the artifacts it explains
│           ├── README-draft-v1.md
│           ├── README-draft-v2.md
│           ├── REVAMP-WIP.md
│           ├── SKILL.md.draft
│           └── voice.md.draft
│
├── _audits/                           <- underscore = not an arc
├── _reports/
└── INDEX.md
```

## What the shape is arguing

**A cycle is a DIRECTORY, not a file.** `037-tincture-revamp/` is the proof: five draft documents
sit beside the cycle that explains what happened to each of them. As a flat `cycle-37.md` those
drafts would have had nowhere to live — which is exactly why, in the corpus this came from, they had
been sitting in an unrelated `plans/` folder for three months, disconnected from any record.

**Most cycles hold only `cycle.md`, and that is fine.** 38 of 39 in this tree do. The directory
costs nothing when empty and is the only thing that works when it isn't.

**Arcs are not evenly sized.** 3, 4, 4, 9, 17. An arc is a through-line, not a bucket — resist
balancing them.

**A leading underscore means "not an arc".** `_audits/`, `_reports/`, `_unsorted/` are containers
the tooling skips. It is a convention, not a rule the format enforces, but it keeps discovery honest:
anything without an underscore is claiming to be a body of work.

## Numbering

Numbers here are **per-project IDs** — `037` is unique in this tree and says nothing outside it.
They ran 001→037 continuously across five arcs, so "cycle 37" is unambiguous in conversation, which
is the whole benefit.

They do **not** survive contact with an estate. In a 494-cycle multi-repo corpus, `04` appears five
times and `01` five times — there, numbers are positions within an arc, not identifiers. **Pick one
model per project and say which.**

## The arc's own entry

An arc SHOULD have its own `cycle.md` at the arc root, holding the through-line:

```
registry-codegen/
├── cycle.md                 <- the arc: why these four belong together
├── 004-registry-tokens-schema/cycle.md
└── …
```

An arc directory with members but no entry is a **folder pretending to be a grouping**. In the
corpus above, 21 groups had no arc entry — and until they were counted, nobody knew the through-line
was missing rather than merely unwritten.

⚠️ Do not confuse that with a directory that groups by *how work was done* rather than by subject
(`fixes/`, `refactors/`, `phase-3/`). Those should dissolve as members complete — writing an arc
entry for one entrenches the axis you are trying to remove. **The two look identical from the
outside and mean opposite things**, so any tool that flags "missing arc entry" must distinguish them
or it will send people to do the wrong work.


---

## Where the tree lives, and the PROJECT tier

The demo above shows one project's tree. In an estate the project tier is **implied by location**,
not by a subdirectory:

```
<project>/.soma/cycles/<arc>/<NNN>-slug/cycle.md
^^^^^^^^^                                            <- the project IS the path
```

**A cycle is owned by the project it is ABOUT**, so it resolves from that project's own directory.
A parent that wants to see everything at once does **not** need to restructure the filesystem: an
indexer that *discovers* trees resolves a live estate of **12 distinct projects** with no links at
all.

### An arc claims a cycle in FRONTMATTER, not on the filesystem

```yaml
arc: <arc-slug>     # in the cycle's own frontmatter, wherever the file sits
```

That is the membership mechanism. The folder is a convenience for **humans reading**, so
consolidating related cycles into one arc folder is a *move*, priced in referrer updates — measure
inbound references, and if they are cheap, move; if not, leave the file and declare `arc:`.

⛔ **Do not link cycles between trees.** It reads as consolidation and is not: a link hands a human
two places one cycle might live, while handing the indexer nothing it could not already discover.
Anything that follows links counts the target twice — one estate measured **113 cycles of inflation
(21%)** from three links, deleted all three, and lost nothing.

**The one exception:** a foreign estate whose record you must not take custody of — a client's tree,
a repo you don't own. Then link it *and record why in the arc's Members table*, because an
unexplained link will eventually be deleted by someone tidying.

<!-- CORRECTED 2026-08-01: this section prescribed pulling sibling projects in by symlink and showed
     `somaverse -> ../../somaverse/.soma/cycles` as the pattern. Those exact three links had already
     been retired in the estate the example came from. Fossil kept: an agent read the instruction,
     followed it, and had to be reversed by hand. -->

## Multi-agent hosts

Nothing above requires the directory to be called `.soma/`. The tree is
`<host-dir>/cycles/<arc>/<NNN>-slug/cycle.md`, and `<host-dir>` is whatever the host uses:

| host | dir |
|---|---|
| Soma | `.soma/` |
| Claude Code | `.claude/` |
| generic | `.agent/` or `.agents/` |

**Only the runtime cares.** A cycle document is markdown with frontmatter and does not know which
directory contains it — which is what makes the format portable across harnesses rather than tied
to one.

⚠️ **A payload is a different matter.** Installable content (`body/`, `amps/`, `skills/`) has to
land in host-specific locations, and those differ per harness — `skills/` is not in the same place
under Soma and Claude Code. That mapping belongs to the **host's installer**, declared once per
host, and must not leak into the cycle format. One map per host is fine; one map per content type
is the thing worth avoiding.
