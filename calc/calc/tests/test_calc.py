import unittest

from calc import (
    calculate
)

class TestCacl(unittest.TestCase):

    def test_simple_eq(self):
        self.assertEqual(calculate('1+2'), 3)
