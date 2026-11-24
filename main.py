#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Entry program: writes one single-line joke about office life to
/output/entry.txt. The text is fixed, so the program is fully
deterministic: every run writes the same bytes. No network, no input,
no randomness.
"""

import os

JOKE = "My performance review said I should be more visible, so now I reply-all to everything."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
