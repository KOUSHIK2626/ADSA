import unittest
from task import countGoodSubstrings

class TestAssignment(unittest.TestCase):

    def test1(self):
        self.assertEqual(countGoodSubstrings("xyzzaz"),1)

    def test2(self):
        self.assertEqual(countGoodSubstrings("aababcabc"),4)

    def test3(self):
        self.assertEqual(countGoodSubstrings( "aaaaa"),0)

if __name__ == "__main__":
    unittest.main()
