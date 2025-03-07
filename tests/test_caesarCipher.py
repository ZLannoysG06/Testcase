import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from caesarCipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")

    def test_case_2(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    def test_case_3(self):
        self.assertEqual(caesarCipher("abc", 0), "abc")

    def test_case_4(self):
        self.assertEqual(caesarCipher("zab", 1), "abc")

if __name__ == '__main__':
    unittest.main()
