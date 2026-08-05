---
type: spec
name: heartwood-execution
status: draft
version: 0.1.0
created: 2026-08-01
updated: 2026-08-01
---

# Execution — a cycle that can be run, not just recorded

> **Entirely optional.** Everything in `cycle-format.md` works with no agent, no runner, and no
> tooling. This layer is additive: a cycle without an `execution:` block is not deficient, it is
> just one a person does.

## Three layers

| layer | you have | you get |
|---|---|---|
| **L0 — recorded** | markdown | the format. Works anywhere, forever, no runtime. |
| **L1 — declared** | `execution:` in frontmatter | a machine-readable statement of who should run this, on what, and what "done" means. **Still needs no runner** — it reads as documentation. |
| **L2 — executed** | a host with a runner | the host dispatches it |

**Each layer degrades to the one below without loss.** A host that does not understand `execution:`
ignores an unknown frontmatter key, which is the correct behaviour and requires no negotiation.

## The block

```yaml
execution:
  role: builder                 # WHO. a named role the host resolves.
  model: sonnet-5               # routing HINT, not an instruction. hosts map to their own catalog.
  mode: delegate                # delegate | phased | manual
  inputs:                       # what a runner must supply. absent = the cycle is self-contained.
    - path/to/thing.md
  success: >                    # the falsifiable bar, written BEFORE the work
    A compact report under 20 lines naming what changed and how it was verified.
  next:                         # conditional routing, written at CLOSE
    - if: shipped
      then: 038-follow-up
    - if: blocked
      then: 039-unblock-first
```

Every key is optional. `role` alone is a useful cycle.

### `mode`

- **`delegate`** — a parent dispatches this as one unit of work and verifies the result. The common case.
- **`phased`** — this cycle is one step in a chain; `next:` routes to the following step. Use when
  the work genuinely has stages that hand off, not merely sub-tasks.

  🔑 **Each stage's brief must PRE-AUTHORIZE refuting its input** ("if the premise is wrong, STOP
  and report — that is a valid outcome"). Measured on a 4-stage chain (L55 persistence,
  s01-7d05d5, 2026-08-05): S2 revoked S1's binding directive, S3 revoked S2's mechanism, S4 shipped
  what survived — **every stage's most valuable output was refuting part of its input**, and the
  chain only worked because each gate treated the refutation as success, not failure. A phased
  chain whose stages may only ADD is a machine for hardening the first stage's mistakes: an
  adjudicated PASS at stage N converts stage N-1's wrong sentence into a binding instruction unless
  stage N+1 is licensed to challenge it.
- **`manual`** — declared for documentation, deliberately not automated. Says *"a person does this,
  on purpose"*, which is different from an absent block meaning *"nobody decided."*

## Why `success:` is the load-bearing field

It is written **before** the work, which is what makes it a bar rather than a description. A runner
can check it; a reviewer can check it; the executing agent can check its own output against it.

**A `success:` that cannot fail is not a success criterion.** "Improve the docs" is unfalsifiable.
"Every path named in `exports` resolves in a fresh clone" is checkable by someone who doubts you.

## Why `next:` is the most valuable field, and the least obvious

`next:` is written **at close, while the context that produced the cycle is still loaded** — and
consumed later, when it is not.

This is the whole point. The agent finishing a cycle knows which follow-up matters and why; the
agent picking up next week has a preload and a directory listing. Routing decided in the first
state and consumed in the second is strictly better than routing re-derived in the second.

It is a **branch, not a pointer**:

```yaml
next:
  - if: shipped   then: 038-follow-up
  - if: blocked   then: 039-unblock-first
```

not `next: 038-follow-up`. A cycle that can end more than one way should say so, because the
condition is exactly what gets forgotten.

## Prior art, and the seam

This layer generalises a pattern already in production elsewhere: **phase folders** whose
frontmatter carries `role:`, `default-model:` and `delegation-mode:`, with a Delegation Contract
(`Inputs:` / `Success:`) and a conditional `## → Next` section.

That system is a **runtime**: it configures how an agent thinks per phase, and it owns roles,
prompts and model catalogs. Heartwood deliberately does **not** absorb any of that.

**The seam:** heartwood declares *that* a cycle is executable and *what done means*. A runtime
decides *how* to execute it — which role file, which prompt, which model, what budget. Heartwood
names the role; it does not define roles.

Keeping the seam is what lets the format stay adoptable by anyone not running that runtime. Absorb
the runtime and heartwood becomes a framework, and frameworks get evaluated where formats get used.

## A host runner (informative)

A host MAY provide a runner. One plausible surface:

```
<host>:run <path/to/cycle.md>
```

which reads `execution:`, resolves `role` against its own role library, maps `model` onto its own
catalog, spawns, and verifies against `success:`. **Nothing in this spec requires that command to
exist**, and a cycle must never depend on one having run.
