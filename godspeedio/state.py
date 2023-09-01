class State:
    """Global state object."""

    def set(self, key, value):
        """Set a value on the state object."""
        setattr(self, key, value)

    def get(self, key):
        """Get a value from the state object."""
        try:
            return getattr(self, key)
        except AttributeError:
            return None

_state = State()

def get_state():
    """Get the global state object."""
    return _state
