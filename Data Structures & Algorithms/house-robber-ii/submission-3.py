class Solution:
    def rob(self, nums: List[int]) -> int:
        max_houses_start_1 = [-1] * (len(nums))
        max_houses_start_2 = [-1] * (len(nums))

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        def calculate_max(i, remaining, memo_arr):
            if len(remaining) == 0:
                return 0
            if memo_arr[i] != -1:
                return memo_arr[i]
            if len(remaining) == 1:
                memo_arr[i] = remaining[0]
                return memo_arr[i]
            if len(remaining) == 2:
                memo_arr[i] = max(remaining[0], remaining[1])
                return memo_arr[i]
            memo_arr[i] = max(nums[i] + calculate_max(i + 2, remaining[2:], memo_arr), calculate_max(i + 1, remaining[1:], memo_arr))
            return memo_arr[i]

        calculate_max(0, nums[:-1], max_houses_start_1)
        calculate_max(1, nums[1:], max_houses_start_2)

        print(max_houses_start_1, max_houses_start_2)
        max_value = max(max_houses_start_1[0], max_houses_start_2[1])

        return max(0, max_value)