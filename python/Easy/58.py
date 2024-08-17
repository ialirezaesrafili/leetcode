class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces
        s = s.rstrip()

        # Find the index of the last space
        last_space_index = s.rfind(' ')

        # The last word's length is the difference between the end of the string and the last space index
        return len(s) - last_space_index - 1
