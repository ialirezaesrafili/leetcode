class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                result = mid  # store potential result
                left = mid + 1  # try to find a larger value
            else:
                right = mid - 1  # find a smaller value

        return result
