class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = [[-1]*len(text2) for i in range(len(text1))]

        def calculateLongest(text1index, text2index):
            if text1index >= len(text1) or text2index >= len(text2):
                return 0
            if text1[text1index] == text2[text2index]:
                memo[text1index][text2index] = 1 + calculateLongest(text1index + 1, text2index + 1)
            elif memo[text1index][text2index] == -1:
                memo[text1index][text2index] = max(calculateLongest(text1index + 1, text2index), calculateLongest(text1index, text2index + 1))

            return memo[text1index][text2index]

        calculateLongest(0,0)

        return memo[0][0]