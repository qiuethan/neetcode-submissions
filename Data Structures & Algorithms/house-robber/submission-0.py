class Solution:
    def rob(self, nums: List[int]) -> int:

        max_value = [-1]*len(nums)

        def calculate_max(i, lst):
            if max_value[i] != -1:
                return max_value[i]
            elif len(lst) <= 0:
                max_value[i] = 0
            elif len(lst) == 1:
                max_value[i] = lst[0]
            elif len(lst) == 2:
                max_value[i] = max(calculate_max(i - 1, lst[:-1]), nums[i])
            else:
                max_value[i] = max(calculate_max(i - 1, lst[:-1]), calculate_max(i - 2, lst[:-2]) + nums[i])
            return max_value[i]

        return calculate_max(len(nums) - 1, nums)