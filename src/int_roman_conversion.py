'''
A Python class to convert Integer to Roman and Vice Versa
Created by Shiva Bhusal
'''
import sys

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
10:'X', 
50:'L', 
100:'C',
1000:'M'
}

class IntRomanConverter:
    def findnN(self,x):
        n=0
        N=0
        while(N<x):
            N=pow(10,n)
            n=n+1
        N=N/10
        q=int(x/N)
        return N,q

    def intToRoman(self,num):
        if num in digits:
            return digits[num]
        elif num==0:
            return ''
        else:
            N,q =self.findnN(num)
            print(N)
            print(q)
            romanValue=''
            while(q):
                romanValue = romanValue + digits[N]
                q = q-1
            rem = num % N
            return romanValue + self.intToRoman(rem)

    def romanToInt(self,romanNum):
        return '10'

obj=IntRomanConverter()

print(obj.intToRoman(int(sys.argv[1])))
