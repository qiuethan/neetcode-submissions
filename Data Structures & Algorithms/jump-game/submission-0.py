class Solution:
    def canJump(self, nums: List[int]) -> bool:
        smallestReachable = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= smallestReachable:
                smallestReachable = i
        
        if smallestReachable <= 0:
            return True
        
        return False
                