class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        valid_sums = set()

        def twoSum(two_sum_target, lp, rp):
            valid_pairs = []

            while lp < rp:
                if nums[lp] + nums[rp] == two_sum_target:
                    valid_pairs.append((nums[lp], nums[rp]))
                    lp += 1
                    rp -= 1
                elif nums[lp] + nums[rp] > two_sum_target:
                    rp -= 1
                else:
                    lp += 1
            
            return valid_pairs
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                valid_pairs = twoSum(target - nums[i] - nums[j], i + 1, j - 1)
                for pair in valid_pairs:
                    valid_sums.add((nums[i], pair[0], pair[1], nums[j]))

        return list(valid_sums)