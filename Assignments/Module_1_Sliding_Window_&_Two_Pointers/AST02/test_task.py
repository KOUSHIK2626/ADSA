import unittest
from task import Check_Palindrome

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Check_Palindrome(4,'abca'),True)

    def test_multiple_digits(self):
        self.assertEqual(Check_Palindrome(4,'batr'),False)

    def test_with_zero(self):
        self.assertEqual(Check_Palindrome(5,'abcba'),True)

if __name__ == "__main__":
    unittest.main()
