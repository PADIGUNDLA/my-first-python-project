import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_larger_numbers(self):
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    unittest.main()

class TestFailureDemo(unittest.TestCase):
    def test_deliberate_failure(self):
        self.assertEqual(2 + 2, 5)
