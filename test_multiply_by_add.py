import unittest
from multiply_by_add import multiply_by_add


class TestMultiplyByAdd(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply_by_add(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_by_add(5, 0), 0)

    def test_zero_by_number(self):
        self.assertEqual(multiply_by_add(0, 7), 0)

    def test_one(self):
        self.assertEqual(multiply_by_add(1, 8), 8)

    def test_negative_multiplier(self):
        self.assertEqual(multiply_by_add(3, -4), -12)

    def test_negative_multiplicand(self):
        self.assertEqual(multiply_by_add(-3, 4), -12)

    def test_both_negative(self):
        self.assertEqual(multiply_by_add(-3, -4), 12)

    def test_large_numbers(self):
        self.assertEqual(multiply_by_add(100, 50), 5000)


if __name__ == "__main__":
    unittest.main()