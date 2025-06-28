class Solution(object):
    def repeatedNTimes(self, nums):
        res = []
        for num in nums:
            if num in res:
                return num
            else:
                res.append(num)
