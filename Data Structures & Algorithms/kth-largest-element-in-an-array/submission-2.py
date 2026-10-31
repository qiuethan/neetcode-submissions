import heapq

# nlogn where n = len(nums)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            # not full yet
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
                continue
            
            # full
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        
        return heapq.heappop(min_heap)