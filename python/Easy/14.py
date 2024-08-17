class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start by assuming the whole first string is the common prefix
        prefix = strs[0]

        # Compare the assumed prefix with each string
        for s in strs[1:]:
            # Reduce the prefix length until it matches the start of the current string
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
