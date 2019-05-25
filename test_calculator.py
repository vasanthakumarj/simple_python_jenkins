import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    ops = Calculator(10, 15)

    def test_sum(self):
        self.assertEqual(self.ops.sum(), 25)

    def test_sub(self):
        self.assertEqual(self.ops.sub(), -5)

if __name__ == "__main__":
    unittest.main()
