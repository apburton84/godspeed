# ⚡ Godspeed IO

## Memory Efficient Stream Processor

Welcome to the Godspeed project! 

This project provides a versatile and memory-efficient solution for processing and transforming text streams in Python. 
Whether you're dealing with large text files, real-time data streams, or any scenario where memory is a concern, this tool aims to meet your needs.

## Features

- **Memory Efficiency**: This project prioritizes memory efficiency, making it suitable for processing large text data without consuming excessive memory resources.
- **Stream Processing**: The core functionality revolves around processing text streams. You can read text data line by line or in chunks, avoiding loading the entire content into memory.
- **Flexible Transformation**: The project enables you to define custom transformation functions to process the text data as it streams through the system.
- **Easy-to-Use**: The provided API is designed to be user-friendly, making it accessible for developers of various skill levels.
- **Integration**: The project can seamlessly integrate into various data processing pipelines, ETL workflows, and text analysis applications.

## ⚒️  Installation

You can install the package from the Python Package Index (PyPI) using `pip`:

```bash
pip install godspeedio
```

## 🪧 Usage

- **Custom Transformation**: Define your custom transformation function that takes a line of text as input and returns the transformed line. This function can perform any operation you need, such as text manipulation, data extraction, or filtering.
- **Process Stream**: Use the `godspeedio()` function to process the text stream. Provide the input and output file handles along with your custom transformation function.
- **Efficient Processing**: The library processes the text stream line by line, minimizing memory usage. It's suitable for situations where loading the entire text data into memory is not feasible.

## 📣 Example

To illustrate the usage of this library, here's a simple example that reads a text file, ensures each row has an equal number of columns, and make it available again for further processing:

```python
from godspeedio import godspeed, processor


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
from godspeedio import godspeed, processor
```

- This line imports two components from the "godspeedio" library: the `godspeed` function and the `processor` decorator.

2.The `@processor` Decorator:

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

- This part of the code demonstrates how to use the `godspeedio` library to process a large CSV file.
- It opens the file named "large_file.csv".
- The `godspeed` function is used as a context manager by passing the file object `file` to it.
- Inside the context, a loop iterates over the chunks (lines) of the file.
- Sequencially applying the transformations to each line.

## 📣 Example - state management

This code sample demonstrates how to use the state management functionality provided by the `godspeedio` library. The primary purpose of this code appears to be to process a large CSV file while maintaining and updating some state information as it processes each line. Let's break down the code and focus on the state management aspect:

```python
from godspeedio import godspeed, processor


@processor(state=True)
def add_relationship(chunk, state):
    # this will be true for the first row
    if "01" == chunk[0:2]:
        state.set("parent_id", chunk.split("*")[1])
    return chunk.rstrip("\n") + "*" + state.get("parent_id") + "\n"


file = open("large_file.csv")
with godspeed(file_obj) as f:
    for chunk in f:
        pass  # Do something with the line (post processing)
```

1. Importing Dependencies:

 ```python
 from godspeedio import godspeed, processor
 ```

 - The code imports two modules from the `godspeedio` library: `godspeed` and `processor`. These modules are used for file input/output and defining custom processing functions.

2. Defining a Custom Processor Function with State:

```python
@processor(state=True)
def add_relationship(chunk, state):
  # this will be true for the first row
  if "01" == chunk[0:2]:
     state.set("parent_id", chunk.split("*")[1])
  return chunk.rstrip("\n") + "*" + state.get("parent_id") + "\n"
```

- The `@processor(state=True)` decorator is used to create a custom processing function called `add_relationship`. The `state=True` argument indicates that this function will use a state object to store and share data between processing iterations.
- Inside this function:
  - It checks if the first two characters of the `chunk` are equal to "01". If this condition is met, it extracts information from the chunk and stores it in the state object using `state.set()`.
  - It modifies the `chunk` by appending some data extracted from the state object and removing any trailing newline characters.
  - Finally, it returns the modified `chunk`.

3. Opening and Reading the CSV File:

```python
file = open("large_file.csv")
with godspeed(file_obj) as f:
   for chunk in f:
       pass  # Do something with the line (post processing)
```

- The script opens a CSV file named "large_file.csv" for reading and assigns it to the `file` variable.
- It then uses a `godspeed` context manager (`with godspeed(file_obj) as f`) to read the file line by line. The `with` statement ensures that the file is properly closed after processing.
- Inside the loop (`for chunk in f:`), each line (or chunk) from the CSV file is processed. However, the loop currently contains a placeholder (`pass`), indicating that the actual post-processing logic needs to be implemented here.

In summary, this example showcases the use of the `godspeedio` library's state management functionality, allowing you to maintain and update shared data (in this case, "parent_id") while processing a large CSV file. The actual post-processing logic should be implemented inside the loop to take advantage of the state information stored in the `add_relationship` function.

```python
from godspeedio import godspeed, processor


@processor(state=True)
def add_relationship(chunk, state):
    # this will be true for the first row
    if "01" == chunk[0:2]:
        state.set("parent_id", chunk.split("*")[1])
    return chunk.rstrip("\n") + "*" + state.get("parent_id") + "\n"


file = open("large_file.csv")
with godspeed(file_obj) as f:
    for chunk in f:
        pass  # Do something with the line (post processing)
```

1. Importing Dependencies:
   ```python
   from godspeedio import godspeed, processor
   ```
   - The code imports two modules from the `godspeedio` library: `godspeed` and `processor`. These modules are used for file input/output and defining custom processing functions.

2. Defining a Custom Processor Function with State:
   ```python
   @processor(state=True)
   def add_relationship(chunk, state):
       # this will be true for the first row
       if "01" == chunk[0:2]:
           state.set("parent_id", chunk.split("*")[1])
       return chunk.rstrip("\n") + "*" + state.get("parent_id") + "\n"
   ```
   - The `@processor(state=True)` decorator is used to create a custom processing function called `add_relationship`. The `state=True` argument indicates that this function will use a state object to store and share data between processing iterations.
   - Inside this function:
     - It checks if the first two characters of the `chunk` are equal to "01". If this condition is met, it extracts information from the chunk and stores it in the state object using `state.set()`.
     - It modifies the `chunk` by appending some data extracted from the state object and removing any trailing newline characters.
     - Finally, it returns the modified `chunk`.

3. Opening and Reading the CSV File:
   ```python
   file = open("large_file.csv")
   with godspeed(file_obj) as f:
       for chunk in f:
           pass  # Do something with the line (post processing)
   ```
   - The script opens a CSV file named "large_file.csv" for reading and assigns it to the `file` variable.
   - It then uses a `godspeed` context manager (`with godspeed(file_obj) as f`) to read the file line by line. The `with` statement ensures that the file is properly closed after processing.
   - Inside the loop (`for chunk in f:`), each line (or chunk) from the CSV file is processed. However, the loop currently contains a placeholder (`pass`), indicating that the actual post-processing logic needs to be implemented here.

In summary, this example showcases the use of the `godspeedio` library's state management functionality, allowing you to maintain and update shared data (in this case, "parent_id") while processing a large CSV file. The actual post-processing logic should be implemented inside the loop to take advantage of the state information stored in the `add_relationship` function.

## 🙏 Contributions

Contributions to this project are welcome! If you have suggestions, bug reports, or want to add new features, feel free to open issues and pull requests on the GitHub repository.


## ⚖️ License

This project is licensed under the MIT License.
