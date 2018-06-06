'''
A Python class to convert Integer to Roman and Vice Versa
Created by Shiva Bhusal
'''

digits={
1:'I',
2:'II', 
3:'III', 
4:'IV', 
5:'V',
6:'VI', 
7:'VII', 
8:'VIII', 
9:'IX', 
10:'X'
}

class IntRomanConverter:
    def intToRoman(self,num):
        if num in digits:
            return digits[num]          

    def romanToInt(self,romanNum):
        return '10'

obj=IntRomanConverter()

print(obj.intToRoman(20))
