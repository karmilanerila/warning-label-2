#!/usr/bin/env python3
"""Warning label for humans — backup angle: the unit that insists it is fine.

Writes a single-line safety warning label for every human being to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "WARNING: This unit will say it is fine while falling apart "
    "- believe the smoke, not the smile; asking twice voids the warranty."
)


def main() -> None:
    # Gate: entry must be UTF-8 text, 1 to 160 characters, not only whitespace.
    stripped = LINE.strip()
    if not stripped or len(LINE) > 160 or "\n" in LINE:
        raise SystemExit("entry line fails the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
