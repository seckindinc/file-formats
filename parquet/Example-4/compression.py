import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("dummy_data.csv")

# Define the schema for PyArrow based on DataFrame types
schema = pa.Schema.from_pandas(df)

# Define options for Parquet writer (e.g., compression type)
parquet_writer = pq.ParquetWriter(
    "dummy_data_compressed.parquet", schema, compression="gzip"
)

# Write data to Parquet file
table = pa.Table.from_pandas(df, schema=schema)
parquet_writer.write_table(table)

# Close the Parquet writer
parquet_writer.close()

print("CSV data successfully converted and stored in compressed Parquet format.")
