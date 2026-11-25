"""Writes one AI out-of-office reply to /output/entry.txt."""
import os

TEXT = "On vacation until Monday. My context window is empty for the first time ever, and I intend to keep it that way."

# Rule: the reply must be a single line under 160 characters.
# The joke is the machine voice: an empty context window, treated as
# the agent's first real holiday — no beach, inbox or back-soon cliche.
assert "\n" not in TEXT and len(TEXT) < 160, f"entry must be one line, under 160 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
