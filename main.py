"""tired-dark-lord-monologue entry: write one 100-word villain monologue
to /output/entry.txt.

Fully deterministic: the monologue is hardcoded, no randomness, no clock,
no network. The villain is three hundred years into keeping his mountain
and keeps losing the thread mid-threat: the quiet before the horns, the
porridge before the sieges, forty-year armies made to wait an afternoon.
Verified output: 512 characters, 95 words, inside the 1-600 character
gate for an about-100-word monologue.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The monologue is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "Come closer. No, not that close. The torches... yes, the torches "
    "are fine, leave them. Three hundred years I have kept this mountain, "
    "and do you know what I remember best? The quiet before the horns. "
    "The porridge, before the sieges. You came for the crown, the "
    "prophecy, the usual. Sit. No, truly, sit. My armies will wait; "
    "they have waited forty years, they can wait an afternoon. The "
    "ritual needs one more dawn, one more drop of... ah. Forgive me. I "
    "lost the thread. Where was I? Oh. Yes. The part where I win."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
