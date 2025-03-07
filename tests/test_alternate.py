import unittest
import sys
import os


sys.path.insert(0, "/Users/zlannoysg/Desktop/Testcase/src")


from alternate import alternate  

class TestAlternate(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_case_2(self):
        self.assertEqual(alternate("aaaa"), 0)

    def test_case_3(self):
        self.assertEqual(alternate("abcabcabc"), 6) 


    def test_case_4(self):
        self.assertEqual(alternate("ababababab"), 10)

    def test_case_5(self):
        self.assertEqual(alternate("a"), 0)

if __name__ == '__main__':
    unittest.main()
