
from quantools.qutils.namedclass import NamedClass

class Qbit(NamedClass):

    def __init__(self, name):
        NamedClass.__init__(self, name)
        self.__state = None

    @property
    def state(self):
        return self.__state
