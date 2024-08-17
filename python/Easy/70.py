class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the first two steps
        first = 1
        second = 2

        # Iterate from 3 to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second
