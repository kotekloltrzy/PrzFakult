import unittest
from src.zadanie1 import Calculator

class TestZadanie1(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(10, 5)

    def test_add(self):
        self.assertEqual(self.calculator.add(), 15)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), 50)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(), 2)

    def test_divide_by_0(self):
        b0 = Calculator(10, 0)
        with self.assertRaises(ValueError):
            b0.divide()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()