'''
A Python class to convert Integer to Roman and Vice Versa
Created by Shiva Bhusal

It can convert the numbers in the range ( 1 - 4999 )
'''
import sys

intToRomanDict={
1:'I',
2:'II', 
3:'III', 
4:'IV', 
5:'V',
6:'VI', 
7:'VII', 
8:'VIII', 
9:'IX', 
10:'X', 
50:'L', 
100:'C',
500:'D',
1000:'M'
}

romanIntDict={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

class IntRomanConverter:
    def intToRoman(self,N):
        '''
        :type s : int
        :rtype: str

        '''
        if N in intToRomanDict:
            return intToRomanDict[N]
        else:
            roman = ""
            if N > 1000:
                q = int(N/1000)
                rem = N %1000
                for i in range(q):
                    roman = roman + self.intToRoman(1000)
                if rem:
                    roman = roman + self.intToRoman(rem)

            elif N > 500 and N <1000:
                q = int(N/500)
                rem = N%500
                for i in range(q):
                    roman = roman+self.intToRoman(500)
                if rem:
                    roman = roman + self.intToRoman(rem)
            elif N > 100 and N <500:
                q = int(N/100)
                rem = N%100
                for i in range(q):
                    roman = roman + self.intToRoman(100)
                if rem:
                    roman = roman + self.intToRoman(rem)
            elif N > 50 and N <100:
                q = int(N/50)
                rem = N%50
                for i in range(q):
                    roman = roman + self.intToRoman(50)
                if rem:
                    roman = roman + self.intToRoman(rem)
            elif N >10 and N <50:
                q = int(N/10)
                rem = N%10
                for i in range(q):
                    roman = roman + self.intToRoman(10)
                if rem:
                    roman = roman + self.intToRoman(rem)
            else:
                return intToRomanDict[N]

            return roman

    def romanToInt(self,romanNum):
        '''
        type romanNum : str
        rtype : int
        '''
        num = 0
        i=0
        j=1
        if romanNum in romanIntDict:
            return romanIntDict[romanNum]
        else:
            while (i<len(romanNum) and j<len(romanNum)):
                if romanIntDict[romanNum[i]]<romanIntDict[romanNum[j]]:
                    num = num + romanIntDict[romanNum[j]] - romanIntDict[romanNum[i]]
                    i= i+2
                    j=j+2
                    if i == len(romanNum)-1:
                        num = num +romanIntDict[romanNum[i]]
                else:
                    num = num+ romanIntDict[romanNum[i]]
                    if i+1 ==len(romanNum)-1:
                        num = num+ romanIntDict[romanNum[i+1]]
                    i=i+1
                    j =j+1
            return num

obj = IntRomanConverter()
for i in range(1,100):
    print(obj.intToRoman(i))
