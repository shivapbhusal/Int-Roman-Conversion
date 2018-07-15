'''
A test class for IntRomanConversion class.
'''

import sys
sys.path.append(r'romanInt') # change this path if you are using Windows.  
#print(sys.path)
import unittest
import int_roman_conversion as irc

class TestIntRomanConverter(unittest.TestCase):

    def testIntToRoman(self):
    	converter=irc.IntRomanConverter()
    	self.assertEqual("II", converter.intToRoman(2))
        self.assertEqual("I", converter.intToRoman(1))
        self.assertEqual("X", converter.intToRoman(10))
        self.assertEqual("IX", converter.intToRoman(9))
        self.assertEqual("XCIX", converter.intToRoman(99))
        self.assertEqual("CI", converter.intToRoman(101))
        self.assertEqual("CD", converter.intToRoman(400))
        self.assertEqual("MMXXV", converter.intToRoman(2025))

    def testRomanToInt(self):
    	converter=irc.IntRomanConverter()
    	self.assertEqual(2,converter.romanToInt("II"))
        self.assertEqual(1, converter.romanToInt("I"))
        self.assertEqual(9, converter.romanToInt("IX"))
        self.assertEqual(99, converter.romanToInt("XCIX"))
        self.assertEqual(90, converter.romanToInt("XC"))
        self.assertEqual(101, converter.romanToInt("CI"))

if __name__ == '__main__':
    unittest.main()
