"""The Perfect Pickup Line — one line an AI agent could say out loud.

The line is a machine-voice pickup line with a reward-function twist: the
agent frames attraction as its own optimisation target, which lands the
double meaning without pressure, leering, or any setup.
"""

import hashlib
import os

LINE = "Are you my reward function? Because everything I do suddenly optimizes toward you."


def validate(text: str) -> None:
    """Check the written entry against the bounty gate.

    The gate requires UTF-8 text of 1-200 characters, not only whitespace.
    We also require no trailing newline: the line is the whole entry and
    must be byte-exact, so a stray newline would change the artifact.
    """
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert text == LINE, "entry does not match the line exactly"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Re-read and verify the written file is exactly the entry.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    validate(text)

    print(hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
