import unittest
from exponent import exponent


class TestExponent(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(exponent(2, 3), 8)

    def test_power_zero(self):
        self.assertEqual(exponent(5, 0), 1)

    def test_power_one(self):
        self.assertEqual(exponent(7, 1), 7)

    def test_zero_base(self):
        self.assertEqual(exponent(0, 5), 0)

    def test_negative_base_even_power(self):
        self.assertEqual(exponent(-2, 2), 4)

    def test_negative_base_odd_power(self):
        self.assertEqual(exponent(-2, 3), -8)

    def test_large_numbers(self):
        self.assertEqual(exponent(10, 5), 100000)

    def test_float_base(self):
        self.assertEqual(exponent(2.5, 2), 6.25)


if __name__ == "__main__":
    unittest.main()