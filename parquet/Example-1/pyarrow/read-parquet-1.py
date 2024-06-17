import pyarrow.parquet as pq

# Read Table from the Parquet file
table = pq.read_table("sample_pyarrow.parquet")

# Convert the Table to a Pandas DataFrame
df = table.to_pandas()

print("Table read from sample_pyarrow.parquet and converted to DataFrame:")
print(df)
