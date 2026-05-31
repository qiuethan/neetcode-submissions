class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = set()

        longest = 0

        while right < len(s):
            print(chars, left, right)
            if s[right] not in chars:
                chars.add(s[right])
            else:
                longest = max(right - left, longest)
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        break
                    chars.remove(s[left])
                    left += 1
            right += 1
        
        longest = max(right - left, longest)

        return longest
