from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        num_prereqs = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[dst].append(src)
            num_prereqs[src] += 1

        finished_q = deque()
        order = []

        for i in range(numCourses):
            if num_prereqs[i] == 0:
                finished_q.append(i)

        while finished_q:
            course = finished_q.popleft()
            order.append(course)
            for connection in adj[course]:
                num_prereqs[connection] -= 1
                if num_prereqs[connection] == 0:
                    finished_q.append(connection)
        
        if len(order) != numCourses:
            return []

        return order

        