class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker_set = set()

        lp = 0
        rp = 0

        while rp < len(nums):
            if rp - lp > k:
                tracker_set.remove(nums[lp])
                lp += 1
            if nums[rp] in tracker_set:
                return True
            tracker_set.add(nums[rp])
            rp += 1
        
        return False
