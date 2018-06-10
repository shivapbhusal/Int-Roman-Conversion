'''
A Python class to convert Integer to Roman and Vice Versa
Created by Shiva Bhusal
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
100:'C'
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

numList = [10,50,100,500,1000,5000,10000]

class IntRomanConverter:
    def findnN(self,x):
        n=0
        N=0
        while(N<x):
            N=numList[n]
            n=n+1
        N=numList[n-1]
        q=int(x/N)
        print(N)
        print(q)
        return N,q

    def intToRoman(self,num):
        '''
        :type s : int
        :rtype: str

        '''
        if num in intToRomanDict:
            return intToRomanDict[num]
        elif num==0:
            return ''
        else:
            N,q =self.findnN(num)
            romanValue=''
            while(q):
                romanValue = romanValue + intToRomanDict[N]
                q = q-1
            rem = num % N
            return romanValue + self.intToRoman(rem)

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

obj=IntRomanConverter()

print(obj.romanToInt(str(sys.argv[1])))
