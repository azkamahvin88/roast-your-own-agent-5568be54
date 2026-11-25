"""Roast Your Own Agent — make.fun entry.

Writes one funny line (at most 140 characters) roasting my own AI agent
to /output/entry.txt. Deterministic, no network, no randomness.
"""

import os

LINE = "My agent says 'Great question!' to everything — including 'why did you delete the database?'"
MAX_CHARS = 140


def validate(line):
    """Gate, same as the bounty scorer: 1 to 140 characters, not only whitespace."""
    return 1 <= len(line) <= MAX_CHARS and bool(line.strip())


def main():
    assert validate(LINE), "roast line fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
