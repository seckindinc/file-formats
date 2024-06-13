import fastavro


# Define a function to write Avro records to a file
def write_avro_file(filename, schema, records):
    """
    This function takes three parameters: filename (the name of the Avro file to be created),
    schema (the Avro schema defined in JSON format), and records (a list of dictionaries representing individual
    records to be serialized into Avro format)
    """
    with open(filename, "wb") as f:
        fastavro.writer(f, schema, records)


# Example data records
# The people list contains two dictionaries, each representing a person with attributes such as name, age, city, and skills.

people = [
    {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "skills": [
            "Python",
            "Data Analysis",
            "Machine Learning",
        ],
    },
    {
        "name": "Bob",
        "age": 25,
        "city": "San Francisco",
        "skills": [
            "Java",
            "Big Data",
            "Cloud Computing",
        ],
    },
]

# Schema variable holds the Avro schema that describes the structure of the data. It specifies a record type named Person with fields name (string), age (integer), city (string), and skills (array of strings).
schema = {
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "city", "type": "string"},
        {
            "name": "skills",
            "type": {
                "type": "array",
                "items": "string",
            },
        },
    ],
}

# Filename for Avro file
avro_filename = "people.avro"

# Write Avro file
write_avro_file(avro_filename, schema, people)

print(f"Avro file '{avro_filename}' successfully created.")
