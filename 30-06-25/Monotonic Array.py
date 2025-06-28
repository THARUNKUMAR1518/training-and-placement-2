class Solution(object):
    def isMonotonic(self, nums):
        inc = True
        dic = True
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] :
                dic = False
            if nums[i]<nums[i-1] :
                inc = False

        if not inc and not dic :
            return False

        return True           
