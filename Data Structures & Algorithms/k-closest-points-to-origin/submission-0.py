import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [((point[0]**2 + point[1]**2), point) for point in points]
        heapq.heapify(distances)
        
        print(distances)

        k_min_distances = []

        for i in range(k):
            k_min_distances.append(heapq.heappop(distances)[1])

        return k_min_distances

