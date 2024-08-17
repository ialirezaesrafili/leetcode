class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        n = len(nums)

        for group in groups:
            group_length = len(group)
            # Search for the `group` in `nums` starting from index `i`
            while i <= n - group_length:
                if nums[i:i + group_length] == group:
                    i += group_length  # Move index `i` to the end of the found group
                    break
                i += 1
            else:
                # If we exit the while loop without breaking, we didn't find the group
                return False

        return True
