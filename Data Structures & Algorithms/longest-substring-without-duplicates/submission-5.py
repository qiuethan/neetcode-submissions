class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0

        max_length = 0
        
        tracker = set()

        while rp < len(s):
            if s[rp] in tracker:
                tracker.remove(s[lp])
                lp += 1
            else:
                tracker.add(s[rp])
                max_length = max(max_length, rp - lp + 1)
                rp += 1
        
        return max_length
