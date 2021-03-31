import unittest
import AddBinary


class Tester(unittest.TestCase):
    def test_addBinary(self):
        a = AddBinary.Solution()
        self.assertEqual(a.addBinary("101", "1011"), "10000")
        self.assertEqual(a.addBinary("11", "1"),  "100")
        self.assertEqual(a.addBinary("1010", "1011"), "10101")


"""
Personal note: make sure you have unit tests as 'test_filename.py'.
For some reason, VSCode is confused about which AddBinary to use, so 
having test_AddBinary adds clear distinction.
"""
