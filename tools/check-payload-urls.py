#!/usr/bin/env python3
"""Publish gate: every absolute URL in the payload must match the real remote.

Format Rule 1 says a payload may only reference paths inside itself, and that
anything outside must be an absolute URL. Following that rule correctly is what
created this defect: converting relative->URL moved the breakage from VISIBLE
(file not found) to INVISIBLE (an authoritative-looking 404). The Rule-1 gate
resolves relative links and never looks at the URLs it told you to write.

This is the other half. It asserts the <org>/<repo> baked into every payload URL
matches the repository's configured remote.

    python3 tools/check-payload-urls.py [PAYLOAD_DIR]

Exit 0 = every URL matches the remote. Exit 1 = mismatch, or no remote at all.
"no remote" is a FAILURE, not a skip: an unpublished repo whose payload already
hardcodes an org is exactly the state where publishing under a different name
bakes wrong URLs into a stranger's install. (Precedent: tincture was decided for
meetsoma/ and shipped at curtismercier/tincture.)

stdlib only.
"""

import os
import re
import subprocess
import sys

URL_RE = re.compile(r"https?://(?:raw\.)?github(?:usercontent)?\.com/([\w.-]+)/([\w.-]+)")


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def configured_remote(root):
    """(org, repo) from origin, or None if there is no remote."""
    try:
        url = subprocess.run(["git", "-C", root, "remote", "get-url", "origin"],
                             capture_output=True, text=True, timeout=15).stdout.strip()
    except Exception:
        return None
    if not url:
        return None
    m = re.search(r"[:/]([\w.-]+)/([\w.-]+?)(?:\.git)?$", url)
    return (m.group(1), m.group(2)) if m else None


def main():
    root = repo_root()
    payload = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, "soma")
    if not os.path.isdir(payload):
        print("no payload dir at %s" % payload)
        return 1

    found = {}  # (org, repo) -> [(file, line)]
    for dirpath, _d, files in os.walk(payload):
        for fn in files:
            if not fn.endswith((".md", ".json", ".txt")):
                continue
            fp = os.path.join(dirpath, fn)
            for i, line in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
                for org, repo in URL_RE.findall(line):
                    found.setdefault((org, repo), []).append(
                        (os.path.relpath(fp, root), i))

    if not found:
        print("OK — no absolute github URLs in the payload")
        return 0

    total = sum(len(v) for v in found.values())
    remote = configured_remote(root)

    if remote is None:
        print("FAIL — payload hardcodes %d URL(s) but this repo has NO REMOTE." % total)
        for (org, repo), hits in sorted(found.items()):
            print("  %s/%s  (%d refs)" % (org, repo, len(hits)))
        print("\nPublishing anywhere other than the org above bakes wrong URLs into")
        print("every install. Set the remote first, or rewrite the URLs.")
        return 1

    bad = {k: v for k, v in found.items() if k != remote}
    if bad:
        print("FAIL — %d URL(s) do not match remote %s/%s:" % (
            sum(len(v) for v in bad.values()), remote[0], remote[1]))
        for (org, repo), hits in sorted(bad.items()):
            print("  %s/%s — %d refs" % (org, repo, len(hits)))
            for f, ln in hits[:5]:
                print("      %s:%d" % (f, ln))
            if len(hits) > 5:
                print("      ... and %d more" % (len(hits) - 5))
        return 1

    print("OK — all %d payload URL(s) match remote %s/%s" % (total, remote[0], remote[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
