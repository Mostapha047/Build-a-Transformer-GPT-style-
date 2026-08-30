import sys, math

# Sinusoidal positional encoding.
# For each "PE <pos> <d_model>" line emit d_model floats:
#   even dim -> sin(pos / 10000^(2k/d_model))
#   odd dim  -> cos(pos / 10000^(2k/d_model))
# Round to 4 decimals.

for raw in sys.stdin:

    line = raw.rstrip("\n").strip()

    if not line or not line.startswith("PE "):
        continue

    # Parse position and model dimension
    parts = line.split()

    pos = int(parts[1])
    d_model = int(parts[2])

    # Store the positional encoding values
    values = []

    # Calculate PE for every dimension
    for i in range(d_model):

        # i = 0,1 -> k = 0
        # i = 2,3 -> k = 1
        # i = 4,5 -> k = 2
        k = i // 2

        # Calculate 10000^(2k / d_model)
        denominator = 10000 ** (2 * k / d_model)

        # Calculate pos / denominator
        angle = pos / denominator

        # Even dimensions use sin
        # Odd dimensions use cos
        if i % 2 == 0:
            value = math.sin(angle)
        else:
            value = math.cos(angle)

        values.append(value)

    # Print comma-separated values with 4 decimal places
    print(",".join(f"{v:.4f}" for v in values))

