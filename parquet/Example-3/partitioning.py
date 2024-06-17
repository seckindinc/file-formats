import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

# Create a sample DataFrame
data = {
    "id": [1, 2, 3, 4, 5, 6],
    "value": [10, 20, 30, 40, 50, 60],
    "category": ["A", "B", "A", "B", "A", "B"],
}
df = pd.DataFrame(data)

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Specify the output directory for the partitioned Parquet files
output_dir = "partitioned_parquet"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write the table to a partitioned Parquet file
pq.write_to_dataset(table, root_path=output_dir, partition_cols=["category"])

print(f"Data written to partitioned Parquet files in directory '{output_dir}'")
