import unittest
from divide_by_subtract import divide_by_subtract


class TestDivideBySubtract(unittest.TestCase):

    def test_exact_division(self):
        self.assertEqual(divide_by_subtract(10, 2), 5)

    def test_integer_division(self):
        self.assertEqual(divide_by_subtract(7, 2), 3)

    def test_divide_by_one(self):
        self.assertEqual(divide_by_subtract(9, 1), 9)

    def test_zero_dividend(self):
        self.assertEqual(divide_by_subtract(0, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(divide_by_subtract(-10, 2), -5)

    def test_negative_divisor(self):
        self.assertEqual(divide_by_subtract(10, -2), -5)

    def test_both_negative(self):
        self.assertEqual(divide_by_subtract(-10, -2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_by_subtract(10, 0)


if __name__ == "__main__":
    unittest.main()