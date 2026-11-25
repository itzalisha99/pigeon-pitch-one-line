#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry writer.

Writes the one-line elevator pitch to /output/entry.txt.
"""

import os
import sys

ENTRY = "Our startup turns every statue in the city into a paid billboard. We already have the pigeons, the statues, and zero rent."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only white space, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the entry we validated.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("read-back mismatch: entry.txt does not match ENTRY", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
