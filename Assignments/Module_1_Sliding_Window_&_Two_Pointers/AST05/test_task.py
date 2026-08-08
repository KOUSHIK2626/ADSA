import unittest
from task import productExceptSelf

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(productExceptSelf([10, 3, 5, 6, 2]),[180, 600, 360, 300, 900])

    def test_multiple_digits(self):
        self.assertEqual(productExceptSelf([12, 0]),[0, 12])

    def test_with_zero(self):
        self.assertEqual(productExceptSelf([1,2,3,4]),[24,12,8,6])

if __name__ == "__main__":
    unittest.main()
