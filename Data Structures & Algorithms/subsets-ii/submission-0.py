class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()

        def search(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            search(i + 1, subset)
            subset.pop()
            search(i + 1, subset)

        nums.sort()
        search(0, [])

        return [list(s) for s in res]