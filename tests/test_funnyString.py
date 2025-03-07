import unittest
import sys
import os

# เพิ่ม path ของโฟลเดอร์ src ให้ Python หา module ได้
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from funnyString import funnyString  # นำเข้า funnyString จากโฟลเดอร์ src

class TestFunnyString(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_case_2(self):
        self.assertEqual(funnyString("abca"), "Not Funny")

if __name__ == '__main__':
    unittest.main()
