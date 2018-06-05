'''
A Python class to convert Integer to Roman and Vice Versa
Created by Shiva Bhusal
'''

digits={1:'I',
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
        if num<=10 and num>0:
        	return digits[num%10]
        elif num==0:
        	return 
        else:
        	if num%10==0:
        		return self.intToRoman(digits[num])
        	else:
        		return self.intToRoman(digits[num])+self.intToRoman(digits[num%10])

    def romanToInt(self,romanNum):
        return '10'

obj=IntRomanConverter()

print(obj.intToRoman(20))