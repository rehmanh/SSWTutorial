import unittest
from MathFunctions import MathFunctions


class TestMathFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.math_funcs = MathFunctions()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def testAdd_returns_correct_integer_when_two_numbers_provided(self):
        # assemble
        a = 10
        b = 15
        expected = 25
        # act
        result = self.math_funcs.add(a)
        # assert
        self.assertEqual(result, expected, 'Add method works as expected')

    def testSubtract_returns_correct_integer_when_two_numbers_provided(self):
        # assemble
        a = 4
        b = 2
        expected = 2
        # act
        result = self.math_funcs.subtract(a, b)
        # assert
        self.assertEqual(result, expected, 'Subtract Method works as expected')

    def testMultiply_returns_correct_integer_when_two_numbers_provided(self):
        # assemble
        a = 5
        b = 6
        expected = 30
        # act
        result = self.math_funcs.multiply(a, b)
        # assert
        self.assertEqual(result, expected, 'Multiply Method works as expected')

    def testDivide_returns_correct_integer_when_two_numbers_provided(self):
        # assemble
        a = 800
        b = 20
        expected = 40
        # act
        result = self.math_funcs.divide(a, b)
        # assert
        self.assertEqual(result, expected, 'Divide Method works as expected')


if __name__ == '__main__':
    print('Running unit tests for MathFunctions')
    unittest.main(exit=False, verbosity=2)
