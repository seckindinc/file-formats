import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Define the schema
schema = pa.schema(
    [
        ("id", pa.int32()),
        ("name", pa.string()),
        ("age", pa.int32()),
        ("city", pa.string()),
    ]
)

# Read the CSV file into a Pandas DataFrame
csv_file = "large_file.csv"
df = pd.read_csv(csv_file)

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df, schema=schema)

# Define the output Parquet file
parquet_file = "compressed_sample.parquet"

# Write the table to a Parquet file with compression
pq.write_table(table, parquet_file, compression="SNAPPY")

print(f"Data from '{csv_file}' written to compressed Parquet file '{parquet_file}'")
