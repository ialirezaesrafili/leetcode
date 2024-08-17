class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total_sum = carry

            if i >= 0:
                total_sum += int(a[i])
                i -= 1

            if j >= 0:
                total_sum += int(b[j])
                j -= 1

            result.append(str(total_sum % 2))  # Append the current bit (0 or 1)
            carry = total_sum // 2  # Calculate the new carry

        # Since we added bits from the end to the start, reverse the result
        return ''.join(reversed(result))
