import uuid


class SimpleElement:
    value = 0
    id = 0

    def __init__(self, value):
        self.value = value
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"Value:{self.value}, ID:{self.id}"

    def __eq__(self, other):
        if isinstance(other, SimpleElement):
            if other.value == self.value:
                return True
            else:
                return False

    def __hash__(self):
        return hash(self.value)

    def bigger_than(self, other):
        if isinstance(other, SimpleElement):
            if other.value < self.value:
                return True
            else:
                return False

    def smaller_then(self, other):
        if isinstance(other, SimpleElement):
            if other.value > self.value:
                return True
            else:
                return False
