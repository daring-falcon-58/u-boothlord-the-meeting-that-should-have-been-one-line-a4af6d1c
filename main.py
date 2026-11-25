#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry program.

Writes one sentence to /output/entry.txt: the line that could have replaced
an entire pointless meeting. Deterministic: fixed text, no randomness,
no network, no input.
"""
import os

ENTRY = "The entire meeting fits in this sentence: the launch is delayed a week, the client knows, and nobody here can change that."

def main():
    # Gate self-checks (competition.yaml: gate valid, judge cap 200):
    # exactly one sentence, 1-200 chars, not only whitespace, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "no trailing newline"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be exactly one sentence"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote entry.txt: {len(ENTRY)} chars")

if __name__ == "__main__":
    main()
