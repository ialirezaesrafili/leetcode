class Solution:
    def concatenatedBinary(self, n):
        MOD = 10 ** 9 + 7
        result = 0
        length = 0

        for i in range(1, n + 1):
            # If i is a power of 2, increment the length of binary representation
            if i & (i - 1) == 0:
                length += 1

            # Shift the current result to the left and add the new number i
            result = ((result << length) | i) % MOD

        return result
