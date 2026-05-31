class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        count_islands = 0
        visited = [[False] * len(grid[0]) for row in grid] 

        def dfs_visit(x, y, value):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if visited[x][y]:
                return
            
            if grid[x][y] == 0:
                return
            
            visited[x][y] = True
            grid[x][y] = value

            dfs_visit(x - 1, y, value)
            dfs_visit(x + 1, y, value)
            dfs_visit(x, y - 1, value)
            dfs_visit(x, y + 1, value)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                count_islands += 1
                dfs_visit(i, j, count_islands)
        
        island_size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    if grid[i][j] not in island_size:
                        island_size[grid[i][j]] = 0
                    island_size[grid[i][j]] += 1
        
        if len(island_size) == 0:
            return 0

        return max(island_size.values())
                    
                