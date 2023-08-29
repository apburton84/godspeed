from godspeed import godspeed, processor


@processor(order=1)
def ensure_equal_columns(chunk, width=10, sep=","):
    """Ensure that all rows have the same number of columns"""
    chunk = chunk.rstrip("\n")
    if chunk.count(sep) < width:
        chunk += sep * (width - chunk.count(sep)) + "\n"
    return chunk


@profile
def performance_test():
    file = open("sample_data_10mb.csv", "rb")
    for chunk in godspeed(file):
        pass


if __name__ == "__main__":
    performance_test()
