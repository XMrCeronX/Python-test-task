import unittest
from solution import sum_two


class TestCalculator(unittest.TestCase):
    def test_default(self):
        self.assertEqual(sum_two(1, 2), 3)
        with self.assertRaises(TypeError) as cm:
            sum_two(1, 2.4)
        self.assertEqual('Типы параметров не должны различаться' in cm.exception.args[0], True)

    def test_int_and_int(self):
        self.assertEqual(sum_two(88, 2), 90)
        self.assertEqual(sum_two(5, 2), 7)
        self.assertEqual(sum_two(99, 4), 103)
        self.assertEqual(sum_two(4525, 434), 4959)

    def test_raise(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.0)
        with self.assertRaises(TypeError):
            sum_two(1, False)
        with self.assertRaises(TypeError):
            sum_two(1, '2.4')
        self.assertEqual(sum_two(1, 55), 56)
