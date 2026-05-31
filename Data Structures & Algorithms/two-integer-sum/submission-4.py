class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for index, num in enumerate(nums):
            if num in indicies:
                if target/2 == num:
                    return [indicies[num], index]
            indicies[num] = index
        
        for index, num in enumerate(nums):
            if num*2 == target:
                continue
            if target-num in indicies:
                return [index, indicies[target-num]] 