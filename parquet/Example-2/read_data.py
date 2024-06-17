import pyarrow.parquet as pq

# Read the Parquet file
table = pq.read_table("sample.parquet")

# Convert the table to a Pandas DataFrame
df = table.to_pandas()

print("Data read from sample.parquet:")
print(df)
