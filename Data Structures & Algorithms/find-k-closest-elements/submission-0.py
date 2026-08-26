class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        closest_values = sorted([(abs(value - x), value) for value in arr])

        return sorted([value[1] for value in closest_values[:k]])