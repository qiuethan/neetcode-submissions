class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0]*(n+1)
        ways[0] = 1

        for i in range(1, n + 1):
            if i - 1 >= 0:
                ways[i] += ways[i-1]
            if i - 2 >= 0:
                ways[i] += ways[i-2]

        print(ways)

        return ways[n]
