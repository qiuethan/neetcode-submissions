class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count_paths = [[0] * n for i in range(m)]

        count_paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    count_paths[i][j] += count_paths[i-1][j]
                if j > 0:
                    count_paths[i][j] += count_paths[i][j-1]
        
        return count_paths[m-1][n-1]