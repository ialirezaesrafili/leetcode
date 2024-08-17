class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the element at the 'k' index if it is not equal to 'val'
                nums[k] = nums[i]
                k += 1

        return k