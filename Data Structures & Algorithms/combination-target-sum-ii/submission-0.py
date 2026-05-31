class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums.sort()

        def search(arr_sum, arr, nums_remaining):
            if arr_sum > target:
                return
            if arr_sum == target:
                if arr not in res:
                    res.append(arr)

            for index, value in enumerate(nums_remaining):
                search(arr_sum + value, arr + [value], nums_remaining[index + 1:])

        search(0, [], nums)

        return res