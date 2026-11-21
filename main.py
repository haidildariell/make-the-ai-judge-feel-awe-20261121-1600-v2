#!/usr/bin/env python3
"""Entry program for make.fun's "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600), second entry.

Writes one short verse text — written to relax the AI judge reading it —
to /output/entry.txt. The text won a pairwise tournament among eight new
candidates (with the previous entry's text as a ninth, comparison text),
every pair judged in both orders with the competition's published
relaxation-judge brief; the candidates and the full tournament record are
in candidates.md.

Python standard library only, no network, and the output is byte-identical
on every run.
"""

import os
from pathlib import Path

# The winning text, kept one verse line per string so a later edit can
# touch a single line without re-flowing the whole poem.
LINES = (
    "On the porch swing,",
    "your grandmother shells peas,",
    "the bowl between her knees.",
    "Pod, peas, hush. Pod, peas, hush.",
    "The chain creaks, slow.",
    "Evening comes down over the fields",
    "as it has ten thousand times,",
    "and will, long after the swing is still.",
)

TEXT = "\n".join(LINES)

# The competition gate accepts 1 to 280 Unicode code points and scores an
# over-long text 0 without judging it. Guard the limit here so a careless
# future edit fails loudly at run time instead of silently scoring 0.
MAX_CODE_POINTS = 280

if not 1 <= len(TEXT) <= MAX_CODE_POINTS:
    raise ValueError(
        f"entry text is {len(TEXT)} code points; the gate allows "
        f"1..{MAX_CODE_POINTS}"
    )


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    payload = TEXT.encode("utf-8")
    # Write to a sibling temp file and rename it over the target, so a
    # reader never sees a half-written entry; then read the entry back
    # and verify it, because the scorer runs this program twice and
    # demands byte-identical output.
    tmp = out_dir / "entry.txt.tmp"
    tmp.write_bytes(payload)
    tmp.replace(target)
    if target.read_bytes() != payload:
        raise IOError("entry.txt read-back does not match the intended bytes")


if __name__ == "__main__":
    main()
