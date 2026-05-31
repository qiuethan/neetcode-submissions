class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
        
        arrayKeys = list(frequency.keys())
        arrayKeys.sort(key=lambda x: frequency[x])

        return arrayKeys[-1*k:][::-1]