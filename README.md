<div align="center">

# HEARTWOOD

**The work-record protocol. Arcs, cycles, and the evidence a cycle leaves when it closes.**

*Finished work is what holds the structure up.*

</div>

---

Heartwood is the dense inner rings of a tree. It carries no sap and does no growing — and it is what
keeps the tree standing. A closed cycle is the same: no longer active, and the reason the project
still makes sense a year later.

## What this is

A specification for **the record work leaves behind** — how a project's efforts are grouped, what a
cycle document contains, and what "closed" is allowed to mean.

It is files. No database, no service, no build step. A cycle is a markdown file with frontmatter, in
a directory, in your repo.

## The model

```
project/                  the thing being built
└── arc/                  a themed body of work with a through-line
    └── NNN-slug/         one cycle
        └── cycle.md
```

**An arc holds many cycles.** It is not a phase that happens to be a cycle — it is a grouping with a
stated through-line, and the cycles inside it are the work.

**A cycle is a directory, not a file.** Because real cycles accumulate evidence — reports, audits,
drafts — and that evidence belongs next to the record that explains it.

## The cycle format

One spine, four variants (`standard`, `branching`, `audit`, `spike`).

The spine was **measured, not designed**: across 38 shipped cycles in a real project, sections
converged on `Goal · Spec · Acceptance · Risks · Files` before, and `What shipped · Decisions ·
Bugs caught` after. Nobody wrote that template first.

→ **[spec/cycle-format.md](spec/cycle-format.md)** — the spine, the variants, and why each section
survives.

Two rules that carry most of the value:

- **Record the option you rejected.** A decision without its alternative is a preference, and the
  rejected option is the only thing that stops the next person relitigating it.
- **An audit states its denominator.** "8 are broken" is unreadable. "8 of the 34 found by
  `grep -rln` over these 4 directories" is checkable.

## Layout

| path | for |
|---|---|
| `spec/` | the protocol — human-readable, no tooling required |
| `templates/` | copyable scaffolds: `cycle/` (the `standard` variant), `arc/`, and three `variants/` |
| `tools/` | `validate.py` — the four spec'd checks, single-tree · `selftest.py` · broken fixtures · `pre-commit` |
| `soma/` | payload that installs into a [Soma](https://github.com/meetsoma/soma-beta) agent's `.soma/` |

## Status

**Draft, v0.1.** The spec is written from measured usage across three projects; the payload is
scaffolded, not finished. The validator is extracted and gates this repo's own demo via
`tools/pre-commit`. See `spec/` for what is settled and what is not.

## Related

Part of a family of open protocols for agent memory and architecture — alongside `breath-cycle`
(the session loop) and `PHASE` (prompt handoff). Heartwood owns the **arc loop**: the work record
itself, which nothing else specified.
