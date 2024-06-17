import pandas as pd
import random
import string

# Define the number of rows
num_rows = 10000000

# Generate random data
data = {
    "id": range(1, num_rows + 1),
    "value1": [random.random() * 100 for _ in range(num_rows)],
    "value2": [random.randint(1, 1000) for _ in range(num_rows)],
    "category": [random.choice(["A", "B", "C"]) for _ in range(num_rows)],
    "text": [
        "".join(random.choices(string.ascii_letters, k=10)) for _ in range(num_rows)
    ],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("dummy_data.csv", index=False)

print(f"Generated {num_rows} rows of dummy data and saved to dummy_data.csv")
