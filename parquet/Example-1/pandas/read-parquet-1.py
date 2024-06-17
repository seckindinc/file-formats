import pandas as pd

# Read DataFrame from the Parquet file
df = pd.read_parquet("sample.parquet", engine="pyarrow")

print("DataFrame read from sample.parquet:")
print(df)
