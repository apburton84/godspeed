from decorator import decorator
from .transformers import TRANSFORMERS


def processor(order=1, state=False):
    """Register a transformer function to be used in the pipeline"""

    def _processor(func, *args, **kwargs):
        TRANSFORMERS[(order, func.__name__, state)] = func

    return _processor
