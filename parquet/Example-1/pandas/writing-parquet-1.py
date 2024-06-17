import pandas as pd

# Create a sample DataFrame
data = {"column1": [1, 2, 3], "column2": ["A", "B", "C"], "column3": [0.1, 0.2, 0.3]}
df = pd.DataFrame(data)

# Write DataFrame to a Parquet file
df.to_parquet(
    "sample.parquet", engine="pyarrow"
)  # we select engine as pyarrow. I recommend not to use fastparquet as it is depricated
print("DataFrame written to sample.parquet")
