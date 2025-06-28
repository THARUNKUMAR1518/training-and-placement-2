class Solution(object):
    def addToArrayForm(self, num, k):
        result=[]
        n=len(num)-1
        while k>0 or n>=0:
            if n>=0:
                k+=num[n]
            result.append(k%10)
            k//=10
            n-=1
        result.reverse()
        return result
