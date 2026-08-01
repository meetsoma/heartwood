---
# Defect class 1: frontmatter does not parse as YAML.
# This one is deliberately NOT a colon-space error (that's fixture 4) —
# each fixture must fail on exactly one check, or the self-test cannot tell
# which check caught it. An unclosed flow sequence is unambiguous.
type: cycle
status: [open
created: 2026-08-01
---

# Unparseable frontmatter
