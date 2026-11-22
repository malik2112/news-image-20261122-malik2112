#!/usr/bin/env python3
"""Entry for make.fun news-image-20261122 (@malik2112).

Copies the bundled front-page image (entry.png) to the output path.
The image itself is the entry: "The Sunday Dispatch", a dense digest
summing up the world news of Sunday 22 November 2026.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: a byte-for-byte copy of the bundled
    # image, so both graded runs write identical output. The copy is the
    # whole program - no rendering, no network, no randomness, no clock.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
