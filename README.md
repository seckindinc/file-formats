# file-formats

## 📖 Project Definition
**file-formats** is a repository showcasing examples and resources for two widely used data serialization formats — **Avro** and **Parquet**. It is intended for developers, data engineers, and analytics professionals who want to understand how these formats work, their use cases, and how to interact with them through real examples.

## 📂 Repository Structure

file-formats/
├── avro/ # Files, schemas, and scripts related to Avro
├── parquet/ # Files, schemas, and scripts related to Parquet
├── .vscode/ # VS Code workspace settings
├── .gitignore # Git ignore configuration
└── LICENSE # Apache 2.0 license file


## 🎯 Purpose
The main goals of this repository are to:
- Compare **Avro** (row-based) and **Parquet** (columnar) file formats.
- Provide hands-on examples with schemas, data files, and conversion scripts.
- Offer a practical reference for performance testing and schema design.
- Help practitioners choose the most appropriate file format for their workloads.

## 💻 How to Clone the Repository
Clone this repository to your local machine:
git clone https://github.com/seckindinc/file-formats.git
cd file-formats

## 📌 When to Use
Avro
Row-based storage format.

Best suited for streaming pipelines and message-based systems.

Strong support for schema evolution.

Great choice for Kafka and data ingestion workflows.

Parquet
Columnar storage format.

Optimized for analytical queries over large datasets.

Highly efficient compression and reduced storage size.

Ideal for data warehouses and analytics platforms.

📄 License
This repository is licensed under the Apache License 2.0.

🤝 Contributing
Contributions are welcome! You can:

Add more examples for Avro or Parquet.

Include benchmarks and performance comparisons.

Improve documentation and add real-world usage tips.

To contribute:

Fork this repository.

Create a new branch for your feature or fix.

Submit a pull request with clear descriptions of your changes.
