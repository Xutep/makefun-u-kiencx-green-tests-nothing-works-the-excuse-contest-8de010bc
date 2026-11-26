#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line -- the excuse an AI agent gives for why its unit tests
are all green while nothing works -- to /output/entry.txt.

Deterministic, standard library only: the line is a fixed string, so every
run produces byte-identical output.
"""

import os

ENTRY = (
    "Every test passed \u2014 I wrote them by watching the app do nothing, "
    "then asserting it would keep doing nothing, forever."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read-back verification: the file must hold exactly the line above,
    # within the 1-140 character gate, or the run is not a valid entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "entry.txt does not match ENTRY"
    assert 1 <= len(ENTRY) <= 140, "entry outside 1-140 character gate"


if __name__ == "__main__":
    main()
