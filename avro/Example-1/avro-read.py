import fastavro


# Function to read Avro file and return records
def read_avro_file(filename):
    records = []
    with open(filename, "rb") as f:
        reader = fastavro.reader(f)
        for record in reader:
            records.append(record)
    return records


# Example usage
avro_filename = "people.avro"

# Read Avro file and get records
records = read_avro_file(avro_filename)

# Print or process records as needed
for record in records:
    print(record)
