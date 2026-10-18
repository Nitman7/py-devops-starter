import unittest
from main import greet, add_numbers


class TestMain(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("John"), "Hello, John! Welcome to DevOps learning.")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 7), 12)
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
