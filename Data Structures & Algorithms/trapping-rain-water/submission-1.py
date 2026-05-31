class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0]

        for i in range(len(height)):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[len(height) - 1 - i]))
        
        water = 0

        for i in range(len(height)):
            if height[i] >= left[i] or height[i] >= right[len(height) - 1 - i]:
                continue
            
            water += min(left[i], right[len(height) - 1 - i]) - height[i]
        

        return water