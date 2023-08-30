from decorator import decorator
from .transformers import TRANSFORMERS


def processor(order=1):
    """Register a transformer function to be used in the pipeline"""

    def _processor(func, *args, **kwargs):
        TRANSFORMERS[(order, func.__name__)] = func

    return _processor
