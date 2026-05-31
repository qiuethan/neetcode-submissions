class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = [[-1] * len(t) for i in range(len(s))]

        def countWays(sIndex, tIndex):

            if tIndex == len(t):
                return 1

            if sIndex >= len(s):
                return 0

            if memo[sIndex][tIndex] != -1:
                return memo[sIndex][tIndex]

            totalWays = 0

            if s[sIndex] == t[tIndex]:
                totalWays += countWays(sIndex + 1, tIndex + 1)
            
            totalWays += countWays(sIndex + 1, tIndex)

            memo[sIndex][tIndex] = totalWays

            return memo[sIndex][tIndex]
    
        countWays(0,0)

        return memo[0][0]