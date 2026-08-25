class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        
        max_val = 0
        max_val_occurences = 0

        for val in tracker:
            if tracker[val] > max_val_occurences:
                max_val = val
                max_val_occurences = tracker[val]
        
        return max_val