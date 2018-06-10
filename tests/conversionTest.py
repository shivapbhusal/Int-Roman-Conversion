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
    	self.assertEqual()

    def testRomanToInt(self):
    	converter=irc.IntRomanConverter()
    	self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()