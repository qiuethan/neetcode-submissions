class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        max_heap = []
        indexes = {}
        max_vals = []

        for i in range(k):
            heapq.heappush(max_heap, -1 * nums[i])
            indexes[nums[i]] = i
        
        max_vals.append(max_heap[0] * - 1)
        
        for i in range(0, len(nums) - k):
            heapq.heappush(max_heap, -1 * nums[i + k])
            indexes[nums[i + k]] = i + k
            while indexes[-1 * max_heap[0]] <= i:
                heapq.heappop(max_heap)
            max_vals.append(max_heap[0]  * -1)
        
        return max_vals