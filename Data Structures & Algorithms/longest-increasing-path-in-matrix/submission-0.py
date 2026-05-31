class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        memo = [[0]*len(matrix[0]) for i in range(len(matrix))]

        def dfs(x, y, last):
            
            if x < 0 or x >= len(matrix):
                return 0
            if y < 0 or y >= len(matrix[0]):
                return 0
            
            if last >= matrix[x][y]:
                return 0

            if memo[x][y] != 0:
                return memo[x][y]
            
            count = 1

            count = max(count, dfs(x - 1, y, matrix[x][y]) + 1)
            count = max(count, dfs(x + 1, y, matrix[x][y]) + 1)
            count = max(count, dfs(x, y - 1, matrix[x][y]) + 1)
            count = max(count, dfs(x, y + 1, matrix[x][y]) + 1)

            memo[x][y] = count

            return memo[x][y]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)

        max_length = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, memo[i][j])

        return max_length

        
            

            
