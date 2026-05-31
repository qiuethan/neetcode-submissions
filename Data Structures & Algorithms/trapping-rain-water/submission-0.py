class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_pos = []
        max_right_pos = []

        max_left = 0
        max_right = 0

        for i in range(len(height)):
            max_left_pos.append(max_left)
            max_left = max(max_left, height[i])
        
        for i in range(len(height)-1, -1, -1):
            max_right_pos.append(max_right)
            max_right = max(max_right, height[i])
        

        total = 0

        for i in range(len(height)):
            height_of_index = min(max_left_pos[i], max_right_pos[len(height) - i - 1])
            total += max(0, height_of_index - height[i])

        return total