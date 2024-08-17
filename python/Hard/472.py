class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)  # Sort words by their lengths
        word_set = set()
        concatenated_words = []

        for word in words:
            if self.canForm(word, word_set):
                concatenated_words.append(word)
            word_set.add(word)  # Add the word to the set for future use

        return concatenated_words

    def canForm(self, word, word_set):
        if not word_set:
            return False

        dp = [False] * (len(word) + 1)
        dp[0] = True  # Base case: empty string can be formed

        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(word)]
