__author__ = 'Shiva'

import int_roman_conversion as inrc

def romanToInt(romanNum):
    '''
    Converts roman number to Integer.

    '''
    converter = inrc.IntRomanConverter()
    return converter.romanToInt(romanNum)

def intToRoman(num):
    '''
    Converts integer to roman num.

    '''
    converter = inrc.IntRomanConverter()
    return converter.intToRoman(num)
