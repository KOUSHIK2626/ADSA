import unittest
from task import pairInSortedRotated

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(pairInSortedRotated([11, 15, 6, 8, 9, 10],16),True)

    def test_multiple_digits(self):
        self.assertEqual(pairInSortedRotated([11, 11, 15, 26, 38, 9, 10],35),True)

    def test_with_zero(self):
        self.assertEqual(pairInSortedRotated([9, 10, 10, 11, 15, 26, 38],45),False)

if __name__ == "__main__":
    unittest.main()
