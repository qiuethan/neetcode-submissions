class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0

        for index, value in enumerate(nums):
            if nums[index] == val:
                val_count += 1
            else:
                nums[index - val_count] = nums[index]

        return len(nums) - val_count