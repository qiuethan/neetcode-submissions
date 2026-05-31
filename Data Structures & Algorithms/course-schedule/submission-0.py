class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacency_matrix = [[False] * numCourses for row in range(numCourses)]
        
        for pair in prerequisites:
            adjacency_matrix[pair[0]][pair[1]] = True

        for i in range(numCourses):
            visited = [False] * numCourses
        
            def dfs(i, target):
                print(i, target, visited)
                if visited[i]:
                    if i == target:
                        return False
                    return True

                visited[i] = True
                
                for adjacent in range(len(adjacency_matrix[0])):
                    if adjacency_matrix[i][adjacent]:
                        if not dfs(adjacent, target):
                            return False
                
                return True
            
            if not dfs(i, i):
                return False

        return True