class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        target = 0

        nums.sort()

        for i in range(len(nums) - 1):
            val = nums[i]
            left = i + 1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[right] == target - val:
                    if [val, nums[left], nums[right]] not in trips:
                        trips.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target-val:
                    left += 1
                else:
                    right -= 1
        
        return trips