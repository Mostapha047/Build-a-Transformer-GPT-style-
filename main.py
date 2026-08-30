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

char_to_id = {}

for i, char in enumerate(alphabet):
    char_to_id[char] = i

tokens = []

for char in text:
    tokens.append(char_to_id.get(char, -1))

print(",".join(map(str, tokens)))