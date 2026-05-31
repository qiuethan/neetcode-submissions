class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increasing = [1]*len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    increasing[i] = max(increasing[i], increasing[j] + 1)
        
        return max(increasing)
