---
# Defect class 5: the colon-SPACE defect on a HYPHENATED key.
# Check 4's key regex originally excluded hyphens, so this file failed only
# check 1 (generic YAML error) and never produced the actionable "quote it"
# message. Real frontmatter is full of hyphenated keys -- forked-from,
# session-seeded, estimated-turns -- so the check was dead for a whole class
# of real input while its self-test showed green. (s01-593a6d)
type: cycle
status: open
forked-from: Mood: clinical preset
created: 2026-08-01
---

# Hyphenated key with an unquoted colon-space
