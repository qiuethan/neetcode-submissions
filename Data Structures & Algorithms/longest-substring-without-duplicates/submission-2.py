class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0

        if len(s) == 0:
            return 0

        max_length = 1

        while rp < len(s):
            if rp - lp == 0:
                rp += 1
                continue
            if s[rp] in s[lp:rp]:
                lp += 1
            else:
                max_length = max(max_length, rp - lp + 1)
                rp += 1
        
        return max_length
