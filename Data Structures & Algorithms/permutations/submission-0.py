class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def search(arr, remaining_nums):
            if len(remaining_nums) == 0:
                res.append(arr)
                return
            
            for index, value in enumerate(remaining_nums):
                search(arr + [value], remaining_nums[:index] + remaining_nums[index + 1:])

        search([], nums)

        return res