from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_dict = {}

        for edge in edges:
            if edge[0] not in adj_dict:
                adj_dict[edge[0]] = []
            if edge[1] not in adj_dict:
                adj_dict[edge[1]] = []
            adj_dict[edge[0]].append(edge[1])
            adj_dict[edge[1]].append(edge[0])
        
        q = deque()
        previous = deque()
        visited = set()

        q.append(0)
        previous.append(-1)

        while len(q) > 0:
            node = q.popleft()
            prev = previous.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            if node not in adj_dict:
                continue

            for neighbour in adj_dict[node]:
                if neighbour == prev:
                    continue
                q.append(neighbour)
                previous.append(node)

        if len(visited) != n:
            return False
        
        return True

        