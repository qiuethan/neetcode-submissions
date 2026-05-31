class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWater = 0

        while left < right:
            maxWater = max(maxWater, min(heights[right], heights[left])*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater