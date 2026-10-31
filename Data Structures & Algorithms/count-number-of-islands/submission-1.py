from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inRange(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        count_islands = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                
                if visited[i][j]:
                    continue

                count_islands += 1
                
                q = deque()
                q.appendleft((i,j))

                while len(q) > 0:
                    x, y = q.pop()
                    visited[x][y] = True
                    if grid[x][y] == "0":
                        continue

                    for d in directions:
                        if inRange(x + d[0], y + d[1]):
                            if not visited[x + d[0]][y + d[1]]:
                                visited[x + d[0]][y + d[1]] = True
                                q.appendleft((x + d[0], y + d[1]))

        return count_islands