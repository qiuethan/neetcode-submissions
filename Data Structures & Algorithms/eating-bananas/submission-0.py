import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left = 1
        right = piles[-1]

        min_k = piles[-1]

        def calculate_hours(k):
            return sum([math.ceil(pile/k) for pile in piles])

        while left <= right:
            mid = (left + right) // 2
            if calculate_hours(mid) <= h:
                min_k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_k
