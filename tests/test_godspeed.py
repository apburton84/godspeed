import sys
import io

sys.path.append("..")

from godspeed.streaming import GSStringWrapper
from godspeed import godspeed


def test_godspeed():
    """Test godspeed function"""
    io_string = io.StringIO("Hello World")
    assert isinstance(godspeed(io_string), GSStringWrapper)


class TestClassGSStringWrapper:
    def test_process(self):
        """Test process method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.process(io_string.read()) == "Hello World"

    def test_enter(self):
        """Test enter method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.__enter__() == processor

    def test_exit(self):
        """Test exit method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.__exit__(None, None, None) == None

    def test_iter(self):
        """Test iter method"""
        io_string = io.StringIO("Hello World")
        for s in GSStringWrapper(io_string):
            assert "Hello World"

    def test_read(self):
        """Test read method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.read() == "Hello World"

    def test_write(self):
        """Test write method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.write("Hello World") == 11

    def test_flush(self):
        """Test flush method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.flush() is None

    def test_readline(self):
        """Test readline method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.readline() == "Hello World"

    def test_readlines(self):
        """Test readlines method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.readlines() == ["Hello World"]

    def test_getvalue(self):
        """Test getvalue method"""
        io_string = io.StringIO("Hello World")
        processor = GSStringWrapper(io_string)
        assert processor.getvalue() == "Hello World"
