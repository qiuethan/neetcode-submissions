class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        psa = [0]

        for num in nums:
            psa.append(psa[-1] + num)

        max_sum = nums[0]

        for i in range(1, len(psa)):
            for j in range(i, len(psa)):
                max_sum = max(max_sum, psa[j] - psa[i-1])

        return max_sum