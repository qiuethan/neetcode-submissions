class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        posmemo = [[-1] * (sum(nums) + 1) for i in range(len(nums))]
        negmemo = [[-1] * (sum(nums) + 1) for i in range(len(nums))]

        def countWays(numsIndex, currentSum):

            if numsIndex == len(nums) and currentSum == target:
                return 1
            
            if numsIndex == len(nums) and currentSum != target:
                return 0

            if numsIndex > len(nums):
                return 0

            if currentSum >= 0:
                if posmemo[numsIndex][currentSum] != -1:
                    return posmemo[numsIndex][currentSum]
            else:
                if negmemo[numsIndex][currentSum * -1] != -1:
                    return negmemo[numsIndex][currentSum * -1]
            
            if currentSum >= 0:
                posmemo[numsIndex][currentSum] = 0
                posmemo[numsIndex][currentSum] += countWays(numsIndex + 1, currentSum - nums[numsIndex])
                posmemo[numsIndex][currentSum] += countWays(numsIndex + 1, currentSum + nums[numsIndex])

                return posmemo[numsIndex][currentSum]
            
            else:
                negmemo[numsIndex][currentSum * -1] = 0
                negmemo[numsIndex][currentSum * -1] += countWays(numsIndex + 1, currentSum - nums[numsIndex])
                negmemo[numsIndex][currentSum * -1] += countWays(numsIndex + 1, currentSum + nums[numsIndex])

                return negmemo[numsIndex][currentSum * -1]
        
        return countWays(0,0)



