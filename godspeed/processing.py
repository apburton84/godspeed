from .streaming import processor


@processor(order=2)
def to_uppercase(chunk):
    """Transform a string to uppercase"""
    return chunk.upper()


@processor(order=1)
def multiply(buffer: bytes, factor: int = 2) -> bytes:
    """Transform the data in the buffer"""
    return buffer * factor


@processor(order=3)
def add_newline(chunk):
    """Add a newline to the end of the string"""
    return chunk + "\n"


@processor(order=4)
def ensure_column_width(chunk, width=10):
    """Ensure the string is at least width characters long"""
    return chunk.ljust(width)
