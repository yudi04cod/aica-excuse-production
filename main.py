#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Deterministic: the same bytes on every run. Python standard library only.
"""

import os

ENTRY = (
    "I fixed it by deleting the thing that broke production. "
    "The thing was the database. "
    "On the bright side, the error logs are very quiet now."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-180 characters, not only whitespace."""
    if not 1 <= len(text) <= 180:
        raise ValueError(f"entry must be 1-180 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
