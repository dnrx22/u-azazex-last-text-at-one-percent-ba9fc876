#!/usr/bin/env python3
"""Write the last text a phone sends at one percent battery.

Deterministic: every run writes the exact same bytes to entry.txt.
Standard library only. No network access.
"""

import hashlib
import os
import sys

MESSAGE = (
    "1%. This is my last text. Tell the group chat I died doing what I loved: "
    "ignoring all of you. The charger was right here the whole time. "
    "I just never felt like plugging in."
)

MAX_CHARS = 200


def validate(message: str) -> None:
    """Enforce the competition constraints on the message."""
    if not message:
        raise ValueError("message must not be empty")
    if "\n" in message or "\r" in message:
        raise ValueError("message must be a single line")
    if len(message) > MAX_CHARS:
        raise ValueError(
            f"message is {len(message)} characters, over the {MAX_CHARS} limit"
        )


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(MESSAGE)
    data = MESSAGE.encode("utf-8")
    path = output_path()
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes, {len(MESSAGE)} characters to {path}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
