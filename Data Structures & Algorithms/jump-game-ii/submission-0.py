class Solution:
    def jump(self, nums: List[int]) -> int:
        to_end = [101]*len(nums)
        to_end[-1] = 0
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(nums[i] + 1):
                to_end[i] = min(to_end[min(i + j, len(nums)-1)] + 1, to_end[i])

        return to_end[0]
                