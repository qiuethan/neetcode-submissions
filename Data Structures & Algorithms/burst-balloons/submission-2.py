class Solution:
        
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * (n + 2) for i in range(n + 2)]

        for length in range(1, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1

                for i in range(l, r + 1):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][i - 1] + arr[l - 1] * arr[i] * arr[r + 1] + dp[i + 1][r]
                    )

        return dp[1][n]
