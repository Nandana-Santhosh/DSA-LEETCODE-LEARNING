'''Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1 '''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power=0
        i=0
        while i<=n/2:
            i=pow(2,power)
            if i==n:
                return True
            power+=1
        return False
    

class Solution:
def isPowerOfTwo(self, n: int) -> bool:
        
        while n>=1:
            if n==1:
                 return True
            elif n%2==0 :   '''on changing 2 to 3/4 we can check the power of those number too'''
             n=n/2

            else:
                return False
            

        