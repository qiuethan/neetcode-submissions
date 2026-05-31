class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        target_sum = nums_sum//2

        reachable = [False]*(target_sum + 1)
        reachable[0] = True

        reachable_lists = [[]] * (target_sum + 1)
        reachable_lists[0] = nums

        for i in range(target_sum):
            if reachable[i]:
                for index, value in enumerate(reachable_lists[i]):
                    if value + i <= target_sum:
                        reachable[value + i] = True
                        reachable_lists[value + i] = reachable_lists[i][:index] + reachable_lists[i][index+1:]

        return reachable[-1]
