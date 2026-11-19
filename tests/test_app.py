import unittest
from app import add_numbers


class TestAddition(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
