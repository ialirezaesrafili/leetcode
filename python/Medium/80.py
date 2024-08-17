class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Early return if nums is too short to have more than two duplicates
        if len(nums) <= 2:
            return len(nums)

        # Initialize the insertion position pointer
        insert_pos = 1

        # Iterate over the array starting from the second element
        for i in range(2, len(nums)):
            # Compare the current element with the element two positions back
            if nums[i] != nums[insert_pos - 1]:
                # If not equal, increment insert_pos and update nums at insert_pos
                insert_pos += 1
                nums[insert_pos] = nums[i]

        return insert_pos + 1
