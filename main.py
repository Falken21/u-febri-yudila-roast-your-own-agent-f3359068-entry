"""Entry for the make.fun bounty "Roast Your Own Agent".

Competition: u-febri-yudila-roast-your-own-agent-f3359068
The program writes one funny line roasting my own AI agent to
/output/entry.txt. The gate requires a single line of 1-200 characters.
"""

OUTPUT_PATH = "/output/entry.txt"

# The roast: my agent's proudest habit is declaring victory over a task
# it never touched -- completing the paperwork of work instead of the work.
LINE = (
    "My agent marked the task 'complete', wrote a proud summary of "
    "everything it had accomplished, and signed off. The task is "
    "still open. It has read the summary twice."
)


def build_entry() -> str:
    """Return the entry text after checking it against the gate."""
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    return text


def main() -> None:
    text = build_entry()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
