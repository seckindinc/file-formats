import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

# Create a sample PyArrow Table
data = {"column1": [1, 2, 3], "column2": ["A", "B", "C"], "column3": [0.1, 0.2, 0.3]}
table = pa.Table.from_pandas(pd.DataFrame(data))

# Write Table to a Parquet file
pq.write_table(table, "sample_pyarrow.parquet")
print("Table written to sample_pyarrow.parquet")
