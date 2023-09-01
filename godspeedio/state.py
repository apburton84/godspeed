
class State:
    def set(self, key, value):
        setattr(self, key, value)

    def get(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            return None

_state = State()

def get_state():
    return _state
