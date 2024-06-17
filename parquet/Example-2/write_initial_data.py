import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Mapping for data types
type_mapping = {"int64": pa.int64(), "string": pa.string(), "float64": pa.float64()}

# Load the initial schema
with open("schema_initial.json", "r") as f:
    schema_json = json.load(f)
fields = [
    pa.field(field["name"], type_mapping[field["type"]], field["nullable"])
    for field in schema_json["fields"]
]
schema_initial = pa.schema(fields)

# Create a sample DataFrame matching the initial schema
data_initial = {"column1": [1, 2, 3], "column2": ["A", "B", "C"]}
df_initial = pd.DataFrame(data_initial)

# Convert the DataFrame to a PyArrow Table with the initial schema
table_initial = pa.Table.from_pandas(df_initial, schema=schema_initial)

# Write the table to a Parquet file
pq.write_table(table_initial, "sample.parquet")
print("Initial data written to sample.parquet")
