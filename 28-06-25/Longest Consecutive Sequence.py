class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a set of nums for O(1) lookup
        set_nums = set(nums)

        # Initialize the variable for the longest sequence found
        longest = 0

        # Iterate over each number in the set
        for n in set_nums:
            # Only start counting if 'n-1' is NOT in the set
            # This ensures we only count sequences starting from the smallest number
            if (n - 1) not in set_nums:
                length = 0
                # As long as the next number in the sequence is present, keep counting
                while (n + length) in set_nums:
                    length += 1
                # Update the longest length found so far
                longest = max(longest, length)

        # Return the longest length
        return longest
