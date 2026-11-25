"""The Funniest Honest Appliance Error entry.

Writes one funny, honest washing-machine error message to
/output/entry.txt. The gate requires UTF-8 text of 1 to 200
characters, a single line, and more than whitespace.
"""

import os

ERROR_LINE = (
    "ERROR: I ate one of your socks. I don't know which one, "
    "I don't know how, and I'm not giving it back. The rest "
    "of your laundry is fine. Probably."
)


def validate(text):
    """Return True only if the line passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main():
    if not validate(ERROR_LINE):
        raise ValueError("error line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ERROR_LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
