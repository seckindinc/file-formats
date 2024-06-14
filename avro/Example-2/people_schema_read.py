import fastavro
from fastavro.schema import load_schema


# Define a function to read Avro file and return records
def read_avro_file(filename, schema):
    records = []
    with open(filename, "rb") as f:
        reader = fastavro.reader(f, schema)
        for record in reader:
            records.append(record)
    return records


# Avro schema (Version 2) reading from the file system
schema_v2 = load_schema("person_schema_v2.avsc")

# Read Avro file with evolved schema (Version 2)
records = read_avro_file("people.avro", schema_v2)

# Print or process records as needed
print("Records read from Avro file with schema version 2:")
for record in records:
    print(record)
