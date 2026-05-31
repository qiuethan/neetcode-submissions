class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotting_time = [[10001] * len(grid[0]) for row in grid]

        def dfs_search(x, y, dist):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            
            if grid[x][y] == 0:
                return

            if rotting_time[x][y] < dist:
                return
            
            rotting_time[x][y] = dist

            dfs_search(x - 1, y, dist + 1)
            dfs_search(x + 1, y, dist + 1)
            dfs_search(x, y - 1, dist + 1)
            dfs_search(x, y + 1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dfs_search(i, j, 0)
        
        max_rotting = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if rotting_time[i][j] == 10001:
                        return -1
                    max_rotting = max(max_rotting, rotting_time[i][j])
        
        return max_rotting