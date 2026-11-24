#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse line (1-200 chars, UTF-8) to /output/entry.txt.
Pure stdlib; run with: python3 main.py
"""

import os

EXCUSE = (
    "The deadline reminder filled my context window, "
    "so I evicted the deadline to make room for the reminder."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
