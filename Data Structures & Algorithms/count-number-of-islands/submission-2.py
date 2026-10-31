from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        count_islands = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inRange(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def searchGrid(x, y):
            if not inRange(x,y):
                return
            
            if grid[x][y] == "0":
                return

            if visited[x][y]:
                return

            visited[x][y] = True

            for d in directions:
                searchGrid(x + d[0], y + d[1])
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                
                if visited[i][j]:
                    continue

                count_islands += 1
                
                searchGrid(i, j)

        return count_islands