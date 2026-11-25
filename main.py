"""The Router Confesses - make.fun entry.

Writes a single one-line excuse from a home Wi-Fi router for dropping
the connection at a movie's climax to /output/entry.txt.
Pure stdlib, no network, fully deterministic.
"""

import os

LINE = ("Six years you've paused me for snacks \u2014 tonight I dropped you, "
        "right at the climax. We're even.")

DST = "/output/entry.txt"


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE.strip():
        raise ValueError("line must be a single line")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s (%d chars)" % (DST, len(LINE)))


if __name__ == "__main__":
    main()
