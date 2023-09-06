import io
from decorator import decorator
from .state import get_state
from .transformers import TRANSFORMERS, sort_transformers


class GSStringWrapper(io.StringIO):
    """A stream of data

    Usage:
        >>> stream = GSStringWrapper()
        >>> stream.write("Hello World!")
        >>> stream.getvalue()
        'Hello World!'

    Attributes:
        _stream: The stream to wrap
        _transformers: The transformers to apply to the stream
    """

    def __init__(self, *args, **kwargs):
        """Initialize the stream

        Args:
            *args: Arguments to pass to the stream
            **kwargs: Keyword arguments to pass to the stream
        """
        super().__init__()

        self._stream = args[0] if len(args) > 0 else io.StringIO()

        self._transformers = sort_transformers(TRANSFORMERS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __enter__(self):
        """Enter the stream"""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the stream

        Args:
            exc_type: The type of exception
            exc_value: The value of the exception
            traceback: The traceback of the exception
        """
        return self._stream.__exit__(exc_type, exc_value, traceback)

    def __iter__(self):
        """Iterate over the stream"""
        for line in self._stream.__iter__():
            if "" == line:
                yield False
            yield self.process(line)

    def process(self, chunk):
        """Process a chunk of data

        Args:
            chunk: The chunk of data to process
        """
        if chunk:
            for transformer in self._transformers:
                if transformer[0][2]:
                    chunk = transformer[1](chunk, get_state())
                else:
                    chunk = transformer[1](chunk)

        return chunk

    def next(self):
        """Get the next line from the stream"""
        return self.process(self._stream.next())

    def write(self, chunk):
        """Write a chunk of data to the stream"""
        return self._stream.write(self.process(chunk))

    def read(self, *args, **kwargs):
        """Read from the stream"""
        resp = self._stream.read(*args, **kwargs)
        if resp is None or "" == resp:
            return resp

        if self.delimiter != resp[-1]:
            resp += self.read_until(self.delimiter)

        post = ""
        for split in resp.split(self.delimiter):
            post += self.process(split)

        return post

    def read_until(self, delimiter):
        """Read until a delimiter is found or EOF"""
        resp = ""
        while True:
            read_one = self._stream.read(1)
            if read_one is None:
                break
            elif resp[-1] == delimiter:
                break
            else:
                resp += read_one

        return resp

    def readline(self, *args, **kwargs):
        """Read a line from the stream"""
        return self.process(self._stream.readline(*args, **kwargs))

    def readlines(self, *args, **kwargs):
        """Read all lines from the stream"""
        return self.process(self._stream.readlines(*args, **kwargs))

    def getvalue(self, *args, **kwargs):
        """Get the value from the stream"""
        return self.process(self._stream.getvalue(*args, **kwargs))

    def flush(self, *args, **kwargs):
        """Flush the stream"""
        return self._stream.flush(*args, **kwargs)


def godspeed(stream: io.StringIO, *args, **kwargs) -> GSStringWrapper:
    """Wrap a stream in a GSStringWrapper

    The purpose of this function is to allow the user to wrap any stream in a
    GSStringWrapper without having to import the class directly.

    Args:
        stream: The stream to wrap

    Returns:
        The wrapped stream

    Usage:
        >>> from godspeed import godspeed, processor
        >>> @processor()
        ... def hello_world(chunk):
        ...     return chunk.replace("Hello", "Goodbye")
        ...
        >>> stream = godspeed(io.StringIO())
        >>> stream.write("Hello World!")
        >>> stream.getvalue()
        'Goodbye World!'
    """
    return GSStringWrapper(stream, *args, **kwargs)
