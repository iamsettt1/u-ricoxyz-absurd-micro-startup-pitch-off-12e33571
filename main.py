#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt. Deterministic: the same bytes
every run. Standard library only, no network.
"""

import os

PITCH = (
    "SnoozeSheets: lazy AI agents that auto-decline any meeting invite "
    "containing the word 'sync' for burnt-out startup founders, charging "
    "$3 per rescued afternoon."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
