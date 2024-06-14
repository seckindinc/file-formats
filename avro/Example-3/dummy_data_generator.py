import csv
import random
import string


# Function to generate random string
def random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


# Number of rows to generate
num_rows = 10000000

# File path for the large CSV file
csv_file = "large_file.csv"

# Create CSV file
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(["id", "name", "age", "city"])
    # Write data rows
    for i in range(num_rows):
        writer.writerow(
            [i, random_string(10), random.randint(18, 80), random_string(10)]
        )

print(f"CSV file '{csv_file}' successfully created.")
