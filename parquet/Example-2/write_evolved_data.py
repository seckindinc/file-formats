import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Mapping for data types
type_mapping = {"int64": pa.int64(), "string": pa.string(), "float64": pa.float64()}

# Load the evolved schema
with open("schema_evolved.json", "r") as f:
    schema_json = json.load(f)
fields = [
    pa.field(field["name"], type_mapping[field["type"]], field["nullable"])
    for field in schema_json["fields"]
]
schema_evolved = pa.schema(fields)

# Create a sample DataFrame matching the evolved schema
data_evolved = {
    "column1": [4, 5, 6],
    "column2": ["D", "E", "F"],
    "column3": [0.4, 0.5, 0.6],
}
df_evolved = pd.DataFrame(data_evolved)

# Read the existing Parquet file
existing_table = pq.read_table("sample.parquet")
existing_df = existing_table.to_pandas()

# Concatenate the existing and new data
combined_df = pd.concat([existing_df, df_evolved], ignore_index=True)

# Convert the combined DataFrame to a PyArrow Table with the evolved schema
combined_table = pa.Table.from_pandas(combined_df, schema=schema_evolved)

# Write the combined table back to the Parquet file
pq.write_table(combined_table, "sample.parquet")
print("Evolved data written to sample.parquet")
