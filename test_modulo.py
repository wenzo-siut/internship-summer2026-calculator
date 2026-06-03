import unittest
from modulo import modulo


class TestModulo(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_even_division(self):
        self.assertEqual(modulo(12, 4), 0)

    def test_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_negative_divisor(self):
        self.assertEqual(modulo(10, -3), -2)

    def test_float_numbers(self):
        self.assertAlmostEqual(modulo(10.5, 3), 1.5)

    def test_large_numbers(self):
        self.assertEqual(modulo(1000001, 1000), 1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            modulo("10", 3)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            modulo(None, 3)


if __name__ == "__main__":
    unittest.main()