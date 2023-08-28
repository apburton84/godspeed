from decorator import decorator

import io


TRANSFORMERS = {}

def processor(order=1):
    """ Register a transformer function to be used in the pipeline """
    def _processor(func, *args, **kwargs):
        print(f"Registering transformer: {func.__name__}")
        TRANSFORMERS[(order, func.__name__)] = func
    return _processor

def sort_transformers(transformers):
    """ Sort the transformers by order """
    return sorted(transformers.items(), key=lambda x: x[0][0])

class IOStreamer(io.StringIO):
    """ A stream of data """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._transformers = sort_transformers(TRANSFORMERS)

    def process(self, chunk):
        print(f"Processing chunk: '{chunk}', {type(chunk)}, {len(chunk)}")
        if isinstance(chunk, str):
            for transformer in self._transformers:
                print(f"Applying transformer: {transformer[0][1]}")
                chunk = transformer[1](chunk)


    def write(self, chunk):
        """ Write a chunk of data to the stream """
        super().write(self.process(chunk))

    def read(self, *args, **kwargs):
        """ Read from the stream """
        return self.process(super().read(*args, **kwargs))  

    def getvalue(self, *args, **kwargs):
        """ Get the value from the stream """
        return self.process(super().getvalue(*args, **kwargs))  


@decorator
def consumer(func, *args, **kwargs):
    """ Decorator to process a stream of data

    Different transformations can be applied to the stream of data.

    args:
        func: function to be decorated
        *args: positional arguments
        **kwargs: keyword arguments

    returns:
        decorated function
    """
    stream = io.StringIO()
    for chunk in func(*args, **kwargs):
        print(f"Processing chunk: '{chunk}', {type(chunk)}, {len(chunk)}")
        if isinstance(chunk, str):
            for transformer in sort_transformers(TRANSFORMERS):
                print(f"Applying transformer: {transformer[0][1]}")
                chunk = transformer[1](chunk)
            stream.write(chunk)
    return stream

@consumer
def consume(stream):
    """ Load a stream of data """
    for line in stream.read(1024):
        yield line

if __name__ == "__main__":
    stream = io.StringIO("hello world nice to meet you")
    res = consume(stream).getvalue()

    print(f"post processing: '{res}'")
