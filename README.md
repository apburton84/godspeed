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

```python
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

The main goal of the code is to ensure that all rows in the CSV file have the same number of columns by padding the rows with separators if necessary.

Let's break down the code step by step and explain its functionality:

1. Import Statements:

```python
from godspeed import godspeed, processor
```

- This line imports two components from the "godspeed" library: the `godspeed` function and the `processor` decorator.

2. `@processor(order=1)` Decorator:

```python
@processor(order=1)
def ensure_equal_columns(chunk, width=10, sep=","):
   """Ensure that all rows have the same number of columns"""
   chunk = chunk.rstrip("\n")
   if chunk.count(sep) < width:
       chunk += sep * (width - chunk.count(sep)) + "\n"
   return chunk
```

- We define a transformation function `ensure_equal_columns` and decorated it with `@processor(order=1)`. 
- The `order=1` argument indicates the order in which processors will be applied. With the `deault=0`
- The function takes three parameters:
  - `chunk`: A single line (chunk) read from the CSV file.
  - `width`: The desired width (number of columns) for each row.
  - `sep`: The separator used in the CSV file (default is a comma `,`).
- The function's purpose is to ensure that each line (row) in the CSV file has the same number of columns. It does this by counting the occurrences of the separator in the current chunk. If the count is less than the desired width, it pads the chunk with additional separators to match the desired width. Finally, it returns the modified chunk.

3. File Handling and Processing:

```python
file = open("large_file.csv")
with godspeed(file_obj) as f:
   for chunk in f:
       pass # Do something with the line (post processing)
```

- This part of the code demonstrates how to use the `godspeed` library to process a large CSV file.
- It opens the file named "large_file.csv".
- The `godspeed` function is used as a context manager by passing the file object `file` to it.
- Inside the context, a loop iterates over the chunks (lines) of the file.
- Sequencially applying the transformations to each line.


**Ease of Use:**

The "godspeed" library simplifies the process of efficiently processing large CSV files by breaking down the processing steps into smaller, manageable functions. By using the `@processor` decorator, you can define individual processing functions and apply them in a specified order. This modular approach makes the code more readable, maintainable, and extensible.

The provided `ensure_equal_columns` function demonstrates how you can easily add custom processing steps to manipulate the data in chunks before further processing. This can be especially useful when dealing with CSV files that might have inconsistencies in their structure.

In summary, the code showcases a streamlined approach to processing large CSV files using the "godspeed" library, making it easier to manage and modify various processing tasks while efficiently handling large datasets.

## Contributions

Contributions to this project are welcome! If you have suggestions, bug reports, or want to add new features, feel free to open issues and pull requests on the GitHub repository.
License

This project is licensed under the MIT License.
