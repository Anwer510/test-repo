import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_mean(self):
        self.assertEqual(self.calc.mean([1, 2, 3, 4, 5]), 3.0)

    def test_median_odd(self):
        self.assertEqual(self.calc.median([1, 3, 5]), 3)

    def test_median_even(self):
        self.assertEqual(self.calc.median([1, 2, 3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
