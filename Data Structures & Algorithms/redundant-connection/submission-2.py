class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            i = find(i)
            j = find(j)

            if i == j:
                return

            if rank[i] < rank[j]:
                i, j = j, i

            rank[i] += rank[j]
            parent[j] = parent[i]
        
        for edge1, edge2 in edges:
            if find(edge1) == find(edge2):
                return [edge1, edge2]
            union(edge1, edge2)
            find(edge1)
            find(edge2)
        
        return []