#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Entry program: writes one single-line joke about office life to
/output/entry.txt. The text is fixed, so the program is fully
deterministic: every run writes the same bytes. No network, no input,
no randomness.
"""

import hashlib
import os
import sys

JOKE = "My performance review said I should be more visible, so now I reply-all to everything."

EXPECTED_SHA256 = "38f08794ab02b5a4345cc9b3eff6fadfa069f360127d84883e429c01093b528e"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Post-write read-back gate: the graded artifact must be exactly the
    # joke above, byte for byte, on every run. Verify the exact string,
    # the exact length (86), no trailing newline, and the pinned sha256
    # of the expected bytes; anything else is a hard fail.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != JOKE.encode("utf-8"):
        print("gate failed: entry.txt bytes differ from JOKE", file=sys.stderr)
        raise SystemExit(1)
    if len(raw) != 86 or raw.endswith(b"\n"):
        print(f"gate failed: entry.txt is {len(raw)} bytes, expected 86 with no trailing newline", file=sys.stderr)
        raise SystemExit(1)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"gate failed: sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        raise SystemExit(1)
    print(f"verified: 86 chars, sha256 {digest}")


if __name__ == "__main__":
    main()
