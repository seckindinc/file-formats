# File Formats

A comprehensive repository showcasing examples and resources for two widely used data serialization formats — **Avro** and **Parquet**. This project is designed for developers, data engineers, and analytics professionals who want to understand how these formats work, their use cases, and how to interact with them through practical examples.

## Project Definition

This repository provides a hands-on learning environment for comparing and understanding Avro and Parquet file formats. It includes schema definitions, sample data files, conversion scripts, and practical examples that demonstrate the strengths and use cases of each format. The project serves as both an educational resource and a practical reference for making informed decisions about data serialization in real-world applications.

## Repository Structure

```
file-formats/
├── avro/                   # Files, schemas, and scripts related to Avro
├── parquet/                # Files, schemas, and scripts related to Parquet  
├── .vscode/                # VS Code workspace settings
├── .gitignore              # Git ignore configuration
├── LICENSE                 # Apache 2.0 license file
└── README.md               # This file
```

## Purpose

The main goals of this repository are to:

- **Compare formats**: Understand the differences between Avro (row-based) and Parquet (columnar) file formats
- **Provide practical examples**: Offer hands-on examples with schemas, data files, and conversion scripts
- **Performance reference**: Create a practical reference for performance testing and schema design
- **Decision support**: Help practitioners choose the most appropriate file format for their specific workloads
- **Educational resource**: Serve as a learning tool for data serialization concepts and best practices

### Avro
- **Row-based storage format**
- Best suited for streaming pipelines and message-based systems
- Strong support for schema evolution
- Great choice for Kafka and data ingestion workflows
- Compact binary serialization with embedded schema

### Parquet
- **Columnar storage format**  
- Optimized for analytical queries over large datasets
- Highly efficient compression and reduced storage size
- Ideal for data warehouses and analytics platforms
- Excellent performance for read-heavy workloads

## How to Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/seckindinc/file-formats.git
cd file-formats
```

After cloning, you'll have access to all the examples, schemas, and scripts needed to explore both Avro and Parquet formats.

## How to Check for Examples

Once you've cloned the repository, explore the examples in each format directory:

### Avro Examples
```bash
# Navigate to Avro directory
cd avro/

# List available files and examples
ls -la

# Look for schema files (typically .avsc extension)
find . -name "*.avsc"

# Look for data files (typically .avro extension)  
find . -name "*.avro"
```

### Parquet Examples
```bash
# Navigate to Parquet directory
cd parquet/

# List available files and examples
ls -la

# Look for Parquet data files
find . -name "*.parquet"

# Look for schema or script files
find . -name "*.py" -o -name "*.json"
```

### Running Examples
Check each directory for:
- **README files** with specific instructions
- **Script files** (.py, .sh) that demonstrate format usage
- **Sample data** files for testing
- **Schema definitions** that show data structure

## When to Use

### Choose Avro When:
- Building **streaming data pipelines** (Kafka, Pulsar)
- Need **schema evolution** capabilities
- Working with **write-heavy** workloads
- Integrating with **message queues** and event streaming
- Requiring **cross-language** data exchange
- Need **compact serialization** for network transfer

### Choose Parquet When:
- Performing **analytical queries** on large datasets
- Building **data warehouses** or data lakes
- Need **efficient compression** and storage optimization
- Working with **read-heavy** analytical workloads
- Using **columnar databases** (BigQuery, Redshift, Snowflake)
- Requiring **fast aggregations** and filtering

### Consider Both When:
- Building **hybrid architectures** (streaming + analytics)
- Need **format conversion** capabilities
- Comparing **performance characteristics**
- Learning **data serialization** concepts

## License

This repository is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for the full license text.

The Apache 2.0 license allows you to:
- Use the code for any purpose (commercial or non-commercial)
- Modify and distribute the code
- Include the code in proprietary software

## Contributing

Contributions are welcome! This project benefits from community input and real-world examples.

### Ways to Contribute:
- **Add more examples** for Avro or Parquet formats
- **Include benchmarks** and performance comparisons
- **Improve documentation** and add real-world usage tips
- **Share use cases** and practical applications
- **Fix bugs** or improve existing code
- **Add new tools** or conversion utilities

### How to Contribute:

1. **Fork this repository**
   ```bash
   # Click "Fork" on GitHub or use GitHub CLI
   gh repo fork seckindinc/file-formats
   ```

2. **Create a new branch** for your feature or fix
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes**
   - Add examples, documentation, or improvements
   - Test your changes thoroughly
   - Follow existing code style and conventions

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a pull request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Provide clear descriptions of your changes
   - Reference any related issues

### Contribution Guidelines:
- Ensure your code is well-documented
- Include examples or tests where applicable
- Update README files if you add new features
- Follow the existing project structure
- Be respectful and constructive in discussions

---

**Questions or suggestions?** Feel free to [open an issue](https://github.com/seckindinc/file-formats/issues) or start a [discussion](https://github.com/seckindinc/file-formats/discussions)!
