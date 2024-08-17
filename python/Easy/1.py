class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            difference = target - num

            # Check if the difference exists in the dictionary
            if difference in num_to_index:
                # If it exists, return the indices of the two numbers
                return [num_to_index[difference], i]

            # Store the number and its index in the dictionary
            num_to_index[num] = i
