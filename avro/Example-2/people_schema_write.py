import fastavro
from fastavro.schema import load_schema


# Define a function to write Avro records to a file
def write_avro_file(filename, schema, records):
    with open(filename, "wb") as f:
        fastavro.writer(f, schema, records)


# Example data records
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
]

# Avro schema (Version 1) reading from the file system
schema_v1 = load_schema("person_schema_v1.avsc")

# Filename for Avro file
avro_filename = "people.avro"

# Write Avro file using initial schema (Version 1)
write_avro_file(avro_filename, schema_v1, people)

print(f"Avro file '{avro_filename}' with schema version 1 successfully created.")
