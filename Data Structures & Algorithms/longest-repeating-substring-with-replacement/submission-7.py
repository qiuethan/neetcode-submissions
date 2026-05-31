class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0]*26

        def add_count(char):
            char_count[ord(char) - ord("A")] += 1
        
        def sub_count(char):
            char_count[ord(char) - ord("A")] -= 1
        
        def count_extra():
            return sum(char_count) - max(char_count)
        
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            add_count(s[right])
            while count_extra() > k and left <= right:
                sub_count(s[left])
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length