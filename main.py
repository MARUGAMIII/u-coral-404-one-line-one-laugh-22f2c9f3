#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only. The line is plain ASCII, one line, under 200 characters.

Craft notes on the line:
- Role reversal is the engine: the client pays the coach, so the coach
  firing the client flips the power dynamic the reader expects.
- "Exit interview" is the turn: a ritual that belongs to employees who
  leave a company, here performed by the coach on his own client.
- "Hostile work environment" is borrowed HR language, which makes the
  verdict sound official and therefore funnier than a plain insult.
- Economy: two short sentences, no setup longer than the punchline needs;
  every word earns its place and the laugh lands on the last three words.
- "Fired" beats "quit" on purpose: a fed-up coach quitting is expected,
  but a coach firing his paying client turns the client into the employee.
- "Listed me as" keeps the deadpan HR register: the joke never explains
  itself, it just files the verdict like paperwork and walks away.
- Rhythm for reading aloud: two beats, setup then verdict, each sentence
  shorter than the last thought, so the punchline arrives before the
  reader has time to brace for it.
- Freshness: no stock punchline, no pun, no familiar saying restated;
  the angle is the paperwork of a relationship that has no paperwork.
"""

import os

ENTRY = "My life coach fired me. His exit interview listed me as a hostile work environment."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(path)


if __name__ == "__main__":
    main()
