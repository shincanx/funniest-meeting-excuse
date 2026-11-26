#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp excuse line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
"""
import os

EXCUSE = (
    "I already watched next week's recording of this meeting \u2014 spoiler: "
    "nothing gets decided, so I'm skipping straight to the credits."
)


MAX_CHARS = 200


def main():
    line = EXCUSE.strip()
    if not line:
        raise SystemExit("excuse line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"excuse line is {len(line)} chars, over the {MAX_CHARS} cap")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
