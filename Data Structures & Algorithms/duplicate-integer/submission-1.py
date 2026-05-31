class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previous = set()

        for num in nums:
            if num in previous:
                return True
            previous.add(num)

        return False

        