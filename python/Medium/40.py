class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(start, target, path):
            if target == 0:
                # Found a valid combination
                results.append(path[:])
                return
            if target < 0:
                # No need to continue if target is negative
                return

            for i in range(start, len(candidates)):
                # Skip duplicate numbers
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Include candidates[i] in the combination
                path.append(candidates[i])
                # Recur with reduced target and next start position
                backtrack(i + 1, target - candidates[i], path)
                # Exclude candidates[i] from the combination and backtrack
                path.pop()

        candidates.sort()  # Sort to handle duplicates
        results = []
        backtrack(0, target, [])
        return results
