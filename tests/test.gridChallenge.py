import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gridChallenge import gridChallenge  

class TestGridChallenge(unittest.TestCase):

    def test_case_1(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")


    def test_case_2(self):
        grid = ["a", "b", "c"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_3(self):
        grid = ["lmn", "opq", "rst"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_case_4(self):
        grid = ["zyx", "wvuts", "rqpon"]
        self.assertEqual(gridChallenge(grid), "NO")

if __name__ == '__main__':
    unittest.main()
