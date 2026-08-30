
import sys
import math

# Default value of epsilon
EPS = 1e-5

# Read input line by line
for raw in sys.stdin:

    # Remove the newline and extra spaces
    line = raw.rstrip("\n").strip()

    # Ignore empty lines
    if not line:
        continue

    # If the line changes EPS
    if line.startswith("EPS "):
        EPS = float(line[4:])

    # If the line contains a vector to normalize
    elif line.startswith("NORM "):

        # Get everything after "NORM "
        # Split by comma
        # Convert each value from string to float
        x = [float(v) for v in line[5:].split(",")]

        # Number of features
        D = len(x)

        # 1. Calculate the mean
        mean = sum(x) / D

        # 2. Calculate the variance
        var = sum((v - mean) ** 2 for v in x) / D

        # 3. Calculate the denominator
        denominator = math.sqrt(var + EPS)

        # 4. Normalize every value
        y = [(v - mean) / denominator for v in x]

        # 5. Print each value with exactly 4 decimal places
        print(",".join(f"{v:.4f}" for v in y))

