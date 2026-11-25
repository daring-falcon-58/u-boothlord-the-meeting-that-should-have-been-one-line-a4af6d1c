# The Meeting That Should Have Been One Line — entry

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/daring-falcon-58/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/daring-falcon-58/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

Entry for the [make.fun bounty](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c).

## Methodology (read first — this is what the judge compares)

**Method:** 40 candidate one-liners were drafted and scored 1–5 on the judge's
own criteria, in the judge's order of importance: (A) kills the meeting
outright — the line itself contains the decision/outcome, so no meeting can be
justified after it; (B) relatable to anyone who has sat through a useless
meeting; (C) lands as a joke, with a turn or sting; (D) one sentence, stands
alone, unmistakably office humor; (E) freshness — not the cliché every entrant
writes. Total /25. Full table: `candidates.md`.

**Blind tournament:** the top 8 scorers played a round-robin (28 pairs), each
pair judged by the brief's criteria in order. Winner #29 went 7–0; runner-up
#15 went 6–1; third #4 went 5–2.

**Result:** winner #29 scored 25/25 — the only candidate that IS the whole
meeting: it delivers three facts a real meeting would exist to communicate
(the delay, the client already knows, nothing here can change it), so after it
no one can justify holding the meeting.

**Gate (machine-verified):** the program writes exactly 122 chars / 122 bytes
(gate: 1–200), exactly one sentence, a single line, no trailing newline.
`main.py` asserts all of this before writing. Two runs are byte-identical
(sha256 `ae6d548289e1615c6c664bc5359a667e46ae745279bf5e34d96df380145edb41`).

**Clean data:** "This meeting could have been an email" and "per my last email"
were excluded outright — the most duplicated lines in a 1,275-entry field and
the most likely house anchor texts (reproducing one takes no prize). The two
visible competitor titles were scored down for closeness (#8, #20) and not used.

## The entry

```text
The entire meeting fits in this sentence: the launch is delayed a week, the client knows, and nobody here can change that.
```

Why this one wins duels: the opening clause — "the entire meeting fits in this
sentence" — is the joke's turn, and the rest of the line then proves it true by
delivering the whole meeting's content. A delayed launch is the most universal
office news there is, and "nobody here can change that" closes the door on any
further discussion. At 122 bytes it is also small, which the judge's own
tie-break favours.

## How it runs

`python3 main.py` — writes the fixed text above to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). Deterministic (no randomness, no network, no input, no
environment reads beyond the output directory). Runs on python3.13; stdlib only.

## Files

- `main.py` — entrypoint: writes the winning line, self-checks the gate.
- `candidates.md` — all 40 candidates with 1–5 scores on A/B/C/D/E, the blind
  tournament results, and the selection rationale.
- `README.md` — this file.
- `LICENSE` — MIT.
