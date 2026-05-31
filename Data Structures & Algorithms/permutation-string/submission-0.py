class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count_s1 = [0]*26
        count_s2 = [0]*26

        def add_count(lst, char):
            lst[ord(char) - ord('a')] += 1
        
        def sub_count(lst, char):
            lst[ord(char) - ord('a')] -= 1

        for i in range(len(s1)):
            add_count(count_s1, s1[i])
        
        left = 0
        right = 0

        while right < len(s2):
            add_count(count_s2, s2[right])
            if len(s1) == right - left + 1:
                if count_s1 == count_s2:
                    return True
                sub_count(count_s2, s2[left])
                left += 1

            right += 1
        
        return False