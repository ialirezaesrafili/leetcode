class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the first pointer
        i = 0

        # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            # When a new unique element is found
            if nums[j] != nums[i]:
                i += 1  # Move the first pointer forward
                nums[i] = nums[j]  # Update the element at i with the new unique element

        # The number of unique elements is i + 1
        return i + 1
