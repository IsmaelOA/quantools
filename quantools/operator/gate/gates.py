
from quantools.operator.gate.base import Gate

__all__ = ['CNOT']

class CNOT(Gate):

    def __init__(self, name):
        Gate.__init__(self, name)

