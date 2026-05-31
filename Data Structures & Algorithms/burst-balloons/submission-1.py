class Solution:
        
    def maxCoins(self, nums: List[int]) -> int:

        memo = {}

        def calculateProduct(nums, i):
            
            if i == 0:
                left = 1
            else:
                left = nums[i - 1]
            
            if i == len(nums) - 1:
                right = 1
            else:
                right = nums[i + 1]
            
            return left * nums[i] * right

        def popBalloon(nums):

            maxScore = 0

            if hash(tuple(nums)) in memo:
                return memo[hash(tuple(nums))]
 
            for i in range(len(nums)):
                maxScore = max(calculateProduct(nums, i) + popBalloon(nums[0:i] + nums[i+1:]), maxScore)
            
            memo[hash(tuple(nums))] = maxScore

            return memo[hash(tuple(nums))]
        
        return popBalloon(nums)
