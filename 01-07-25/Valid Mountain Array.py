class Solution(object):
    def validMountainArray(self, arr):
        index=len(arr)
        i=0
        for i in range(0,index-1): 
            if arr[i+1]>arr[i]:
                continue
            else:
                break
        if i==0 or i==index-1:
            return False
        for j in range(index-1,i,-1):
            if arr[j-1]>arr[j]: 
                continue
            else:
                return False
        return True 
