from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        qx = deque()
        qy = deque()
        distance = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    qx.append(i)
                    qy.append(j)
                    distance.append(0)

        neighbours = [[-1,0], [1, 0], [0, -1], [0, 1]]

        while not len(qx) == 0:
            x = qx.popleft()
            y = qy.popleft()
            dist = distance.popleft()

            for i, j in neighbours:
                if x + i < 0 or x + i >= len(grid):
                    continue
                if y + j < 0 or y + j >= len(grid[0]):
                    continue
                if grid[x + i][y + j] == -1:
                    continue
                if grid[x + i][y + j] == 2147483647:
                    grid[x + i][y + j] = dist + 1
                    qx.append(x + i)
                    qy.append(y + j)
                    distance.append(dist + 1)
        
        return