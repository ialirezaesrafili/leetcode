class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()

        # Binary search on the answer
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            # Count pairs with distance <= mid
            count = 0
            j = 0

            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1

            # If count is greater than or equal to k, it means we should search in the left half
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
