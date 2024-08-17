class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def kadane(arr):
            max_ending_here = max_so_far = 0
            for x in arr:
                max_ending_here = max(0, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        def prefix_suffix_max_sum(arr):
            max_prefix_sum = current_sum = 0
            for x in arr:
                current_sum += x
                max_prefix_sum = max(max_prefix_sum, current_sum)

            max_suffix_sum = current_sum = 0
            for x in reversed(arr):
                current_sum += x
                max_suffix_sum = max(max_suffix_sum, current_sum)

            return max_prefix_sum, max_suffix_sum

        # Compute prefix and suffix maximum sums
        max_prefix_sum, max_suffix_sum = prefix_suffix_max_sum(arr)
        total_sum = sum(arr)

        # Max subarray sum for the array once
        max_subarray_sum = kadane(arr)

        # Case 1: Single array
        if k == 1:
            return max_subarray_sum % MOD

        # Case 2: Two arrays
        combined_max = max_suffix_sum + max_prefix_sum

        # Case 3: More than two arrays
        if total_sum > 0:
            combined_max = max(combined_max, max_suffix_sum + max_prefix_sum + (k - 2) * total_sum)

        return max(max_subarray_sum, combined_max) % MOD
