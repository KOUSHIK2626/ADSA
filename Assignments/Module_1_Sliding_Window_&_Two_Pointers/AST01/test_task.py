import unittest
from task import The_Great_Run

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(The_Great_Run(7,2,[2,4,8,1,2,1,8]),12)

    def test_multiple_digits(self):
        self.assertEqual(The_Great_Run(5,3,[1,2,3,4,5]),12)

    def test_with_zero(self):
        self.assertEqual(The_Great_Run(8,4,[5,2,8,1,9,3,7,4]),23)

if __name__ == "__main__":
    unittest.main()
