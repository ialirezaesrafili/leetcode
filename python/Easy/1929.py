class Solution:
    def getConcatenation(self, nums):
        """
        Given an integer array nums, this function returns an array ans
        of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
        for 0 <= i < n.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * (2 * n)  # Create an array of size 2n

        for i in range(n):
            ans[i] = nums[i]  # First half is nums
            ans[i + n] = nums[i]  # Second half is also nums

        return ans
