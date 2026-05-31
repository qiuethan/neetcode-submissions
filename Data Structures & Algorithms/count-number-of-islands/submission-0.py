class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count_islands = 0
        visited = [[False] * len(grid[0]) for row in grid] 

        def dfs_visit(x, y):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if visited[x][y]:
                return
            
            if grid[x][y] == "0":
                return
            
            visited[x][y] = True

            dfs_visit(x - 1, y)
            dfs_visit(x + 1, y)
            dfs_visit(x, y - 1)
            dfs_visit(x, y + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                if visited[i][j]:
                    continue
                count_islands += 1
                dfs_visit(i, j)
        
        return count_islands
                