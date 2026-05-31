class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def dfs_search(x, y, dist):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            
            if grid[x][y] < dist:
                return
            
            grid[x][y] = dist

            dfs_search(x - 1, y, dist + 1)
            dfs_search(x + 1, y, dist + 1)
            dfs_search(x, y - 1, dist + 1)
            dfs_search(x, y + 1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs_search(i, j, 0)
        
        return
            
