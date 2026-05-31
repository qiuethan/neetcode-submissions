class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        djs = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def parent(i):
            if djs[i] == i:
                return i
            
            djs[i] = parent(djs[i])
            return djs[i]
        
        def union(i, j):
            i = parent(i)
            j = parent(j)
            
            if i == j:
                return

            if rank[j] > rank[i]:
                i, j = j, i
            
            djs[j] = djs[i]
            rank[i] += rank[j]
        

        for edge1, edge2 in edges:
            union(edge1, edge2)

        for i in range(len(djs)):
            djs[i] = parent(djs[i])

        print(djs)
            
        set_djs = set(djs)

        return len(set_djs)