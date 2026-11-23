#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to /output/entry.txt.
The line is 123 characters, inside the 1-200 character gate.
"""

import os

LINE = (
    "I killed my houseplant, so I bought a plastic one. "
    "It died too \u2014 honestly, that's the most impressive "
    "thing I've ever done."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
