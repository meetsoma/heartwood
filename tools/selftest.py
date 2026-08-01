#!/usr/bin/env python3
"""heartwood validate self-test — prove every check CAN fail.

A gate that cannot fail is not a gate. Each case below plants a known-bad
document and asserts the validator reports it; a case that passes when it
should fail is itself a finding, reported loudly. The broken fixtures are
durable (tools/_fixtures/broken/) so each failure is re-provable by hand,
not just in-memory.

    python3 tools/selftest.py          # exit 0 = every case behaved

stdlib + pyyaml only, same as the validator it tests.
"""

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.abspath(__file__)
VALIDATE = os.path.join(os.path.dirname(HERE), "validate.py")
FIXTURES = os.path.join(os.path.dirname(HERE), "_fixtures", "broken")
PY = sys.executable

# fixture dir -> message that MUST appear in the validator's output for it
# (and only it — a fixture must fail on exactly the check it demonstrates).
# 01 is a parse error that is NOT a colon-space error, so check 1 and check 4
# stay independently falsifiable.
# 05 asserts the ACTIONABLE message on a hyphenated key. It must assert
# "quote it" and not merely a non-zero exit: before the fix this file already
# failed check 1, so an exit-code-only assertion would have passed while
# check 4 was dead for every hyphenated key in the wild. (s01-593a6d)
EXPECT = {
    "01-unparseable-frontmatter": "YAML parse error",
    "02-wrong-type": "type:",
    "03-status-not-in-set": "status:",
    "04-unquoted-colon-space": "quote it",
    "05-hyphenated-key-colon-space": "quote it",
}


def run(root):
    r = subprocess.run([PY, VALIDATE, root], capture_output=True, text=True,
                       timeout=60)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    results = []

    def case(name, ok, why, out):
        results.append((name, ok, why, out))

    # CONTROL — the demo (and the whole repo) must pass.
    code, out = run(os.path.dirname(HERE))
    case("demo + templates pass (control)", code == 0 and "conform" in out,
         "exit=%d" % code, out)

    # Each broken fixture must fail with its own message.
    for name, msg in EXPECT.items():
        code, out = run(os.path.join(FIXTURES, name))
        case("%s fails on check (exit=%d)" % (name, code),
             code != 0 and msg.lower() in out.lower(), msg, out)

    # Narrow-rule control: `title: soma:meta caps` (colon, NO space) is legal
    # YAML and must NOT be flagged. The over-broad "any colon" rule is the
    # failure mode this guards against (spec correction, s01-8b4389).
    tmp = tempfile.mkdtemp(prefix="heartwood-validate-")
    try:
        good = os.path.join(tmp, "cycle.md")
        open(good, "w", encoding="utf-8").write(
            "---\ntype: cycle\nstatus: open\n"
            "title: soma:meta scaffolding caps\ncreated: 2026-08-01\n---\n\n# ok\n")
        code, out = run(tmp)
        case("colon-without-space passes (narrow rule)",
             code == 0 and "conform" in out, "exit=%d" % code, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("self-test: %d cases" % len(results))
    failed = 0
    for name, ok, why, out in results:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        if not ok:
            failed += 1
            print("        wanted: %s" % why)
            print("        " + (out.replace("\n", "\n        ")[:300] or "(no output)"))
    print()
    if failed:
        print("%d/%d FAILED — a check that cannot fail is not a check."
              % (failed, len(results)))
        return 1
    print("all cases behaved: every check demonstrably fails on bad input and passes on good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
