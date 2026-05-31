class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flow = []

        pacific_flow = [[False] * len(heights[0]) for row in heights]
        pacific_visited = [[False]*len(heights[0]) for row in heights]

        atlantic_flow = [[False] * len(heights[0]) for row in heights]
        atlantic_visited = [[False]*len(heights[0]) for row in heights]

        for i in range(len(heights[0])):
            pacific_flow[0][i] = True
            atlantic_flow[-1][i] = True
        
        for i in range(len(heights)):
            pacific_flow[i][0] = True
            atlantic_flow[i][-1] = True
        
        def dfs_flow_pacific(x, y, previous):
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]):
                return
            
            if pacific_visited[x][y]:
                return
            
            if heights[x][y] < previous:
                return
            
            pacific_visited[x][y] = True
            pacific_flow[x][y] = True

            dfs_flow_pacific(x - 1, y, heights[x][y])
            dfs_flow_pacific(x + 1, y, heights[x][y])
            dfs_flow_pacific(x, y - 1, heights[x][y])
            dfs_flow_pacific(x, y + 1, heights[x][y])

        def dfs_flow_atlantic(x, y, previous):
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]):
                return
            
            if atlantic_visited[x][y]:
                return
            
            if heights[x][y] < previous:
                return
            
            atlantic_visited[x][y] = True
            atlantic_flow[x][y] = True

            dfs_flow_atlantic(x - 1, y, heights[x][y])
            dfs_flow_atlantic(x + 1, y, heights[x][y])
            dfs_flow_atlantic(x, y - 1, heights[x][y])
            dfs_flow_atlantic(x, y + 1, heights[x][y])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific_flow[i][j]:
                    dfs_flow_pacific(i, j, -1)
                if atlantic_flow[i][j]:
                    dfs_flow_atlantic(i, j, -1)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific_flow[i][j] and atlantic_flow[i][j]:
                    flow.append([i,j])
        
        return flow

