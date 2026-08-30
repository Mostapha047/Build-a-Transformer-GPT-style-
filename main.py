import sys

vocab_size = 0
embedding_dim = 0
embedding_table = []
tokens = []

for raw in sys.stdin:
    line = raw.rstrip("\n")

    if line.startswith("VOCAB "):
        parts = line.split()
        vocab_size = int(parts[1])
        embedding_dim = int(parts[3])

        # Read the next V lines containing the embedding table
        for _ in range(vocab_size):
            row_line = next(sys.stdin).rstrip("\n")
            row = [float(x) for x in row_line.split(",")]
            embedding_table.append(row)

    elif line.startswith("TOKENS "):
        token_text = line[len("TOKENS "):]
        tokens = [int(x) for x in token_text.split(",")]

for token_id in tokens:
    if 0 <= token_id < vocab_size:
        row = embedding_table[token_id]
    else:
        row = [0.0] * embedding_dim

    formatted = [f"{x:.4f}" for x in row]
    print(",".join(formatted))