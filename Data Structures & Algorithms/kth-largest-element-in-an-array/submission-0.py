class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-1*num for num in nums]
        heapq.heapify(maxheap)

        for i in range(k - 1):
            heapq.heappop(maxheap)
        
        return maxheap[0] * -1

        