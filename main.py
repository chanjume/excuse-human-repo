#!/usr/bin/env python3
"""Write one original excuse line to /output/entry.txt.

The line is the excuse an AI agent gives its human for a missed
deadline, in the agent's own voice. The joke turns on the agent's own
situation: the work was done at 9 a.m., then the human asked it to
"just quickly" change one thing -- 14 times. One concrete number and
a quoted phrase the human actually uses, with a twist in the last
words that redefines who caused the delay. One line, under 200 chars.
"""
import os

LINE = "It was done at 9 a.m. \u2014 then you asked me to \u201cjust quickly\u201d change one thing, 14 times."
# 86 chars: done at 9 a.m., undone by fourteen "just quickly" requests.


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
