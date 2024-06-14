import fastavro
from fastavro.schema import load_schema
import csv

# Avro schema definition
avro_schema = {
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "city", "type": "string"},
    ],
}


# Function to write Avro file with compression
def write_avro_file_with_compression(csv_filename, avro_filename, schema, compression):
    records = []
    # Read CSV file
    with open(csv_filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "age": int(row["age"]),
                    "city": row["city"],
                }
            )
            # Limit to avoid excessive memory usage during demonstration
            if len(records) >= 1_000_000:
                break

    # Write Avro file with compression
    with open(avro_filename, "wb") as f:
        fastavro.writer(f, schema, records, codec=compression)


# File path for the Avro file
avro_file = "compressed_data.avro"
compression_codec = (
    "snappy"  # Change this to 'deflate', 'bzip2', or 'xz' for other compression options
)

# Write Avro file with compression
write_avro_file_with_compression(
    "large_file.csv", avro_file, avro_schema, compression_codec
)

print(
    f"Avro file '{avro_file}' with compression '{compression_codec}' successfully created."
)
