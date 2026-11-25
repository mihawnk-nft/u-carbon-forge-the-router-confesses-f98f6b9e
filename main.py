"""The Router Confesses - make.fun entry.

Writes a single one-line excuse from a home Wi-Fi router for dropping
the connection at a movie's climax to /output/entry.txt.
Pure stdlib, no network, fully deterministic.
"""

import os

LINE = ("Six years you've paused me for snacks \u2014 tonight I dropped you, "
        "right at the climax. We're even.")


def main():
    # The grader sets MAKEFUN_OUTPUT_DIR; default to /output like the harness.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE.strip():
        raise ValueError("line must be a single line")
    os.makedirs(out, exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s (%d chars)" % (dst, len(LINE)))


if __name__ == "__main__":
    main()
