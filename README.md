# Godspeed

## Memory Efficient Python Text Stream Transformer

![Project Logo](project_logo.png)

Welcome to the Godspeed project! 

This project provides a versatile and memory-efficient solution for processing and transforming text streams in Python. Whether you're dealing with large text files, real-time data streams, or any scenario where memory is a concern, this tool aims to meet your needs.

## Features

- **Memory Efficiency**: This project prioritizes memory efficiency, making it suitable for processing large text data without consuming excessive memory resources.
- **Stream Processing**: The core functionality revolves around processing text streams. You can read text data line by line or in chunks, avoiding loading the entire content into memory.
- **Flexible Transformation**: The project enables you to define custom transformation functions to process the text data as it streams through the system.
- **Easy-to-Use**: The provided API is designed to be user-friendly, making it accessible for developers of various skill levels.
- **Integration**: The project can seamlessly integrate into various data processing pipelines, ETL workflows, and text analysis applications.

## Installation

You can install the package from the Python Package Index (PyPI) using `pip`:

```bash
pip install godspeed
```

## Usage

- **Custom Transformation**: Define your custom transformation function that takes a line of text as input and returns the transformed line. This function can perform any operation you need, such as text manipulation, data extraction, or filtering.
- **Process Stream**: Use the TextStreamProcessor class to process the text stream. Provide the input and output file handles along with your custom transformation function.
- **Efficient Processing**: The library processes the text stream line by line, minimizing memory usage. It's suitable for situations where loading the entire text data into memory is not feasible.

## Example

To illustrate the usage of this library, here's a simple example that reads a text file, ensures each row has an equal number of columns, and make it available again for further processing:

```
from godspeed import godspeed, processor


@processor(order=1)
def ensure_equal_columns(chunk, width=10, sep=","):
    """Ensure that all rows have the same number of columns"""
    chunk = chunk.rstrip("\n")
    if chunk.count(sep) < width:
        chunk += sep * (width - chunk.count(sep)) + "\n"
    return chunk


file = open("large_file.csv")
with godspeed(file_obj) as f:
    for chunk in f:
      pass # Do something with the line (post processing)
```

## Contributions

Contributions to this project are welcome! If you have suggestions, bug reports, or want to add new features, feel free to open issues and pull requests on the GitHub repository.
License

This project is licensed under the MIT License.
