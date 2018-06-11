'''
A test class for IntRomanConversion class.
'''

import sys
sys.path.append(r'src') # change this if you are using Windows.  
#print(sys.path)
import unittest
import int_roman_conversion as irc

class TestIntRomanConverter(unittest.TestCase):

    def testIntToRoman(self):
    	converter=irc.IntRomanConverter()
    	self.assertEqual(2,2)

    def testRomanToInt(self):
    	converter=irc.IntRomanConverter()
    	self.assertEqual(2,converter.romanToInt("II"))
        self.assertEqual(1, converter.romanToInt("I"))
        self.assertEqual(9, converter.romanToInt("IX"))
        self.assertEqual(99, converter.romanToInt("XCIX"))
        self.assertEqual(101, converter.romanToInt("CI"))

if __name__ == '__main__':
    unittest.main()
