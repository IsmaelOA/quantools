
import logging
import unittest
import collections

logging.basicConfig(level=logging.DEBUG)

from quantools.operator.gate import CNOT

class TestBasic(unittest.TestCase):
    def test_basic(self):
        
        cnot = CNOT('my_cnot_gate')
        print(cnot)
        