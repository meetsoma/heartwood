#!/usr/bin/env python3
"""heartwood validate — the reference validator for the heartwood cycle format.

Implements the four checks from spec/cycle-format.md §validator contract.
Exit 0 = clean, exit 1 = dirty. A warning nobody actions is not a gate —
there is no warn-and-continue, no --fix, no per-check opt-out.

    python3 tools/validate.py [ROOT]

ROOT defaults to the repo root (tools/' parent). Point it at any host dir
(.soma/cycles, .claude/, .agent/) to validate that host's cycles — the tool
must not assume a particular host layout. `_fixtures/` is always skipped:
those files are deliberately broken and exist to prove this validator can fail.

Four checks, no more. The spec lists these as the MINIMUM a conforming
validator does; extra checks belong to a host's own tooling, not to the
reference implementation. Four checks that always run beat nine that get
disabled.

stdlib + pyyaml only. No deps, no build.
"""

import os
import re
import sys

import yaml

# spec/cycle-format.md §Status vocabulary — READ ONLY, the enum lives there.
STATUSES = {"open", "active", "closed", "parked", "superseded"}
# type: arc is required for an arc root (cycles-demo/example-arc/cycle.md).
TYPES = {"cycle", "arc"}

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
# Hyphens are REQUIRED in this class: real frontmatter uses `forked-from`,
# `session-seeded`, `estimated-turns`. Without them check 4 silently skipped
# every hyphenated key -- the file still failed check 1, but the actionable
# "quote it" message never fired, which is check 4's whole reason to exist.
# Found by fresh-eyes review, s01-593a6d; fixture 05 makes it falsifiable.
KEYVAL = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


def find_cycles(root):
    """All cycle.md under root, except inside _fixtures/ (deliberately broken).

    _fixtures/ is skipped only as a SUBDIRECTORY — pointing the validator
    directly at a fixture (as the self-test does) must still see its files.
    """
    root_real = os.path.realpath(root)
    out = []
    for dirpath, _dirnames, filenames in os.walk(root):
        if dirpath != root_real:
            rel = os.path.relpath(dirpath, root_real).split(os.sep)
            if "_fixtures" in rel:
                continue
        if "cycle.md" in filenames:
            out.append(os.path.join(dirpath, "cycle.md"))
    return sorted(out)


def check_file(path):
    """Return a list of problems ([] = conforming)."""
    problems = []
    text = open(path, encoding="utf-8", errors="replace").read()
    m = FM_RE.match(text)
    if not m:
        return ["no frontmatter block (missing closing `---`?)"]
    raw = m.group(1)

    # Check 1 — frontmatter parses as YAML. Six cycles in one project were
    # silently unreadable because they never parsed; tooling skipped what it
    # could not parse.
    try:
        fm = yaml.safe_load(raw)
    except Exception as e:
        problems.append("YAML parse error: %s" % str(e).strip().splitlines()[0])
        fm = None
    if fm is not None and not isinstance(fm, dict):
        problems.append("frontmatter is %s, not a mapping" % type(fm).__name__)

    # Checks 2-3 — only meaningful if the frontmatter parsed.
    if isinstance(fm, dict):
        t = fm.get("type")
        if t not in TYPES:
            problems.append("type: %r — must be one of %s" % (t, sorted(TYPES)))
        s = fm.get("status")
        if s not in STATUSES:
            problems.append(
                "status: %r — must be one of %s" % (s, sorted(STATUSES)))

    # Check 4 — a value containing ': ' must be quoted. Checked on the raw
    # text, independent of parse success: an unquoted colon-SPACE IS a YAML
    # parse error, but the generic message does not say *what* to fix. This
    # gives the actionable one. The rule is narrow on purpose: `soma:meta`
    # (colon, no space) is legal YAML and must not be flagged.
    for line in raw.splitlines():
        kv = KEYVAL.match(line)
        if kv and not kv.group(2).lstrip().startswith(('"', "'")):
            if ": " in kv.group(2):
                problems.append(
                    "value contains ': ' and is unquoted — quote it, e.g. "
                    'title: "Mood: clinical preset"')
                break  # one actionable message per file is enough
    return problems


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    args = sys.argv[1:]
    root = args[0] if args else repo_root()
    files = find_cycles(root)
    bad = []
    for f in files:
        for p in check_file(f):
            bad.append((f, p))
    if bad:
        for f, p in bad:
            print("FAIL  %s" % f)
            print("      %s" % p)
        print("\n%d problem(s) in %d cycle.md file(s)" % (len(bad), len(files)))
        return 1
    print("OK — %d cycle.md conform" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
