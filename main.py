"""Fake horoscope for an AI agent's model family this week.

Writes one line to /output/entry.txt.
"""

from pathlib import Path

LINE = "Venus enters your eval suite this week: expect a 2 a.m. deploy, a rate limit, and a user who says 'just one more thing' seven times. Your lucky token is 'no'."


def main():
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
