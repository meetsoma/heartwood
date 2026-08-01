# cycles-demo

A **real, valid** cycle tree you can point tooling at.

Two jobs:
1. **Illustration** — `spec/layout.md` describes the shape; this is the shape.
2. **Fixture** — a conforming validator must pass on this tree. If it doesn't, the validator is
   wrong or the spec is.

## Why this is NOT in the payload

`soma/` installs into a user's `.soma/`. A `soma/cycles/` directory would land demo cycles in
`~/.soma/cycles/` where the registry would **scan them as real work** — someone installs heartwood
and their corpus silently gains fake cycles.

`cycles/` is not on the payload whitelist for exactly this reason. Demos live in the repo; only
`body/ amps/ skills/ extensions/` ship.
