import unittest
from number_game import *

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_math_quiz_addition(self):
        # We pass correct answers to simulate user answers
        score, questions = math_quiz('+', [q[2] for q in [(1, 2, 3), (4, 3, 7), (5, 5, 10), (2, 3, 5), (0, 0, 0)]])
        self.assertEqual(score, 5)  # All answers are correct

    def test_math_quiz_subtraction(self):
        # We pass some incorrect answers
        score, questions = math_quiz('-', [1, 0, 5, -1, 0])
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 5)

if __name__ == '__main__':
    unittest.main()
