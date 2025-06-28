class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        # Step 1: Compute prefix sums
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        min_length = float('inf')

        # Step 2: Check all subarrays
        for start in range(n):
            for end in range(start, n):
                subarray_sum = prefix[end + 1] - prefix[start]
                if subarray_sum >= target:
                    min_length = min(min_length, end - start + 1)

        return 0 if min_length == float('inf') else min_length
