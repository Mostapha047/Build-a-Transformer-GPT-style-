import sys

# Character-level tokenizer.
# Parse the ALPHABET line, build a char -> index map,
# then map every char of the TEXT line. Missing chars -> -1.
alphabet = ""
text = ""
for raw in sys.stdin:
    line = raw.rstrip("\n")
    if line.startswith("ALPHABET "):
        alphabet = line[len("ALPHABET "):]
    elif line.startswith("TEXT "):
        text = line[len("TEXT "):]

# TODO: build the alphabet->index map and emit comma-separated ids.
lookup = {ch: i for i, ch in enumerate(alphabet)}
ids = [lookup.get(ch, -1) for ch in text]
print(",".join(str(n) for n in ids))