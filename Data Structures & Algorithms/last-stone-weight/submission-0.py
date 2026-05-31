class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-1*stone for stone in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            first_stone = heapq.heappop(maxheap) * -1
            second_stone = heapq.heappop(maxheap) * -1

            if first_stone != second_stone:
                remaining = max(first_stone, second_stone) - min(first_stone, second_stone)
                heapq.heappush(maxheap, remaining * -1)
        
        if len(maxheap) == 0:
            return 0
        else:
            return maxheap[0] * -1