class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums.sort()

        def search(arr_sum, arr, nums_remaining):
            if arr_sum > target:
                return
            if arr_sum == target:
                res.append(arr)

            for index, value in enumerate(nums_remaining):
                search(arr_sum + value, arr + [value], nums_remaining[index:])

        search(0, [], nums)

        return res