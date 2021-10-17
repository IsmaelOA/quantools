

class NamedClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{}-{} at {}'.format(self.__class__.__name__, self.name, hex(id(self)))

    def __repr__(self):
        return self.__str__()