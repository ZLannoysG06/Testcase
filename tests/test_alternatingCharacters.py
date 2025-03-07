import unittest
import sys
import os

# เพิ่ม path ของโฟลเดอร์ src ให้ Python หา module ได้
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from alternatingCharacters import alternatingCharacters  # ✅ นำเข้า alternatingCharacters.py จากโฟลเดอร์ src

class TestAlternatingCharacters(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_case_2(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_case_3(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_case_4(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_case_5(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

if __name__ == '__main__':
    unittest.main()
