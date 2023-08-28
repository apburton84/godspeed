import io

from godspeed import IOStreamer, consume
from godspeed import processor, consumer
from godspeed import to_uppercase, multiply, add_newline, ensure_column_width

# Usage Examples

# Example 1: Using the consumer function
#
# with open("test.txt", "w") as f:
#     f.write("hello world")
#
# with open("test.txt", "r") as f:
#     stream = consume(f)
#     print(stream.getvalue())
#
# Output:
# Processing chunk: 'hello world', <class 'str'>, 11
# Applying transformer: to_uppercase
# Applying transformer: multiply
# Applying transformer: add_newline
# Applying transformer: ensure_column_width
# HELLO WORLD
#

newline = "\n"

# Example 2: Using the IOStreamer class
#
# In this example let's correct the column width of the is comma separated data

f = io.StringIO(f"1,2,3,4{newline}1,2,3,4{newline}1,2,3{newline}")
stream = IOStreamer(f)

print(stream.getvalue())

# Output:
# Processing chunk: 'hello world', <class 'str'>, 11
# Applying transformer: to_uppercase
# Applying transformer: multiply
# Applying transformer: add_newline
# Applying transformer: ensure_column_width
# HELLO WORL
#

# Example 3: Using the processor decorator
#
# @processor(order=2)
# def to_uppercase(chunk):
#     """ Transform a string to uppercase """
#     return chunk.upper()
#

# Example 4: Using the consumer decorator
#
# @consumer
# def consume(stream):
#     for chunk in stream:
#         yield chunk
#
# with open("test.txt", "w") as f:
#     f.write("hello world")
#
# with open("test.txt", "r") as f:
#     stream = consume(f)
#     print(stream.getvalue())
#
# Output:
# Processing chunk: 'hello world', <class 'str'>, 11
# Applying transformer: to_uppercase
# Applying transformer: multiply
# Applying transformer: add_newline
# Applying transformer: ensure_column_width
# HELLO WORLD



#  stream = io.StringIO("hello world nice to meet you")
#  res = consume(stream).getvalue()
#  print(f"post processing: '{res}'")

