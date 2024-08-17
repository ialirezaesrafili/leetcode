class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the last digit and move left
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # Increment the current digit by one
            if digits[i] < 10:  # No carry, just return the result
                return digits
            digits[i] = 0  # If the digit is 10, set it to 0 and continue

        # If we finished the loop, all digits were 9 and are now 0
        return [1] + digits
