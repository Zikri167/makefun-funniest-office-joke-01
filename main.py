#!/usr/bin/env python3
"""Write one original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib-only, no network, no clock, no files outside the
output directory: every run writes the same bytes.
"""

import os

JOKE = "My boss says we're a family, so I asked HR for my weekly allowance."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
