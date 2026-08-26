class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp = 0
        rp = 0
        subarray_sum = 0

        min_length = len(nums) + 1

        while rp < len(nums):
            subarray_sum += nums[rp]
            while subarray_sum >= target and lp <= rp:
                min_length = min(min_length, rp - lp + 1)
                subarray_sum -= nums[lp]
                lp += 1
            rp += 1

        if min_length == len(nums) + 1:
            return 0
        
        return min_length