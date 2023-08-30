TRANSFORMERS = {}


def sort_transformers(transformers):
    """Sort the transformers by order"""
    return sorted(transformers.items(), key=lambda x: x[0][0])
